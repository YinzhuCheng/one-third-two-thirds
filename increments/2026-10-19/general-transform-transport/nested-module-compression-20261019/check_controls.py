#!/usr/bin/env python3
"""Eight preselected exact controls; no family or poset sweep."""
from fractions import Fraction as F
from itertools import permutations
from math import comb, prod
import json
from pathlib import Path


def extensions(labels, edges):
    labels = tuple(labels)
    preds = {x: {a for a,b in edges if b == x} for x in labels}
    out = []
    def rec(order, rest):
        if not rest:
            out.append(tuple(order)); return
        used = set(order)
        for x in sorted(rest):
            if preds[x] <= used:
                rec(order+[x], rest-{x})
    rec([], set(labels))
    return out


def rank(A):
    if not A: return 0
    A = [list(map(F,r)) for r in A]
    p = 0
    for c in range(len(A[0])):
        j = next((j for j in range(p,len(A)) if A[j][c]), None)
        if j is None: continue
        A[p],A[j] = A[j],A[p]
        z=A[p][c]; A[p]=[v/z for v in A[p]]
        for j in range(len(A)):
            if j != p:
                z=A[j][c]; A[j]=[a-z*b for a,b in zip(A[j],A[p])]
        p+=1
        if p == len(A): break
    return p


def nullvector(A):
    A = [list(map(F,r)) for r in A]
    n=len(A[0]); p=0; piv=[]
    for c in range(n):
        j=next((j for j in range(p,len(A)) if A[j][c]),None)
        if j is None: continue
        A[p],A[j]=A[j],A[p]
        z=A[p][c]; A[p]=[v/z for v in A[p]]
        for j in range(len(A)):
            if j != p:
                z=A[j][c]; A[j]=[a-z*b for a,b in zip(A[j],A[p])]
        piv.append(c); p+=1
        if p==len(A): break
    free=next(c for c in range(n) if c not in piv)
    z=[F(0)]*n; z[free]=F(1)
    for j,c in enumerate(piv): z[c]=-A[j][free]
    return z


def sparse_mix(features, weights):
    """Remove affine dependences exactly, preserving nonnegative weights."""
    weights=list(map(F,weights)); original_weights=list(weights)
    support=[i for i,w in enumerate(weights) if w]
    while True:
        A=[[F(1) for _ in support]]
        A += [[F(features[i][a]) for i in support] for a in range(len(features[0]))]
        if rank(A)==len(support): break
        z=nullvector(A)
        eps=min(weights[i]/v for i,v in zip(support,z) if v>0)
        for i,v in zip(support,z): weights[i]-=eps*v
        support=[i for i in support if weights[i]]
    assert all(w>=0 for w in weights) and sum(weights)==1
    for a in range(len(features[0])):
        assert sum(weights[i]*features[i][a] for i in range(len(weights))) == sum(w*f[a] for w,f in zip(original_weights,features))
    return [(i,weights[i]) for i in support]


def shuffle_kernel(m,h):
    L=extensions([f'a{i}' for i in range(m)]+[f'b{j}' for j in range(h)],
                 [(f'a{i}',f'a{i+1}') for i in range(m-1)]+[(f'b{j}',f'b{j+1}') for j in range(h-1)])
    return [[F(sum(w.index(f'b{j}')<w.index(f'a{i}') for w in L),len(L)) for i in range(m)] for j in range(h)]


def finite_difference(v, k):
    for _ in range(k): v=[b-a for a,b in zip(v,v[1:])]
    return v


def matmul(A,B):
    return [[sum(a*b for a,b in zip(row,col)) for col in zip(*B)] for row in A]


def transfer(words,label,m):
    n=len(words[0]); T=[[F(0) for _ in range(m)] for _ in range(n)]
    for w in words:
        seen=0
        for t,x in enumerate(w):
            if x==label:
                T[t][seen]+=F(1,len(words)); seen+=1
    return T


def labelled_skeleton(sizes, edges):
    states=[]
    def rec(w,c):
        if all(c[x]==sizes[x] for x in sizes): states.append(tuple(w)); return
        for x in sorted(sizes):
            if c[x]<sizes[x] and all(c[a]==sizes[a] for a,b in edges if b==x):
                c[x]+=1; rec(w+[x],c); c[x]-=1
    rec([],{x:0 for x in sizes}); return states


R=[]
for m,h in [(6,2),(6,5),(3,5)]:
    K=shuffle_kernel(m,h)
    d=rank([[F(1)]*m]+K)-1
    assert d==min(h,m-1)
    assert all(all(v==0 for v in finite_difference(row,h+1)) for row in K)
    R.append({'control':f'disjoint_chain_m{m}_h{h}','d':d,'kernels_y_before_i':K})

# A genuinely constrained environment: D={d}, U={u}, I={a,b,c}.
m=4
outside=['a','b','c','d','u']
edges=[('d','u'),('d','a'),('b','u'),('a','c')]
full_edges=edges+[(f'x{i}',f'x{i+1}') for i in range(m-1)]+[('d','x0'),('x3','u')]
W=extensions(outside+[f'x{i}' for i in range(m)],full_edges)
K=[[F(sum(w.index(y)<w.index(f'x{i}') for w in W),len(W)) for i in range(m)] for y in ['a','b','c']]
assert all(all(v==0 for v in finite_difference(row,4)) for row in K)
ext=extensions(outside,edges)
assert len(W)==sum(comb(m+w.index('u')-w.index('d')-1,m) for w in ext)
def rising(i,r): return prod(range(i,i+r))
def chain_tail(m,q,t,i):
    return sum(F((-1)**(r-t)*comb(r-1,t-1)*comb(q,r)*rising(i,r),rising(m+1,r)) for r in range(t,q+1))
for yi,y in enumerate(['a','b','c']):
    for i in range(1,m+1):
        total=F(0)
        for w in ext:
            a=w.index('d')+1; b=w.index('u')+1; q=b-a-1
            pos=w.index(y)+1
            conditional=F(1) if pos<=a else F(0) if pos>=b else chain_tail(m,q,pos-a,i)
            total+=comb(m+q,q)*conditional
        assert K[yi][i-1]==total/len(W)
assert all(all(v==0 for v in finite_difference(row,3)) for row in K)
coeffs=[(0,F(55,161),F(-4,161)),(F(21,161),F(28,161),0),(0,0,F(4,161))]
for row,cs in zip(K,coeffs):
    assert row==[cs[0]+cs[1]*i+cs[2]*i*(i+1) for i in range(1,m+1)]
R.append({'control':'constrained_environment','extensions':len(W),'d':rank([[F(1)]*m]+K)-1,'kernels_y_before_i':K,'basis':['1','i','i*(i+1)'],'reconstruction_coefficients':coeffs})

# Nested law: B=C2 disjoint singleton; A=(B<z) disjoint C2.
WB=labelled_skeleton({'X':2,'y':1},[])
WA=labelled_skeleton({'B':3,'z':1,'E':2},[('B','z')])
TB=transfer(WB,'X',2); TA=transfer(WA,'B',3)
L=extensions(['x0','x1','y','z','e0','e1'],[('x0','x1'),('x0','z'),('x1','z'),('y','z'),('e0','e1')])
direct=[[F(sum(w[t]==x for w in L),len(L)) for x in ['x0','x1']] for t in range(6)]
assert matmul(TA,TB)==direct
assert len(L)==len(WA)*len(WB)
R.append({'control':'nested_transfer','extensions':len(L),'T_A_from_B':TA,'T_B_from_X':TB,'composed_equals_direct':True})

# One marked element, exact two-moment interface on six ranks.
features=[(i,i*(i+1)) for i in range(1,7)]
weights=[F(1,6)]*6
mix=sparse_mix(features,weights)
assert len(mix)<=3
assert all(sum(w*features[i][a] for i,w in mix)==sum(w*f[a] for w,f in zip(weights,features)) for a in range(2))
R.append({'control':'single_element_sparse_moments','support':[(i+1,w) for i,w in mix]})

# A joint interface built only from actual LE of the four-point antichain.
LE=list(permutations('abcd')); features=[tuple(w.index(x)+1 for x in 'abcd') for w in LE]
weights=[F(1,len(LE))]*len(LE); mix=sparse_mix(features,weights)
assert len(mix)<=4
assert all(sum(w*features[i][a] for i,w in mix)==F(5,2) for a in range(4))
changes=[]
for x,y in [('a','b'),('a','c'),('a','d'),('b','c'),('b','d'),('c','d')]:
    p=sum(w for i,w in mix if LE[i].index(x)<LE[i].index(y))
    if p!=F(1,2): changes.append((x,y,p))
R.append({'control':'joint_weighted_actual_extensions','support':[(''.join(LE[i]),w) for i,w in mix],'internal_pair_changes':changes})

# With no nonconstant probes, one actual extension is a valid interface,
# but its weighted-law balance need not be the true uniform-LE balance.
assert sparse_mix([(),()],[F(1,2),F(1,2)]) in [[(0,F(1))],[(1,F(1))]]
R.append({'control':'zero_probe_delta_obstruction','antichain_2_uniform_delta':F(1,2),'one_state_weighted_delta':F(0)})

def clean(x):
    if isinstance(x,F): return str(x)
    if isinstance(x,dict): return {k:clean(v) for k,v in x.items()}
    if isinstance(x,(list,tuple)): return [clean(v) for v in x]
    return x

assert len(R)==8
out=Path(__file__).with_name('controls.json'); out.write_text(json.dumps(clean(R),ensure_ascii=False,indent=2)+'\n')
print(json.dumps(clean(R),ensure_ascii=False,indent=2))
