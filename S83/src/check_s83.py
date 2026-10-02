#!/usr/bin/env python3
"""Exact S83 checks; standard library only; finite checks do not prove the general conjecture.
Run: python S83/src/check_s83.py --output S83/evidence/check_s83.json
"""
from __future__ import annotations
import argparse
import itertools
import json
from fractions import Fraction
from functools import lru_cache
from pathlib import Path

SEEDS = ((0,0,0,1,4,7,29,93), (0,0,0,5,5,15,29,31))

def validate(pred: tuple[int, ...]) -> None:
    for j, mask in enumerate(pred):
        if not 0 <= mask < 1 << j:
            raise ValueError('Expected naturally labelled strict predecessor masks')
        if any(mask >> i & 1 and pred[i] & mask != pred[i] for i in range(j)):
            raise ValueError('Input must include transitive closure')

def dp(pred: tuple[int, ...]):
    validate(pred)
    n = len(pred)
    @lru_cache(None)
    def count(S: int) -> int:
        if not S: return 1
        return sum(count(S ^ (1 << i)) for i in range(n)
                   if S >> i & 1 and not pred[i] & S)
    @lru_cache(None)
    def before(S: int, x: int, y: int) -> int:
        # Called while both marks remain; stop at the first removed mark.
        if not S >> x & 1: return count(S)
        if not S >> y & 1: return 0
        return sum(before(S ^ (1 << i), x, y) for i in range(n)
                   if S >> i & 1 and not pred[i] & S)
    return count, before

def brute(pred: tuple[int, ...]) -> tuple[int, list[list[int]]]:
    """Independent rejection of every permutation, without subset recurrence."""
    n = len(pred)
    edges = [(i,j) for j in range(n) for i in range(j) if pred[j] >> i & 1]
    E = 0
    matrix = [[0]*n for _ in range(n)]
    for perm in itertools.permutations(range(n)):
        rank = [0]*n
        for k,x in enumerate(perm): rank[x] = k
        if any(rank[i] >= rank[j] for i,j in edges): continue
        E += 1
        for i in range(n):
            for j in range(n): matrix[i][j] += int(rank[i] < rank[j])
    return E, matrix

def gate(pred: tuple[int, ...], t: int) -> tuple[int, ...]:
    """Old marks 0,1 shift to t,t+1. New gates precede all other old vertices."""
    if t < 0 or len(pred) < 2 or pred[0] or pred[1]:
        raise ValueError('Requires t>=0 and marked minima 0,1')
    mask = (1 << t)-1
    out = tuple((1 << i)-1 for i in range(t))
    out += tuple((p << t) | (mask if i >= 2 else 0) for i,p in enumerate(pred))
    validate(out)
    return out

def width(pred: tuple[int, ...]) -> int:
    return max(S.bit_count() for S in range(1 << len(pred))
               if all(not S >> j & 1 or not pred[j] & S for j in range(len(pred))))

def covers(pred: tuple[int, ...]) -> list[list[int]]:
    return [[i,j] for j in range(len(pred)) for i in range(j)
            if pred[j] >> i & 1 and not any(pred[j] >> k & 1 and pred[k] >> i & 1
                                            for k in range(i+1,j))]

def signature(pred: tuple[int, ...], marks: tuple[int, ...]) -> list[int]:
    count,_ = dp(pred)
    full = (1 << len(pred))-1
    return [count(full ^ sum(1 << v for k,v in enumerate(marks) if S >> k & 1))
            for S in range(1 << len(marks))]

def audit(pred: tuple[int, ...], x: int, y: int) -> dict:
    count,before = dp(pred)
    n = len(pred)
    full = (1 << n)-1
    E,matrix = brute(pred)
    assert E == count(full)
    assert all(matrix[i][j] == before(full,i,j) for i in range(n)
               for j in range(n) if i != j)
    bal,a,b = max((min(matrix[i][j], E-matrix[i][j]),i,j)
                 for i in range(n) for j in range(i+1,n))
    U = matrix[x][y]
    return {'predecessor_masks':list(pred), 'covers':covers(pred), 'width':width(pred),
            'linear_extensions':E, 'marked_pair':[x,y], 'forward_count':U,
            'backward_count':E-U, 'marked_probability':str(Fraction(U,E)),
            'marked_balance':str(Fraction(min(U,E-U),E)),
            'marked_balanced':3*min(U,E-U)>=E,
            'global_balance':str(Fraction(bal,E)), 'global_witness':[a,b]}

def run() -> dict:
    seeds = [audit(p,0,1) for p in SEEDS]
    outputs = [audit(gate(p,1),1,2) for p in SEEDS]
    assert [r['linear_extensions'] for r in seeds] == [144,144]
    assert [r['forward_count'] for r in seeds] == [98,102]
    assert [r['forward_count'] for r in outputs] == [170,174]
    assert [r['marked_balanced'] for r in outputs] == [True,False]
    sigs = [signature(gate(p,1),(1,2,0)) for p in SEEDS]
    assert sigs[0] == sigs[1] == [258,72,42,14,144,58,28,14]
    for case,sig in zip(outputs,sigs): case['minimal_boolean_signature_xyg'] = sig
    transition_checks = 0
    for pred in SEEDS:
        count,before = dp(pred)
        full = (1 << len(pred))-1
        E,A,B,D = [count(full ^ s) for s in (0,1,2,3)]
        U = before(full,0,1)
        assert (E,A,B,D) == (144,58,28,14)
        for t in range(13):
            q = gate(pred,t)
            c,b = dp(q)
            f = (1 << len(q))-1
            actual = (c(f),c(f^(1<<t)),c(f^(1<<(t+1))),
                      c(f^(1<<t)^(1<<(t+1))),b(f,t,t+1))
            expected = (E+t*(A+B)+t*(t+1)*D,A+t*D,B+t*D,D,
                        U+t*A+t*(t+1)*D//2)
            assert actual == expected
            transition_checks += 1
    diamond_checks = 0
    for pred in [gate(p,1) for p in SEEDS]:
        c,_ = dp(pred)
        n = len(pred)
        full = (1 << n)-1
        for I in range(1 << n):
            if any(I >> j & 1 and pred[j]&I != pred[j] for j in range(n)): continue
            R = full ^ I
            m = R.bit_count()
            mins = [i for i in range(n) if R >> i & 1 and not pred[i]&R]
            for x,y in itertools.combinations(mins,2):
                num = c(R)*c(R^(1<<x)^(1<<y))
                den = c(R^(1<<x))*c(R^(1<<y))
                assert (m-1)*num >= m*den and num <= 2*den
                diamond_checks += 1
    nonmono_seed = (0,0,0,1,6,23)
    nonmono = [audit(nonmono_seed,0,1),audit(gate(nonmono_seed,1),1,2)]
    assert [r['marked_balance'] for r in nonmono] == ['1/2','27/55']
    return {'round':'S83', 'status':'exact checks passed',
            'scope':'Analytic transition is proved separately. No general conjecture certified.',
            'seeds':seeds, 'nine_point_collision':outputs,
            'gate_family_checks_t_0_to_12':transition_checks,
            'local_diamonds_at_all_ideals':diamond_checks,
            'independent_full_permutation_cases':6,
            'fixed_pair_nonmonotonicity':nonmono, 'search_minimality_claim':False}

def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path)
    args = parser.parse_args()
    text = json.dumps(run(),ensure_ascii=False,indent=2)
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(text+'\n',encoding='utf-8')
    print(text)

if __name__ == '__main__': main()
