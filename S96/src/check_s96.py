#!/usr/bin/env python3
"""S96 exact diagnostics (standard library). No finite run proves the theorem."""
from __future__ import annotations
from functools import lru_cache
from fractions import Fraction as F
from itertools import combinations, permutations
from pathlib import Path
import json, random

def closure(n, edges):
    p=[0]*n
    for a,b in edges:
        if not (0<=a<n and 0<=b<n): raise ValueError('invalid vertex')
        p[b]|=1<<a
    for a in range(n):
        for b in range(n):
            if p[b]>>a&1:p[b]|=p[a]
    if any(p[v]>>v&1 for v in range(n)):raise ValueError('cycle')
    return tuple(p)

def counter(p):
    n=len(p);full=(1<<n)-1
    @lru_cache(None)
    def f(mask):
        if mask==full:return 1
        return sum(f(mask|1<<v) for v in range(n) if not(mask>>v&1) and p[v]&mask==p[v])
    return f

def induced(p, deleted):
    vs=[v for v in range(len(p)) if v not in deleted]; ix={v:i for i,v in enumerate(vs)}
    return tuple(sum(1<<ix[u] for u in vs if p[v]>>u&1) for v in vs),ix

def rank_hist(p,x):
    f=counter(p); out=[0]*len(p); fw={0:1}
    for k in range(len(p)):
        nxt={}
        for mask,w in fw.items():
            for v in range(len(p)):
                if mask>>v&1 or p[v]&mask!=p[v]:continue
                mm=mask|1<<v;nxt[mm]=nxt.get(mm,0)+w
                if v==x:out[k]+=w*f(mm)
        fw=nxt
    return out

def pair_count(p,x,y):
    pp=list(p); pp[y]|=1<<x
    pp=closure(len(p),[(u,v) for v in range(len(p)) for u in range(len(p)) if pp[v]>>u&1])
    return counter(pp)(0)

def avoidance(p,x,y):
    assert p[x]==p[y]==0
    B=[v for v in range(len(p)) if v not in (x,y) and not(p[v]>>x&1 or p[v]>>y&1)]
    B.sort(key=lambda v:p[v].bit_count())
    assert all(p[B[j]]>>B[i]&1 for i in range(len(B)) for j in range(i+1,len(B)))
    return B

def gate(p,B):
    bm=sum(1<<v for v in B)
    assert all(p[v]&~bm==0 for v in B)
    g=len(p)
    pp=tuple(p[v] | (0 if v in B else 1<<g) for v in range(g))+(0,)
    return pp,g

def fields(p,x,y):
    B=avoidance(p,x,y);f=counter(p);E=f(0); ms=[0]
    for b in B:ms.append(ms[-1]|1<<b)
    Es=[f(m) for m in ms]
    C=[[f(m|1<<z) for m in ms] for z in(x,y)]
    assert sum(C[0])+sum(C[1])==E
    return B,E,Es,C

def tail_bound(c,h):
    R=len(c)-1; prefix=sum(c[:h+1]);n=R-h
    if n==0:return F(prefix)
    q=F(c[h],c[h-1])
    return F(prefix)+c[h]*sum((q**j for j in range(1,n+1)),F(0))

def random_poset(rng, sizes):
    Cs=[];k=0
    for n in sizes:Cs.append(list(range(k,k+n)));k+=n
    edges=[(a,b) for C in Cs for a,b in zip(C,C[1:])]
    order=[C[0] for C in Cs]; rest=[C[1:] for C in Cs]
    while any(rest):
        c=rng.choice([i for i,R in enumerate(rest) if R]);order.append(rest[c].pop(0))
    root=set(order[:3]); chain={v:i for i,C in enumerate(Cs)for v in C}
    for i,a in enumerate(order):
        for b in order[i+1:]:
            if b not in root and chain[a]!=chain[b] and rng.random()<.15:edges.append((a,b))
    return closure(k,edges),Cs

def main():
    rng=random.Random(9606);counts=dict(posets=0,root_configurations=0,log_concavity_checks=0,gate_rank_equalities=0,tail_bounds=0,five_count_certificates=0)
    for _ in range(180):
        p,Cs=random_poset(rng,[rng.randint(1,5) for _ in range(3)])
        counts['posets']+=1
        for x,y in combinations([C[0]for C in Cs],2):
            B,E,Es,C=fields(p,x,y);R=len(B)
            if R<1:continue
            counts['root_configurations']+=1
            for seq in [Es,*C]:
                assert all(a>=b>0 for a,b in zip(seq,seq[1:]))
                for j in range(1,R):
                    assert seq[j]**2>=seq[j-1]*seq[j+1];counts['log_concavity_checks']+=1
            if counts['root_configurations']<=60:
                for z,c in zip((x,y),C):
                    pp,ix=induced(p,{z});BB=[ix[b]for b in B];gg,g=gate(pp,BB)
                    rh=rank_hist(gg,g)
                    assert rh[:R+1]==c and not any(rh[R+1:])
                    counts['gate_rank_equalities']+=len(rh)
            for c in C:
                for h in range(1,R+1):
                    assert sum(c)<=tail_bound(c,h);counts['tail_bounds']+=1
                    if c[h]<c[h-1]:
                        upper=F(sum(c[:h+1]))+F(c[h]**2,c[h-1]-c[h])
                        assert sum(c)<=upper;counts['tail_bounds']+=1
            if all(c[0]>c[1] and 3*c[0]**2<=2*E*(c[0]-c[1]) for c in C):
                assert 3*min(sum(c)for c in C)>=E;counts['five_count_certificates']+=1
    p=(0,5,0,4,13,29,0,68,204);x,y=0,6
    B,E,Es,C=fields(p,x,y)
    pairs=[[pair_count(p,b,z)for b in B]for z in(x,y)]
    assert B==[2,3] and E==737 and C==[[187,133,60],[183,129,45]]
    assert all(3*q[0]>2*E and 3*q[1]<E for q in pairs)
    independent=0;dirxy=0;pref=[[0]*3,[0]*3]
    for sig in permutations(range(9)):
        m=0;ok=True
        for v in sig:
            if p[v]&m!=p[v]:ok=False;break
            m|=1<<v
        if not ok:continue
        independent+=1;loc={v:i for i,v in enumerate(sig)};dirxy+=loc[x]<loc[y]
        z=x if loc[x]<loc[y]else y;j=sum(loc[b]<loc[z]for b in B);pref[(x,y).index(z)][j]+=1
    assert independent==E and dirxy==380 and pref==C
    R,m,n=12,4,5;x=R;y=R+m
    ed=list(zip(range(R),range(1,R)))+list(zip(range(R,R+m),range(R+1,R+m)))+list(zip(range(R+m,R+m+n),range(R+m+1,R+m+n)))+[(2,R+2),(4,R+m+2)]
    p2=closure(R+m+n,ed);B2,E2,Es2,C2=fields(p2,x,y)
    assert E2==24172740 and [c[:2]for c in C2]==[[4215480,2959380],[4311300,3069990]]
    upp=[F(c[0]**2,c[0]-c[1]) for c in C2]
    lo=max(F(sum(C2[0][:2]),E2),1-upp[1]/E2)
    hi=min(upp[0]/E2,1-F(sum(C2[1][:2]),E2))
    assert F(1,3)<=lo<=F(sum(C2[0]),E2)<=hi<=F(2,3)
    assert max(sum(c[:2])for c in C2)<F(E2,3)
    out={'checks':counts,'guard9':{'p':list(p),'B':B,'roots':[0,6],'E':E,'E_j':Es,'marked':C,'B_before_root_counts':pairs,'entry_pair_count':380,'independent_full_permutation_extensions':independent},'certificate21':{'p':list(p2),'B':B2,'roots':[x,y],'E':E2,'initial_marked':[c[:2]for c in C2],'geometric_upper_probabilities':[str(v/E2)for v in upp],'certified_interval_x_before_y':[str(lo),str(hi)],'actual_probability':str(F(sum(C2[0]),E2)),'actual_marked':C2},'scope':'finite diagnostics only; the general argument is in notes/PROOF.md'}
    ff=counter(p2);ff(0);out['certificate21']['state_count']=ff.cache_info().currsize
    print(json.dumps(out,ensure_ascii=False,indent=2))
if __name__=='__main__':main()
