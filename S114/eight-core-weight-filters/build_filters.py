#!/usr/bin/env python3
"""Discover portable exact certificates. SciPy is discovery only; verify.py is stdlib."""
from pathlib import Path
import json,itertools,math
from fractions import Fraction
import numpy as np
from scipy.optimize import linprog,milp,Bounds,LinearConstraint
HERE=Path(__file__).parent
SOURCE=HERE/'input_cores.json'  # portable frozen eight-core snapshot

def bits(m):return [i for i in range(m.bit_length()) if m>>i&1]
def derive(q):
 u=q['strict_up_masks'];n=len(u);d=[sum(1<<i for i in range(n) if u[i]>>j&1) for j in range(n)]
 def chain(m):return all(u[i]>>j&1 or u[j]>>i&1 for i,j in itertools.combinations(bits(m),2))
 rules=[]
 for i in range(n):
  inc=[j for j in range(n) if j!=i and not ((u[i]|d[i])>>j&1)]
  B=[j for j in inc if d[i]==d[j] and chain(u[i]&~u[j])]
  T=[j for j in inc if u[i]==u[j] and chain(d[i]&~d[j])]
  if B or T:rules.append({'target':i,'incomparable_indices':inc,'bottom_witnesses':B,'top_witnesses':T,'coefficients':[2 if k==i else -1 if k in inc else 0 for k in range(n)],'integer_rhs':-1})
 return rules

def lcm(a,b):return abs(a*b)//math.gcd(a,b)
def certificate(A,b,free):
 # y >= 0, A^T y >= 0, b*y = -1; x = w-lower >= 0.
 r=len(b)
 res=linprog(np.ones(r),A_ub=-np.array(A).T if free else None,b_ub=np.zeros(len(free)) if free else None,A_eq=[b],b_eq=[-1],bounds=[(0,None)]*r,method='highs')
 assert res.success,res
 yy=[Fraction(float(x)).limit_denominator(10000) for x in res.x]
 den=math.lcm(*(x.denominator for x in yy));y=[int(x*den) for x in yy];g=math.gcd(*y);y=[x//g for x in y]
 assert min(y)>=0 and sum(bb*yy for bb,yy in zip(b,y))<0
 assert all(sum(y[r]*A[r][k] for r in range(len(y)))>=0 for k in range(len(free)))
 return {'row_multipliers':y,'combined_free_coefficients':[sum(y[r]*A[r][k] for r in range(len(y))) for k in range(len(free))],'combined_rhs':sum(bb*yy for bb,yy in zip(b,y))}

def main():
 original=[q for q in json.loads(SOURCE.read_text()) if q['n']==8]
 (HERE/'input_cores.json').write_text(json.dumps(original,indent=2)+'\n')
 out=[]
 for q in original:
  n=8;rules=derive(q);rows=[r['coefficients'] for r in rules]
  mandatory=sorted(s['singleton_vertices'][0] for s in q['minimal_forbidden_singleton_subsets'])
  assert all(len(s['singleton_vertices'])==1 for s in q['minimal_forbidden_singleton_subsets'])
  base=[2 if i in mandatory else 1 for i in range(n)]
  sections=[];bad=[];good=[]
  avail=[i for i in range(n) if i not in mandatory]
  for k in range(len(avail)+1):
   for singleton in itertools.combinations(avail,k):
    free=[i for i in range(n) if i not in singleton]
    b=[-1-sum(a*w for a,w in zip(row,base)) for row in rows]
    A=[[row[i] for i in free] for row in rows]
    sec={'singleton_indices':list(singleton),'lower_weights':base,'free_indices':free}
    if not free:
     ok=all(v>=0 for v in b)
    else:
     res=linprog(np.ones(len(free)),A_ub=A,b_ub=b,bounds=[(0,None)]*len(free),method='highs');ok=res.success
    if ok:
     if free:
      M=milp(np.ones(len(free)),integrality=np.ones(len(free)),bounds=Bounds(np.zeros(len(free)),np.inf),constraints=LinearConstraint(np.array(A),-np.inf,np.array(b)))
      assert M.success,('rational feasible but integral unavailable',q['class_id'],singleton,M)
      w=base.copy()
      for i,v in zip(free,M.x):w[i]+=round(v)
     else:w=base.copy()
     assert all(sum(a*z for a,z in zip(row,w))<=-1 for row in rows)
     assert all(w[i]==1 for i in singleton)
     sec.update(status='feasible_integer_witness',weights=w);good.append(sec)
    else:
     sec.update(status='infeasible_real_relaxation',certificate=certificate(A,b,free));bad.append(sec)
    sections.append(sec)
  minimal_bad=[s for s in bad if not any(set(t['singleton_indices'])<set(s['singleton_indices']) for t in bad)]
  maximal_good=[s for s in good if not any(set(s['singleton_indices'])<set(t['singleton_indices']) for t in good)]
  qout={'class_id':q['class_id'],'strict_up_masks':q['strict_up_masks'],'cover_edges':q['cover_edges'],'rules':rules,'port_forced_nonsingleton_indices':mandatory,'port_certificates':q['minimal_forbidden_singleton_subsets'],'minimal_additional_forbidden_singleton_sets':minimal_bad,'maximal_feasible_singleton_sets':maximal_good,'section_count':len(sections),'infeasible_sections':len(bad),'feasible_sections':len(good),'global_integer_witness':[2]*8,'all_sections':sections}
  assert all(sum(a*2 for a in row)<=-1 for row in rows)
  out.append(qout)
  print(q['class_id'],'targets',[r['target'] for r in rules],'port',mandatory,'extra',[s['singleton_indices'] for s in minimal_bad],'maxsing',max(len(s['singleton_indices']) for s in good),flush=True)
 (HERE/'weight_filter_catalogue.json').write_text(json.dumps({'schema':1,'scope':'17 frozen 8-point classes C02-C18, positive integer chain weights','cores':out},indent=2)+'\n')
if __name__=='__main__':main()
