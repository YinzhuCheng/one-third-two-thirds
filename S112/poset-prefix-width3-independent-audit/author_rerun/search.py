from itertools import combinations, product
from fractions import Fraction as Q
from functools import lru_cache
from pathlib import Path
import json,sys,time
import numpy as np
from scipy.optimize import linprog
OUT=Path(__file__).resolve().parent

def gen_posets(n):
 if not n: yield (); return
 for ps in gen_posets(n-1):
  for s in range(1<<(n-1)):
   if all(not (s>>i&1) or not(p&~s) for i,p in enumerate(ps)):
    yield ps+(s,)

def width(ps):
 return max(s.bit_count() for s in range(1<<len(ps)) if all(not(s>>i&1) or not(p&s) for i,p in enumerate(ps)))

def profile(ps):
 n=len(ps);full=(1<<n)-1
 maxima=[i for i in range(n) if not any(p>>i&1 for p in ps)]
 ids=[full^(1<<i) for i in maxima]
 common=full
 for s in ids:common &=s
 @lru_cache(None)
 def e(s):
  if not s:return 1
  return sum(e(s^(1<<i)) for i in range(n) if (s>>i&1) and not any((s>>j&1) and (ps[j]>>i&1) for j in range(n)))
 F=[e(s) for s in ids]
 pairs=[];A=[]
 for x,y in combinations([i for i in range(n) if common>>i&1],2):
  if ps[y]>>x&1:continue
  @lru_cache(None)
  def ee(s):
   if not s:return 1
   return sum(ee(s^(1<<i)) for i in range(n) if (s>>i&1) and not any((s>>j&1) and ((ps[j]>>i&1) or (j==y and i==x)) for j in range(n)))
  a=[ee(s) for s in ids]
  if all(f<=3*v<=2*f for v,f in zip(a,F)):
   return None
  pairs.append([x,y]);A.append(a)
 if not pairs:return None
 return dict(pred=list(ps),n=n,r=n-1,maxima=maxima,ideals=ids,F=F,pairs=pairs,A=A)

def cover(prof):
 rows=np.array(prof['A'],float)/np.array(prof['F'],float)
 m=len(prof['F']);k=len(rows)
 for sides in product([0,1],repeat=k):
  h=np.array([([1/3]*m-q if side==0 else q-[2/3]*m) for q,side in zip(rows,sides)])
  z=linprog([0]*m+[-1],A_ub=np.c_[-h,np.ones(k)],b_ub=[0]*k,A_eq=[[1]*m+[0]],b_eq=[1],bounds=[(0,None)]*m+[(None,None)],method='highs')
  assert z.success
  if z.x[-1]>1e-9:return False
 return True

def reductions(ps):
 return [[j,i] for i,p in enumerate(ps) for j in range(i) if p>>j&1 and not any(p>>k&1 and ps[k]>>j&1 for k in range(j+1,i))]

def canonical(ps):
 # Tiny graph isomorphism brute force separated by predecessor/successor degree.
 from itertools import permutations
 n=len(ps);su=[sum(bool(p>>i&1) for p in ps) for i in range(n)]
 groups={}
 for i,p in enumerate(ps):groups.setdefault((p.bit_count(),su[i]),[]).append(i)
 gs=[groups[k] for k in sorted(groups)]
 best=None
 for parts in product(*(list(permutations(g)) for g in gs)):
  perm=sum((list(x) for x in parts),[])
  code=tuple(int(ps[j]>>i&1) for i in perm for j in perm)
  if best is None or code<best:best=code
 return best

if __name__=='__main__':
 found=[];seen=set();stats={};start=time.time()
 for n in range(5,8):
  cnt=[0,0,0,0]
  for ps in gen_posets(n):
   cnt[0]+=1
   maxima=[i for i in range(n) if not any(p>>i&1 for p in ps)]
   if len(maxima)!=3 or width(ps)!=3:continue
   cnt[1]+=1
   prof=profile(ps)
   if prof is None:continue
   cnt[2]+=1
   code=canonical(ps)
   if code in seen:continue
   seen.add(code)
   if cover(prof):
    cnt[3]+=1;prof['covers']=True;prof['covers_edges']=reductions(ps);found.append(prof)
    print('FOUND',json.dumps(prof),flush=True)
  stats[n]=cnt
  print('STATS',n,cnt,time.time()-start,flush=True)
 (OUT/'candidates.json').write_text(json.dumps({'stats':stats,'candidates':found},indent=2))
