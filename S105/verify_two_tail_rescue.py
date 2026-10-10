"""Exact symbolic checks supporting two_tail_mc3_rescue.txt.

The proof itself is self-contained. This script independently checks the s=1
counting base, the arbitrary-s induction increments for all six counts,
the coupled identities, the binomial inverse-ratio increment, and the
strict rescue estimate. No floating-point inequalities or probability
renormalizations are used.
"""
from pathlib import Path
import json
import sympy as z

s = z.symbols('s', integer=True, positive=True)
U0,U1,U2,I,u,v,S = z.symbols('U0 U1 U2 I u v S')
M,R,j = z.symbols('M R j')
C=U0+2*U1

def counts(ss,ii,uu):
    return z.Matrix([
        C+2*ii-(2*ss+1)*uu,
        2*ii-(2*ss+1)*uu,
        2*U0+ii-(ss+1)*uu,
        ii-(2*ss+1)*uu,
        3*U0-2*U1-uu,
        3*U0,
    ])  # E,K_ax,K_ay,K_bx,K_by,K_xy

checks=[]
def equal(name,a,b=0):
    if isinstance(a,z.MatrixBase):
        diff=a-b
        assert all(z.simplify(t)==0 for t in diff),(name,diff)
    else:
        assert z.simplify(a-b)==0,(name,z.simplify(a-b))
    checks.append(name)

# Direct six-cell s=1 partition. Each row has all six event counts.
V0,V1=U0-U1,U1-U2
rows=[
    [U0+U1,0,U0,0,V0,U0+U1],
    [U1,0,0,0,0,0],
    [U0,U0,U0,0,V0,U0],
    [2*U1,2*U1,U1,0,0,0],
    [V0,V0,V0,V0,V0,V0],
    [3*V1,3*V1,2*V1,3*V1,V1,0],
]
base=sum((z.Matrix(row) for row in rows),z.zeros(6,1))
equal('all six base counts at s=1',counts(1,U0+2*U1,U2),base)

# Advancing s adds precisely the two cells (1,s+1),(2,s+1).
# Here u=U_(s+1), v=U_(s+2), and the prefix counts are 2 and 2s+3.
added=z.Matrix([
    2*u+(2*s+3)*(u-v),
    2*u+(2*s+3)*(u-v),
    u+(s+2)*(u-v),
    (2*s+3)*(u-v),
    u-v,
    0,
])
equal('all six arbitrary-s induction increments',counts(s+1,I+2*u,v)-counts(s,I,u),added)

E,A,Y,B,BY,X=counts(s,I,u)
equal('HALF difference',2*B-A,-(2*s+1)*u)
equal('exact opposite-marginal coupling',BY,2*Y-E)
equal('entry count',X,3*U0)
T=(2*s+1)*u
E,A,Y,B,BY,X=[z.expand(t.subs(I,C+2*S)) for t in counts(s,I,u)]
equal('a-majority margin',3*A-2*E,4*S-T)
equal('b-low margin',3*B-E,2*(S-T))
equal('opposite upper-margin form',2*E-3*BY,-3*U0+18*U1+8*S+(1-4*s)*u)

# U_j/U_(j+1)=(M+R-1-j)/(R-j).
rho=(M+R-1-j)/(R-j)
equal('inverse-ratio increment',rho.subs(j,j+1)-rho,(M-1)/((R-j)*(R-j-1)))
equal('inverse-ratio normal form',rho,1+(M-1)/(R-j))
equal('s>=2 ratio cap',5-(2*s+1)/(s-1),3*(s-2)/(s-1))

# Make the two strict positive gaps explicit. If g1=5U1-U0>0 and
# g2=4S-(2s+1)u>0, the upper margin is 3U1+3u+3g1+2g2.
g1,g2=z.symbols('g1 g2')
upper=2*E-3*BY
equal('strict rescue positivity decomposition',upper,
      3*U1+3*u+3*(5*U1-U0)+2*(4*S-T))

result={'status':'all exact symbolic checks passed','checks':checks,
        'scope':'P(m,r,s): m>=1, r>=1, 1<=s<=r; proof uses original full extension counts',
        'formal_proof':False,
        'note':'Symbolic algebra supports the self-contained combinatorial proof; it is not a proof-assistant certificate.'}
out=Path(__file__).with_name('two_tail_symbolic_check.json')
out.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
