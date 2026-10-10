"""Independent S104 audit: explicit closures and exact complete-extension sets.
No dependencies on check_joint_square.py. Experiments are not a proof.
"""
from itertools import combinations
from fractions import Fraction

def close(n, edges):
    reach = [set() for _ in range(n)]
    for x, y in edges:
        reach[x].add(y)
    for k in range(n):
        for i in range(n):
            if k in reach[i]:
                reach[i] |= reach[k]
    assert all(i not in reach[i] for i in range(n)), 'cycle'
    return tuple(frozenset(x) for x in reach)

def lower(up):
    return tuple(frozenset(x for x, ys in enumerate(up) if y in ys) for y in range(len(up)))

def extensions(up):
    pred = lower(up)
    out = set()
    def dfs(prefix, remaining):
        if not remaining:
            out.add(prefix)
        else:
            for x in remaining:
                if not (pred[x] & remaining):
                    dfs(prefix + (x,), remaining - {x})
    dfs((), frozenset(range(len(up))))
    return out

def neutral(up, down, a, b):
    return frozenset(range(len(up))) - {a, b} - up[a] - up[b] - down[a] - down[b]

def cells(up, down, exts, a, b):
    out = [[0, 0, 0, 0], [0, 0, 0, 0]]
    for ext in exts:
        loc = {v: i for i, v in enumerate(ext)}
        direction = int(loc[a] > loc[b])
        x, y = (a, b) if direction == 0 else (b, a)
        succ = any(loc[x] < loc[z] < loc[y] for z in up[x])
        pred = any(loc[x] < loc[z] < loc[y] for z in down[y])
        out[direction][succ + 2 * pred] += 1
        swapped = tuple(y if z == x else x if z == y else z for z in ext)
        assert (swapped in exts) == (not succ and not pred)
    return out

def run():
    total = allpairs = eligible = 0
    for n in range(2, 6):
        possible = list(combinations(range(n), 2))
        snapshots = set()
        for mask in range(1 << len(possible)):
            snapshots.add(close(n, (e for i, e in enumerate(possible) if mask & (1 << i))))
        for up in snapshots:
            total += 1
            down = lower(up)
            original = extensions(up)
            edges = [(x, y) for x in range(n) for y in up[x]]
            for a, b in possible:
                if b in up[a]:
                    continue
                allpairs += 1
                D, U = down[a] | down[b], up[a] | up[b]
                N = neutral(up, down, a, b)
                assert not D & U
                low = close(n, edges + [(d, v) for d in D for v in (a, b)])
                high = close(n, edges + [(v, u) for u in U for v in (a, b)])
                lowdown, highdown = lower(low), lower(high)
                assert b not in low[a] and a not in low[b]
                assert b not in high[a] and a not in high[b]
                assert lowdown[a] == lowdown[b] == D
                assert low[a] == up[a] and low[b] == up[b]
                assert high[a] == high[b] == U
                assert highdown[a] == down[a] and highdown[b] == down[b]
                assert neutral(low, lowdown, a, b) == neutral(high, highdown, a, b) == N
                low_exts, high_exts = extensions(low), extensions(high)
                low_event, high_event = set(), set()
                for ext in original:
                    where = {v: i for i, v in enumerate(ext)}
                    if all(where[d] < min(where[a], where[b]) for d in D):
                        low_event.add(ext)
                    if all(where[u] > max(where[a], where[b]) for u in U):
                        high_event.add(ext)
                assert low_exts == low_event and high_exts == high_event
                original_cells = cells(up, down, original, a, b)
                h, r, l, k = original_cells[0]
                hh, rr, ll, kk = original_cells[1]
                assert h == hh and h > 0
                assert cells(low, lowdown, low_exts, a, b) == [[h, r, 0, 0], [h, rr, 0, 0]]
                assert cells(high, highdown, high_exts, a, b) == [[h, 0, l, 0], [h, 0, ll, 0]]
                assert len(low_exts) == 2*h+r+rr and len(high_exts) == 2*h+l+ll
                if all(y in up[x] or x in up[y] for x, y in combinations(N, 2)):
                    eligible += 1
                    assert r*rr <= h*h and l*ll <= h*h
        print(f'n={n}: {len(snapshots)} posets; cumulative all pairs={allpairs}, eligible pairs={eligible}')
    # Exact six-point example, a=1,b=4.
    up = close(6, [(0, 1), (1, 2), (3, 4), (4, 5)])
    example_exts = extensions(up)
    assert len(example_exts) == 20
    assert cells(up, lower(up), example_exts, 1, 4) == [[4, 2, 2, 2], [4, 2, 2, 2]]
    h, r, l, k, rr, ll, kk = map(Fraction, ('12/100','24/100','24/100','15/100','4/100','4/100','5/100'))
    p, beta = h+r+l+k, 1-(h+r+l+k)
    assert 2*h+r+l+k+rr+ll+kk == 1 and all(x>0 for x in (h,r,l,k,rr,ll,kk))
    assert p > Fraction(2,3) and r*rr < h*h and l*ll < h*h
    assert r+k <= 2*beta and l+k <= 2*beta and rr+kk <= beta and ll+kk <= beta
    assert r+l+k-rr-ll-kk == 2*p-1
    print(f'PASS: {total} posets, {allpairs} structural pairs, {eligible} neutral-chain pairs; six-point and rational-relaxation examples exact.')

if __name__ == '__main__':
    run()
