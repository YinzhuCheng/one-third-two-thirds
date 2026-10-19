#!/usr/bin/env python3
"""Independent auditor: enumerate original labeled linear extensions.
No producer imports, chain-state dynamic programming, or shuffle formulas.
Each expanded label has its own predecessor bit mask; DFS visits complete
linear extensions and counts every originally labeled cross-block pair.
"""
from fractions import Fraction
from itertools import combinations
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parent

def audit(base_edges, lengths):
    labels=[(u,i) for u,m in enumerate(lengths) for i in range(1,m+1)]
    ids={x:i for i,x in enumerate(labels)}
    pred=[0]*len(labels)
    for u,m in enumerate(lengths):
        for i in range(2,m+1): pred[ids[u,i]] |= 1 << ids[u,i-1]
    for u,v in base_edges:
        for i in range(1,lengths[u]+1):
            for j in range(1,lengths[v]+1): pred[ids[v,j]] |= 1 << ids[u,i]
    # Cross-block pair counters retain original expanded labels.
    pairs=[(x,y) for x,y in combinations(range(len(labels)),2)
           if labels[x][0]!=labels[y][0]]
    totals={pair:0 for pair in pairs}
    full=(1<<len(labels))-1
    extension_count=0
    def visit(mask,order):
        nonlocal extension_count
        if mask==full:
            extension_count+=1
            pos={v:j for j,v in enumerate(order)}
            for pair in pairs:
                if pos[pair[0]]<pos[pair[1]]: totals[pair]+=1
            return
        for x in range(len(labels)):
            if not (mask>>x)&1 and not (pred[x]&~mask):
                visit(mask | 1<<x,order+(x,))
    visit(0,())
    assert extension_count>0
    # Infer comparability from probabilities of full labeled extensions;
    # pairs with probability 0 or 1 are harmless and have balance zero.
    rows=[]
    delta=Fraction(0)
    for (x,y),num in totals.items():
        p=Fraction(num,extension_count)
        bal=min(p,1-p)
        delta=max(delta,bal)
        rows.append({'x':list(labels[x]),'y':list(labels[y]),'count':num,
                     'total':extension_count,'p':str(p),'balance':str(bal)})
    return {'base_edges':base_edges,'lengths':lengths,
            'extensions':extension_count,'delta':str(delta),'pairs':rows}

if __name__=='__main__':
    cases=[([], [3,2]),([], [2,2]),([], [3,1]),([], [2,1]),
           ([], [4,3]),([], [3,3]),([], [4,2]),
           ([(0,2),(1,2)], [2,2,1])]
    result=[audit(edges,lengths) for edges,lengths in cases]
    (ROOT/'labeled_counts.json').write_text(json.dumps(result,indent=2)+'\n')
    for row in result: print(row['base_edges'],row['lengths'],row['extensions'],row['delta'])
