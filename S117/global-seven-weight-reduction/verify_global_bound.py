#!/usr/bin/env python3
from fractions import Fraction as Q
import json


def require(condition, label):
    if not condition:
        raise RuntimeError(label)


def log_interval(z, n=12):
    s = 2 * sum((z ** (2*j+1) / (2*j+1) for j in range(n)), Q(0))
    r = 2*z**(2*n+1)/((2*n+1)*(1-z*z))
    return s, s+r

Alo, Ahi = Q(405465,10**6), Q(405466,10**6)
Blo, Bhi = Q(1098612,10**6), Q(1098613,10**6)
for z, lo, hi in ((Q(1,5),Alo,Ahi),(Q(1,2),Blo,Bhi)):
    lower, upper = log_interval(z)
    require(lo < lower < upper < hi, 'exact logarithm bracket')
C = 1/Ahi-2/Blo
F = lambda k: C*k-2/Blo-Q(1,2)-Bhi/(6*(k+1))
require(C > Q(16,25), 'positive linear-comparison slope')
require(F(2) > Q(32,25)-Q(12,5), 'all-k line base case')
require(3*25**2 < 44**2, 'gamma1 exact radical bound')
require(F(4) > Q(11,50), 'gamma at least four')
require(F(5) > Q(87,100), 'gamma at least five')
require(Q(290,7) > 41 and Q(290,7) <=42, 'outer sum cap')
require(Q(4100,37)>110 and Q(4100,37)<=111, 'large-large port cap')

V={1:3,2:9,3:29,4:43}
Ds={1:50,2:92,3:181}
Vs={1:17,2:32,3:63,4:56}
case_rows=[]
for a in range(1,5):
    u=V[a]
    d_cap=Q(25*a+120+(85-16*a)*u,7)
    if a<=3:
        require(Ds[a] < d_cap <= Ds[a]+1, 'mixed outer cap')
    K=25*a+(85-16*a)*u
    require(-1500-16*K<0, 'decreasing mixed port ratio')
    v_cap=Q(125+K,20)
    require(Vs[a] < v_cap <= Vs[a]+1, 'mixed port cap')
    case_rows.append({'a':a,'u_cap':u,'strict_d_bound':str(d_cap),
                      'd_cap_used':Ds.get(a,36),
                      'strict_v_bound':str(v_cap),'v_cap':Vs[a],
                      'port_sum_cap':u+Vs[a]})
require(Q(16*6,25)-Q(12,5)-1>0, 'a4 d>=6 positive coefficient')
require(2*Q(11,50)-2-2*Q(12,5) == -Q(159,25), 'a4 constant')
require(Q(4)+Q(159,25)==Q(259,25), 'a4 outer bound d<37')
require(Q(259,7)==37, 'a4 outer cap36')
require(max(1+50,2+92,3+181,4+36,41,8)==184,'global outer sum')
require(max(86,20,41,92,99,110)==110,'conditional global port sum')
require(Q(3,2)*Q(177,32)+Q(5,4)==Q(611,64),'N port coefficient')
require(Q(3,2)*Q(25,16)+1==Q(107,32),'N outer coefficient')
N_bound=Q(611,64)*110+Q(107,32)*184
require(N_bound==Q(53293,32)==1665+Q(13,32),'total-order bound')
B_bound=Q(177,32)*110+Q(25,16)*184
require(895<B_bound<896,'inner sum cap895')
require((895+55-1)//2==474,'middle cap474')
report={
 'status':'PASS',
 'arithmetic':'exact integers and fractions only',
 'full_bound_dependency':'independently audited H4: d=4 implies v<=43 and its dual',
 'C_lower_expression':str(C),
 'F2':str(F(2)), 'F4':str(F(4)), 'F5':str(F(5)),
 'gamma_uniform_lower':'16*k/25 - 12/5',
 'mixed_cases':case_rows,
 'unconditional_outer_max':181,
 'unconditional_outer_sum_max':184,
 'global_port_sum_max':110,
 'global_total_order_strict_bound':str(N_bound),
 'global_total_order_max':1665,
 'large_census_started':False,
}
print(json.dumps(report,indent=2))
