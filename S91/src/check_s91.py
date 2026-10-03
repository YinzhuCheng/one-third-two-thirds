#!/usr/bin/env python3
"""Exact diagnostics for S91. Standard library only; not a general proof."""
from __future__ import annotations
from functools import lru_cache
from fractions import Fraction
from itertools import permutations
from math import comb
from pathlib import Path
import argparse
import json
import random


def closure(n: int, edges: list[tuple[int,int]]) -> tuple[int,...]:
    pred=[0]*n
    for a,b in edges:
        if a==b or not(0<=a<n and 0<=b<n): raise ValueError('bad edge')
        pred[b]|=1<<a
    for k in range(n):
        for v in range(n):
            if pred[v]>>k&1: pred[v]|=pred[k]
    if any(pred[i]>>i&1 for i in range(n)): raise ValueError('cycle')
    return tuple(pred)


def le_counts(pred: tuple[int,...], chain: tuple[int,...], forbidden: frozenset[tuple[int,int]]=frozenset()):
    n=len(pred); full=(1<<n)-1; cm=sum(1<<c for c in chain)
    @lru_cache(None)
    def tail(mask: int) -> int:
        if mask==full:return 1
        rank=(mask&cm).bit_count()
        return sum(tail(mask|(1<<v)) for v in range(n)
                   if not(mask>>v&1) and pred[v]&mask==pred[v]
                   and (v,rank) not in forbidden)
    E=tail(0)
    return E,tail


def rank_distributions(pred:tuple[int,...], C:tuple[int,...]):
    """Count J_v by the unique transition that inserts v, under full uniform LE."""
    n=len(pred); t=len(C); cm=sum(1<<c for c in C)
    E,tail=le_counts(pred,C)
    front={0:1}; totals=[[0]*(t+1) for _ in range(n)]
    for level in range(n):
        nxt={}
        for mask,f in front.items():
            k=(mask&cm).bit_count()
            for v in range(n):
                if mask>>v&1 or pred[v]&mask!=pred[v]:continue
                target=mask|(1<<v)
                totals[v][k]+=f*tail(target)
                nxt[target]=nxt.get(target,0)+f
        front=nxt
    assert list(front.values())==[E]
    assert all(sum(a)==E for a in totals)
    return E,totals


def relation_type(pred:tuple[int,...], C:tuple[int,...], v:int)->str:
    if all(pred[c]>>v&1 for c in C):return 'below'
    if all(pred[v]>>c&1 for c in C):return 'above'
    if all(not(pred[v]>>c&1 or pred[c]>>v&1) for c in C):return 'neutral'
    return 'splitter'


def enum_extensions(pred):
    n=len(pred)
    def rec(seq,mask):
        if len(seq)==n:
            yield tuple(seq);return
        for v in range(n):
            if not(mask>>v&1) and pred[v]&mask==pred[v]:
                yield from rec(seq+[v],mask|(1<<v))
    yield from rec([],0)


def brute_count(pred):
    n=len(pred); count=0
    for p in permutations(range(n)):
        mask=0
        for v in p:
            if pred[v]&mask!=pred[v]:break
            mask|=1<<v
        else:count+=1
    return count


def fibre_check(pred,C,x,S):
    """Partition at consecutive S-neighbours of x and verify induced middle law."""
    groups={};cm=set(C);S=set(S)
    for ext in enum_extensions(pred):
        at=ext.index(x)
        lo=max([-1]+[i for i in range(at) if ext[i] in S])
        hi=min([len(ext)]+[i for i in range(at+1,len(ext)) if ext[i] in S])
        key=(ext[:lo+1],ext[hi:])
        groups.setdefault(key,[]).append(ext[lo+1:hi])
    for (pre,suf),middles in groups.items():
        verts=tuple(sorted(middles[0])); local={v:i for i,v in enumerate(verts)}
        q=tuple(sum(1<<local[u] for u in verts if pred[v]>>u&1) for v in verts)
        locC=tuple(local[c] for c in C if c in local)
        assert le_counts(q,locC)[0]==len(middles)
        # This same finite fibre must be full, not an arbitrary conditional subset.
        assert len(set(middles))==len(middles)
        for v in verts:
            if v not in cm and locC:
                assert relation_type(q,locC,local[v])!='splitter'
    return len(groups)


def ballot_stats(t:int,L:int):
    """Independent 2-chain prefix/suffix DP for C_i<S_i, A_L<S_1.
    A singleton x is inserted before the unique maximum S_t afterwards.
    """
    n=L+2*t
    fw=[[0]*(L+t+1) for _ in range(t+1)];fw[0][0]=1
    for i in range(t+1):
        for j in range(L+t+1):
            if j>L+i:continue
            f=fw[i][j]
            if i<t:fw[i+1][j]+=f
            if j<L+t and j+1<=L+i:fw[i][j+1]+=f
    bw=[[0]*(L+t+1) for _ in range(t+1)];bw[t][L+t]=1
    for i in range(t,-1,-1):
        for j in range(L+t,-1,-1):
            if j>L+i or (i,j)==(t,L+t):continue
            bw[i][j]=(bw[i+1][j] if i<t else 0)+(bw[i][j+1] if j<L+t and j+1<=L+i else 0)
    E=fw[t][L+t]
    assert E==bw[0][0]==comb(n,t)-comb(n,t-1)
    p=[]
    for r in range(1,t+1):
        U=sum((r+j)*fw[r-1][j]*bw[r][j] for j in range(L+t+1) if j<=L+r-1)
        p.append(Fraction(U,n*E))
    eps=1-Fraction(comb(L+t,t),E)
    product=Fraction(1)
    for i in range(2,t+1): product*=Fraction(L+i,L+t+i)
    assert eps==1-product
    assert eps<=Fraction(t*(t-1),L+t+2)
    return {'t':t,'L':L,'base_extensions':E,'full_extensions':n*E,
            'p_x_before_C':[str(v) for v in p], 'p3':str(p[2]) if t>=3 else None,
            'epsilon_exact':str(eps),'epsilon_upper':str(Fraction(t*(t-1),L+t+2))},p,eps


def ladder_poset(t,L):
    # labels: C[0:t], A[t:t+L], S[t+L:t+L+t], x last
    C=tuple(range(t));A=tuple(range(t,t+L));S=tuple(range(t+L,L+2*t));x=L+2*t
    edges=list(zip(C,C[1:]))+list(zip(A,A[1:]))+list(zip(S,S[1:]))
    if A:edges.append((A[-1],S[0]))
    edges +=[(C[i],S[i]) for i in range(t)] +[(x,S[-1])]
    return closure(x+1,edges),C,S,x


def run():
    rng=random.Random(202610031119)
    out={'status':'passed','general_theorems_proved_in':'notes/PROOF.md','external_review':False}
    beta_checks=0
    for ell in range(6,27):
        for k in range(1,33):
            den=comb(ell+k,k)
            for j in range(1,k+1):
                for q in range(3,ell-2):
                    num=comb(q+j-1,j-1)*comb(ell-q+k-j,k-j)
                    assert 16*num<=5*den
                    beta_checks+=1
    out['central_beta_binomial_checks']=beta_checks

    accepted=0;attempts=0;ineqs=0;crossings=0;fibre_total=0;fibre_cases=0
    example_records=[]
    # Do not fix exceptional cut positions or replace their joint law by independent marginals.
    while accepted<90 and attempts<2000:
        attempts+=1;t=rng.randint(6,10);extra=rng.randint(2,5);n=t+extra
        C=tuple(range(t));ext=list(range(t,n))
        # Insert outside points in a random topological order, preserving chain order.
        order=list(C)
        for v in ext:order.insert(rng.randrange(len(order)+1),v)
        edges=list(zip(C,C[1:]))
        for i in range(n):
            for j in range(i+1,n):
                if (order[i] not in C or order[j] not in C) and rng.random()<0.10:
                    edges.append((order[i],order[j]))
        pred=closure(n,edges)
        S=tuple(v for v in ext if relation_type(pred,C,v)=='splitter')
        N=tuple(v for v in ext if relation_type(pred,C,v)=='neutral')
        if not N:continue
        E,atoms=rank_distributions(pred,C)
        eps_values=[]
        for r in range(3,t-2):
            forbidden=frozenset((s,k) for s in S for k in range(max(0,r-2),min(t,r+2)+1))
            good,_=le_counts(pred,C,forbidden);bad=E-good
            eps_values.append(Fraction(bad,E))
            for x in N:
                assert 16*atoms[x][r]<=5*E+11*bad
                ineqs+=1
                u=sum(atoms[x][:r]);v=u+atoms[x][r]
                if 2*u<=E<=2*v:
                    best=max(min(Fraction(u,E),1-Fraction(u,E)),min(Fraction(v,E),1-Fraction(v,E)))
                    assert best>=Fraction(11*(E-bad),32*E)
                    crossings+=1
        assert sum(eps_values)<=5*len(S)
        if n<=9 and fibre_cases<8 and E<=30000:
            fibre_total+=fibre_check(pred,C,N[0],S);fibre_cases+=1
        if accepted<3:
            example_records.append({'pred':pred,'C':C,'S':S,'neutral':N,'extensions':E,
                                    'epsilons':[str(e) for e in eps_values]})
        accepted+=1
    assert accepted==90
    out['arbitrary_chain_cases']=accepted
    out['actual_law_defect_inequalities']=ineqs
    out['actual_half_crossings']=crossings
    out['prefix_suffix_fibre_cases']=fibre_cases
    out['verified_full_middle_fibres']=fibre_total
    out['sample_cases']=example_records

    # Independent entire permutation filtering for a small non-autonomous example.
    small,CC,SS,xx=ladder_poset(3,2)
    E,ats=rank_distributions(small,CC)
    assert E==brute_count(small)
    row,ps,ep=ballot_stats(3,2)
    assert row['full_extensions']==E
    assert all(Fraction(sum(ats[xx][:r]),E)==ps[r-1] for r in range(1,4))
    out['independent_full_permutation_case']={'n':len(small),'extensions':E}

    # Compare separate two-chain DP with generic ideal DP, and verify no C interval of size>=2 is autonomous.
    ladder_checks=0
    for t in range(2,7):
        for L in range(0,6):
            pred,C,S,x=ladder_poset(t,L)
            E,ats=rank_distributions(pred,C)
            record,ps,eps=ballot_stats(t,L)
            assert record['full_extensions']==E
            assert all(Fraction(sum(ats[x][:r]),E)==ps[r-1] for r in range(1,t+1))
            for i in range(t-1):
                assert pred[S[i]]>>C[i]&1
                assert not(pred[S[i]]>>C[i+1]&1 or pred[C[i+1]]>>S[i]&1)
            ladder_checks+=1
    out['independent_ladder_formula_checks']=ladder_checks
    out['large_ladder_examples']=[]
    for L in [982,1000,2000]:
        row,ps,eps=ballot_stats(6,L)
        assert eps<Fraction(1,33)
        assert ps[2]<Fraction(1,2)<ps[3]
        assert ps[3]-ps[2]<=Fraction(5,16)+Fraction(11,16)*eps
        row['guaranteed_balance']=str(Fraction(11,32)*(1-eps))
        row['best_of_c3_c4']=str(max(min(p,1-p) for p in ps[2:4]))
        out['large_ladder_examples'].append(row)

    # Maximal window audit: construct all-neutral central extensions in arbitrary module surroundings.
    audits=0
    for _ in range(45):
        nd=rng.randrange(3); nn=rng.randrange(1,5); nf=rng.randrange(3);n=nd+nn+nf
        D=set(range(nd));N=set(range(nd,nd+nn));F=set(range(nd+nn,n))
        edges=[(d,f) for d in D for f in F]
        for u in range(n):
            for v in range(u+1,n):
                if rng.random()<.25:edges.append((u,v))
        pred=closure(n,edges)
        vals=[]
        for seq in enum_extensions(pred):
            positions={v:i for i,v in enumerate(seq)}
            a=max([-1]+[positions[d] for d in D]);b=min([n]+[positions[f] for f in F])
            vals.append(b-a-1)
        assert max(vals)==nn
        audits+=1
    out['maximum_window_kappa_equals_N_checks']=audits
    return out

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--output',default=None)
    args=parser.parse_args();result=run();text=json.dumps(result,ensure_ascii=False,indent=2)
    if args.output:Path(args.output).write_text(text+'\n',encoding='utf-8')
    print(text)
