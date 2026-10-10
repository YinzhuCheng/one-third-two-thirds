#!/usr/bin/env python3
"""Exact checks of the path-spectral identities; finite checks are not the proof."""
import sympy as s
from fractions import Fraction as Q
for R in range(1,5):
 a=[s.Integer((j+1)*(j+2)//2) for j in range(R+1)]
 E=[s.Integer((R+2-j)*(R+1-j)) for j in range(R+1)]+[s.Integer(0)]
 f=[sum(a[:j+1]) for j in range(R+1)]
 d=s.Matrix([E[j]-E[j+1] for j in range(R+1)])
 F=s.zeros(R+1)
 w=[]
 for j in range(R):
  de=E[j+1]**2-E[j]*E[j+2]
  F[j,j]+=f[j]*E[j+2]/de
  F[j,j+1]-=f[j]*E[j+1]/de;F[j+1,j]-=f[j]*E[j+1]/de
  F[j+1,j+1]+=f[j]*E[j]/de
  w.append(f[j]*E[j+1]*d[j]*d[j+1]/de)
 F[R,R]-=f[R]/E[R]
 assert F*d==-s.Matrix(a)
 m=[a[j]*d[j] for j in range(R+1)]
 K=s.zeros(R+1)
 for j in range(R):
  K[j,j]+=w[j];K[j+1,j+1]+=w[j];K[j,j+1]-=w[j];K[j+1,j]-=w[j]
 assert s.diag(*d)*F*s.diag(*d)==K-s.diag(*m)
 L=s.diag(*[1/v for v in m])*K
 phi=s.Matrix([E[j]/d[j] for j in range(R+1)])
 assert L*phi==phi-s.Matrix([f[j]/a[j] for j in range(R+1)])
 D=s.zeros(R,R+1)
 for j in range(R):D[j,j]=1;D[j,j+1]=-1
 alpha=[w[j]/m[j] for j in range(R)]+[0]
 beta=[0]+[w[j-1]/m[j] for j in range(1,R+1)]
 A=s.zeros(R)
 for j in range(R):
  A[j,j]=alpha[j]+beta[j+1]
  if j:A[j,j-1]=-beta[j]
  if j<R-1:A[j,j+1]=-alpha[j+1]
 assert D*L==A*D
 assert s.diag(*w)*A==(s.diag(*w)*A).T
 g=list(s.symbols('g0:'+str(R+1)))+[0,0]
 x=s.Matrix([E[j+1]*g[j+1]-E[j]*g[j] for j in range(R+1)])
 c=[a[0]]+[a[j]-a[j-1] for j in range(1,R+1)]
 energy=sum(f[j]*E[j]*(g[j]-g[j+1])**2 for j in range(R))
 variance=sum(c[j]*E[j]*g[j]**2 for j in range(R+1))
 curvature=sum(f[j]*E[j+2]/(E[j+1]**2-E[j]*E[j+2])*(E[j]*(g[j+1]-g[j])-E[j+1]*(g[j+2]-g[j+1]))**2 for j in range(R))
 assert s.expand((x.T*F*x)[0]-energy+variance-curvature)==0
 print('R',R,'all exact matrix, gradient, and energy identities PASS')
print('Finite algebra checks only; refer to the general proof for validity at every R.')
