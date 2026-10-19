from fractions import Fraction as F
from math import comb
import json
import sympy as S
from pathlib import Path
ROOT=Path(__file__).parent
law={(0,0):F(200,400),(0,1):F(100,400),(0,2):F(22,400),(1,2):F(28,400),(0,3):F(15,400),(1,3):F(10,400),(0,4):F(23,400),(1,4):F(2,400)}
assert sum(law.values())==1 and all(x<=y for x,y in law)
E=lambda fun:sum(p*fun(x,y) for (x,y),p in law.items())
r,s,c=E(lambda x,y:x),E(lambda x,y:y),E(lambda x,y:x*y)
cov=c-r*s
assert (r,s,c,cov,cov-r*(r+1))==(F(1,10),F(15,16),F(47,200),F(113,800),F(1,32))
def C(n,k):return comb(n,k) if n>=k>=0 else 0
def lc(a):return [a[j]**2-(a[j-1]*a[j+1] if j<len(a)-1 else 0) for j in range(1,len(a))]
qx=[E(lambda x,y,i=i:int(x>=i)) for i in range(2)]
qy=[E(lambda x,y,i=i:int(y>=i)) for i in range(5)]
mx=[E(lambda x,y,i=i:C(x,i)) for i in range(2)]
my=[E(lambda x,y,i=i:C(y,i)) for i in range(5)]
a=[E(lambda x,y,i=i:int(x>=i)*(y-i+1)) for i in range(2)]
b=[E(lambda x,y,j=j:int(y>=j)*(min(x,j)+1)) for j in range(5)]
B=[F(1)]+[E(lambda x,y,k=k:(x+1)*C(y,k)-C(x,k+1)) for k in range(1,5)]
for seq in [qx,qy,mx,my,a,b,B]:assert min(lc(seq))>=0
assert all(E(lambda x,y,i=i,j=j:int(x>=i and y>=j))>0 for i in range(2) for j in range(i,5))
w=E(lambda x,y:sum(y-i+1 for i in range(x+1)))
u=E(lambda x,y:sum(i*(y-i+1) for i in range(x+1)))
d=E(lambda x,y:sum(C(y-i+1,2) for i in range(x+1)))
v=E(lambda x,y:sum(i*C(y-i+1,2) for i in range(x+1)))
assert (w,u,d,v,u*d-w*v)==(F(869,400),F(47,200),F(9,5),F(7,40),F(137,3200))
m=S.symbols('m', integer=True, positive=True)
pY={y:sum(p for (x,t),p in law.items() if t==y) for y in range(5)}
zY={y:law.get((1,y),F(0)) for y in range(5)}
def binpoly(y,start):
    # binom(m+y,m+start), polynomial degree y-start
    return S.prod(m+k for k in range(start+1,y+1))/S.factorial(y-start) if y>=start else S.Integer(0)
def sf(f):return S.Rational(f.numerator,f.denominator)
A=sum(sf(pY[y])*binpoly(y,0) for y in range(5))
Bm=sum(sf(zY[y])*binpoly(y-1,0) for y in range(1,5))
Cm=sum(sf(pY[y])*binpoly(y,1) for y in range(5))
Dm=sum(sf(zY[y])*binpoly(y-1,1) for y in range(1,5))
P=S.factor(Bm*Cm-A*Dm)
expected=(m**6+45*m**5+739*m**4+5223*m**3+16612*m**2+16116*m-19008)/460800
assert S.expand(P-expected)==0
# Shift m=1+t: every coefficient positive implies positivity for all m>=1.
t=S.symbols('t',nonnegative=True)
assert all(v>0 for v in S.Poly(S.expand(P.subs(m,t+1)),t).all_coeffs())
bm={0:S.Integer(1)}
for j in range(1,5):
    z=E(lambda x,y,j=j:int(x==1 and y>=j))
    bm[j]=S.prod(m+k for k in range(j))/S.factorial(j)*sf(qy[j])+S.prod(m+k for k in range(j-1))/S.factorial(j-1)*sf(z)
blc={}
for j in range(1,4):
    value=S.factor(bm[j]**2-bm[j-1]*bm[j+1]);blc[j]=str(value)
    assert all(v>0 for v in S.Poly(S.expand(value.subs(m,t+1)),t).all_coeffs())
# The stronger h=1 actual deletion/FKG constraint fails, independent of T.
mu=c/r-1
assert mu==F(27,20) and mu>s
varx=r-r*r; vary=E(lambda x,y:y*y)-s*s
assert r*(r+1)-varx==F(1,50)
assert cov-varx==F(41,800)
record={'law':{str(k):str(v) for k,v in law.items()},'r':str(r),'s':str(s),'EXY':str(c),'cov':str(cov),'target_violation':str(cov-r*(r+1)),'qx':list(map(str,qx)),'qy':list(map(str,qy)),'Mx':list(map(str,mx)),'My':list(map(str,my)),'My_LC':list(map(str,lc(my))),'a':list(map(str,a)),'b':list(map(str,b)),'b_LC':list(map(str,lc(b))),'B':list(map(str,B)),'JC':[str(v) for v in (w,u,d,v,u*d-w*v)],'JC_m':str(P),'JC_m_shift_coefficients':[str(v) for v in S.Poly(S.expand(P.subs(m,t+1)),t).all_coeffs()],'last_marker_LC':blc,'mu':str(mu),'varY':str(vary),'controls':1,'all_m_proof':'Exact polynomial identity; all coefficients after m=1+t strictly positive.'}
(ROOT/'verification.json').write_text(json.dumps(record,indent=2,ensure_ascii=False))
print('PASS: one abstract ordered law; all exact finite values checked.')
print('PASS: all m>=1 JC_m and last-marker LC certified by positive m-1 coefficients.')
print('PASS: target violated by',cov-r*(r+1),'; independent singleton actual constraint fails.')
print(json.dumps(record,indent=2,ensure_ascii=False))
