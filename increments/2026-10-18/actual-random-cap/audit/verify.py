"""Four fixed actual-poset controls; no parameter or poset search."""
from collections import Counter
from fractions import Fraction as F
from itertools import combinations, permutations, product
from math import comb
import json
from pathlib import Path

OUT = Path(__file__).parent


def extensions(elements, edges):
    ans = []
    for word in permutations(elements):
        p = {x: i for i, x in enumerate(word)}
        if all(p[x] < p[y] for x, y in edges):
            ans.append(word)
    return ans


def check(label, W, E_W, V, E_V, S):
    a, b = len(W), len(V)
    EW, EV = extensions(W, E_W), extensions(V, E_V)
    EU = extensions(W + V, E_W + E_V)
    patterns = list(combinations(range(a + b), a))
    generated = []
    joint = Counter()
    samples = []
    for w, v, pos in product(EW, EV, patterns):
        positions = set(pos)
        wi, vi = iter(w), iter(v)
        u = tuple(next(wi) if i in positions else next(vi)
                  for i in range(a + b))
        generated.append(u)
        J = next(i for i, x in enumerate(u) if x in V)
        K = next((i for i, x in enumerate(w) if x in S), a)
        R = next(i for i, x in enumerate(u) if x in set(V) | S)
        T = next(i for i, x in enumerate(u) if x in V)
        assert (R, T) == (min(J, K), J)
        joint[J, K] += 1
        samples.append((R, T, J, K))
    assert len(generated) == len(set(generated)) == len(EU)
    assert set(generated) == set(EU)
    assert len(EU) == len(EW) * len(EV) * comb(a + b, a)
    m = len(samples)
    mean = lambda values: F(sum(values), m)
    r, s = mean([t[0] for t in samples]), mean([t[1] for t in samples])
    e2 = mean([t[0] ** 2 for t in samples])
    cov = mean([t[0] * t[1] for t in samples]) - r * s
    var = e2 - r * r
    g = r * (r + 1) - var
    margin = r * (r + 1) - cov
    jcounts = Counter(t[2] for t in samples)
    kcounts = Counter(t[3] for t in samples)
    for j, k in product(jcounts, kcounts):
        assert F(joint[j, k], m) == F(jcounts[j], m) * F(kcounts[k], m)
    tails = []
    for i in range(a + 1):
        p = F(sum(t[2] >= i for t in samples), m)
        q = F(sum(t[3] >= i for t in samples), m)
        h = F(sum(t[0] >= i for t in samples), m)
        assert p == F(comb(a + b - i, b), comb(a + b, b))
        assert h == p * q
        conditional_J = F(sum(t[2] for t in samples if t[2] >= i),
                          sum(t[2] >= i for t in samples))
        assert conditional_J == F(a + i * b, b + 1)
        tails.append(dict(i=i, p=p, q=q, h=h, conditional_J=conditional_J))
    assert s == F(a, b + 1)
    assert cov == F(b, 2 * (b + 1)) * (e2 + r)
    assert g >= 0
    assert margin == F(1, b + 1) * r * (r + 1) + F(b, 2 * (b + 1)) * g
    assert cov <= F(b, b + 1) * r * (r + 1)
    assert margin >= F(1, b + 1) * r * (r + 1)
    return dict(label=label, a=a, b=b, LE_U=m, LE_W=len(EW), LE_V=len(EV),
                S=sorted(S), K_pmf={str(k): F(v, m) for k, v in kcounts.items()},
                r=r, s=s, ER2=e2, VarR=var, Cov=cov, g_R=g, target_margin=margin,
                tails=tails)


W, EW, V, EV = ('w0', 'w1', 'w2'), [('w0', 'w1')], ('v0', 'v1'), [('v0', 'v1')]
actual = [
    check('random_cap', W, EW, V, EV, {'w1'}),
    check('empty_S', W, EW, V, EV, set()),
    check('full_S', W, EW, V, EV, set(W)),
    check('empty_W', (), [], V, EV, set()),
]

J = {0: F(1, 2), 1: F(1, 4), 2: F(1, 8), 3: F(1, 8)}
K = {0: F(9, 10), 3: F(1, 10)}
old_r = sum(p * q * min(j, k) for j, p in J.items() for k, q in K.items())
old_e2 = sum(p * q * min(j, k) ** 2 for j, p in J.items() for k, q in K.items())
old_var = old_e2 - old_r ** 2
old_g = old_r * (old_r + 1) - old_var
assert (old_r, old_e2, old_var, old_g) == (F(7, 80), F(3, 16), F(1151, 6400), -F(271, 3200))

data = dict(scope='Four fixed actual models and the existing abstract counterexample only.',
            actual=actual, old_abstract=dict(r=old_r, ER2=old_e2, VarR=old_var, g_R=old_g))
text = json.dumps(data, ensure_ascii=False, indent=2, default=str)
(OUT / 'verification.json').write_text(text + '\n')
print(text)
