"""Exact checks for the singleton-upper-spine integral obstruction.

Standard library only.  No imports from the earlier project implementations.
All probabilities are integer counts of actual labelled linear extensions.
Run: python verify_single_inner_spine.py
"""
from fractions import Fraction
from functools import lru_cache
from itertools import product
from math import comb
from pathlib import Path
import json

COVERS = ((0, 3), (1, 2), (1, 4), (2, 3), (2, 6), (3, 5), (4, 5))


def require(condition, context):
    """A verification check that remains active under python -O."""
    if not condition:
        raise RuntimeError('Verification failed: ' + repr(context))


def actual_poset(weights):
    blocks = []
    n = 0
    for size in weights:
        blocks.append(tuple(range(n, n + size)))
        n += size
    pred = [0] * n
    for chain in blocks:
        for left, right in zip(chain, chain[1:]):
            pred[right] |= 1 << left
    for left, right in COVERS:
        pred[blocks[right][0]] |= 1 << blocks[left][-1]
    return blocks, pred


def extension_count(pred, extra=None):
    pred = list(pred)
    if extra is not None:
        left, right = extra
        pred[right] |= 1 << left
    full = (1 << len(pred)) - 1

    @lru_cache(None)
    def count(ideal):
        if ideal == full:
            return 1
        result = 0
        for vertex, predecessors in enumerate(pred):
            bit = 1 << vertex
            if not ideal & bit and predecessors & ideal == predecessors:
                result += count(ideal | bit)
        return result

    return count(0)


def closure(pred):
    down = list(pred)
    changed = True
    while changed:
        changed = False
        for v in range(len(down)):
            expanded = down[v]
            for p in range(len(down)):
                if down[v] >> p & 1:
                    expanded |= down[p]
            if expanded != down[v]:
                down[v] = expanded
                changed = True
    up = [0] * len(down)
    for v, predecessors in enumerate(down):
        for p in range(len(down)):
            if predecessors >> p & 1:
                up[p] |= 1 << v
    return down, up


def is_chain(mask, down):
    vertices = [i for i in range(len(down)) if mask >> i & 1]
    return all((down[i] >> j & 1) or (down[j] >> i & 1)
               for index, i in enumerate(vertices) for j in vertices[index + 1:])


def dual_good_edge(left, right, down, up):
    incomparable = not ((down[left] >> right & 1) or (down[right] >> left & 1))
    return (incomparable and up[right] & ~up[left] == 0
            and is_chain(down[left] & ~down[right], down))


def lower_good_edge(left, right, down, up):
    incomparable = not ((down[left] >> right & 1) or (down[right] >> left & 1))
    return (incomparable and down[left] & ~down[right] == 0
            and is_chain(up[right] & ~up[left], down))


def power_integral(alpha, exponent):
    return (1 - alpha ** (exponent + 1)) / (exponent + 1)


def integral_margin(alpha, delta, t, v):
    """Exact integral of (z+delta)^t K(z), with K as in the proof."""
    result = Fraction(0)
    for j in range(t + 1):
        coefficient = comb(t, j) * delta ** (t - j)
        first = power_integral(alpha, j + 1) - alpha * power_integral(alpha, j)
        second = power_integral(alpha, j + v + 1) - alpha * power_integral(alpha, j + v)
        third = (power_integral(alpha, j + v + 1)
                 - alpha ** (v + 1) * power_integral(alpha, j)) / (v + 1)
        result += coefficient * (first - 2 * second + third)
    return result


def main():
    checked = 0
    edge_checks = 0
    worst_margin = None
    worst_vector = None
    for u, a, b, t in product(range(1, 5), repeat=4):
        for v in range(t + 1, t + 5):
            weights = (u, a, b, 1, t, 1, v)
            blocks, pred = actual_poset(weights)
            x, z, f = blocks[3][0], blocks[5][0], blocks[6][-1]
            down, up = closure(pred)
            require(dual_good_edge(x, f, down, up), ('forced x<F', weights))
            require(dual_good_edge(f, z, down, up), ('forced F<z', weights))
            edge_checks += 2
            total = extension_count(pred)
            nx_before_f = extension_count(pred, (x, f))
            nf_before_z = extension_count(pred, (f, z))
            margin = 2 * total - nx_before_f - 2 * nf_before_z
            require(margin >= 0, ('probability inequality', weights, total, nx_before_f, nf_before_z))
            normalized = Fraction(margin, total)
            if worst_margin is None or normalized < worst_margin:
                worst_margin, worst_vector = normalized, weights
            checked += 1

    singleton_checks = 0
    for u, a, b, t in product(range(1, 4), repeat=4):
        weights = (u, a, b, 1, t, 1, 1)
        blocks, pred = actual_poset(weights)
        down, up = closure(pred)
        x, f = blocks[3][0], blocks[6][0]
        require(dual_good_edge(x, f, down, up), ('v1 forced x<F', weights))
        require(lower_good_edge(f, x, down, up), ('v1 forced F<x', weights))
        singleton_checks += 1

    integral_checks = 0
    identities = 0
    for alpha, delta, t, offset in product(
            (Fraction(0), Fraction(1, 5), Fraction(1, 2), Fraction(4, 5)),
            (Fraction(0), Fraction(1, 3), Fraction(2)), range(1, 9), range(1, 5)):
        v = t + offset
        margin = integral_margin(alpha, delta, t, v)
        require(margin >= 0, ('integral inequality', alpha, delta, t, v, margin))
        integral_checks += 1
        if delta == 0 and offset == 1:
            require(margin == 0, ('boundary identity', alpha, t, v, margin))
            identities += 1

    # An explicit boundary countercheck: the lemma is not asserted when v<=t.
    outside_margin = integral_margin(Fraction(0), Fraction(0), 2, 2)
    require(outside_margin < 0, ('out-of-scope negative margin', outside_margin))

    result = {
        'status': 'PASS',
        'exact_labelled_vectors': checked,
        'weight_scope': 'u,a,b,t each in {1,2,3,4}; c=d=1; v in {t+1,t+2,t+3,t+4}',
        'independent_labelled_ideal_counts': 3 * checked,
        'actual_vertex_forced_edge_checks': edge_checks,
        'smallest_normalized_inequality_margin': str(worst_margin),
        'margin_vector': worst_vector,
        'v1_structural_cycle_vectors': singleton_checks,
        'exact_rational_integral_checks': integral_checks,
        'boundary_zero_identities': identities,
        'out_of_scope_integral_countercheck': {
            'alpha': '0', 'delta': '0', 't': 2, 'v': 2,
            'integral_margin': str(outside_margin),
        },
        'interpretation': 'Finite implementation checks only; the unbounded theorem uses the written proof.',
    }
    destination = Path(__file__).with_name('verification.json')
    destination.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
