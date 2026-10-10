#!/usr/bin/env python3
"""Independent exact finite sanity checks for the structural redundancy audit.
The unbounded result is proved in AUDIT.md; this checks all naturally ordered
three-vertex tail extensions of each core, with and without a 2-antichain below.
Uses no author code and no assertions (also runs unchanged under python -O).
"""
from itertools import combinations
from pathlib import Path
import json

CORES = [
    ('six-boundary', 'abcdef', [('a','c'),('a','d'),('b','d'),('c','e'),('b','f'),('c','f')], ('a','b'), ['c','e'], []),
    ('six-triangle', 'abcdef', [('a','c'),('b','d'),('c','e'),('b','f'),('c','f')], ('a','b'), ['c','e'], ['d']),
    ('seven-three-minima', 'abcdefg', [('a','d'),('b','e'),('a','f'),('c','f'),('b','g'),('d','g')], ('a','c'), ['d','g'], []),
]

def require(condition, msg):
    if not condition:
        raise ValueError(msg)

def closure(labels, edges):
    pred = [0]*len(labels)
    for a,b in edges:
        pred[labels.index(b)] |= 1 << labels.index(a)
    for _ in labels:
        for j in range(len(labels)):
            for i in range(len(labels)):
                if pred[j] >> i & 1:
                    pred[j] |= pred[i]
    require(all(not (pred[i] >> i & 1) for i in range(len(labels))), 'cycle')
    return pred

def is_ideal(pred, mask):
    return all(not(mask>>i & 1) or not(p & ~mask) for i,p in enumerate(pred))

def ideals(pred):
    return [s for s in range(1<<len(pred)) if is_ideal(pred,s)]

def upper(pred, i):
    return {j for j,p in enumerate(pred) if p>>i & 1}

def chain(pred, members):
    return all((pred[a]>>b & 1) or (pred[b]>>a & 1) for a,b in combinations(members, 2))

def check_pair(pred,a,b,expected_d,expected_left,expected_right):
    ua,ub=upper(pred,a),upper(pred,b)
    require(pred[a] == pred[b] == expected_d, 'strict lower sets changed')
    require(ua-ub == expected_left, 'first upper difference changed')
    require(ub-ua == expected_right, 'second upper difference changed')
    require(chain(pred,ua-ub) and chain(pred,ub-ua), 'difference not a chain')

def inspect_completion(pred, n, base_pred, pair, expected_d, left, right):
    require(pred[:n] == base_pred, 'core changed')
    maxima = [i for i in range(n) if not upper(base_pred,i)]
    nonmax = set(range(n))-set(maxima)
    require(all(pred[z]>>a & 1 for a in nonmax for z in range(n,len(pred))), 'nonmax guard lemma failed')
    expected_states = {(1<<n)-1-(1<<m) for m in maxima}
    actual_states = {s for s in ideals(pred) if s.bit_count()==n-1}
    require(actual_states==expected_states, 'actual cut support differs')
    require(set().union(*(set(i for i in range(len(pred)) if s>>i&1) for s in actual_states)) == set(range(n)), 'union of support differs from core')
    check_pair(pred,*pair,expected_d,left,right)

def check_family(labels,edges,pair_names,left_names,right_names,h):
    core=closure(labels,edges)
    pred=[0]*h + [((1<<h)-1) | (p<<h) for p in core]
    n=len(pred)
    pair=tuple(labels.index(x)+h for x in pair_names)
    left={labels.index(x)+h for x in left_names}
    right={labels.index(x)+h for x in right_names}
    levels=[pred]
    counts=[]
    for depth in range(4):
        for p in levels:
            inspect_completion(p,n,pred,pair,(1<<h)-1,left,right)
        counts.append(len(levels))
        if depth < 3:
            levels=[p+[s] for p in levels for s in ideals(p) if s.bit_count()>=n-1]
    return {'lower_antichain_size':h,'checked_by_tail_size':dict(enumerate(counts)),'total_checked':sum(counts)}

def main():
    results=[]
    for name, labels,edges,pair,left,right in CORES:
        base=closure(labels,edges)
        check_pair(base,*(labels.index(x) for x in pair),0,{labels.index(x) for x in left},{labels.index(x) for x in right})
        families=[check_family(labels,edges,pair,left,right,h) for h in [0,2]]
        results.append({'core':name,'pair':pair,'strict_lower_sets':[],'upper_difference_first':left,'upper_difference_second':right,'families':families})
    out={'verdict':'PASS','scope':'Exact finite sanity checks; unbounded theorem has a separate proof in AUDIT.md. Three outside vertices, all natural-label predecessor ideals meeting the full guard; lower antichain sizes zero and two.','primary_source':'https://arxiv.org/pdf/1610.00809','source_pin':'arXiv:1610.00809v3, Definition 5 and Theorem 2','results':results}
    Path(__file__).with_name('checks.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))

if __name__=='__main__':
    main()
