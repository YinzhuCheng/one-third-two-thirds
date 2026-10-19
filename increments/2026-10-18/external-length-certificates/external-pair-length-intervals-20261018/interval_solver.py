"""Exact integer length intervals for the completely external-pair mechanism.

No scan over the current or target chain lengths.  Standard-library only.
All intervals are inclusive integer intervals (lo, hi); hi=None means infinity.
The mathematical domain is k >= 1.  Numerators are actual K-window counts.
"""
from math import isqrt
from typing import Optional

Interval = tuple[int, Optional[int]]


def merge(intervals: list[Interval]) -> list[Interval]:
    """Union of inclusive integer intervals, merging integer-adjacent pieces."""
    out = []
    for lo, hi in sorted(intervals, key=lambda item: item[0]):
        if hi is not None and hi < lo:
            continue
        if not out:
            out.append((lo, hi))
            continue
        old_lo, old_hi = out[-1]
        if old_hi is None:
            break
        if lo <= old_hi + 1:
            new_hi = None if hi is None else max(old_hi, hi)
            out[-1] = (old_lo, new_hi)
        else:
            out.append((lo, hi))
    return out


def intersect(left: list[Interval], right: list[Interval]) -> list[Interval]:
    out = []
    for a, b in left:
        for c, d in right:
            lo = max(a, c)
            hi = d if b is None else b if d is None else min(b, d)
            if hi is None or lo <= hi:
                out.append((lo, hi))
    return merge(out)


def rational_floor_ceil(p: int, q: int) -> tuple[int, int]:
    assert q != 0
    if q < 0:
        p, q = -p, -q
    return p // q, -((-p) // q)


def radical_floor_ceil(p: int, sign: int, delta: int, q: int) -> tuple[int, int]:
    """floor/ceil((p + sign*sqrt(delta))/q), using integer arithmetic only."""
    assert sign in (-1, 1) and delta >= 0 and q > 0
    s = isqrt(delta)
    if s * s == delta:
        return rational_floor_ceil(p + sign * s, q)
    # sqrt(delta) lies strictly between the adjacent integers s and s+1.
    floor = (p + s) // q if sign == 1 else (p - s - 1) // q
    return floor, floor + 1


def positive_intervals(A: int, B: int, C: int, upper: Optional[int] = None) -> list[Interval]:
    """Exactly {k in Z: 1 <= k <= upper and A*k*k+B*k+C > 0}."""
    domain = [] if upper is not None and upper < 1 else [(1, upper)]
    if not domain:
        return []
    if A == 0:
        if B == 0:
            return domain if C > 0 else []
        floor, ceil = rational_floor_ceil(-C, B)
        raw = [(floor + 1, None)] if B > 0 else [(1, ceil - 1)]
        return intersect(raw, domain)
    delta = B * B - 4 * A * C
    if delta < 0:
        return domain if A > 0 else []
    if delta == 0:
        if A < 0:
            return []
        floor, ceil = rational_floor_ceil(-B, 2 * A)
        return intersect([(1, ceil - 1), (floor + 1, None)], domain)
    # Multiply by sign(A), so the roots have positive denominator 2*abs(A).
    p = -B if A > 0 else B
    q = 2 * abs(A)
    lower_floor, lower_ceil = radical_floor_ceil(p, -1, delta, q)
    upper_floor, upper_ceil = radical_floor_ceil(p, 1, delta, q)
    if A > 0:
        raw = [(1, lower_ceil - 1), (upper_floor + 1, None)]
    else:
        raw = [(lower_floor + 1, upper_ceil - 1)]
    return intersect(raw, domain)


def binomial_kernel_coefficients(a: int, b: int, c: int) -> tuple[int, int, int]:
    """Coefficients of 2*(a+b*(k+1)+c*binom(k+2,2))."""
    return c, 2 * b + 3 * c, 2 * (a + b + c)


def evaluate(poly: tuple[int, int, int], k: int) -> int:
    A, B, C = poly
    return (A * k + B) * k + C


def threshold_polynomials(total: tuple[int, int, int], event: tuple[int, int, int]):
    """Return coefficients of 2*(T-3N), 2*(3N-2T)."""
    a, b, c = total
    x, y, z = event
    low = binomial_kernel_coefficients(a - 3*x, b - 3*y, c - 3*z)
    high = binomial_kernel_coefficients(3*x - 2*a, 3*y - 2*b, 3*z - 2*c)
    return low, high


def external_length_intervals(total, events, current=None, preserve_side=False):
    """Exact simultaneous external safety intervals.

    total=(a,b,c), events={label:(a_E,b_E,c_E)}.
    If current is provided, targets are 1 <= k < current.
    preserve_side=True additionally requires old safety, and keeps each old side.
    Without current, preserve_side must be False and the full tail is returned.
    Returned details are a finite, replayable interval certificate.
    """
    total = tuple(total)
    assert len(total) == 3 and all(isinstance(t, int) and t >= 0 for t in total)
    assert total[2] > 0
    if preserve_side and current is None:
        raise ValueError('preserve_side needs a current length')
    if current is not None and current < 1:
        raise ValueError('current length must be >= 1')
    upper = None if current is None else current - 1
    allowed = [] if upper is not None and upper < 1 else [(1, upper)]
    details = {}
    for label, event in events.items():
        event = tuple(event)
        assert len(event) == 3 and all(isinstance(x, int) and 0 <= x <= t
                                      for x, t in zip(event, total))
        low, high = threshold_polynomials(total, event)
        low_set = positive_intervals(*low, upper=upper)
        high_set = positive_intervals(*high, upper=upper)
        old_side = None
        if current is not None:
            lv, hv = evaluate(low, current), evaluate(high, current)
            old_side = 'low' if lv > 0 else 'high' if hv > 0 else 'balanced'
        if preserve_side:
            if old_side == 'balanced':
                raise ValueError(f'{label}: old pair is in the closed balanced interval')
            pair_set = low_set if old_side == 'low' else high_set
        else:
            pair_set = merge(low_set + high_set)
        details[label] = dict(low=low, high=high, low_intervals=low_set,
                              high_intervals=high_set, old_side=old_side,
                              allowed=pair_set)
        allowed = intersect(allowed, pair_set)
    return allowed, details


def external_balanced_cover(total, events, current):
    """Return the union and each pair's closed-balanced target length intervals.

    They cover every integer 1<=k<current iff there is no safe external target.
    This uses Q<=0 iff 1-Q>0 for integer Q, including singleton root lengths.
    """
    if current < 1:
        raise ValueError('current length must be >= 1')
    total = tuple(total)
    assert len(total) == 3 and all(isinstance(x, int) and x >= 0 for x in total)
    assert total[2] > 0
    upper = current - 1
    covered, details = [], {}
    for label, event in events.items():
        event = tuple(event)
        assert len(event) == 3 and all(isinstance(x, int) and 0 <= x <= t
                                      for x, t in zip(event, total))
        low, high = threshold_polynomials(total, event)
        nonpositive = lambda q: positive_intervals(-q[0], -q[1], 1-q[2], upper=upper)
        balanced = intersect(nonpositive(low), nonpositive(high))
        details[label] = balanced
        covered = merge(covered + balanced)
    return covered, details


def window_counts(n: int, predecessor_masks: list[int], D: set[int], I: set[int],
                  U: set[int], event=None) -> tuple[int, ...]:
    """Count actual K-window fibers by ideal DP, without any chain lengths.

    Labels are 0..n-1. predecessor_masks may contain all predecessors or an edge
    generating set. D,I,U partition labels and must be the stated block type.
    event=(u,v) restricts to extensions in which u occurs before v.
    This is a finite exact count for a given R, not a search over posets.
    """
    assert D | I | U == set(range(n)) and not (D & I or D & U or I & U)
    assert len(predecessor_masks) == n
    Dmask = sum(1 << x for x in D)
    Umask = sum(1 << x for x in U)
    t = len(I)
    dp = {0: [1] + [0] * t}
    for size in range(n):
        next_dp = {}
        for mask, counts in dp.items():
            assert mask.bit_count() == size
            for x in range(n):
                bit = 1 << x
                if mask & bit or predecessor_masks[x] & ~mask:
                    continue
                if event is not None and x == event[1] and not (mask >> event[0]) & 1:
                    continue
                inc = int(x in I and mask & Dmask == Dmask and mask & Umask == 0)
                new = next_dp.setdefault(mask | bit, [0] * (t+1))
                for K, count in enumerate(counts):
                    if count:
                        assert K + inc <= t
                        new[K + inc] += count
        dp = next_dp
    return tuple(dp.get((1 << n) - 1, [0] * (t+1)))


if __name__ == '__main__':
    for title, total, event, current in [
        ('Boundary d=3,j=2', (0,3,2), (0,1,2), 2),
        ('Actual side switch d=7,j=7', (0,7,2), (0,0,2), 13),
    ]:
        safe, detail = external_length_intervals(total, {'E':event}, current=current)
        same, _ = external_length_intervals(total, {'E':event}, current=current,
                                           preserve_side=True)
        full, _ = external_length_intervals(total, {'E':event})
        print(title)
        print('all safe lengths:', full)
        print('shorter safe targets:', safe, 'same-old-side targets:', same)
        print('certificate:', detail)
