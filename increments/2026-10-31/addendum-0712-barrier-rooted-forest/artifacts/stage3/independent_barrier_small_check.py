from itertools import permutations
from functools import lru_cache

def audit(n,mandatory,blocks,L,M,R):
 seen=set();valid=0;checks=0
 protected=set().union(*blocks)
 for order in permutations(range(n)):
  ix={v:i for i,v in enumerate(order)}
  if any(ix[a]>ix[b] for a,b in mandatory):continue
  pairs=[(a,b) for i,a in enumerate(order) for b in order[i+1:] if a in R or b in R]
  for mask in range(1<<len(pairs)):
   up=[0]*n
   for a,b in mandatory:up[a]|=1<<b
   for j,(a,b) in enumerate(pairs):
    if mask>>j&1:up[a]|=1<<b
   for k in range(n):
    for i in range(n):
     if up[i]>>k&1:up[i]|=up[k]
   tup=tuple(up)
   if tup in seen:continue
   seen.add(tup)
   # Preserve precisely the designated induced blocks, including absence of all cross-block comparisons.
   allowed=set(mandatory)
   if any((up[a]>>b&1) != ((a,b) in allowed) for a in protected for b in protected):continue
   pre=[sum(1<<j for j in range(n) if up[j]>>i&1) for i in range(n)];K=protected-M;rmask=sum(1<<r for r in R)
   du=0;uc=(1<<n)-1
   for x in M:du|=pre[x]&rmask;uc&=up[x]&rmask
   if any(du&~pre[k] or (up[k]&rmask)&~uc for k in K):continue
   valid+=1
   for cm in range(1<<len(R)):
    C={r for i,r in enumerate(sorted(R)) if cm>>i&1}
    def count(target):
     pp=pre+[0]
     for z in target:pp[z]|=1<<n
     @lru_cache(None)
     def rec(mask):
      if mask==(1<<(n+1))-1:return 1
      return sum(rec(mask|1<<i) for i in range(n+1) if not mask>>i&1 and pp[i]&mask==pp[i])
     return rec(0)
    B=count(M|C);Z=count(L|C);assert B<=Z,(up,C,B,Z);checks+=1
 return {'distinct_closures':len(seen),'valid_orders':valid,'C_instances':checks}
print('single fork q1,l2,m1:',audit(6,{(0,1),(0,2)},[{0,1,2},{3}],{1,2},{3},{4,5}))
print('two disjoint q1,l1 branches,m1:',audit(6,{(0,1),(2,3)},[{0,1},{2,3},{4}],{1,3},{4},{5}))
# Cross-branch counterexample: h1<l1<h2<l2, with independent m.
words=[p for p in permutations(range(5)) if p.index(0)<p.index(1)<p.index(2)<p.index(3)]
print('cross-branch counterexample:',{'N':len(words),'B':sum(p.index(4)+1 for p in words),'Z':sum(min(p.index(1),p.index(3))+1 for p in words)})
