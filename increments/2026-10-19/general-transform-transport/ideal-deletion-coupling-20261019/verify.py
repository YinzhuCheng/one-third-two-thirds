from fractions import Fraction as F
from collections import Counter, defaultdict
from math import comb
import json
from pathlib import Path
ROOT=Path(__file__).parent
# Six structures are fixed before computation; selected pairs only, no search.
CONTROLS=[
 dict(name='A3-sharp',n=3,edges=[],pairs=[({0},{0,1}),({0,1},{1,2})]),
 dict(name='C2-plus-C1-positive-gap',n=3,edges=[(0,1)],pairs=[({0},{0,1}),({0,1},{0,2})]),
 dict(name='A8-cov-greater-than-r',n=8,edges=[],pairs=[(set(range(6)),set(range(7))),(set(range(6)),set(range(2,8)))]),
 dict(name='C2-plus-C2',n=4,edges=[(0,1),(2,3)],pairs=[({0,2},{0,1,2}),({0,1},{2,3})]),
 dict(name='fork-tail-isolate',n=5,edges=[(0,2),(1,2),(2,3)],pairs=[({0,1},{0,1,2,4}),({0,1,2},{0,4})]),
 dict(name='asymmetric-twofork',n=6,edges=[(0,3),(1,3),(1,4),(2,4),(3,5),(4,5)],pairs=[({0,1,2},{0,1,2,3,4}),({0,1,3},{1,2,4})]),
]
def extensions(n,edges,subset=None):
 if subset is None:subset=set(range(n))
 pred={v:set() for v in subset}
 for a,b in edges:
  if a in subset and b in subset:pred[b].add(a)
 ans=[]
 def rec(w,remaining):
  if not remaining:ans.append(tuple(w));return
  for x in sorted(remaining):
   if not(pred[x]&remaining):rec(w+[x],remaining-{x})
 rec([],set(subset))
 return ans

def run(w,A):
 z=0
 for x in w:
  if x not in A:break
  z+=1
 return z

def f(x):return str(x)
results=[]
for c in CONTROLS:
 n=c['n'];edges=c['edges'];LE=extensions(n,edges);N=len(LE)
 out={'name':c['name'],'n':n,'edges':edges,'extensions':N,'pairs':[]}
 for K,L in c['pairs']:
  assert all(not(b in K) or a in K for a,b in edges)
  assert all(not(b in L) or a in L for a,b in edges)
  X=[run(w,K) for w in LE];Y=[run(w,L) for w in LE]
  r=F(sum(X),N);s=F(sum(Y),N);m2=F(sum(comb(x,2) for x in X),N)
  v=F(sum(x*x for x in X),N)-r*r
  cov=F(sum(x*y for x,y in zip(X,Y)),N)-r*s
  a=F(n,1)/(n+1)-s/(n+1)
  b1=a*(r+m2);b2=r*r-m2-(s+1)*(r+m2)/(n+1)
  finite_moment=F(n+1,1)*r*(r+1)/(n+r+2)
  finite_var=F(n,1)*r*(r+1)/(n+r+2)-r*r*(r+1)/(n+r+2)
  finite_cov=(n-s)*r*(r+1)/(n+r+2)
  assert r+m2<=finite_moment and v<=finite_var and cov<=finite_cov
  assert cov<=b1 and cov-v<=b2 and cov<=r*(r+1)
  assert m2<=r*r
  minmean=F(sum(min(x,y) for x,y in zip(X,Y)),N)
  finite_slot_r=r+(n-s)*r*(r+1)/(n+r+2)
  finite_slot_s=s+(n-r)*s*(s+1)/(n+s+2)
  assert cov+minmean<=min(finite_slot_r,finite_slot_s)
  assert r*r+2*r-(cov+minmean)>=r*(r+1)*(r+s+2)/(n+r+2)
  assert cov+minmean<=min(r*r+2*r,s*s+2*s)
  words_checked=0;ideals_checked=0
  by_word={}
  for i in range(1,len(K)+1):
   groups=defaultdict(list)
   for w,y in zip(LE,Y):
    if set(w[:i])<=K:groups[w[:i]].append((w[i:],y))
   for word,rem in groups.items():
    A=set(word);Q=set(range(n))-A
    residual=extensions(n,edges,Q)
    # Exact conditional bijection: each remaining LE occurs exactly once.
    assert Counter(w for w,y in rem)==Counter(residual)
    my=F(sum(y for w,y in rem),len(rem))
    assert my<=s+i*a
    if A<=L:
     mu=F(sum(run(w,L-A) for w in residual),len(residual))
     assert my==i+mu
     assert mu<=s-F(i,1)*(s+1)/(n+1)
     ideals_checked+=1
    else:
     assert len({y for w,y in rem})==1
     assert my<=i-1
    words_checked+=1
   if groups:
    allrem=[z for group in groups.values() for z in group]
    conditional=F(sum(y for w,y in allrem),len(allrem))
    assert conditional<=s+i*a
  out['pairs'].append({'K':sorted(K),'L':sorted(L),'nested':K<=L,'r':f(r),'s':f(s),'M2':f(m2),'VarX':f(v),'cov':f(cov),'finite_moment_bound':f(finite_moment),'finite_var_bound':f(finite_var),'finite_cov_bound':f(finite_cov),'C1_bound':f(b1),'C1_slack':f(b1-cov),'cov_X_YminusX':f(cov-v),'C2_bound':f(b2),'gX':f(r*(r+1)-v),'cov_minus_r':f(cov-r),'prefix_words_checked':words_checked,'prefix_ideal_occurrences_checked':ideals_checked})
 results.append(out)
 print(c['name'],'LE=',N)
 for p in out['pairs']:print(' ',p)
ROOT.joinpath('verification.json').write_text(json.dumps({'status':'PASS','actual_structures':len(CONTROLS),'selected_pairs':sum(len(c['pairs']) for c in CONTROLS),'controls':results},ensure_ascii=False,indent=2)+'\n')
print('PASS: six fixed actual structures, twelve selected ideal pairs; exact Fraction verification.')
