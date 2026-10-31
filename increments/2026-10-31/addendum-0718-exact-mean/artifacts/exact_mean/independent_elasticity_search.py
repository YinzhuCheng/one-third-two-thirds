from itertools import product,permutations
from fractions import Fraction as F
from math import comb

def tpoly(n,hist,total):
 c=[F(0)]*(n+1)
 for r in range(1,n+1):
  for j in range(r):
   for k in range(j+1):c[n-j+k]+=F(hist[r]*comb(n,j)*comb(j,k)*(-1)**k,total)
 return c

def val(c,u):
 a=F(0)
 for x in reversed(c):a=a*u+x
 return a

def check(c):
 d=[(i+1)*c[i+1] for i in range(len(c)-1)];dd=[(i+1)*d[i+1] for i in range(len(d)-1)]
 for j in range(1,10):
  u=F(j,10);t=val(c,u);dt=val(d,u);ddt=val(dd,u)
  # derivative of u T'/T, times T^2
  numer=t*dt+u*t*ddt-u*dt*dt
  if numer>0:return u,numer
 return None
forests=instances=0
for n in range(1,7):
 for pars in product(*[range(-1,i) for i in range(n)]):
  sub=[1<<i for i in range(n)]
  for i in reversed(range(n)):
   if pars[i]>=0:sub[pars[i]]|=sub[i]
  les=[p for p in permutations(range(n)) if all(pars[x]<0 or p.index(pars[x])<p.index(x) for x in range(n))]
  forests+=1
  for mask in range(1,1<<n):
   if any(mask>>i&1 and sub[i]&mask!=sub[i] for i in range(n)):continue
   hist=[0]*(n+1)
   for p in les:hist[next(j+1 for j,x in enumerate(p) if mask>>x&1)]+=1
   bad=check(tpoly(n,hist,len(les)));assert bad is None,(n,pars,mask,bad)
   instances+=1
print('ROOT_FOREST',forests,instances,'instances;',instances*9,'exact elasticity-derivative tests passed',flush=True)
# Independent exhaustive non-rooted search at n=5, permitting arbitrary upsets.
n=5;pairs=[(i,j) for i in range(n) for j in range(i+1,n)];seen=set();tested=0
for emask in range(1<<len(pairs)):
 up=[0]*n
 for j,(a,b) in enumerate(pairs):
  if emask>>j&1:up[a]|=1<<b
 for k in range(n):
  for i in range(n):
   if up[i]>>k&1:up[i]|=up[k]
 if tuple(up) in seen:continue
 seen.add(tuple(up));les=[p for p in permutations(range(n)) if all(p.index(i)<p.index(j) for i in range(n) for j in range(n) if up[i]>>j&1)]
 for mask in range(1,1<<n):
  if any(mask>>i&1 and up[i]&mask!=up[i] for i in range(n)):continue
  hist=[0]*(n+1)
  for p in les:hist[next(j+1 for j,x in enumerate(p) if mask>>x&1)]+=1
  bad=check(tpoly(n,hist,len(les)));tested+=1
  if bad:
   print('NONFOREST_ELASTICITY_COUNTEREXAMPLE',{'n':n,'up':up,'Lmask':mask,'rankhist':hist,'N':len(les),'u':str(bad[0]),'positive_derivative_numerator':str(bad[1])});raise SystemExit
print('ARBITRARY_5_NO_COUNTEREXAMPLE',len(seen),tested)
