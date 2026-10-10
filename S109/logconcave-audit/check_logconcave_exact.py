#!/usr/bin/env python3
"""Exact rational regression tests, not a substitute for the accompanying proof."""
from fractions import Fraction as Q
import json, random
from pathlib import Path


def clip(poly, a, b, c):
    out = []
    if not poly:
        return out
    for p, q in zip(poly, poly[1:] + poly[:1]):
        dp, dq = a*p[0] + b*p[1] - c, a*q[0] + b*q[1] - c
        if dp <= 0:
            out.append(p)
        if (dp < 0 and dq > 0) or (dp > 0 and dq < 0):
            t = dp/(dp-dq)
            out.append((p[0]+t*(q[0]-p[0]), p[1]+t*(q[1]-p[1])))
    return out


def area(poly):
    return abs(sum((p[0]*q[1]-p[1]*q[0] for p,q in zip(poly,poly[1:]+poly[:1])), Q(0)))/2


def audit_polygon(constraints):
    # Strict positivity of some a and some b provides finite coordinate bounds.
    X = min(c/a for a,b,c in constraints if a)
    Y = min(c/b for a,b,c in constraints if b)
    poly = [(Q(0),Q(0)),(X,Q(0)),(X,Y),(Q(0),Y)]
    for a,b,c in constraints:
        poly = clip(poly,a,b,c)
    diagonal = min(c/(a+b) for a,b,c in constraints)
    H = diagonal*diagonal/2
    upper = area(clip(poly,Q(1),Q(-1),Q(0)))
    lower = area(clip(poly,Q(-1),Q(1),Q(0)))
    Ru,Ry = upper-H,lower-H
    delta = H*H-Ru*Ry
    assert area(poly)==upper+lower
    assert Ru>=0 and Ry>=0 and delta>=0, (constraints,H,Ru,Ry,delta)
    return H,Ru,Ry,delta


def run():
    rng = random.Random(109002)
    result = {}
    for name, n in [('uniform_downward_polygons',5000),('homogeneous_max_affine_exponentials',5000)]:
        eq = zero_wing = 0
        max_ratio = Q(0)
        for _ in range(n):
            if name == 'uniform_downward_polygons':
                constraints = [(Q(1),Q(0),Q(rng.randint(1,12))), (Q(0),Q(1),Q(rng.randint(1,12)))]
                constraints += [(Q(rng.randint(1,9)),Q(rng.randint(1,9)),Q(rng.randint(1,30))) for i in range(rng.randint(1,8))]
            else:
                constraints = [(Q(rng.randint(1,12)),Q(rng.randint(1,12)),Q(1)) for i in range(rng.randint(1,8))]
            H,Ru,Ry,delta = audit_polygon(constraints)
            # exp(-max(a_i*s+b_i*t)) multiplies all three masses by 2
            # relative to the indicator of its unit sublevel polygon.
            if name == 'homogeneous_max_affine_exponentials':
                H,Ru,Ry,delta = 2*H,2*Ru,2*Ry,4*delta
            eq += delta==0
            zero_wing += Ru==0 or Ry==0
            max_ratio = max(max_ratio,Ru*Ry/(H*H))
        result[name] = dict(cases=n,exact_equality_cases=eq,zero_wing_cases=zero_wing,maximum_RuRy_over_H2=str(max_ratio),counterexamples=0)
    # Product survival f=(1-s)^m_+(1-t)^n_+, supported on the unit square.
    count = 0
    for m in range(31):
        for n in range(31):
            H=Q(1,(m+n+1)*(m+n+2))
            Ru=Q(m,n+1)*H
            Ry=Q(n,m+1)*H
            assert H*H-Ru*Ry == H*H*Q(m+n+1,(m+1)*(n+1)) > 0
            count += 1
    result['polynomial_product_survivals'] = dict(cases=count,counterexamples=0,formula='RuRy/H^2 = mn/((m+1)(n+1))')
    result['nonhomogeneous_positive_affine_exact_witness'] = dict(f='exp(-max(2*s+t,s+2*t-1))',H='1/9',Ru='2/9-1/(6*e)',Ry='1/18',delta='1/(108*e)>0')
    result['seed']=109002
    path=Path(__file__).with_name('exact_checks.json')
    path.write_text(json.dumps(result,indent=2)+'\n')
    print(path.read_text())

if __name__=='__main__':
    run()
