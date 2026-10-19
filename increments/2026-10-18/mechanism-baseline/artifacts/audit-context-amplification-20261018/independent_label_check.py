#!/usr/bin/env python3
"""Independent, small full-permutation labeled check of the N mixture.

This does not import the derivation worker's code. Legal orders are selected
from all permutations of distinct labels by direct position inequalities.
"""
from collections import Counter, defaultdict
from fractions import Fraction as F
from itertools import permutations, product
from math import comb, factorial
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent

def choose(n, r):
    return comb(n,r) if n >= 0 and 0 <= r <= n else 0

def inspect(a,b,c,d):
    chains = {v:tuple(f'{v}{i}' for i in range(1,n+1))
              for v,n in zip('ABCD',(a,b,c,d))}
    labels = sum(chains.values(),())
    totals=Counter()
    event=defaultdict(Counter)
    prefixes=defaultdict(Counter)
    for order in permutations(labels):
        pos={x:i for i,x in enumerate(order)}
        if any(any(pos[ch[i]] > pos[ch[i+1]] for i in range(len(ch)-1))
               for ch in chains.values()):
            continue
        # These inequalities plus the checked internal orders impose all
        # expanded N relations and only those relations.
        if not (pos[chains['A'][-1]] < pos['C1']
                and pos[chains['A'][-1]] < pos['D1']
                and pos[chains['B'][-1]] < pos['D1']):
            continue
        k=sum(pos[x] < pos['D1'] for x in chains['C'])
        totals[k]+=1
        prefix=order[:pos['D1']]
        prefixes[k][prefix]+=1
        for j in range(1,b+1):
            event[k][j]+=pos['A1'] < pos[f'B{j}']
    E=sum(totals.values())
    weights=[]
    for k in range(c+1):
        n=a+b+k
        r=a+k
        tail=comb(c-k+d-1,c-k)
        w=comb(n,r)*tail
        assert totals[k]==w, (a,b,c,d,k,totals[k],w)
        assert len(prefixes[k])==comb(n,r)
        assert set(prefixes[k].values())=={tail}
        for j in range(1,b+1):
            q=1-F(choose(n-j,r),comb(n,r))
            assert F(event[k][j],w)==q
        weights.append(w)
    p=[F(0)]+[F(sum(event[k][j] for k in range(c+1)),E)
                     for j in range(1,b+1)]+[F(1)]
    jumps=[p[j]-p[j-1] for j in range(1,b+2)]
    h=sum(F(weights[k],E)*F(a+k,a+b+k) for k in range(c+1))
    H=F(a+c,a+b+c)
    assert max(jumps)==h==p[1]
    assert h < H < 1
    assert all(0 < x < 1 for x in p[1:-1])
    nearest_all=min(range(b+2),key=lambda j: (abs(p[j]-F(1,2)),j))
    assert 1 <= nearest_all <= b
    assert min(p[nearest_all],1-p[nearest_all]) >= F(1,2)-h/2
    if c==d==1:
        assert h == F((a+1)*(2*a+b),(a+b)*(2*a+b+2))
    return {
        'lengths':[a,b,c,d], 'all_labeled_permutations':factorial(len(labels)),
        'legal_extensions':E, 'k_counts':[totals[k] for k in range(c+1)],
        'A1_before_Bj_counts_by_k':[[event[k][j] for j in range(1,b+1)]
                                   for k in range(c+1)],
        'p_grid_with_sentinels':[str(x) for x in p],
        'grid_jumps':[str(x) for x in jumps],
        'h':str(h), 'H':str(H), 'actual_witness_j':nearest_all,
        'pair_balance':str(min(p[nearest_all],1-p[nearest_all])),
        'lower_bound':str(F(1,2)-h/2),
        'prefix_uniformity':'every distinct labeled prefix has exactly T_k completions'
    }

def main():
    cases=[(1,1,1,1),(1,2,1,1),(2,1,1,1),(2,2,1,1),
           (2,1,2,1),(1,2,1,2),(2,2,2,1),(1,3,2,2),
           (2,1,1,3),(1,1,3,2),(1,5,1,1)]
    reports=[inspect(*x) for x in cases]
    out={'status':'PASS','method':'full permutations of distinct element labels, independently filtered by direct position inequalities',
         'cases':len(reports), 'all_permutations_tested':sum(r['all_labeled_permutations'] for r in reports),
         'legal_extensions_checked':sum(r['legal_extensions'] for r in reports), 'reports':reports}
    (ROOT/'independent_label_results.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))

if __name__=='__main__': main()
