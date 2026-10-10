#!/usr/bin/env python3
"""Independent exhaustive ideal-DAG certificate for the MC3 examples.

Only the small candidate JSON is used as input. No discoverer/verifier code is
imported. All pair counts are obtained at once by forward/backward path counts
on the DAG of chain-prefix ideals, not by adding comparison edges.
"""
import argparse
import hashlib
import itertools
import json
from fractions import Fraction
from pathlib import Path


def closure(n, edges):
    # Independently traverse the generating graph from every start vertex.
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
    R = []
    for start in range(n):
        seen, todo = set(), list(adj[start])
        while todo:
            v = todo.pop()
            if v not in seen:
                seen.add(v)
                todo.extend(adj[v])
        assert start not in seen, 'The generating relation has a cycle.'
        R.append(seen)
    pred = [sum(1 << u for u in range(n) if v in R[u]) for v in range(n)]
    return R, pred


def ideal_dag_counts(chains, edges):
    n = sum(map(len, chains))
    assert sorted(itertools.chain.from_iterable(chains)) == list(range(n))
    R, pred = closure(n, edges)
    for chain in chains:
        assert all(v in R[u] for u, v in itertools.combinations(chain, 2))
    prefix_masks = []
    for chain in chains:
        masks = [0]
        for v in chain:
            masks.append(masks[-1] | (1 << v))
        prefix_masks.append(masks)
    states = []
    masks = {}
    for state in itertools.product(*(range(len(c) + 1) for c in chains)):
        mask = 0
        for j, count in enumerate(state):
            mask |= prefix_masks[j][count]
        # Every included vertex must contain ALL predecessors, including those
        # supplied by the transitive closure of cross-chain generating edges.
        included = [u for u in range(n) if mask >> u & 1]
        if all(pred[u] & mask == pred[u] for u in included):
            states.append(state)
            masks[state] = mask
    states.sort(key=lambda s: (sum(s), s))
    edges_dag = {}
    for state in states:
        outgoing = []
        for j, chain in enumerate(chains):
            if state[j] == len(chain):
                continue
            v = chain[state[j]]
            if pred[v] & masks[state] == pred[v]:
                dest = tuple(count + (j == k) for k, count in enumerate(state))
                assert dest in masks
                outgoing.append((dest, v))
        edges_dag[state] = outgoing
    start = tuple(0 for _ in chains)
    end = tuple(map(len, chains))
    F = {state: 0 for state in states}
    F[start] = 1
    for state in states:
        for dest, v in edges_dag[state]:
            F[dest] += F[state]
    G = {state: 0 for state in states}
    G[end] = 1
    for state in reversed(states):
        for dest, v in edges_dag[state]:
            G[state] += G[dest]
    E = F[end]
    assert G[start] == E
    assert all(F[s] > 0 and G[s] > 0 for s in states)
    # The edge s -> s+v is used by F[s]G[s+v] extensions. Each extension
    # contributes once to N[u,v], at the unique edge where v is appended.
    N = [[0] * n for _ in range(n)]
    for state in states:
        included = [u for u in range(n) if masks[state] >> u & 1]
        for dest, v in edges_dag[state]:
            weight = F[state] * G[dest]
            for u in included:
                N[u][v] += weight
    for u, v in itertools.combinations(range(n), 2):
        assert N[u][v] + N[v][u] == E
        if v in R[u]:
            assert N[u][v] == E and N[v][u] == 0
        if u in R[v]:
            assert N[v][u] == E and N[u][v] == 0
    rank_mass = [0] * (n + 1)
    for state in states:
        rank_mass[sum(state)] += F[state] * G[state]
    assert rank_mass == [E] * (n + 1)
    return R, pred, E, N, len(states), sum(map(len, edges_dag.values()))


def self_test():
    # Exhaustive permutations on small, fixed examples independently test
    # both the number of extensions and every ordered-pair marginal.
    chains = [[0, 1], [2, 3], [4, 5]]
    base = [(0, 1), (2, 3), (4, 5)]
    cross = [(0, 3), (2, 5), (0, 5), (4, 3)]
    tested = 0
    for bits in range(1 << len(cross)):
        edges = base + [e for j, e in enumerate(cross) if bits >> j & 1]
        R, pred, E, N, _, _ = ideal_dag_counts(chains, edges)
        brute_E = 0
        brute_N = [[0] * 6 for _ in range(6)]
        for order in itertools.permutations(range(6)):
            pos = [0] * 6
            for i, u in enumerate(order):
                pos[u] = i
            if all(pos[u] < pos[v] for u, v in edges):
                brute_E += 1
                for i, u in enumerate(order):
                    for v in order[i + 1:]:
                        brute_N[u][v] += 1
        assert (E, N) == (brute_E, brute_N)
        tested += 1
    return tested


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', type=Path, default=Path(__file__).parent / 'mc3_coupled_search/MC3_COUNTEREXAMPLE_high.json')
    parser.add_argument('--outdir', type=Path, default=Path(__file__).parent)
    parser.add_argument('--stem', default='mc3_counterexample_audit')
    args = parser.parse_args()
    raw = args.input.read_bytes()
    src = json.loads(raw)
    chains, cursor = [], 0
    for length in src['shape']:
        chains.append(list(range(cursor, cursor + length)))
        cursor += length
    n = cursor
    generating = [list(e) for c in chains for e in zip(c, c[1:])] + src['extra_edges']
    labels = {'x': 0, 'y': len(chains[0]), 'a': len(chains[0]) + len(chains[1]), 'b': len(chains[0]) + len(chains[1]) + 1}
    x, y, a, b = (labels[z] for z in ('x', 'y', 'a', 'b'))
    assert len(chains) == 3 and len(chains[0]) == 2
    small_checks = self_test()
    R, pred, E, N, ideals, transitions = ideal_dag_counts(chains, generating)
    covers = [[u, v] for u in range(n) for v in sorted(R[u])
              if not any(v in R[w] for w in R[u])]
    assert closure(n, covers)[0] == R
    minima = [u for u in range(n) if pred[u] == 0]
    assert x in minima and y in minima
    antichain = [x, y, a]
    assert all(v not in R[u] and u not in R[v] for u, v in itertools.combinations(antichain, 2))
    upx, upy = {x} | R[x], {y} | R[y]
    B = sorted(set(range(n)) - upx - upy)
    assert B == [a, b] and b in R[a]
    pair_labels = [('a', 'x'), ('a', 'y'), ('b', 'x'), ('b', 'y'), ('x', 'y')]
    menu = []
    for left, right in pair_labels:
        u, v = labels[left], labels[right]
        assert u not in R[v] and v not in R[u]
        k = N[u][v]
        f = Fraction(k, E)
        menu.append({'pair': f'{left}<{right}', 'indices': [u, v], 'count': k,
                     'reverse_count': N[v][u], 'probability_reduced': str(f),
                     'probability_decimal': float(f), 'balanced': E <= 3 * k <= 2 * E,
                     'three_count_minus_total': 3 * k - E,
                     'three_count_minus_twice_total': 3 * k - 2 * E})
    expected_counts_match = E == int(src['E']) and [m['count'] for m in menu] == list(map(int, src['K']))
    assert expected_counts_match
    assert all(not m['balanced'] for m in menu)
    slacks = [3 * N[a][x] - 2 * E, 3 * N[a][y] - 2 * E,
              3 * N[x][y] - 2 * E, E - 3 * N[b][x], 3 * N[b][y] - 2 * E]
    assert all(s > 0 for s in slacks)
    balanced = []
    for u, v in itertools.combinations(range(n), 2):
        if E <= 3 * N[u][v] <= 2 * E:
            balanced.append({'indices': [u, v], 'count': N[u][v],
                             'reverse_count': N[v][u],
                             'probability_reduced': str(Fraction(N[u][v], E)),
                             'probability_decimal': float(Fraction(N[u][v], E))})
    assert balanced
    simple_pair = next((row for row in balanced if row['indices'] == [y, b + 1]), balanced[0])
    nearest = sorted(balanced, key=lambda d: (abs(2 * d['count'] - E), d['indices']))[:5]
    result = {
        'verdict': 'Confirmed MC3 five-pair menu counterexample; not a main theorem or WIDTH3 counterexample.',
        'source_file': str(args.input), 'source_sha256': hashlib.sha256(raw).hexdigest(),
        'method': 'Independent transitive closure traversal; enumerate every chain-prefix ideal; exact forward/backward extension counts; all ordered-pair marginals from transition weights.',
        'n': n, 'labels': labels, 'chain_cover': chains, 'generating_edges': generating,
        'covers': covers, 'strict_closure': [sorted(row) for row in R],
        'minimal_elements': minima, 'antichain_witness': antichain, 'width': 3,
        'reflexive_up_x': sorted(upx), 'reflexive_up_y': sorted(upy), 'avoidance_B': B,
        'total_extensions': E, 'ideal_count': ideals, 'ideal_transition_count': transitions,
        'menu_order': ['ax', 'ay', 'bx', 'by', 'xy'], 'menu': menu,
        'strict_slack_order': ['3Kax-2E', '3Kay-2E', '3Kxy-2E', 'E-3Kbx', '3Kby-2E'],
        'strict_integer_slacks': slacks, 'source_counts_match': expected_counts_match,
        'number_of_balanced_unordered_pairs': len(balanced),
        'balanced_pairs_lex_first_five': balanced[:5], 'balanced_pairs_nearest_half': nearest,
        'simple_balanced_pair': simple_pair,
        'all_balanced_unordered_pairs': balanced,
        'all_ordered_pair_counts': N,
        'checks': {'all_pair_complements_sum_to_E': True,
                   'all_comparable_pair_counts_are_deterministic': True,
                   'all_rank_path_masses_equal_E': True,
                   'covers_reconstruct_same_closure': True,
                   'small_posets_checked_against_all_720_permutations': small_checks}
    }
    out_json = args.outdir / (args.stem + '.json')
    out_json.write_text(json.dumps(result, indent=2) + '\n')
    lines = [
        'S105 independent audit: complete MC3 five-pair menu counterexample',
        '=================================================================',
        result['verdict'], '',
        'Input: ' + str(args.input), 'Input SHA256: ' + result['source_sha256'],
        'No discoverer or existing verifier code was imported or reused.',
        'Only raw candidate shape/extra edges/counts and the confirmed label convention were used as computational input.', '',
        'STRUCTURE',
        'C0: 0=x < 1=t',
        f'C1: {y}=y < {y+1}=y1 < ... < {chains[1][-1]}=y{len(chains[1])-1}',
        f'C2: {a}=a < {b}=b < {b+1}=c1 < ... < {n-1}=c{len(chains[2])-2}',
        'Additional generating edges: ' + json.dumps(src['extra_edges']),
        'All chain-adjacent edges and all extra edges are covers: ' + str(covers == sorted(generating)),
        'Exact cover list: ' + json.dumps(covers),
        f'The 3 displayed chains cover all {n} vertices, so width <= 3.',
        f'The minima are {minima}; this is an antichain of size 3, so width = 3.',
        f'x={x} and y={y} are minimal. Reflexive principal upsets give B=P\\(up(x) union up(y))={B}={{a<b}}.',
        'All five menu pairs are incomparable in the original poset.', '',
        'COUNTING METHOD',
        'Enumerate each triple of chain prefix lengths; retain it iff every included vertex contains all predecessors.',
        f'This yields {ideals} ideals and {transitions} legal one-vertex transitions.',
        'F(I) counts paths from empty to I; G(I) counts paths from I to P.',
        'For each edge I -> I+v, add F(I)*G(I+v) to N(u<v) for every u in I.',
        'Every linear extension contributes exactly once to N(u<v), when v is appended.',
        f'This computes all {n}*{n-1} oriented pair counts at once using only original-poset transitions.',
        f'All {n*(n-1)//2} complementary pair sums equal E. All comparable counts are 0 or E.',
        f'At every one of the {n+1} ranks, sum_I F(I)G(I)=E.',
        f'Algorithm independently tested on {small_checks} small posets by checking all 720 permutations of each.', '',
        'ORIGINAL-LAW EXACT COUNTS', f'E = {E}',
    ]
    for m in menu:
        lines.append(f"{m['pair']}: K={m['count']}; reverse={m['reverse_count']}; p={m['probability_reduced']} = {m['probability_decimal']:.15f}; balanced={m['balanced']}")
    lines += ['', 'STRICT MC3 PREMISE/FAILURE CERTIFICATE']
    for label, slack in zip(result['strict_slack_order'], slacks):
        lines.append(f'{label} = {slack} > 0')
    lines += ['Thus P(a<x), P(a<y), P(x<y) are all strictly >2/3;',
              'q=P(b<x) is strictly <1/3; r=P(b<y) is strictly >2/3.',
              'The five prescribed unordered pairs and their reverse orientations are all unbalanced.', '',
              'WHY THIS IS NOT A MAIN-THEOREM/WIDTH3 COUNTEREXAMPLE',
              f'The full poset has {len(balanced)} balanced unordered pairs. Examples:']
    for row in balanced[:5]:
        lines.append(f"  {row['indices']}: K={row['count']}; reverse={row['reverse_count']}; p={row['probability_reduced']} = {row['probability_decimal']:.15f}")
    lines += ['Simple balanced pair:', json.dumps(simple_pair), 'Closest-to-half balanced pair:', json.dumps(nearest[0]), '',
              'This refutes only the claimed sufficiency of this fixed five-pair MC3 rescue menu under the listed hypotheses.',
              'It does not refute existence of a balanced pair in width-three posets or any broader main theorem.', '',
              'REPRODUCE', f'python3 {Path(__file__).resolve()} --input {args.input} --outdir {args.outdir} --stem {args.stem}',
              f'Machine certificate: {out_json}',
              'All reproduction outputs are local.']
    out_txt = args.outdir / (args.stem + '.txt')
    out_txt.write_text('\n'.join(lines) + '\n')
    print('\n'.join(lines))


if __name__ == '__main__':
    main()
