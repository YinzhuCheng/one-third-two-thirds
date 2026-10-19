"""Small fixed independent endpoint controls; no parameter or poset search."""
import importlib.util
import json
from pathlib import Path

root = Path(__file__).resolve().parent
producer = root.parent / 'external-pair-length-intervals-20261018' / 'interval_solver.py'
spec = importlib.util.spec_from_file_location('producer_interval_solver', producer)
p = importlib.util.module_from_spec(spec)
spec.loader.exec_module(p)

# Expected integer intervals were derived directly, independently of the solver.
cases = [
    ((1,-4,3), [(4,None)]),             # integer simple roots 1,3
    ((-1,4,-3), [(2,2)]),              # strict interior of integer roots
    ((1,-2,1), [(2,None)]),            # excluded repeated integer root
    ((-1,2,-1), []),                   # negative square
    ((4,-4,1), [(1,None)]),            # repeated noninteger root
    ((1,0,-2), [(2,None)]),            # positive irrational root
    ((-1,0,2), [(1,1)]),
    ((-1,5,-5), [(2,3)]),              # two positive irrational roots
    ((1,0,1), [(1,None)]),             # no real roots, positive
    ((-1,0,-1), []),                   # no real roots, negative
    ((0,1,-1), [(2,None)]),            # positive linear, integer root
    ((0,-1,2), [(1,1)]),               # negative linear, strict endpoint
    ((0,0,0), []),                    # zero polynomial
    ((0,0,1), [(1,None)]),
    ((0,0,-1), []),
    ((4,-4,-1), [(2,None)]),
    ((1,-6,8), [(1,1),(5,None)]),       # two safe components
]
for coeffs, expected in cases:
    actual = p.positive_intervals(*coeffs)
    assert actual == expected, (coeffs, expected, actual)

assert p.positive_intervals(1,-6,8,upper=4)==[(1,1)]
assert p.positive_intervals(1,0,1,upper=0)==[]
assert p.merge([(4,None),(1,1),(2,3)])==[(1,None)]
assert p.merge([(1,2),(4,5)])==[(1,2),(4,5)]
assert p.intersect([(1,3),(8,None)],[(2,9)])==[(2,3),(8,9)]
assert p.intersect([],[(1,None)])==[]
assert p.external_length_intervals((0,3,2),{},current=1)[0]==[]
assert p.external_length_intervals((0,3,2),{},current=8)[0]==[(1,7)]

# Actual two-neighbor control coefficients specified by the producer.  The
# expected outputs follow from direct factorization of the threshold polynomials.
full, detail=p.external_length_intervals((0,3,2),{'E':(0,1,2)})
assert full==[(2,None)], (full,detail)
assert p.external_length_intervals((0,3,2),{'E':(0,1,2)},current=2)[0]==[]
full, detail=p.external_length_intervals((0,7,2),{'E':(0,0,2)})
assert full==[(1,1),(13,None)], (full,detail)
assert p.external_length_intervals((0,7,2),{'E':(0,0,2)},current=13)[0]==[(1,1)]
assert p.external_length_intervals((0,7,2),{'E':(0,0,2)},current=13,preserve_side=True)[0]==[]

# Fixed empty-boundary and highest-fiber controls for the actual-window DP.
assert p.window_counts(0,[],set(),set(),set()) == (1,)
assert p.window_counts(2,[0,1],{0},set(),{1}) == (1,)
assert p.window_counts(2,[0,0],set(),{0,1},set()) == (0,0,2)
assert p.window_counts(2,[0,1],set(),{0,1},set()) == (0,0,1)
# D and U are nonempty antichains, I is a two-point chain; only K=t is
# possible.  a_t=e(D)e(I)e(U)=2*1*2=4.
pred=[0,0,3,7,15,15]
assert p.window_counts(6,pred,{0,1},{2,3},{4,5}) == (0,0,4)
assert p.window_counts(6,pred,{0,1},{2,3},{4,5},event=(0,1)) == (0,0,2)

# Closed-balanced coverage: strict endpoint roots must remain included.
assert p.external_balanced_cover((0,3,2),{'E':(0,1,2)},current=2)[0] == [(1,1)]
assert p.external_balanced_cover((0,7,2),{'E':(0,0,2)},current=13)[0] == [(2,12)]
assert p.external_balanced_cover((0,0,6),{'E':(0,0,2)},current=9)[0] == [(1,8)]
assert p.external_balanced_cover((0,3,2),{},current=8)[0] == []
assert p.external_balanced_cover((0,3,2),{'E':(0,1,2)},current=1)[0] == []

report={
    'status':'PASS',
    'fixed_quadratic_linear_constant_cases':len(cases),
    'extra_boundary_union_intersection_controls':8,
    'actual_two_neighbor_coefficient_controls':2,
    'fixed_empty_boundary_highest_fiber_dp_controls':6,
    'closed_balanced_cover_controls':5,
    'scope':'Fixed endpoint controls only; no enumeration over chain lengths or posets.'
}
(root/'fixed_boundary_checks.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(report,ensure_ascii=False,indent=2))
