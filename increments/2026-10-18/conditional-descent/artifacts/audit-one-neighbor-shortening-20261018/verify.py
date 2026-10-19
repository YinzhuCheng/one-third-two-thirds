#!/usr/bin/env python3
"""Independent, fully labelled exhaustive check for m=2,3.

Uses only predecessor sets and generic topological-sort enumeration; does not
assume the counting factorization being audited. Run --dump to print every
full linear extension (40+35+77+70=222 orders).
"""
from fractions import Fraction
from itertools import combinations
import argparse


def make_poset(m, k):
    a = tuple(f'a{i}' for i in range(1, 2*m+1))
    c = tuple(f'c{i}' for i in range(1, k+1))
    vertices = a + ('z',) + c + ('y',)
    relations = {(a[i], a[j]) for i in range(len(a)) for j in range(i+1, len(a))}
    relations |= {(c[i], c[j]) for i in range(len(c)) for j in range(i+1, len(c))}
    relations |= {(d, ci) for d in a+('z',) for ci in c}
    return vertices, relations, a, c


def linear_extensions(vertices, relations):
    predecessors = {v: {x for x,y in relations if y == v} for v in vertices}
    def visit(prefix, remaining):
        if not remaining:
            yield tuple(prefix)
            return
        placed = set(prefix)
        for v in vertices:
            if v in remaining and predecessors[v] <= placed:
                yield from visit(prefix+[v], remaining-{v})
    return list(visit([], set(vertices)))


def probability(orders, x, y):
    return Fraction(sum(o.index(x) < o.index(y) for o in orders), len(orders))


def sign(x, y, relations):
    return -1 if (x,y) in relations else 1 if (y,x) in relations else 0


def autonomous(subset, vertices, relations):
    for x in set(vertices)-subset:
        if len({sign(x, c, relations) for c in subset}) != 1:
            return False
    return True


def chain(subset, relations):
    return all((x,y) in relations or (y,x) in relations for x,y in combinations(subset,2))


def audit(m, k, dump=False):
    vertices, relations, a, c = make_poset(m,k)
    orders = linear_extensions(vertices,relations)
    expected = (2*m+1)*(2*m+k+2)
    assert len(orders) == expected
    assert len(set(orders)) == expected
    for o in orders:
        assert set(o) == set(vertices) and len(o) == len(vertices)
        assert all(o.index(x) < o.index(y) for x,y in relations)
    assert autonomous(set(c),vertices,relations)
    outside = tuple(x for x in vertices if x not in c)
    for r in range(1,len(outside)+1):
        for extra in combinations(outside,r):
            s = set(c)|set(extra)
            assert not (chain(s,relations) and autonomous(s,vertices,relations))
    incomparable_to_entire_chain = [x for x in outside
        if all(sign(x,ci,relations)==0 for ci in c)]
    assert incomparable_to_entire_chain == ['y']
    q = [probability(orders,ci,'y') for ci in c]
    assert q == [Fraction(k+1-i,2*m+k+2) for i in range(1,k+1)]
    assert all(x < Fraction(1,3) for x in q)
    f_count = sum(o.index('y') < o.index(f'a{m}') for o in orders)
    assert f_count == 2*m*(m+1)
    p = Fraction(f_count,len(orders))
    if k == m:
        assert p < Fraction(1,3)
    else:
        assert Fraction(1,3) < p < Fraction(2,3)
    z_pair = probability(orders,'z',f'a{m}')
    assert z_pair == Fraction(m,2*m+1)
    assert Fraction(1,3) < z_pair < Fraction(1,2)
    balanced = [(x,y,probability(orders,x,y)) for x,y in combinations(vertices,2)
        if sign(x,y,relations)==0 and Fraction(1,3) <= probability(orders,x,y) <= Fraction(2,3)]
    delta = max(min(probability(orders,x,y),probability(orders,y,x))
        for x,y in combinations(vertices,2) if sign(x,y,relations)==0)
    print(f'm={m}, chain_length={k}, n={len(vertices)}, LE={len(orders)}, F_count={f_count}, P(F)={p}, q={q}, P(z<a_m)={z_pair}, delta={delta}')
    print('  balanced pairs: '+', '.join(f'{x}<{y}: {p}' for x,y,p in balanced))
    if dump:
        for i,o in enumerate(orders,1):
            print(f'  {i:03d}: '+ ' < '.join(o))
    return orders


def audit_external(m):
    vertices, relations, a, c = make_poset(m,m)
    qv = tuple(x for x in vertices if x not in c)
    qr = {(x,y) for x,y in relations if x in qv and y in qv}
    orders = linear_extensions(qv,qr)
    d = set(a)|{'z'}
    C0 = sum(o.index('y') > max(o.index(x) for x in d) for o in orders)
    A = len(orders)-C0
    C_F = sum(o.index('y') > max(o.index(x) for x in d) and o.index('y') < o.index(f'a{m}') for o in orders)
    assert A == (2*m+1)**2
    assert C0 == 2*m+1
    assert C_F == 0
    print(f'm={m}, external_LE={len(orders)}, A={A}, B=0, C0={C0}, C_F={C_F}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--dump',action='store_true')
    args = parser.parse_args()
    for m in (2,3):
        audit_external(m)
        audit(m,m,args.dump)
        audit(m,m-1,args.dump)
    print('PASS: all labelled linear extensions and all claimed identities verified.')
