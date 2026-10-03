#!/usr/bin/env python3
"""Exact checks for S84. Standard library only; proofs are in ../notes/PROOF.md.

A poset is a tuple of transitively closed strict-predecessor bitmasks on
0,...,n-1. Independent permutation filtering is used for the displayed seeds.
Run: python check_s84.py --output ../evidence/check_s84.json
"""
from __future__ import annotations
import argparse
import json
import random
from fractions import Fraction
from functools import lru_cache
from itertools import combinations, permutations, product
from math import comb, factorial
from pathlib import Path
from typing import Iterable

Poset = tuple[int, ...]
CORE: Poset = (0, 1, 0, 3, 15, 3, 31)
LEFT: Poset = (0, 0, 1, 1, 11, 27, 3, 59)
RIGHT: Poset = (0, 0, 1, 5, 3, 7, 47, 39)
LOSS: Poset = (0, 0, 1, 5, 15, 2, 5, 39)


def validate(p: Poset) -> None:
    for j, mask in enumerate(p):
        assert mask >= 0 and mask < (1 << j), (p, j, 'not natural')
        for i in range(j):
            if mask >> i & 1:
                assert p[i] & ~mask == 0, (p, j, 'not transitive')


def is_ideal(p: Poset, mask: int) -> bool:
    return all(not (mask >> j & 1) or not (q & ~mask)
               for j, q in enumerate(p))


def ideals(p: Poset) -> list[int]:
    return [m for m in range(1 << len(p)) if is_ideal(p, m)]


def count(p: Poset, removed: int = 0, pair: tuple[int, int] | None = None) -> int:
    """Subset DP. Adding the edge x<y counts that fixed event exactly."""
    pp = list(p)
    if pair is not None:
        x, y = pair
        assert x != y and not (removed >> x & 1 or removed >> y & 1)
        pp[y] |= 1 << x
    full = (1 << len(p)) - 1
    @lru_cache(None)
    def go(mask: int) -> int:
        if mask == full:
            return 1
        return sum(go(mask | (1 << j)) for j, q in enumerate(pp)
                   if not (mask >> j & 1) and not (q & ~mask))
    return go(removed)


def extensions(p: Poset) -> list[tuple[int, ...]]:
    full = (1 << len(p)) - 1
    def go(mask: int, seq: tuple[int, ...]):
        if mask == full:
            yield seq
        else:
            for j, q in enumerate(p):
                if not (mask >> j & 1) and not (q & ~mask):
                    yield from go(mask | (1 << j), seq + (j,))
    return list(go(0, ()))


def permutation_extensions(p: Poset) -> list[tuple[int, ...]]:
    """No DP / no ideal enumeration: check all n! permutations against edges."""
    edges = [(i, j) for j, mask in enumerate(p)
             for i in range(j) if mask >> i & 1]
    out = []
    for seq in permutations(range(len(p))):
        pos = [0] * len(p)
        for rank, label in enumerate(seq):
            pos[label] = rank
        if all(pos[i] < pos[j] for i, j in edges):
            out.append(seq)
    return out


def width(p: Poset, mask: int | None = None) -> int:
    if mask is None:
        mask = (1 << len(p)) - 1
    best = 0
    s = mask
    while True:
        if s.bit_count() > best and all(not (s >> j & 1) or not (q & s)
                                       for j, q in enumerate(p)):
            best = s.bit_count()
        if s == 0:
            return best
        s = (s - 1) & mask


def profiles(exs: Iterable[tuple[int, ...]], Is: tuple[int, ...],
             pair: tuple[int, int]) -> tuple[dict, dict]:
    c, u = {}, {}
    x, y = pair
    for ex in exs:
        k = tuple(next((i for i, z in enumerate(ex) if not (I >> z & 1)), len(ex))
                  for I in Is)
        c[k] = c.get(k, 0) + 1
        u[k] = u.get(k, 0) + (ex.index(x) < ex.index(y))
    return c, u


def orthants(c: dict, u: dict, ds: tuple[int, ...]) -> list[dict]:
    out = []
    for h in product(*(range(d + 1) for d in ds)):
        keys = [k for k in c if all(ki >= hi for ki, hi in zip(k, h))]
        e, a = sum(c[k] for k in keys), sum(u[k] for k in keys)
        out.append({'threshold': list(h), 'total': e, 'forward': a,
                    'probability': str(Fraction(a, e)) if e else None,
                    'lower_1_3_slack': 3*a-e, 'upper_5_9_slack': 5*e-9*a})
    return out


def attach(q: Poset, g: Poset, types: tuple[int, ...], Is: tuple[int, ...]) -> Poset:
    assert len(g) == len(types)
    assert all(is_ideal(q, I) for I in Is)
    n, m = len(q), len(g)
    full = (1 << n) - 1
    Fs = tuple(full ^ I for I in Is)
    for b, pred in enumerate(g):
        for a in range(b):
            if pred >> a & 1:
                assert Fs[types[b]] & ~Fs[types[a]] == 0, 'incompatible types'
    out = list(g)
    for v, pred in enumerate(q):
        before = sum(1 << j for j, ty in enumerate(types) if Fs[ty] >> v & 1)
        out.append((pred << m) | before)
    result = tuple(out)
    validate(result)
    return result


def chain(n: int) -> Poset:
    return tuple((1 << j)-1 for j in range(n))


def tails(a: list[int], t: int) -> list[int]:
    return [sum(a[k]*comb(t+k, k) for k in range(h, len(a)))
            for h in range(len(a))]


def cutoff(a: list[int]) -> int | None:
    support = [j for j, v in enumerate(a) if v]
    if not support:
        return 0
    j = max(support)
    if a[j] < 0:
        return None
    negative = sum(-v for v in a[:j] if v < 0)
    numerator = j*(negative-a[j])
    return max(0, -((-numerator)//a[j]))


def one_profile(p: Poset, I: int, xy: tuple[int,int], exs=None):
    if exs is None:
        exs = extensions(p)
    c0, u0 = profiles(exs, (I,), xy)
    d = I.bit_count()
    return ([c0.get((k,), 0) for k in range(d+1)],
            [u0.get((k,), 0) for k in range(d+1)])


def random_poset(n: int, rng: random.Random) -> Poset:
    pp = []
    for j in range(n):
        mask = 0
        for i in range(j):
            if rng.random() < .32:
                mask |= (1 << i) | pp[i]
        pp.append(mask)
    return tuple(pp)


def natural_posets(n: int) -> list[Poset]:
    out = [()]
    for _ in range(n):
        out = [p+(I,) for p in out for I in ideals(p)]
    return out


def main() -> dict:
    for p in (CORE, LEFT, RIGHT, LOSS):
        validate(p)
    report = {'round': 'S84', 'date': '2026-10-03', 'status': 'all exact checks passed',
              'proof_boundary': 'Finite checks audit identities and displayed examples; general theorems are proved separately.'}
    # The core certificate is independently generated by all 7! permutations.
    ex = permutation_extensions(CORE)
    assert ex == sorted(extensions(CORE)) and len(ex) == count(CORE) == 18
    c, u = profiles(ex, (7,15), (1,2))
    grid = orthants(c,u,(3,4))
    assert all(row['lower_1_3_slack'] >= 0 and row['upper_5_9_slack'] >= 0 for row in grid)
    assert width(CORE)==3 and width(CORE,7)==width(CORE,15)==2
    report['universal_core'] = {
        'predecessor_masks': list(CORE), 'pair': [1,2], 'ideal_masks': [7,15],
        'width':3, 'total':18, 'forward':10,
        'joint_profile':[{'k':list(k),'total':c[k],'forward':u[k]} for k in sorted(c)],
        'orthant_certificate':grid}
    # Every chain size pair here is an audit, not the proof of all sizes.
    chain_cases=[]
    for s,t in product(range(9), repeat=2):
        g=chain(s+t)
        pq=attach(CORE,g,(0,)*s+(1,)*t,(7,15))
        e=count(pq); a=count(pq,pair=(1+s+t,2+s+t))
        assert 3*a>=e and 9*a<=5*e
        if s+t<=2:
            assert width(pq)==3
        chain_cases.append({'s':s,'t':t,'total':e,'forward':a})
    report['two_parameter_chain_checks']={'cases':len(chain_cases),'range':'0 <= s,t <= 8', 'rows':chain_cases}
    rng=random.Random(841034)
    attachment_cases=0
    for m in range(1,7):
        for _ in range(20):
            g=random_poset(m,rng);split=rng.randrange(m+1)
            ty=(0,)*split+(1,)*(m-split)
            pq=attach(CORE,g,ty,(7,15))
            e=count(pq);a=count(pq,pair=(1+m,2+m))
            assert 3*a>=e and 9*a<=5*e
            attachment_cases+=1
    report['arbitrary_attachment_checks']={'cases':attachment_cases,'new_sizes':'1..6','random_seed':841034}
    # Two identical five-coordinate seeds; all-length formulas verified directly.
    family=[];permutation_cases=1
    for name,q,expectc,expectu in [('left',LEFT,[0,24,54,15],[0,24,29,10]),
                                 ('right',RIGHT,[0,0,18,75],[0,0,13,50])]:
        independent=permutation_extensions(q);permutation_cases+=1
        assert independent==sorted(extensions(q))
        c,u=one_profile(q,7,(0,1),independent)
        assert (c,u)==(expectc,expectu)
        sig=[count(q),count(q,1),count(q,2),count(q,3),count(q,pair=(0,1))]
        assert sig==[93,63,30,30,63]
        lower=[3*v-w for w,v in zip(c,u)];upper=[2*w-3*v for w,v in zip(c,u)]
        rows=[]
        for t in range(21):
            pq=attach(q,chain(t),(0,)*t,(7,))
            e=count(pq);a=count(pq,pair=(t,t+1))
            assert e==sum(v*comb(t+k,k) for k,v in enumerate(c))
            assert a==sum(v*comb(t+k,k) for k,v in enumerate(u))
            if name=='left':
                assert 2*e==(t+1)*(5*t*t+79*t+186)
                assert 6*a==(t+1)*(10*t*t+137*t+378)
                if t>=1:assert e<=3*a<=2*e
            else:
                assert 2*e==(t+1)*(t+2)*(25*t+93)
                assert 6*a==(t+1)*(t+2)*(50*t+189)
                assert 3*a>2*e
            for residual in(lower,upper):
                old,new=tails(residual,t),tails(residual,t+1)
                for h in range(len(residual)):
                    assert (t+1)*new[h]==(t+h+1)*old[h]+sum(old[h+1:])
            if t==1:
                raw=permutation_extensions(pq);permutation_cases+=1
                assert len(raw)==e and sum(z.index(t)<z.index(t+1) for z in raw)==a
            if t<=2:assert width(pq)==(width(q) if t==0 else max(width(q),width(q,7)+1))
            rows.append({'t':t,'total':e,'forward':a,'probability':str(Fraction(a,e))})
        family.append({'name':name,'predecessor_masks':list(q),'five_counts':sig,
                       'c':c,'u':u,'lower_residual':lower,'upper_residual':upper,
                       'cutoff_lower':cutoff(lower),'cutoff_upper':cutoff(upper),
                       'rows':rows})
    report['five_coordinate_collision']=family
    # Strict loss of a pre-existing balanced fixed pair.
    c,u=one_profile(LOSS,15,(0,1))
    assert (c,u)==([0,12,33,57,48],[0,0,21,39,36])
    loss_rows=[]
    for t in (0,1):
        pq=attach(LOSS,chain(t),(0,)*t,(15,));e=count(pq);a=count(pq,pair=(t,t+1))
        loss_rows.append({'t':t,'total':e,'forward':a,'probability':str(Fraction(a,e))})
    assert loss_rows[0]['probability']=='16/25' and loss_rows[1]['probability']=='133/197'
    report['unconditional_preservation_counterexample']={'predecessor_masks':list(LOSS),'I':15,'pair':[0,1], 'c':c,'u':u,'rows':loss_rows}
    # Systematic audit of the general one-filter formula at n<=5, not a conjecture search.
    np=profiles_checked=direct_checks=recurrences=cutoff_checks=0
    for n in range(1,6):
        for q in natural_posets(n):
            validate(q);np+=1
            ex=extensions(q)
            for I in ideals(q):
                if I==0 or I==(1<<n)-1:continue
                labels=[j for j in range(n) if I>>j&1]
                for x,y in combinations(labels,2):
                    if q[y]>>x&1:continue
                    c,u=one_profile(q,I,(x,y),ex);profiles_checked+=1
                    for t in range(4):
                        pq=attach(q,chain(t),(0,)*t,(I,))
                        assert count(pq)==sum(v*comb(t+k,k) for k,v in enumerate(c))
                        assert count(pq,pair=(t+x,t+y))==sum(v*comb(t+k,k) for k,v in enumerate(u))
                        direct_checks+=1
                        for a in ([3*v-w for w,v in zip(c,u)],[2*w-3*v for w,v in zip(c,u)]):
                            old,new=tails(a,t),tails(a,t+1)
                            for h in range(len(a)):
                                assert (t+1)*new[h]==(t+h+1)*old[h]+sum(old[h+1:]);recurrences+=1
                    for a in ([3*v-w for w,v in zip(c,u)],[2*w-3*v for w,v in zip(c,u)]):
                        T=cutoff(a)
                        if T is not None:
                            assert min(tails(a,T))>=0 and min(tails(a,T+1))>=0
                            cutoff_checks+=1
    assert np==407
    report['systematic_audit']={'natural_labelled_posets_n_1_to_5':np,'marked_ideal_profiles':profiles_checked,
                              'direct_expanded_poset_checks':direct_checks,'tail_recurrence_identities':recurrences,
                              'eventual_cutoff_checks':cutoff_checks}
    report['independent_full_permutation_cases']=permutation_cases
    report['search_minimality_claim']=False
    return report

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,default=Path(__file__).resolve().parents[1]/'evidence'/'check_s84.json')
    args=parser.parse_args()
    result=main()
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k in ('round','status','systematic_audit','independent_full_permutation_cases')},ensure_ascii=False,indent=2))
