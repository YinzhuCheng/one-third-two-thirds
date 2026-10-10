#!/usr/bin/env python3
"""Test structural very-good-pair lifting; theorem existence scope is external."""
from itertools import product,combinations
from collections import Counter
from pathlib import Path
import json
from independent_audit import generate,sign,ischain

def down(up,x):return sum(1<<i for i in range(len(up)) if up[i]&(1<<x))
def verygood(up,a,b,dual=False):
    if a==b:return False
    A,B=(up[a],up[b]) if dual else (down(up,a),down(up,b))
    if A!=B:return False
    X,Y=(down(up,a),down(up,b)) if dual else (up[a],up[b])
    return ischain(up,X&~Y) and ischain(up,Y&~X)

def inflate(up,w):
    offsets=[0]
    for wi in w:offsets.append(offsets[-1]+wi)
    expanded=[]
    for i,wi in enumerate(w):
        for r in range(wi):
            expanded.append(sum(1<<x for j in range(len(w)) if up[i]&(1<<j) for x in range(offsets[j],offsets[j+1]))+sum(1<<x for x in range(offsets[i]+r+1,offsets[i+1])))
    return tuple(expanded),offsets

if __name__=="__main__":
    stats=Counter()
    for n in range(2,6):
        for Q in generate(n):
            witnesses=[(a,b,dual) for a,b in combinations(range(n),2) for dual in (False,True) if verygood(Q,a,b,dual)]
            stats['base_posets']+=1
            if not witnesses:continue
            stats['base_posets_with_very_good_pair']+=1
            for w in product((1,2),repeat=n):
                P,offset=inflate(Q,w)
                stats['weighted_inflations']+=1
                for a,b,dual in witnesses:
                    x=offset[a]+(w[a]-1 if dual else 0)
                    y=offset[b]+(w[b]-1 if dual else 0)
                    assert verygood(P,x,y,dual),(Q,w,a,b,dual)
                    stats['lifted_pair_witnesses']+=1
    report={'status':'PASS','max_quotient_n':5,'each_weight':[1,2],'checks':dict(stats),'source':'https://arxiv.org/html/1610.00809','source_scope':'Definition 5 plus Theorem 2: existence of some balanced pair; chosen very-good pair need not itself be balanced.'}
    Path(__file__).with_name('very_good_results.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))
