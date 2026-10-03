#!/usr/bin/env python3
"""S85 exact diagnostic checks. Standard library only; proofs are in notes/PROOF.md.

Run: python S85/src/check_s85.py --output S85/evidence/check_s85.json
No enumeration below substitutes for the general layout proof.
"""
from __future__ import annotations
import argparse
from collections import Counter
from fractions import Fraction
from functools import lru_cache
from itertools import combinations_with_replacement, permutations, product
import json
from pathlib import Path
import random
from typing import Iterable

CORE = (0, 1, 0, 3, 15, 3, 31)
TYPES = ((0, 120), (0, 112), (7, 80), (15, 64))
GUARD_TYPE = (3, 112)


def close(pred: Iterable[int]) -> tuple[int, ...]:
    p = list(pred)
    n = len(p)
    for k in range(n):
        for v in range(n):
            if p[v] >> k & 1:
                p[v] |= p[k]
    if any(x >> v & 1 for v, x in enumerate(p)):
        raise ValueError('Relations contain a directed cycle.')
    if any(x >> n for x in p):
        raise ValueError('Predecessor mask outside vertex set.')
    return tuple(p)


def induced(pred: tuple[int, ...], vertices: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(sum(1 << i for i, u in enumerate(vertices) if pred[v] >> u & 1)
                 for v in vertices)


def count(pred: tuple[int, ...], pair: tuple[int, int] | None = None) -> int:
    n = len(pred)
    full = (1 << n) - 1
    @lru_cache(None)
    def visit(used: int) -> int:
        if used == full:
            return 1
        ans = 0
        for v, need in enumerate(pred):
            if used >> v & 1 or need & ~used:
                continue
            if pair is not None and v == pair[1] and not (used >> pair[0] & 1):
                continue
            ans += visit(used | (1 << v))
        return ans
    return visit(0)


def extensions(pred: tuple[int, ...]) -> list[tuple[int, ...]]:
    n = len(pred)
    full = (1 << n) - 1
    result = []
    def visit(used: int, order: tuple[int, ...]) -> None:
        if used == full:
            result.append(order)
            return
        for v, need in enumerate(pred):
            if not (used >> v & 1) and not (need & ~used):
                visit(used | (1 << v), order + (v,))
    visit(0, ())
    return result


def brute(pred: tuple[int, ...], pair: tuple[int, int]) -> tuple[int, int]:
    """Independent full permutation screening, not the order-ideal recursion."""
    n = len(pred)
    edges = [(u, v) for v, p in enumerate(pred) for u in range(n) if p >> u & 1]
    total = forward = 0
    for order in permutations(range(n)):
        pos = [0] * n
        for i, v in enumerate(order):
            pos[v] = i
        if all(pos[u] < pos[v] for u, v in edges):
            total += 1
            forward += pos[pair[0]] < pos[pair[1]]
    return total, forward


def bounds(order: tuple[int, ...], d: int, f: int) -> tuple[int, int]:
    pos = {v: i + 1 for i, v in enumerate(order)}
    lower = max([0] + [pos[v] for v in pos if d >> v & 1])
    upper = min([len(order) + 1] + [pos[v] for v in pos if f >> v & 1]) - 1
    return lower, upper


def filter_family(ext: list[tuple[int, ...]], types: tuple[tuple[int, int], ...]) -> set[int]:
    full = (1 << len(ext)) - 1
    result = {full}
    for d, f in types:
        windows = [bounds(tau, d, f) for tau in ext]
        for s in range(len(ext[0]) + 1):
            result.add(sum(1 << i for i, (lo, hi) in enumerate(windows) if lo <= s <= hi))
    todo = list(result)
    while todo:
        s = todo.pop()
        for t in tuple(result):
            z = s & t
            if z not in result:
                result.add(z)
                todo.append(z)
    return result


def attach(q: tuple[int, ...], types: tuple[tuple[int, int], ...],
           extra_edges: Iterable[tuple[int, int]] = ()) -> tuple[int, ...]:
    n, m = len(q), len(types)
    p = list(q) + [0] * m
    for i, (d, f) in enumerate(types):
        p[n + i] |= d
        for v in range(n):
            if f >> v & 1:
                p[v] |= 1 << (n + i)
    for i, j in extra_edges:
        p[n + j] |= 1 << (n + i)
    p = close(p)
    if induced(p, tuple(range(n))) != q:
        raise ValueError('Attachment changes the induced core.')
    for i, (d, f) in enumerate(types):
        actual_d = p[n + i] & ((1 << n) - 1)
        actual_f = sum(1 << v for v in range(n) if p[v] >> (n + i) & 1)
        if (d, f) != (actual_d, actual_f):
            raise ValueError('Attachment changes an intended exterior type.')
    return p


def chain_attach(q: tuple[int, ...], types: tuple[tuple[int, int], ...]) -> tuple[int, ...]:
    return attach(q, types, ((i, i + 1) for i in range(len(types) - 1)))


def layout_weights(p: tuple[int, ...], core_vertices: tuple[int, ...]):
    """Explicit exterior orders and slot layouts; independent of full-poset DP."""
    n = len(core_vertices)
    other = tuple(v for v in range(len(p)) if v not in core_vertices)
    q = induced(p, core_vertices)
    g = induced(p, other)
    ext = extensions(q)
    ty = tuple((sum(1 << i for i, v in enumerate(core_vertices) if p[z] >> v & 1),
                sum(1 << i for i, v in enumerate(core_vertices) if p[v] >> z & 1))
               for z in other)
    win = [[bounds(tau, *t) for t in ty] for tau in ext]
    weights = [0] * len(ext)
    layouts = Counter()
    for sigma in extensions(g):
        for slots in combinations_with_replacement(range(n + 1), len(other)):
            mask = 0
            for i in range(len(ext)):
                if all(win[i][v][0] <= s <= win[i][v][1] for v, s in zip(sigma, slots)):
                    mask |= 1 << i
                    weights[i] += 1
            layouts[mask] += 1
    return ext, weights, layouts


def random_poset(n: int, rng: random.Random) -> tuple[int, ...]:
    p = [0] * n
    for j in range(n):
        for i in range(j):
            if rng.random() < 0.3:
                p[j] |= (1 << i) | p[i]
    return close(p)


def main() -> dict:
    ext = extensions(CORE)
    assert len(ext) == 18
    assert brute(CORE, (1, 2)) == (18, 10)
    fw = sum(1 << i for i, tau in enumerate(ext) if tau.index(1) < tau.index(2))
    assert fw == 1023
    fs = filter_family(ext, TYPES)
    assert len(fs) == 22 and all(a & b in fs for a in fs for b in fs)
    cert = []
    zero_lower = zero_upper = 0
    for h in sorted(fs):
        c, u = h.bit_count(), (h & fw).bit_count()
        assert 3 * u >= c and 5 * u <= 3 * c
        if 3 * u == c:
            zero_lower |= h
        if 5 * u == 3 * c:
            zero_upper |= h
        cert.append({'mask': h, 'C': c, 'U': u, '3U-C': 3*u-c, '3C-5U': 3*c-5*u})
    assert zero_lower == 261135 and zero_upper == 209868
    assert zero_lower != (1 << 18) - 1 and zero_upper != (1 << 18) - 1

    grid = []
    for sizes in product(range(4), repeat=4):
        ty = tuple(t for t, m in zip(TYPES, sizes) for _ in range(m))
        p = chain_attach(CORE, ty)
        e, u = count(p), count(p, (1, 2))
        assert 3*u > e and 5*u < 3*e
        grid.append({'sizes': sizes, 'E': e, 'U': u})

    rng = random.Random(850310)
    arbitrary = []
    for iteration in range(64):
        ids = sorted(rng.randrange(4) for _ in range(rng.randint(1, 5)))
        ty = tuple(TYPES[i] for i in ids)
        edges = [(i, j) for i in range(len(ids)) for j in range(i + 1, len(ids))
                 if rng.random() < 0.3]
        p = attach(CORE, ty, edges)
        e, u = count(p), count(p, (1, 2))
        ex, w, layouts = layout_weights(p, tuple(range(7)))
        assert ex == ext and min(w) > 0
        assert sum(w) == e
        assert sum(w[i] for i in range(18) if fw >> i & 1) == u
        assert all(mask in fs for mask in layouts)
        for h in fs:
            direct_lo = sum(w[i] * (3 * int(bool(fw >> i & 1)) - 1)
                            for i in range(18) if h >> i & 1)
            via_lo = sum(mult * (3*((h & mask) & fw).bit_count() - (h & mask).bit_count())
                         for mask, mult in layouts.items())
            assert direct_lo == via_lo and via_lo >= 0
        assert 3*u > e and 5*u < 3*e
        arbitrary.append({'type_ids': ids, 'E': e, 'U': u, 'exterior_relations':
                          list(induced(p, tuple(range(7, len(p)))))})

    generic = []
    for iteration in range(160):
        n = rng.randint(4, 7)
        p = random_poset(n, rng)
        core_vertices = tuple(sorted(rng.sample(range(n), rng.randint(2, min(4, n - 1)))))
        ex, w, layouts = layout_weights(p, core_vertices)
        a, b = core_vertices[:2]
        e, u = count(p), count(p, (a, b))
        assert min(w) > 0 and sum(w) == e
        assert sum(weight for tau, weight in zip(ex, w) if tau.index(0) < tau.index(1)) == u
        generic.append({'n': n, 'core': core_vertices, 'E': e, 'U': u})

    guard_layers = Counter()
    for tau in ext:
        lo, hi = bounds(tau, *GUARD_TYPE)
        guard_layers[(hi - lo, int(tau.index(1) < tau.index(2)))] += 1
    assert [sum(v for (k, event), v in guard_layers.items() if k == j) for j in range(3)] == [4, 8, 6]
    assert [guard_layers[(j, 1)] for j in range(3)] == [2, 2, 6]
    guard = []
    for t in range(21):
        p = chain_attach(CORE, (GUARD_TYPE,) * t)
        e, u = count(p), count(p, (1, 2))
        assert e == 3*t*t+17*t+18 and u == 3*t*t+11*t+10
        if t >= 2:
            assert 3*u > 2*e
        guard.append({'t': t, 'E': e, 'U': u})
    g2 = chain_attach(CORE, (GUARD_TYPE,) * 2)
    assert brute(g2, (1, 2)) == (64, 44)
    core_with_inner = chain_attach(CORE, (TYPES[2],))
    assert brute(core_with_inner, (1, 2)) == (38, 18)

    q6 = (0, 1, 3, 0, 8, 24)
    ex6 = extensions(q6)
    f6 = filter_family(ex6, ((0, 48),))
    menu_cert = []
    for h in sorted(f6):
        c = h.bit_count()
        u1 = sum(1 for i, tau in enumerate(ex6) if h >> i & 1 and tau.index(0) < tau.index(3))
        u2 = sum(1 for i, tau in enumerate(ex6) if h >> i & 1 and tau.index(1) < tau.index(3))
        assert 2*u1 >= c and 2*u2 <= c and 2*u1-u2 <= c
        menu_cert.append({'mask': h, 'C': c, 'U1': u1, 'U2': u2})
    assert brute(q6, (0, 3)) == (20, 10)
    menu_examples = []
    for t in range(21):
        p = chain_attach(q6, ((0, 48),) * t)
        e = count(p)
        u1, u2 = count(p, (0, 3)), count(p, (1, 3))
        assert max(min(u1, e-u1), min(u2, e-u2))*3 >= e
        menu_examples.append({'t': t, 'E': e, 'U1': u1, 'U2': u2})

    return {'round': 'S85', 'date': '2026-10-03',
            'status': 'exact checks passed; general theorems have separate proofs',
            'canonical_parent': 'online S84 @02d60e5937a84140c1b893559dce3daff025f42b',
            'core': {'predecessor_masks': CORE, 'extensions': ext, 'event_mask': fw,
                     'types': TYPES, 'filters': cert,
                     'zero_lower_union': zero_lower, 'zero_upper_union': zero_upper},
            'four_parameter_grid': {'range_each': [0, 3], 'checked': len(grid),
                'selected': [row for row in grid if tuple(row['sizes']) in
                             [(0,0,0,0),(0,0,1,0),(1,1,1,1),(3,3,3,3)]],
                'observed_min_p': str(min(Fraction(row['U'], row['E']) for row in grid)),
                'observed_max_p': str(max(Fraction(row['U'], row['E']) for row in grid))},
            'arbitrary_exterior_cases': {'checked': len(arbitrary), 'new_points': [1,5],
                                         'seed': 850310, 'all_assertions_passed': True},
            'generic_induced_core_layout_cases': {'checked': len(generic), 'total_points': [4,7],
                'core_points': [2,4], 'all_assertions_passed': True},
            'guard': {'type': GUARD_TYPE, 'c': [4,8,6], 'u': [2,2,6], 'cases': guard},
            'two_candidate_menu': {'core': q6, 'filters': menu_cert, 'chain_checks': menu_examples},
            'counts': {'core_filters': len(fs), 'four_parameter_grid': len(grid),
                       'arbitrary_exteriors': len(arbitrary), 'generic_layouts': len(generic),
                       'guard_parameters': len(guard), 'independent_permutation_cases': 4,
                       'menu_parameters': len(menu_examples)},
            'limits': ['No general 1/3-2/3 conjecture certification.',
                       'No claim of optimal constants or minimal seed size.',
                       'Sampled exterior checks do not prove the arbitrary-exterior theorem.',
                       'No old experimental counts are included as new runs.']}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path,
                        default=Path(__file__).resolve().parents[1] / 'evidence/check_s85.json')
    args = parser.parse_args()
    result = main()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(result['counts'], ensure_ascii=False))
    print(args.output)
