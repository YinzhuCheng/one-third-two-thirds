#!/usr/bin/env python3
"""Independent exact actual-poset checks. No project transfer code is imported."""
from fractions import Fraction
from itertools import permutations
from pathlib import Path
from math import factorial
import json

OUT = Path(__file__).resolve().parent
stats = {"natural_posets": 0, "positive_blocks": 0, "positive_entries": 0,
         "permutation_entry_checks": 0, "common_transition_checks": 0,
         "degree_one_incomparable_pairs": 0}

def validate(pred):
    n = len(pred)
    for j, p in enumerate(pred):
        assert p >> j == 0
        for i in range(j):
            if p >> i & 1:
                assert pred[i] & ~p == 0
    return max((sum(1 for j in range(n) if i != j and
                    not ((pred[j] >> i & 1) if i < j else (pred[i] >> j & 1)))
                for i in range(n)), default=0)

def solve(pred):
    n = len(pred); full = (1 << n) - 1
    layers = [{0: 1}]; successors = {}
    for r in range(n):
        nxt = {}
        for mask, f in layers[-1].items():
            edges = []
            for j, p in enumerate(pred):
                if not mask >> j & 1 and not p & ~mask:
                    m = mask | (1 << j)
                    edges.append((j + 1, m))
                    nxt[m] = nxt.get(m, 0) + f
            successors[mask] = edges
        layers.append(nxt)
    back = {full: 1}
    for layer in reversed(layers[:-1]):
        for mask in layer:
            back[mask] = sum(back[m] for _, m in successors[mask])
    assert back[0] == layers[-1][full]
    return {"pred": pred, "n": n, "layers": layers, "succ": successors,
            "B": back, "E": back[0]}

def key(mask, r, D, n):
    lo = max(0, r - D); hi = min(n, r + D)
    assert mask & ((1 << lo) - 1) == (1 << lo) - 1
    assert mask >> hi == 0
    return tuple(i + 1 - r for i in range(lo, hi) if mask >> i & 1)

def profiles(sol, r, D):
    f = {}; b = {}
    for mask, count in sol["layers"][r].items():
        k = key(mask, r, D, sol["n"])
        assert k not in f
        f[k] = count; b[k] = sol["B"][mask]
    return f, b

def transitions(sol, r, D):
    return {(key(mask, r, D, sol["n"]), j - r,
             key(nxt, r + 1, D, sol["n"]))
            for mask in sol["layers"][r] for j, nxt in sol["succ"][mask]}

def block(sol, a, b, D, pair=None):
    result = {}; event = {}
    for initial in sol["layers"][a]:
        start = key(initial, a, D, sol["n"])
        paths = {(initial, 0): 1}
        for r in range(a, b):
            nxtpaths = {}
            for (mask, flag), count in paths.items():
                for j, nxt in sol["succ"][mask]:
                    nf = flag
                    if pair and not flag:
                        if j == pair[0]: nf = 1
                        elif j == pair[1]: nf = 2
                    k = (nxt, nf)
                    nxtpaths[k] = nxtpaths.get(k, 0) + count
            paths = nxtpaths
        for (mask, flag), count in paths.items():
            end = key(mask, b, D, sol["n"]); k = (start, end)
            result[k] = result.get(k, 0) + count
            if flag == 1: event[k] = event.get(k, 0) + count
            if pair: assert flag in (1, 2)
    return result, event

def probability(sol, x, y):
    total = 0; bits = (1 << (x - 1)) | (1 << (y - 1))
    for layer in sol["layers"][:-1]:
        for mask, count in layer.items():
            if mask & bits: continue
            for j, nxt in sol["succ"][mask]:
                if j == x: total += count * sol["B"][nxt]
    return Fraction(total, sol["E"])

def natural_posets(n, pred=()):
    if len(pred) == n:
        yield list(pred); return
    for s in range(1 << len(pred)):
        if all(not (s >> j & 1) or not p & ~s for j, p in enumerate(pred)):
            yield from natural_posets(n, pred + (s,))

def exhaustive(max_n=6):
    by_n = []
    for n in range(max_n + 1):
        count = 0
        for pred in natural_posets(n):
            count += 1; stats["natural_posets"] += 1
            D = validate(pred)
            if not D or 2 * D > n: continue
            sol = solve(pred); M = factorial(2 * D)
            if D == 1:
                for y in range(1, n + 1):
                    for x in range(1, y):
                        if not pred[y - 1] >> (x - 1) & 1:
                            assert probability(sol, x, y) == Fraction(1, 2)
                            stats["degree_one_incomparable_pairs"] += 1
            for r in range(n - 2 * D + 1):
                tab, _ = block(sol, r, r + 2 * D, D)
                stats["positive_blocks"] += 1
                for j in sol["layers"][r]:
                    for k in sol["layers"][r + 2 * D]:
                        assert not j & ~k
                        v = tab[(key(j, r, D, n), key(k, r + 2 * D, D, n))]
                        assert 1 <= v <= M
                        stats["positive_entries"] += 1
                        if n <= 5:
                            labels = [i for i in range(n) if (k ^ j) >> i & 1]
                            good = 0
                            for perm in permutations(labels):
                                seen = j; ok = True
                                for i in perm:
                                    if pred[i] & ~seen: ok = False; break
                                    seen |= 1 << i
                                good += ok
                            assert good == v
                            stats["permutation_entry_checks"] += 1
        by_n.append({"n": n, "posets": count})
    return by_n

def serial(n, gaps):
    return [sum(1 << i for i in range(j) if j - i not in gaps) for j in range(n)]

def ordinal_segments(pred, cuts):
    n = len(pred); cuts = sorted({0, n, *cuts}); new = []
    for start, end in zip(cuts, cuts[1:]):
        for j in range(start, end):
            new.append(pred[j] | ((1 << start) - 1))
    return new

def ratio_range(p, q):
    assert p.keys() == q.keys()
    vals = [Fraction(q[k], p[k]) for k in p]
    return max(vals) / min(vals)

def fmt(q):
    return {"exact": str(q), "decimal": float(q)}

def local_case(name, P, Q, x, y, shift, D, m, induced=False):
    assert D >= 1 and m >= 0
    assert validate(P) <= D and validate(Q) <= D
    np, nq = len(P), len(Q); xp, yp = x + shift, y + shift
    radius = 2 * D * (m + 1)
    lo, hi = max(1, x - radius), min(np, y + radius)
    lq, hq = max(1, xp - radius), min(nq, yp + radius)
    assert (lq, hq) == (lo + shift, hi + shift)
    if not induced:
        assert (lo == 1) == (lq == 1) and (hi == np) == (hq == nq)
    else:
        assert Q == [((p >> (lo - 1)) & ((1 << (hi - lo + 1)) - 1)) for p in P[lo - 1:hi]]
    for j in range(lo, hi + 1):
        for i in range(lo, j):
            assert (P[j - 1] >> (i - 1) & 1) == (Q[j + shift - 1] >> (i + shift - 1) & 1)
    p, q = solve(P), solve(Q)
    a, b = max(0, x - D - 1), min(np, y + D)
    aq, bq = max(0, xp - D - 1), min(nq, yp + D)
    assert (aq, bq) == (a + shift, b + shift)
    left_exact = lo == 1; right_exact = hi == np
    start = a if left_exact else a - 2 * D * m
    stop = b if right_exact else b + 2 * D * m
    for r in range(start, stop):
        assert transitions(p, r, D) == transitions(q, r + shift, D)
        stats["common_transition_checks"] += 1
    C = factorial(2 * D) // factorial(D); M = factorial(2 * D)
    fp, _ = profiles(p, a, D); fq, _ = profiles(q, aq, D)
    _, bp = profiles(p, b, D); _, bqv = profiles(q, bq, D)
    rf, rb = ratio_range(fp, fq), ratio_range(bp, bqv)
    if left_exact: assert fp == fq
    else:
        f0, _ = profiles(p, start, D); f1, _ = profiles(q, start + shift, D)
        assert ratio_range(f0, f1) <= C * C
    if right_exact: assert bp == bqv
    else:
        _, b0 = profiles(p, stop, D); _, b1 = profiles(q, stop + shift, D)
        assert ratio_range(b0, b1) <= C * C
    for r in range(start, a, 2 * D):
        mat, _ = block(p, r, r + 2 * D, D)
        assert len(mat) == len(p["layers"][r]) * len(p["layers"][r + 2 * D])
        assert all(1 <= v <= M for v in mat.values())
    for r in range(b, stop, 2 * D):
        mat, _ = block(p, r, r + 2 * D, D)
        assert len(mat) == len(p["layers"][r]) * len(p["layers"][r + 2 * D])
        assert all(1 <= v <= M for v in mat.values())
    mat, marked = block(p, a, b, D, (x, y))
    matq, markedq = block(q, aq, bq, D, (xp, yp))
    assert mat == matq and marked == markedq
    ep = sum(fp[i] * v * bp[j] for (i, j), v in mat.items())
    eq = sum(fq[i] * v * bqv[j] for (i, j), v in mat.items())
    assert ep == p["E"] and eq == q["E"]
    pp, qq = probability(p, x, y), probability(q, xp, yp)
    assert pp == Fraction(sum(fp[i] * v * bp[j] for (i, j), v in marked.items()), ep)
    assert qq == Fraction(sum(fq[i] * v * bqv[j] for (i, j), v in marked.items()), eq)
    error = abs(pp - qq); distortion = rf * rb
    assert (1 + error) ** 2 <= distortion * (1 - error) ** 2
    # log C >= 2(C-1)/(C+1), and tanh z >= z/(1+z), z >= 0.
    # Thus passing this rational lower bound certifies the stated irrational bound.
    sides = int(not left_exact) + int(not right_exact)
    z = Fraction(sides * (C - 1), C + 1) * Fraction(M - 1, M + 1) ** m
    rational_lower_bound = z / (1 + z)
    assert error <= rational_lower_bound
    sizes = sorted({len(p["layers"][r]) for r in range(start, stop + 1)})
    return {"name": name, "induced_window": induced, "D": D, "m": m, "n": [np, nq], "pair": [x, y],
            "translation": shift, "matched_window": [lo, hi],
            "endpoint_exact": [left_exact, right_exact], "support_sizes": sizes,
            "extension_counts": [str(p["E"]), str(q["E"])],
            "probabilities": [fmt(pp), fmt(qq)], "error": fmt(error),
            "certified_lower_bound_on_theorem_bound": fmt(rational_lower_bound),
            "central_forward_distortion": fmt(rf), "central_backward_distortion": fmt(rb),
            "all_exact_checks_pass": True}

def long_cases():
    ans = []
    for m in [0, 1, 2, 4, 10, 50]:
        D = 2; rad = 2 * D * (m + 1); x = rad + 8; y = x + 1; n = y + rad + 9
        P = serial(n, {1}); Q = ordinal_segments(P, [x - rad - 1, y + rad])
        ans.append(local_case(f"path-two-sided-m{m}", P, Q, x, y, 0, D, m))
    for D, gaps in [(4, {1, 2}), (4, {1, 3}), (6, {1, 2, 3})]:
        for m in [0, 1, 2]:
            rad = 2 * D * (m + 1); x = rad + 5; y = x + 1; n = y + rad + 6
            P = serial(n, gaps); Q = ordinal_segments(P, [x - rad - 1, y + rad])
            ans.append(local_case(f"gaps-{sorted(gaps)}-m{m}", P, Q, x, y, 0, D, m))
    for m in [0, 1, 4, 8]:
        P = serial(40, {1}); Q = serial(55, {1})
        ans.append(local_case(f"left-clipped-m{m}", P, Q, 2, 3, 0, 2, m))
        ans.append(local_case(f"right-clipped-m{m}", P, Q, 38, 39, 15, 2, m))
    P = serial(45, {1}); Q = serial(60, {1})
    ans.append(local_case("translated-interior", P, Q, 20, 21, 5, 2, 2))
    P = ordinal_segments(serial(50, {1}), [12, 20, 29, 38])
    Q = ordinal_segments(P, [3, 45])
    ans.append(local_case("changing-legal-supports", P, Q, 24, 25, 0, 2, 4))
    P = serial(16, {1}); P = ordinal_segments(P, list(range(2, 16, 2)))
    Q = ordinal_segments(P, [1, 15])
    ans.append(local_case("degree-one", P, Q, 7, 8, 0, 1, 1))
    P = serial(8, {1})
    ans.append(local_case("both-endpoints-clipped", P, P, 4, 5, 0, 2, 2))
    ans.append(local_case("loose-D-exceeds-size", P, P, 4, 5, 0, 10, 0))
    for D, gaps, n in [(2, {1}, 89), (4, {1, 3}, 89), (6, {1, 2, 3}, 99)]:
        P = serial(n, gaps)
        for m in [0, 1, 2]:
            for x in [1, 2, n // 2, n - 2, n - 1]:
                y = x + 1; radius = 2 * D * (m + 1)
                lo, hi = max(1, x - radius), min(n, y + radius)
                Q = [(p >> (lo - 1)) & ((1 << (hi - lo + 1)) - 1) for p in P[lo - 1:hi]]
                ans.append(local_case(f"induced-D{D}-m{m}-x{x}", P, Q, x, y, 1 - lo, D, m, True))
    chain = serial(6, set()); sol = solve(chain)
    assert validate(chain) == 0 and sol["E"] == 1 and probability(sol, 2, 5) == 1
    return ans

if __name__ == "__main__":
    result = {"method": "Independent full-ideal path enumeration; integer counts and Fraction arithmetic; no imported project modules."}
    result["exhaustive_by_n"] = exhaustive()
    result["actual_poset_cases"] = long_cases()
    result["stats"] = stats
    result["status"] = "PASS"
    (OUT / "exact_checks.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({"status": "PASS", "stats": stats, "actual_poset_cases": len(result["actual_poset_cases"])}))
