from itertools import product,permutations
from fractions import Fraction as F
from math import comb,ceil

def poly_integral_survival(n,r):
 c=[F(0)]*(n+2)
 for j in range(r):
  for k in range(n-j+1):c[j+k+1]+=F(comb(n,j)*comb(n-j,k)*(-1)**k,j+k+1)
 return c

def value(c,t):
 a=F(0)
 for v in reversed(c):a=a*t+v
 return a
orders=ideals=checks=0
for n in range(1,7):
 rankpoly=[None]+[poly_integral_survival(n,r) for r in range(1,n+1)]
 for pars in product(*[range(-1,i) for i in range(n)]):
  children=[[] for _ in range(n)];roots=[];anc=[0]*n
  for i,p in enumerate(pars):
   if p<0:roots.append(i)
   else:children[p].append(i);anc[i]=anc[p]|1<<p
  sub=[1<<i for i in range(n)]
  for i in reversed(range(n)):
   for j in children[i]:sub[i]|=sub[j]
  les=[p for p in permutations(range(n)) if all(pars[x]<0 or p.index(pars[x])<p.index(x) for x in range(n))]
  orders+=1
  for mask in range(1,1<<n):
   if any(mask>>i&1 and sub[i]&mask!=sub[i] for i in range(n)):continue
   def cap(i):
    if not sub[i]&mask:return F(0)
    size=sub[i].bit_count()
    if sub[i]&mask==sub[i]:return F(size)
    s=sum((cap(j) for j in children[i]),F(0))
    return size*s/(size+s+1)
   kappa=sum((cap(i) for i in roots),F(0));assert 0<kappa<=mask.bit_count()
   m=ceil(kappa);hist=[0]*(n+1)
   for p in les:hist[next(j+1 for j,x in enumerate(p) if mask>>x&1)]+=1
   coeff=[sum((F(hist[r],len(les))*rankpoly[r][i] for r in range(1,n+1)),F(0)) for i in range(n+2)]
   target=poly_integral_survival(m,1)
   for i,c in enumerate(target):coeff[i]-=c
   for j in range(1,11):
    t=F(j,10);assert value(coeff,t)>=0,(n,pars,mask,kappa,t,value(coeff,t));checks+=1
   ideals+=1
print({'indexed_root_forests':orders,'nonempty_upper_ideal_instances':ideals,'exact_rational_truncation_checks':checks,'max_n':6})
