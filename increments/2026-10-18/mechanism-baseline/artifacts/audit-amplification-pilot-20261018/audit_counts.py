#!/usr/bin/env python3
"""Independent exhaustive multiset-word audit; no producer code is imported.

Choose every set of positions for each block label, reject words violating the
base relations, then count every ordered-by-element-ID pair directly in each
complete extension. There are no ideal-state recurrences or path weights.
"""
from itertools import combinations
from fractions import Fraction
from pathlib import Path
import json

PRODUCER = Path('/workspace/shared/amplification-mechanism-pilot-20261018')
OUT = Path(__file__).resolve().parent
FIXTURES = [('two_independent_chains', (), ls) for ls in
 [(1,1), (1,2), (1,3), (1,4), (1,10), (1,20), (2,1), (20,1), (2,3), (3,2)]]
FIXTURES += [
 ('asymmetric_three_block', ((0,2),), (1,2,1)),
 ('asymmetric_three_block_extreme', ((0,2),), (1,10,2)),
 ('four_block_N', ((0,2), (0,3), (1,3)), (1,2,1,1)),
 ('four_block_N_unequal', ((0,2), (0,3), (1,3)), (2,1,3,2)),
]
CERTIFY = {('two_independent_chains', (1,2)), ('two_independent_chains', (2,3)), ('four_block_N', (1,2,1,1))}

def words(lengths):
    """Every multiset word once, using choices of occupied positions."""
    n = sum(lengths)
    positions = [None] * len(lengths)
    def place(label, remaining):
        if label == len(lengths)-1:
            positions[label] = remaining
            yield tuple(positions)
            return
        for chosen in combinations(remaining, lengths[label]):
            occupied = set(chosen)
            positions[label] = chosen
            yield from place(label+1, tuple(x for x in remaining if x not in occupied))
    yield from place(0, tuple(range(n)))

def inspect(edges, lengths):
    elements = [(u, i) for u, m in enumerate(lengths) for i in range(1, m+1)]
    pairs = list(combinations(elements, 2))
    counts = {pair: 0 for pair in pairs}
    extensions = []
    for pos in words(lengths):
        if any(pos[u][-1] >= pos[v][0] for u, v in edges):
            continue
        linear = tuple(e for _, e in sorted((pos[u][i-1], (u, i)) for u, i in elements))
        extensions.append(linear)
        for (u, i), (v, j) in pairs:
            counts[(u, i), (v, j)] += pos[u][i-1] < pos[v][j-1]
    # This fixture has the complete strict base relation already listed.
    incomparable = [(x,y) for x,y in pairs if x[0]!=y[0] and (x[0],y[0]) not in edges and (y[0],x[0]) not in edges]
    total = len(extensions)
    scores = {pair: min(k, total-k) for pair,k in counts.items() if pair in incomparable}
    best = max(scores.values())
    witnesses = [pair for pair,k in scores.items() if k==best]
    return elements, pairs, counts, extensions, Fraction(best,total), witnesses

def main():
    producer = json.loads((PRODUCER/'exact_results.json').read_text())
    summary=[]
    for name,edges,lengths in FIXTURES:
        case = next(c for c in producer if c['name']==name and c['before']['lengths']==list(lengths))
        assert case['base_n']==len(lengths) and sorted(map(tuple,case['base_relations']))==sorted(edges)
        # Independently identify the lexicographically smallest incomparable pair.
        label_pairs=[(u,v) for u,v in combinations(range(len(lengths)),2) if (u,v) not in edges and (v,u) not in edges]
        selected=min(label_pairs)
        assert case['selected_blocks']==list(selected)
        after=list(lengths)
        after[selected[0]]*=2
        after[selected[1]]*=3
        assert case['after']['lengths']==after
        for stage,ls in [('before',lengths),('after',tuple(after))]:
            els,pairs,counts,extensions,delta,witnesses=inspect(edges,ls)
            ref=case[stage]
            assert len(extensions)==ref['extensions']
            assert delta==Fraction(ref['delta'])
            rows=ref['all_cross_block_pairs']
            expected_cross={pair for pair in pairs if pair[0][0]!=pair[1][0]}
            recorded_cross=[(tuple(row['u']),tuple(row['v'])) for row in rows]
            assert len(recorded_cross)==len(expected_cross) and set(recorded_cross)==expected_cross
            for row in rows:
                pair=tuple(row['u']),tuple(row['v'])
                assert counts[pair]==row['numerator'], (name,stage,pair)
                assert row['denominator']==len(extensions)
                probability=Fraction(counts[pair],len(extensions))
                assert Fraction(row['reduced'])==probability
                u,v=pair[0][0],pair[1][0]
                comparable=(u,v) in edges or (v,u) in edges
                assert row['comparable']==comparable
                if not comparable:
                    assert Fraction(row['balance'])==min(probability,1-probability)
            actual_witnesses={tuple(map(tuple,(w['u'],w['v']))) for w in ref['witnesses']}
            assert actual_witnesses==set(witnesses)
            for w in ref['witnesses']:
                pair=tuple(w['u']),tuple(w['v'])
                assert Fraction(w['p'])==Fraction(counts[pair],len(extensions))
                assert Fraction(w['balance'])==delta
            slug=name+'_'+ '_'.join(map(str,ls))
            # Full certificates retain original labels, including same-chain pairs.
            rows=['u_label,u_chain_index,v_label,v_chain_index,count_u_before_v,total_extensions,probability,balance']
            for (u,i),(v,j) in pairs:
                k=counts[(u,i),(v,j)]
                rows.append(f'{u},{i},{v},{j},{k},{len(extensions)},{Fraction(k,len(extensions))},{Fraction(min(k,len(extensions)-k),len(extensions))}')
            if (name,lengths) in CERTIFY:
                (OUT/(slug+'_all_pairs.csv')).write_text('\n'.join(rows)+'\n')
                (OUT/(slug+'_extensions.txt')).write_text('\n'.join(' '.join(f'{u}:{i}' for u,i in ext) for ext in extensions)+'\n')
            summary.append({'case':name,'stage':stage,'lengths':ls,'selected_original_block_labels':selected,'extensions':len(extensions),'all_unordered_element_pairs':len(pairs),'delta':str(delta),'witnesses':[{'u':x,'v':y,'u_before_v_count':counts[x,y],'extensions':len(extensions)} for x,y in witnesses]})
    result={'status':'PASS','method':'Exhaust all multiset block words via position combinations, filter base relations, count every element pair in every complete linear extension. No producer code is imported.','checks':summary}
    (OUT/'independent_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print('PASS:', len(FIXTURES), 'input cases,', len(summary), 'states,', sum(x['extensions'] for x in summary), 'complete extensions,', sum(x['all_unordered_element_pairs'] for x in summary), 'full element-pair entries.')

if __name__=='__main__':
    main()
