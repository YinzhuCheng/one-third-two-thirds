"""Strictly bounded cross-pair test on the already frozen 96 objects."""
import json
import sys
import time
from collections import Counter
from fractions import Fraction
from math import comb
from pathlib import Path

sys.dont_write_bytecode = True
sys.path.insert(0, '/workspace/shared/external-pair-length-intervals-20261018')
from interval_solver import (binomial_kernel_coefficients, threshold_polynomials,
                             positive_intervals, intersect, evaluate)

OUT = Path(__file__).resolve().parent
SOURCE = Path('/workspace/shared/disconnected-balance-interval-test-20261018/frozen_cases.json')


def count(p, q, y, z, event=None):
    """The old prefix DP, now gating the compared I insertion, not D."""
    dp = [[[0] * 4 for _ in range(q + 1)] for _ in range(p + 1)]
    dp[0][0][0] = 1
    for i in range(p + 1):
        for j in range(q + 1):
            if i == p and j == q:
                continue
            for mask in range(4):
                v = dp[i][j][mask]
                if not v:
                    continue
                if i < p:
                    dp[i + 1][j][mask] += v
                if j < q:
                    dp[i][j + 1][mask] += v
                for h, gate in enumerate((y, z)):
                    if mask & (1 << h) or i < gate[0] or j < gate[1]:
                        continue
                    if event is not None and event['I'] == ('y', 'z')[h]:
                        if event['D_chain'] == 'A' and i < p:
                            continue
                        if event['D_chain'] == 'B' and j < q:
                            continue
                    dp[i][j][mask | (1 << h)] += v
    final = dp[p][q]
    return (final[3], final[1] + final[2], 2 * final[0])


def diff_poly(total, event):
    A, B, C = binomial_kernel_coefficients(*total)
    a, b, c = binomial_kernel_coefficients(*event)
    d0, d1, d2 = a * B - b * A, 2 * (a * C - c * A), b * C - c * B
    return (d0, d0 + d1, d1 // 2 + d2)


def nonpositive(poly):
    return positive_intervals(-poly[0], -poly[1], 1 - poly[2])


def quadratic_vertex(poly, mode):
    """Integer extremum over m>=1, for strictly convex/concave poly."""
    A, B, C = poly
    assert A != 0 and (A > 0) == (mode == 'min')
    v = Fraction(-B, 2 * A)
    floor = v.numerator // v.denominator
    candidates = sorted({1, max(1, floor), max(1, floor + 1)})
    vals = [(evaluate(poly, m), m) for m in candidates]
    extreme = min(v for v, m in vals) if mode == 'min' else max(v for v, m in vals)
    return {'real_vertex': str(v), 'integer_extreme_m': [m for v, m in vals if v == extreme],
            'twice_extreme': extreme}


def enumerate_control(case, candidates):
    """Independent shuffle + slot enumeration of actual R, for one old case."""
    p, q = case['p'], case['q']
    nD = p + q
    total = [0, 0, 0]
    events = {e['label']: [0, 0, 0] for e in candidates if not e['skip_comparable']}
    words = 0

    def visit(word, i, j):
        nonlocal words
        if i < p:
            visit(word + ['A' + str(i + 1)], i + 1, j)
        if j < q:
            visit(word + ['B' + str(j + 1)], i, j + 1)
        if i != p or j != q:
            return
        words += 1
        positions = {x: k + 1 for k, x in enumerate(word)}
        release = []
        for gate in (case['y'], case['z']):
            predecessor_positions = [positions[chain + str(r)]
                                     for chain, r in zip(('A', 'B'), gate) if r]
            release.append(max([0] + predecessor_positions))
        # Slot s means after exactly s D points; same slot has two I orders.
        for sy in range(release[0], nD + 1):
            for sz in range(release[1], nD + 1):
                orders = [('y', 'z'), ('z', 'y')] if sy == sz else [('y', 'z') if sy < sz else ('z', 'y')]
                for order in orders:
                    R = []
                    for slot in range(nD + 1):
                        R.extend(x for x in order if {'y': sy, 'z': sz}[x] == slot)
                        if slot < nD:
                            R.append(word[slot])
                    K = int(sy == nD) + int(sz == nD)
                    total[K] += 1
                    for e in candidates:
                        if not e['skip_comparable'] and R.index(e['D_label']) < R.index(e['I']):
                            events[e['label']][K] += 1
    visit([], 0, 0)
    assert words == comb(nD, p)
    return {'D_words': words, 'total': total, 'events': events}


def direct_m1_control(case, candidates):
    """Independently enumerate P_1 LE from generating relations."""
    p, q = case['p'], case['q']
    labels = ['A' + str(i) for i in range(1, p + 1)] + ['B' + str(j) for j in range(1, q + 1)] + ['y', 'z', 'C1']
    idx = {x: i for i, x in enumerate(labels)}
    pred = [0] * len(labels)
    for chain, length in [('A', p), ('B', q)]:
        for r in range(2, length + 1):
            pred[idx[chain + str(r)]] |= 1 << idx[chain + str(r - 1)]
    for x, gate in [('y', case['y']), ('z', case['z'])]:
        for chain, r in zip(('A', 'B'), gate):
            if r:
                pred[idx[x]] |= 1 << idx[chain + str(r)]
    pred[idx['C1']] = (1 << (p + q)) - 1
    events = {e['label']: 0 for e in candidates if not e['skip_comparable']}
    total = 0
    full = (1 << len(labels)) - 1
    def rec(mask, word):
        nonlocal total
        if mask == full:
            total += 1
            pos = {labels[x]: i for i, x in enumerate(word)}
            for e in candidates:
                if not e['skip_comparable'] and pos[e['D_label']] < pos[e['I']]:
                    events[e['label']] += 1
            return
        for i in range(len(labels)):
            if not mask >> i & 1 and not pred[i] & ~mask:
                rec(mask | (1 << i), word + [i])
    rec(0, [])
    return {'total': total, 'events': events}


def main():
    start = time.monotonic()
    cases = json.loads(SOURCE.read_text())
    assert len(cases) == 96
    assert len({(c['p'], c['q'], tuple(c['y']), tuple(c['z'])) for c in cases}) == 96
    manifest = []
    for c in cases:
        for chain, endpoint in [('A', c['p']), ('B', c['q'])]:
            for I in ('y', 'z'):
                other_I = 'z' if I == 'y' else 'y'
                other_gate = c[other_I]
                item = {'case_index': c['case_index'], 'label': f'{chain}{endpoint}<{I}',
                        'D_chain': chain, 'D_label': chain + str(endpoint), 'I': I,
                        'skip_comparable': c[I][chain == 'B'] == endpoint,
                        'other_I': other_I,
                        'other_I_ordinal_cut': other_gate == [0, 0] or other_gate == [c['p'], c['q']]}
                manifest.append(item)
    assert len(manifest) == 384
    (OUT / 'candidate_manifest.json').write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + '\n')
    print('Frozen 96 existing structures and 384 candidate slots; no hashes.', flush=True)
    results = []
    summary = Counter({'tested': 0, 'skipped_comparable': 0, 'covered_beta_le_6c': 0,
                       'beta_gt_6c': 0, 'discrete_nonmonotone': 0})
    witnesses, uncovered, nonmonotone = [], [], []
    histogram = Counter()
    all_ratios = []
    for case in cases:
        entries = []
        candidates = [e for e in manifest if e['case_index'] == case['case_index']]
        total = count(case['p'], case['q'], case['y'], case['z'])
        assert total[2] == 2 * comb(case['p'] + case['q'], case['p'])
        for e in candidates:
            if e['skip_comparable']:
                entries.append(e)
                summary['skipped_comparable'] += 1
                continue
            summary['tested'] += 1
            summary['ordinal_cut_structure_covered'] += int(e['other_I_ordinal_cut'])
            event = count(case['p'], case['q'], case['y'], case['z'], e)
            assert all(0 <= v <= t for v, t in zip(event, total))
            assert event[2] == total[2]
            failure = tuple(t - v for t, v in zip(total, event))
            assert failure[2] == 0
            ratio = Fraction(failure[1], total[2])
            all_ratios.append(ratio)
            covered = failure[1] <= 6 * total[2]
            summary['covered_beta_le_6c' if covered else 'beta_gt_6c'] += 1
            if not covered:
                summary['beta_gt_6c_ordinal_cut_covered'] += int(e['other_I_ordinal_cut'])
            low, high = threshold_polynomials(total, event)
            # Exact intervals for the whole infinite integer domain, never an m scan.
            H = nonpositive(high)
            L = positive_intervals(*low)
            balanced = intersect(nonpositive(low), H)
            histogram[len(balanced)] += 1
            two_via_H_minus_L = (len(H) == len(L) == 1 and H[0][1] is not None
                                and L[0][1] is not None and H[0][0] < L[0][0]
                                <= L[0][1] < H[0][1])
            assert two_via_H_minus_L == (len(balanced) == 2)
            if covered:
                assert len(balanced) <= 1
            diff = diff_poly(total, event)
            pos, neg = positive_intervals(*diff), positive_intervals(*[-v for v in diff])
            nm = bool(pos and neg)
            if nm:
                summary['discrete_nonmonotone'] += 1
            entry = {**e, 'event': event, 'failure': failure, 'B_fail_over_c': str(ratio),
                     'mean_failure_slots_beta': str(2 * ratio), 'covered_beta_le_6c': covered,
                     'low': low, 'high': high, 'H_high_nonpositive': H, 'L_low_positive': L,
                     'balanced': balanced, 'two_components_exact_H_minus_L': two_via_H_minus_L,
                     'discrete_difference': diff, 'difference_positive': pos, 'difference_negative': neg,
                     'discrete_nonmonotone': nm}
            if not covered:
                low_vertex = quadratic_vertex(low, 'max')
                high_vertex = quadratic_vertex(high, 'min')
                alpha, beta, _ = failure
                a, b, c = total
                zstar = max(2, (3 * beta - 2 * b) // (2 * c))
                F2 = 3 * alpha + 6 * beta - 2 * a - 4 * b - 6 * c
                Fstar = 3 * alpha - 2 * a + (3 * beta - 2 * b) * zstar - c * zstar * (zstar + 1)
                simplified = F2 <= 0 < Fstar
                assert evaluate(low, zstar - 1) == 2 * Fstar == low_vertex['twice_extreme']
                assert simplified == two_via_H_minus_L
                entry['vertex_check'] = {'low_concave': low_vertex, 'high_convex': high_vertex,
                                         'failure_low_first_F2': F2, 'maximizer_z': zstar,
                                         'failure_low_integer_max': Fstar,
                                         'simplified_two_component_criterion': simplified}
            entries.append(entry)
            base = {k: case[k] for k in ['case_index', 'label', 'p', 'q', 'n', 'y', 'z']}
            base = {**base, 'total': total, 'entry': entry}
            if not covered:
                uncovered.append(base)
            if nm:
                nonmonotone.append(base)
            if len(balanced) == 2:
                witnesses.append(base)
                print('TWO COMPONENT WITNESS:', json.dumps(base, ensure_ascii=False), flush=True)
        results.append({k: v for k, v in case.items() if k != 'pairs'} | {'total': total, 'events': entries})
    assert summary['tested'] + summary['skipped_comparable'] == 384
    summary['beta_gt_6c_outside_ordinal_cut_structure_class'] = (
        summary['beta_gt_6c'] - summary['beta_gt_6c_ordinal_cut_covered'])
    summary_data = {'source_structures': 96, 'candidate_slots': 384, **dict(summary),
                    'balance_component_histogram': dict(histogram), 'two_component_pairs': len(witnesses),
                    'B_fail_over_c_min': str(min(all_ratios)), 'B_fail_over_c_max': str(max(all_ratios)),
                    'elapsed_seconds': time.monotonic() - start,
                    'witnesses': witnesses, 'uncovered': uncovered, 'nonmonotone': nonmonotone}
    (OUT / 'all_counts.json').write_text(json.dumps(results, indent=2, ensure_ascii=False) + '\n')
    (OUT / 'summary.json').write_text(json.dumps(summary_data, indent=2, ensure_ascii=False) + '\n')
    # Independent controls on one existing object, using exactly its fixed pairs.
    case = cases[0]
    candidates = [e for e in manifest if e['case_index'] == case['case_index']]
    slot = enumerate_control(case, candidates)
    direct = direct_m1_control(case, candidates)
    rec = results[0]
    assert slot['total'] == list(rec['total'])
    T1 = rec['total'][0] + 2 * rec['total'][1] + 3 * rec['total'][2]
    assert direct['total'] == T1
    for e in rec['events']:
        if e['skip_comparable']:
            continue
        assert slot['events'][e['label']] == list(e['event'])
        assert direct['events'][e['label']] == e['event'][0] + 2 * e['event'][1] + 3 * e['event'][2]
    controls = {'case_index': 1, 'slot_enumeration': slot, 'direct_m1': direct, 'status': 'PASS'}
    (OUT / 'controls.json').write_text(json.dumps(controls, indent=2, ensure_ascii=False) + '\n')
    print(json.dumps({k: v for k, v in summary_data.items() if k not in ['witnesses', 'uncovered', 'nonmonotone']}, indent=2), flush=True)
    print('Independent old-case controls: PASS', flush=True)


if __name__ == '__main__':
    main()
