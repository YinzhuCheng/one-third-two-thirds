#!/usr/bin/env python3
"""Independent canonical rank-deletion and endpoint/average density controls."""
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations
from pathlib import Path
import json
from verify_independent import natural_posets, extensions
ROOT=Path(__file__).resolve().parent
counts=[]
for n in range(2,6):
    modules=0; deletion_ranks=0; external_pairs=0; rank_pairs=0
    for p in natural_posets(n):
        PP=extensions(p)
        for m in range(2,n+1):
            for C in combinations(range(n),m):
                if not all(p[b]>>a&1 for a,b in combinations(C,2)):continue
                outside=[v for v in range(n) if v not in C]
                DC=[];UC=[];IC=[];ok=True
                for v in outside:
                    states=[-1 if p[c]>>v&1 else (1 if p[v]>>c&1 else 0) for c in C]
                    if len(set(states))!=1:ok=False;break
                    {-1:DC,1:UC,0:IC}[states[0]].append(v)
                if not ok:continue
                modules+=1;deletion_ranks+=m
                Q=extensions(p,C[-1]);weights=[]; K=[]
                for L in Q:
                    pos={v:i+1 for i,v in enumerate(L)}
                    a0=max((pos[v] for v in DC),default=0)
                    b0=min((pos[v] for v in UC),default=n)
                    boundary=[a0]+[pos[c] for c in C[:-1]]+[b0]
                    row=[boundary[j+1]-boundary[j] for j in range(m)]
                    kk=sum(a0<pos[z]<b0 for z in IC)
                    assert sum(row)==m+kk
                    weights.append(row);K.append(kk)
                external_groups=defaultdict(list)
                for idx,L in enumerate(Q):
                    external_groups[tuple(v for v in L if v not in C)].append(idx)
                for indices in external_groups.values():
                    assert len({K[k] for k in indices})==1
                    kk=K[indices[0]]
                    for j in range(m):
                        assert Fraction(sum(weights[k][j] for k in indices),len(indices))==Fraction(m+kk,m)
                for j in range(m):
                    def canonical(L):
                        return tuple(v if v not in C else C[C.index(v)-(C.index(v)>j)] for v in L if v!=C[j])
                    direct=Counter(canonical(L) for L in PP)
                    assert all(direct[L]==weights[k][j] for k,L in enumerate(Q))
                    assert min(row[j] for row in weights)==1
                    assert max(row[j] for row in weights)==len(IC)+1
                for a,b in combinations(outside,2):
                    external_pairs+=1
                    events=[L.index(a)<L.index(b) for L in Q]
                    pP=Fraction(sum(L.index(a)<L.index(b) for L in PP),len(PP))
                    pQ=Fraction(sum(events),len(Q));eK=Fraction(sum(K),len(Q))
                    cov=Fraction(sum(kk for kk,ev in zip(K,events) if ev),len(Q))-pQ*eK
                    assert pP-pQ==cov/(m+eK)
                for z in IC:
                    for r in range(1,m):
                        rank_pairs+=1
                        ar=Fraction(sum(L.index(C[r-1])<L.index(z) for L in PP),len(PP))
                        ar1=Fraction(sum(L.index(C[r])<L.index(z) for L in PP),len(PP))
                        events=[L.index(C[r-1])<L.index(z) for L in Q]
                        br=Fraction(sum(events),len(Q));eK=Fraction(sum(K),len(Q))
                        cov=Fraction(sum(kk for kk,ev in zip(K,events) if ev),len(Q))-br*eK
                        assert Fraction(m-r,m)*ar+Fraction(r,m)*ar1==br+cov/(m+eK)
    counts.append({'n':n,'autonomous_chain_modules':modules,'fixed_deletion_ranks':deletion_ranks,'external_pair_checks':external_pairs,'rank_interpolation_checks':rank_pairs})
    print(counts[-1],flush=True)
(ROOT/'autonomous_endpoint_results.json').write_text(json.dumps({'status':'all assertions passed','summary':counts},indent=2)+'\n')
