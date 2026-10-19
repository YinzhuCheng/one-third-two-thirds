#!/usr/bin/env python3
"""Exact local shuffle controls; no enumeration of posets or delta values."""
from fractions import Fraction
from itertools import combinations
from math import comb
from pathlib import Path
import json


def pmf(m, K, r, j):
    assert m >= 2 and 1 <= r <= K and 0 <= j <= m
    return Fraction(
        comb(j + r - 1, r - 1) * comb(m - j + K - r, K - r),
        comb(m + K, K),
    )


formula_cases = 0
internal_cases = 0
normalizations = 0
for m in range(2, 21):
    for K in range(1, 21):
        bound = Fraction(K, m + K)
        for r in range(1, K + 1):
            values = [pmf(m, K, r, j) for j in range(m + 1)]
            assert sum(values) == 1
            normalizations += 1
            for j, p in enumerate(values):
                assert p <= bound
                assert p == pmf(m, K, K + 1 - r, m - j)
                formula_cases += 1
                if K == 1:
                    assert p == bound
                else:
                    assert (p == bound) == ((r, j) in ((1, 0), (K, m)))
                if 1 <= j < m:
                    internal_cases += 1
                    if K >= 2:
                        assert p < bound
                    if m >= K:
                        sharp_bound = Fraction(m * K, (m + K) * (m + K - 1))
                        assert p <= sharp_bound <= Fraction(1, 3)
                    if m >= 2 * K:
                        assert p <= Fraction(1, 3)

sharp_parameter_pairs = 0
for m in range(2, 21):
    for t in range(1, m + 1):
        sharp_bound = Fraction(m * t, (m + t) * (m + t - 1))
        assert pmf(m, t, 1, 1) == sharp_bound
        assert sharp_bound <= Fraction(1, 3)
        assert (sharp_bound == Fraction(1, 3)) == ((m, t) in ((2, 1), (2, 2)))
        sharp_parameter_pairs += 1
        for K in range(1, t):
            now = Fraction(m * K, (m + K) * (m + K - 1))
            after = Fraction(m * (K + 1), (m + K + 1) * (m + K))
            exact_difference = Fraction(
                m * (m - K - 1), (m + K - 1) * (m + K) * (m + K + 1)
            )
            assert after - now == exact_difference >= 0

# Directly enumerate only short uniform shuffles, independently of the formula.
subset_count = 0
subset_histograms = 0
for m in range(2, 8):
    for K in range(1, 8):
        hist = [[0] * (m + 1) for _ in range(K)]
        subsets = list(combinations(range(1, m + K + 1), K))
        subset_count += len(subsets)
        for positions in subsets:
            for r, x in enumerate(positions, 1):
                j = x - r
                hist[r - 1][j] += 1
        for r in range(1, K + 1):
            for j in range(m + 1):
                assert Fraction(hist[r - 1][j], len(subsets)) == pmf(m, K, r, j)
                subset_histograms += 1

# Actual P = chain(c1,c2) disjoint union chain(a,y,b).
example = [pmf(2, 3, 2, j) for j in range(3)]
q1 = example[1] + example[2]
q2 = example[2]
assert example == [Fraction(3, 10), Fraction(4, 10), Fraction(3, 10)]
assert (q1, q2) == (Fraction(7, 10), Fraction(3, 10))
assert (q1 + q2) / 2 == Fraction(1, 2)

result = {
    "scope": "Local shuffle law and threshold arithmetic only; no poset/delta classification.",
    "exact_arithmetic": "fractions.Fraction and integer binomial coefficients",
    "formula_grid": {"m": [2, 20], "K": [1, 20]},
    "pmf_values_checked": formula_cases,
    "internal_pmf_values_checked": internal_cases,
    "normalizations_checked": normalizations,
    "sharp_bound_parameter_pairs_checked": sharp_parameter_pairs,
    "direct_subset_grid": {"m": [2, 7], "K": [1, 7]},
    "direct_subsets_enumerated": subset_count,
    "direct_histogram_entries_checked": subset_histograms,
    "example": {"m": 2, "K": 3, "r": 2,
                "J_distribution": [str(v) for v in example],
                "q": [str(q1), str(q2)], "shortened_probability": "1/2"},
    "status": "all checks passed",
}
Path(__file__).with_name("CHECKS.json").write_text(
    json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
)
print(json.dumps(result, ensure_ascii=False, indent=2))
