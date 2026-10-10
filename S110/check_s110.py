#!/usr/bin/env python3
"""Independent integer checks of the S110 bounded-cut profile lemma.

No dependencies beyond Python's standard library. Natural posets are generated
by independently trying every forward relation matrix and testing transitivity;
this does not assume the frontier/ratio theorem under test. Extension counts
come from the usual ideal-lattice recurrence. A second permutation-based test
checks individual deletion fibers and their tail support, for every n<=6.
"""
from __future__ import annotations

import argparse
import itertools
import json
import math
import time
from collections import Counter, defaultdict
from pathlib import Path


def natural_posets(n):
    """All transitive subrelations of the natural strict total order, once each.

    Rows are predecessor masks. Selecting a predecessor set for the new largest
    label preserves transitivity iff it contains every predecessor of each of
    its elements. This test concerns just the definition of transitivity.
    """
    pred = []

    def extend(k):
        if k == n:
            yield tuple(pred)
            return
        for s in range(1 << k):
            rem, valid = s, True
            while rem:
                bit = rem & -rem
                i = bit.bit_length() - 1
                if pred[i] & ~s:
                    valid = False
                    break
                rem -= bit
            if valid:
                pred.append(s)
                yield from extend(k + 1)
                pred.pop()

    yield from extend(0)


def successor_masks(pred):
    succ = [0] * len(pred)
    for j, p in enumerate(pred):
        for i in range(j):
            if p >> i & 1:
                succ[i] |= 1 << j
    return succ


def counts(pred):
    """Forward and backward path counts on ALL subsets, with unreachable=0."""
    n = len(pred)
    full = (1 << n) - 1
    f, b = [0] * (1 << n), [0] * (1 << n)
    f[0] = 1
    for s in range(1 << n):
        if not f[s]:
            continue
        for i, p in enumerate(pred):
            if not (s >> i & 1) and p & ~s == 0:
                f[s | (1 << i)] += f[s]
    b[full] = 1
    for s in range(full - 1, -1, -1):
        if not f[s]:
            continue
        b[s] = sum(b[s | (1 << i)] for i, p in enumerate(pred)
                   if not (s >> i & 1) and p & ~s == 0)
    return f, b


def extension_permutations(mask, pred):
    """Independent brute permutation filter, not the count recurrence."""
    elements = [i for i in range(len(pred)) if mask >> i & 1]
    for perm in itertools.permutations(elements):
        seen, valid = 0, True
        for i in perm:
            if pred[i] & mask & ~seen:
                valid = False
                break
            seen |= 1 << i
        if valid:
            yield perm


def check_fibers(inserted_set, core, pred, D, dual=False):
    """Compute every deletion fiber directly and check the common-tail claim."""
    assert core & ~inserted_set == 0
    fibers = Counter()
    a, m = (inserted_set ^ core).bit_count(), core.bit_count()
    t = min(D, m)
    bound = math.factorial(t + a) // math.factorial(t)
    for perm in extension_permutations(inserted_set, pred):
        base = tuple(i for i in perm if core >> i & 1)
        fibers[base] += 1
        ordered_perm = perm[::-1] if dual else perm
        ordered_base = base[::-1] if dual else base
        assert ordered_perm[:m - t] == ordered_base[:m - t], (
            "Tail support failed", pred, inserted_set, core, D, perm, base, dual)
    core_extensions = tuple(extension_permutations(core, pred))
    assert set(fibers) == set(core_extensions), ("Deletion is not onto", pred)
    assert all(1 <= x <= bound for x in fibers.values()), (
        "Fiber bound failed", pred, inserted_set, core, D, dict(fibers), bound)
    return len(fibers), sum(fibers.values()), min(fibers.values()), max(fibers.values())


def check_poset(pred, fiber_max, summary):
    n = len(pred)
    full = (1 << n) - 1
    succ = successor_masks(pred)
    degrees = [n - 1 - pred[i].bit_count() - succ[i].bit_count() for i in range(n)]
    D = max(degrees, default=0)
    f, b = counts(pred)
    C = math.factorial(2 * D) // math.factorial(D)
    N = math.comb(2 * D, D)
    layers = defaultdict(list)
    for s, value in enumerate(f):
        if value:
            layers[s.bit_count()].append(s)
    summary["degree_histogram"][str(D)] += 1
    summary["posets"] += 1
    summary["ideals"] += sum(map(len, layers.values()))
    for r, ideals in layers.items():
        l_size, r_start = max(0, r - D), min(n, r + D)
        L = (1 << l_size) - 1
        R = full ^ ((1 << r_start) - 1)
        W = full ^ L ^ R
        a, bb = r - l_size, r_start - r
        tf, tb = min(D, l_size), min(D, n - r_start)
        CF = math.factorial(tf + a) // math.factorial(tf)
        CB = math.factorial(tb + bb) // math.factorial(tb)
        fbase, bbase = f[L], b[full ^ R]
        k = len(ideals)
        # Determine legal support using ONLY the induced window relation.
        window_points = [i for i in range(n) if W >> i & 1]
        local_support = set()
        for choice in itertools.combinations(window_points, a):
            s_window = sum(1 << i for i in choice)
            if all(pred[i] & W & ~s_window == 0 for i in choice):
                local_support.add(L | s_window)
        assert local_support == set(ideals), ("Local support differs", pred, D, r)
        summary["exact_support_checks"] += 1
        assert k <= math.comb(W.bit_count(), a) <= N
        assert CF <= C and CB <= C
        assert fbase > 0 and bbase > 0
        SF, SB = sum(f[s] for s in ideals), sum(b[s] for s in ideals)
        E = f[full]
        assert sum(f[s] * b[s] for s in ideals) == E
        for s in ideals:
            assert L & ~s == 0 and s & R == 0, ("Guard failed", pred, D, r, s)
            assert fbase <= f[s] <= CF * fbase, ("Forward failed", pred, D, r, s)
            assert bbase <= b[s] <= CB * bbase, ("Backward failed", pred, D, r, s)
            # All normalized bounds are checked by exact integer comparison.
            assert f[s] * (1 + (k - 1) * CF) >= SF
            assert f[s] * (CF + k - 1) <= CF * SF
            assert b[s] * (1 + (k - 1) * CB) >= SB
            assert b[s] * (CB + k - 1) <= CB * SB
            assert f[s] * b[s] * (1 + (k - 1) * CF * CB) >= E
            assert f[s] * b[s] * (CF * CB + k - 1) <= CF * CB * E
            summary["ratio_checks"] += 2
            summary["normalized_checks"] += 6
            # Also test every permissible LOOSER D, not only pi(P).
            for DD in range(D + 1, n + 1):
                LL = (1 << max(0, r - DD)) - 1
                RR = full ^ ((1 << min(n, r + DD)) - 1)
                CC = math.factorial(2 * DD) // math.factorial(DD)
                assert f[LL] <= f[s] <= CC * f[LL]
                assert b[full ^ RR] <= b[s] <= CC * b[full ^ RR]
                summary["looser_degree_ratio_checks"] += 2
            if n <= fiber_max:
                f_result = check_fibers(s, L, pred, D)
                b_result = check_fibers(full ^ s, R, pred, D, dual=True)
                assert f_result[0] == fbase and f_result[1] == f[s]
                assert b_result[0] == bbase and b_result[1] == b[s]
                summary["fiber_groups"] += f_result[0] + b_result[0]
                summary["permutation_extensions"] += f_result[1] + b_result[1]
                if f_result[2] != f_result[3] or b_result[2] != b_result[3]:
                    summary["nonuniform_fiber_profiles"] += 1


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-n", type=int, default=7)
    parser.add_argument("--fiber-max-n", type=int, default=6)
    parser.add_argument("--output", default="s110_checks.json")
    args = parser.parse_args()
    results = {"method": "All naturally labelled posets; exact ideal DP and independent direct permutations",
               "max_n": args.max_n, "fiber_max_n": args.fiber_max_n,
               "per_n": [], "passed": False}
    start = time.time()
    known_counts = [1, 1, 2, 7, 40, 357, 4824, 96428]
    for n in range(args.max_n + 1):
        summary = {"n": n, "posets": 0, "ideals": 0, "ratio_checks": 0,
                   "exact_support_checks": 0,
                   "normalized_checks": 0, "looser_degree_ratio_checks": 0,
                   "fiber_groups": 0, "permutation_extensions": 0,
                   "nonuniform_fiber_profiles": 0, "degree_histogram": Counter()}
        for pred in natural_posets(n):
            check_poset(pred, args.fiber_max_n, summary)
        if n < len(known_counts):
            assert summary["posets"] == known_counts[n]
        results["per_n"].append(summary)
        print(json.dumps(summary, sort_keys=True), flush=True)
    results["passed"] = True
    results["elapsed_seconds"] = round(time.time() - start, 3)
    Path(args.output).write_text(json.dumps(results, indent=2, sort_keys=True) + "\n")
    print("PASS", args.output, results["elapsed_seconds"], flush=True)


if __name__ == "__main__":
    main()
