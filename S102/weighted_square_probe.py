from functools import lru_cache
from random import Random
from fractions import Fraction
import json
rng=Random(171981)
def test(n,edges):
 pred=[0]*n
 for a,b in edges:pred[b]|=1<<a
 for b in range(n):
  for a in range(b):
   if pred[b]>>a&1:pred[b]|=pred[a]
 @lru_cache(None)
 def dp(m):
  if m==(1<<n)-1:return 1
  return sum(dp(m|1<<i) for i in range(n) if not m>>i&1 and pred[i]&m==pred[i])
 E=dp(0); f={0:1}; sums=[[0,0,0] for _ in range(n)]
 y=0
 for m in range(1<<n):
  if m not in f:continue
  count=f[m]
  if not m&1:
   w=count*dp(m|1)
   for u in range(1,n):
    if pred[u]&1:continue
    if pred[u]&m==pred[u]:sums[u][0]+=w
    if m>>u&1:sums[u][1]+=w
    if any(m>>s&1 and pred[s]>>u&1 for s in range(n)):sums[u][2]+=w
  for i in range(1,n):
   if not m>>i&1 and pred[i]&m==pred[i]:
    j=m|1<<i;f[j]=f.get(j,0)+count
 for u,(D,A,B) in enumerate(sums):
  if D*B>A*A:return dict(n=n,edges=edges,u=u,E=E,D=D,A=A,B=B,pred=pred)
 return None
for n in range(4,13):
 for k in range(3000):
  q=rng.random()*.6
  edges=[(a,b) for a in range(n) for b in range(a+1,n) if rng.random()<q]
  r=test(n,edges)
  if r:print('COUNTER',json.dumps(r),flush=True);raise SystemExit
 print('PASS',n,flush=True)
