from fractions import Fraction as F
from math import comb
from pathlib import Path
import json

# One already-existing actual example, checked from its PMF rather than a tail-moment formula.
a,b,k,ell=10,190,7,9
p=[F(comb(a+b-j,a-j),comb(a+b,a)) for j in range(a+1)]+[F(0)]
pmf=[p[j]-p[j+1] for j in range(a+1)]
r=sum((pmf[j]*min(j,k) for j in range(a+1)),F(0))
s=sum((pmf[j]*min(j,ell) for j in range(a+1)),F(0))
product=sum((pmf[j]*min(j,k)*min(j,ell) for j in range(a+1)),F(0))
N=product+r
cov=product-r*s
gap=r*(r+1)-cov
assert r==F(996464317,19032468455)
assert s==F(6154163621889,117544525178080)
assert N==F(234277819681,2137173185056)
assert gap==F(6550878543122831207,11414094221988575803400)
old_case={'parameters':[a,b,k,ell], 'r':str(r),'s':str(s),'N':str(N),'gap':str(gap)}

# Parent-specified random-cap boundary, direct moments with exact fractions.
pmf={0:F(1,2),1:F(1,4),2:F(1,8),3:F(1,8)}
mu=sum((j*p for j,p in pmf.items()),F(0))
second=sum((j*j*p for j,p in pmf.items()),F(0))
r=mu/10
cov=(second-mu*mu)/10
bound=r*(r+1)
assert (mu,second,r,cov,bound,cov-bound)==(F(7,8),F(15,8),F(7,80),F(71,640),F(609,6400),F(101,6400))
random_cap={'EJ':str(mu),'EJ2':str(second),'r':str(r),'cov':str(cov),'bound':str(bound),'excess':str(cov-bound),'actual_poset_claim':False}
result={'existing_case':old_case,'random_cap':random_cap,'passes':True}
Path('/workspace/shared/audit-nbu-prefix-20261018/final_addenda_checks.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(result,ensure_ascii=False,indent=2))
