#!/usr/bin/env python3
"""Exact diagnostics for S93; FKG theorem and counting proofs are in notes/PROOF.md."""
from __future__ import annotations
from fractions import Fraction as F
from functools import lru_cache
from itertools import combinations_with_replacement, permutations
from math import comb
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

def relations(p):
    return [(a,b) for b in range(len(p)) for a in range(len(p)) if p[b]>>a&1]

def counter(p):
    full=(1<<len(p))-1
    @lru_cache(None)
    def tail(m):
        if m==full:return 1
        return sum(tail(m|1<<v) for v in range(len(p))
                   if not(m>>v&1) and p[v]&m==p[v])
    return tail

def rank(p,A,x):
    n=len(p);am=sum(1<<v for v in A);tail=counter(p)
    fw={0:1};out=[0]*(len(A)+1)
    for _ in range(n):
        nxt={}
        for m,w in fw.items():
            for v in range(n):
                if m>>v&1 or p[v]&m!=p[v]:continue
                mm=m|1<<v
                nxt[mm]=nxt.get(mm,0)+w
                if v==x:out[(m&am).bit_count()]+=w*tail(mm)
        fw=nxt
    assert sum(out)==tail(0)
    return out

def extensions(p, labels=None):
    if labels is None:labels=tuple(range(len(p)))
    active=sum(1<<v for v in labels)
    def gen(seq,m):
        if m==active:
            yield tuple(seq);return
        for v in labels:
            if not(m>>v&1) and p[v]&active&m==p[v]&active:
                yield from gen(seq+[v],m|1<<v)
    return gen([],0)

def width(p):
    # Used only on the small illustrative cases.
    return max((m.bit_count() for m in range(1<<len(p))
                if all(not(p[v]&m) for v in range(len(p)) if m>>v&1)),default=0)

def setup(p,A,x):
    am=sum(1<<v for v in A);Q=tuple(v for v in range(len(p)) if not(am>>v&1))
    assert all(p[a]&~am==0 for a in A)
    assert all(p[A[j]]>>A[i]&1 for i in range(len(A)) for j in range(i+1,len(A)))
    assert not(p[x]&am) and all(not(p[a]>>x&1) for a in A)
    I=tuple(v for v in Q if not(p[v]>>A[-1]&1))
    assert x in I and all(v==x or p[v]>>x&1 for v in I)
    return am,Q,I

def verify(p,A,x):
    am,Q,I=setup(p,A,x);L=len(A);d=len(I)
    w=rank(p,A,x);E=sum(w);tail=counter(p);E0=tail(am);G0=tail(am|1<<x)
    assert w[-1]==E0
    assert E>=E0+L*G0
    assert all(w[j]>=w[j+1] for j in range(L-1))
    assert (L+d)*max(w[:-1])<=d*E
    mask=0
    for i,a in enumerate(A,1):
        mask|=1<<a
        assert tail(mask)==sum(w[i:])
        if i<L:assert tail(mask)-tail(mask|1<<A[i])==w[i]
    ps=[F(sum(w[:i]),E) for i in range(1,L+1)]
    best=max(min(v,1-v) for v in ps)
    if L>=d and 2*E0<=E:
        assert best>=F(L,2*(L+d))
    if L>=2*d and L*G0>=E0:
        assert best>=F(1,3)
    if L>=2*d and best<F(1,3):
        assert 3*E0>2*E
    return dict(n=len(p),L=L,d=d,E=E,E0=E0,G0=G0,
                theta=str(F(E0,E)),gamma=str(F(G0,E0)),
                atoms=w,best=str(best),best_index=max(range(L),key=lambda i:min(ps[i],1-ps[i]))+1)

def random_poset(rng,L,d,f):
    n=L+d+f;x=L
    ed=list(zip(range(L),range(1,L)))+[(x,v) for v in range(x+1,x+d)]
    ed +=[(u,v) for u in range(L,n) for v in range(u+1,n) if rng.random()<.3]
    ed +=[(L-1,v) for v in range(L+d,n)]
    for v in range(L+1,L+d):
        h=rng.randrange(L)
        if h:ed.append((h-1,v))
    return closure(n,ed),tuple(range(L)),x

def sandwich(r,q,L,M,thresholds,BE):
    t=r+q;C=tuple(range(t));A=tuple(range(t,t+L));s=t+L;z=s+1;u=z+1
    B=tuple(range(u+1,u+1+M))
    ed=list(zip(C,C[1:]))+list(zip(A,A[1:]))+[(A[-1],s),(s,z),(z,u),(C[r-1],u),(s,C[r])]
    ed += [(u,b) for b in B]+[(B[i],B[j]) for i,j in BE]
    for j,h in enumerate(thresholds,1):
        if h:ed.append((A[h-1],C[j]))
    return closure(u+1+M,ed),A,C[0],(C,s,z,u,B)

def main():
    rng=random.Random(93031026);out={};nprofiles=0;nlattice=0
    for L in range(1,7):
      for k in range(1,6):
        ys=list(combinations_with_replacement(range(L+1),k))
        assert len(ys)==comb(L+k,k)
        for tailh in combinations_with_replacement(range(L),k-1):
            h=(0,)+tailh;w=[0]*(L+1)
            for y in ys:
                nlattice+=1
                if all(a>=b for a,b in zip(y,h)):w[y[0]]+=1
            assert all(w[j]>=w[j+1] for j in range(L))
            assert (L+k)*w[0]<=k*sum(w)
            nprofiles+=1
    out['complete_release_profiles']=nprofiles;out['profile_layout_tests']=nlattice
    generic=0;prefixes=0;half=0;sufficient=0
    for _ in range(320):
        L=rng.randint(1,8);d=rng.randint(1,5);f=rng.randint(0,4)
        p,A,x=random_poset(rng,L,d,f);v=verify(p,A,x)
        generic+=1;prefixes+=L;half+=int(L>=d and 2*v['E0']<=v['E'])
        sufficient+=int(L>=2*d and L*v['G0']>=v['E0'])
    out['generic_actual_posets']=generic;out['prefix_identities']=prefixes
    out['generic_half_crossing_checks']=half;out['gamma_sufficient_checks']=sufficient
    # Check actual old-projection weights and uniform minorization independently.
    weights_cases=0;old_orders=0
    for _ in range(32):
        p,A,x=random_poset(rng,rng.randint(1,4),rng.randint(1,3),rng.randint(0,2))
        am,Q,I=setup(p,A,x);Im=set(I);L=len(A);wt={};ex=0
        for tau in extensions(p,Q):
            k=next((j for j,v in enumerate(tau) if v not in Im),len(tau))
            if k==0:c=1
            else:
                h=[(p[v]&am).bit_count() for v in tau[:k]]
                c=sum(all(a>=b for a,b in zip(y,h)) for y in combinations_with_replacement(range(L+1),k))
            assert c>=1;wt[tau]=c;ex+=c
        assert ex==counter(p)(0)
        nQ=len(wt);q=F(nQ,ex)
        tv=sum(abs(F(c,ex)-F(1,nQ)) for c in wt.values())/2
        assert tv<=1-q
        old_orders+=nQ;weights_cases+=1
    out['independent_old_projection_cases']=weights_cases;out['old_projection_fibres']=old_orders
    # Arbitrary release vectors in the S92 sandwich, not a parameter proof.
    sandcases=0;examples=[]
    for r in range(1,5):
      for q in range(1,4):
       for M in range(4):
        for extra in (0,1,3):
            L=max(3,2*r)+extra
            hs=[rng.randrange(L) for _ in range(r-1)]
            BE=[(i,j) for i in range(M) for j in range(i+1,M) if rng.random()<.4]
            p,A,x,labels=sandwich(r,q,L,M,hs,BE);v=verify(p,A,x)
            rr=F(r*(r+1+2*F(q,M+2)),(r+1)*(r+2+2*F(q,M+2)))
            assert F(v['G0'],v['E0'])==rr>=F(1,3)
            assert F(v['best'])>=F(L,2*(L+r))>=F(1,3)
            sandcases+=1
    out['perturbed_sandwich_posets']=sandcases
    for L,hs in [(6,[2,5]),(8,[3,7]),(12,[4,10])]:
        p,A,x,labels=sandwich(3,3,L,2,hs,[]);v=verify(p,A,x)
        v.update(thresholds=hs,lower_bound=str(F(L,2*(L+3))),
                 predecessor_masks=p,chain_A=A,target=x)
        if L==6:v['width']=width(p)
        examples.append(v)
    out['illustrative_non_autonomous_examples']=examples
    # Endpoint obstruction: A_L<F_M with an otherwise isolated x.
    guards=[]
    for L in (2,4,8):
        M=3*L;x=L+M;A=tuple(range(L))
        p=closure(x+1,list(zip(range(L+M),range(1,L+M))))
        v=verify(p,A,x)
        assert v['atoms']==[1]*L+[M+1]
        assert F(v['theta'])>F(2,3) and F(v['best'])<F(1,3)
        guards.append({k:v[k] for k in ('L','d','E','theta','gamma','atoms','best')})
    out['terminal_guard_examples']=guards
    # Exact extremality of the d/(L+d) bound, A_L disjoint I_d.
    sharp=0
    for L in range(1,9):
      for d in range(1,6):
        p=closure(L+d,list(zip(range(L),range(1,L)))+list(zip(range(L,L+d),range(L+1,L+d))))
        v=verify(p,tuple(range(L)),L)
        assert F(v['atoms'][0],v['E'])==F(d,L+d);sharp+=1
    out['sharpness_cases']=sharp
    # Independent all-permutation enumeration of three small instances.
    brute=0
    for pars in [(2,2,1),(3,2,1),(3,3,1)]:
        p,A,x=random_poset(rng,*pars);w=[0]*(len(A)+1)
        for seq in permutations(range(len(p))):
            pos={v:i for i,v in enumerate(seq)}
            if all(pos[a]<pos[b] for a,b in relations(p)):
                w[sum(pos[a]<pos[x] for a in A)]+=1
        assert w==rank(p,A,x);brute+=1
    out['independent_full_permutation_cases']=brute
    out['scope']='Exact diagnostics; infinite-parameter assertions are proved in notes/PROOF.md. Not an external review.'
    dest=Path(__file__).resolve().parents[1]/'evidence'/'check_s93.json'
    dest.parent.mkdir(exist_ok=True);dest.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if not isinstance(v,list)},ensure_ascii=False,indent=2))
    for e in examples:print('example',e['L'],e['E'],e['atoms'],e['best_index'],e['best'])
if __name__=='__main__':main()
