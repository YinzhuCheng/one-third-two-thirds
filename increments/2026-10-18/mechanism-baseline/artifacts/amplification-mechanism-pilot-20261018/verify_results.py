#!/usr/bin/env python3
"""Independent explicit-element enumeration for the decisive counterexamples."""
from fractions import Fraction
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parent

def explicit_enumeration(n,relations,lengths):
    elements=[(u,i) for u in range(n) for i in range(1,lengths[u]+1)]
    index={e:k for k,e in enumerate(elements)}
    preds=[]
    for u,i in elements:
        before={(u,i-1)} if i>1 else set()
        before.update((v,j) for v,w in relations if w==u for j in range(1,lengths[v]+1))
        preds.append(sum(1<<index[e] for e in before))
    cross=[(k,l) for k,(u,i) in enumerate(elements) for l,(v,j) in enumerate(elements) if u<v]
    counts={pair:0 for pair in cross}
    number=0
    full=(1<<len(elements))-1
    def visit(mask,positions):
        nonlocal number
        if mask==full:
            number+=1
            for k,l in cross:
                if positions[k]<positions[l]: counts[k,l]+=1
            return
        for k in range(len(elements)):
            if not (mask>>k)&1 and preds[k]&mask==preds[k]:
                positions[k]=mask.bit_count()
                visit(mask|(1<<k),positions)
    visit(0,[None]*len(elements))
    return number,{(elements[k],elements[l]):v for (k,l),v in counts.items()}

def main():
    results=json.loads((ROOT/'exact_results.json').read_text())
    checked=[]
    for case in results:
        decisive=(case['name']=='two_independent_chains' and case['before']['lengths'] in [[1,2],[2,3]]) or case['name']=='four_block_N'
        if not decisive: continue
        for stage in ['before','after']:
            table=case[stage]
            total,counts=explicit_enumeration(case['base_n'],case['base_relations'],table['lengths'])
            assert total==table['extensions']
            for row in table['all_cross_block_pairs']:
                assert counts[tuple(row['u']),tuple(row['v'])]==row['numerator']
            checked.append({'case':case['name'],'lengths':table['lengths'],
                            'explicit_extensions':total,'cross_pairs_checked':len(counts)})
    assert len(checked)==6
    # Verify both one-step failure and non-monotonicity in the opposite direction.
    get=lambda ls: next(c for c in results if c['name']=='two_independent_chains' and c['before']['lengths']==ls)
    x=get([1,2]); assert Fraction(x['before']['delta'])==Fraction(1,3) and Fraction(x['after']['delta'])==Fraction(13,28)
    x=get([1,1]); assert Fraction(x['after']['delta']) < Fraction(x['before']['delta'])
    report={'status':'PASS','independent_explicit_checks':checked,
            'all_two_chain_pairs_cross_checked_by_hypergeometric_formula':True}
    (ROOT/'verification.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))

if __name__=='__main__': main()
