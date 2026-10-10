#!/usr/bin/env python3
"""Independent fail-closed audit. Standard library only; imports no author code."""
from pathlib import Path
from fractions import Fraction as Q
from itertools import combinations, permutations, product
from collections import Counter
from functools import lru_cache
import json, copy, hashlib, sys
ROOT=Path(__file__).resolve().parent
class Invalid(ValueError): pass
def need(ok,msg):
 if not ok: raise Invalid(msg)
def rat(x):
 need(type(x) in (str,int),'rational encoding')
 try: return Q(x)
 except (ValueError,ZeroDivisionError): raise Invalid('invalid rational')
def members(mask,n): return [v for v in range(n) if mask>>v&1]
def from_edges(n,edges):
 need(type(n) is int and n>0,'order size'); u=[set() for _ in range(n)]
 for e in edges:
  need(type(e) is list and len(e)==2 and all(type(x) is int and 0<=x<n for x in e),'edge schema')
  a,b=e;need(a!=b,'loop');u[a].add(b)
 for k in range(n):
  for i in range(n):
   if k in u[i]:u[i]|=u[k]
 need(all(i not in u[i] for i in range(n)),'cyclic order')
 d=[{j for j in range(n) if i in u[j]} for i in range(n)]
 covers=[[i,j] for i in range(n) for j in sorted(u[i]) if not(u[i]&d[j])]
 return d,u,covers
def from_pred(pred):
 n=len(pred);need(all(type(x) is int and 0<=x<1<<n for x in pred),'predecessor encoding')
 d,u,c=from_edges(n,[[a,b] for b,m in enumerate(pred) for a in members(m,n)])
 need(pred==[sum(1<<a for a in s) for s in d],'predecessors must already be transitive')
 return d,u,c
def mask(s):return sum(1<<x for x in s)
def extensions(d,subset=None):
 vertices=set(range(len(d))) if subset is None else set(subset)
 def rec(done,out):
  if done==vertices:yield tuple(out);return
  for v in sorted(vertices-done):
   if d[v]&vertices<=done:yield from rec(done|{v},out+[v])
 yield from rec(set(),[])
def brute_extensions(d,subset):
 verts=sorted(subset)
 for order in permutations(verts):
  rank={v:k for k,v in enumerate(order)}
  if all(rank[a]<rank[b] for b in verts for a in d[b]&subset):yield order
def ischain(s,u):return all(b in u[a] or a in u[b] for a,b in combinations(s,2))
def incompar(a,b,u):return a!=b and b not in u[a] and a not in u[b]
def graph(d,u):
 n=len(d);g=[set(x) for x in u];low=[];high=[]
 for a in range(n):
  for b in range(n):
   if not incompar(a,b,u):continue
   if d[a]<=d[b] and ischain(u[b]-u[a],u):g[a].add(b);low.append([a,b])
   if u[b]<=u[a] and ischain(d[a]-d[b],u):g[a].add(b);high.append([a,b])
 return g,low,high
def topo(g):
 left=set(range(len(g)));out=[]
 while left:
  sources=[v for v in sorted(left) if not any(v in g[w] for w in left)]
  if not sources:return None
  out+=sources;left-=set(sources)
 return out
def cycle_valid(c,g):
 return type(c) is list and len(c)>2 and c[0]==c[-1] and all(type(x) is int and 0<=x<len(g) for x in c) and all(b in g[a] for a,b in zip(c,c[1:]))
def vgp(d,u):
 lo=[];hi=[]
 for a,b in combinations(range(len(d)),2):
  if d[a]==d[b] and ischain(u[a]-u[b],u) and ischain(u[b]-u[a],u):lo.append([a,b])
  if u[a]==u[b] and ischain(d[a]-d[b],u) and ischain(d[b]-d[a],u):hi.append([a,b])
 return [lo,hi]
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def hrows(F,A,pat):
 need(type(pat) is str and len(pat)==len(A) and set(pat)<=set('LH'),'orientation schema')
 return [[Q(1,3)-Q(a,f) if x=='L' else Q(a,f)-Q(2,3) for a,f in zip(row,F)] for row,x in zip(A,pat)]
def fresh_cell(F,A,pat):
 # Only one selected row, or the two-row/two-state adaptive case occur here.
 h=hrows(F,A,pat);m=len(F);k=len(A)
 vertices=[[Q(int(i==j)) for j in range(m)] for i in range(m)]
 if k==2:
  need(m==2,'independent solver bounded dimension')
  diff=[h[0][j]-h[1][j] for j in range(m)]
  if diff[0]!=diff[1]:
   t=-diff[1]/(diff[0]-diff[1])
   if 0<=t<=1:vertices.append([t,1-t])
 else:need(k==1,'selected menu size')
 opt,mu=max((min(dot(row,v) for row in h),v) for v in vertices)
 if k==1:lam=[Q(1)]
 else:
  weights=[Q(0),Q(1)];a=h[0][0]-h[1][0];b=h[0][1]-h[1][1]
  if a!=b:
   t=(h[1][1]-h[1][0])/(a-b)
   if 0<=t<=1:weights.append(t)
  dual,t=min((max(t*h[0][j]+(1-t)*h[1][j] for j in range(m)),t) for t in weights)
  need(dual==opt,'independent primal-dual solve mismatch');lam=[t,1-t]
 eta=[opt-sum(lam[i]*h[i][j] for i in range(k)) for j in range(m)]
 c=dict(pattern=pat,optimum=str(opt),mu=list(map(str,mu)),lambda_pairs=list(map(str,lam)),eta=list(map(str,eta)),nu=str(opt))
 check_cell(F,A,c);return c

def check_cell(F,A,c,require_optimal=True):
 need(type(F) is list and F and all(type(f) is int and f>0 for f in F),'F positivity')
 need(type(A) is list and A and all(type(r) is list and len(r)==len(F) for r in A),'A dimensions')
 need(all(type(a) is int and 0<=a<=f for r in A for a,f in zip(r,F)),'A entries')
 need(type(c) is dict and all(k in c for k in ('pattern','lambda_pairs','eta','nu')),'cell keys')
 h=hrows(F,A,c['pattern']);nu=rat(c['nu']);lam=list(map(rat,c['lambda_pairs']));eta=list(map(rat,c['eta']))
 need(len(lam)==len(A) and len(eta)==len(F),'dual dimensions')
 need(all(x>=0 for x in lam+eta) and sum(lam)==1,'dual signs normalization')
 need(all(sum(lam[i]*h[i][j] for i in range(len(A)))+eta[j]==nu for j in range(len(F))),'dual equality')
 need(nu<=0,'strict bad cell not ruled out')
 if require_optimal:
  need('mu' in c and 'optimum' in c,'primal keys');mu=list(map(rat,c['mu']));op=rat(c['optimum'])
  need(len(mu)==len(F) and all(x>=0 for x in mu) and sum(mu)==1,'primal simplex')
  need(all(dot(row,mu)>=op for row in h),'primal inequalities');need(op==nu,'duality gap')
 return True

def profile_check(r,cat):
 need(type(r) is dict and type(r.get('class_index')) is int and r.get('direction') in ('primal','dual'),'profile identification')
 ci=r['class_index'];need(0<=ci<len(cat),'catalogue index');p=r['profile'];n=p['n']
 d,u,covers=from_edges(n,p['covers_edges'])
 need(covers==p['covers_edges'],'edges are exactly Hasse edges')
 rep=cat[ci]['representative_masks'];repd,repu,_=from_edges(len(rep),[[a,b] for a,m in enumerate(rep) for b in members(m,len(rep))])
 expected=repu if r['direction']=='primal' else repd
 need(u==expected,'catalogue class/direction mismatch')
 need([mask(s) for s in d]==p['pred'],'pred disagreement');need([mask(s) for s in u]==r['strict_up_masks'],'up disagreement')
 maxima=[v for v in range(n) if not u[v]];ideals=[((1<<n)-1)^(1<<v) for v in maxima]
 all_ideals=[sum(1<<x for x in s) for s in combinations(range(n),n-1) if all(d[v]<=set(s) for v in s)]
 need(sorted(ideals)==sorted(all_ideals),'cut ideal completeness')
 need(p['r']==n-1 and p['maxima']==maxima and p['ideals']==ideals,'cut data disagreement')
 common=set(range(n))-set(maxima);pairs=[list(z) for z in combinations(sorted(common),2) if incompar(*z,u)]
 need(pairs==p['pairs'],'complete fully observed pair menu')
 F=[];A=[[] for _ in pairs]
 for omitted in maxima:
  orders=list(brute_extensions(d,set(range(n))-{omitted}));F.append(len(orders))
  for i,(a,b) in enumerate(pairs):A[i].append(sum(o.index(a)<o.index(b) for o in orders))
 need(F==p['F'] and A==p['A'],'independent permutation F/A mismatch')
 core_orders=list(brute_extensions(d,set(range(n))));need(len(core_orders)==sum(F),'core count identity')
 fixed=[i for i,row in enumerate(A) if all(f<=3*a<=2*f for a,f in zip(row,F))]
 need(fixed==r['fixed_pairs'],'fixed menu mismatch');selected=r['selected']
 need(type(selected) is list and selected and len(set(selected))==len(selected) and all(type(i) is int and 0<=i<len(A) for i in selected),'selected indices')
 pats=[''.join(x) for x in product('LH',repeat=len(selected))]
 need(len(r['cells'])==len(pats) and sorted(c['pattern'] for c in r['cells'])==sorted(pats),'selected orientations incomplete or duplicated')
 selectedA=[A[i] for i in selected];fresh={}
 for c in r['cells']:
  check_cell(F,selectedA,c);fc=fresh_cell(F,selectedA,c['pattern']);need(rat(fc['optimum'])==rat(c['optimum']),'independent optimum mismatch');fresh[c['pattern']]=fc
 expanded=[]
 for pat in map(''.join,product('LH',repeat=len(A))):
  small=''.join(pat[i] for i in selected);c=fresh[small];lam=['0']*len(A)
  for i,l in zip(selected,c['lambda_pairs']):lam[i]=l
  cert=dict(pattern=pat,lambda_pairs=lam,eta=c['eta'],nu=c['nu'])
  check_cell(F,A,cert,False);expanded.append(cert)
 g,low,hi=graph(d,u);t=topo(g)
 need((r['core_cycle'] is None)==(t is not None),'core acyclicity disagreement')
 if r['core_cycle'] is not None:need(cycle_valid(r['core_cycle'],g),'claimed core cycle invalid')
 need(vgp(d,u)==[r['core_vgp_bottom'],r['core_vgp_top']],'VGP disagreement')
 need(vgp(d,u)==[[],[]],'survivor VGP failure');need(r['covered'] is True and p['covers'] is True,'covered flag')
 return dict(id=r['id'],n=n,F=F,A=A,pairs=pairs,selected=selected,fixed_pairs=fixed,core_extensions=len(core_orders),selected_certificates=list(fresh.values()),full_menu_certificates=expanded,core_forced_topological_order=t)

def connected(g):
 if not g:return False
 seen={0};stack=[0]
 while stack:
  v=stack.pop()
  for w in g[v]-seen:seen.add(w);stack.append(w)
 return len(seen)==len(g)
def module_closure(a,b,d,u):
 n=len(d);s={a,b}
 while True:
  add=set()
  for v in set(range(n))-s:
   kinds={(1 if x in u[v] else -1 if x in d[v] else 0) for x in s}
   if len(kinds)>1:add.add(v)
  if not add:return s
  s|=add

def automorphisms(d,u):
 n=len(d);color=[(len(d[i]),len(u[i])) for i in range(n)]
 while True:
  keys=[(color[i],tuple(sorted(color[x] for x in d[i])),tuple(sorted(color[x] for x in u[i]))) for i in range(n)]
  unique={x:k for k,x in enumerate(sorted(set(keys)))};nxt=[unique[x] for x in keys]
  if len(set(nxt))==len(set(color)):color=nxt;break
  color=nxt
 cand={v:[w for w in range(n) if color[v]==color[w]] for v in range(n)}
 order=sorted(range(n),key=lambda v:(len(cand[v]),v));count=0;nonidentity=None
 def rec(k,m,used):
  nonlocal count,nonidentity
  if k==n:
   count+=1
   if any(m[v]!=v for v in range(n)):nonidentity=[m[v] for v in range(n)]
   return
  a=order[k]
  for b in cand[a]:
   if b in used:continue
   if any((x in u[a])!=(y in u[b]) or (x in d[a])!=(y in d[b]) for x,y in m.items()):continue
   rec(k+1,{**m,a:b},used|{b})
 rec(0,{},set());return count,nonidentity

def structure(d,u):
 n=len(d);comp=[d[i]|u[i] for i in range(n)];inc=[set(range(n))-{i}-comp[i] for i in range(n)]
 nonchain=[];chainmodules=set()
 for a,b in combinations(range(n),2):
  s=module_closure(a,b,d,u)
  if len(s)<n:
   if not ischain(s,u):nonchain.append(sorted(s))
   else:chainmodules.add(tuple(sorted(s)))
 # Width via Dilworth: independent bipartite augmenting-path matching.
 match={}
 def augment(a,seen):
  for b in sorted(u[a]):
   if b in seen:continue
   seen.add(b)
   if b not in match or augment(match[b],seen):match[b]=a;return True
  return False
 matching=sum(augment(a,set()) for a in range(n));width=n-matching
 @lru_cache(None)
 def ht(v):return 1+max([ht(x) for x in d[v]] or [0])
 ac,nonauto=automorphisms(d,u)
 cc=connected(comp);ic=connected(inc);pi=max(map(len,inc));height=max(ht(v) for v in range(n));fg=graph(d,u)[0]
 covers=[[a,b] for a in range(n) for b in u[a] if not(u[a]&d[b])]
 parent=list(range(n))
 def find(a):
  while parent[a]!=a:a=parent[a]
  return a
 forest=True
 for a,b in covers:
  x,y=find(a),find(b)
  if x==y:forest=False
  else:parent[x]=y
 return dict(comparability_connected=cc,incomparability_connected=ic,proper_nonchain_module_witnesses=sorted({tuple(x) for x in nonchain}),proper_chain_modules=sorted(chainmodules),automorphism_count=ac,nonidentity_automorphism=nonauto,width=width,height=height,maximum_incomparability_degree=pi,minima=[v for v in range(n) if not d[v]],maxima=[v for v in range(n) if not u[v]],cover_graph_forest=forest,full_forced_topological_order=topo(fg),very_good_pairs=vgp(d,u),passes_requested_structural_funnel=cc and ic and not nonchain and ac==1 and width>=3 and height>=3 and pi>=7 and topo(fg) is not None)

def completion_check(r,w):
 p=r['profile'];n=p['n'];pred=w['pred'];N=len(pred);d,u,_=from_pred(pred)
 need(N>n,'nonempty tail');need(pred[:n]==p['pred'],'core initial and induced order')
 need(all(len(d[z])>=n-1 for z in range(n,N)),'full predecessor guard fails')
 orders=list(extensions(d));need(orders,'empty extension set')
 support=Counter(mask(o[:n-1]) for o in orders);need(sorted(support)==sorted(p['ideals']),'actual cut support')
 B=[]
 for I in p['ideals']:B.append(sum(1 for _ in extensions(d,set(range(N))-set(members(I,N)))))
 need(B==w['B'],'B recomputation mismatch')
 need(all(support[I]==f*b for I,f,b in zip(p['ideals'],p['F'],B)),'cut F*B law')
 denom=len(orders);need(denom==dot(p['F'],B),'total F*B law')
 numerators=[sum(o.index(a)<o.index(b) for o in orders) for a,b in p['pairs']]
 need(numerators==[dot(row,B) for row in p['A']],'pair A*B law')
 probs=[Q(a,denom) for a in numerators]
 need(any(Q(1,3)<=probs[i]<=Q(2,3) for i in r['selected']),'no selected balanced pair in actual completion')
 if 'pair_probabilities' in w:need(probs==list(map(rat,w['pair_probabilities'])),'full pair probabilities mismatch')
 fg=graph(d,u)[0];vg=vgp(d,u)
 if 'forced_graph' in w:need(w['forced_graph']==[mask(x) for x in fg],'actual full graph edges mismatch')
 if 'very_good_pairs' in w:need(w['very_good_pairs']==vg,'actual VGP mismatch')
 if 'vgp' in w:need(w['vgp']==vg,'witness VGP mismatch')
 if 'cycle' in w:
  need((w['cycle'] is None)==(topo(fg) is not None),'witness cyclicity mismatch')
  if w['cycle'] is not None:need(cycle_valid(w['cycle'],fg),'witness cycle invalid')
 if 'pair' in w:
  i=p['pairs'].index(w['pair']);need(probs[i]==rat(w['probability']),'fixed failure probability')
  need(not Q(1,3)<=probs[i]<=Q(2,3),'fixed failure not outside closed interval')
 return dict(profile_id=r['id'],vertices=N,pred=pred,extensions=denom,F=p['F'],B=B,pair_numerators=numerators,pair_probabilities=list(map(str,probs)),support_counts={str(k):v for k,v in sorted(support.items())},structural=structure(d,u))

def mutate_tests(rows,cat):
 base=rows[0];tests=[]
 def bad(name,fn):
  r=copy.deepcopy(base);fn(r)
  try:profile_check(r,cat)
  except (Invalid,KeyError,TypeError,IndexError):tests.append(name);return
  raise Invalid('accepted mutated certificate: '+name)
 bad('F corrupted',lambda r:r['profile']['F'].__setitem__(0,r['profile']['F'][0]+1))
 bad('A corrupted',lambda r:r['profile']['A'][0].__setitem__(0,r['profile']['A'][0][0]+1))
 bad('pair menu incomplete',lambda r:r['profile']['pairs'].pop())
 bad('cut state omitted',lambda r:r['profile']['ideals'].pop())
 bad('orientation cell omitted',lambda r:r['cells'].pop())
 bad('orientation duplicated',lambda r:r['cells'].__setitem__(1,copy.deepcopy(r['cells'][0])))
 bad('lambda negative',lambda r:r['cells'][0]['lambda_pairs'].__setitem__(0,'-1'))
 bad('lambda dimensions',lambda r:r['cells'][0]['lambda_pairs'].append('0'))
 bad('eta corrupted',lambda r:r['cells'][0]['eta'].__setitem__(0,'1'))
 bad('nu positive',lambda r:r['cells'][0].__setitem__('nu','1'))
 bad('float rational forbidden',lambda r:r['cells'][0].__setitem__('nu',-0.5))
 bad('primal infeasible',lambda r:r['cells'][0]['mu'].__setitem__(0,'2'))
 bad('catalogue direction swapped',lambda r:r.__setitem__('direction','dual'))
 return tests

def main():
 src=ROOT/'author_snapshot';rows=json.loads((src/'initial_profiles.json').read_text());cat=json.loads((ROOT/'catalogue_snapshot/orbit_and_singleton_audit.json').read_text())['classes']
 need(len(rows)==36 and len(cat)==18,'scope cardinality');need({(r['class_index'],r['direction']) for r in rows}==set(product(range(18),('primal','dual'))),'scope exact coverage');need(len({r['id'] for r in rows})==36,'IDs unique')
 checked=[]
 for r in rows:
  a=profile_check(r,cat);checked.append(a);print('PROFILE PASS',r['id'],'full masks',len(a['full_menu_certificates']),flush=True)
 byid={r['id']:r for r in rows};comp=json.loads((src/'completion_checks.json').read_text());need({r['id'] for r in comp}==set(byid) and len(comp)==36,'completion scope');comps=[];persistent=[];bounded_absent=[]
 for cr in comp:
  r=byid[cr['id']];p=r['profile'];d,u,_=from_pred(p['pred']);g=graph(d,u)[0];nonmax=set(range(p['n']))-set(p['maxima']);induced=[(s&nonmax if i in nonmax else set()) for i,s in enumerate(g)];t=topo(induced)
  need((cr['nonmax_persistent_cycle'] is None)==(t is not None),'persistent cycle status')
  if cr['nonmax_persistent_cycle'] is not None:need(cycle_valid(cr['nonmax_persistent_cycle'],induced),'persistent cycle edges');persistent.append(cr['id'])
  if cr['acyclic_completion'] is not None:
   c=completion_check(r,cr['acyclic_completion']);need(c['structural']['full_forced_topological_order'] is not None,'claimed acyclic completion cyclic');comps.append(c)
  elif t is not None:bounded_absent.append(cr['id'])
 failures=[]
 for w in json.loads((src/'adaptive_fixed_pair_failures.json').read_text()):failures.append(completion_check(byid['n8c15-primal'],w))
 mut=mutate_tests(rows,cat)
 out=dict(verdict='PASS',profiles=checked,summary=dict(profiles=len(rows),fixed_profiles=sum(bool(r['fixed_pairs']) for r in rows),adaptive_profiles=[r['id'] for r in rows if not r['fixed_pairs']],selected_cells=sum(len(r['cells']) for r in rows),full_menu_masks=sum(len(r['full_menu_certificates']) for r in checked),persistent_cycle_profiles=persistent,acyclic_ordinal_completion_profiles=[r['profile_id'] for r in comps],no_witness_in_author_bounded_test_profiles=bounded_absent),actual_ordinal_completions=comps,adaptive_fixed_pair_failures=failures,mutation_tests=mut)
 dest=ROOT/('results_optimized.json' if sys.flags.optimize else 'results.json');dest.write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps(out['summary'],indent=2));print('FIXED FAILURE STRUCTURES',json.dumps([r['structural'] for r in failures],indent=2));print('PASS; fail-closed mutation tests:',len(mut))
if __name__=='__main__':main()
