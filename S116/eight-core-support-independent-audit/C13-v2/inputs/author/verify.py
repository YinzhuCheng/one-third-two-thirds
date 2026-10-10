#!/usr/bin/env python3
"""Independent labelled-element ideal DP; no occupancy code or imports."""
from functools import lru_cache
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parent

def count(up,w,edge=None):
    vertices=[(i,r) for i in range(8) for r in range(w[i])];index={v:k for k,v in enumerate(vertices)};pred=[0]*len(vertices)
    for k,(i,r) in enumerate(vertices):
        for l,(j,s) in enumerate(vertices):
            if (i==j and s<r) or up[j]>>i&1:pred[k]|=1<<l
    if edge:pred[index[tuple(edge[1])]]|=1<<index[tuple(edge[0])]
    full=(1<<len(vertices))-1
    @lru_cache(None)
    def f(mask):
        if mask==full:return 1
        return sum(f(mask|1<<k) for k in range(len(vertices)) if not mask>>k&1 and pred[k]&mask==pred[k])
    return f(0)

c=json.loads((ROOT/'certificate.json').read_text());up=c['strict_up_masks']
# Exact support exhaustion from original forced set and the two audited clauses.
allowed=[]
for mask in range(256):
    S={i for i in range(8) if mask>>i&1}
    if len(S)<=3 and {0,3}<=S and S&{1,2,4,6} and S&{4,5,6,7}:allowed.append(sorted(S))
assert allowed==[[0,3,4],[0,3,6]]
for case in c['cases']:
    S=case['support'];A=case['matrix'];H=case['inverse_times_four'];b=case['rhs']
    assert S in allowed and A==[[2,0,-1],[0,2,-1],[-1,-1,2]] and b==[2,2,1]
    assert all(x>=0 for row in H for x in row)
    for i in range(3):
        for j in range(3):assert sum(H[i][k]*A[k][j] for k in range(3))==4*(i==j)
    upper=[sum(H[i][k]*b[k] for k in range(3))//4 for i in range(3)];assert upper==[2,2,3]
    feasible=[]
    for a in range(2,upper[0]+1):
        for d in range(2,upper[1]+1):
            for e in range(2,upper[2]+1):
                x=[a,d,e]
                if all(sum(p*q for p,q in zip(row,x))<=r for row,r in zip(A,b)):feasible.append(x)
    assert feasible==[[2,2,2]]
    w=case['weights'];assert all(w[i]==(2 if i in S else 1) for i in range(8))
    p=case['pair'];Z=count(up,w);N=count(up,w,p);R=count(up,w,list(reversed(p)))
    assert Z==case['denominator']==2060 and N==case['numerator'] and N+R==Z
    assert Z<=3*N<=2*Z
print('PASS: all C13 inflations with at most three nonsingleton chains excluded; two independent exact certificates.')
