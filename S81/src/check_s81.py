"""Targeted S81 arithmetic, not a proof gate. Stdlib + mpmath for analytic probes.
Run: python S81/src/check_s81.py. No network calls and no historical large reruns.
"""
from __future__ import annotations
from collections import Counter
from fractions import Fraction as F
from functools import lru_cache
from itertools import combinations
from math import comb, factorial
from pathlib import Path
import cmath, json
import mpmath as mp

mp.mp.dps = 65


def posets(n: int):
    edges = list(combinations(range(n), 2))
    for b in range(1 << len(edges)):
        p = [0] * n
        for j, (x, y) in enumerate(edges):
            if b >> j & 1:
                p[y] |= 1 << x
        if all(not (p[x] & ~p[y]) for y in range(n) for x in range(y) if p[y] >> x & 1):
            yield tuple(p)


def extensions(pre: tuple[int, ...]):
    full = (1 << len(pre)) - 1
    def dfs(mask, word):
        if mask == full:
            yield word
        for v in range(len(pre)):
            if not mask >> v & 1 and not pre[v] & ~mask:
                yield from dfs(mask | 1 << v, word + (v,))
    yield from dfs(0, ())


def raw_law(pre, mark):
    labels = [v for v in range(len(pre)) if v != mark]
    new = tuple(sum(1 << j for j, v in enumerate(labels) if pre[w] >> v & 1) for w in labels)
    out = Counter()
    for word in extensions(new):
        rank = {labels[v]: j + 1 for j, v in enumerate(word)}
        lo = max([rank[v] for v in labels if pre[mark] >> v & 1] + [0])
        hi = min([rank[v] for v in labels if pre[v] >> mark & 1] + [len(pre)])
        out[hi - lo] += 1
    return out


def mm(v):
    return mp.mpf(v.numerator) / v.denominator if isinstance(v, F) else mp.mpf(v)


@lru_cache(None)
def call(k: int, t):
    t = mm(t)
    return mp.exp(-t) * sum((k - v) * t**v / factorial(v) for v in range(k))


def kernel(k, t):
    return call(k, t) - max(mp.mpf(0), k - mm(t))


def beta_binomial(m: int, q: int, s: int):
    if not 1 <= q <= s:
        raise ValueError('Require 1 <= q <= s')
    if q == s:
        return [(q + m, F(1))]
    den = comb(m + s - 1, s - 1)
    return [(q + v, F(comb(v + q - 1, q - 1) * comb(m - v + s - q - 1, s - q - 1), den)) for v in range(m + 1)]


def run():
    stat = Counter()
    tol = mp.mpf('1e-55')
    min_hinge = mp.inf
    for k in range(2, 25):
        for t in [F(i, 3) for i in range(1, 91)]:
            kk = kernel(k, t)
            assert kk > 0
            rhs = mp.exp(-mm(t)) * sum(mm(t)**v / factorial(v) for v in range(k + 1))
            rhs -= max(0, k + 1 - t) - max(0, k - t)
            assert abs(kernel(k + 1, t) - kk - rhs) < tol
            stat['kernel_recurrences_numeric'] += 1
    for q in range(2, 7):
        for b in range(q, 20):
            for t in [F(1, 2), F(3, 2), F(4), F(21, 2), F(25)]:
                assert abs(min(kernel(k, t) for k in range(q, b + 1)) - min(kernel(q, t), kernel(b, t))) < tol
                stat['endpoint_minimum_numeric'] += 1
    by_n = {}
    for n in range(1, 5):
        by_n[n] = 0
        for pre in posets(n):
            by_n[n] += 1
            for x in range(n):
                raw = raw_law(pre, x)
                for r in range(1, 5):
                    q = r + 1
                    hist = {l + r: c * comb(l + r - 1, r) for l, c in raw.items()}
                    total = sum(hist.values())
                    mu = F(sum(z * c for z, c in hist.items()), total)
                    theta = mu / q
                    var = F(sum(z * z * c for z, c in hist.items()), total) - mu * mu
                    deficit = mu * (mu - q) / q - var
                    assert deficit >= 0
                    stat['exact_block_laws'] += 1
                    for t in [F(1, 2), F(2), mu, F(7), F(15)]:
                        j = sum(F(c, total) * kernel(z, t) for z, c in hist.items())
                        direct = sum(F(c, total) * max(0, z - t) for z, c in hist.items())
                        tc = sum(F(c, total) * call(z, t) for z, c in hist.items())
                        gc = mm(theta) * call(q, t / theta)
                        assert abs(tc - mm(direct) - j) < tol
                        assert gc - tc >= -tol
                        lower = min(kernel(q, t), kernel(max(hist), t))
                        assert gc - mm(direct) >= lower - tol
                        min_hinge = min(min_hinge, gc - mm(direct))
                        stat['threshold_decompositions_numeric'] += 1
                        # Event A is a genuine window event in the original extension law.
                        cut = sorted(hist)[len(hist) // 2]
                        prob = sum((F(c, total) for z, c in hist.items() if z >= cut), F(0))
                        actual = sum((F((z - q) * c, total) for z, c in hist.items() if z >= cut), F(0))
                        upper = mm((t - q) * prob) + gc - j
                        assert mm(actual) <= upper + tol
                        stat['event_bounds_numeric'] += 1
    rows = []
    for s in [12, 40, 120, 400]:
        m = 2 * s
        for q in sorted(set([2, int(s**0.5), s // 2, s])):
            law = beta_binomial(m, q, s)
            assert sum(p for _, p in law) == 1
            mu = F(q * (m + s), s)
            theta = mu / q
            var = sum((p * (z - mu)**2 for z, p in law), F(0))
            c = F(m * (m + s), s * s * (s + 1))
            deficit = q * (q + 1) * c
            assert var == q * (s - q) * c
            assert deficit == mu * (mu - q) / q - var
            stat['finite_population_moment_identities_exact'] += 1
            errs = []
            for u in [0.2, 0.4, 0.7]:
                cf = sum(float(p) * cmath.exp(1j * u * float(z - mu) / q**0.5) for z, p in law)
                gauss = mp.exp(-mm(theta * (theta - 1)) * u * u / 2)
                bound = mp.exp(mm(theta) * u * u / 2) * (u * mp.sqrt(mm(deficit) / q) +
                    (2*mm(theta)*u**3/3 + u*u*mp.sqrt(mm(theta*(theta-1)))/2 + 2*mm(theta)**3*u**3/3)/mp.sqrt(q))
                if u * max(1, float(theta)) / q**0.5 <= 0.5:
                    assert abs(cf - complex(gauss)) <= float(bound) + 1e-12
                    stat['characteristic_bounds_numeric'] += 1
                errs.append(abs(cf - complex(gauss)))
            rows.append({'s': s, 'm': m, 'q': q, 'D_over_q': str(deficit / q),
                         'variance_ratio': str(var / (q * theta * (theta - 1))),
                         'characteristic_errors_at_0.2_0.4_0.7': errs})
    eta = F(23, 20_000_000_000_000)
    mu0 = F(34896609280, 27)
    eps = F(9, 100)
    scalar = mu0 * (21 * F(17, 2) * eta + F(42**3 + 8*42**2 + 27*42 + 38, 20**14) / eps**2)
    assert scalar == F(146306406272, 533935546875) < F(11, 40)
    assert F(27, 34896609253) > 6*eta
    assert sum((F(3**i, factorial(i)) for i in range(9)), F(0)) > 20
    result = {'counts': dict(stat), 'base_natural_posets': by_n,
              'minimum_observed_hinge_gap': str(min_hinge),
              'U58_scalar_upper_exact': str(scalar),
              'growing_block_examples': rows,
              'precision': '65 decimal digits; thresholds and CF are numerical probes, not exact certificates',
              'exact_scope': 'block weights, moments, scalar rational inequalities and finite-population variances',
              'scope': 'No general theorem or CLT is inferred from these finite probes. No historical counts are relabelled as current runs.',
              'result': 'all checks passed'}
    out = Path(__file__).resolve().parents[1] / 'evidence/checks.json'
    out.write_text(json.dumps(result, ensure_ascii=False, indent=2))
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    run()
