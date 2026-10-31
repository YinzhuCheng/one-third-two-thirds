import sympy as s, json, time
q,y,E,t,a,g,b=s.symbols('q y E t a g b', nonnegative=True)
J=(y+g)*(t-2*y)+(y*y+E*E)/2+E*g
K=(y+a)*q-(y*y+E*E)/2-E*a
inner=s.integrate(s.expand((t-q)*(q*t-E*E)*K),(q,y,t))
mid=s.integrate(s.expand((y-E)*J*inner/2),(E,0,y))
positive=s.factor(s.integrate(s.expand(mid),(y,0,t)))
print('POSITIVE',positive,flush=True)
expected=t**9*(2750*a*g+3608*a*t-550*g*t+929*t*t)/s.factorial(11)
assert s.expand(positive-expected)==0
# c1 latest: a=g=0, E below0 spans b; r=y, K=y*q-y²/2, J=y*t-3y²/2.
J0=y*t-s.Rational(3,2)*y*y
K0=y*q-y*y/2
low=s.factor(s.integrate(s.expand(y*J0*s.integrate(s.expand((t-q)*q*t*K0/2),(q,y,t))),(y,0,t)))
print('C-LATEST',s.factor(positive.subs({a:0,g:0})+b*low),flush=True)
assert s.expand(low-t**10*4950/s.factorial(11))==0
# b latest, E<0, J independent E, with s0=-g and b=0.
Jb=s.expand((y+g)*(t-2*y)+y*y/2) # -g²/2+g²/2 cancels
# E <= c=-a: r=y+a, K=(y+a)q-(y²-a²)/2.
Kb0=(y+a)*q-(y*y-a*a)/2
f0=s.expand((y+a)*Jb*s.integrate(s.expand((t-q)*q*t*Kb0/2),(q,y,t)))
# E >= c=-a: r=y-E, K=(y+a)q-(y²+E²)/2-Ea.
f1=s.expand((y-E)*Jb*s.integrate(s.expand((t-q)*q*t*K/2),(q,y,t)))
# case d=-b <= c=-a (b>=a): E -b..-a then -a..0.
neg1=s.integrate(s.expand((b-a)*f0+s.integrate(f1,(E,-a,0))),(y,0,t))
res1=s.factor(positive+neg1)
print('B-LATEST d<c RAW',res1,flush=True)
# case c=-a <= d=-b: only E -b..0.
neg2=s.integrate(s.expand(s.integrate(f1,(E,-b,0))),(y,0,t))
res2=s.factor(positive+neg2)
print('B-LATEST c<d RAW',res2,flush=True)
x,z,w=s.symbols('x z w',nonnegative=True)
print('B-LATEST d<c POS',s.factor(res1.subs({g:a,b:a+x})),flush=True)
print('B-LATEST c<d POS',s.factor(res2.subs({a:b+x+z,g:b+x})),flush=True)

A=221760*b**3+194040*b*b*t+15840*b*t*t+2750*t**3
B0=360360*b**4+434280*b**3*t+112860*b*b*t*t+22330*b*t**3+3058*t**4
C0=138600*b**5+219450*b**4*t+89760*b**3*t*t+28985*b*b*t**3+8008*b*t**4+929*t**5
D0=221760*b**4+249480*b**3*t+85140*b*b*t*t+27500*b*t**3+3608*t**4
E0=332640*b**4+443520*b**3*t+156420*b*b*t*t+35640*b*t**3+4950*t**4
assert s.expand(res2.subs({a:b+x+z,g:b+x})-t**6*(C0+x*B0+x*x*A+z*(D0+x*A))/s.factorial(11))==0
assert s.expand(res1.subs({g:a,b:a+x})-t**6*(C0+x*E0).subs(b,a)/s.factorial(11))==0
print('All direct analytic integral identities passed; no linear extensions enumerated.')

R=t**6*(b*(15840*a*g*t*t+24750*a*t**3-7920*g*t**3+4950*t**4)+b*b*(194040*a*g*t+69300*a*t*t+11880*g*t*t+9405*t**3)+b**3*(221760*a*g+55440*a*t-9240*g*t-7260*t*t)-b**4*(83160*g+20790*t))/s.factorial(11)
L=t**6*(332640*a**3*g+83160*a**3*t+360360*a*a*g*t+116820*a*a*t*t+39600*a*g*t*t+43560*a*t**3-7920*g*t**3+4950*t**4)/s.factorial(11)
assert s.expand(neg2-R)==0
assert s.expand(neg1-(R.subs(b,a)+(b-a)*L))==0
print('Paper-certificate R and L identities also passed.')
