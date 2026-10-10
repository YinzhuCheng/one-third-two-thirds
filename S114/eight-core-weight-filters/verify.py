#!/usr/bin/env python3
"""Standard-library exact verification; no optimization library or imported catalogue code."""
from pathlib import Path
import itertools,json
HERE=Path(__file__).parent

def core_relation(q):
 n=len(q['strict_up_masks'])
 return {(i,j) for i in range(n) for j in range(n) if q['strict_up_masks'][i]>>j&1}

def endpoint_graph(n,R):
 U=[{b for a,b in R if a==i} for i in range(n)]
 D=[{a for a,b in R if b==i} for i in range(n)]
 def chain(S):return all((i,j) in R or (j,i) in R for i,j in itertools.combinations(S,2))
 E={(2*i,2*i+1) for i in range(n)}|{(2*i+a,2*j+b) for i,j in R for a in (0,1) for b in (0,1)}
 for i in range(n):
  for j in range(n):
   if i==j or (i,j) in R or (j,i) in R:continue
   if D[i]<=D[j] and chain(U[j]-U[i]):E.add((2*i,2*j))
   if U[j]<=U[i] and chain(D[i]-D[j]):E.add((2*i+1,2*j+1))
 return U,D,E

def iscyclic(V,E):
 done=set()
 while len(done)<len(V):
  nxt={v for v in V-done if not any(b==v and a not in done for a,b in E)}
  if not nxt:return True
  done|=nxt
 return False

def contract(n,E,S):
 def f(v):return v-1 if v%2 and v//2 in S else v
 V={f(v) for v in range(2*n)};F={(f(a),f(b)) for a,b in E if f(a)!=f(b)}
 return V,F

def main():
 original=json.loads((HERE/'input_cores.json').read_text())
 result=json.loads((HERE/'weight_filter_catalogue.json').read_text())
 assert len(original)==len(result['cores'])==17
 counts={'cores':0,'distinct_linear_inequalities':0,'bottom_witnesses':0,'top_witnesses':0,'singleton_port_patterns':0,'linear_sections':0,'farkas_certificates':0,'integer_feasible_witnesses':0}
 for inp,q in zip(original,result['cores']):
  n=8;R=core_relation(inp);U,D,E=endpoint_graph(n,R)
  assert q['class_id']==inp['class_id'] and q['strict_up_masks']==inp['strict_up_masks']
  def chain(S):return all((i,j) in R or (j,i) in R for i,j in itertools.combinations(S,2))
  expected=[]
  for i in range(n):
   inc={j for j in range(n) if j!=i and (i,j) not in R and (j,i) not in R}
   B=sorted(j for j in inc if D[i]==D[j] and chain(U[i]-U[j]))
   T=sorted(j for j in inc if U[i]==U[j] and chain(D[i]-D[j]))
   if B or T:
    expected.append({'target':i,'incomparable_indices':sorted(inc),'bottom_witnesses':B,'top_witnesses':T,'coefficients':[2 if k==i else -1 if k in inc else 0 for k in range(n)],'integer_rhs':-1})
  assert q['rules']==expected
  counts['distinct_linear_inequalities']+=len(expected)
  counts['bottom_witnesses']+=sum(len(r['bottom_witnesses']) for r in expected)
  counts['top_witnesses']+=sum(len(r['top_witnesses']) for r in expected)
  mandatory=set(q['port_forced_nonsingleton_indices'])
  assert [s['singleton_vertices'] for s in q['port_certificates']]==[[i] for i in sorted(mandatory)]
  for mask in range(1<<n):
   S={i for i in range(n) if mask>>i&1};V,F=contract(n,E,S)
   assert iscyclic(V,F)==bool(S&mandatory),(q['class_id'],S)
   counts['singleton_port_patterns']+=1
  for port in q['port_certificates']:
   V,F=contract(n,E,set(port['singleton_vertices']));cy=port['cycle_representative_ports']
   assert cy[0]==cy[-1] and all((a,b) in F for a,b in zip(cy,cy[1:]))
  rows=[r['coefficients'] for r in expected]
  assert all(sum(a*b for a,b in zip(row,q['global_integer_witness']))<=-1 for row in rows)
  sections=q['all_sections']; avail=set(range(n))-mandatory
  assert len(sections)==1<<len(avail)
  assert {tuple(s['singleton_indices']) for s in sections}=={tuple(sorted(i for i in avail if mask>>i&1)) for mask in range(1<<n)}
  bad=[];good=[]
  for sec in sections:
   S=set(sec['singleton_indices']);base=sec['lower_weights'];free=sec['free_indices']
   assert base==[2 if i in mandatory else 1 for i in range(n)]
   assert free==[i for i in range(n) if i not in S]
   if sec['status']=='feasible_integer_witness':
    w=sec['weights'];assert len(w)==n and all(isinstance(v,int) for v in w)
    assert all(w[i]>=base[i] for i in range(n)) and all(w[i]==1 for i in S)
    assert all(sum(a*b for a,b in zip(row,w))<=-1 for row in rows)
    counts['integer_feasible_witnesses']+=1;good.append(sec)
   else:
    assert sec['status']=='infeasible_real_relaxation'
    c=sec['certificate'];y=c['row_multipliers']
    assert len(y)==len(rows) and all(isinstance(v,int) and v>=0 for v in y)
    b=[-1-sum(a*w for a,w in zip(row,base)) for row in rows]
    combo=[sum(y[r]*rows[r][i] for r in range(len(rows))) for i in free]
    rhs=sum(a*b for a,b in zip(y,b))
    assert min(combo,default=0)>=0 and rhs<0
    assert c['combined_free_coefficients']==combo and c['combined_rhs']==rhs
    counts['farkas_certificates']+=1;bad.append(sec)
   counts['linear_sections']+=1
  assert q['minimal_additional_forbidden_singleton_sets']==[s for s in bad if not any(set(t['singleton_indices'])<set(s['singleton_indices']) for t in bad)]
  assert q['maximal_feasible_singleton_sets']==[s for s in good if not any(set(s['singleton_indices'])<set(t['singleton_indices']) for t in good)]
  counts['cores']+=1
 out={'status':'PASS','method':'Independent set-based derivation and exact integer certificate verification, standard library only','counts':counts}
 (HERE/'certificate_verification.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
