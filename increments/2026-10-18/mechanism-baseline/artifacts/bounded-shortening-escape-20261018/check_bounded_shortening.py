#!/usr/bin/env python3
"""Exact certificates for bounded shortening within the Pell (a, 2) family.

No floating point, no linear-extension enumeration, no external writes.
For b=2, all incomparable-pair probabilities reduce to t(t+1)/D.
The nearest two triangular products are located by integer square root.
"""

from fractions import Fraction
from math import comb, isqrt
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent


def delta(n, b):
    assert n >= 1 and b in (1, 2)
    if b == 1:
        return Fraction((n + 1) // 2, n + 1)
    D = (n + 1) * (n + 2)
    k = (isqrt(1 + 2 * D) - 1) // 2
    candidates = [t for t in (k, k + 1) if 1 <= t <= n]
    h = min(abs(2 * t * (t + 1) - D) for t in candidates)
    return Fraction(1, 2) - Fraction(h, 2 * D)


def check_all_pairs(n, b):
    """Independent hypergeometric all-pair check of the short-chain formulas."""
    observed = Fraction(0)
    for i in range(1, n + 1):
        for j in range(1, b + 1):
            positions = i + j - 1
            numerator = sum(
                comb(n, k) * comb(b, positions - k)
                for k in range(max(i, positions - b), min(n, positions) + 1)
            )
            p = Fraction(numerator, comb(n + b, positions))
            observed = max(observed, min(p, 1 - p))
    assert delta(n, b) == observed, (n, b, delta(n, b), observed)


def pell_members(count=10):
    x, u = 1, 0
    for power in range(1, count + 1):
        x, u = 3 * x + 8 * u, x + 3 * u
        a = (x - 3) // 2
        if a >= 2:
            assert x * x - 8 * u * u == 1
            assert (a + 1) * (a + 2) == 2 * u * u
            yield power, a, u


def within_radius(a, u, r, include_records=False):
    d0 = Fraction(u - 1, 2 * u)
    records = []
    passes = True
    for ell in (0, 1):
        for j in range(r + 1 - ell):
            if j + ell == 0 or a - j < 1:
                continue
            d1 = delta(a - j, 2 - ell)
            passes = passes and d1 > d0
            if include_records:
                records.append({
                    "j": j, "ell": ell, "total_deletions": j + ell,
                    "lengths": [a - j, 2 - ell], "delta": str(d1),
                    "delta_minus_original": str(d1 - d0),
                    "strictly_above_original": d1 > d0,
                })
    return passes, records


def theorem_witness(a, u, r):
    """Check every inequality needed at the theorem's explicit threshold."""
    assert u >= 5 * r * r
    assert a - u >= r
    d0 = Fraction(u - 1, 2 * u)
    for j in range(1, r + 1):
        # s = ceil(j/sqrt(2)); j/sqrt(2) is never an integer for j >= 1.
        s = isqrt((j * j) // 2) + 1
        assert 2 * (s - 1) ** 2 < j * j < 2 * s * s
        t = u - s
        n = a - j
        assert 1 <= t <= n
        D = (n + 1) * (n + 2)
        L = 2 * t * (t + 1) - D
        assert u * abs(L) < D
        p = Fraction(t * (t + 1), D)
        assert min(p, 1 - p) > d0
        assert delta(n, 2) >= min(p, 1 - p)
    for j in range(r):
        n = a - j
        assert n + 1 > u
        assert delta(n, 1) > d0
    assert within_radius(a, u, r)[0]


def first_escape(a, u):
    """Find first admissible endpoint with delta <= starting delta.

    At total deletion count m, the only new endpoints are (a-m,2) and
    (a-m+1,1). Earlier radii have already been checked.
    """
    d0 = Fraction(u - 1, 2 * u)
    for m in range(1, a + 1):
        failures = []
        for ell, j in ((0, m), (1, m - 1)):
            n = a - j
            if n >= 1:
                d1 = delta(n, 2 - ell)
                if d1 <= d0:
                    failures.append({"j": j, "ell": ell,
                                     "lengths": [n, 2 - ell],
                                     "delta": str(d1),
                                     "delta_minus_original": str(d1 - d0)})
        if failures:
            return {"minimum_total_deletions": m,
                    "first_nonimproving_endpoints": failures}
    raise AssertionError("(1,2) must eventually give an escape")


def main():
    for n in range(1, 201):
        for b in (1, 2):
            check_all_pairs(n, b)
    members = list(pell_members(12))
    finite_table = []
    for power, a, u in members[:9]:
        d0 = Fraction(u - 1, 2 * u)
        assert delta(a, 2) == d0
        finite_table.append({
            "power": power, "a": a, "u": u, "delta": str(d0),
            "radius_checks": {str(r): within_radius(a, u, r)[0]
                              for r in (2, 3, 5, 10)},
            **first_escape(a, u),
        })
    detailed_examples = []
    for r, index in ((2, 0), (3, 1), (5, 1), (10, 2)):
        power, a, u = members[index]
        passes, endpoints = within_radius(a, u, r, True)
        assert passes
        detailed_examples.append({"radius": r, "power": power, "a": a,
                                  "u": u, "delta": str(Fraction(u - 1, 2 * u)),
                                  "endpoints": endpoints})
    threshold_checks = []
    for r in (1, 2, 3, 5, 10, 25, 100, 1000):
        power, a, u = next(member for member in members if member[2] >= 5*r*r)
        theorem_witness(a, u, r)
        threshold_checks.append({"r": r, "power": power, "a": a, "u": u,
                                 "required_u_at_least": 5*r*r,
                                 "all_witness_inequalities_verified": True})
    output = {
        "status": "proved; finite checks are supporting certificates only",
        "explicit_sufficient_condition": "u >= 5 r^2",
        "independent_all_pair_formula_checks": 400,
        "all_pair_check_n_range": [1, 200],
        "finite_pell_table": finite_table,
        "requested_radius_examples": detailed_examples,
        "explicit_threshold_checks": threshold_checks,
    }
    (ROOT / "exact_certificates.json").write_text(
        json.dumps(output, ensure_ascii=False, indent=2) + "\n")
    print("All 400 independent all-pair checks passed.")
    print("All requested radii and explicit-threshold witnesses passed.")
    print("Pell members: a, u, radius 2/3/5/10, first escape deletion count")
    for row in finite_table:
        print(row["a"], row["u"], row["radius_checks"],
              row["minimum_total_deletions"])


if __name__ == "__main__":
    main()
