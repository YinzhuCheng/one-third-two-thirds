"""Optional exact checks for S82; no result here replaces the analytic proof."""
from __future__ import annotations
from collections import Counter
from fractions import Fraction as F
from functools import lru_cache
from itertools import combinations
from math import comb
from pathlib import Path
import json


def posets(n: int):
    pairs = list(combinations(range(n), 2))
    for mask in range(1 << len(pairs)):
        pred = [0] * n
        for k, (i, j) in enumerate(pairs):
            if mask >> k & 1:
                pred[j] |= 1 << i
        if all(not(pred[i] & ~pred[j]) for j in range(n)
               for i in range(j) if pred[j] >> i & 1):
            yield tuple(pred)


def extensions(pred: tuple[int, ...], removed: int | None = None):
    full = (1 << len(pred)) - 1
    used = 0 if removed is None else 1 << removed
    def rec(state, word):
        if state == full:
            yield word
        else:
            for v, p in enumerate(pred):
                if not(state >> v & 1) and not(p & ~state):
                    yield from rec(state | (1 << v), word + (v,))
    yield from rec(used, ())


def restricted_count(pred: tuple[int, ...], subset: set[int]) -> int:
    mask = sum(1 << x for x in subset)
    @lru_cache(None)
    def count(rem):
        if not rem: return 1
        return sum(count(rem ^ (1 << x)) for x in subset
                   if rem >> x & 1 and not(pred[x] & rem))
    return count(mask)


def run():
    stats = Counter()
    for n in range(1, 6):
        for pred in posets(n):
            stats['naturally_labelled_posets_n1_to_5'] += 1
            for x in range(n):
                D={i for i in range(n) if pred[x] >> i & 1}
                U={i for i in range(n) if pred[i] >> x & 1}
                I=set(range(n)) - D - U - {x}
                K=len(I)
                counts=Counter()
                for word in extensions(pred,x):
                    loc={v:i for i,v in enumerate(word)}
                    lo=max([loc[v] for v in D],default=-1)
                    hi=min([loc[v] for v in U],default=n-1)
                    counts[hi-lo] += 1
                stats['marked_prototypes'] += 1
                assert max(counts)==K+1
                emax=restricted_count(pred,D)*restricted_count(pred,I)*restricted_count(pred,U)
                assert counts[K+1]==emax
                stats['max_window_factorizations'] += 1
                a=[sum(c*comb(r+l-1,l-1) for l,c in counts.items()) for r in range(11)]
                assert all(a[r+1]**2 >= a[r]*a[r+2] for r in range(9))
                stats['log_concavity_checks'] += 9
                for r in range(1,9):
                    weights={l:c*comb(r+l-1,l-1) for l,c in counts.items()}
                    q=r+1
                    mu=sum(F(w*(r+l),a[r]) for l,w in weights.items())
                    second=sum(F(w*(r+l)**2,a[r]) for l,w in weights.items())
                    var=second-mu*mu
                    deficit=mu*(mu-q)/q-var
                    assert mu==q*F(a[r+1],a[r])
                    target=q*(q+1)*F(a[r+1]**2-a[r]*a[r+2],a[r]**2)
                    assert deficit==target
                    if K: assert deficit>0
                    else: assert deficit==0
                    eps=1-F(weights[K+1],a[r])
                    bound=F((sum(counts.values())-emax)*K,emax*(r+K)) if K else F(0)
                    assert 0 <= eps <= bound
                    stats['block_defect_identities'] += 1
                    stats['external_law_TV_bounds'] += 1
    pred=(0,1,0)
    single=[]
    for word in extensions(pred):
        loc={v:i+1 for i,v in enumerate(word)}
        single.append(loc[1])
    assert F(sum(single),len(single))==F(8,3)
    stats['single_copy_counterexample']={'extensions':3,'single_copy_mean':'8/3','whole_block_mean':4}
    stats['gaussian_endpoint_counterexample']={
        'family':'C_r disjoint union singleton', 'q':'r+1',
        'Z':'q+1 (constant)','theta':'1+1/q', 'D':'1+1/q',
        'D_over_q':'1/q+1/q^2 -> 0', 'standardized_law':'point mass 0, not N(0,1)'}
    stats['scope']='Exact arithmetic on naturally labelled posets n<=5; does not prove the general statements.'
    return dict(stats)

if __name__=='__main__':
    result=run()
    out=Path(__file__).resolve().parent.parent/'evidence'/'checks.json'
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(result,ensure_ascii=False,indent=2))
