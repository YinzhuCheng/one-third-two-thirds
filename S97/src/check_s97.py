#!/usr/bin/env python3
"""S97 exact diagnostics. Standard library only; finite checks are not a proof.
Usage: python check_s97.py --output results.json
"""
from __future__ import annotations
from functools import lru_cache
from fractions import Fraction
from itertools import combinations, permutations
import argparse, json, random

def closure(n, edges):
    p=[0]*n
    for a,b in edges:
        if a==b or not(0<=a<n and 0<=b<n): raise ValueError('invalid edge')
        p[b]|=1<<a
    for a in range(n):
        for b in range(n):
            if p[b]>>a&1: p[b]|=p[a]
    if any(p[v]>>v&1 for v in range(n)): raise ValueError('cycle')
    return tuple(p)

def tail_counter(p):
    full=(1<<len(p))-1
    @lru_cache(None)
    def f(mask):
        if mask==full:return 1
        return sum(f(mask|1<<v) for v in range(len(p))
            if not(mask>>v&1) and not(p[v]&~mask))
    return f

def extensions(p, removed=0):
    full=(1<<len(p))-1
    def rec(mask,seq):
        if mask==full:
            yield tuple(seq); return
        for v in range(len(p)):
            if not(mask>>v&1) and not(p[v]&~mask):
                seq.append(v); yield from rec(mask|1<<v,seq); seq.pop()
    yield from rec(removed,[])

def direction(p,x,y):
    edges=[(a,b) for b in range(len(p)) for a in range(len(p)) if p[b]>>a&1]
    return tail_counter(closure(len(p),edges+[(x,y)]))(0)

def pair_analysis(p,x,y,details=False):
    assert x!=y and p[x]==p[y]==0
    f=tail_counter(p);E=f(0);S=Rx=Ry=0;fibers=0
    for tau in extensions(p,(1<<x)|(1<<y)):
        dx=next((i+1 for i,v in enumerate(tau) if p[v]>>x&1),len(tau)+1)
        dy=next((i+1 for i,v in enumerate(tau) if p[v]>>y&1),len(tau)+1)
        m=min(dx,dy)
        S+=m*(m+1);Rx+=m*max(dy-dx,0);Ry+=m*max(dx-dy,0);fibers+=1
    U=direction(p,x,y)
    assert E==S+Rx+Ry and U==S//2+Rx
    assert E-U==S//2+Ry
    assert (3*min(U,E-U)>=E)==(2*Rx<=S+4*Ry and 2*Ry<=S+4*Rx)
    assert Fraction(min(U,E-U),E)>=Fraction(S,2*E)
    if 2*(Rx+Ry)<=S:assert 3*min(U,E-U)>=E
    row=dict(n=len(p),x=x,y=y,E=E,U=U,S=S,Rx=Rx,Ry=Ry,deleted_fibers=fibers)
    bm=sum(1<<v for v in range(len(p)) if v not in(x,y) and not(p[v]>>x&1) and not(p[v]>>y&1))
    edges=[(a,b) for b in range(len(p)) for a in range(len(p)) if p[b]>>a&1]
    for root,other,excess,qnum in ((x,y,Rx,U),(y,x,Ry,E-U)):
        removed=bm|1<<root
        Sroot=[v for v in range(len(p)) if v!=other and not(removed>>v&1) and not(p[v]&~removed)]
        complement=tail_counter(closure(len(p),edges+[(other,s) for s in Sroot]))(0)
        assert E-complement==excess
        assert excess>=2*qnum-E
        if Sroot:
            best=max(direction(p,s,other) for s in Sroot)
            k=len(Sroot)
            assert (E-best)**k <= 2*(E-qnum)*E**(k-1)
            if k==1 and 3*qnum>=2*E: assert 3*best>=E
            if k==2 and 9*qnum>=7*E: assert 3*best>=E
        if details: row['private_support_'+str(root)]=Sroot

    B=[v for v in range(len(p)) if v not in(x,y) and not(p[v]>>x&1) and not(p[v]>>y&1)]
    B.sort(key=lambda v:p[v].bit_count())
    ischain=all(p[b]>>a&1 for a,b in combinations(B,2))
    if ischain:
        masks=[0]
        for b in B:masks.append(masks[-1]|1<<b)
        Cx=[f(m|1<<x) for m in masks];Cy=[f(m|1<<y) for m in masks]
        D=[f(m|1<<x|1<<y) for m in masks]
        releases={x:[],y:[]};labels={x:[],y:[]}
        for j,m in enumerate(masks):
            for z,other,C in ((x,y,Cx),(y,x,Cy)):
                rem=m|1<<z
                mins=[v for v in range(len(p)) if not(rem>>v&1) and not(p[v]&~rem)]
                private=[v for v in mins if v!=other and (j==len(B) or v!=B[j])]
                val=sum(f(rem|1<<v) for v in private)
                nxt=C[j+1] if j<len(B) else 0
                assert C[j]-nxt==D[j]+val
                assert val>=0
                releases[z].append(val);labels[z].append(private)
        assert S==2*sum((j+1)*v for j,v in enumerate(D))
        assert Rx==sum((j+1)*v for j,v in enumerate(releases[x]))
        assert Ry==sum((j+1)*v for j,v in enumerate(releases[y]))
        assert U==sum(Cx) and E-U==sum(Cy)
        row['prefix_steps']=len(masks)
        if details:row.update(B=B,Cx=Cx,Cy=Cy,D=D,private_x=releases[x],private_y=releases[y],release_labels=labels)
    if details:row['predecessor_masks']=list(p)
    return row

def guard():
    # b1,b2,b3,x,y,u,v,z
    return closure(8,[(0,1),(1,2),(0,5),(3,5),(0,6),(4,6),(5,7),(6,7)])

def threechain(rng,sizes):
    chains=[];n=0
    for size in sizes:chains.append(list(range(n,n+size)));n+=size
    roots=[C[0] for C in chains]; order=roots[:];rest=[C[1:] for C in chains]
    while any(rest):
        i=rng.choice([i for i,r in enumerate(rest) if r]);order.append(rest[i].pop(0))
    edges=[(a,b) for C in chains for a,b in zip(C,C[1:])]
    for i,a in enumerate(order):
        for b in order[i+1:]:
            if b not in roots and rng.random()<.17:edges.append((a,b))
    return closure(n,edges),roots

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output');args=ap.parse_args()
    rng=random.Random(96042026);rows=[]
    for _ in range(160):
        n=rng.randint(3,9)
        edges=[(i,j) for j in range(2,n) for i in range(j) if rng.random()<.27]
        rows.append(pair_analysis(closure(n,edges),0,1))
    for _ in range(100):
        p,roots=threechain(rng,[rng.randint(1,3) for _ in range(3)])
        for x,y in combinations(roots,2):rows.append(pair_analysis(p,x,y))
    p=guard();G=pair_analysis(p,3,4,True)
    valid=[]
    for seq in permutations(range(8)):
        mask=0
        for v in seq:
            if p[v]&~mask:break
            mask|=1<<v
        else:valid.append(seq)
    assert len(valid)==256
    directions={str(z):[sum(seq.index(i)<seq.index(z) for seq in valid) for i in range(3)] for z in (3,4)}
    assert directions=={'3':[171,74,20],'4':[171,74,20]}
    assert direction(p,3,4)==128
    for z in (3,4):
        assert 3*directions[str(z)][0]>2*256
        assert all(3*min(c,256-c)<256 for c in directions[str(z)])
    G.update(B_before_root_counts=directions,brute_extensions=len(valid),group=[a+b for a,b in zip(G['Cx'],G['Cy'])])
    # Exact width-three certificate: chain cover and antichain.
    covers=[[0,1,2],[3,5,7],[4,6]]
    assert all(p[b]>>a&1 for C in covers for a,b in zip(C,C[1:]))
    assert all(not(p[b]>>a&1) and not(p[a]>>b&1) for a,b in combinations([0,3,4],2))
    G['three_chain_cover']=covers
    out=dict(status='PASSED',seed=96042026,arbitrary_posets=160,three_chain_posets=100,
             pair_instances=len(rows),deleted_fibers=sum(r['deleted_fibers'] for r in rows),
             avoidance_chain_instances=sum('prefix_steps'in r for r in rows),
             private_release_steps=sum(r.get('prefix_steps',0) for r in rows),guard=G,
             checks='Original ideal DP, independent double-deletion enumeration, private-release identities; guard full permutation sieve',
             scope='Finite diagnostics only. No global counterexample claim; no minimality claim.')
    txt=json.dumps(out,ensure_ascii=False,indent=2)
    if args.output:
        from pathlib import Path
        Path(args.output).write_text(txt+'\n',encoding='utf-8')
    print(txt)
if __name__=='__main__':main()
