from fractions import Fraction as Q
from math import comb
import sympy as s
for R in range(1,7):
 for mode in ('quadratic','geometric','mixed'):
  a=[Q(comb(j+2,2)) for j in range(R+1)];f=[sum(a[:j+1]) for j in range(R+1)]
  E=[Q((R-j+2)*(R-j+1)) for j in range(R+1)] if mode=='quadratic' else [Q(1,2**j) for j in range(R+1)]
  if mode=='mixed':E=[Q(1,2**j)*Q(1,3**max(0,j-2)**2) for j in range(R+1)]
  E+=[Q(0),Q(0)];pi=[f[j]*E[j] for j in range(R+1)];rho=[pi[j+1]/pi[j] for j in range(R)]+[Q(0)]
  omega=[pi[j+1] for j in range(R)];D=s.zeros(R,R+1);L=s.zeros(R+1,R+1);A=s.zeros(R)
  for j in range(R):
   D[j,j]=-1;D[j,j+1]=1
   L[j,j]+=rho[j];L[j,j+1]-=rho[j];L[j+1,j+1]+=1;L[j+1,j]-=1
   A[j,j]=1+rho[j]
   if j>0:A[j,j-1]=-1
   if j<R-1:A[j,j+1]=-rho[j+1]
  assert D*L==A*D
  Om=s.diag(*omega);P=s.diag(*pi)
  assert P*L==D.T*Om*D
  ground=s.zeros(R)
  for j in range(R-1):
   u=s.zeros(R,1);u[j]=-1;u[j+1]=1;ground+=omega[j]*rho[j+1]*u*u.T
  ground+=s.diag(*[omega[j]*(rho[j]-rho[j+1]+(j==0)) for j in range(R)])
  assert Om*A==ground
  for j in range(R):assert rho[j]>rho[j+1]
  r=[E[j+1]/E[j] for j in range(R+1)];v=s.Matrix([1-t for t in r]);K=-s.diag(*pi);constraints=[]
  for j in range(R):
   u=s.zeros(R+1,1);u[j]=-1;u[j+1]=1
   delta=E[j+1]**2-E[j]*E[j+2]
   if delta:
    lam=E[j+1]**2/delta
    assert lam>=rho[j]/(rho[j]-rho[j+1])
    K+=pi[j]*lam*u*u.T
   else:constraints.append(list(u))
  S=s.Matrix(constraints).nullspace() if constraints else [s.eye(R+1)[:,j] for j in range(R+1)]
  B=s.Matrix.hstack(*S)
  assert B.T*(K*v+s.Matrix([a[j]*E[j] for j in range(R+1)]))==s.zeros(B.cols,1)
  assert (v.T*K*v)[0]==-sum(a[j]*(E[j]-E[j+1]) for j in range(R+1))
  ortho=s.Matrix([[a[j]*E[j] for j in range(R+1)]])*B
  N=s.Matrix.hstack(*ortho.nullspace()) if ortho.nullspace() else s.zeros(B.cols,0)
  T=N.T*B.T*K*B*N
  for k in range(1,T.rows+1):assert T[:k,:k].det()>0
print('PASS: exact BL commutation/grounded-energy identity; all endpoints; strict and zero-Delta constrained Jacobi pairings and positive forms, R=1..6.')
