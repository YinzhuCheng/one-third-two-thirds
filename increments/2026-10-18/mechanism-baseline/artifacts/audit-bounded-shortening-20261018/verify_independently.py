#!/usr/bin/env python3
"""Independent exact checks for the bounded-shortening Pell barrier.

Only Python's standard library is used.  This file does not import or modify
the producer's code and writes no files.  It enumerates only placements of
one or two B labels for small n, never a large set of linear extensions.
Large-n maxima are found by integer binary search, not by the producer's
integer-square-root implementation.  Finite checks do not replace the proof.
"""

from fractions import Fraction
from itertools import combinations
from math import isqrt


def placement_counts(n, b):
    """Count every labelled A_i < B_j event directly from B positions."""
    counts = [[0] * b for _ in range(n)]
    total = 0
    for bp in combinations(range(n + b), b):
        bs = set(bp)
        ap = [p for p in range(n + b) if p not in bs]
        total += 1
        for i, p in enumerate(ap):
            for j, q in enumerate(bp):
                counts[i][j] += p < q
    return total, counts


def direct_formula(n, i, j, b):
    if b == 1:
        return Fraction(n + 1 - i, n + 1)
    D = (n + 1) * (n + 2)
    if j == 1:
        return Fraction((n + 1 - i) * (n + 2 - i), D)
    return 1 - Fraction(i * (i + 1), D)


def delta_by_binary_search(n, b):
    if b == 1:
        return Fraction((n + 1) // 2, n + 1)
    D = (n + 1) * (n + 2)
    lo, hi = 0, n + 1
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if 2 * mid * (mid + 1) <= D:
            lo = mid
        else:
            hi = mid
    candidates = [t for t in (lo, hi) if 1 <= t <= n]
    return max(min(Fraction(t * (t + 1), D),
                   1 - Fraction(t * (t + 1), D)) for t in candidates)


def pell_at_threshold(r):
    a, u = 7, 6
    while u < 5 * r * r:
        a, u = 3 * a + 4 * u + 3, 2 * a + 3 * u + 3
    assert (a + 1) * (a + 2) == 2 * u * u
    return a, u


def check_long_witness(a, u, r, j):
    assert 1 <= j <= r and u >= 5 * r * r
    s = isqrt((j * j) // 2) + 1
    assert 2 * (s - 1) ** 2 < j * j < 2 * s * s
    # These are precisely the squared rational inequalities
    # sqrt(2)j - 2(s-1) > 1/(2j) and 2s - sqrt(2)j > 1/(2j).
    assert (4 * j * (s - 1) + 1) ** 2 < 8 * j**4
    assert 8 * j**4 < (4 * j * s - 1) ** 2
    C = 2 * s * (s - 1) - j * j
    assert 4 * C * C < 9 * j * j
    n, t = a - j, u - s
    assert 1 <= t <= n
    D = (n + 1) * (n + 2)
    L = 2 * t * (t + 1) - D
    # This is the final strictly positive exact numerator, without radicals.
    slack = D - u * abs(L)
    assert slack > 0
    old = Fraction(u - 1, 2 * u)
    p = Fraction(t * (t + 1), D)
    assert min(p, 1 - p) > old
    assert delta_by_binary_search(n, 2) >= min(p, 1 - p)
    return slack


def check_short_endpoint(a, u, j):
    n = a - j
    assert n >= 1 and n + 1 > u
    assert delta_by_binary_search(n, 1) > Fraction(u - 1, 2 * u)


def main():
    pair_count = 0
    object_count = 0
    for n in range(1, 41):
        for b in (1, 2):
            E, counts = placement_counts(n, b)
            d = Fraction(0)
            for i in range(1, n + 1):
                for j in range(1, b + 1):
                    p = Fraction(counts[i - 1][j - 1], E)
                    assert p == direct_formula(n, i, j, b)
                    d = max(d, min(p, 1 - p))
                    pair_count += 1
            assert d == delta_by_binary_search(n, b)
            object_count += 1

    # An independent full-t maximum check, without enumeration of extensions.
    for n in range(1, 1001):
        D = (n + 1) * (n + 2)
        all_t = max(Fraction(min(t * (t + 1), D - t * (t + 1)), D)
                    for t in range(1, n + 1))
        assert all_t == delta_by_binary_search(n, 2)

    rows = []
    for r in (1, 2, 3, 5, 10, 25, 100, 1000, 10**6, 10**12):
        a, u = pell_at_threshold(r)
        assert a - u >= r
        assert delta_by_binary_search(a, 2) == Fraction(u - 1, 2 * u)
        if r <= 1000:
            js = list(range(1, r + 1))
            short_js = list(range(r))
            scope = "all endpoints"
        else:
            js = sorted({1, 2, 3, r, r - 1, r - 2, r // 2, isqrt(r)})
            short_js = sorted({0, 1, r - 1, r - 2, r // 2})
            scope = "selected endpoints only"
        slacks = [check_long_witness(a, u, r, j) for j in js]
        for j in short_js:
            check_short_endpoint(a, u, j)
        rows.append((r, a, u, len(js), len(short_js), min(slacks), scope))

    # Smallest-family boundary: radius 2 holds but radius 3 already fails.
    assert delta_by_binary_search(7, 2) == Fraction(5, 12)
    assert delta_by_binary_search(6, 2) == Fraction(13, 28)
    assert delta_by_binary_search(7, 1) == Fraction(1, 2)
    assert delta_by_binary_search(5, 2) > Fraction(5, 12)
    assert delta_by_binary_search(6, 1) > Fraction(5, 12)
    assert delta_by_binary_search(4, 2) == Fraction(2, 5) < Fraction(5, 12)

    print(f"PASS: {object_count} small objects, {pair_count} individual pair probabilities.")
    print("PASS: all-t maxima independently checked for n=1,...,1000.")
    print("r | a | u | long checks | short checks | minimum witness slack D-u|L| | scope")
    for row in rows:
        print(" | ".join(map(str, row)))
    print("PASS: smallest Pell member r=1 boundary and radius-3 escape.")
    print("No floating point, producer import, external write, or large-extension enumeration.")


if __name__ == "__main__":
    main()
