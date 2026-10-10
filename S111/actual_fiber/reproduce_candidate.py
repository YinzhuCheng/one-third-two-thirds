#!/usr/bin/env python3
from fractions import Fraction
from test_exact_fiber_mtp2 import *
from pathlib import Path
from certify_small_mtp2 import poly,log_cross
m=6
# Omega labels a,b,v,w,r,s. P additionally has u,y, with common D={a,b},
# Uu={r}, Uy={s}.
out=closure(m,[(0,2),(1,3),(0,4),(1,4),(0,5),(1,5),(2,4),(3,5)])
pred=predecessors(out);exts=list(extensions(pred));C=rank_histogram(exts,3,16,32,m)
Q=100
vals={str((i,j)):Fraction(sum(c*kernel(m,p,q,i,j,Q) for (p,q),c in C.items()),math.factorial(m)*Q**m) for i,j in [(0,0),(1,0),(0,1),(1,1)]}
det=vals['(0, 0)']*vals['(1, 1)']-vals['(0, 1)']*vals['(1, 0)']
counts=count_integrals(C);E,F,G,H=[counts[x] for x in ['E','F','G','H']]
R=dict(deletion_predecessors=pred,histogram=[[*pq,v] for pq,v in sorted(C.items())],deletion_extension_count=len(exts),fiber_values={k:str(v) for k,v in vals.items()},mtp2_determinant=str(det),integrals=counts,square_slack=E*H-F*G,dimension_sharp_slack=7*E*H-8*F*G,origin_homogeneous_cross_coefficient=log_cross(poly(C,m)).get((0,0,2*m-2),0))
assert det==Fraction(-24895078440973240401,6400000000000000000000000000)
assert counts==dict(E=200,F=100,G=100,H=74)
json.dump(R,open(Path(__file__).resolve().parent/'actual_mtp2_counter_audit.json','w'),indent=2)
print(json.dumps(R,indent=2))
