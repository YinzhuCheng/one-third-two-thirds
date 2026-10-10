#!/usr/bin/env python3
"""Exact finite checks of structural identities, not a proof of the conjecture."""
from itertools import combinations, permutations
from collections import Counter
from fractions import Fraction
from math import comb
import json
from pathlib import Path


def posets(n):
    edges=list(combinations(range(n),2)); seen=set()
    for bits in range(1<<len(edges)):
        rows=[0]*n
        for z,(i,j) in enumerate(edges):
            if bits>>z&1: rows[i]|=1<<j
        for i in reversed(range(n)):
            for j in range(i+1,n):
                if rows[i]>>j&1: rows[i]|=rows[j]
        r=tuple(rows)
        if r not in seen: seen.add(r); yield r


def rel(rows,x,y):
    return -1 if rows[x]>>y&1 else (1 if rows[y]>>x&1 else 0)


def extensions(rows,vertices=None):
    vs=tuple(range(len(rows))) if vertices is None else tuple(vertices)
    return [p for p in permutations(vs) if all(not (rows[p[j]]>>p[i]&1) for i in range(len(p)) for j in range(i+1,len(p)))]


def module(rows,M):
    return all(len({rel(rows,x,y) for y in M})==1 for x in range(len(rows)) if x not in M)


def chain(rows,M):
    return all(rel(rows,x,y) for x,y in combinations(M,2))


def quotient(rows,blocks):
    return tuple(sum(1<<j for j,N in enumerate(blocks) if rel(rows,next(iter(M)),next(iter(N)))==-1) for M in blocks)


def check_all(max_n=5):
    report={'max_n':max_n,'naturally_labeled_posets':0,'module_laws':0,'chain_module_fiber_laws':0,'weighted_prime_decompositions':0}
    for n in range(1,max_n+1):
        for rows in posets(n):
            report['naturally_labeled_posets']+=1
            le=extensions(rows)
            mods=[frozenset(M) for r in range(1,n+1) for M in combinations(range(n),r) if module(rows,M)]
            for M in mods:
                counts=Counter(tuple(x for x in p if x in M) for p in le)
                assert len(counts)==len(extensions(rows,sorted(M))) and len(set(counts.values()))==1
                report['module_laws']+=1
                if len(M)<=1 or not chain(rows,M): continue
                ordered=sorted(M); k=len(M); R=set(range(n))-M
                low={x for x in R if rel(rows,x,ordered[0])==-1}
                high={x for x in R if rel(rows,x,ordered[0])==1}
                outside=extensions(rows,sorted(R))
                e_formula=0
                for sigma in outside:
                    a=max([sigma.index(x) for x in low],default=-1)
                    b=min([sigma.index(x) for x in high],default=len(sigma))
                    d=b-a-1
                    e_formula+=comb(d+k,k)
                    for j,mj in enumerate(ordered,1):
                        reduced=Counter(tuple(x for x in p if x in R or x==mj) for p in le)
                        for t in range(d+1):
                            eta=sigma[:a+1+t]+(mj,)+sigma[a+1+t:]
                            F=comb(t+j-1,j-1)*comb(d-t+k-j,k-j)
                            assert reduced[eta]==F,(rows,M,j,sigma,t,reduced[eta],F)
                assert e_formula==len(le)
                report['chain_module_fiber_laws']+=1
            if n>1 and not chain(rows,range(n)) and all(len(M)==n or chain(rows,M) for M in mods):
                cm=[M for M in mods if chain(rows,M)]
                maximal=[M for M in cm if not any(M<N for N in cm)]
                assert len(set.union(*(set(M) for M in maximal)))==n
                assert sum(map(len,maximal))==n
                q=quotient(rows,maximal); qn=len(q)
                assert not any(module(q,M) for r in range(2,qn) for M in combinations(range(qn),r))
                weights=[len(M) for M in maximal]
                lookup={x:i for i,M in enumerate(maximal) for x in M}
                words=[tuple(lookup[x] for x in p) for p in le]
                assert len(set(words))==len(le)
                def dp(a):
                    if list(a)==weights:return 1
                    s=0
                    for i in range(qn):
                        if a[i]<weights[i] and all(a[j]==weights[j] for j in range(qn) if q[j]>>i&1):
                            b=list(a); b[i]+=1; s+=dp(tuple(b))
                    return s
                assert dp((0,)*qn)==len(le)
                report['weighted_prime_decompositions']+=1
    return report


def before(le,x,y):return Fraction(sum(p.index(x)<p.index(y) for p in le),len(le))


def examples():
    # P: 0<1<2 and isolated 3; contract {1,2}, keeping vertex 1.
    p=(6,4,0,0); lp=extensions(p); lq=extensions(p,(0,1,3))
    # P: chain {0,1} parallel to chain {2,3,4}; y=3.
    p2=(2,0,24,16,0); lp2=extensions(p2); lq2=extensions(p2,(0,2,3,4))
    out={'external_pair':{'P_e':len(lp),'Q_e':len(lq),'P_p':str(before(lp,0,3)),'Q_p':str(before(lq,0,3))},
         'averaged_lift':{'P_e':len(lp2),'Q_e':len(lq2),'P_first':str(before(lp2,0,3)),'P_second':str(before(lp2,1,3)),'Q_p':str(before(lq2,0,3))}}
    assert out['external_pair']['P_p']=='3/4' and out['external_pair']['Q_p']=='2/3'
    assert out['averaged_lift']['P_first']=='7/10' and out['averaged_lift']['P_second']=='3/10' and out['averaged_lift']['Q_p']=='1/2'
    return out

if __name__=='__main__':
    result=check_all(); result['examples']=examples(); result['status']='PASS'
    path=Path(__file__).with_name('check_results.json'); path.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
