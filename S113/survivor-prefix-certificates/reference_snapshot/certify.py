#!/usr/bin/env python3
"""Generate and verify exact prefix certificates, including under ``python -O``.

``verify`` checks one primal/dual cell, while ``verify_bundle`` checks the whole
three-template export, its reconstructed profiles, and every orientation mask.
Successful verification never depends on Python assertions.
"""
from fractions import Fraction as Q
from itertools import combinations, product, permutations
from pathlib import Path
import json

OUT = Path(__file__).resolve().parent


class Invalid(ValueError):
    """A certificate, profile, or solver invariant failed validation."""


def require(ok, message):
    if not ok:
        raise Invalid(message)


def rat(value):
    # Reject bools, binary floats, and implicit coercions at the input boundary.
    require(type(value) in (int, str), 'rational input must be integer or string')
    try:
        return Q(value)
    except (ValueError, ZeroDivisionError) as exc:
        raise Invalid('invalid rational') from exc


def schema(value, fields, name):
    require(type(value) is dict, name + ' dictionary')
    require(set(fields) <= value.keys(), name + ' missing required fields')


def table(F, A):
    require(type(F) is list and F and
            all(type(f) is int and f > 0 for f in F), 'F positive integers')
    require(type(A) is list and A and
            all(type(row) is list and len(row) == len(F) for row in A),
            'A dimensions')
    require(all(type(a) is int and 0 <= a <= f
                for row in A for a, f in zip(row, F)), 'A range')


def pattern_check(pattern, size):
    require(type(pattern) is str and len(pattern) == size and
            set(pattern) <= set('LH'), 'cell pattern')


def dot(a, b):
    require(len(a) == len(b), 'dot dimensions')
    return sum((x * y for x, y in zip(a, b)), Q())


def solve(A, b):
    n = len(b)
    require(n > 0 and len(A) == n and all(len(row) == n for row in A),
            'linear system dimensions')
    M = [[Q(x) for x in a] + [Q(bb)] for a, bb in zip(A, b)]
    for k in range(n):
        j = next((j for j in range(k, n) if M[j][k]), None)
        if j is None:
            return None
        M[k], M[j] = M[j], M[k]
        d = M[k][k]
        M[k] = [v / d for v in M[k]]
        for j in range(n):
            if j != k:
                d = M[j][k]
                M[j] = [v - d * w for v, w in zip(M[j], M[k])]
    return [row[-1] for row in M]


def cell_data(F, A, pattern):
    q = [[Q(a, f) for a, f in zip(row, F)] for row in A]
    return [[Q(1, 3) - x if side == 'L' else x - Q(2, 3) for x in row]
            for row, side in zip(q, pattern)]


def lp(F, A, pattern):
    table(F, A)
    # product() supplies tuples; saved certificates always use strings.
    require(type(pattern) in (str, tuple, list), 'cell pattern type')
    require(all(type(side) is str and side in ('L', 'H') for side in pattern),
            'cell pattern letters')
    pattern = ''.join(pattern)
    m = len(F)
    pattern_check(pattern, len(A))
    h = cell_data(F, A, pattern)
    rows = [[-int(i == j) for j in range(m)] + [0] for i in range(m)] + [
        [-x for x in hh] + [1] for hh in h]
    eq = [Q(1)] * m + [Q(0)]
    best = None
    for active in combinations(range(len(rows)), m):
        x = solve([eq] + [rows[i] for i in active], [1] + [0] * m)
        if x is not None and all(dot(r, x) <= 0 for r in rows):
            if best is None or x[-1] > best[-1]:
                best = x
    require(best is not None, 'missing primal optimum')
    tight = [i for i, r in enumerate(rows) if dot(r, best) == 0]
    for active in combinations(tight, m):
        basis = [rows[i] for i in active] + [eq]
        w = solve(list(map(list, zip(*basis))), [0] * m + [1])
        if w is None or any(t < 0 for t in w[:-1]):
            continue
        weights = [Q(0)] * len(rows)
        for i, v in zip(active, w[:-1]):
            weights[i] = v
        require(w[-1] == best[-1], 'solver primal dual equality')
        result = dict(pattern=pattern, optimum=str(best[-1]),
                      mu=[str(x) for x in best[:-1]],
                      lambda_pairs=[str(x) for x in weights[m:]],
                      eta=[str(x) for x in weights[:m]], nu=str(w[-1]))
        verify(F, A, result)
        return result
    raise Invalid('missing dual')


def verify(F, A, c):
    """Check one cell exactly; this alone does not certify full-mask coverage."""
    table(F, A)
    schema(c, ('pattern', 'mu', 'lambda_pairs', 'eta', 'nu', 'optimum'), 'cell')
    m, k = len(F), len(A)
    pattern_check(c['pattern'], k)
    for key, size in (('mu', m), ('lambda_pairs', k), ('eta', m)):
        require(type(c[key]) is list and len(c[key]) == size, key + ' dimensions')
    mu = list(map(rat, c['mu']))
    lam = list(map(rat, c['lambda_pairs']))
    eta = list(map(rat, c['eta']))
    nu, opt = rat(c['nu']), rat(c['optimum'])
    h = cell_data(F, A, c['pattern'])
    require(all(x >= 0 for x in mu + lam + eta), 'nonnegative multipliers')
    require(sum(mu) == 1 and sum(lam) == 1, 'normalizations')
    require(all(dot(hh, mu) >= opt for hh in h), 'primal feasible')
    require(all(sum(lam[i] * h[i][j] for i in range(k)) + eta[j] == nu
                for j in range(m)), 'dual identity')
    require(opt == nu, 'primal dual equality')
    return opt


def verify_cells(F, A, cells):
    """Require every orientation exactly once before accepting their optima."""
    table(F, A)
    require(type(cells) is list and len(cells) == 2 ** len(A),
            'complete unique masks')
    for c in cells:
        schema(c, ('pattern',), 'cell')
        pattern_check(c['pattern'], len(A))
    masks = {''.join(p) for p in product('LH', repeat=len(A))}
    require({c['pattern'] for c in cells} == masks, 'complete unique masks')
    return [verify(F, A, c) for c in cells]


def permutation_profile(pred, maxima, pairs):
    n = len(pred)
    F, A = [], [[] for _ in pairs]
    for omitted in maxima:
        vertices = [i for i in range(n) if i != omitted]
        valid = []
        for perm in permutations(vertices):
            where = {v: i for i, v in enumerate(perm)}
            if all(where[x] < where[y] for y in vertices for x in vertices
                   if pred[y] >> x & 1):
                valid.append(where)
        F.append(len(valid))
        for row, (x, y) in zip(A, pairs):
            row.append(sum(v[x] < v[y] for v in valid))
    return F, A


def pair_list(value, n, name):
    require(type(value) is list and all(
        type(pair) is list and len(pair) == 2 and
        all(type(v) is int and 0 <= v < n for v in pair) and pair[0] != pair[1]
        for pair in value), name + ' endpoints')


def verify_profile(p):
    """Rebuild the cut profile from Hasse edges rather than trust count tables."""
    schema(p, ('n', 'r', 'pred', 'covers_edges', 'maxima', 'ideals', 'pairs',
               'F', 'A', 'covers'), 'profile')
    n, r = p['n'], p['r']
    require(type(n) is int and n > 0 and type(r) is int and r == n - 1, 'cut')
    full = (1 << n) - 1
    require(type(p['pred']) is list and len(p['pred']) == n and
            all(type(v) is int and 0 <= v <= full for v in p['pred']),
            'predecessor masks')
    pair_list(p['covers_edges'], n, 'Hasse edges')
    edges = set(map(tuple, p['covers_edges']))
    require(len(edges) == len(p['covers_edges']), 'duplicate Hasse edges')
    relation = set(edges)
    for k in range(n):
        relation |= {(i, j) for i in range(n) for j in range(n)
                     if (i, k) in relation and (k, j) in relation}
    require(all(a != b for a, b in relation), 'acyclic order')
    pred = [sum(1 << a for a, b in relation if b == i) for i in range(n)]
    require(p['pred'] == pred, 'predecessor closure')
    covers = {(a, b) for a, b in relation if not any(
        (a, c) in relation and (c, b) in relation for c in range(n))}
    require(edges == covers, 'Hasse edges')
    maxima = [i for i in range(n) if not any(a == i for a, b in relation)]
    ideals = [full ^ (1 << i) for i in maxima]
    for key, expected in (('maxima', maxima), ('ideals', ideals)):
        require(type(p[key]) is list and all(type(v) is int for v in p[key])
                and p[key] == expected, 'recomputed ' + key)
    common = [i for i in range(n) if all(state >> i & 1 for state in ideals)]
    pairs = [list(pair) for pair in combinations(common, 2)
             if pair not in relation and pair[::-1] not in relation]
    pair_list(p['pairs'], n, 'observed pairs')
    require(p['pairs'] == pairs, 'recomputed pairs')
    table(p['F'], p['A'])
    require(len(p['F']) == len(ideals) and len(p['A']) == len(pairs),
            'profile table dimensions')
    require(permutation_profile(pred, maxima, pairs) == (p['F'], p['A']),
            'recomputed F and A')
    require(p['covers'] is True, 'successful profile')


def selection(p, selected):
    require(type(selected) is list and selected and all(
        type(i) is int and 0 <= i < len(p['A']) for i in selected),
        'selected indices')
    require(len(set(selected)) == len(selected), 'unique selected indices')
    return [p['A'][i] for i in selected]


def verify_template(p):
    verify_profile(p)
    schema(p, ('name', 'selected_indices', 'selected_pairs', 'certificates',
               'covered', 'all_observed_pairs_nonfixed'), 'template')
    require(type(p['name']) is str and p['name'], 'template name')
    A = selection(p, p['selected_indices'])
    pair_list(p['selected_pairs'], p['n'], 'selected pairs')
    require(p['selected_pairs'] == [p['pairs'][i] for i in p['selected_indices']],
            'selected endpoints')
    opts = verify_cells(p['F'], A, p['certificates'])
    covered = all(v <= 0 for v in opts)
    require(type(p['covered']) is bool and p['covered'] == covered,
            'aggregate coverage')
    require(covered, 'successful template')
    nonfixed = all(any(not Q(1, 3) <= Q(a, f) <= Q(2, 3)
                       for a, f in zip(row, p['F'])) for row in p['A'])
    require(p['all_observed_pairs_nonfixed'] is nonfixed and nonfixed,
            'fixed-pair status')
    return True


def verify_bundle(data):
    """Verify the complete three-template export, not isolated cells only."""
    require(type(data) is list and len(data) == 3, 'three templates')
    for p in data:
        verify_template(p)
    require(len({p['name'] for p in data}) == len(data), 'unique templates')
    return True


def cert(prof, name, selected):
    verify_profile(prof)
    prof = dict(prof)
    F, A = prof['F'], selection(prof, selected)
    cells = [lp(F, A, p) for p in product('LH', repeat=len(A))]
    prof.update(name=name, selected_indices=selected,
                selected_pairs=[prof['pairs'][i] for i in selected],
                certificates=cells, covered=True, all_observed_pairs_nonfixed=True)
    verify_template(prof)
    print(name, 'F', F, 'A', A)
    for c in cells:
        print(c)
    return prof


if __name__ == '__main__':
    data = json.loads((OUT / 'candidates.json').read_text())
    specs = [('W3-six-boundary', [0, 0, 1, 3, 5, 7], [0, 1]),
             ('W3-six-triangle', [0, 0, 1, 2, 5, 7], [0, 1]),
             ('W3-seven-three-minima', [0, 0, 0, 1, 2, 5, 11], [0, 2])]
    result = []
    for name, pred, sel in specs:
        p = next(p for p in data['candidates'] if p['pred'] == pred)
        result.append(cert(p, name, sel))
    verify_bundle(result)
    (OUT / 'exact_templates.json').write_text(json.dumps(result, indent=2))
