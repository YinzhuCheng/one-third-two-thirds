import sympy as S
p,q,r,s,M,N,m=S.symbols('p q r s M N m')
F=(M+p*s+r+s+1)*(p+q+r+s+6)+(p+1)*(6-M-N-p*s-q*r)
bridge=(p+1)*((r+s)**2+q*s+6*(r+s)+7-N)+(M-p*r+1)*(q+r+s+5)
assert S.expand(F-bridge)==0
A=M+N+p*s+q*r;B=p+q+r+s
Tm=A+B*(m+1)+(m+1)*(m+2)
u=M+p*s+r+s+1;v=p+1;w=N+q*r+r+s+1;x=q+1
first=1-(u+v*(m+1))/Tm;last=(w+x*(m+1))/Tm
Dm=lambda u,v: v*(m+1)*(m+2)+2*u*(m+2)+B*u-A*v
assert S.cancel(first.subs(m,m+1)-first-Dm(u,v)/(Tm*Tm.subs(m,m+1)))==0
assert S.cancel(last.subs(m,m+1)-last+Dm(w,x)/(Tm*Tm.subs(m,m+1)))==0
assert S.expand(Dm(u,v).subs(m,m+1)-Dm(u,v)-2*(v*(m+2)+u))==0
Q=lambda i:(N+q*r+q*(m+1)+(m-i+1)*(r+s+m+2))/Tm
i=S.symbols('i')
assert S.cancel(Q(1)-first)==0 and S.cancel(Q(m)-last)==0
assert S.cancel(Q(i)-Q(i+1)-(r+s+m+2)/Tm)==0
assert S.expand(Tm-(m+1)*(r+s+m+2)-(M+N+p*s+q*r+(p+q)*(m+1)))==0
print('Independent endpoint, bridge, all-m difference, and full-column identities passed.')
