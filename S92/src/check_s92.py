#!/usr/bin/env python3
"""Exact diagnostics for S92. Standard library; analytic proofs in notes/PROOF.md."""
from __future__ import annotations
from functools import lru_cache
from fractions import Fraction as F
from itertools import permutations
from math import comb
from pathlib import Path
import json, random


def closure(n,edges):
    pred=[0]*n
    for a,b in edges: pred[b]|=1<<a
    for k in range(n):
        for v in range(n):
            if pred[v]>>k&1: pred[v]|=pred[k]
    assert not any(pred[v]>>v&1 for v in range(n))
    return tuple(pred)


def count(pred, forbidden=frozenset(), C=()):
    n=len(pred); full=(1<<n)-1;cm=sum(1<<v for v in C)
    @lru_cache(None)
    def go(mask):
        if mask==full:return 1
        k=(mask&cm).bit_count()
        return sum(go(mask|1<<v) for v in range(n) if not(mask>>v&1)
                   and pred[v]&mask==pred[v] and (v,k) not in forbidden)
    return go(0)


def rank_counts(pred,C,x):
    n=len(pred);full=(1<<n)-1;cm=sum(1<<v for v in C)
    @lru_cache(None)
    def tail(mask):
        if mask==full:return 1
        return sum(tail(mask|1<<v) for v in range(n)
                   if not(mask>>v&1) and pred[v]&mask==pred[v])
    fw={0:1};out=[0]*(len(C)+1)
    for _ in range(n):
        nxt={}
        for mask,f in fw.items():
            for v in range(n):
                if mask>>v&1 or pred[v]&mask!=pred[v]:continue
                m=mask|1<<v
                if v==x:out[(mask&cm).bit_count()]+=f*tail(m)
                nxt[m]=nxt.get(m,0)+f
        fw=nxt
    assert sum(out)==tail(0)
    return tail(0),out


def direction(pred,a,b):
    return count(closure(len(pred),[(u,v) for v in range(len(pred))
                 for u in range(len(pred)) if pred[v]>>u&1]+[(a,b)]))


def make(r,q,L,M,AE=None,BE=None):
    # C[0:r+q], A, s,x,u, B. AE/BE refer to local block labels.
    t=r+q; C=tuple(range(t)); A=tuple(range(t,t+L));s=t+L;x=s+1;u=x+1
    B=tuple(range(u+1,u+1+M));n=u+1+M
    if AE is None: AE=list(zip(range(L),range(1,L)))
    if BE is None: BE=list(zip(range(M),range(1,M)))
    edges=list(zip(C,C[1:]))+[(A[a],A[b]) for a,b in AE]+[(B[a],B[b]) for a,b in BE]
    edges += [(a,s) for a in A]+[(s,x),(x,u)]+[(u,b) for b in B]+[(C[r-1],u),(s,C[r])]
    return closure(n,edges),C,A,s,x,u,B


def atom_formula(r,q,L,M):
    f=[comb(L+min(r,k)+1,min(r,k))*comb(M+min(q,r+q-k)+1,min(q,r+q-k))
       for k in range(r+q+1)]
    Z=comb(L+r+1,r)*comb(M+q+1,q)*(1+F(r,L+2)+F(q,M+2))
    assert Z.denominator==1 and sum(f)==Z
    return int(Z),f


def H(r,q,M,z):
    return (1+F(q,M+2))*comb(z+r+1,r)+comb(z+r+1,r-1)


def select(r,q,L,M):
    h=H(r,q,M,L)
    p=[1-H(r,q,M,L-i)/h for i in range(L+1)]
    assert p[0]==0
    i=next(i for i,v in enumerate(p) if v>=F(1,2))
    choices=[j for j in (i-1,i) if j>=1]
    best=max(choices,key=lambda j:min(p[j],1-p[j]))
    beta=F(L+1,2*(L+r+1))
    assert min(p[best],1-p[best])>=beta>=F(1,3)
    return best,p[best],beta


def brute(pred,C,x):
    out=[0]*(len(C)+1);n=len(pred)
    for seq in permutations(range(n)):
        mask=0;k=0;j=None
        for v in seq:
            if pred[v]&mask!=pred[v]:break
            if v==x:j=k
            if v in C:k+=1
            mask|=1<<v
        else:out[j]+=1
    return sum(out),out


def main():
    rng=random.Random(92031026);stats={};atom_cases=0;atom_items=0;prefix_items=0
    for r in range(1,5):
      for q in range(1,5):
       for L in range(5):
        for M in range(5):
         P,C,A,s,x,u,B=make(r,q,L,M)
         E,a=rank_counts(P,C,x);Z,f=atom_formula(r,q,L,M)
         assert (E,a)==(Z,f)
         assert all(not(P[x]>>c&1 or P[c]>>x&1) for c in C)
         assert all((P[x]>>v&1 or P[v]>>x&1) for v in (*A,s,u,*B))
         atom_cases+=1;atom_items+=len(a)
         if L:
          E2,d=rank_counts(P,A,C[0]);assert E2==E
          for i in range(1,L+1):
           assert F(sum(d[:i]),E)==1-H(r,q,M,L-i)/H(r,q,M,L)
           prefix_items+=1
    stats['chain_block_posets']=atom_cases;stats['central_rank_identities']=atom_items
    stats['actual_prefix_direction_identities']=prefix_items
    shapes=0
    for _ in range(60):
        r=rng.randint(1,3);q=rng.randint(1,3);L=rng.randint(0,4);M=rng.randint(0,4)
        AE=[(i,j) for i in range(L) for j in range(i+1,L) if rng.random()<.35]
        BE=[(i,j) for i in range(M) for j in range(i+1,M) if rng.random()<.35]
        P,C,A,s,x,u,B=make(r,q,L,M,AE,BE)
        eA=count(closure(L,AE));eB=count(closure(M,BE));E,a=rank_counts(P,C,x);Z,f=atom_formula(r,q,L,M)
        assert E==eA*eB*Z and a==[eA*eB*v for v in f]
        shapes+=1
    stats['arbitrary_block_shape_posets']=shapes
    quantiles=0;extra_dp=0
    for r in range(1,9):
      for q in range(1,6):
       for M in (0,1,3,10):
        start=max(3,2*r-1)
        for L in (start,start+1,start+5,start+19):
          j,p,b=select(r,q,L,M);quantiles+=1
          vals=[H(r,q,M,z) for z in range(L+1)]
          differences=[vals[i+1]-vals[i] for i in range(L)]
          assert differences==sorted(differences)
          assert differences[-1]/vals[-1]<=F(r,L+r+1)
          assert vals[0]/vals[-1]<=F(1,2)
          if L<=8 and r+q<=6 and M<=3:
            P,C,A,s,x,u,B=make(r,q,L,M)
            assert F(direction(P,C[0],A[j-1]),count(P))==p;extra_dp+=1
    stats['all_parameter_quantile_diagnostics']=quantiles;stats['quantile_extra_full_poset_dp']=extra_dp
    eps=[]
    for n in range(0,9):
        P,C,A,s,x,u,B=make(3,3,n,n)
        E,a=rank_counts(P,C,x);S=(*A,s,u,*B)
        good=count(P,frozenset((v,k) for v in S for k in range(1,6)),C)
        assert good==7
        chi_num=a[3]-1
        assert F(sum(a[:3]),E)==F(3,n+8)
        assert F(a[3],E)==F(n+2,n+8)
        assert 16*a[3]<=5*E+11*chi_num
        if n>=2: assert all(min(F(sum(a[:i]),E),1-F(sum(a[:i]),E))<F(1,3) for i in range(1,7))
        eps.append({'n':n,'extensions_per_shape_factor':E,'p_x_before_c3':str(F(sum(a[:3]),E)),
                    'p_x_before_c4':str(F(sum(a[:4]),E)),'central_atom':str(F(a[3],E)),
                    'epsilon3':str(1-F(good,E)),'chi3':str(F(chi_num,E))})
    stats['symmetric_congestion_examples']=eps
    bcases=0
    for args in [(1,1,1,1),(2,1,1,1),(2,2,1,1)]:
        P,C,A,s,x,u,B=make(*args)
        assert brute(P,C,x)==rank_counts(P,C,x);bcases+=1
    stats['independent_full_permutation_cases']=bcases
    # Exact width-three witness with an antichain A_2 and chain B_2.
    P,C,A,s,x,u,B=make(3,3,2,2,[],[(0,1)])
    E,a=rank_counts(P,C,x)
    anti=(A[0],A[1],C[0]);assert all(not(P[v]>>w&1 or P[w]>>v&1) for v in anti for w in anti if v!=w)
    assert E==2000
    stats['explicit_width3_example']={'predecessor_masks':P,'C':C,'x':x,'A':A,'s':s,'u':u,'B':B,
                                    'extensions':E,'x_rank_counts':a,'three_antichain':anti}
    stats['selected_symmetric_witnesses']=[]
    for n in [5,10,30,1000]:
        j,p,b=select(3,3,n,n)
        stats['selected_symmetric_witnesses'].append({'L':n,'selected_A_rank':j,'probability_c1_before_a':str(p),'balance':str(min(p,1-p)),'guaranteed':str(b)})
    # Independent full-P joint-event computation for the collision refinement.
    checked=0;cases=0;attempts=0
    while cases<50 and attempts<2000:
        attempts+=1;t=rng.randint(6,9);extra=rng.randint(2,4);n=t+extra
        C=tuple(range(t));order=list(C)
        for v in range(t,n):order.insert(rng.randrange(len(order)+1),v)
        ed=list(zip(C,C[1:]))
        for i in range(n):
          for j in range(i+1,n):
            if (order[i]>=t or order[j]>=t) and rng.random()<.11:ed.append((order[i],order[j]))
        P=closure(n,ed);S=[];neutral=[]
        for v in range(t,n):
            lo=all(P[c]>>v&1 for c in C);hi=all(P[v]>>c&1 for c in C)
            inc=all(not(P[c]>>v&1 or P[v]>>c&1) for c in C)
            if inc:neutral.append(v)
            elif not(lo or hi):S.append(v)
        if not neutral:continue
        for x in neutral:
            E,atoms=rank_counts(P,C,x)
            for rr in range(3,t-2):
                forbid=frozenset([(v,k) for v in S for k in range(max(0,rr-2),min(t,rr+2)+1)]
                                  +[(x,k) for k in range(t+1) if k!=rr])
                jointly_good=count(P,forbid,C)
                chi=atoms[rr]-jointly_good
                assert 0<=chi<=atoms[rr] and 16*atoms[rr]<=5*E+11*chi
                checked+=1
        cases+=1
    stats['generic_collision_posets']=cases;stats['generic_collision_inequalities']=checked
    stats['status']='passed';stats['external_review']=False
    path=Path(__file__).resolve().parents[1]/'evidence/check_s92.json'
    path.write_text(json.dumps(stats,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(stats,ensure_ascii=False,indent=2))

if __name__=='__main__':main()
