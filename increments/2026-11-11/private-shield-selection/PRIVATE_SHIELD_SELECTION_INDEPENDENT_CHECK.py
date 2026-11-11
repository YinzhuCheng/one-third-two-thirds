#!/usr/bin/env python3
"""Independent diagnostic for the selected-private-shield rank and root bank.
No author checker is imported. All counts are integer subset recursion on full posets.
Enumeration is naturally labelled posets, not isomorphism classes.
"""
from functools import lru_cache
from itertools import product
from pathlib import Path
import hashlib
import json


def bits(mask):
    while mask:
        low = mask & -mask
        yield low.bit_length() - 1
        mask ^= low


def natural_posets(n):
    # Append vertex n-1 with any actual ideal as its full predecessor set.
    if n == 0:
        yield ()
        return
    for pred in natural_posets(n - 1):
        for mask in ideals(pred):
            yield pred + (mask,)


def ideals(pred):
    return [mask for mask in range(1 << len(pred))
            if all(pred[x] & ~mask == 0 for x in bits(mask))]


def subset_is_ideal(pred, mask):
    return all(pred[x] & ~mask == 0 for x in bits(mask))


def count_and_rank(pred, private):
    full = (1 << len(pred)) - 1
    @lru_cache(None)
    def rec(mask):
        if mask == full:
            return 1, 1  # no common remaining: rank = remaining size + 1
        count = total_rank = 0
        for x in bits(full ^ mask):
            if pred[x] & ~mask:
                continue
            child_count, child_rank = rec(mask | (1 << x))
            count += child_count
            total_rank += child_count
            if private & (1 << x):
                total_rank += child_rank
        return count, total_rank
    return rec(0)


def event_counts(pred, A=(2, 1), D=(3, 2)):
    # A and D are evaluated at the literal instant their first endpoint is placed.
    # No event-edge insertion, root identity, or tail-rank reduction is used here.
    full = (1 << len(pred)) - 1
    @lru_cache(None)
    def rec(mask):
        if mask == full:
            return 1, 0, 0
        count = ca = cd = 0
        for x in bits(full ^ mask):
            if pred[x] & ~mask:
                continue
            nc, ac, dc = rec(mask | (1 << x))
            count += nc
            ca += ac + (nc if x == A[0] and not mask & (1 << A[1]) else 0)
            cd += dc + (nc if x == D[0] and not mask & (1 << D[1]) else 0)
        return count, ca, cd
    return rec(0)


def full_root(pred, private):
    # Roots 0=a,1=b,2=u,3=v. Tail is shifted by four.
    return (0, 0, 1, 1) + tuple((p << 4) | 5 |
        (0 if private & (1 << x) else 2) for x, p in enumerate(pred))


def exceptional(pred, private, selected):
    return sum(1 << y for y in range(len(pred))
        if not private & (1 << y) and selected & ~pred[y])


def matching_size(pred, private, common):
    matched = {}
    def augment(y, seen):
        for x in bits(pred[y] & private):
            if x in seen:
                continue
            seen.add(x)
            if x not in matched or augment(matched[x], seen):
                matched[x] = y
                return True
        return False
    return sum(augment(y, set()) for y in bits(common))


def gate(pred, private, selected):
    a = selected.bit_count()
    exceptional_set = exceptional(pred, private, selected)
    s = exceptional_set.bit_count()
    F = len(pred) * (a - s - 1) + 4 * a + 2 * s + 2
    deficiency = s - matching_size(pred, private, exceptional_set)
    return deficiency <= 2 and F >= 0


def linear_extensions(pred):
    full = (1 << len(pred)) - 1
    def walk(mask, word):
        if mask == full:
            yield word
            return
        for x in bits(full ^ mask):
            if not pred[x] & ~mask:
                yield from walk(mask | (1 << x), word + (x,))
    yield from walk(0, ())


def induced(pred, subset):
    labels = tuple(bits(subset))
    return tuple(sum(1 << i for i, old in enumerate(labels) if pred[x] & (1 << old))
                 for x in labels)


def degree(pred):
    return max((sum(y != x and not pred[x] & (1 << y)
                    and not pred[y] & (1 << x) for y in range(len(pred)))
                for x in range(len(pred))), default=0)


def main():
    totals = {"natural_posets": 0, "private_ideals": 0,
              "rank_all_subsets": 0, "rank_ideal_subsets": 0,
              "rank_equalities": 0, "full_root_instances": 0,
              "full_root_gate_instances": 0, "qualifying_ideal_choices": 0,
              "literal_cells": 0, "cell_partition_instances": 0,
              "one_exterior_instances": 0}
    per_n = {}
    for n in range(6):
        n_posets = n_ideals = n_choices = 0
        for pred in natural_posets(n):
            n_posets += 1
            all_mask = (1 << n) - 1
            for private in ideals(pred):
                n_ideals += 1
                count, rank_total = count_and_rank(pred, private)
                root = full_root(pred, private)
                root_count, ca, cd = event_counts(root)
                totals["full_root_instances"] += 1
                # Independently counted full-root identity is a diagnostic only.
                assert root_count == (n + 3) * rank_total + (2 * n + 5) * count
                assert ca == (n + 3) * rank_total
                assert cd == rank_total + 3 * count
                any_gate = False
                selected = private
                while True:
                    a = selected.bit_count()
                    b0 = exceptional(pred, private, selected)
                    s = b0.bit_count()
                    defect = (s + 1) * rank_total - (s + 1 + a) * count
                    assert defect >= 0, (pred, private, selected, count, rank_total)
                    totals["rank_all_subsets"] += 1
                    totals["rank_equalities"] += defect == 0
                    ideal_selected = subset_is_ideal(pred, selected)
                    if ideal_selected:
                        totals["rank_ideal_subsets"] += 1
                        n_choices += 1
                        if gate(pred, private, selected):
                            totals["qualifying_ideal_choices"] += 1
                            any_gate = True
                    # Independent literal-cell audit (through n=4).
                    if n <= 4:
                        b1 = (all_mask ^ private) & ~b0
                        if b1:
                            cells = {}
                            for word in linear_extensions(pred):
                                at = next(i for i, x in enumerate(word) if b1 & (1 << x))
                                prefix_mask = sum(1 << x for x in word[:at])
                                key = (prefix_mask, word[at:])
                                first_common = next(i + 1 for i, x in enumerate(word)
                                                    if not private & (1 << x))
                                nc, nr = cells.get(key, (0, 0))
                                cells[key] = (nc + 1, nr + first_common)
                            for (prefix_mask, suffix), (nc, nr) in cells.items():
                                assert selected & ~prefix_mask == 0
                                assert ((prefix_mask & ~private).bit_count()) <= s
                                # Cell's raw count equals the independent induced-prefix DP.
                                ipred = induced(pred, prefix_mask)
                                iprivate = sum(1 << i for i, x in enumerate(bits(prefix_mask))
                                               if private & (1 << x))
                                prefix_words, prefix_rank = count_and_rank(ipred, iprivate)
                                assert (nc, nr) == (prefix_words, prefix_rank)
                                assert (s + 1) * nr >= (s + 1 + a) * nc
                                totals["literal_cells"] += 1
                            totals["cell_partition_instances"] += 1
                    if selected == 0:
                        break
                    selected = (selected - 1) & private
                if any_gate:
                    totals["full_root_gate_instances"] += 1
                    assert 2 * ca + cd - root_count >= 0
                    if n <= 3:
                        for predecessor_ideal in ideals(root):
                            if predecessor_ideal & (1 << 3):
                                N, A, D = event_counts(root + (predecessor_ideal,))
                                assert 2 * A + D - N >= 0
                                totals["one_exterior_instances"] += 1
        per_n[n] = {"posets": n_posets, "private_ideals": n_ideals,
                    "selected_ideals": n_choices}
        totals["natural_posets"] += n_posets
        totals["private_ideals"] += n_ideals

    # Strict mechanism separation: a selected private point p shields the z-chain,
    # while the extra private minimum d is incomparable with that whole chain.
    tail = (0, 0, 0, 5, 13, 29, 61)  # p,d,q,z1,z2,z3,z4
    private, selected = 3, 1
    root = full_root(tail, private)
    N, A, D = event_counts(root)
    assert gate(tail, private, selected)
    assert not gate(tail, private, private)
    assert (N, A, D, 2 * A + D - N) == (506, 240, 66, 40)
    separation = {"tail_pred": tail, "private_mask": private,
                  "selected_mask": selected, "full_Q_pred": root,
                  "a": 1, "s": 1, "n": 7, "F": 1,
                  "full_private_F": -8, "Delta": degree(root),
                  "N": N, "A": A, "D": D, "margin": 2 * A + D - N,
                  "tail_extension_count_and_rank_sum": count_and_rank(tail, private)}
    # Boundary counterexample for dropping F: no extra private labels are needed.
    tail_bad = (0, 0, 0, 7, 15, 31)
    bad_root = full_root(tail_bad, 1)
    N, A, D = event_counts(bad_root)
    assert (N, A, D, 2 * A + D - N) == (174, 72, 26, -4)
    negative = {"tail_pred": tail_bad, "private_mask": 1, "selected_mask": 1,
                "a": 1, "s": 2, "n": 6, "F": -2,
                "Delta": degree(bad_root), "N": N, "A": A, "D": D,
                "margin": 2 * A + D - N}
    author_root = (0, 0, 1, 1, 5, 5, 37, 7, 151, 407, 919)
    author_tail = tuple(p >> 4 for p in author_root[4:])
    assert gate(author_tail, 7, 1) and not gate(author_tail, 7, 7)
    N, A, D = event_counts(author_root)
    author_control = {"full_Q_pred": author_root, "Delta": degree(author_root),
                      "N": N, "A": A, "D": D, "margin": 2 * A + D - N}
    # FG(D) is NOT contained in the selected-shield contract, even in degree9.
    delay_tail = (0, 0, 1, 1, 2, 2, 2)
    delay_private = 3
    assert all(p for x, p in enumerate(delay_tail) if not delay_private & (1 << x))
    failed_choices = []
    for choice in (0, 1, 2, 3):
        a = choice.bit_count()
        s = exceptional(delay_tail, delay_private, choice).bit_count()
        F = 7 * (a - s - 1) + 4 * a + 2 * s + 2
        assert not gate(delay_tail, delay_private, choice)
        failed_choices.append({"S_mask": choice, "a": a, "s": s, "F": F})
    delay_root = full_root(delay_tail, delay_private)
    N, A, D = event_counts(delay_root)
    delay_control = {"tail_pred": delay_tail, "full_Q_pred": delay_root,
                     "Delta": degree(delay_root), "N": N, "A": A, "D": D,
                     "margin": 2 * A + D - N, "failed_choices": failed_choices}
    result = {"status": "PASS", "diagnostic_scope":
        "All naturally labelled H through size 5, all private ideals, all S subsets; "
        "literal first-shield cells through size 4; all one-exterior predecessor ideals "
        "for qualifying H through size 3. Finite diagnostics are not the proof.",
        "totals": totals, "per_n": per_n, "strict_contract_separation": separation,
        "negative_F_control": negative, "author_strict_contract_control": author_control,
        "FG_D_not_included_control": delay_control,
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
