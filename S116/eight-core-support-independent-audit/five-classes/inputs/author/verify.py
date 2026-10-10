#!/usr/bin/env python3
"""Independent labelled-ideal recurrence and polynomial certificate verifier.
No imports from author occupancy or outside-fiber implementations.
"""
from functools import lru_cache
from fractions import Fraction
from math import comb
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parent
c=json.loads((ROOT/'certificate.json').read_text())
cores={q['class_id']:q for q in c['cores']}

def count(up,w,edge=None):
    V=[(i,r) for i in range(8) for r in range(w[i])];idx={v:k for k,v in enumerate(V)}
    pred=[sum(1<<l for l,(j,s) in enumerate(V) if (i==j and s<r) or up[j]>>i&1) for i,r in V]
    if edge:pred[idx[edge[1]]]|=1<<idx[edge[0]]
    full=(1<<len(V))-1
    @lru_cache(None)
    def f(mask):
        if mask==full:return 1
        total=0
        for k in range(len(V)):
            if not mask>>k&1 and (pred[k]&mask)==pred[k]:total+=f(mask|1<<k)
        return total
    return f(0)

def ev(a,t):return sum(x*comb(t+h,h) for h,x in enumerate(a))
def shift(a,k):
    v=[ev(a,k+j) for j in range(8)];out=[]
    while v:out.append(v[0]);v=[v[j+1]-v[j] for j in range(len(v)-1)]
    return out

def witness(case):
    up=cores[case['class_id']]['strict_up_masks'];w=case['weights'];a,b=map(tuple,case['pair'])
    assert a[0]!=b[0] and not(up[a[0]]>>b[0]&1) and not(up[b[0]]>>a[0]&1)
    Z=count(up,w);N=count(up,w,(a,b));R=count(up,w,(b,a))
    assert Z==case['denominator'] and N==case['numerator'] and N+R==Z and Z<=3*N<=2*Z

def polycounts(cls,i,Z,checks):
    # Combinatorial derivation in THEOREM.md proves degree at most seven.
    # Eight distinct positive evaluations certify each stored polynomial identity.
    assert len(Z)==8
    for t in range(1,9):
        w=[1]*8;w[i]=t;z=count(cores[cls]['strict_up_masks'],w);assert z==ev(Z,t)
        for pair,P in checks:
            a,sa,b,sb=pair;a=(a,w[a]-1 if sa else 0);b=(b,w[b]-1 if sb else 0)
            assert count(cores[cls]['strict_up_masks'],w,(a,b))==ev(P,t)
            assert count(cores[cls]['strict_up_masks'],w,(b,a))+ev(P,t)==z

covered=set();evaluations=0
for x in c['polynomial_certificates']:
    cls=x['class_id'];i=x['variable'];assert (cls,i) not in covered;covered.add((cls,i));Z=x['denominator_coefficients'];P=x['numerator_coefficients'];K=x['tail_start']
    up=cores[cls]['strict_up_masks'];a,sa,b,sb=x['pair'];assert a!=b and not(up[a]>>b&1) and not(up[b]>>a&1)
    polycounts(cls,i,Z,[(x['pair'],P)]);evaluations+=8
    A=shift([3*p-z for p,z in zip(P,Z)],K);B=shift([2*z-3*p for p,z in zip(P,Z)],K)
    assert A==x['lower_balance_newton_coefficients'] and B==x['upper_balance_newton_coefficients'] and all(v>=0 for v in A+B)
    assert [f['weight'] for f in x['finite_prefix']]==list(range(2,K))
    for f in x['finite_prefix']:
        t=f['weight'];w=[1]*8;w[i]=t;a,sa,b,sb=f['pair']
        witness(dict(class_id=cls,weights=w,pair=[[a,w[a]-1 if sa else 0],[b,w[b]-1 if sb else 0]],numerator=f['numerator'],denominator=f['denominator']))
for x in c['bounded_certificates']:
    cls=x['class_id'];i=x['variable'];assert i==6 and (cls,i) not in covered;covered.add((cls,i));up=cores[cls]['strict_up_masks']
    I=[j for j in range(8) if j!=i and not(up[i]>>j&1) and not(up[j]>>i&1)];assert I==x['incomparable_indices'] and len(I)==5
    U=[{j for j in range(8) if row>>j&1} for row in up];D=[{j for j in range(8) if k in U[j]} for k in range(8)]
    chain=lambda S:all(a in U[b] or b in U[a] for a in S for b in S if a!=b)
    assert any(D[i]==D[j] and chain(U[i]-U[j]) or U[i]==U[j] and chain(D[i]-D[j]) for j in I)
    assert x['integer_upper_bound']==2 and x['case']['weights']==[2 if j==i else 1 for j in range(8)];witness(x['case'])
x=c['long_chain_certificate'];cls=x['class_id'];i=x['variable'];assert (cls,i)==('C09',1) and (cls,i) not in covered;covered.add((cls,i));up=cores[cls]['strict_up_masks'];j=x['comparison_vertex']
I=[k for k in range(8) if k!=i and not(up[i]>>k&1) and not(up[k]>>i&1)];assert I==x['incomparable_indices'] and j in I
M=len(I);K=x['tail_start'];assert M==x['incomparable_outside_mass']==5 and K==10 and K>=2*M
Z=x['denominator_coefficients'];P=x['bottom_numerator_coefficients'];T=x['top_numerator_coefficients'];polycounts(cls,i,Z,[([i,0,j,0],P),([i,1,j,0],T)]);evaluations+=8
A=shift([3*p-2*z for p,z in zip(P,Z)],K);B=shift([z-3*t for z,t in zip(Z,T)],K)
assert A==x['bottom_minus_two_thirds_newton'] and B==x['one_third_minus_top_newton'] and all(v>=0 for v in A+B)
assert [p['weights'][i] for p in x['finite_prefix']]==list(range(2,K))
for p in x['finite_prefix']:witness(p)
assert covered=={(cls,i) for cls in cores for i in range(8)} and len(covered)==40
assert {p['class_id'] for p in c['zero_support_certificates']}==set(cores)
for p in c['zero_support_certificates']:assert p['weights']==[1]*8;witness(p)
print('PASS: 40 exact-support families covered, including 36 fixed-pair polynomial certificates, three inequality-bounded families, and one long-chain rank-crossing family. Five all-singleton cases also recounted. Independent polynomial evaluation grids:',evaluations)
