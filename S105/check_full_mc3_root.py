import json,sys
from functools import lru_cache
from fractions import Fraction
from pathlib import Path
p=Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).parent/'mc3_coupled_search/MC3_COUNTEREXAMPLE_high.json'
j=json.loads(p.read_text()); shape=j['shape']; starts=[0,shape[0],shape[0]+shape[1]];n=sum(shape);pred=[0]*n
for o,L in zip(starts,shape):
 for i in range(o+1,o+L):pred[i]|=1<<(i-1)
for u,v in j['extra_edges']:pred[v]|=1<<u
full=(1<<n)-1
def e(pair=None):
 pp=pred.copy()
 if pair:pp[pair[1]]|=1<<pair[0]
 @lru_cache(None)
 def f(mask):
  if mask==full:return 1
  return sum(f(mask|1<<i) for i in range(n) if not(mask>>i&1) and pp[i]&mask==pp[i])
 return f(0)
x,y,a=starts;b=a+1;pairs=[(a,x),(a,y),(b,x),(b,y),(x,y)]
E=e();K=[e(q) for q in pairs]
assert E==int(j['E']) and K==list(map(int,j['K']))
assert min(3*K[0]-2*E,3*K[1]-2*E,3*K[4]-2*E,E-3*K[2],3*K[3]-2*E)>0
print('PASS five counts',E,K,flush=True)
print('margins',[3*K[0]-2*E,3*K[1]-2*E,3*K[4]-2*E,E-3*K[2],3*K[3]-2*E],flush=True)
for c in range(n):
 if c in [a,b,x,y]:continue
 for z in [a,b,x,y]:
  k=e((c,z))
  if E<=3*k<=2*E:
   print('ACTUAL BALANCED PAIR',(c,z),str(Fraction(k,E)),k,E,flush=True);raise SystemExit
