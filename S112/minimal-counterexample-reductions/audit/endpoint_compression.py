#!/usr/bin/env python3
"""Independently verify endpoint characterization of the structural forced graph."""
from itertools import product
from collections import Counter
from pathlib import Path
import json
from independent_audit import generate,sign,ischain
from very_good_inflation import inflate,down

def lower(up,a,b):
    return a!=b and sign(up,a,b)==0 and down(up,a)&~down(up,b)==0 and ischain(up,up[b]&~up[a])
def upper(up,a,b):
    return a!=b and sign(up,a,b)==0 and up[b]&~up[a]==0 and ischain(up,down(up,a)&~down(up,b))
def cyclic(edges,n):
    adj=[[] for _ in range(n)]; deg=[0]*n
    for a,b in set(edges):adj[a].append(b);deg[b]+=1
    stack=[i for i in range(n) if deg[i]==0]; count=0
    while stack:
        a=stack.pop();count+=1
        for b in adj[a]:
            deg[b]-=1
            if deg[b]==0:stack.append(b)
    return count<n

stats=Counter()
for n in range(1,6):
    for Q in generate(n):
        low={(a,b) for a in range(n) for b in range(n) if lower(Q,a,b)}
        high={(a,b) for a in range(n) for b in range(n) if upper(Q,a,b)}
        for w in product((1,2),repeat=n):
            P,offset=inflate(Q,w); N=len(P)
            block={x:i for i in range(n) for x in range(offset[i],offset[i+1])}
            bot={i:offset[i] for i in range(n)}; top={i:offset[i+1]-1 for i in range(n)}
            actual=[]
            for x in range(N):
                for y in range(N):
                    if x==y:continue
                    A,B=block[x],block[y]
                    lo=lower(P,x,y); hi=upper(P,x,y)
                    assert lo==((A,B) in low and x==bot[A])
                    assert hi==((A,B) in high and y==top[B])
                    stats['actual_ordered_pair_characterizations']+=1
                    if sign(P,x,y)==1 or lo or hi:actual.append((x,y))
            endpoint=[]
            endpoint.extend((bot[a],bot[b]) for a,b in low)
            endpoint.extend((top[a],top[b]) for a,b in high)
            endpoint.extend((top[a],bot[b]) for a in range(n) for b in range(n) if sign(Q,a,b)==1)
            endpoint.extend((bot[a],top[a]) for a in range(n) if w[a]>1)
            assert cyclic(actual,N)==cyclic(endpoint,N)
            stats['inflation_cycle_equivalences']+=1
report={'status':'PASS','max_quotient_n':5,'each_weight':[1,2],'checks':dict(stats)}
Path(__file__).with_name('endpoint_results.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
