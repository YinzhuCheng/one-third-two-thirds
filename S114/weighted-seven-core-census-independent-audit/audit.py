#!/usr/bin/env python3
"""Independent actual-label constrained-extension audit; Python stdlib only.

No author code is imported or run. The oracle adds x<y by discarding every
original ideal containing y without x and counts paths on the induced DAG.
All checks use explicit exceptions and remain active under python -O.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations, product
from math import comb
from pathlib import Path
import argparse
import hashlib
import json

ROOT = Path(__file__).resolve().parent
AUTHOR = ROOT.parent / 'weighted-seven-core-census'
COVERS = ((0,3),(1,2),(1,4),(2,3),(2,6),(3,5),(4,5))
DUAL = (6,5,3,2,4,1,0)
OLD = ('B1<B0','T6<T5','T2<T0','B6<B3')
MIDDLE = ('B2<B4','T4<T3')

def require(condition, message):
    if not condition:
        raise RuntimeError(message)

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def closure():
    relation = [[False]*7 for _ in range(7)]
    for i,j in COVERS:
        relation[i][j] = True
    for k in range(7):
        for i in range(7):
            for j in range(7):
                relation[i][j] |= relation[i][k] and relation[k][j]
    return relation

REL = closure()

def bottom_good_pairs(relation):
    lower = [{k for k in range(7) if relation[k][i]} for i in range(7)]
    upper = [{k for k in range(7) if relation[i][k]} for i in range(7)]
    answer = []
    for i,j in product(range(7), repeat=2):
        if i == j or relation[i][j] or relation[j][i]:
            continue
        difference = upper[j] - upper[i]
        if lower[i] <= lower[j] and all(relation[x][y] or relation[y][x]
                                         for x,y in combinations(difference,2)):
            answer.append((i,j))
    return answer

BOTTOM = bottom_good_pairs(REL)
REVERSE = [[REL[j][i] for j in range(7)] for i in range(7)]
TOP = [(j,i) for i,j in bottom_good_pairs(REVERSE)]
ARROWS = [('B',i,j) for i,j in BOTTOM] + [('T',i,j) for i,j in TOP]
NAMES = tuple(f'{p}{i}<{p}{j}' for p,i,j in ARROWS)

def independent_cone():
    """Global rectangular bound, not the author's floor/interval enumerator.

    Four strict conditions imply 2t <= a+d+3b+3c-4 <= 20.
    Then 2u <= 15+v and 2v <= 15+u, so u,v <= 15.
    """
    output = set()
    candidates = 0
    for a,b,c,d in product(range(1,4),repeat=4):
        for u,t,v in product(range(2,16),range(1,11),range(2,16)):
            candidates += 1
            if (2*u < a+b+t+v and 2*v < u+c+t+d
                    and 2*t < b+c+u and 2*t < b+c+v):
                output.add((u,a,b,c,t,d,v))
    return output, candidates

class LabelledIdealOracle:
    def __init__(self, weights):
        self.labels = [(block,rank) for block,size in enumerate(weights)
                       for rank in range(1,size+1)]
        self.index = {label:k for k,label in enumerate(self.labels)}
        n = len(self.labels)
        # Reconstruct every transitive actual-label predecessor, independently
        # of a block-prefix recurrence or the author's cover-mask construction.
        predecessors = []
        for block,rank in self.labels:
            predecessors.append(sum(1 << k for k,(b,r) in enumerate(self.labels)
                                    if REL[b][block] or (b == block and r < rank)))
        full = (1 << n)-1
        pending = [0]
        discovered = {0}
        graph = {}
        while pending:
            ideal = pending.pop()
            missing = full ^ ideal
            following = []
            while missing:
                bit = missing & -missing
                missing ^= bit
                k = bit.bit_length()-1
                if predecessors[k] & ideal == predecessors[k]:
                    nxt = ideal | bit
                    following.append(nxt)
                    if nxt not in discovered:
                        discovered.add(nxt)
                        pending.append(nxt)
            graph[ideal] = following
        # Adding a label increases the integer mask, so this is topological.
        self.masks = sorted(discovered)
        indices = {mask:k for k,mask in enumerate(self.masks)}
        self.children = [tuple(indices[x] for x in graph[mask]) for mask in self.masks]
        self.last = len(self.masks)-1
        require(self.masks[self.last] == full,'Full ideal missing')
        self.base = [0]*len(self.masks)
        self.base[self.last] = 1
        for k in range(self.last-1,-1,-1):
            self.base[k] = sum(self.base[j] for j in self.children[k])
        self.total = self.base[0]
        self.cache = {}

    def count_before(self,x,y):
        """Count all extensions of the poset augmented by the edge x<y.

        Invalid original ideals have y present and x absent. Once x is present,
        the added relation is resolved and the original suffix count applies.
        Otherwise sum allowed child counts. This is a separate constrained
        recurrence, not a forward/backward transition-event accumulator.
        """
        if (x,y) in self.cache:
            return self.cache[x,y]
        xb,yb = 1<<x,1<<y
        values = [0]*len(self.masks)
        for k in range(self.last,-1,-1):
            mask = self.masks[k]
            if mask & xb:
                values[k] = self.base[k]
            elif mask & yb:
                values[k] = 0
            else:
                values[k] = sum(values[j] for j in self.children[k])
        self.cache[x,y] = values[0]
        return values[0]

    def endpoints(self,weights):
        counts = {}
        for port,i,j in ARROWS:
            x = self.index[i,1 if port == 'B' else weights[i]]
            y = self.index[j,1 if port == 'B' else weights[j]]
            counts[f'{port}{i}<{port}{j}'] = self.count_before(x,y)
        return counts

    def all_incomparable(self):
        answer = []
        for x,y in combinations(range(len(self.labels)),2):
            i,r = self.labels[x]
            j,s = self.labels[y]
            if i == j or REL[i][j] or REL[j][i]:
                continue
            answer.append((self.labels[x],self.labels[y],self.count_before(x,y)))
        return answer

def diagnostic(weights):
    u,a,b,c,t,d,v = weights
    A = comb(a+b+t+v+u,u)
    B = comb(d+c+t+u+v,v)
    bounds = ((comb(b+t+v+u,u),A), (comb(c+t+u+v,v),B),
              (comb(a+b+u-1,u),A), (comb(d+c+v-1,v),B))
    flags = [3*n > 2*z if k < 2 else 3*n < z
             for k,(n,z) in enumerate(bounds)]
    return bounds,flags

def all_minimum_menus(records):
    universe = (1<<len(records))-1
    rejected = {name:0 for name in NAMES}
    for k,row in enumerate(records):
        for name in row['failed_arrows']:
            rejected[name] |= 1<<k
    checked = Counter()
    for size in range(len(NAMES)+1):
        menus = []
        for names in combinations(NAMES,size):
            checked[size] += 1
            mask = 0
            for name in names:
                mask |= rejected[name]
            if mask == universe:
                menus.append(list(names))
        if menus:
            return {'size':size,'menus':menus,
                    'subsets_tested_by_size':dict(sorted(checked.items()))}
    raise RuntimeError('Full menu does not cover the actual complete cone')

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output',default=str(ROOT/'results.json'))
    args = parser.parse_args()
    author_hashes = {}
    for line in (AUTHOR/'MANIFEST.sha256').read_text().splitlines():
        expected,name = line.split(maxsplit=1)
        author_hashes[name] = digest(AUTHOR/name)
        require(author_hashes[name] == expected, f'Frozen author hash mismatch: {name}')
    source = json.loads((AUTHOR/'census.json').read_text())
    verification = json.loads((AUTHOR/'verification.json').read_text())
    analytic_source = json.loads((AUTHOR/'analytic_filters.json').read_text())
    require(source['scope_max_spine'] == 3,'Unexpected author scope')
    require(list(NAMES) == source['arrows'],'Structural arrow reconstruction mismatch')
    require(len(NAMES) == 18,'Unexpected arrow number')
    universe,candidates = independent_cone()
    original = {tuple(row['weights']):row for row in source['records']}
    require(len(original) == len(source['records']),'Duplicate author vectors')
    require(universe == set(original),'Cone sets differ')
    author_pair_rows = {tuple(row['weights']):row for row in verification['per_vector']}
    old_details = {tuple(row['weights']):row for row in source['old_four_menu_survivor_actual_dp']}
    require(set(author_pair_rows) == universe,'Author all-pair coverage differs')
    rows = []
    total_pairs = total_balanced = total_states = 0
    for count,weights in enumerate(sorted(universe,key=lambda w:(sum(w),w)),1):
        oracle = LabelledIdealOracle(weights)
        z = oracle.total
        endpoints = oracle.endpoints(weights)
        claimed = original[weights]
        require(z == claimed['extensions'],f'Denominator mismatch {weights}')
        require([endpoints[name] for name in NAMES] == claimed['forced_endpoint_numerators'],
                f'Endpoint mismatch {weights}')
        require(len(oracle.masks) == claimed['ideal_states'],f'Ideal count mismatch {weights}')
        failures = [name for name,n in endpoints.items() if 3*n <= 2*z]
        equalities = [name for name,n in endpoints.items() if 3*n == 2*z]
        require([NAMES.index(name) for name in failures] == claimed['failed_forced_arrow_indices'],
                f'Closed threshold mismatch {weights}')
        require(failures,f'Unrejected vector {weights}')
        pairs = oracle.all_incomparable()
        best = max(min(n,z-n) for x,y,n in pairs)
        maximizers = [{'x':list(x),'y':list(y),'numerator_x_before_y':n}
                      for x,y,n in pairs if min(n,z-n) == best]
        balanced = sum(z <= 3*n <= 2*z for x,y,n in pairs)
        delta = str(Fraction(best,z))
        reference = author_pair_rows[weights]
        require(len(pairs) == reference['incomparable_pair_count'],f'Pair count mismatch {weights}')
        require(balanced == reference['balanced_pair_count'],f'Balanced count mismatch {weights}')
        require(delta == reference['delta_reduced'],f'Delta mismatch {weights}')
        require(maximizers == reference['maximizing_pairs'],f'Maximizers mismatch {weights}')
        require(3*best >= z,f'No actual balanced pair {weights}')
        if weights in old_details:
            all_pairs = [{'x':list(x),'y':list(y),'numerator_x_before_y':n} for x,y,n in pairs]
            require(all_pairs == old_details[weights]['incomparable_pairs'],
                    f'Old survivor all-pair numerators mismatch {weights}')
        bounds,flags = diagnostic(weights)
        row = {'weights':weights,'extensions':z,'ideal_states':len(oracle.masks),
               'endpoint_numerators':endpoints,'failed_arrows':failures,
               'threshold_equalities':equalities,'incomparable_pair_count':len(pairs),
               'balanced_pair_count':balanced,'delta':delta,'maximizers':maximizers,
               'analytic_bounds':bounds,'analytic_passes':flags}
        rows.append(row)
        total_pairs += len(pairs)
        total_balanced += balanced
        total_states += len(oracle.masks)
        if count % 250 == 0:
            print(f'Independently counted {count}/{len(universe)} vectors',flush=True)
    byweights = {tuple(r['weights']):r for r in rows}
    dual_map = {}
    for p,i,j in ARROWS:
        other = 'T' if p == 'B' else 'B'
        dual_map[f'{p}{i}<{p}{j}'] = f'{other}{DUAL[j]}<{other}{DUAL[i]}'
    for w,row in byweights.items():
        dual = byweights[tuple(w[i] for i in DUAL)]
        require(row['extensions'] == dual['extensions'],'Dual denominator mismatch')
        for name,other in dual_map.items():
            require(row['endpoint_numerators'][name] == dual['endpoint_numerators'][other],
                    f'Dual endpoint mismatch {w} {name}')
    summaries = []
    for m in range(1,4):
        selected = [r for r in rows if max(r['weights'][i] for i in (1,2,3,5)) <= m]
        survivors = [r for r in selected if not set(OLD)&set(r['failed_arrows'])]
        live = selected
        sequential = []
        for name in OLD+MIDDLE:
            live = [r for r in live if name not in r['failed_arrows']]
            sequential.append(len(live))
        diagnostic_live = selected
        diagnostic_sequential = []
        for k in range(4):
            diagnostic_live = [r for r in diagnostic_live if r['analytic_passes'][k]]
            diagnostic_sequential.append(len(diagnostic_live))
        analytic_then_old = [r['weights'] for r in diagnostic_live
                             if not set(OLD)&set(r['failed_arrows'])]
        menus = all_minimum_menus(selected)
        claimed = source['summaries'][m-1]
        require(len(selected) == claimed['cone_vectors'],'Scope size mismatch')
        require([list(r['weights']) for r in survivors] == claimed['old_four_menu_survivors'],
                'Old survivor mismatch')
        require(menus['size'] == claimed['minimum_arrow_covers']['minimum_size'],'Minimum size mismatch')
        require(menus['menus'] == claimed['minimum_arrow_covers']['minimum_subsets'],'Minimum menus mismatch')
        aclaimed = analytic_source['summaries'][m-1]
        require(len(diagnostic_live) == aclaimed['analytic_survivor_count'],'Analytic count mismatch')
        require([list(w) for w in analytic_then_old] == aclaimed['analytic_survivors_then_old_four_exact'],
                'Analytic/old intersection mismatch')
        summaries.append({'maximum_spine_weight':m,'spines':m**4,'cone_vectors':len(selected),
                          'maximum_order':max(sum(r['weights']) for r in selected),
                          'old_four_survivors':[r['weights'] for r in survivors],
                          'six_test_survivor_counts':sequential,
                          'full_eighteen_survivors':sum(not r['failed_arrows'] for r in selected),
                          'minimum_menus':menus,'analytic_sequential_counts':diagnostic_sequential,
                          'analytic_then_old_four_survivors':analytic_then_old})
    analytic_observed = {tuple(r['weights']) for r in rows if all(r['analytic_passes'])}
    require(analytic_observed == {tuple(r['weights']) for r in analytic_source['analytic_survivors']},
            'Entire analytic survivor set mismatch')
    min_delta = min(Fraction(r['delta']) for r in rows)
    output = {'verdict':'PASS','independent_peer_audit':True,
              'oracle':'Actual-label augmented-comparison ideal-path recurrence; no author code imported',
              'author_sha256':author_hashes,'spine_scope':[1,2,3],
              'rectangular_cone_candidates_checked':candidates,'cone_set_equality':True,
              'all_spines_counted':81,'cone_vectors':len(rows),'arrows':NAMES,
              'independent_denominator_comparisons':len(rows),
              'independent_endpoint_comparisons':18*len(rows),
              'independent_actual_incomparable_pair_counts':total_pairs,
              'independent_balanced_pairs':total_balanced,'aggregate_ideal_states':total_states,
              'threshold_equality_occurrences':sum(len(r['threshold_equalities']) for r in rows),
              'minimum_delta_within_cone_only':str(min_delta),
              'minimum_delta_vectors':[r['weights'] for r in rows if Fraction(r['delta']) == min_delta],
              'summaries':summaries,'records':rows,
              'infinite_family_scope':'All positive u,t,v with each a,b,c,d in {1,2,3}, conditional on the explicitly identified previously audited structural, port, outer-cone, and generalized-shuffle proof prerequisites. No arbitrary-spine or global delta claim.'}
    Path(args.output).write_text(json.dumps(output,indent=2)+'\n')
    print(json.dumps({k:v for k,v in output.items() if k not in ('records','author_sha256')},indent=2))

if __name__ == '__main__':
    main()
