import sympy as S
L,s,t=S.symbols('L s t', real=True)
x=1-L
ks=(x*x-s*s)/2
kt=(x*x-t*t)/2
integrand=2*L*ks*kt+L*L/2*(ks*(x-t)+kt*(x-s))
f=S.factor(S.integrate(integrand,(L,0,1-t))) # s<=t
print('f(s,t), s<=t:',f)
f00=f.subs({s:0,t:0})
ds=S.diff(f,s).subs({s:0,t:0});dt=S.diff(f,t).subs({s:0,t:0});dst=S.diff(f,s,t).subs({s:0,t:0})
print('f00,fs00,ft00,fst00:',f00,ds,dt,dst)
e=S.Rational(1,100)
f01=f.subs({s:0,t:e});f11=f.subs({s:e,t:e})
print('epsilon='+str(e)+'; f(0,epsilon),f(epsilon,epsilon):',f01,f11)
print('MTP determinant f00*f11-f01^2:',S.factor(f00*f11-f01*f01))
# strictly positive interior rectangle (e,2e)^2
f10=f.subs({s:e,t:e});f12=f.subs({s:e,t:2*e});f22=f.subs({s:2*e,t:2*e})
print('f(epsilon,epsilon),f(epsilon,2epsilon),f(2epsilon,2epsilon):',f10,f12,f22)
print('interior MTP determinant:',S.factor(f10*f22-f12*f12))
# all derivatives near origin and exact defect epsilon formula
z=S.symbols('z',real=True)
print('origin defect polynomial:',S.factor(f00*f.subs({s:z,t:z})-f.subs({s:0,t:z})**2))
