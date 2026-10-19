"""Independent 8! enumeration, written for the October 19 public-source check.
No imports from or execution of the source author's repository.
"""
from itertools import permutations, combinations
from collections import Counter
import json
V = ('b','x','z','y','a','t1','t2','t3')
EDGES = [('b','z'),('z','a'),('x','a'),('b','y'),('t1','t2'),('t2','t3')]
EDGES += [(t,q) for t in ('t1','t2','t3') for q in ('x','y','a')]
L=[]
for word in permutations(V):
    rank={v:i for i,v in enumerate(word)}
    if all(rank[u]<rank[v] for u,v in EDGES): L.append(rank)
E=len(L)
inc=[p for p in combinations(V,2) if 0<sum(r[p[0]]<r[p[1]] for r in L)<E]
corepairs=[p for p in inc if all(v in V[:5] for v in p)]
def table(first,second):
    cells=[[0,0],[0,0]]
    for rank in L:
        cells[int(rank[first[0]]<rank[first[1]])][int(rank[second[0]]<rank[second[1]])]+=1
    return cells
def deficit(first,second,answer):
    cells=table(first,second)
    return E-sum(cells[answer])-max(cells[answer])
width=max(len(S) for size in range(1,len(V)+1) for S in combinations(V,size)
          if all(p in inc for p in combinations(S,2)))
rows=[]
for p in corepairs:
    n=sum(r[p[0]]<r[p[1]] for r in L)
    heavy=int(2*n>=E)
    rows.append(dict(first=p,forward_count=n,heavy_branch=max(n,E-n),
                     best_heavy_branch_deficit=max(deficit(p,q,heavy) for q in corepairs)))
receipt=dict(extensions=E,width=width,incomparability_degrees={v:sum(v in p for p in inc) for v in V},
             core_histogram={' '.join(w):n for w,n in Counter(tuple(sorted(V[:5],key=r.get)) for r in L).items()},
             first_comparison_rows=rows,
             best_adaptive_core_only_deficit=max(min(max(deficit(p,q,a) for q in corepairs) for a in (0,1)) for p in corepairs),
             exterior_fixed_strategy=dict(first=('b','t2'),second=('z','t3'),cells=table(('b','t2'),('z','t3'))))
print(json.dumps(receipt,indent=2))
