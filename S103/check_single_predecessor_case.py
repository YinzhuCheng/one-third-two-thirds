#!/usr/bin/env python3
"""Exact algebra audit for the k<=3 path inequality and an abstract k=4 obstruction."""
from fractions import Fraction
import sympy as s
for k in range(1,4):
    m=s.symbols('m0:'+str(k+1), positive=True)
    S=sum(m)
    B=s.diag(*[s.Integer((j+1)*(j+2)//2)*m[j]*S for j in range(k)])
    for a in range(k+1):
        for b in range(a+1,k+1):
            v=s.Matrix([int(a<=j<b) for j in range(k)])
            B-=m[a]*m[b]*v*v.T
    assert s.expand(B[0,0]-m[0]**2)==0
    if k==2:
        assert s.expand(B.det()-m[0]**2*S*(3*m[1]-m[2]))==0
    if k==3:
        assert s.expand(B[:2,:2].det()-m[0]**2*S*(3*m[1]-m[2]-m[3]))==0
        T=18*m[1]*m[2]-3*m[1]*m[3]-6*m[2]**2-5*m[2]*m[3]
        assert s.expand(B.det()-m[0]**2*S*S*T)==0
    print('k=',k,'principal minors:',[s.factor(B[:j,:j].det()) for j in range(1,k+1)])
m=[104,103,102,101,100];t=[45,15,5,0,0]
mean=Fraction(sum(x*y for x,y in zip(m,t)),sum(m))
variance=sum(x*(y-mean)**2 for x,y in zip(m,t))
energy=sum(Fraction((j+1)*(j+2),2)*m[j]*(t[j]-t[j+1])**2 for j in range(4))
assert variance==Fraction(5011035,34)
assert energy==139800
assert variance-energy==Fraction(257835,34)
print('abstract k=4 obstruction:',mean,variance,energy,variance-energy)
print('PASS: symbolic identities only; no assertion of the unrestricted candidate.')
