#!/usr/bin/env python3
"""Independent exact symbolic audit of the eight-cell L-counterexample family.
The eight-cell prefix argument is separately reviewed in the audit text.
"""
from pathlib import Path
from math import comb
from fractions import Fraction
import hashlib, json
import sympy as s
HERE=Path(__file__).resolve().parent
u0,u1,u2,u3=s.symbols('U0 U1 U2 U3')
v0,v1,v2=u0-u1,u1-u2,u2-u3
# Direct transcription of the independently derived legal-prefix cell counts.
rows=[(0,0,u0+u1,u0,v0),(0,1,u1,0,0),
      (1,0,u0,u0,v0),(1,1,2*u1,u1,0),(1,2,2*u2,u2,0),
      (2,0,v0,v0,v0),(2,1,3*v1,2*v1,v1),(2,2,5*v2,3*v2,v2)]
formula={
'E':s.expand(sum(row[2] for row in rows)),
'K_ax':s.expand(sum(w for i,j,w,a,b in rows if i>=1)),
'K_ay':s.expand(sum(row[3] for row in rows)),
'K_bx':s.expand(sum(w for i,j,w,a,b in rows if i==2)),
'K_by':s.expand(sum(row[4] for row in rows)),
'K_xy':s.expand(sum(w for i,j,w,a,b in rows if j==0)),
}
claimed_formula={
'E':3*u0+6*u1+4*u2-5*u3,
'K_ax':2*u0+4*u1+4*u2-5*u3,
'K_ay':3*u0+2*u1+2*u2-3*u3,
'K_bx':u0+2*u1+2*u2-5*u3,
'K_by':3*u0-2*u1-u3,
'K_xy':3*u0,
}
assert all(s.expand(formula[k]-v)==0 for k,v in claimed_formula.items())
assert s.expand(2*formula['K_bx']-formula['K_ax']) == -5*u3
assert s.expand(3*formula['K_bx']-formula['E']) == 2*u2-10*u3
assert s.expand(3*formula['K_by']-formula['E']-2*(3*formula['K_ay']-2*formula['E']))==0
r=s.symbols('r',integer=True,positive=True)
u=s.symbols('u',nonnegative=True)
t=5*r-6
# Derive U_j/U_3 by telescoping binomial ratios, then multiply by U_3/h.
base=(r-1)*r*(r+1)
ratio_to_U3={3:s.Integer(1)}
for j in (2,1,0):
    # U_j=C(N-1-j,M-1), N=5r-3, M=4r-4.
    # U_j/U_(j+1)=(N-1-j)/(N-M-j)=(5r-4-j)/(r+1-j).
    ratio_to_U3[j]=s.cancel(ratio_to_U3[j+1]*(5*r-4-j)/(r+1-j))
scaled_U={sym:s.cancel(base*ratio_to_U3[j]) for j,sym in enumerate((u0,u1,u2,u3))}
claim_U=[t*(t+1)*(t+2),(r+1)*t*(t+1),r*(r+1)*t,base]
assert all(s.expand(scaled_U[sym]-val)==0 for sym,val in zip((u0,u1,u2,u3),claim_U))
polys={k:s.expand(v.subs(scaled_U)) for k,v in formula.items()}
claimed_polys={
'E':540*r**3-1309*r**2+941*r-180,
'K_ax':365*r**3-874*r**2+621*r-120,
'K_ay':432*r**3-1187*r**2+1051*r-300,
'K_bx':(4*r-5)*(45*r**2-53*r+12),
'K_by':3*(r-1)*(4*r-5)*(27*r-28),
'K_xy':15*(r-1)*(5*r-6)*(5*r-4),
}
assert all(s.expand(polys[k]-v)==0 for k,v in claimed_polys.items())
slacks={
'ax_majority':3*polys['K_ax']-2*polys['E'],
'ay_majority':3*polys['K_ay']-2*polys['E'],
'xy_majority':3*polys['K_xy']-2*polys['E'],
'bx_lower_failure':3*polys['K_bx']-polys['E'],
'by_lower_rescue':3*polys['K_by']-polys['E'],
'by_upper_rescue':2*polys['E']-3*polys['K_by'],
}
claims={
'ax_majority':r*(r+1)*(15*r-19),
'ay_majority':216*r**3-943*r**2+1271*r-540,
'xy_majority':45*r**3-757*r**2+1448*r-720,
'bx_lower_failure':-2*r*(r+1),
'by_lower_rescue':2*(216*r**3-943*r**2+1271*r-540),
'by_upper_rescue':108*r**3+577*r**2-1601*r+900,
}
assert all(s.expand(slacks[k]-v)==0 for k,v in claims.items())
shifted={k:s.Poly(s.expand(v.subs(r,u+15)),u) for k,v in slacks.items()}
for k,poly in shifted.items():
    assert all(c<0 for c in poly.all_coeffs()) if k=='bx_lower_failure' else all(c>0 for c in poly.all_coeffs())
claimed_shifts={
'ay_majority':216*u**3+8777*u**2+118781*u+535350,
'xy_majority':45*u**3+1268*u**2+9113*u+2550,
'by_upper_rescue':108*u**3+5437*u**2+88609*u+471210,
}
assert all(s.expand(shifted[k].as_expr()-v)==0 for k,v in claimed_shifts.items())
# Direct binomial substitution verifies the general formulas at both stated examples.
examples=[]
for m,rv in [(13,3),(54,15)]:
    M,R=m+2,rv+1;N=M+R
    U=[comb(N-1-j,M-1) for j in range(4)]
    counts={k:int(v.subs(dict(zip((u0,u1,u2,u3),U)))) for k,v in formula.items()}
    examples.append({'m':m,'r':rv,'U':U,**counts})
assert list(examples[0][k] for k in ('E','K_ax','K_ay','K_bx','K_by','K_xy'))==[13665,9245,10735,4585,7805,9180]
assert list(examples[1][k] for k in ('E','K_ax','K_ay','K_bx','K_by','K_xy'))==[14395164266463908,9750632308747096,11262772937084132,4796894339975628,8130381607704356,9604711718385252]
# For general m,r, U2/U3=(m+r)/(r-1), so the L-slack factor is correct.
m=s.symbols('m',integer=True,positive=True)
assert s.cancel(2*((m+r)/(r-1)-5)-2*(m-4*r+5)/(r-1))==0
result={'status':'PASS: eight-cell summations and all stated family polynomial identities',
        'reviewed_document_sha256':hashlib.sha256((HERE/'mc3_half_proof.txt').read_bytes()).hexdigest(),
        'scaled_count_polynomials':{k:str(s.factor(v)) for k,v in polys.items()},
        'shifted_slacks':{k:str(v.as_expr()) for k,v in shifted.items()},
        'all_shifted_coefficient_signs_verified':True,'direct_binomial_examples':examples}
(HERE/'L_family_symbolic_independent_audit.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
