"""Independent exact arithmetic for the seven-core global finite reduction.
Run: python check.py. No author imports, floating point, or third-party packages.
Infinite coverage is proved in AUDIT.md; arithmetic here checks its certificates.
"""
from fractions import Fraction as F
from math import prod
import json

checks = []
def require(condition, label):
    if not condition:
        raise ArithmeticError(label)
    checks.append(label)

def atanh_log_interval(z, terms=16):
    # log((1+z)/(1-z)); positive tail bounded geometrically.
    partial = 2*sum((z**(2*j+1)/F(2*j+1) for j in range(terms)), F(0))
    remainder = 2*z**(2*terms+1)/(F(2*terms+1)*(1-z*z))
    return partial, partial+remainder

Alo, Ahi = F(405465,10**6), F(405466,10**6)
Blo, Bhi = F(1098612,10**6), F(1098613,10**6)
for label,z,lo,hi in [('log(3/2)',F(1,5),Alo,Ahi),('log(3)',F(1,2),Blo,Bhi)]:
    lower, upper = atanh_log_interval(z)
    require(lo < lower < upper < hi, label+' rational bracket')
require(Blo > 1, 'log(3)>1')
C = 1/Ahi-2/Blo
L = lambda k: C*k-2/Blo-F(1,2)-Bhi/F(6*(k+1))
require(C > F(16,25), 'gamma slope')
require(L(2) > F(32,25)-F(12,5), 'gamma lower affine bound at k=2')
require(F(44,25)**2 > 3, 'gamma_1=-sqrt(3)>-44/25')
require(L(4)>F(22,100), 'gamma_4>22/100')
require(L(5)>F(87,100), 'gamma_k>87/100 for k>=5 by monotonicity')

# 7 S < 290, 37 P < 100 S in the a,d>=5 case.
S_high = (290-1)//7
P_high = (100*S_high-1)//37
require((S_high,P_high)==(41,110), 'large/large strict integer caps')
small=[]
for a,U in [(1,3),(2,9),(3,29)]:
    K=25*a+(85-16*a)*U
    # 7d < 25a+120+(85-16a)u; v < (25d+K)/(16d-60).
    D=(K+120-1)//7
    require(K>0 and -1500-16*K<0, f'small outer {a}: rational v bound decreases in d')
    r=F(125+K,20)
    V=(r.numerator-1)//r.denominator
    small.append(dict(a=a,u_max=U,d_max=D,v_max=V,S_max=a+D,P_max=U+V))
require([(x['d_max'],x['v_max']) for x in small]==[(50,17),(92,32),(181,63)], 'mixed small/large caps')
require(max(x['S_max'] for x in small)==184, 'mixed small/large outer sum')
require(max(x['P_max'] for x in small)==92, 'mixed small/large port sum')

# a=4,d>=6: 7d<259; d=5 is included separately.
D_four=(259-1)//7
require(D_four==36, 'four/large outer cap')
# a=4,u<=43: v<(25d+100+21u)/(16d-60), maximal at d=5,u=43.
K_four=100+21*43
require(-1500-16*K_four<0, 'four/large rational v bound decreases in d')
r_four=F(125+K_four,20)
V_four=(r_four.numerator-1)//r_four.denominator
require(V_four==56 and 43+V_four==99, 'four/large port caps')
require(2*43==86 and 2*4==8, 'small/small caps')
S=max(S_high,184,4+D_four,8)
P=max(P_high,92,99,86)
require((S,P)==(184,110), 'global sum caps')

# Independent d=4 adjacent-product boundary arithmetic.
def ratio(c):
    return prod((F(c+i,c+43+i) for i in range(5)),start=F(1))
require(ratio(172)==F(2207480,6660009)<F(1,3), 'd4 last allowed inner boundary')
require(ratio(173)==F(1480015,4440006)>F(1,3), 'd4 first excluded inner boundary')

coarse = F(611,64)*P+F(107,32)*S
require(coarse==F(53293,32) and coarse==1665+F(13,32), 'coarse total exact fraction')
BC_bound=F(177,32)*P+F(25,16)*S
BC=(BC_bound.numerator-1)//BC_bound.denominator
T=(BC+P//2-1)//2
require((BC,T)==(895,474), 'inner sum and middle coordinate caps')

# Reconstruct the four-coordinate envelope in both outer orders directly,
# rather than forming it by duplicating the author's a<=d enumeration.
V_small={1:3,2:9,3:29,4:43}
D_mixed={1:50,2:92,3:181,4:36}
P_other={1:17,2:32,3:63,4:56}
ordered_counts={'both_outer_at_most_four':0,'mixed':0,'both_outer_at_least_five':0}
canonical_counts=dict.fromkeys(ordered_counts,0)
for a in range(1,182):
    for d in range(1,182):
        if a<=4 and d<=4:
            umax,vmax=V_small[a],V_small[d]
            category='both_outer_at_most_four'
        elif a>=5 and d>=5:
            if a+d>41:
                continue
            umax=vmax=108
            category='both_outer_at_least_five'
        else:
            small_outer=min(a,d)
            if max(a,d)>D_mixed[small_outer]:
                continue
            umax,vmax=(V_small[a],P_other[a]) if a<=4 else (P_other[d],V_small[d])
            category='mixed'
        for u in range(2,umax+1):
            for v in range(2,vmax+1):
                if u+v>110:
                    continue
                if 16*(a*u+d*v)>=60*(u+v)+25*min(u,v)+25*(a+d):
                    continue
                if a<=4 and d>=5 and (16*d-60)*v>=25*d+25*a+(85-16*a)*u:
                    continue
                if d<=4 and a>=5 and (16*a-60)*u>=25*a+25*d+(85-16*d)*v:
                    continue
                ordered_counts[category]+=1
                if a<=d:
                    canonical_counts[category]+=1
require(list(canonical_counts.values())==[4508,8703,979], 'four-coordinate canonical category counts')
require(list(ordered_counts.values())==[6400,17406,1720], 'four-coordinate ordered category counts')
require(sum(canonical_counts.values())==14190 and sum(ordered_counts.values())==25526, 'four-coordinate envelope totals')

report={'status':'PASS','exact_checks':len(checks),'checks':checks,
        'mixed_small_large':small,'global_caps':{'a':181,'d':181,'a_plus_d':S,'u_plus_v':P,'u':P-2,'v':P-2,'b_plus_c':BC,'b':895,'c':895,'t':T},
        'coarse_N_strict_upper':str(coarse),'coarse_N_max':1665,
        'four_coordinate_envelope':{'canonical_a_le_d':canonical_counts,'ordered':ordered_counts,'canonical_total':sum(canonical_counts.values()),'ordered_total':sum(ordered_counts.values())}}
print(json.dumps(report,indent=2))
