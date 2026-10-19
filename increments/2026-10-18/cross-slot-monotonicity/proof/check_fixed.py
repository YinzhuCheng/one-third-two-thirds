#!/usr/bin/env python3
"""One fixed actual example; exact enumeration and ideal DP, no parameter search."""
from fractions import Fraction
from itertools import permutations
import json
from pathlib import Path

OUT = Path(__file__).parent
D = ['a', 'd', 'b', 'c']
U = ['u', 'v']
I = ['y', 'z']
D_edges = [(w, v) for w in ['a', 'd'] for v in ['b', 'c']]
y_pred = {'a'}
z_pred = {'a', 'd', 'b'}
y_succ = {'v'}
z_succ = {'u'}

def extensions(nodes, edges):
    return [p for p in permutations(nodes) if all(p.index(a) < p.index(b) for a, b in edges)]

deltas = extensions(D, D_edges)
nus = extensions(U, [])
rows = []
for delta in deltas:
    rank = {v: k + 1 for k, v in enumerate(delta)}
    ly = len(D) - max((rank[v] for v in y_pred), default=0)
    lz = len(D) - max((rank[v] for v in z_pred), default=0)
    lyp = min(ly, len(D) - rank['d'])
    for nu in nus:
        urank = {v: k + 1 for k, v in enumerate(nu)}
        cy = min((urank[v] for v in y_succ), default=len(U)+1)-1
        cz = min((urank[v] for v in z_succ), default=len(U)+1)-1
        rows.append(dict(delta=list(delta), nu=list(nu), Ly=ly, Lz=lz, Lyp=lyp, X=ly-lyp, Cy=cy, Cz=cz))

def mean(fn):
    return sum((Fraction(fn(row)) for row in rows), Fraction()) / len(rows)

p, r, q, s, beta = [mean(lambda row, k=k: row[k]) for k in ['Ly', 'Lz', 'Cy', 'Cz', 'X']]
M = mean(lambda a: a['Ly']*a['Lz'] + min(a['Ly'], a['Lz']))
N = mean(lambda a: a['Cy']*a['Cz'] + min(a['Cy'], a['Cz']))
F = mean(lambda a: a['X']*(a['Lz']+a['Cz']) + min(a['Ly'],a['Lz'])-min(a['Lyp'],a['Lz']))
A, B = M + N + p*s + r*q, p+r+q+s
assert M == p*r+r
assert F == beta*(r+s)
assert N <= q*s+s*s+2*s
assert sorted((a['Ly'],a['X'],a['Lz']) for a in rows) == sorted((ly,x,lz) for ly,x in [(3,1),(2,0)] for lz in [0,1] for _ in range(2))

def count_le(nodes, edges):
    ix = {v:k for k,v in enumerate(nodes)}
    n = len(nodes)
    pre = [0]*n
    for a,b in edges:
        pre[ix[b]] |= 1 << ix[a]
    dp = [0]*(1<<n)
    dp[0] = 1
    for mask in range(1<<n):
        if not dp[mask]:
            continue
        for j in range(n):
            if not (mask>>j)&1 and pre[j]&mask == pre[j]:
                dp[mask|(1<<j)] += dp[mask]
    return dp[-1]

checks = []
for m in range(4):
    chain = ['k'+str(k) for k in range(m)]
    nodes = D+I+U+chain
    edges = list(D_edges)
    edges += [(a,b) for a in D for b in U]
    edges += [(a,'y') for a in y_pred] + [(a,'z') for a in z_pred]
    edges += [('y',a) for a in y_succ] + [('z',a) for a in z_succ]
    edges += [(a,b) for a in D for b in chain]
    edges += [(a,b) for a in chain for b in U]
    edges += list(zip(chain,chain[1:]))
    total = count_le(nodes, edges)
    event = count_le(nodes, edges+[('d','y')])
    t = m+1
    predicted_total = len(rows)*(t*t+(B+1)*t+A)
    predicted_failure = len(rows)*(beta*t+F)
    assert total == predicted_total
    assert total-event == predicted_failure
    checks.append(dict(m=m,t=t,total=total,event=event,failure=total-event,probability=str(Fraction(event,total))))
assert all(Fraction(a['probability']) < Fraction(b['probability']) for a,b in zip(checks,checks[1:]))
output = dict(description='One fixed W antichain 2, V antichain 2, U antichain 2 example; both z slots nonconstant.',
              moments={k:str(v) for k,v in dict(p=p,r=r,q=q,s=s,beta=beta,M=M,N=N,F=F,A=A,B=B).items()},
              fibers=rows, checks=checks)
(OUT/'fixed_checks.json').write_text(json.dumps(output,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(moments=output['moments'],checks=checks),indent=2))
