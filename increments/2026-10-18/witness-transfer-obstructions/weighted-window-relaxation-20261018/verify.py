#!/usr/bin/env python3
"""Exact check of one prescribed weighted model; no search and no external IO."""
from collections import defaultdict
from fractions import Fraction as F
from itertools import combinations, permutations

R = ('u', 'v', 'y')
EXT = list(permutations(R))

def extensions(m):
    C = tuple(f'c{i}' for i in range(1, m + 1))
    labels = R + C
    edges = [(d, c) for d in ('u', 'v') for c in C]
    edges += list(zip(C, C[1:]))
    return [p for p in permutations(labels)
            if all(p.index(a) < p.index(b) for a, b in edges)]

def external(p):
    return tuple(x for x in p if x in R)

def law(m, eps=None):
    w = dict.fromkeys(EXT, F(1) if eps is None else F(eps))
    if eps is not None:
        w.update({('y', 'u', 'v'): F(38),
                  ('y', 'v', 'u'): F(32),
                  ('u', 'v', 'y'): F(10)})
    data = [(p, w[external(p)]) for p in extensions(m)]
    Z = sum((w for _, w in data), F(0))
    return data, Z

def before(data, Z, a, b):
    return sum((w for p, w in data if p.index(a) < p.index(b)), F(0)) / Z

def rows(m, eps):
    data, Z = law(m, eps)
    return {(a, b): before(data, Z, a, b)
            for a, b in combinations(R + tuple(f'c{i}' for i in range(1, m+1)), 2)}

for m in (2, 1):
    fibers = defaultdict(list)
    for p in extensions(m):
        fibers[external(p)].append(p)
    assert len(extensions(m)) == (10 if m == 2 else 8)
    for s in EXT:
        assert len(fibers[s]) == (m + 1 if s[-1] == 'y' else 1)
    print(f'm={m}: external fiber sizes', {''.join(s): len(fibers[s]) for s in EXT})

for eps in (F(0), F(1, 10)):
    d2, Z2 = law(2, eps)
    d1, Z1 = law(1, eps)
    assert Z2 == 100 + 5 * eps and Z1 == 90 + 4 * eps
    assert before(d2, Z2, 'v', 'u') == (32 + 4 * eps) / Z2
    assert before(d1, Z1, 'v', 'u') == (32 + 3 * eps) / Z1
    for d in ('u', 'v'):
        assert before(d2, Z2, d, 'y') == (30 + 4 * eps) / Z2
        assert before(d1, Z1, d, 'y') == (20 + 3 * eps) / Z1
    assert before(d2, Z2, 'c1', 'y') == (20 + 2 * eps) / Z2
    assert before(d2, Z2, 'c2', 'y') == (10 + eps) / Z2
    assert before(d1, Z1, 'c1', 'y') == (10 + eps) / Z1
    old = [before(d2, Z2, a, b) for a, b in
           [('v','u'), ('u','y'), ('v','y'), ('c1','y'), ('c2','y')]]
    beta2 = max(min(p, 1-p) for p in old)
    q = before(d1, Z1, 'v', 'u')
    assert all(min(p, 1-p) < F(1, 3) for p in old)
    assert F(1, 3) <= q <= F(2, 3)
    assert beta2 == (32 + 4 * eps) / Z2
    if eps:
        assert all(w > 0 for _, w in d2 + d1)
    print(f'\nepsilon={eps}; Z2={Z2}; Z1={Z1}; beta2={beta2}; v<u after={q}')
    for m in (2, 1):
        print(f'all label-pair probabilities, m={m}:')
        for (a, b), p in rows(m, eps).items():
            print(f'  {a}<{b}: {p}; reverse: {1-p}; minority: {min(p,1-p)}')

# Averaging the two rank deletions is a different law from the target law.
d2, Z2 = law(2, F(0))
push = defaultdict(F)
for p, w in d2:
    for removed in ('c1', 'c2'):
        q = tuple('c1' if x in ('c1','c2') else x for x in p if x != removed)
        push[q] += w / 2
assert sum(push.values()) == Z2
assert sorted(w for w in push.values() if w > 0) == list(map(F, [15,15,32,38]))
assert before(list(push.items()), Z2, 'v', 'u') == F(8,25)
assert before(law(1, F(0))[0], F(90), 'v', 'u') == F(16,45)

# The actual uniform laws of these posets have u,v balanced already.
for m in (2, 1):
    data, Z = law(m, None)
    assert before(data, Z, 'u', 'v') == F(1, 2)
    print(f'actual uniform m={m}: Z={Z}; u<v=1/2')

beta, rav = F(8,25), F(3,2)
threshold = (1-beta)/(2*beta)
odds_bound = rav*beta/(1-beta+rav*beta)
assert threshold == F(17,16) and rav > threshold
assert odds_bound == F(12,29) and F(16,45) <= odds_bound
print(f'\nslack check: beta={beta}; R_av={rav}; threshold={threshold}; odds bound={odds_bound}')
print('All exact assertions passed. This certifies only the prescribed weighted relaxation.')
