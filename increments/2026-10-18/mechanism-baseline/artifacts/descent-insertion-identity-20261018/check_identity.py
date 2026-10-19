#!/usr/bin/env python3
"""Small exact controls of insertion identities, not a descent search."""
import itertools,json
from fractions import Fraction
from pathlib import Path


def closure(n, edges):
    r=set(edges)
    for k in range(n):
        for i in range(n):
            if (i,k) in r:
                for j in range(n):
                    if (k,j) in r:r.add((i,j))
    return frozenset(r)

def extensions(V,r):
    return [p for p in itertools.permutations(V) if all(p.index(a)<p.index(b) for a,b in r if a in V and b in V)]

def check_one(n,r,x):
    V=tuple(i for i in range(n) if i!=x)
    D={i for i in V if (i,x) in r};U={i for i in V if (x,i) in r};I=set(V)-D-U
    ds=[d for d in D if not any((d,d2) in r for d2 in D)] if D else [None]
    us=[u for u in U if not any((u2,u) in r for u2 in U)] if U else [None]
    alpha=1+min(sum((d is None or (d,z) in r) and (u is None or (z,u) in r) for z in I) for d in ds for u in us)
    beta=len(I)+1
    Ls=extensions(V,r); weights=[]
    for L in Ls:
        pos={z:j+1 for j,z in enumerate(L)}
        a=max([pos[z] for z in D],default=0)
        b=min([pos[z] for z in U],default=n)
        weights.append(b-a)
    assert min(weights)==alpha,(n,r,x,weights,alpha)
    assert max(weights)==beta,(n,r,x,weights,beta)
    slab=all((d,z) in r for d in D for z in I) and all((z,u) in r for z in I for u in U)
    assert (len(set(weights))==1)==slab,(n,r,x,weights,slab)
    Ps=extensions(tuple(range(n)),r)
    assert sum(weights)==len(Ps)
    for u,v in itertools.combinations(V,2):
        if (u,v) in r or (v,u) in r:continue
        p=Fraction(sum(L.index(u)<L.index(v) for L in Ps),len(Ps))
        q=Fraction(sum(L.index(u)<L.index(v) for L in Ls),len(Ls))
        ew=Fraction(sum(weights),len(weights))
        eiw=Fraction(sum(w for L,w in zip(Ls,weights) if L.index(u)<L.index(v)),len(Ls))
        assert p-q==(eiw-q*ew)/ew
    return len(Ls)

counts=[];cases=0
for n in range(1,6):
    possible=list(itertools.combinations(range(n),2));seen=set()
    for mask in range(1<<len(possible)):
        r=closure(n,[e for j,e in enumerate(possible) if mask>>j&1])
        if r in seen:continue
        seen.add(r)
        for x in range(n):
            check_one(n,r,x);cases+=1
    counts.append({'n':n,'distinct_naturally_labelled_posets':len(seen)})

# Autonomous chain example: d<c1<c2 and b isolated; delete c1.
names=['d','c1','c2','b'];r=closure(4,[(0,1),(1,2)]);x=1
V=(0,2,3);Ls=extensions(V,r)
rows=[]
for L in Ls:
    pos={z:j+1 for j,z in enumerate(L)};w=pos[2]-pos[0]
    rows.append({'L':' '.join(names[z] for z in L),'w':w,'b_before_d':L.index(3)<L.index(0)})
q=Fraction(sum(z['b_before_d'] for z in rows),len(rows));ew=Fraction(sum(z['w'] for z in rows),len(rows));eiw=Fraction(sum(z['w'] for z in rows if z['b_before_d']),len(rows));cov=eiw-q*ew
out={'purpose':'Exact small controls for algebraic identities and sharp relation-only bounds; no global descent or conjecture search.','counts':counts,'deletion_cases':cases,'all_checks_passed':True,'negative_covariance_example':{'Q_extensions':rows,'p_Q':str(q),'E_Q_w':str(ew),'covariance':str(cov),'p_P':str(q+cov/ew)}}
path=Path(__file__).with_name('CHECKS.json');path.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n');print(json.dumps(out,ensure_ascii=False,indent=2))
