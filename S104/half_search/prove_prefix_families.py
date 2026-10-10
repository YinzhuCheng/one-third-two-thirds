"""Exact symbolic identities from the prefix proof, not interpolation."""
import sympy as s
from structural_family import counts
T=s.symbols('t',integer=True,positive=True)
def choose(n,k):return s.prod(n-j for j in range(k))/s.factorial(k)
H={(0,0):1,(0,1):1,(1,0):1,(1,1):2,(1,2):2,(2,0):1,(2,1):3,(2,2):5}
for r,threshold in [(3,10),(4,13)]:
 R={ij:choose(T+r+2-sum(ij),r-ij[1]) if ij[0] else (choose(T+r+2,r)-choose(T+r,r-2) if ij[1]==0 else choose(T+r,r-1)) for ij in H}
 E=s.factor(sum(H[z]*R[z] for z in H));Ax=s.factor(sum(H[z]*R[z] for z in H if z[0]>=1));Bx=s.factor(sum(H[z]*R[z] for z in H if z[0]>=2));Xy=s.factor(sum(H[z]*R[z] for z in H if z[1]==0));Ay=s.factor(choose(T+r+1,r)+R[1,0]+R[1,1]+R[1,2]+R[2,0]+2*R[2,1]+3*R[2,2]);By=s.factor(2*choose(T+r,r)+R[2,0]+R[2,1]+R[2,2])
 for t in range(1,101):
  e,k=counts(r,1,2,t)
  assert [int(f.subs(T,t)) for f in [E,Ax,Ay,Bx,By,Xy]]==[e]+k
 u=s.symbols('u')
 for f in [3*Ax-2*E,3*Ay-2*E,3*Xy-2*E]:assert all(c>0 for c in s.Poly(s.expand(f.subs(T,u+threshold)),u).all_coeffs())
 half=-5 if r==3 else -5*(T+2);lower=2*(T-3) if r==3 else (T-7)*(T+2)
 assert s.simplify(2*Bx-Ax-half)==0 and s.simplify(3*Bx-E-lower)==0
 print('r=',r,'all strict premises for t>=',threshold)
 for name,f in [('E',E),('Ax',Ax),('Ay',Ay),('Bx',Bx),('By',By),('Xy',Xy),('3Ax-2E',3*Ax-2*E),('3Ay-2E',3*Ay-2*E),('3Xy-2E',3*Xy-2*E),('2Bx-Ax',2*Bx-Ax),('3Bx-E',3*Bx-E)]:print(name,s.factor(f))
print('PASS: exact prefix formulas, identities, all-t premise proofs, and independent DP cross-checks t=1..100.')
