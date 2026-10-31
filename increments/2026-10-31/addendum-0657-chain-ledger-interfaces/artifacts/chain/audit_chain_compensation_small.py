from itertools import permutations
from functools import lru_cache
seen=set();valid=[];all_count=0
n=6;K={0,1,2};M={3};R={4,5};Rmask=(1<<4)|(1<<5)
for order in permutations(range(n)):
 if not(order.index(0)<order.index(1)<order.index(2)):continue
 pairs=[(a,b) for i,a in enumerate(order) for b in order[i+1:] if not(a in K and b in K) and not((a in K and b in M) or(a in M and b in K))]
 for mask in range(1<<len(pairs)):
  up=[0]*n;up[0]=(1<<1)|(1<<2);up[1]=1<<2
  for j,(a,b) in enumerate(pairs):
   if mask>>j&1:up[a]|=1<<b
  for k in range(n):
   for i in range(n):
    if up[i]>>k&1:up[i]|=up[k]
  tup=tuple(up)
  if tup in seen:continue
  seen.add(tup)
  if any((up[k]>>3&1) or(up[3]>>k&1) for k in K):continue
  pre=[sum(1<<j for j in range(n) if up[j]>>i&1) for i in range(n)]
  if (pre[3]&Rmask)&~pre[0] or(up[0]&Rmask)&~up[3]:continue
  all_count+=1
  for C in [set(),{4},{5},{4,5}]:
   def insertion_count(targets):
    pp=pre+[0]
    for z in targets:pp[z]|=1<<n
    @lru_cache(None)
    def dp(mask):
     if mask==(1<<(n+1))-1:return 1
     return sum(dp(mask|1<<i) for i in range(n+1) if not mask>>i&1 and pp[i]&mask==pp[i])
    return dp(0)
   B=insertion_count(M|C);Z=insertion_count({1,2}|C)
   assert B<=Z,(up,C,B,Z)
print('Distinct six-point orders considered:',len(seen))
print('Orders satisfying chain separation and endpoint conditions:',all_count)
print('Tested C choices:',all_count*4,'; no counterexamples')
