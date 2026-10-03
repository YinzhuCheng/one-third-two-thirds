#!/usr/bin/env python3
"""S95 exact diagnostics. Standalone standard-library code, not a general proof.
All direction probabilities come from the full original poset's extension counts.
"""
from __future__ import annotations
from functools import lru_cache
from fractions import Fraction as F
from itertools import combinations, permutations
from pathlib import Path
import json, random


def closure(n, edges):
    p=[0]*n
    for a,b in edges:
        if not (0<=a<n and 0<=b<n): raise ValueError('bad label')
        p[b] |= 1<<a
    for a in range(n):
        for b in range(n):
            if p[b]>>a&1:p[b] |= p[a]
    if any(p[v]>>v&1 for v in range(n)):raise ValueError('cycle')
    return tuple(p)


def counter(p):
    n=len(p); full=(1<<n)-1
    @lru_cache(None)
    def tail(m):
        if m==full:return 1
        return sum(tail(m|1<<v) for v in range(n)
                   if not(m>>v&1) and p[v]&m==p[v])
    return tail


def avoidance(p,x,y):
    assert p[x]==p[y]==0 and x!=y
    B=[v for v in range(len(p)) if v not in (x,y)
       and not(p[v]>>x&1) and not(p[v]>>y&1)]
    B.sort(key=lambda v:p[v].bit_count())
    assert all(p[B[j]]>>B[i]&1 for i in range(len(B)) for j in range(i+1,len(B)))
    bm=sum(1<<v for v in B)
    assert all(p[v]&~bm==0 for v in B)
    return B


def histogram(p,B,targets):
    n=len(p); bm=sum(1<<v for v in B); rm=sum(1<<z for z in targets)
    tail=counter(p);E=tail(0);R=len(B)
    group=[0]*(R+1);by_first={z:[0]*(R+1) for z in targets}
    marginal={z:[0]*(R+1) for z in targets};fw={0:1}
    for _ in range(n):
        nxt={}
        for mask,w in fw.items():
            for v in range(n):
                if mask>>v&1 or p[v]&mask!=p[v]:continue
                mm=mask|1<<v;nxt[mm]=nxt.get(mm,0)+w
                if v in marginal:
                    j=(mask&bm).bit_count(); c=w*tail(mm)
                    marginal[v][j]+=c
                    if not(mask&rm):group[j]+=c;by_first[v][j]+=c
        fw=nxt
    return tail,E,group,by_first,marginal


def analyze(p,x,y,initial_L=None,keep=False):
    B=avoidance(p,x,y);R=len(B)
    assert R>=1
    f,E,g,gz,h=histogram(p,B,(x,y))
    masks=[0]
    for b in B:masks.append(masks[-1]|1<<b)
    Es=[f(m) for m in masks]
    assert sum(g)==E
    for j,m in enumerate(masks):
        assert g[j]==sum(f(m|1<<z) for z in (x,y))
        for z in (x,y):
            assert gz[z][j]==f(m|1<<z)
            if j<R:assert gz[z][j]>=gz[z][j+1]
        if j<R:assert Es[j]-Es[j+1]==g[j]
        assert sum(g[j:])==Es[j]
        assert Es[j]+j*g[j]<=E
    assert Es[-1]==g[-1] and (R+1)*g[-1]<=E
    uv={z:[sum(h[z][i:]) for i in range(1,R+1)] for z in (x,y)}
    for i in range(1,R+1):
        u,v=uv[x][i-1],uv[y][i-1]
        assert u>=Es[i] and v>=Es[i]
        assert u*v<=Es[i]*E
    safe=[i for i in range(1,R+1) if 3*Es[i]>=E and 9*Es[i]<=4*E]
    selected=None
    if 9*g[0]<=E:
        assert safe
        i=next(i for i in range(1,R+1) if 9*Es[i]<=4*E)
        z=min((x,y),key=lambda z:uv[z][i-1]);c=uv[z][i-1]
        assert 3*min(c,E-c)>=E
        selected=dict(index=i,label=z,joint=str(F(Es[i],E)),
                      direction=str(F(c,E)),balance=str(F(min(c,E-c),E)))
    # General-lambda first-atom criterion.
    general=0
    for lam in (F(1,4),F(1,3),F(3,8)):
        U=(1-lam)**2; gap=U-lam
        if gap>0 and F(g[0],E)<=gap:
            i=next(i for i in range(1,R+1) if F(Es[i],E)<=U)
            z=min((x,y),key=lambda z:uv[z][i-1]);c=F(uv[z][i-1],E)
            assert lam<=c<=1-lam;general+=1
    partner=any(3*min(c,E-c)>=E for z in (x,y) for c in uv[z])
    front=None
    if R>=2 and not partner:
        i=next(i for i in range(1,R+1) if 9*Es[i]<=4*E)
        assert 2*E<6*Es[i-1] # redundant positive sanity, not the main threshold
        assert 9*Es[i-1]>4*E and 3*Es[i]<E and i<=5
        front=i
    init=None
    if initial_L is not None:
        assert initial_L<=R
        a=B[initial_L-1]
        d=sum(v not in B[:initial_L] and not(p[v]>>a&1) for v in range(len(p)))
        assert g[0]*(initial_L+d)<=d*E # inherited S94 first-atom lemma
        T=F(Es[initial_L],E)
        old_partner=any(3*min(c,E-c)>=E for z in (x,y) for c in uv[z][:initial_L])
        if initial_L>=8*d:
            assert selected is not None
            if not old_partner:assert selected['index']>initial_L
        init=dict(L=initial_L,d=d,theta=str(T),theta_float=float(T),
                  has_entry_partner=old_partner,
                  last_directions={str(z):str(F(uv[z][initial_L-1],E)) for z in (x,y)})
    row=dict(n=len(p),R=R,E=E,first_atom=str(F(g[0],E)),
             last_atom=str(F(g[-1],E)),selected=selected,initial=init,
             general_lambda_checks=general,no_entry_partner_front=front,
             states=f.cache_info().currsize)
    if keep:
        row.update(B=B,entries=[x,y],predecessor_masks=list(p),group=g,
                   entrance_split={str(z):gz[z] for z in (x,y)},
                   fixed_rank_histograms={str(z):h[z] for z in (x,y)})
    return row


def family(R,h,k,m=1):
    x,z,w,y=R,R+1,R+2,R+3
    ed=list(zip(range(R),range(1,R)))+[(x,z),(z,w)]
    for j in range(m):ed.extend([(R-1,R+4+j),(y if j==0 else R+3+j,R+4+j)])
    if h:ed.append((h-1,z))
    if k:ed.append((k-1,w))
    return closure(R+4+m,ed),x,y


def random_three_chains(rng,R,pn,qn,protected=0):
    B=list(range(R));X=list(range(R,R+pn));Y=list(range(R+pn,R+pn+qn))
    ed=list(zip(B,B[1:]))+list(zip(X,X[1:]))+list(zip(Y,Y[1:]))
    # Topological template starts at the three minimal roots, then randomly merges chains.
    order=[B[0],X[0],Y[0]];rests=[B[1:],X[1:],Y[1:]]
    while any(rests):
        c=rng.choice([i for i,r in enumerate(rests) if r]);order.append(rests[c].pop(0))
    roots=set(order[:3]);cid={v:j for j,C in enumerate((B,X,Y)) for v in C}
    for i,a in enumerate(order):
        for b in order[i+1:]:
            if b in roots or cid[a]==cid[b]:continue
            if cid[b]==0 and b<protected:continue
            if rng.random()<.12:ed.append((a,b))
    return closure(R+pn+qn,ed),X[0],Y[0]


def brute(p,x,y):
    B=avoidance(p,x,y);R=len(B);g=[0]*(R+1);gz={z:[0]*(R+1) for z in (x,y)}
    valid=[];n=len(p)
    for seq in permutations(range(n)):
        mask=0
        for v in seq:
            if p[v]&mask!=p[v]:break
            mask|=1<<v
        else:
            valid.append(seq);pos={v:i for i,v in enumerate(seq)}
            z=min((x,y),key=pos.get);j=sum(pos[b]<pos[z] for b in B)
            g[j]+=1;gz[z][j]+=1
    images={};checks=0
    for seq in valid:
        pos={v:i for i,v in enumerate(seq)};z=min((x,y),key=pos.get)
        j=sum(pos[b]<pos[z] for b in B)
        if j==0:continue
        assert seq[:j]==tuple(B[:j]) and seq[j]==z
        out=seq[:j-1]+(z,B[j-1])+seq[j+1:]
        mask=0
        for v in out:assert p[v]&mask==p[v];mask|=1<<v
        key=(j,z,out);assert key not in images;images[key]=seq;checks+=1
    _,E,g2,gz2,_=histogram(p,B,(x,y))
    assert (len(valid),g,gz)==(E,g2,gz2)
    return dict(n=n,E=E,swap_injection_checks=checks)



def independent_grid(R,h,k,m,selected_i):
    """Different state representation: prefixes of the three given chains."""
    @lru_cache(None)
    def f(a,j,l):
        if (a,j,l)==(R,3,m+1):return 1
        ans=0
        if a<R:ans+=f(a+1,j,l)
        if j<3 and (j==0 or a>=(h if j==1 else k)):ans+=f(a,j+1,l)
        if l<m+1 and (l==0 or a==R):ans+=f(a,j,l+1)
        return ans
    E=f(0,0,0);fw={(0,0,0):1};uv=[0,0]
    for _ in range(R+m+4):
        nxt={}
        for (a,j,l),v in fw.items():
            moves=[]
            if a<R:moves.append((a+1,j,l))
            if j<3 and (j==0 or a>=(h if j==1 else k)):
                moves.append((a,j+1,l))
                if j==0 and a>=selected_i:uv[0]+=v*f(a,j+1,l)
            if l<m+1 and (l==0 or a==R):
                moves.append((a,j,l+1))
                if l==0 and a>=selected_i:uv[1]+=v*f(a,j,l+1)
            for st in moves:nxt[st]=nxt.get(st,0)+v
        fw=nxt
    return E,f(32,0,0),uv

def main():
    rng=random.Random(951003);out={};rows=[]
    for _ in range(180):
        p,x,y=random_three_chains(rng,rng.randint(1,12),rng.randint(1,5),rng.randint(1,5))
        rows.append(analyze(p,x,y))
    long=[]
    for _ in range(36):
        pnum,qnum=rng.randint(1,4),rng.randint(1,4)
        L=8*(pnum+qnum);R=L+rng.randint(0,50)
        p,x,y=random_three_chains(rng,R,pnum,qnum,protected=L)
        long.append(analyze(p,x,y,initial_L=L))
    out['general_three_chain_cases']=len(rows)
    out['qualified_long_prefix_cases']=len(long)
    out['joint_XYZ_checks']=sum(v['R'] for v in rows+long)
    out['exact_prefix_and_split_indices']=sum(v['R']+1 for v in rows+long)
    out['monotone_labelled_swap_comparisons']=2*sum(v['R'] for v in rows+long)
    out['general_lambda_checks']=sum(v['general_lambda_checks'] for v in rows+long)
    out['front5_cases_without_entry_partner']=sum(v['no_entry_partner_front'] is not None for v in rows)
    out['terminal_long_prefix_cases']=sum(not v['initial']['has_entry_partner'] for v in long)
    out['sample_general_cases']=rows[:5];out['sample_qualified_cases']=long[:3]
    fam=[]
    for R in (32,40,64,96):
        for m in (0,1,3):
            for h,k in ((0,0),(8,16),(20,5),(31,31)):
                p,x,y=family(R,h,k,m);fam.append(analyze(p,x,y,initial_L=32))
    out['infinite_family_diagnostic_cases']=len(fam)
    out['family_sample']=fam[:4]
    p,x,y=family(256,8,16,1)
    big=analyze(p,x,y,initial_L=32,keep=True)
    assert not big['initial']['has_entry_partner'] and big['selected']['index']>32
    # x<y from a separate added-comparison count.
    ed=[(a,b) for b in range(len(p)) for a in range(len(p)) if p[b]>>a&1]
    big['entrance_x_before_y']=str(F(counter(closure(len(p),ed+[(x,y)]))(0),big['E']))
    assert not F(1,3)<=F(big['entrance_x_before_y'])<=F(2,3)
    grid_E,grid_T,grid_uv=independent_grid(256,8,16,1,big['selected']['index'])
    assert grid_E==big['E'] and F(grid_T,grid_E)==F(big['initial']['theta'])
    assert F(grid_uv[0],grid_E)==F(big['selected']['direction'])
    out['independent_large_grid']=dict(E=grid_E,prefix32_count=grid_T,
                                      selected_direction_counts=grid_uv)
    out['genuine_terminal_example']=big
    br=[]
    for R,h,k,m in ((2,0,1,0),(2,1,1,1),(3,1,2,1)):
        p,x,y=family(R,h,k,m);br.append(brute(p,x,y))
    out['independent_full_permutation_cases']=br
    # Arbitrarily long avoidance chain alone is insufficient: B_R disjoint C_(9R),C_(3R).
    guard=[]
    for R in range(1,7):
        ed=[]
        for a,b in ((0,R),(R,10*R),(10*R,13*R)):ed.extend(zip(range(a,b-1),range(a+1,b)))
        p=closure(13*R,ed);x,y=R,10*R
        v=analyze(p,x,y)
        assert v['selected'] is None and (R==1 or v['no_entry_partner_front']==1)
        guard.append(dict(R=R,E=v['E'],T1='1/13',b1_before_x='1/10',b1_before_y='1/4'))
    out['long_chain_guard_cases']=guard
    path=Path(__file__).resolve().parents[1]/'evidence'/'check_s95.json'
    path.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    summary={k:v for k,v in out.items() if isinstance(v,(int,str))}
    summary['terminal_example']={k:v for k,v in big.items() if k not in ('B','predecessor_masks','group','entrance_split','fixed_rank_histograms')}
    print(json.dumps(summary,ensure_ascii=False,indent=2))

if __name__=='__main__':main()
