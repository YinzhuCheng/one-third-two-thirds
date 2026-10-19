"""Pure algebra controls for the one-round direction-cone audit; no poset search."""
from pathlib import Path
import json
import sympy as S

a,b,c,k,m,r0,r1,r2=S.symbols('a b c k m r0 r1 r2', positive=True)
T=lambda s:a+b*(s+1)+c*(s+1)*(s+2)/2
q=lambda s:[a/T(s),b*(s+1)/T(s),c*(s+1)*(s+2)/(2*T(s))]
qk,qm=q(k),q(m)
A=qk[0]-qm[0];B=qm[2]-qk[2]
theta=c*(a*(m+k+3)+b*(m+1)*(k+1))/(a*(2*b+c*(m+k+3)))
checks={
 'positive_A_formula':S.factor(A-a*(m-k)*(2*b+c*(m+k+3))/(2*T(k)*T(m))),
 'positive_B_formula':S.factor(B-c*(m-k)*(a*(m+k+3)+b*(m+1)*(k+1))/(2*T(k)*T(m))),
 'theta_equals_B_over_A':S.factor(B-A*theta),
 'direction_identity':S.factor(sum((qk[j]-qm[j])*r for j,r in enumerate([r0,r1,r2]))-A*((r0-r1)+theta*(r1-r2))),
 'theta_derivative':S.factor(S.diff(theta,k)-c*b*(2*a+2*b*(m+1)+c*(m+1)*(m+2))/(a*(2*b+c*(m+k+3))**2)),
}
assert all(v==0 for v in checks.values())
out={'checks':'PASS','zero_residuals':{k:str(v) for k,v in checks.items()},'status':'Pure identities only; cone sufficiency also reviewed in natural-language proof.'}
(Path(__file__).parent/'direction_identities.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(out,ensure_ascii=False,indent=2))
