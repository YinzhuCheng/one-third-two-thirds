"""Three-chain extension flow for the project ten-module template.
Reused from the S72/S75 counting helper. This is optional exact arithmetic,
not a proof of any infinite parameter statement.
"""
from functools import lru_cache
from fractions import Fraction
from itertools import accumulate


def distribution(main=(1,) * 6, outer=(1,) * 4):
    if len(main) != 6 or len(outer) != 4 or min(*main, *outer) < 1:
        raise ValueError('six positive main lengths and four positive outer lengths required')
    cuts = list(accumulate(main))
    a, b, c, d = outer
    end = (cuts[-1], a + d, b + c)

    @lru_cache(None)
    def succ(state):
        i, j, k = state
        out = []
        if i < end[0] and (i != cuts[1] or j >= a) and (i != cuts[4] or k >= b + c):
            out.append((0, (i + 1, j, k)))
        if j < a or (j < end[1] and i >= cuts[3] and k >= b):
            out.append((1, (i, j + 1, k)))
        if (k < b and i >= cuts[0]) or (b <= k < end[2] and j >= a):
            out.append((2, (i, j, k + 1)))
        return tuple(out)

    @lru_cache(None)
    def suffix(state):
        if state == end:
            return 1
        return sum(suffix(nxt) for _, nxt in succ(state))

    start = (0, 0, 0)
    total = suffix(start)
    # hist[q,r][j][i]: extensions with i elements of chain r before chain q's (j+1)-st point.
    hist = {(q, r): [[0] * (end[r] + 1) for _ in range(end[q])]
            for q in range(3) for r in range(3) if r != q}
    layer = {start: 1}
    for _ in range(sum(end)):
        nxt_layer = {}
        for state, count_prefix in layer.items():
            for q, nxt in succ(state):
                nxt_layer[nxt] = nxt_layer.get(nxt, 0) + count_prefix
                count = count_prefix * suffix(nxt)
                for r in range(3):
                    if r != q:
                        hist[q, r][state[q]][state[r]] += count
        layer = nxt_layer
    pairs = []
    for q in range(3):
        for r in range(q + 1, 3):
            for j, row in enumerate(hist[q, r]):
                cumulative = 0
                for i, value in enumerate(row[:-1]):
                    cumulative += value
                    pairs.append(((q, j + 1), (r, i + 1), cumulative))
    best = max(pairs, key=lambda p: min(p[2], total - p[2]))
    stats = dict(total=total, best=best,
                 delta=Fraction(min(best[2], total - best[2]), total),
                 states=suffix.cache_info().currsize)
    return stats, hist
