#!/usr/bin/env python3
"""Independent small oracle: edge-mask generator and set/matrix predicates.
No third-party software; exact integer extension counts. Finite tests are QA,
not substitutes for the all-weights proofs in README.md.
"""
import json, itertools, sys, time
from functools import lru_cache
from pathlib import Path
import catalogue as primary


def direct_posets(n):
    edges=list(itertools.combinations(range(n),2))
    for mask in range(1<<len(edges)):
        R={(a,b) for k,(a,b) in enumerate(edges) if mask>>k&1}
        if all((a,c) in R for a,b in R for bb,c in R if b==bb):yield R


def masks(n,R):return tuple(sum(1<<b for a,b in R if a==x) for x in range(n))
def chain(R,S):return all((a,b) in R or (b,a) in R for a,b in itertools.combinations(S,2))
def width(n,R):return max(len(S) for k in range(n+1) for S in itertools.combinations(range(n),k) if all((a,b) not in R and (b,a) not in R for a,b in itertools.combinations(S,2)))
def is_module(n,R,M):
    def sign(a,b):return 1 if (a,b) in R else -1 if (b,a) in R else 0
    return all(len({sign(x,y) for y in M})==1 for x in set(range(n))-M)
def module_witness(n,R):
    return next((set(M) for k in range(2,n) for M in itertools.combinations(range(n),k) if is_module(n,R,set(M))),None)
def predicates(n,R):
    down=[{x for x,y in R if y==a} for a in range(n)]
    up=[{y for x,y in R if x==a} for a in range(n)]
    good={(a,b) for a in range(n) for b in range(n) if a!=b and (a,b) not in R and (b,a) not in R and down[a]<=down[b] and chain(R,up[b]-up[a])}
    very={(a,b) for a,b in itertools.combinations(range(n),2) if down[a]==down[b] and chain(R,up[a]-up[b]) and chain(R,up[b]-up[a])}
    return good,very

def cyclic(n,E):
    # Independent Floyd-Warshall reachability oracle, versus DFS in primary.
    reach=[[int((a,b) in E) for b in range(n)] for a in range(n)]
    for k in range(n):
        for a in range(n):
            if reach[a][k]:
                for b in range(n):reach[a][b]|=reach[k][b]
    return any(reach[a][a] for a in range(n))

def twoport(n,R,good,dualgood):
    E={(2*a,2*a+1) for a in range(n)}
    E|={(2*a+i,2*b+j) for a,b in R for i in (0,1) for j in (0,1)}
    E|={(2*a,2*b) for a,b in good}
    E|={(2*b+1,2*a+1) for a,b in dualgood}
    return E

def inflate(n,R,w):
    V=[(a,k) for a in range(n) for k in range(w[a])];index={v:i for i,v in enumerate(V)}
    E={(i,j) for i,(a,k) in enumerate(V) for j,(b,l) in enumerate(V) if (a,b) in R or (a==b and k<l)}
    return V,E,index

def exact_pair_counts(n,R):
    pred=[sum(1<<a for a,b in R if b==x) for x in range(n)];end=(1<<n)-1
    @lru_cache(None)
    def tails(M):
        if M==end:return 1
        return sum(tails(M|(1<<a)) for a in range(n) if not M>>a&1 and pred[a]&~M==0)
    total=tails(0);prefix=[0]*(1<<n);prefix[0]=1;pair=[[0]*n for _ in range(n)]
    for M in range(1<<n):
        if not prefix[M]:continue
        for a in range(n):
            if M>>a&1 or pred[a]&~M:continue
            N=M|(1<<a);prefix[N]+=prefix[M];ways=prefix[M]*tails(N)
            for b in range(n):
                if b!=a and not M>>b&1:pair[a][b]+=ways
    assert prefix[end]==total
    return total,pair


def run():
    begin=time.monotonic();counts={'oracle_posets':0,'weighted_inflations':0,'very_good_lifts':0,'forced_good_lifts':0,'exact_balanced_existence_checks':0,'width_preservation_checks':0};by_n={}
    for n in range(1,7):
        oracle=set()
        for R in direct_posets(n):
            rows=masks(n,R);oracle.add(rows);counts['oracle_posets']+=1
            assert bool(primary.proper_module(rows))==bool(module_witness(n,R)),('prime',rows)
            assert primary.width(rows)==width(n,R),('width',rows)
            good,very=predicates(n,R);DR={(b,a) for a,b in R};dg,dv=predicates(n,DR)
            assert set(primary.forced_good_edges(rows))==good
            assert set(primary.very_good_pairs(rows))==very
            assert set(primary.forced_good_edges(primary.dual(rows)))==dg
            assert set(primary.very_good_pairs(primary.dual(rows)))==dv
            assert bool(primary.directed_cycle(primary.forced_graph(rows)))==cyclic(n,R|good)
            assert bool(primary.directed_cycle(primary.forced_graph(primary.dual(rows))))==cyclic(n,DR|dg)
            E=twoport(n,R,good,dg)
            assert primary.two_port_graph(rows)==masks(2*n,E)
            assert bool(primary.directed_cycle(primary.two_port_graph(rows)))==cyclic(2*n,E)
            if n>4:continue
            for w in itertools.product((1,2),repeat=n):
                V,P,index=inflate(n,R,w);N=len(V);counts['weighted_inflations']+=1
                pg,pv=predicates(N,P);pdg,pdv=predicates(N,{(b,a) for a,b in P})
                assert width(N,P)==width(n,R);counts['width_preservation_checks']+=1
                for a,b in good:
                    assert (index[a,0],index[b,0]) in pg;counts['forced_good_lifts']+=1
                for a,b in dg:
                    assert (index[a,w[a]-1],index[b,w[b]-1]) in pdg;counts['forced_good_lifts']+=1
                for a,b in very:
                    assert tuple(sorted((index[a,0],index[b,0]))) in pv;counts['very_good_lifts']+=1
                for a,b in dv:
                    assert tuple(sorted((index[a,w[a]-1],index[b,w[b]-1]))) in pdv;counts['very_good_lifts']+=1
                total,pairs=exact_pair_counts(N,P)
                # Small theorem-side checks, using exact integers only.
                if len(P)<N*(N-1)//2:
                    assert any(total<=3*pairs[a][b]<=2*total for a in range(N) for b in range(a+1,N) if (a,b) not in P and (b,a) not in P)
                    counts['exact_balanced_existence_checks']+=1
        primary_set=set(primary.naturally_labelled(n));assert primary_set==oracle
        by_n[n]=len(oracle);print('independent n',n,len(oracle),flush=True)
    result={'status':'PASS','independent_generator_max_n':6,'all_positive_weights_in_test_grid':[1,2],'weight_grid_max_core_n':4,'independent_natural_counts':by_n,'checks':counts,'elapsed_seconds':round(time.monotonic()-begin,3),'limitations':'Finite checks supplement but do not prove the universal structural theorems. Independent oracle uses no primary predicate except in assertions.'}
    Path(__file__).with_name('independent_test_results.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))

if __name__=='__main__':run()
