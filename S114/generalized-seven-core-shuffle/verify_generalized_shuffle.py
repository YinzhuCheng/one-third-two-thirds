"""Self-contained exact checks of generalized seven-core shuffle bounds.

The probability formulas, block-state recurrence, complete-word fiber census,
and integer cone checks use separate implementations. Standard library only.
All numerical comparisons are integer comparisons, including boundary values.
"""
from collections import defaultdict
from functools import lru_cache
from itertools import product
from math import comb
from pathlib import Path
import json
import random

COVERS = ((0, 3), (1, 2), (1, 4), (2, 3), (2, 6), (3, 5), (4, 5))
PREDECESSORS = tuple(tuple(i for i, j in COVERS if j == block) for block in range(7))


def require(condition, context):
    """Checks remain active under python -O."""
    if not condition:
        raise RuntimeError(str(context))


def dual(w):
    u, a, b, c, t, d, v = w
    return v, d, c, b, t, a, u


def exact_formula(w):
    """Return (e(P), e(P with B2<B4)) by the T2-split double sum."""
    u, a, b, c, t, d, v = w
    require(len(w) == 7 and min(w) >= 1, 'len(w) == 7 and min(w) >= 1')
    total = numerator = 0
    for i in range(u + 1):
        for j in range(t + 1):
            common = (comb(a + b + i + j - 1, i)
                      * comb(u - i + c + t - j, t - j)
                      * comb(u - i + c + t - j + d + v, v))
            total += comb(b + j - 1, j) * common
            first2 = 1 if j == 0 else (0 if b == 1 else comb(b + j - 2, j))
            numerator += first2 * common
    return total, numerator


def block_count(w, extra=None):
    """Independent recurrence over consumed chain lengths.

    extra=(i,r,j,s) requires element (i,r) before element (j,s),
    with ranks starting at one. No double-sum formula is used.
    """
    @lru_cache(None)
    def count(state):
        if state == w:
            return 1
        result = 0
        for j in range(7):
            if state[j] == w[j]:
                continue
            if any(state[i] < w[i] for i in PREDECESSORS[j]):
                continue
            if extra is not None:
                i, r, target, s = extra
                if j == target and state[j] + 1 == s and state[i] < r:
                    continue
            next_state = list(state)
            next_state[j] += 1
            result += count(tuple(next_state))
        return result
    return count((0,) * 7)


def complete_words(w):
    """Enumerate every valid block word exactly once, without count formulas."""
    state = [0] * 7
    word = []
    n = sum(w)
    def visit():
        if len(word) == n:
            yield tuple(word)
            return
        for j in range(7):
            if state[j] == w[j]:
                continue
            if any(state[i] < w[i] for i in PREDECESSORS[j]):
                continue
            state[j] += 1
            word.append(j)
            yield from visit()
            word.pop()
            state[j] -= 1
    yield from visit()


def fiber_prediction(m, k, t, q):
    """Binary order statistics plus A-insertion multiplicity, no full words."""
    total = favorable = 0
    for r in range(q, q + t + 1):
        insertion = comb(m + r - 1, m)
        after = comb(k + t - r, k - q)
        total += comb(r - 1, q - 1) * after * insertion
        if q == 1:
            if r == 1:
                favorable += after * insertion
        else:
            favorable += comb(r - 2, q - 2) * after * insertion
    return total, favorable


def check_fibers(w):
    fibers = defaultdict(lambda: [0, 0])
    word_count = 0
    for word in complete_words(w):
        end_prefix = max(i for i, x in enumerate(word) if x == 1)
        start_suffix = word.index(5)
        prefix = word[:end_prefix + 1]
        suffix = word[start_suffix:]
        middle = word[end_prefix + 1:start_suffix]
        fixed_s = tuple(x for x in middle if x in (2, 3, 6))
        key = prefix, suffix, fixed_s
        fibers[key][0] += 1
        fibers[key][1] += word.index(2) < word.index(4)
        word_count += 1
    require(word_count == exact_formula(w)[0], 'word_count == exact_formula(w)[0]')
    for (prefix, suffix, fixed_s), counts in fibers.items():
        require(prefix[-1] == 1 and set(prefix) <= {0, 1}, 'prefix[-1] == 1 and set(prefix) <= {0, 1}')
        require(suffix[0] == 5 and set(suffix) <= {5, 6}, 'suffix[0] == 5 and set(suffix) <= {5, 6}')
        require(fixed_s[0] == 2, 'fixed_s[0] == 2')
        m = w[0] - prefix.count(0)
        k = len(fixed_s)
        q = fixed_s.index(3) + 1
        t = w[4]
        require(k == w[2] + w[3] + fixed_s.count(6), 'k == w[2] + w[3] + fixed_s.count(6)')
        require(q >= w[2] + 1, 'q >= w[2] + 1')
        require(tuple(counts) == fiber_prediction(m, k, t, q), (w, prefix, suffix, fixed_s, counts))
        require(counts[1] * (k + t) <= counts[0] * k, 'counts[1] * (k + t) <= counts[0] * k')
    return word_count, len(fibers)


def constants(spine):
    a, b, c, d = spine
    s = b + c
    alpha, beta = a + b - 1, c + d - 1
    U, V = (2 * alpha + beta) // 3, (alpha + 2 * beta) // 3
    T = s - 1 + min(U, V)
    return s, alpha, beta, U, V, T


def original_cone(spine, u, t, v):
    a, b, c, d = spine
    return (u >= 2 and t >= 1 and v >= 2
            and 2 * u < a + b + t + v
            and 2 * v < u + c + t + d
            and 2 * t < b + c + u
            and 2 * t < b + c + v)


def envelope(spine, u, t, v):
    s, alpha, beta, U, V, T = constants(spine)
    low = max(2, 2 * t - s + 1)
    return (1 <= t <= T and low <= u <= t + U
            and max(low, 2 * u - t - alpha) <= v <= (u + t + beta) // 2)


def run():
    formula_cases = list(product(range(1, 4), repeat=7))
    rng = random.Random(20261010)
    stress_cases = [tuple(rng.randint(1, 8) for _ in range(7)) for _ in range(64)]
    stress_cases.extend([(1, 12, 1, 1, 1, 12, 1), (8, 1, 1, 1, 8, 1, 8),
                         (1, 7, 4, 3, 8, 6, 2), (9, 2, 1, 5, 3, 7, 1)])
    for w in formula_cases + stress_cases:
        z, n24 = exact_formula(w)
        zd, n43 = exact_formula(dual(w))
        require(z == zd, 'z == zd')
        require(z == block_count(w), w)
        require(n24 == block_count(w, (2, 1, 4, 1)), w)
        require(n43 == block_count(w, (4, w[4], 3, w[3])), w)
        u, a, b, c, t, d, v = w
        require(n24 * (b + c + v + t) < z * (b + c + v), w)
        require(n43 * (b + c + u + t) < z * (b + c + u), w)

    fiber_words = fiber_count = 0
    for w in product(range(1, 3), repeat=7):
        nw, nf = check_fibers(w)
        fiber_words += nw
        fiber_count += nf

    cone_comparisons = cone_points = extremal_witnesses = 0
    for spine in product(range(1, 5), repeat=4):
        s, alpha, beta, U, V, T = constants(spine)
        a, b, c, d = spine
        require(2 * U - V <= alpha and 2 * V - U <= beta, '2 * U - V <= alpha and 2 * V - U <= beta')
        require(T == min((2*a+d+5*b+4*c-6)//3, (a+2*d+4*b+5*c-6)//3), 'T == min((2*a+d+5*b+4*c-6)//3, (a+2*d+4*b+5*c-6)//3)')
        require(2 * T <= a + d + 3*b + 3*c - 4, '2 * T <= a + d + 3*b + 3*c - 4')
        for t in range(1, T + 1):
            require(original_cone(spine, t + U, t, t + V), 'original_cone(spine, t + U, t, t + V)')
            extremal_witnesses += 1
        for t in range(1, T + 3):
            for u in range(1, t + U + 3):
                for v in range(1, t + V + 3):
                    actual = original_cone(spine, u, t, v)
                    require(actual == envelope(spine, u, t, v), (spine, u, t, v))
                    cone_comparisons += 1
                    cone_points += actual

    singleton = []
    spine = (1, 1, 1, 1)
    _, _, _, U, V, T = constants(spine)
    for t in range(1, T + 1):
        for u in range(2, t + U + 1):
            for v in range(2, t + V + 1):
                if original_cone(spine, u, t, v):
                    singleton.append([u, t, v])
    require(singleton == [[2, 1, 2], [3, 2, 3]], 'singleton == [[2, 1, 2], [3, 2, 3]]')

    result = {
        'status': 'PASS',
        'formula_box': {'weights': 'each wi in {1,2,3}', 'vectors': len(formula_cases)},
        'deterministic_stress_cases': stress_cases,
        'total_formula_vectors': len(formula_cases) + len(stress_cases),
        'independent_block_dp_counts': 3 * (len(formula_cases) + len(stress_cases)),
        'strict_probability_bound_checks': 2 * (len(formula_cases) + len(stress_cases)),
        'complete_fiber_box': {'weights': 'each wi in {1,2}', 'vectors': 128,
                               'complete_words': fiber_words, 'conditioning_fibers': fiber_count},
        'integer_cone': {'spine_weights': 'each of a,b,c,d in {1,2,3,4}', 'spine_vectors': 256,
                         'candidate_triples_compared': cone_comparisons, 'cone_triples': cone_points,
                         'componentwise_extremal_witnesses': extremal_witnesses,
                         'test_range': '1<=t<=T+2, 1<=u<=t+U+2, 1<=v<=t+V+2'},
        'singleton_spine_cone': singleton,
        'scope': 'Exact finite checks validate implementations. Universal claims have direct proofs; all-positive seven-weight balance remains open.'
    }
    output = Path(__file__).with_name('verification.json')
    output.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({k: v for k, v in result.items() if k != 'deterministic_stress_cases'}, indent=2))


if __name__ == '__main__':
    run()
