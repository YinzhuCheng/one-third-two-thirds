#!/usr/bin/env python3
"""S71 finite arithmetic appendix.

Only evaluate the binomial formulas in S71/notes/PROOF.md.
This is not a proof-validation gate and does not enumerate linear extensions.
Run: python S71/src/finite_core.py --output S71/evidence/finite_core.csv
"""
from __future__ import annotations
import argparse
import csv
from fractions import Fraction
from itertools import product
from math import comb
from pathlib import Path

Pair = tuple[str, str]

def upper_coefficients(h: int, d: int) -> tuple[int, tuple[int, ...]]:
    """Proof (1.3): five classes of upper-module orders."""
    B = lambda s: (s + 1) * comb(s + d + 2, d)
    r = sum(comb(h - s + 1, 2) * B(s) for s in range(h))
    a0 = sum((h - s) * B(s) for s in range(h))
    a1 = sum(B(s) for s in range(h))
    a3 = comb(h + d + 1, d)
    a2 = (h + 1) * comb(h + d + 2, d) - a3
    return r, (a0, a1, a2, a3)

def one_side(a: int, b: int, h: int, d: int) -> tuple[int, dict[Pair, int]]:
    """The c1/c2 event counts in (3.1)-(3.5) and (6.1)."""
    if min(a, b, h, d) < 1:
        raise ValueError("All four chain lengths must be positive.")
    r, alpha = upper_coefficients(h, d)
    C = comb(a + b + 1, a)
    R = r * C
    D = [sum(alpha[s] * comb(b + t + s + 1, b) for s in range(4))
         for t in range(a + 1)]
    E = R + sum((t + 1) * v for t, v in enumerate(D))
    L = [sum(D[k:]) + (R if k == 0 else 0) for k in range(a + 1)]
    Acoef = lambda q: (alpha[0] * int(q == 0) + alpha[1]
                       + alpha[2] * (q + 1) + alpha[3] * comb(q + 2, 2))
    T = [comb(a + j + 2, a) * Acoef(b - j) for j in range(b + 1)]
    F = lambda t: sum((j + 1) * comb(t + j + 3, j + 3)
                      for j in range(d + 1))
    Q = [sum(T[k:]) for k in range(b + 1)]
    Q += [C * F(h - q) for q in range(1, h + 1)]
    events = {("c1", "u1"): r * comb(a + b, a) + (a + 1) * D[a]}
    for t in range(1, a + 1):
        events[(f"u{a-t+1}", "c2")] = sum(L[:t])
    for t in range(1, b + h + 1):
        events[("c2", f"v{t}" if t <= b else f"w{t-b}")] = sum(Q[:t])
    return E, events

def from_dual(label: str, a: int, b: int, h: int, d: int) -> str:
    """Dual parameters are (d,h,b,a); labels reverse within a module."""
    kind, i = label[0], int(label[1:])
    if kind == "c":
        return f"c{7-i}"
    target, length = {"u": ("z", d), "v": ("w", h),
                      "w": ("v", b), "z": ("u", a)}[kind]
    return f"{target}{length+1-i}"

def finite_witness(a: int, b: int, h: int, d: int) -> tuple[int, Pair, int]:
    E, events = one_side(a, b, h, d)
    _, dual_events = one_side(d, h, b, a)
    for (x, y), N in dual_events.items():
        events[(from_dual(y, a, b, h, d), from_dual(x, a, b, h, d))] = N
    pair, N = min(events.items(), key=lambda item: abs(2 * item[1] - E))
    if (a, b, h, d) == (1, 3, 3, 1):
        # Proof (6.2), not a hard-coded probability.
        _, alpha = upper_coefficients(h, d)
        t = 3
        N = sum((j+1) * comb(a+j+2, a) *
                (alpha[1] + alpha[2]*(b-j+1) + alpha[3]*comb(b-j+2, 2))
                for j in range(t))
        pair = ("c3", "v3")
    return E, pair, N

def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path,
                        default=Path(__file__).resolve().parents[1] / "evidence/finite_core.csv")
    args = parser.parse_args()
    rows = []
    for a, b, h, d in product(range(1, 6), range(1, 5), range(1, 5), range(1, 6)):
        if (a, b, h, d) == (1, 1, 1, 1):
            continue
        E, (x, y), N = finite_witness(a, b, h, d)
        rows.append((a, b, h, d, E, x, y, N, E-N, 5*N-2*E, 3*E-5*N))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(("a", "b", "h", "d", "E", "x", "y", "N_x_before_y",
                         "E_minus_N", "5N_minus_2E", "3E_minus_5N"))
        writer.writerows(rows)
    weakest = min(rows, key=lambda r: Fraction(min(r[7], r[8]), r[4]))
    print(f"Rows: {len(rows)}")
    print(f"Smallest displayed slack: {min(min(r[-2:]) for r in rows)}")
    print(f"Weakest selected fraction: {Fraction(min(weakest[7:9]), weakest[4])}")
    print(f"Output: {args.output}")

if __name__ == "__main__":
    main()
