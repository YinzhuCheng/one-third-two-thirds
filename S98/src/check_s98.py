#!/usr/bin/env python3
"""Exact finite diagnostics for S98. Standard library; not a proof by sampling.
Run: python check_s98.py --output result.json
"""
from __future__ import annotations
from functools import lru_cache
from fractions import Fraction as F
from itertools import combinations, permutations
import argparse, json, random

def closure(n, edges):
    p=[0]*n
    for a,b in edges:
        if not 0<=a<n or not 0<=b<n or a==b: raise ValueError('invalid edge')
        p[b]|=1<<a
    for a in range(n):
        for b in range(n):
            if p[b]>>a&1: p[b]|=p[a]
    if any(p[v]>>v&1 for v in range(n)): raise ValueError('cycle')
    return tuple(p)

def counter(p):
    full=(1<<len(p))-1
    @lru_cache(None)
    def f(mask):
        if mask==full:return 1
        return sum(f(mask|1<<v) for v in range(len(p))
                   if not(mask>>v&1) and not(p[v]&~mask))
    return f

def mins(p,mask=0):
    return [v for v in range(len(p)) if not(mask>>v&1) and not(p[v]&~mask)]

def dot(a,b):return sum(x*y for x,y in zip(a,b))
def mv(A,x):return [dot(row,x) for row in A]
def qf(A,x):return dot(x,mv(A,x))

def det(A):
    """Fraction elimination; exact, including singular principal minors."""
    n=len(A);B=[[F(v) for v in row] for row in A];out=F(1)
    for k in range(n):
        pivot=next((i for i in range(k,n) if B[i][k]),None)
        if pivot is None:return F(0)
        if pivot!=k:B[k],B[pivot]=B[pivot],B[k];out=-out
        v=B[k][k];out*=v
        for i in range(k+1,n):
            r=B[i][k]/v
            for j in range(k+1,n):B[i][j]-=r*B[k][j]
        for i in range(k+1,n):B[i][k]=0
    return out

def check_signature(A):
    """Verify PSD of ss^T-EA, E=1^TA1>0. This implies <=1 positive direction."""
    s=[sum(row) for row in A];E=sum(s)
    if E==0:
        assert all(v==0 for row in A for v in row);return 0
    assert E>0
    K=[[s[i]*s[j]-E*A[i][j] for j in range(len(A))] for i in range(len(A))]
    count=0
    for k in range(1,len(A)+1):
        for I in combinations(range(len(A)),k):
            assert det([[K[i][j] for j in I] for i in I])>=0
            count+=1
    return count

def make_model(rng,m,R):
    chains=[list(range(R))];n=R
    for _ in range(m):
        size=rng.randint(1,4);chains.append(list(range(n,n+size)));n+=size
    roots=[C[0] for C in chains[1:]]
    order=[0]+roots;rest=[C[1:] for C in chains]
    while any(rest):
        k=rng.choice([k for k,c in enumerate(rest) if c]);order.append(rest[k].pop(0))
    edges=[(a,b) for C in chains for a,b in zip(C,C[1:])]
    Bset=set(chains[0]);rootset=set(roots)
    for i,a in enumerate(order):
        for b in order[i+1:]:
            if b not in Bset|rootset and rng.random()<.15:edges.append((a,b))
    return closure(n,edges),roots

def analyze(p,Z,details=False):
    m=len(Z);f=counter(p);E=f(0)
    assert m>=2 and all(p[z]==0 for z in Z)
    B=[v for v in range(len(p)) if v not in Z and all(not(p[v]>>z&1) for z in Z)]
    B.sort(key=lambda v:p[v].bit_count());R=len(B)
    assert R>=1 and all(p[b]>>a&1 for a,b in combinations(B,2))
    masks=[0]
    for b in B:masks.append(masks[-1]|1<<b)
    es=[f(mask) for mask in masks]+[0,0]
    cs=[[f(mask|1<<z) for z in Z] for mask in masks]+[[0]*m]
    vs=[];locals_=[];minor_count=0;compressed=0
    for j,mask in enumerate(masks):
        M=mins(p,mask);assert set(M)==set(Z+([B[j]] if j<R else []))
        V=[]
        for z in Z:
            row=[]
            for w in Z:
                if z!=w:row.append(f(mask|1<<z|1<<w))
                else:
                    newly=[v for v in mins(p,mask|1<<z) if v not in M]
                    assert all(p[v]>>z&1 for v in newly)
                    row.append(sum(f(mask|1<<z|1<<v) for v in newly))
            V.append(row)
        assert [sum(row)+cs[j+1][i] for i,row in enumerate(V)]==cs[j]
        assert es[j]-es[j+1]==sum(cs[j])
        A=[row+[cs[j+1][i]] for i,row in enumerate(V)]+[cs[j+1]+[es[j+2]]]
        assert sum(map(sum,A))==es[j]
        minor_count+=check_signature(A)
        Mblock=[row+[cs[j][i],cs[j+1][i]] for i,row in enumerate(V)]
        Mblock+=[cs[j]+[es[j],es[j+1]],cs[j+1]+[es[j+1],es[j+2]]]
        # Congruence columns: entrance coordinate vectors, all-ones, and b.
        columns=[[int(i==k) for i in range(m+1)] for k in range(m)]
        columns+=[[1]*(m+1),[0]*m+[1]]
        comp=[[dot(a,mv(A,b)) for b in columns] for a in columns]
        assert comp==Mblock;compressed+=1
        vs.append(V);locals_.append(Mblock)
    s=[sum(c[i] for c in cs) for i in range(m)];assert sum(s)==E
    W=[[sum((j+1)*vs[j][a][b] for j in range(R+1)) for b in range(m)] for a in range(m)]
    assert [sum(row) for row in W]==s;minor_count+=check_signature(W)
    local_ineq=energy_ineq=0
    hs=[]
    for i in range(m-1):
        h=[0]*m;h[i]=s[-1];h[-1]=-s[i];hs.append(h)
    if len(hs)>1:hs.append([a-b for a,b in zip(hs[0],hs[-1])])
    for h in hs:
        assert dot(h,s)==0
        g=[F(0)];a=0
        for t in range(1,R+1):
            a+=dot(h,cs[t-1]);g.append(F(a,es[t]))
        g.extend([F(0),F(0)])
        vals=[es[t]*g[t]**2 for t in range(R+3)]
        residual=F(0)
        for t in range(1,R+2):
            assert dot(h,cs[t-1])==es[t]*g[t]-es[t-1]*g[t-1]
            v=list(map(F,h))+[g[t],-g[t]]
            assert qf(locals_[t-1],v)-es[t-1]*(g[t]-g[t-1])**2-es[t+1]*(g[t]-g[t+1])**2==qf(vs[t-1],h)+2*vals[t]-vals[t-1]-vals[t+1]
            assert -qf(vs[t-1],h)>=2*vals[t]-vals[t-1]-vals[t+1]+es[t+1]*(g[t]-g[t+1])**2
            residual+=t*es[t+1]*(g[t]-g[t+1])**2;local_ineq+=1
        assert -qf(W,h)>=residual;energy_ineq+=1
    out=dict(n=len(p),m=m,R=R,E=E,local_blocks=compressed,principal_minors=minor_count,local_energy_checks=local_ineq,global_energy_checks=energy_ineq)
    if m==2:
        H=W[0][1];rx=W[0][0];ry=W[1][1];prob=F(s[0],E)
        qs=[F(sum(c[0] for c in cs[j:]),es[j]) for j in range(R+1)]
        delta=F(H,E)-prob*(1-prob)
        en=sum(F(t*es[t+1],E)*(qs[t+1]-qs[t])**2 for t in range(1,R))
        assert en<=delta
        sym=None;drift=None
        if R>=2:
            beta=[F(1,2)]+[F(t*es[t+1]+(t+1)*es[t],2*E) for t in range(1,R-1)]+[F((R-1)*es[R],2*E)]
            sym=sum(beta[t]*(qs[t+1]-qs[t])**2 for t in range(R));assert sym<=delta
            drift=delta*sum(1/b for b in beta);assert (qs[-1]-prob)**2<=drift
        out.update(p=str(prob),delta=str(delta),energy=str(en),symmetric_energy=str(sym),terminal_drift_bound2=str(drift))
    if details:out.update(predecessor_masks=list(p),entrances=Z,B=B,E_j=es[:R+1],C_j=cs[:R+1],V_j=vs,W=W,S=s,posterior=[str(q) for q in qs] if m==2 else None)
    return out

def brute(p):
    rows=[]
    for L in permutations(range(len(p))):
        mask=0
        for v in L:
            if p[v]&~mask:break
            mask|=1<<v
        else:rows.append(L)
    return rows

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output');args=ap.parse_args()
    rng=random.Random(981008);rows=[]
    for m,count in ((2,140),(3,60)):
        for _ in range(count):
            p,Z=make_model(rng,m,rng.randint(1,7));rows.append(analyze(p,Z))
    # Exact independent permutation checks of entrance totals and prefix first-entry components.
    brute_cases=[]
    for sizes in ((2,2,2),(3,2,2),(3,3,2)):
        R=sizes[0];n=sum(sizes);x=R;y=R+sizes[1]
        edges=[(i,i+1) for start,size in ((0,R),(x,sizes[1]),(y,sizes[2])) for i in range(start,start+size-1)]
        if R>=3:edges.append((0,x+1))
        p=closure(n,edges);v=analyze(p,[x,y],True);L=brute(p)
        assert len(L)==v['E'] and sum(s.index(x)<s.index(y) for s in L)==v['S'][0]
        for j,c in enumerate(v['C_j']):
            for z,num in zip([x,y],c):assert sum(s[:j]==tuple(v['B'][:j]) and s[j]==z for s in L)==num
        brute_cases.append(dict(n=n,E=len(L)))
    p=closure(21,[(i,i+1) for start,end in ((0,12),(12,16),(16,21)) for i in range(start,end-1)]+[(2,14),(4,18)])
    example=analyze(p,[12,16],True)
    # A raw coordinate-deletion array is NOT the correct first-two matrix.
    N=[[1,0,2],[0,0,1],[2,1,0]];v=[1,0,0];w=[-2,3,1]
    assert det(N)==-1 and qf(N,v)==1 and dot(v,mv(N,w))==0 and qf(N,w)==2
    # It arises from P=(0<1) disjoint union (2<3), coordinate chains (0,1),(3),(2).
    p0=closure(4,[(0,1),(2,3)]);f=counter(p0);chains=[[0,1],[3],[2]]
    raw=[]
    for i in range(3):
        row=[]
        for j in range(3):
            removed=chains[i][:2] if i==j else [chains[i][0],chains[j][0]]
            valid=len(removed)==2;mask=sum(1<<z for z in removed)
            valid=valid and all(not(p0[z]&~mask) for z in removed)
            row.append(f(mask) if valid else 0)
        raw.append(row)
    assert raw==N
    out=dict(status='PASSED',seed=981008,random_models=len(rows),two_entrance_models=140,three_entrance_models=60,
      local_blocks=sum(r['local_blocks'] for r in rows),exact_principal_minor_checks=sum(r['principal_minors'] for r in rows),
      local_energy_checks=sum(r['local_energy_checks'] for r in rows),global_energy_checks=sum(r['global_energy_checks'] for r in rows),
      permutation_cases=brute_cases,nonautonomous_example=example,
      raw_array_guard={'poset_predecessor_masks':list(p0),'coordinate_chains':chains,'matrix':N,'positive_subspace_basis':[v,w],'restricted_form':[[1,0],[0,2]]},
      scope='Finite exact diagnostics, not exhaustive poset classification or independent proof of Chan-Pak. Analytic proof handles arbitrary chain length and backend.')
    txt=json.dumps(out,ensure_ascii=False,indent=2)+'\n'
    if args.output:
        from pathlib import Path
        Path(args.output).write_text(txt,encoding='utf-8')
    print(txt)
if __name__=='__main__':main()
