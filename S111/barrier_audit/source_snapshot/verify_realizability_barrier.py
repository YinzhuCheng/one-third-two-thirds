#!/usr/bin/env python3
"""Exact finite certificate: positive mixtures of true n=7 fibers can fail
(n-1) E H >= n F G, even with integer rank-histogram and integral counts.
This is NOT a poset counterexample. No external writes or network calls.
"""
import itertools
from collections import Counter
from fractions import Fraction
import sympy as S

s,t=S.symbols('s t', real=True)
f1=(1-s)**2*(1-t)**3
f2=(1-s)*(1-t)**3
g=S.Rational(5,6)*f1+S.Rational(1,6)*f2

def integrals(f):
    F=S.integrate(f,(s,0,t),(t,0,1))
    G=S.integrate(f,(t,0,s),(s,0,1))
    H=S.integrate(t*f.subs(s,t),(t,0,1))
    E=F+G
    return dict(E=E,F=F,G=G,H=H,delta=S.factor(6*E*H-7*F*G))

def histogram(U,V):
    C=Counter()
    for seq in itertools.permutations(range(5)):
        C[min(seq.index(u)+1 for u in U),min(seq.index(v)+1 for v in V)]+=1
    return C

C1=histogram({0,1},{2,3,4})
C2=histogram({0},{2,3,4})
C={k:Fraction(5*C1[k]+C2[k],6) for k in C1.keys()|C2.keys()}
assert all(v.denominator==1 for v in C.values())
assert sum(C.values())==120
C={k:int(v) for k,v in C.items()}

counts=dict(E=0,F=0,G=0,H=0)
for (p,q),c in C.items():
    a=min(p,q);h=a*(a+1)//2
    F=h+p*(q-p) if p<=q else h
    G=h+q*(p-q) if q<=p else h
    for key,val in dict(E=F+G,F=F,G=G,H=h).items():counts[key]+=c*val
assert counts==dict(E=455,F=185,G=270,H=128)
assert 6*counts['E']*counts['H']-7*counts['F']*counts['G']==-210
assert all(S.factor(integrals(g)[k]*S.factorial(7)-v)==0 for k,v in counts.items())
# Positive simplex-Bernstein coefficients: homogeneous coordinates
# x=s, y=t-s, z=1-t, so 1-s=y+z and 1-t=z.
x,y,z=S.symbols('x y z', nonnegative=True)
P=(y+z)*(x+6*y+6*z)*z**3/S.Integer(6)
assert all(c>=0 for mon,c in S.Poly(P,x,y,z).terms())
assert S.factor(P.subs({x:s,y:t-s,z:1-t})-g)==0

print('f1 integrals:',integrals(f1))
print('f2 integrals:',integrals(f2))
print('g integrals:',integrals(g))
print('g rank histogram:',sorted(C.items()))
print('g integral counts:',counts)
print('g count delta:',6*counts['E']*counts['H']-7*counts['F']*counts['G'])
print('positive homogeneous sector polynomial:',S.expand(P))
print('PASS: all exact assertions; g is not a realizable fixed-poset fiber.')
