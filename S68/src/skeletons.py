"""Exact positive kernels for chain substitutions. Python standard library only.
All masks describe the strict, transitively closed template order.
First-copy events, not arbitrary unmarked internal copies, are recorded.
"""
from __future__ import annotations
from functools import lru_cache
from itertools import product, combinations
from collections import defaultdict
from math import comb

def check(pred: tuple[int,...]) -> None:
    n=len(pred);mask=(1<<n)-1
    for i,p in enumerate(pred):
        if p & ~mask or p>>i&1: raise ValueError('invalid predecessor mask')
        for j in range(n):
            if p>>j&1 and pred[j]&~p: raise ValueError('order is not transitive')

def successors(pred):
    return tuple(sum(1<<j for j in range(len(pred)) if pred[j]>>i&1) for i in range(len(pred)))

def first_appearance_counts(pred, lengths):
    """Coefficient of the first-appearance rational kernel and event subkernels.
    Deliberately permits introducing a successor before a predecessor's quota is
    filled; those paths cannot be accepted and contribute zero. This differs from
    the ordinary expanded-poset recurrence below.
    """
    pred=tuple(pred);lengths=tuple(lengths);check(pred);n=len(pred)
    if len(lengths)!=n or any(m<1 for m in lengths):raise ValueError('positive lengths required')
    succ=successors(pred);pairs=tuple(combinations(range(n),2))
    @lru_cache(None)
    def go(t):
        if t==lengths:return (1,)+(0,)*len(pairs)
        I=sum(1<<i for i,x in enumerate(t) if x)
        ans=[0]*(len(pairs)+1)
        for i in range(n):
            if t[i]==lengths[i] or succ[i]&I:continue
            new=t[i]==0
            if new and pred[i]&~I:continue
            z=list(t);z[i]+=1;v=go(tuple(z))
            for j,w in enumerate(v):ans[j]+=w
            if new:
                for j,(a,b) in enumerate(pairs):
                    if a==i and not (I>>b&1):ans[j+1]+=v[0]
        return tuple(ans)
    return go((0,)*n)

def expanded_counts(pred,lengths):
    """Independent order-ideal recurrence on individually labelled copies."""
    pred=tuple(pred);lengths=tuple(lengths);check(pred);n=len(pred)
    offsets=[];r=0
    for m in lengths:offsets.append(r);r+=m
    masks=[]
    for i,m in enumerate(lengths):
        external=sum(((1<<lengths[j])-1)<<offsets[j] for j in range(n) if pred[i]>>j&1)
        for k in range(m):masks.append(external|(((1<<k)-1)<<offsets[i]))
    pairs=tuple(combinations(range(n),2));allmask=(1<<r)-1
    @lru_cache(None)
    def go(I):
        if I==allmask:return (1,)+(0,)*len(pairs)
        ans=[0]*(len(pairs)+1)
        for x,p in enumerate(masks):
            if I>>x&1 or p&~I:continue
            v=go(I|1<<x)
            for j,w in enumerate(v):ans[j]+=w
            for j,(a,b) in enumerate(pairs):
                if x==offsets[a] and not (I>>offsets[b]&1):ans[j+1]+=v[0]
        return tuple(ans)
    return go(0)

def run_coefficients(pred, variable):
    """Return alpha -> [skeleton count, first-copy event counts].
    variable must be a chain; all other modules have length one.
    The basis is product binom(m_i-1, alpha_i). No polynomial extrapolation.
    """
    pred=tuple(pred);check(pred);n=len(pred);S=tuple(variable);V=set(S)
    if len(V)!=len(S) or any(i<0 or i>=n for i in S):raise ValueError('bad variable set')
    if any(not(pred[a]>>b&1 or pred[b]>>a&1) for a,b in combinations(S,2)):
        raise ValueError('variable modules must form a chain')
    succ=successors(pred);pairs=tuple(combinations(range(n),2));out=defaultdict(lambda:[0]*(1+len(pairs)))
    def dfs(word,seen,runs):
        if seen==(1<<n)-1:
            # Accept here, but permit one final separated maximal-variable run;
            # e.g. A,x,A must not be lost merely because A,x already saw all labels.
            alpha=tuple(runs[i]-1 for i in range(len(S)))
            assert min(alpha,default=0)>=0 and sum(alpha)<=n-len(S)
            a=out[alpha];a[0]+=1;pos={x:word.index(x) for x in range(n)}
            for j,(x,y) in enumerate(pairs):a[j+1]+=pos[x]<pos[y]
        for i in range(n):
            used=bool(seen>>i&1)
            if succ[i]&seen or pred[i]&~seen:continue
            if used and (i not in V or word[-1]==i):continue
            z=list(runs)
            if i in V:z[S.index(i)]+=1
            dfs(word+(i,),seen|1<<i,tuple(z))
    dfs((),0,(0,)*len(S))
    return dict(out)

def evaluate_run(coeff,lengths):
    ans=[0]*len(next(iter(coeff.values())))
    for alpha,row in coeff.items():
        w=1
        for a,m in zip(alpha,lengths):w*=comb(m-1,a) if m-1>=a else 0
        for j,x in enumerate(row):ans[j]+=w*x
    return tuple(ans)

def natural_posets(n):
    """Canonical predecessor-ideal recursion; each natural-labelled order once."""
    if n==0:yield ();return
    for pred in natural_posets(n-1):
        for I in range(1<<(n-1)):
            if all(not(I>>j&1) or not(pred[j]&~I) for j in range(n-1)):
                yield pred+(I,)

def first_skeleton_list(pred):
    """List (first occurrence order, maximal sets in successive ideals)."""
    succ=successors(pred);n=len(pred)
    def rec(order,I,sets):
        if len(order)==n:yield order,sets;return
        for i in range(n):
            if I>>i&1 or pred[i]&~I:continue
            J=I|1<<i
            A=tuple(j for j in range(n) if J>>j&1 and not(succ[j]&J))
            yield from rec(order+(i,),J,sets+(A,))
    return list(rec((),0,()))
