#!/usr/bin/env python3
"""Exact isomorphism classification of remaining candidates ONLY.
No claim that the full enumeration was unlabelled. Invariant colour classes
reduce, but do not replace, exhaustive bijection testing within each class.
"""
import argparse,itertools,json
from collections import defaultdict
from pathlib import Path
import catalogue as c


def canonical(up):
    n=len(up);down=c.dual(up)
    # In/out degree is an isomorphism invariant. Class order is fixed by key.
    groups=defaultdict(list)
    for a in range(n):groups[(down[a].bit_count(),up[a].bit_count())].append(a)
    parts=[groups[k] for k in sorted(groups)]
    best=None;best_order=None;equal_best=0
    for product in itertools.product(*(itertools.permutations(group) for group in parts)):
        order=sum(product,());inverse={x:i for i,x in enumerate(order)}
        key=tuple(sum(1<<inverse[b] for b in c.vertices(up[a])) for a in order)
        if best is None or key<best:best=key;best_order=order;equal_best=1
        elif key==best:equal_best+=1
    return best,best_order,equal_best


def classify(records):
    groups={}
    for d in sorted(records,key=lambda d:(d['n'],tuple(d['strict_up_masks']))):
        key,order,automorphisms=canonical(d['strict_up_masks']);k=(d['n'],key)
        if k not in groups:
            groups[k]={'n':d['n'],'canonical_strict_up_masks':list(key),'representative_naturally_labelled':d,'natural_labelled_multiplicity':0,'canonical_order_old_labels':list(order),'automorphisms':automorphisms,'member_strict_up_masks':[]}
        groups[k]['natural_labelled_multiplicity']+=1
        groups[k]['member_strict_up_masks'].append(d['strict_up_masks'])
    result=list(groups.values())
    from independent_tests import exact_pair_counts
    for record in result:
        up=record['representative_naturally_labelled']['strict_up_masks'];n=len(up)
        R={(a,b) for a in range(n) for b in c.vertices(up[a])}
        e,_=exact_pair_counts(n,R);record['linear_extensions_of_representative']=e
        assert e==record['natural_labelled_multiplicity']*record['automorphisms']
    result.sort(key=lambda d:(d['n'],d['representative_naturally_labelled']['width'],len(d['representative_naturally_labelled']['cover_edges']),d['canonical_strict_up_masks']))
    return result

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--input',type=Path,default=Path(__file__).parent/'results/survivors.json');ap.add_argument('--output',type=Path,default=Path(__file__).parent/'results/survivor_isomorphism_classes.json');args=ap.parse_args()
    data=classify(json.loads(args.input.read_text()));args.output.write_text(json.dumps(data,indent=2)+'\n');print(json.dumps({'classes':len(data),'by_n':{n:sum(d['n']==n for d in data) for n in sorted({d['n'] for d in data})},'multiplicities':[d['natural_labelled_multiplicity'] for d in data]}))
