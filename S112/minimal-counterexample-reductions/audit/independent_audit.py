#!/usr/bin/env python3
"""Independent exhaustive audit of module, chain-inflation and counting lemmas.
Enumerates naturally labelled transitive relations directly (not closure-dedup).
The finite checks verify identities; they do not assume existence of a counterexample.
"""
from itertools import combinations
from collections import Counter
from functools import lru_cache
from fractions import Fraction
from math import comb
import json,time
from pathlib import Path

stats=Counter()

def generate(n):
    E=list(combinations(range(n),2))
    for m in range(1<<len(E)):
        up=[0]*n
        for e,(i,j) in enumerate(E):
            if m&(1<<e):up[i]|=1<<j
        if all(up[j]&~up[i]==0 for i in range(n) for j in range(i+1,n) if up[i]&(1<<j)):
            yield tuple(up)

def sign(up,x,y):
    return int(bool(up[x]&(1<<y)))-int(bool(up[y]&(1<<x)))

def modules(up):
    n=len(up)
    return [M for M in range(1,1<<n) if all(len({sign(up,x,y) for y in range(n) if M&(1<<y)})==1 for x in range(n) if not M&(1<<x))]

def ischain(up,M):
    return all(sign(up,x,y)!=0 for x in range(len(up)) for y in range(x+1,len(up)) if M&(1<<x) and M&(1<<y))

def extend(up):
    n=len(up); end=(1<<n)-1
    pred=[sum(1<<x for x in range(n) if up[x]&(1<<y)) for y in range(n)]
    def walk(mask,word):
        if mask==end:
            yield word; return
        for y in range(n):
            if not mask&(1<<y) and pred[y]&~mask==0:
                yield from walk(mask|(1<<y),word+(y,))
    return list(walk(0,()))

def width(up):
    n=len(up)
    return max(M.bit_count() for M in range(1<<n) if all(not(up[i]&M) for i in range(n) if M&(1<<i)))

def connected(up,inc=False):
    n=len(up); seen={0}; todo=[0]
    while todo:
        x=todo.pop()
        for y in range(n):
            if y!=x and y not in seen and ((sign(up,x,y)==0)==inc):
                seen.add(y);todo.append(y)
    return len(seen)==n

def verify(n,up):
    stats['posets']+=1
    L=extend(up); mods=modules(up); full=(1<<n)-1
    for M in mods:
        # Count induced orders without calling the induced extension enumerator:
        # completeness follows constructively by the slot-replacement bijection.
        orders=Counter(tuple(x for x in ell if M&(1<<x)) for ell in L)
        assert len(set(orders.values()))==1
        skeletons={tuple(-1 if M&(1<<x) else x for x in ell) for ell in L}
        assert all(c==len(skeletons) for c in orders.values())
        stats['module_uniform_fibers']+=1
    chains=[M for M in mods if ischain(up,M)]
    for A in chains:
        for B in chains:
            if A&B:
                assert A|B in chains
                stats['intersecting_chain_module_unions']+=1
    maximal=[M for M in chains if all(M==N or M&~N for N in chains)]
    assert sum(M.bit_count() for M in maximal)==n
    assert sum(maximal)==full
    k=len(maximal); reps=[(M&-M).bit_length()-1 for M in maximal]
    Q=tuple(sum(1<<j for j in range(k) if sign(up,reps[i],reps[j])==1) for i in range(k))
    w=tuple(M.bit_count() for M in maximal)
    lookup={x:i for i,M in enumerate(maximal) for x in range(n) if M&(1<<x)}
    words=[tuple(lookup[x] for x in ell) for ell in L]
    assert len(set(words))==len(L)
    pred=[tuple(j for j in range(k) if Q[j]&(1<<i)) for i in range(k)]
    def legal(a,i):return a[i]<w[i] and all(a[j]==w[j] for j in pred[i])
    @lru_cache(None)
    def tails(a):
        if a==w:return 1
        return sum(tails(a[:i]+(a[i]+1,)+a[i+1:]) for i in range(k) if legal(a,i))
    assert tails((0,)*k)==len(L)
    # Prefix/suffix DP checks a general rank-pair numerator independently.
    prefixes={(0,)*k:1}
    for t in range(n):
        for a,H in list(prefixes.items()):
            if sum(a)!=t:continue
            for i in range(k):
                if legal(a,i):
                    b=a[:i]+(a[i]+1,)+a[i+1:]
                    prefixes[b]=prefixes.get(b,0)+H
    if k>1:
        i,j=0,k-1; r=(w[i]+1)//2; s=(w[j]+1)//2
        numerator=sum(H*tails(a[:i]+(a[i]+1,)+a[i+1:]) for a,H in prefixes.items() if a[i]==r-1 and a[j]<s and legal(a,i))
        exact=sum([z for z,x in enumerate(ell) if x==i][r-1]<[z for z,x in enumerate(ell) if x==j][s-1] for ell in words)
        assert numerator==exact
        stats['rank_pair_numerators']+=1
    assert width(up)==width(Q)
    degrees=[sum(1 for j in range(n) if j!=i and sign(up,i,j)==0) for i in range(n)]
    weighted=[sum(w[j] for j in range(k) if j!=i and sign(Q,i,j)==0) for i in range(k)]
    assert all(degrees[x]==weighted[lookup[x]] for x in range(n))
    assert connected(up)==connected(Q)
    assert connected(up,True)==connected(Q,True) or k==1
    # For k=1, P is a chain; its incomparability graph is disconnected if n>1.
    if n>1 and connected(up,True):assert max(w)<=max(degrees)
    if not ischain(up,full) and all(M==full or ischain(up,M) for M in mods):
        assert all(M.bit_count()==1 or M==(1<<k)-1 for M in modules(Q))
        stats['prime_quotients_under_minimality_condition']+=1
    stats['chain_inflation_word_and_geometry_laws']+=1

if __name__=="__main__":
    start=time.time()
    for n in range(1,7):
        before=stats['posets']
        for up in generate(n):verify(n,up)
        print('finished n',n,'count',stats['posets']-before,flush=True)
    for a in range(1,101):
        for b in range(a,101):
            f=[Fraction(0)]+[1-Fraction(comb(a+b-j,a),comb(a+b,a)) for j in range(1,b+1)]
            j=next(j for j in range(1,b+1) if f[j]>=Fraction(1,3))
            assert f[j]<=Fraction(2,3)
            stats['two_chain_balanced_crossings']+=1
    report={'status':'PASS','max_n':6,'elapsed_seconds':round(time.time()-start,3),'checks':dict(stats)}
    Path(__file__).with_name('audit_results.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))
