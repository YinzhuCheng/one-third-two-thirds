"""S69 optional exact arithmetic; the proof is in ../notes/PROOF.md.
Not a proof gate, formal verifier, or independent proof of the formulas.
Python standard library only.
"""
from __future__ import annotations
from fractions import Fraction
from math import comb
import argparse


def _nonnegative(a: int, b: int) -> None:
    if a < 0 or b < 0:
        raise ValueError("Chain lengths must be nonnegative (zero is auxiliary).")


def head_count(a: int, b: int) -> int:
    """Extensions with c1 before every U copy."""
    _nonnegative(a, b)
    return 3 * comb(a + b, a) + (a + 1) * sum(
        weight * comb(a + b + s + 1, b)
        for s, weight in enumerate((3, 3, 5, 3))
    )


def extension_count(a: int, b: int) -> int:
    _nonnegative(a, b)
    return sum(head_count(p, b) for p in range(a + 1))


def c3_masses(a: int, b: int) -> list[int]:
    """N[j] counts extensions with j V copies before c3."""
    _nonnegative(a, b)
    out = []
    for j in range(b + 1):
        k = b - j
        block = (j + 1) * comb(a + j + 2, j + 2)
        value = block * (3 + 5 * (k + 1) + 3 * comb(k + 2, 2))
        if j == b:
            value += 3 * block + 3 * comb(a + b + 1, b + 1)
        out.append(value)
    return out


def c3_before_v(a: int, b: int, t: int) -> Fraction:
    if not 1 <= t <= b:
        raise ValueError("The V copy index must lie between 1 and b.")
    return Fraction(sum(c3_masses(a, b)[:t]), extension_count(a, b))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("a", type=int, nargs="?", default=3)
    parser.add_argument("b", type=int, nargs="?", default=50)
    parser.add_argument("--v", type=int, default=None)
    args = parser.parse_args()
    try:
        E = extension_count(args.a, args.b)
        print(f"E({args.a},{args.b}) = {E}")
        if args.a >= 1:
            print("p(c1<u1) =", Fraction(head_count(args.a, args.b), E))
        if args.v is not None:
            p = c3_before_v(args.a, args.b, args.v)
            print(f"p(c3<v_{args.v}) = {p}; smaller direction = {min(p, 1-p)}")
    except ValueError as exc:
        parser.error(str(exc))


if __name__ == "__main__":
    main()
