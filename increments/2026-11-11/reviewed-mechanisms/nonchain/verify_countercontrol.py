"""Exact independent ideal-DP cross-check, not the analytic proof."""
import json
from functools import lru_cache
from pathlib import Path
ROOT=Path(__file__).parent

def build(n,orientation=None):
 V=['a','b','c','u','v','x','d']+['z'+str(i) for i in range(1,n+1)]
 E=[('a','u'),('a','v'),('b','c'),('a','x'),('c','x'),('a','d'),('c','d'),('u','z1'),('v','z1'),('d','z1'),('x','z'+str(n))]
 E += [('z'+str(i),'z'+str(i+1)) for i in range(1,n)]
 if orientation:E += [orientation]
 ix={v:i for i,v in enumerate(V)};p=[0]*len(V)
 for a,b in E:p[ix[b]]|=1<<ix[a]
 for k in range(len(V)):
  for i in range(len(V)):
   if p[i]>>k&1:p[i]|=p[k]
 return V,E,p

def calculate(n,orientation=None):
 V,E,p=build(n,orientation);ix={x:i for i,x in enumerate(V)};full=(1<<len(V))-1
 def le(pre):
  @lru_cache(None)
  def dp(I):
   if I==full:return 1
   return sum(dp(I|1<<i) for i in range(len(V)) if not I>>i&1 and pre[i]&I==pre[i])
  return dp(0)
 N=le(p)
 # Count an event by adding exactly its oriented edge and taking closure.
 K={}
 for a,b in [('b','a'),('v','c'),('x','v'),('d','v')]:
  q=p[:];q[ix[b]]|=1<<ix[a]
  for k in range(len(V)):
   for i in range(len(V)):
    if q[i]>>k&1:q[i]|=q[k]
  K[a+'<'+b]=0 if any(q[i]>>i&1 for i in range(len(V))) else le(q)
 up=[sum(1<<j for j in range(len(V)) if p[j]>>i&1) for i in range(len(V))]
 deg={v:len(V)-1-(p[i]|up[i]).bit_count() for i,v in enumerate(V)}
 D={v:[V[j] for j in range(len(V)) if p[i]>>j&1] for i,v in enumerate(V)}
 if not orientation:
  assert set(D['x'])==set(D['d'])=={'a','b','c'}
  assert set(D['u'])==set(D['v'])=={'a'}
  assert [v for i,v in enumerate(V) if v!='a' and not(p[i]>>ix['a']&1)]==['b','c']
  assert deg['x']==n+2 and max(deg.values())==max(5,n+2)
 return {'n':n,'orientation':orientation,'N':N,'K':K,'degrees':deg,'B_x':K['b<a']+K['v<c']+K['x<v']-N,'B_d':K['b<a']+K['v<c']+K['d<v']-N}

rows=[]
for n in range(1,9):
 r=calculate(n);plus=calculate(n,('x','d'));minus=calculate(n,('d','x'))
 assert r['N']==38*n+86
 assert r['K']=={'b<a':18*n+46,'v<c':14*n+20,'x<v':45,'d<v':12*n+33}
 assert r['B_x']==25-6*n and r['B_d']==6*n+13
 assert plus['N']==62 and plus['K']=={'b<a':32,'v<c':17,'x<v':30,'d<v':15} and plus['B_x']==17
 assert minus['N']==38*n+24 and minus['K']=={'b<a':18*n+14,'v<c':14*n+3,'x<v':15,'d<v':12*n+18} and minus['B_d']==6*n+11
 assert r['N']==plus['N']+minus['N']
 assert all(r['K'][k]==plus['K'][k]+minus['K'][k] for k in r['K'])
 rows.append({'original':r,'actual_fibers':[plus,minus]})
(ROOT/'VERIFIED_COUNTERCONTROL.json').write_text(json.dumps({'status':'PASS','method':'exact integer ideal DP; each event counted by one added edge','rows':rows},indent=2)+'\n')
print('PASS: analytic formulas and true orientation fibers, n=1..8; negative bank n=5..8, Delta=7..10.')
