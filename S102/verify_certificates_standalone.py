"""Exact, dependency-free verification of two local counterexamples.

Run: python3 verify_certificates_standalone.py
Optional: --permutations also filters all n! permutations.
These are NOT counterexamples to the 1/3-2/3 conjecture.
"""
from itertools import combinations, permutations
from fractions import Fraction
import sys

CASES = [
    ('seven', 'u s t y a b c', 'us ut ua ya tb yb bc', 62),
    ('ten', 'y u s a c d t b e f', 'yc us uc ut sa ab cd cb be ef', 372),
]

for title, names, edge_text, expected in CASES:
    labels=names.split(); n=len(labels); ix={x:i for i,x in enumerate(labels)}
    edges=[(ix[a],ix[b]) for a,b in edge_text.split()]
    pre=[0]*n
    for a,b in edges: pre[b] |= 1<<a
    for _ in range(n):
        for j in range(n):
            for i in range(n):
                if pre[j]>>i&1: pre[j] |= pre[i]
    assert all(not pre[i]>>i&1 for i in range(n))
    extensions=[]
    def visit(p,mask):
        if len(p)==n: extensions.append(tuple(p)); return
        for i in range(n):
            if not mask>>i&1 and pre[i]&mask==pre[i]: visit(p+[i],mask|1<<i)
    visit([],0); E=len(extensions); assert E==expected
    counts=[[0]*n for _ in range(n)]
    for p in extensions:
        for k,a in enumerate(p):
            for b in p[k+1:]: counts[a][b]+=1
    # Independent subset dynamic program counts every orientation.
    size=1<<n; forward=[0]*size; backward=[0]*size
    forward[0]=1; backward[-1]=1
    for mask in range(size):
        for j in range(n):
            if not mask>>j&1 and pre[j]&mask==pre[j]: forward[mask|1<<j]+=forward[mask]
    dp=[[0]*n for _ in range(n)]
    for mask in range(size-2,-1,-1):
        for j in range(n):
            if not mask>>j&1 and pre[j]&mask==pre[j]: backward[mask]+=backward[mask|1<<j]
    for mask in range(size):
        for j in range(n):
            if not mask>>j&1 and pre[j]&mask==pre[j]:
                for i in range(n):
                    if mask>>i&1: dp[i][j]+=forward[mask]*backward[mask|1<<j]
    assert forward[-1]==backward[0]==E and dp==counts
    def incomparable(i,j): return i!=j and not pre[i]>>j&1 and not pre[j]>>i&1
    def balanced(i,j): return E<=3*counts[i][j]<=2*E
    width=max(k for k in range(n+1) for S in combinations(range(n),k)
              if all(incomparable(i,j) for i,j in combinations(S,2)))
    y,u,s,t=map(ix.get,['y','u','s','t'])
    inc=[i for i in range(n) if incomparable(i,y)]
    majority=[i for i in inc if 3*counts[i][y]>2*E]
    assert pre[y]==0 and width==3 and majority==[u]
    assert all(not balanced(i,y) for i in inc)
    private=[i for i in range(n) if pre[i]>>u&1 and not pre[i]>>y&1]
    private_min=[i for i in private if not any(pre[i]>>j&1 for j in private)]
    assert set(private_min)=={s,t}
    assert 2*E<3*counts[u][y] and 9*counts[u][y]<7*E
    assert 3*counts[s][y]<E and 3*counts[t][y]<E
    d=sum(all(p.index(v)<p.index(y) for v in range(n) if pre[u]>>v&1) for p in extensions)
    assert 9*d>18*counts[u][y]-5*E
    common=[i for i in range(n) if pre[i]>>u&1 and pre[i]>>y&1]
    common_min=[i for i in common if not any(pre[i]>>j&1 for j in common)]
    menu=[y,u,s,t]+(common_min if title=='ten' else [])
    assert all(not balanced(i,j) for i,j in combinations(menu,2))
    if '--permutations' in sys.argv:
        full=[]
        for p in permutations(range(n)):
            rank=[0]*n
            for k,v in enumerate(p): rank[v]=k
            if all(rank[a]<rank[b] for a,b in edges): full.append(p)
        assert set(full)==set(extensions)
    pairs=[(labels[i],labels[j],str(Fraction(counts[i][j],E)))
           for i,j in combinations(range(n),2) if balanced(i,j)]
    assert pairs
    print(title, 'PASS; E =', E, '; width =', width)
    print('No balanced pair within', [labels[i] for i in menu])
    print('Balanced pairs in full poset:',pairs)
