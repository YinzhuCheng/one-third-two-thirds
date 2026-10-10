#!/usr/bin/env python3
"""Independent exact Section 5 audit. Standard library only; no source imports.

Enumerates all naturally labelled Q, every ideal D and every ordered pair of
admissible upper ideals U,V. Checks genuine extension counts by direct listing,
literal swap legality, and complete rational fiber polynomial identities.
"""
import argparse
from collections import Counter, defaultdict
from fractions import Fraction as F
from functools import lru_cache
import hashlib
import itertools
import json
import math
from pathlib import Path
import time


def bits(mask):
    while mask:
        b = mask & -mask
        yield b.bit_length() - 1
        mask -= b


def ideals(pred):
    return [s for s in range(1 << len(pred))
            if all(pred[v] & s == pred[v] for v in bits(s))]


def natural_posets(m):
    if m == 0:
        yield ()
        return
    for old in natural_posets(m - 1):
        for d in ideals(old):
            yield old + (d,)


def extensions(pred):
    full = (1 << len(pred)) - 1
    def rec(seen, seq):
        if seen == full:
            yield seq
        else:
            for v in bits(full ^ seen):
                if pred[v] & seen == pred[v]:
                    yield from rec(seen | (1 << v), seq + (v,))
    return rec(0, ())


@lru_cache(None)
def ecount(pred):
    if not pred:
        return 1
    return sum(ecount(induced(pred, ((1 << len(pred)) - 1) ^ (1 << v)))
               for v, p in enumerate(pred) if p == 0)


def induced(pred, keep):
    vv = tuple(bits(keep))
    return tuple(sum(1 << j for j, w in enumerate(vv) if pred[v] >> w & 1)
                 for v in vv)


def cut_configuration(pred, D, U, V, keep):
    vv = tuple(bits(keep))
    masks = [sum(1 << j for j, w in enumerate(vv) if S >> w & 1)
             for S in (D, U, V)]
    return (induced(pred, keep), *masks)


def full_poset(pred, D, U, V):
    m = len(pred)
    return tuple(p | ((1 << m) if U >> v & 1 else 0)
                 | ((1 << (m + 1)) if V >> v & 1 else 0)
                 for v, p in enumerate(pred)) + (D, D)


def legal(pred, seq):
    seen = 0
    for v in seq:
        if pred[v] & seen != pred[v]:
            return False
        seen |= 1 << v
    return seen == (1 << len(pred)) - 1


def swap(seq, u, y):
    return tuple(y if v == u else u if v == y else v for v in seq)


def classification(pred, seq):
    u, y = len(pred) - 2, len(pred) - 1
    forward = seq.index(u) < seq.index(y)
    swappable = legal(pred, swap(seq, u, y))
    return (1, int(forward), int(not forward), int(forward and swappable))


def add_counts(a, b, multiplier=1):
    return tuple(x + multiplier * y for x, y in zip(a, b))


@lru_cache(16384)
def literal_counts(pred):
    ans = (0, 0, 0, 0)
    for seq in extensions(pred):
        ans = add_counts(ans, classification(pred, seq))
    return ans


def add_poly(dst, src, scale=1):
    for ij, c in src.items():
        dst[ij] += scale * c


def clean(poly):
    return {ij: c for ij, c in poly.items() if c}


@lru_cache(None)
def ordered_simplex_poly(m, p, q):
    # In sector 0<=s<=t<=1: classify m independent uniform samples into
    # [0,s), [s,t), [t,1]. Divide probability by m! for simplex volume.
    ans = defaultdict(F)
    for i in range(m + 1):
        for j in range(m - i + 1):
            k = m - i - j
            if i >= p or i + j >= q:
                continue
            coeff = F(1, math.factorial(i) * math.factorial(j) * math.factorial(k))
            for h in range(j + 1):
                for z in range(k + 1):
                    ans[i + h, j - h + z] += (
                        coeff * math.comb(j, h) * math.comb(k, z) * (-1) ** (h + z))
    return clean(ans)


@lru_cache(None)
def fiber_from_hist(m, hist):
    ans = defaultdict(F)
    for p, q, c in hist:
        add_poly(ans, ordered_simplex_poly(m, p, q), c)
    return clean(ans)


@lru_cache(32768)
def fiber(pred, D, U, V):
    m = len(pred)
    hist = Counter()
    for seq in extensions(pred):
        positions = {v: i + 1 for i, v in enumerate(seq)}
        a = max((positions[v] for v in bits(D)), default=0)
        b = min((positions[v] for v in bits(U)), default=m + 1)
        c = min((positions[v] for v in bits(V)), default=m + 1)
        assert a < b and a < c
        hist[b - a, c - a] += 1
    return fiber_from_hist(m, tuple((p, q, c) for (p, q), c in sorted(hist.items())))


def radial_integral(poly, suffix_dimension, prefix_size):
    # On s<=t, support forces r=1-L >= t. Expand (1-r)^(a-1).
    # Returns integral_t^1 (1-r)^(a-1) r^k f_R(s/r,t/r) dr.
    ans = defaultdict(F)
    for (i, j), c in poly.items():
        power = suffix_dimension - i - j
        assert power >= 0
        for h in range(prefix_size):
            exponent = power + h + 1
            coeff = c * F((-1) ** h * math.comb(prefix_size - 1, h), exponent)
            ans[i, j] += coeff
            ans[i, j + exponent] -= coeff
    return clean(ans)


def branches(pred, D):
    assert D
    for I in ideals(pred):
        if I & D != D:
            continue
        for d in bits(D):
            if I >> d & 1 and all(not (pred[v] >> d & 1) for v in bits(I)):
                yield I, d


def polynomial_counts(pred, D, U, V):
    p = fiber(pred, D, U, V)
    q = fiber(pred, D, V, U)
    fact = math.factorial(len(pred) + 2)
    forward = sum((c / ((i + 1) * (i + j + 2)) for (i, j), c in p.items()), F()) * fact
    reverse = sum((c / ((i + 1) * (i + j + 2)) for (i, j), c in q.items()), F()) * fact
    h = sum((c / (i + j + 2) for (i, j), c in p.items()), F()) * fact
    return (forward + reverse, forward, reverse, h)


def evaluate(poly, s, t):
    return sum((c * s ** i * t ** j for (i, j), c in poly.items()), F())


def audit_one(pred, D, U, V, tally, digest, literal_partition, examples):
    m = len(pred)
    allq = (1 << m) - 1
    P = full_poset(pred, D, U, V)
    original = literal_counts(P)
    assert tuple(polynomial_counts(pred, D, U, V)) == original
    tally['configurations'] += 1
    tally['full_extension_counts'] += original[0]
    tally['forward_swap_checks'] += original[1]
    tally['common_successor_configurations'] += bool(U & V)
    tally['equal_upper_set_configurations'] += U == V
    tally['empty_upper_set_configurations'] += U == 0 or V == 0
    p = fiber(pred, D, U, V)
    q = fiber(pred, D, V, U)
    z = F(ecount(pred), math.factorial(m))
    assert evaluate(p, 0, 0) == z
    assert evaluate(p, 0, 1) == (z if D == V == 0 else 0)
    assert evaluate(q, 0, 1) == (z if D == U == 0 else 0)
    assert evaluate(p, 1, 1) == (z if D == U == V == 0 else 0)
    diag_p, diag_q = defaultdict(F), defaultdict(F)
    for (i, j), c in p.items():
        diag_p[i + j] += c
    for (i, j), c in q.items():
        diag_q[i + j] += c
    assert clean(diag_p) == clean(diag_q)
    tally['endpoint_and_diagonal_checks'] += 5
    if not D:
        tally['empty_downset_configurations'] += 1
        # There is no marked d, hence no nonempty-D sum to apply here.
        digest.update(repr((pred, D, U, V, original, 'empty-D base case')).encode())
        return
    tally['nonempty_downset_configurations'] += 1
    # First-coordinate identities, in both sectors, with literal count checks.
    first_p, first_q = defaultdict(F), defaultdict(F)
    first_counts = (0, 0, 0, 0)
    for v, predecessors in enumerate(pred):
        if predecessors:
            continue
        assert not ((U | V) >> v & 1)
        conf = cut_configuration(pred, D, U, V, allq ^ (1 << v))
        add_poly(first_p, radial_integral(fiber(*conf), m - 1, 1))
        add_poly(first_q, radial_integral(fiber(conf[0], conf[1], conf[3], conf[2]), m - 1, 1))
        first_counts = add_counts(first_counts, literal_counts(full_poset(*conf)))
    assert clean(first_p) == p and clean(first_q) == q
    assert first_counts == original
    tally['first_coordinate_sector_identities'] += 2
    # Last-D marked-ideal identities, in both sectors and all original counts.
    last_p, last_q = defaultdict(F), defaultdict(F)
    last_counts = (0, 0, 0, 0)
    deletion_total = 0
    branch_targets = {}
    ratios = set()
    for I, d in branches(pred, D):
        assert not I & (U | V)
        a = I.bit_count()
        keep = allq ^ I
        conf = cut_configuration(pred, D, U, V, keep)
        assert conf[1] == 0
        prefix = ecount(induced(pred, I ^ (1 << d)))
        suffix = literal_counts(full_poset(*conf))
        ratios.add(F(suffix[1], suffix[0]))
        coeff = F(prefix, math.factorial(a - 1))
        add_poly(last_p, radial_integral(fiber(*conf), m - a, a), coeff)
        add_poly(last_q, radial_integral(fiber(conf[0], 0, conf[3], conf[2]), m - a, a), coeff)
        last_counts = add_counts(last_counts, suffix, prefix)
        deletion_total += prefix * ecount(conf[0])
        branch_targets[I, d] = tuple(prefix * x for x in suffix)
        tally['marked_ideal_branches'] += 1
        tally['empty_suffix_branches'] += a == m
        # Independently check the factorial beta cancellation for degree 2.
        beta = F(math.factorial(a - 1) * math.factorial(m - a + 2), math.factorial(m + 2))
        assert math.factorial(m + 2) * coeff * beta / math.factorial(m - a + 2) == prefix
    assert clean(last_p) == p and clean(last_q) == q
    assert last_counts == original
    assert deletion_total == ecount(pred)
    tally['last_predecessor_sector_identities'] += 2
    tally['original_count_recurrence_equalities'] += 8
    if len(ratios) > 1 and 'varying_forward_probability' not in examples:
        examples['varying_forward_probability'] = {
            'Q_predecessor_masks': pred, 'D': D, 'U': U, 'V': V,
            'original_EFGH': original,
            'branches': [dict(I=I, d=d, weighted_EFGH=x, conditional_F_over_E=str(F(x[1], x[0])))
                         for (I, d), x in branch_targets.items()]}
    if literal_partition:
        observed = defaultdict(lambda: (0, 0, 0, 0))
        deletion_observed = Counter()
        for seq in extensions(pred):
            at = max(i for i, v in enumerate(seq) if D >> v & 1)
            I = sum(1 << v for v in seq[:at + 1])
            deletion_observed[I, seq[at]] += 1
        for I, d in branch_targets:
            assert deletion_observed[I, d] == ecount(induced(pred, I ^ (1 << d))) * ecount(induced(pred, allq ^ I))
        for seq in extensions(P):
            at = max(i for i, v in enumerate(seq) if v < m and D >> v & 1)
            I = sum(1 << v for v in seq[:at + 1])
            d = seq[at]
            assert I >> m == 0 and (I, d) in branch_targets
            cls = classification(P, seq)
            observed[I, d] = add_counts(observed[I, d], cls)
            keep = ((1 << (m + 2)) - 1) ^ I
            vv = tuple(bits(keep))
            mapping = {v: j for j, v in enumerate(vv)}
            remainder = tuple(mapping[v] for v in seq[at + 1:])
            subP = induced(P, keep)
            assert legal(subP, remainder)
            assert cls == classification(subP, remainder)
            assert legal(P, swap(seq, m, m + 1)) == legal(
                subP, swap(remainder, len(subP) - 2, len(subP) - 1))
            tally['literal_H_inheritance_checks'] += 1
        assert dict(observed) == branch_targets
        tally['literal_branch_partition_checks'] += len(branch_targets)
    digest.update(repr((pred, D, U, V, original, tuple(sorted(branch_targets.items())))).encode())


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--max-m', type=int, default=5)
    ap.add_argument('--literal-partition-max-m', type=int, default=5)
    ap.add_argument('--out', default='section5_exact_checks.json')
    args = ap.parse_args()
    result = {'status': 'PASS', 'scope': vars(args), 'dimensions': [], 'examples': {}}
    start = time.time()
    for m in range(args.max_m + 1):
        tally = Counter()
        digest = hashlib.sha256()
        for pred in natural_posets(m):
            tally['naturally_labelled_posets'] += 1
            allq = (1 << m) - 1
            ii = ideals(pred)
            uppers = [allq ^ I for I in ii]
            for D in ii:
                common = sum(1 << v for v in range(m)
                             if not (D >> v & 1) and pred[v] & D == D)
                admissible = [U for U in uppers if U & common == U]
                for U, V in itertools.product(admissible, repeat=2):
                    audit_one(pred, D, U, V, tally, digest,
                              m <= args.literal_partition_max_m, result['examples'])
        row = dict(m=m, n=m + 2, **dict(sorted(tally.items())), record_sha256=digest.hexdigest())
        result['dimensions'].append(row)
        print(json.dumps(row), flush=True)
        Path(args.out).write_text(json.dumps(result, indent=2) + '\n')
    # Also verify the genuine 8-element candidate with the full literal test.
    tally, digest = Counter(), hashlib.sha256()
    audit_one((0, 0, 1, 2, 7, 11), 3, 16, 32, tally, digest, True, result['examples'])
    result['eight_element_candidate'] = dict(tally, record_sha256=digest.hexdigest())
    result['elapsed_seconds'] = round(time.time() - start, 3)
    Path(args.out).write_text(json.dumps(result, indent=2) + '\n')
    print('PASS in', result['elapsed_seconds'], 'seconds', flush=True)


if __name__ == '__main__':
    main()
