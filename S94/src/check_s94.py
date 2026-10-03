#!/usr/bin/env python3
"""Exact S94 diagnostics. General results rely on the proof, not this sample.
The ideal-DP/counting utilities use the same standard approach as S93, but
this file is standalone and treats two free entrances explicitly.
"""
from __future__ import annotations
from fractions import Fraction as F
from functools import lru_cache
from itertools import permutations, combinations_with_replacement
from pathlib import Path
import json, random

def closure(n, edges):
    p=[0]*n
    for a,b in edges:p[b]|=1<<a
    for a in range(n):
        for b in range(n):
            if p[b]>>a&1:p[b]|=p[a]
    assert not any(p[v]>>v&1 for v in range(n))
    return tuple(p)

def counter(p):
    full=(1<<len(p))-1
    @lru_cache(None)
    def tail(m):
        if m==full:return 1
        return sum(tail(m|1<<v) for v in range(len(p))
                   if not(m>>v&1) and p[v]&m==p[v])
    return tail

def extensions(p, labels=None):
    labels=tuple(range(len(p))) if labels is None else tuple(labels)
    active=sum(1<<v for v in labels)
    def rec(seq,m):
        if m==active:
            yield tuple(seq);return
        for v in labels:
            if not(m>>v&1) and p[v]&active&m==p[v]&active:
                yield from rec(seq+(v,),m|1<<v)
    return rec((),0)

def histograms(p,A,R):
    """Forward/backward ideal DP for first-entrance and both fixed ranks."""
    L=len(A);am=sum(1<<a for a in A);rm=sum(1<<x for x in R)
    tail=counter(p);E=tail(0);group=[0]*(L+1)
    ranks={x:[0]*(L+1) for x in R};fw={0:1}
    for _ in range(len(p)):
        nxt={}
        for m,w in fw.items():
            for v in range(len(p)):
                if m>>v&1 or p[v]&m!=p[v]:continue
                mm=m|1<<v;nxt[mm]=nxt.get(mm,0)+w
                if v in ranks:
                    j=(m&am).bit_count();c=w*tail(mm)
                    ranks[v][j]+=c
                    if not(m&rm):group[j]+=c
        fw=nxt
    assert sum(group)==E and all(sum(h)==E for h in ranks.values())
    return tail,E,group,ranks

def verify(p,A,R):
    L=len(A);am=sum(1<<a for a in A);qm=((1<<len(p))-1)^am
    assert len(R)==2 and all(p[a]&~am==0 for a in A)
    assert all(p[A[j]]>>A[i]&1 for i in range(L) for j in range(i+1,L))
    I=tuple(v for v in range(len(p)) if qm>>v&1 and not(p[v]>>A[-1]&1))
    im=sum(1<<v for v in I)
    assert set(v for v in I if not(p[v]&im))==set(R)
    assert all(not(p[x]&am) and all(not(p[a]>>x&1) for a in A) for x in R)
    tail,E,g,hist=histograms(p,A,R);d=len(I)
    masks=[0]
    for a in A:masks.append(masks[-1]|1<<a)
    Es=[tail(m) for m in masks];eQ=Es[-1]
    gamma_num=sum(tail(am|1<<x) for x in R)
    assert g[-1]==eQ
    assert E>=eQ+L*gamma_num
    assert gamma_num<=eQ and gamma_num*qm.bit_count()>=2*eQ
    for j in range(L):
        assert g[j]==Es[j]-Es[j+1]
        assert Es[j]-Es[j+1]==sum(tail(masks[j]|1<<x) for x in R)
        assert (L+d)*g[j]<=d*E
        if j+1<L:assert g[j]>=g[j+1]
    pair_counts={x:[sum(hist[x][i:]) for i in range(1,L+1)] for x in R}
    selected=[];general_checks=0
    for i in range(1,L+1):
        u,v=(pair_counts[x][i-1] for x in R)
        assert Es[i]==sum(g[i:])
        assert u>=Es[i] and v>=Es[i]
        assert u*v<=Es[i]*E # classical XYZ, checked on the actual P
        if 3*Es[i]>=E and 9*Es[i]<=4*E:
            z=min(R,key=lambda x:pair_counts[x][i-1]);cnt=pair_counts[z][i-1]
            assert 3*min(cnt,E-cnt)>=E
            selected.append((i,z,str(F(cnt,E)),str(F(min(cnt,E-cnt),E))))
    delta=F(max(g[:-1]),E);theta=F(eQ,E)
    for lam in (F(1,4),F(1,3),F(3,8)):
        upper=(1-lam)**2
        if delta<=upper-lam and theta<=upper:
            i=next(i for i in range(1,L+1) if F(Es[i],E)<=upper)
            z=min(R,key=lambda x:pair_counts[x][i-1]);cnt=pair_counts[z][i-1]
            assert min(F(cnt,E),1-F(cnt,E))>=lam
            general_checks+=1
    if L>=8*d and 9*eQ<=4*E:assert selected
    if L>=8*d and 4*L*gamma_num>=5*eQ:assert selected
    any_partner=any(3*min(c,E-c)>=E for cs in pair_counts.values() for c in cs)
    if L>=8*d and not any_partner:
        assert 9*eQ>4*E and 4*L*gamma_num<5*eQ
    return dict(n=len(p),L=L,d=d,E=E,eQ=eQ,Gamma=str(F(gamma_num,eQ)),
                theta=str(theta),delta=str(delta),group=g,
                fixed_ranks={str(x):hist[x] for x in R},
                selected=selected[:1],general_lambda_checks=general_checks,
                qualified=bool(L>=8*d and 9*eQ<=4*E),
                endpoint_failure=bool(L>=8*d and not any_partner))

def random_model(rng,L,d,f):
    R=(L,L+1);ed=list(zip(range(L),range(1,L)))
    for v in range(L+2,L+d):
        ps=[u for u in range(L,v) if rng.random()<.35]
        if not ps:ps=[rng.choice(R)]
        ed.extend((u,v) for u in ps)
        h=rng.randrange(L)
        if h:ed.append((h-1,v))
    for v in range(L+d,L+d+f):
        ed.append((L-1,v))
        ed.extend((u,v) for u in range(L,v) if rng.random()<.25)
    return closure(L+d+f,ed),tuple(range(L)),R

def example(L,h,k,m):
    x,y,z,w=L,L+1,L+2,L+3
    ed=list(zip(range(L),range(1,L)))+[(x,z),(z,w)]
    for v in range(L+4,L+4+m):ed.extend([(L-1,v),(y if v==L+4 else v-1,v)])
    if h:ed.append((h-1,z))
    if k:ed.append((k-1,w))
    return closure(L+4+m,ed),tuple(range(L)),(x,y)

def brute(p,A,R):
    g=[0]*(len(A)+1);hs={x:[0]*(len(A)+1) for x in R};E=0
    for seq in permutations(range(len(p))):
        m=0;valid=True
        for v in seq:
            if p[v]&m!=p[v]:valid=False;break
            m|=1<<v
        if not valid:continue
        E+=1;pos={v:i for i,v in enumerate(seq)}
        ks={x:sum(pos[a]<pos[x] for a in A) for x in R}
        g[min(ks.values())]+=1
        for x,j in ks.items():hs[x][j]+=1
    _,E2,g2,h2=histograms(p,A,R)
    assert (E,g,hs)==(E2,g2,h2)
    return dict(n=len(p),E=E,group=g,fixed_ranks=hs)

def main():
    rng=random.Random(94031026);out={};rows=[];xyz=0;gc=0
    for _ in range(260):
        L=rng.randint(1,10);d=rng.randint(2,6);f=rng.randint(0,4)
        p,A,R=random_model(rng,L,d,f);v=verify(p,A,R)
        rows.append(v);xyz+=L;gc+=v['general_lambda_checks']
    for _ in range(60):
        d=rng.randint(2,5);L=8*d+rng.randint(0,4);f=rng.randint(0,4)
        p,A,R=random_model(rng,L,d,f);v=verify(p,A,R)
        rows.append(v);xyz+=L;gc+=v['general_lambda_checks']
    out['actual_random_posets']=len(rows);out['actual_XYZ_and_prefix_checks']=xyz
    out['general_lambda_selector_checks']=gc
    out['qualified_random_selectors']=sum(v['qualified'] for v in rows)
    out['random_endpoint_failures']=sum(v['endpoint_failure'] for v in rows)
    # Independent explicit old-order + slot enumeration, not uniform deletion.
    nf=0;no=0
    for _ in range(28):
        p,A,R=random_model(rng,rng.randint(1,4),rng.randint(2,4),rng.randint(0,2))
        am=sum(1<<a for a in A);Q=[v for v in range(len(p)) if not(am>>v&1)]
        g=[0]*(len(A)+1);total=0
        for tau in extensions(p,Q):
            k=next((j for j,v in enumerate(tau) if p[v]>>A[-1]&1),len(tau))
            if k==0:g[-1]+=1;total+=1
            else:
                assert tau[0] in R
                hs=[(p[v]&am).bit_count() for v in tau[:k]]
                for ys in combinations_with_replacement(range(len(A)+1),k):
                    if all(y>=h for y,h in zip(ys,hs)):
                        g[ys[0]]+=1;total+=1
            no+=1
        _,E,g2,_=histograms(p,A,R)
        assert g==g2 and E==total;nf+=1
    out['independent_old_projection_cases']=nf;out['old_order_fibres']=no
    family=[]
    for _ in range(64):
        L=rng.randint(32,46);h=rng.randrange(L);k=rng.randrange(L);m=rng.randrange(9)
        p,A,R=example(L,h,k,m);v=verify(p,A,R);assert v['qualified']
        family.append(v)
    out['multithreshold_family_instances']=len(family)
    p,A,R=example(32,8,16,2);v=verify(p,A,R)
    xyedges=[(a,b) for b in range(len(p)) for a in range(len(p)) if p[b]>>a&1]+[(R[0],R[1])]
    v['p_x_before_y']=str(F(counter(closure(len(p),xyedges))(0),v['E']))
    v['selected_index']=8;v['T8']=str(F(counter(p)(sum(1<<a for a in A[:8])),v['E']))
    v['p_a8_before_x']=str(F(sum(v['fixed_ranks'][str(R[0])][8:]),v['E']))
    v['p_a8_before_y']=str(F(sum(v['fixed_ranks'][str(R[1])][8:]),v['E']))
    out['illustration_38_points']=v
    # Actual median counterexample, no main-conjecture counterexample.
    L=18;p=closure(L+2,list(zip(range(L),range(1,L))));A=tuple(range(L));R=(L,L+1)
    v=verify(p,A,R);T=lambda i:F(counter(p)(sum(1<<a for a in A[:i])),v['E'])
    assert T(5)>F(1,2)>T(6)
    assert F(sum(v['fixed_ranks'][str(L)][6:]),v['E'])==F(13,19)
    out['group_median_guard']=dict(n=20,E=v['E'],median_index=6,T6=str(T(6)),
        marginal_at_6='13/19',balance_at_6='6/19',safe_index=7,T7=str(T(7)),balance_at_7='7/19')
    p=(0,1,0,0,5);out['individual_monotonicity_guard']=brute(p,(0,1),(2,3))
    assert out['individual_monotonicity_guard']['fixed_ranks'][3]==[7,9,9]
    brutes=[out['individual_monotonicity_guard']]
    for L,d,f in ((2,3,2),(3,3,2)):
        p,A,R=random_model(rng,L,d,f);brutes.append(brute(p,A,R))
    out['independent_full_permutation_cases']=brutes
    endpoints=[]
    for L in (16,20,32):
        M=2*L;p=closure(L+M+2,list(zip(range(L+M),range(1,L+M))))
        A=tuple(range(L));R=(L+M,L+M+1);v=verify(p,A,R)
        assert v['endpoint_failure'];endpoints.append({k:v[k] for k in ('L','d','theta','Gamma','endpoint_failure')})
    out['terminal_condition_guards']=endpoints
    out['status']='ALL_ASSERTIONS_PASSED'
    print(json.dumps(out,ensure_ascii=False,indent=2))

if __name__=='__main__':main()
