"""Small exact verification, no poset search and no chain-length sweep."""
from fractions import Fraction
from interval_solver import (positive_intervals, external_length_intervals,
                             radical_floor_ceil, window_counts, evaluate,
                             threshold_polynomials, merge, external_balanced_cover)

# Root/degree/strict-endpoint cases. These are algebraic unit tests, not posets.
CASES = [
    ((0,0,0), []), ((0,0,1), [(1,None)]), ((0,0,-1), []),
    ((0,1,-1), [(2,None)]), ((0,-1,2), [(1,1)]),
    ((1,-4,4), [(1,1),(3,None)]), ((-1,4,-4), []),
    ((1,0,-2), [(2,None)]), ((-1,0,2), [(1,1)]),
    ((1,-5,6), [(1,1),(4,None)]), ((-1,6,-8), [(3,3)]),
    ((4,-12,9), [(1,None)]), ((-25,75,-54), []),
    ((1,0,1), [(1,None)]), ((-1,0,-1), []),
]
for poly, expected in CASES:
    actual = positive_intervals(*poly)
    assert actual == expected, (poly, actual, expected)
assert merge([(1,None),(1,2)]) == [(1,None)]
assert radical_floor_ceil(-10, -1, 2, 6) == (-2,-1)
assert radical_floor_ceil(-10, 1, 2, 6) == (-2,-1)
assert radical_floor_ceil(-2, 1, 4, 2) == (0,0)
assert positive_intervals(1,-4,4,upper=2) == [(1,1)]
assert positive_intervals(0,0,1,upper=0) == []


def isolated_z_example(d, j):
    # D=0<...<d-1, D<y=d; z=d+1 is isolated; U empty.
    n = d + 2
    pred = [0]*n
    for x in range(d):
        pred[x] = (1 << x)-1
    pred[d] = (1 << d)-1
    partition = (set(range(d)), {d,d+1}, set())
    total = window_counts(n,pred,*partition)
    event = window_counts(n,pred,*partition,event=(j-1,d+1))
    assert total == (0,d,2)
    assert event == (0,d-j,2)
    return total,event

# The existing actual strict-boundary example: m=2 safe, k=1 hits 2/3.
total,event = isolated_z_example(3,2)
assert external_length_intervals(total,{'d2<z':event})[0] == [(2,None)]
assert external_length_intervals(total,{'d2<z':event},current=2)[0] == []
assert external_balanced_cover(total,{'d2<z':event},current=2)[0] == [(1,1)]
assert Fraction(1+3,1+5) == Fraction(2,3)
assert Fraction(2+3,2+5) == Fraction(5,7)

# Actual direct side switch: k=1 low, m=13 high; no safe intermediate.
total,event = isolated_z_example(7,7)
assert external_length_intervals(total,{'d7<z':event})[0] == [(1,1),(13,None)]
assert external_length_intervals(total,{'d7<z':event},current=13)[0] == [(1,1)]
assert external_length_intervals(total,{'d7<z':event},current=13,
                                 preserve_side=True)[0] == []
assert external_balanced_cover(total,{'d7<z':event},current=13)[0] == [(2,12)]
assert Fraction(1+2,1+9) == Fraction(3,10)
assert Fraction(13+2,13+9) == Fraction(15,22)
# This huge-domain test performs the same fixed number of quadratic operations.
assert external_length_intervals(total,{'d7<z':event},current=10**100)[0] == [
    (1,1),(13,10**100-1)]

# Comparable y<z is counted once in the K=2 fiber, with no extra factor two.
pred = [0,1]
assert window_counts(2,pred,set(),{0,1},set()) == (0,0,1)
assert window_counts(2,pred,set(),{0,1},set(),event=(0,1)) == (0,0,1)
assert window_counts(2,pred,set(),{0,1},set(),event=(1,0)) == (0,0,0)
assert external_length_intervals((0,0,1),{'y<z':(0,0,1),'z<y':(0,0,0)})[0] == [(1,None)]

# An actual identically 1/3 external pair: D has a<b and isolated x,
# and every D-point is below both y,z; I={y,z}, U empty.
# For E=(x<a), exactly one of D's three extensions realizes E.
pred = [0,1,0,7,7]
total = window_counts(5,pred,{0,1,2},{3,4},set())
event = window_counts(5,pred,{0,1,2},{3,4},set(),event=(2,0))
assert total == (0,0,6) and event == (0,0,2)
low,high = threshold_polynomials(total,event)
assert low == (0,0,0)
assert external_length_intervals(total,{'x<a':event})[0] == []

# General-t counting (not a chain-column preservation claim).
assert window_counts(3,[0,0,0],set(),{0,1,2},set()) == (0,0,0,6)
assert window_counts(3,[0,0,0],set(),{0,1,2},set(),event=(0,1)) == (0,0,0,3)
print('PASS: 15 degree/root tests; exact DP for 5 explicit posets; boundary, side switch, comparable pair, identically-zero threshold; general-t fiber count.')
