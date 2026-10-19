"""Symbolic identities only; no poset/extension enumeration."""
from fractions import Fraction
import sympy as sp

p, r, q, s, M, N, m, i = sp.symbols('p r q s M N m i')
h = sp.symbols('h', positive=True)
a = h*(M+N+p*s+q*r)
b = h*(p+q+r+s)
c = 2*h
u = h*(M+p*s+r+s+1)
v = h*(p+1)
w = h*(N+q*r+r+s+1)
x = h*(q+1)
T = lambda j: a+b*(j+1)+c*(j+1)*(j+2)/2
D = lambda j, aa, bb: c*bb*(j+1)*(j+2)/2+c*aa*(j+2)+b*aa-a*bb
f = lambda j: 1-(u+v*(j+1))/T(j)
g = lambda j: (w+x*(j+1))/T(j)
assert sp.simplify((f(m+1)-f(m))*T(m)*T(m+1)-D(m,u,v)) == 0
assert sp.simplify((g(m+1)-g(m))*T(m)*T(m+1)+D(m,w,x)) == 0
assert sp.simplify(D(m+1,u,v)-D(m,u,v)-c*(v*(m+2)+u)) == 0
F = (M+p*s+r+s+1)*(p+q+r+s+6)+(p+1)*(6-M-N-p*s-q*r)
B = (p+1)*((r+s)**2+q*s+6*(r+s)+7-N)
assert sp.expand(F-B-(M-p*r+1)*(q+r+s+5)) == 0
assert sp.simplify(D(1,u,v)/h**2-F) == 0
Fdual = F.xreplace({p:q,r:s,q:p,s:r,M:N,N:M})
assert sp.simplify(D(1,w,x)/h**2-Fdual) == 0
assert sp.expand(B.subs(N,q*s+s*s+2*s)-(p+1)*(r*r+2*r*s+6*r+4*s+7)) == 0

t = T(m)/h
full = lambda j: (N+q*r+q*(m+1)+(m-j+1)*(r+s+m+2))/t
assert sp.simplify(full(1)-f(m)) == 0
assert sp.simplify(full(m)-g(m)) == 0
assert sp.simplify(full(i)-full(i+1)-(r+s+m+2)/t) == 0
assert sp.simplify(t-(m+1)*(r+s+m+2)-(M+N+p*s+q*r+(p+q)*(m+1))) == 0

external = lambda j: 1-Fraction(2,j+5)
assert external(2) == Fraction(5,7)
assert external(1) == Fraction(2,3)
print('All symbolic endpoint, duality, full-column, and boundary-fraction identities passed.')
