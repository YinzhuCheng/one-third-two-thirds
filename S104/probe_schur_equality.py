from functools import lru_cache
from random import Random
from fractions import Fraction as F
import json
rng=Random(941)
def count(p):
 n=len(p)
 @lru_cache(None)
 def e(S):
  if not S:return 1
  return sum(e(S^(1<<i)) for i in range(n) if S>>i&1 and not p[i]&S)
 return e
zeros=[];best=None
for trial in range(40000):
 n=rng.randrange(3,14);p=[0]*n
 # first three are minima; every later vertex has ancestor first-three
 for v in range(3,n):
  for i in range(v):
   if rng.random()<.25:p[v]|=(1<<i)|p[i]
  if not p[v]:p[v]=1<<rng.randrange(3)
 e=count(p);S=(1<<n)-1
 B=[[0]*3 for _ in range(3)]
 for i in range(3):
  for j in range(3):
   if i!=j:B[i][j]=e(S^(1<<i)^(1<<j))
   else:B[i][i]=sum(e(S^(1<<i)^(1<<v)) for v in range(3,n) if p[v]==1<<i)
 a,b,c=B[0];d,f=B[1][1:];h=B[2][2]
 det=a*d*h+2*b*c*f-a*f*f-d*c*c-h*b*b
 if det==0:
  zeros.append(dict(p=p,B=B,n=n)); print('ZERO',zeros[-1],flush=True);break
 if det<0:raise Exception((p,B,det))
 val=F(det,e(S)**3)
 if best is None or val<best['val']:best=dict(val=val,p=p,B=B)
print('done',trial,'zeros',zeros,'best',best)
