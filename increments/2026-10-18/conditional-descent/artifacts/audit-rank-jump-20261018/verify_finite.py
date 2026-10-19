#!/usr/bin/env python3
"""Independent exact controls for the rank-jump audit; no producer imports."""
from collections import Counter, defaultdict
from fractions import Fraction as F
from itertools import combinations
from math import comb
from pathlib import Path
import json


def C(n, k):
    return comb(n, k) if n >= 0 and 0 <= k <= n else 0


def mass(m, K, r, j):
    return F(C(j+r-1, r-1)*C(m-j+K-r, K-r), C(m+K, K))


def extensions(labels, edges):
    pred = {x: set() for x in labels}
    for a, b in edges:
        pred[b].add(a)
    def visit(prefix, used):
        if len(prefix) == len(labels):
            yield tuple(prefix)
            return
        for x in labels:
            if x not in used and pred[x] <= used:
                yield from visit(prefix+[x], used|{x})
    return list(visit([], set()))


summary = {}
# Count the actual uniform-subset model, independently of its binomial formula.
subset_cases = subset_rank_laws = subset_atoms = 0
for m in range(2, 7):
    for K in range(1, 6):
        N = m+K
        cnt = [Counter() for _ in range(K)]
        total = 0
        for selected in combinations(range(1, N+1), K):
            total += 1
            for rr, x in enumerate(selected, 1):
                cnt[rr-1][x-rr] += 1
        for r in range(1, K+1):
            for j in range(m+1):
                assert F(cnt[r-1][j], total) == mass(m, K, r, j)
                subset_atoms += 1
            subset_rank_laws += 1
        subset_cases += 1
summary['uniform_subset_model'] = dict(parameter_cases=subset_cases,
    rank_laws=subset_rank_laws, atoms=subset_atoms)

# Small exact algebra grid, including all boundary ranks.
atoms = interior_atoms = 0
for m in range(2, 17):
    for K in range(1, 17):
        N = m+K
        for r in range(1, K+1):
            ps = [mass(m,K,r,j) for j in range(m+1)]
            assert sum(ps) == 1
            for j, p in enumerate(ps):
                assert p <= F(K,N)
                assert (p == F(K,N)) == (K == 1 or (r,j) in ((1,0),(K,m)))
                atoms += 1
                if m >= K and 1 <= j < m:
                    assert p <= F(K*m, N*(N-1)) <= F(1,3)
                    interior_atoms += 1
            if m >= K:
                assert mass(m,K,1,1) == F(K*m,N*(N-1))
summary['coefficient_grid'] = dict(atoms=atoms, interior_atoms_m_ge_K=interior_atoms,
    all_assertions_passed=True)

# Actual autonomous-chain fibers, with nontrivial outside-window occurrences.
fibers = outside_y_fibers = rank_jump_checks = mixed_density_checks = covariance_checks = 0
case_records = []
for m in range(2,5):
    chain = tuple(f'c{i}' for i in range(1,m+1))
    for model in range(3):
        if model < 2:
            outside = ('d','u','y','z'); D=('d',); U=('u',); I=('y','z')
            e = [('d',chain[0]), (chain[-1],'u'), ('d','u')]
            if model == 1:
                e += [('d','z'), ('y','u')]
        else:
            outside = ('u','y','z'); D=(); U=('u',); I=('y','z')
            e = [(chain[-1],'u'), ('y','u')]
        e += list(zip(chain,chain[1:]))
        labels = chain+outside
        extP = extensions(labels,e)
        grouped=defaultdict(list)
        def context(S):
            pos={x:i for i,x in enumerate(S)}
            lo=max((pos[x] for x in D),default=-1)
            hi=min((pos[x] for x in U),default=len(S))
            window=tuple(x for x in S[lo+1:hi] if x in I)
            return pos,lo,hi,window
        for L in extP:
            S=tuple(x for x in L if x not in chain)
            grouped[S].append(L)
        for S, LL in grouped.items():
            pos,lo,hi,window=context(S); K=len(window)
            assert len(LL)==C(m+K,K)
            fibers += 1
            for y in I:
                count=Counter(sum(L.index(c)<L.index(y) for c in chain) for L in LL)
                if y not in window:
                    outside_y_fibers += 1
                    expected=0 if pos[y]<lo else m
                    assert count == Counter({expected:len(LL)})
                else:
                    r=window.index(y)+1
                    for j in range(m+1):
                        assert F(count[j],len(LL))==mass(m,K,r,j)
                for j in range(1,m):
                    p=F(count[j],len(LL))
                    assert p<=F(K,m+K) if K else p==0
                    assert p<=F(1,3)  # Here m>=t=2.
                    rank_jump_checks += 1

        # Enumerate actual mixed deletions, reindexing the survivor chain.
        deleted=Counter()
        survivor=chain[:-1]
        for L in extP:
            for removed in chain:
                keep=[c for c in chain if c!=removed]
                rename=dict(zip(keep,survivor))
                deleted[tuple(rename.get(x,x) for x in L if x!=removed)]+=1
        qedges=[]
        for a,b in e:
            # Rebuild the same external relations and shortened module.
            if a not in chain and b not in chain:
                qedges.append((a,b))
        qedges+=list(zip(survivor,survivor[1:]))
        qedges += [(d,survivor[0]) for d in D]
        qedges += [(survivor[-1],u) for u in U]
        extQ=extensions(survivor+outside,qedges)
        assert set(extQ)==set(deleted)
        kval={}
        for L in extQ:
            S=tuple(x for x in L if x not in survivor)
            kval[L]=len(context(S)[3])
            assert deleted[L]==m+kval[L]
            mixed_density_checks += 1
        EK=F(sum(kval.values()),len(extQ))
        assert m*len(extP)==len(extQ)*(m+EK)
        for y in I:
            aa=[F(sum(L.index(c)<L.index(y) for L in extP),len(extP)) for c in chain]
            for r in range(1,m):
                qq=F(sum(L.index(survivor[r-1])<L.index(y) for L in extQ),len(extQ))
                eik=F(sum(kval[L] for L in extQ if L.index(survivor[r-1])<L.index(y)),len(extQ))
                covariance=eik-qq*EK
                mix=F(m-r,m)*aa[r-1]+F(r,m)*aa[r]
                direct=F(sum(n for L,n in deleted.items() if L.index(survivor[r-1])<L.index(y)),m*len(extP))
                assert mix==direct==qq+covariance/(m+EK)
                covariance_checks += 1
        case_records.append(dict(m=m,model=model,eP=len(extP),eQ=len(extQ),external_fibers=len(grouped)))
summary['actual_poset_controls']=dict(cases=case_records,external_fibers=fibers,
    outside_window_point_fibers=outside_y_fibers,internal_jump_checks=rank_jump_checks,
    mixed_density_extensions=mixed_density_checks,covariance_identities=covariance_checks)

# Exact boundary control: interior jump may exceed 1/3 without m>=t.
assert mass(2,3,2,1)==F(2,5)>F(1,3)
summary['boundary_control']={'m':2,'K':3,'r':2,'j':1,'mass':'2/5',
    'interpretation':'C2 disjoint C3; middle external label; not an original-conjecture counterexample'}
summary['status']='PASS'
out=Path(__file__).with_name('verification.json')
out.write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(summary,ensure_ascii=False,indent=2))
