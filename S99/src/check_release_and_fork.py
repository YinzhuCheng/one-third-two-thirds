#!/usr/bin/env python3
"""Deterministic, exact S99 diagnostics using actual linear extensions.

No third-party dependencies, random sampling, floating-point tests, or inherited
run counts.  The swap checks below verify the proposed injection on every source
extension of nine specified posets; they are finite diagnostics, not a proof for
all posets.  Shepp XYZ remains an external theorem in the analytic fork argument.

Run from any directory:
    python check_release_and_fork.py --output ../evidence/release_and_fork.json
"""
from __future__ import annotations

import argparse
from dataclasses import dataclass
from fractions import Fraction
from itertools import combinations
import json
from pathlib import Path


@dataclass(frozen=True)
class Poset:
    names: tuple[str, ...]
    pred: tuple[int, ...]

    @classmethod
    def from_edges(cls, names, edges):
        names = tuple(names)
        lookup = {v: i for i, v in enumerate(names)}
        assert len(lookup) == len(names)
        pred = [0] * len(names)
        for a, b in edges:
            i, j = lookup[a], lookup[b]
            assert i != j
            pred[j] |= 1 << i
        for k in range(len(names)):
            for j in range(len(names)):
                if pred[j] & (1 << k):
                    pred[j] |= pred[k]
        assert all(not (pred[j] & (1 << j)) for j in range(len(names)))
        return cls(names, tuple(pred))

    def induced_without(self, removed):
        kept = [i for i, name in enumerate(self.names) if name not in removed]
        return Poset.from_edges(
            [self.names[i] for i in kept],
            [(self.names[i], self.names[j]) for i in kept for j in kept
             if self.pred[j] & (1 << i)],
        )

    def extensions(self):
        n = len(self.names)
        full = (1 << n) - 1
        result = []

        def visit(prefix, used):
            if used == full:
                result.append(tuple(prefix))
                return
            for v in range(n):
                if not (used & (1 << v)) and not (self.pred[v] & ~used):
                    prefix.append(v)
                    visit(prefix, used | (1 << v))
                    prefix.pop()

        visit([], 0)
        return result

    def minimal(self):
        return [i for i, mask in enumerate(self.pred) if mask == 0]

    def incomparable(self, u, v):
        return u != v and not (self.pred[u] & (1 << v)) and not (self.pred[v] & (1 << u))

    def width(self):
        n = len(self.names)
        for size in range(n, 0, -1):
            for selected in combinations(range(n), size):
                if all(self.incomparable(u, v) for u, v in combinations(selected, 2)):
                    return size
        return 0

    def private_successors(self, u, y):
        private = [v for v in range(len(self.names))
                   if self.pred[v] & (1 << u) and not (self.pred[v] & (1 << y))]
        private_mask = sum(1 << v for v in private)
        return [v for v in private if not (self.pred[v] & private_mask)]

    def lower_covers(self, u):
        down = [v for v in range(len(self.names)) if self.pred[u] & (1 << v)]
        return [v for v in down
                if not any(self.pred[w] & (1 << v) for w in down)]


def fraction(numerator, denominator):
    return str(Fraction(numerator, denominator))


def make_cases():
    fork_names = ["a", "u", "s", "t", "y"]
    fork_edges = [(a, b) for a in ("a", "u") for b in ("s", "t")]
    masks_s96 = (0, 5, 0, 4, 13, 29, 0, 68, 204)
    s96_names = [f"v{i}" for i in range(9)]
    chain9 = [f"a{i}" for i in range(1, 10)]
    return [
        ("antichain_3", Poset.from_edges(["a", "b", "y"], [])),
        ("two_disjoint_2_chains", Poset.from_edges(
            ["a", "b", "c", "d"], [("a", "b"), ("c", "d")])),
        ("fixed_minimal_fork_5", Poset.from_edges(fork_names, fork_edges)),
        ("fixed_minimal_fork_ordinal_top_7", Poset.from_edges(
            fork_names + ["z1", "z2"],
            fork_edges + [(v, "z1") for v in fork_names] + [("z1", "z2")])),
        ("nonminimal_square_guard_10", Poset.from_edges(
            chain9 + ["y"], list(zip(chain9, chain9[1:])))),
        ("nonminimal_fork_6", Poset.from_edges(
            ["v", "a", "u", "s", "t", "y"],
            [("v", "u"), ("a", "s"), ("a", "t"), ("u", "s"), ("u", "t")])),
        ("delayed_release_7", Poset.from_edges(
            ["b1", "b2", "b3", "x", "s", "y", "t"],
            [("b1", "b2"), ("b2", "b3"), ("x", "s"), ("y", "t"),
             ("b2", "s"), ("b1", "t")])),
        ("s97_guard_8", Poset.from_edges(
            ["b1", "b2", "b3", "x", "y", "u", "v", "z"],
            [("b1", "b2"), ("b2", "b3"), ("b1", "u"), ("x", "u"),
             ("b1", "v"), ("y", "v"), ("u", "z"), ("v", "z")])),
        ("s96_guard_9", Poset.from_edges(
            s96_names,
            [(s96_names[i], s96_names[j]) for j, mask in enumerate(masks_s96)
             for i in range(9) if mask & (1 << i)])),
    ]


def minimal_pair_windows(P, x_name, y_name):
    x, y = P.names.index(x_name), P.names.index(y_name)
    assert P.pred[x] == P.pred[y] == 0
    deleted = P.induced_without({x_name, y_name})
    H = rx = ry = 0
    for extension in deleted.extensions():
        old_names = [deleted.names[v] for v in extension]

        def slots(z):
            return next((i for i, name in enumerate(old_names, 1)
                         if P.pred[P.names.index(name)] & (1 << z)), len(old_names) + 1)

        a, b = slots(x), slots(y)
        m = min(a, b)
        H += m * (m + 1) // 2
        rx += m * max(b - a, 0)
        ry += m * max(a - b, 0)
    return H, rx, ry


def inspect_case(name, P):
    extensions = P.extensions()
    extension_set = set(extensions)
    E = len(extensions)
    assert E > 0 and len(extension_set) == E
    width = P.width()
    assert width <= 3
    positions = []
    for extension in extensions:
        rank = [0] * len(P.names)
        for i, v in enumerate(extension):
            rank[v] = i
        assert all(rank[u] < rank[v] for v in range(len(P.names))
                   for u in range(len(P.names)) if P.pred[v] & (1 << u))
        positions.append(rank)

    pair_data = {}
    injection_count = 0
    nonminimal_pairs = 0
    nonminimal_injections = 0
    fork_certificates = []
    for y in P.minimal():
        incomparable = [u for u in range(len(P.names)) if P.incomparable(u, y)]
        for u in incomparable:
            S = P.private_successors(u, y)
            all_private = [v for v in range(len(P.names))
                           if P.pred[v] & (1 << u) and not (P.pred[v] & (1 << y))]
            assert all(P.incomparable(s, y) for s in S)
            assert len(S) <= 2
            for s in S:
                assert not any(P.pred[v] & (1 << u) and P.pred[s] & (1 << v)
                               for v in range(len(P.names)))
            p_events = {i for i, rank in enumerate(positions) if rank[u] < rank[y]}
            d_events = {i for i, rank in enumerate(positions)
                        if all(rank[v] < rank[y] for v in range(len(P.names))
                               if P.pred[u] & (1 << v))}
            U_events = {i for i, rank in enumerate(positions)
                        if any(rank[s] < rank[y] for s in S)}
            all_successor_events = {i for i, rank in enumerate(positions)
                                    if any(rank[s] < rank[y] for s in all_private)}
            assert U_events == all_successor_events
            assert U_events <= p_events <= d_events
            source = p_events - U_events
            target = d_events - p_events
            target_extensions = {extensions[i] for i in target}
            images = set()
            for i in source:
                swapped = list(extensions[i])
                old_u, old_y = positions[i][u], positions[i][y]
                swapped[old_u], swapped[old_y] = swapped[old_y], swapped[old_u]
                image = tuple(swapped)
                assert image in extension_set
                assert image in target_extensions
                assert image not in images
                images.add(image)
            assert len(images) == len(source) <= len(target)
            p, d, U = len(p_events), len(d_events), len(U_events)
            assert U >= 2 * p - d >= 2 * p - E
            pair_data[(u, y)] = {"p": p, "d": d, "U": U, "S": S}
            injection_count += len(source)
            if P.pred[u]:
                nonminimal_pairs += 1
                nonminimal_injections += len(source)

        no_balanced_partner = all(
            3 * pair_data[(u, y)]["p"] < E or 3 * pair_data[(u, y)]["p"] > 2 * E
            for u in incomparable)
        majority = [u for u in incomparable if 3 * pair_data[(u, y)]["p"] > 2 * E]
        if not no_balanced_partner or not majority:
            continue
        maximal_majority = [u for u in majority
                            if not any(P.pred[v] & (1 << u) for v in majority)]
        assert maximal_majority
        for u in maximal_majority:
            data = pair_data[(u, y)]
            p, d, U, S = (data[k] for k in ("p", "d", "U", "S"))
            assert len(S) == 2
            ps, pt = [pair_data[(s, y)]["p"] for s in S]
            assert 3 * ps < E and 3 * pt < E
            # An exact check of the XYZ input on this particular triple.
            assert (E - ps) * (E - pt) <= E * (E - U)
            assert 9 * U < 5 * E
            assert 3 * p > 2 * E and 9 * p < 7 * E
            assert 9 * d > 18 * p - 5 * E and 9 * d > 7 * E
            lower = P.lower_covers(u)
            assert len(lower) <= 2
            assert all(P.incomparable(v, y) and pair_data[(v, y)]["p"] >= d for v in lower)
            fork_certificates.append({
                "y": P.names[y], "u": P.names[u], "private_upper_covers": [P.names[s] for s in S],
                "p_u": fraction(p, E), "d": fraction(d, E), "U": fraction(U, E),
                "upper_probabilities": [fraction(ps, E), fraction(pt, E)],
                "lower_covers": [P.names[v] for v in lower],
                "lower_probabilities": [fraction(pair_data[(v, y)]["p"], E) for v in lower],
            })

    row = {
        "name": name, "n": len(P.names), "width": width, "linear_extensions": E,
        "labels": list(P.names), "predecessor_masks": list(P.pred),
        "minimal_y_incomparable_u_configurations": len(pair_data),
        "direct_swap_source_extensions_checked": injection_count,
        "nonminimal_u_configurations": nonminimal_pairs,
        "nonminimal_u_swap_source_extensions_checked": nonminimal_injections,
        "maximal_majority_fork_certificates": fork_certificates,
    }
    return row, pair_data, E


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path,
                        default=Path(__file__).resolve().parents[1] / "evidence" / "release_and_fork.json")
    args = parser.parse_args()
    rows = []
    known_guards = {}
    for name, P in make_cases():
        row, pair_data, E = inspect_case(name, P)
        rows.append(row)
        if name == "fixed_minimal_fork_5":
            y, u = P.names.index("y"), P.names.index("u")
            data = pair_data[(u, y)]
            assert E == 20 and (data["p"], data["d"], data["U"]) == (14, 20, 8)
            assert [pair_data[(P.names.index(v), y)]["p"] for v in ("a", "u", "s", "t")] == [14, 14, 6, 6]
            assert len(row["maximal_majority_fork_certificates"]) == 2
            H, rx, ry = minimal_pair_windows(P, "u", "y")
            assert (H, rx, ry) == (6, 8, 0) and 2 * H + rx + ry == E
            delta = Fraction(H, E) - Fraction(data["p"], E) * (1 - Fraction(data["p"], E))
            assert delta == Fraction(9, 100)
            known_guards[name] = {
                "E": E, "p_a_y": "7/10", "p_u_y": "7/10", "p_s_y": "3/10", "p_t_y": "3/10",
                "d": "1", "U": "2/5", "H": H, "R_x": rx, "R_y": ry, "delta": str(delta),
                "claim_refuted": "A fixed minimal y with a majority-preceding element must have a balanced partner.",
                "main_conjecture_counterexample": False,
            }
        if name == "nonminimal_square_guard_10":
            y, u = P.names.index("y"), P.names.index("a2")
            data = pair_data[(u, y)]
            assert E == 10 and (data["p"], data["d"], data["U"]) == (8, 9, 7)
            assert [P.names[s] for s in data["S"]] == ["a3"]
            assert 3 * data["p"] > 2 * E and 3 * data["p"] ** 2 <= 2 * E ** 2
            assert 3 * data["U"] > 2 * E and data["U"] * E > data["p"] ** 2
            assert data["U"] == 2 * data["p"] - data["d"]
            assert pair_data[(P.names.index("a4"), y)]["p"] == 6
            known_guards[name] = {
                "E": E, "u": "a2", "s": "a3", "y": "y", "p_u_y": "4/5", "p_s_y": "7/10",
                "p_u_y_squared": "16/25", "d": "9/10", "U": "7/10", "p_a4_y": "3/5",
                "predecessor_corrected_lower_bound_is_equality": True,
                "claim_refuted": "The minimal-entrance square bound and its closing interval apply unchanged to nonminimal u.",
                "main_conjecture_counterexample": False,
            }
        if name == "s97_guard_8":
            assert E == 256
        if name == "s96_guard_9":
            assert E == 737

    evidence = {
        "status": "PASSED", "method": "Deterministic enumeration of all linear extensions of nine specified posets; integer and Fraction arithmetic.",
        "models": len(rows),
        "total_linear_extensions_across_models": sum(row["linear_extensions"] for row in rows),
        "minimal_y_incomparable_u_configurations": sum(row["minimal_y_incomparable_u_configurations"] for row in rows),
        "direct_swap_source_extensions_checked": sum(row["direct_swap_source_extensions_checked"] for row in rows),
        "nonminimal_u_configurations": sum(row["nonminimal_u_configurations"] for row in rows),
        "nonminimal_u_swap_source_extensions_checked": sum(row["nonminimal_u_swap_source_extensions_checked"] for row in rows),
        "maximal_majority_fork_certificates": sum(len(row["maximal_majority_fork_certificates"]) for row in rows),
        "exact_guards": known_guards,
        "cases": rows,
        "scope": "Finite diagnostics, not exhaustive isomorphism-class coverage and not a general proof. The ordinal-top case deliberately checks probability preservation; no random-search or prior-run counts are included. The unproved candidate d*U <= p^2 is not an assertion in this checker.",
    }
    assert evidence["nonminimal_u_configurations"] > 0
    assert evidence["maximal_majority_fork_certificates"] >= 4
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(evidence, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: evidence[key] for key in (
        "status", "models", "total_linear_extensions_across_models", "minimal_y_incomparable_u_configurations",
        "direct_swap_source_extensions_checked", "nonminimal_u_configurations",
        "nonminimal_u_swap_source_extensions_checked", "maximal_majority_fork_certificates")}, ensure_ascii=False))


if __name__ == "__main__":
    main()
