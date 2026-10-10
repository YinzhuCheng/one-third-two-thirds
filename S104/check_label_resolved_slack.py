#!/usr/bin/env python3
"""Exact finite checks for label_resolved_slack.txt; no external access."""
import itertools,json
from functools import lru_cache

def closure(pred):
    p=list(pred);n=len(p)
    for k in range(n):
        for v in range(n):
            if p[v]>>k&1:p[v]|=p[k]
    assert all(not(p[i]>>i&1) for i in range(n))
    return tuple(p)

def extensions(pred):
    n=len(pred);full=(1<<n)-1;out=[]
    def rec(used,order):
        if used==full:out.append(tuple(order));return
        for v in range(n):
            if not(used>>v&1) and not(pred[v]&~used):rec(used|1<<v,order+[v])
    rec(0,[]);return out

def counter(pred):
    @lru_cache(None)
    def count(mask):
        if not mask:return 1
        return sum(count(mask^(1<<v)) for v in range(len(pred)) if mask>>v&1 and not(pred[v]&mask))
    return count

def successors(pred,v):return {w for w in range(len(pred)) if pred[w]>>v&1}
def minimum(pred,vs):return {v for v in vs if not any(pred[v]>>w&1 for w in vs)}
def maximum(pred,vs):return {v for v in vs if not any(pred[w]>>v&1 for w in vs)}
def comparable(pred,a,b):return (pred[a]>>b&1) or (pred[b]>>a&1)

def check(pred,a,b,les):
    n=len(pred);full=(1<<n)-1
    N=[v for v in range(n) if v not in (a,b) and not comparable(pred,a,v) and not comparable(pred,b,v)]
    if any(not comparable(pred,x,y) for x,y in itertools.combinations(N,2)):return False
    # N is a chain in the original natural labelling.
    D=pred[a]|pred[b];q=list(pred);q[a]|=D;q[b]|=D;q=closure(q);ec=counter(q)
    C=minimum(pred,successors(pred,a)-successors(pred,b))
    T=maximum(pred,{v for v in range(n) if pred[b]>>v&1 and not(pred[a]>>v&1)})
    direct={c:0 for c in C};cond=0
    for L in les:
        pos={v:i for i,v in enumerate(L)}
        iscond=all(pos[v]<min(pos[a],pos[b]) for v in range(n) if D>>v&1)
        if iscond:cond+=1
        if pos[a]<pos[b] and iscond and any(pos[c]<pos[b] for c in C):
            direct[min(C,key=pos.get)]+=1
        for c in C:
            for d in T:
                lhs=int(pos[a]<pos[d] and pos[c]<pos[b])
                rhs=int(pos[c]<pos[d])+int(pos[a]<pos[d]<pos[c]<pos[b])
                assert lhs==rhs,(pred,a,b,c,d,L)
    assert ec(full)==cond
    weighted={c:0 for c in C};pref=D;f=0
    for j in range(len(N)+1):
        if j:pref|=1<<N[j-1]
        f+=ec(pref);back=full^pref
        for c in C:
            eligible=(q[c]&back)==(1<<a)
            tau=max([i+1 for i,v in enumerate(N) if q[c]>>v&1] or [0])
            assert eligible==(j>=tau)
            if eligible:weighted[c]+=f*ec(back^(1<<a)^(1<<c))
    assert direct==weighted,(pred,a,b,direct,weighted)
    return True

def example(edges,n,a,b):
    p=[0]*n
    for x,y in edges:p[y]|=1<<x
    p=closure(p);ec=counter(p);full=(1<<n)-1
    H=ec(full^(1<<a)^(1<<b));Ca=ec(full^(1<<a));Cb=ec(full^(1<<b));E=ec(full)
    rel={str(v):ec(full^(1<<a)^(1<<v)) for v in range(n) if p[v]==1<<a}
    probs={str(v):sum(L.index(v)<L.index(b) for L in extensions(p)) for v in map(int,rel)}
    return {'pred':p,'E':E,'C':[Ca,Cb],'V':[[Ca-H,H],[H,Cb-H]],'release_counts':rel,'comparison_counts_before_b':probs}

def main():
    sizes={};pairs=0;total=0
    for n in range(2,6):
        edges=list(itertools.combinations(range(n),2));ps=set()
        for mask in range(1<<len(edges)):
            p=[0]*n
            for i,(a,b) in enumerate(edges):
                if mask>>i&1:p[b]|=1<<a
            ps.add(closure(p))
        sizes[n]=len(ps);total+=len(ps)
        for p in sorted(ps):
            les=extensions(p)
            for a,b in itertools.permutations(range(n),2):
                if not comparable(p,a,b):pairs+=check(p,a,b,les)
    ex1=example([(0,1),(1,2),(1,3)],5,0,4)
    ex2=example([(0,1),(0,2),(1,3),(2,3)],5,0,4)
    assert ex1['E']==ex2['E']==10 and ex1['C']==ex2['C']==[8,2]
    assert ex1['V']==ex2['V']==[[6,2],[2,0]]
    assert ex1['release_counts']=={'1':6} and ex2['release_counts']=={'1':3,'2':3}
    assert ex2['comparison_counts_before_b']=={'1':5,'2':5}
    print(json.dumps({'status':'PASS','natural_posets_by_size':sizes,'posets':total,'ordered_pairs_checked':pairs,'example_I':ex1,'example_II':ex2},indent=2))
if __name__=='__main__':main()
