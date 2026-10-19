#!/usr/bin/env python3
"""Exact labeled checks for the one-block chain replacement theorem.
No quotient or automorphism reduction is used. All counts are Python integers.
"""
from collections import defaultdict, Counter
from functools import lru_cache
from fractions import Fraction
from math import comb, ceil
from pathlib import Path
import json

OUT=Path(__file__).resolve().parent

class Poset:
    def __init__(self, labels, edges):
        self.labels=tuple(labels)
        self.index={s:i for i,s in enumerate(labels)}
        n=len(labels)
        suc=[0]*n
        for a,b in edges:
            suc[self.index[a]] |= 1 << self.index[b]
        for k in range(n):
            for i in range(n):
                if (suc[i]>>k)&1:
                    suc[i] |= suc[k]
        assert all(not ((suc[i]>>i)&1) for i in range(n))
        self.suc=suc
        self.pred=[sum(1<<j for j in range(n) if (suc[j]>>i)&1) for i in range(n)]
        self.full=(1<<n)-1
    def induced(self, labels):
        labels=tuple(labels)
        return Poset(labels,[(a,b) for a in labels for b in labels if (self.suc[self.index[a]]>>self.index[b])&1])
    def count(self):
        return self.counter()(0)
    def counter(self):
        @lru_cache(None)
        def go(mask):
            if mask==self.full:return 1
            return sum(go(mask | (1<<i)) for i in range(len(self.labels)) if not (mask>>i)&1 and self.pred[i]&mask==self.pred[i])
        return go
    def extensions(self):
        def go(mask,prefix):
            if mask==self.full:
                yield tuple(prefix)
                return
            for i,s in enumerate(self.labels):
                if not (mask>>i)&1 and self.pred[i]&mask==self.pred[i]:
                    yield from go(mask | (1<<i),prefix+[s])
        yield from go(0,[])

def blowup(P,k):
    outside=[s for s in P.labels if s!='x']
    xi=P.index['x']
    D=[s for s in outside if (P.suc[P.index[s]]>>xi)&1]
    U=[s for s in outside if (P.suc[xi]>>P.index[s])&1]
    S=[s for s in outside if s not in D and s not in U]
    C=[f'c{i}' for i in range(1,k+1)]
    outsideP=P.induced(outside)
    edges=[(a,b) for a in outside for b in outside if (outsideP.suc[outsideP.index[a]]>>outsideP.index[b])&1]
    edges += list(zip(C,C[1:]))+[(d,'c1') for d in D]+[(C[-1],u) for u in U]
    return Poset(outside+C,edges),D,U,S,C

def exact_statistics(Q,S,C):
    """Full labeled-ideal DP; a clone has its own original index and bit."""
    suffix=Q.counter()
    total=suffix(0)
    n=len(Q.labels)
    prefix={0:1}
    atoms={s:[0]*(len(C)+1) for s in S}
    pair_counts=defaultdict(int)
    clone_mask=sum(1<<Q.index[c] for c in C)
    states=0
    for size in range(n):
        nxt=defaultdict(int)
        for mask,ways in prefix.items():
            states+=1
            for i,a in enumerate(Q.labels):
                if (mask>>i)&1 or Q.pred[i]&mask!=Q.pred[i]:continue
                new=mask | (1<<i)
                nxt[new] += ways
                completions=ways*suffix(new)
                if a in atoms:
                    j=(mask&clone_mask).bit_count()
                    atoms[a][j]+=completions
                for b in Q.labels:
                    bi=Q.index[b]
                    if a!=b and not (mask>>bi)&1 and not (Q.suc[i]>>bi)&1 and not (Q.suc[bi]>>i)&1:
                        pair_counts[(a,b)] += completions
        prefix=nxt
    assert prefix[Q.full]==total
    assert all(sum(h)==total for h in atoms.values())
    best=Fraction(0)
    bestpairs=[]
    for (a,b),c in pair_counts.items():
        if Q.index[a]>Q.index[b]:continue
        assert c+pair_counts[(b,a)]==total
        bal=Fraction(min(c,total-c),total)
        if bal>best:best,bestpairs=bal,[(a,b)]
        elif bal==best:bestpairs.append((a,b))
    return total,atoms,best,bestpairs,states+1

def verify_direct_projection(P,k):
    Q,D,U,S,C=blowup(P,k)
    outside=set(P.labels)-{'x'}
    Cset=set(C)
    seen={}
    counts=Counter()
    small_counter=Counter()
    for ext in Q.extensions():
        L=tuple(a for a in ext if a in outside)
        projection=tuple(a for a in ext if a not in D and a not in U)
        key=(L,projection)
        assert key not in seen, ('projection collision',seen.get(key),ext)
        seen[key]=ext
        small_counter['extensions']+=1
        for y in S:
            yidx=projection.index(y)
            j=sum(a in Cset for a in projection[:yidx])
            counts[(L,y,j)]+=1
    for L in P.induced([a for a in P.labels if a!='x']).extensions():
        SL=[a for a in L if a in S]
        for y in S:
            r=SL.index(y)
            for j in range(k+1):
                exact_unrestricted=comb(j+r,r)*comb(k-j+len(S)-1-r,len(S)-1-r)
                assert counts[(L,y,j)]<=exact_unrestricted<=comb(k+len(S)-1,len(S)-1)
    # Independently build all lower-bound D | shuffle(S, C) | U extensions.
    lower_set=set()
    def shuffles(a,b):
        if not a:yield tuple(b);return
        if not b:yield tuple(a);return
        for tail in shuffles(a[1:],b):yield (a[0],)+tail
        for tail in shuffles(a,b[1:]):yield (b[0],)+tail
    for ld in P.induced(D).extensions():
        for ls in P.induced(S).extensions():
            for lu in P.induced(U).extensions():
                for mid in shuffles(ls,C):
                    ext=ld+mid+lu
                    rank={a:i for i,a in enumerate(ext)}
                    assert all(rank[Q.labels[i]]<rank[Q.labels[j]] for i in range(len(Q.labels)) for j in range(len(Q.labels)) if (Q.suc[i]>>j)&1)
                    assert ext not in lower_set
                    lower_set.add(ext)
    assert len(lower_set)==P.induced(D).count()*P.induced(S).count()*P.induced(U).count()*comb(k+len(S),len(S))
    assert len(lower_set)<=small_counter['extensions']
    return {'k':k,'enumerated_extensions':small_counter['extensions'],'projection_keys':len(seen),'explicit_lower_extensions':len(lower_set)}

CASES=[
 {'name':'chain_wings_cross_links','labels':['d0','d1','x','u0','u1','s0','s1'],
  'edges':[('d0','d1'),('d1','x'),('x','u0'),('u0','u1'),('d1','s0'),('d0','s1'),('s1','u0'),('s0','u1')]},
 {'name':'forked_wings_ordered_incomparables','labels':['d0','d1','x','u0','u1','s0','s1','s2'],
  'edges':[('d0','x'),('d1','x'),('x','u0'),('x','u1'),('s0','s1'),('d0','s0'),('d1','s2'),('s1','u0'),('s2','u1')]},
 {'name':'mixed_rank_incomparables','labels':['d0','d1','x','u0','s0','s1','s2'],
  'edges':[('d0','d1'),('d1','x'),('x','u0'),('s0','s2'),('s1','s2'),('d0','s1'),('d1','s2'),('s0','u0')]},
 {'name':'upper_only','labels':['x','u0','s0','s1','s2'],
  'edges':[('x','u0'),('s0','s1'),('s1','u0')]},
 {'name':'lower_only','labels':['d0','x','s0','s1','s2'],
  'edges':[('d0','x'),('s0','s1'),('d0','s0')]},
 {'name':'one_incomparable_forked_wings','labels':['d0','d1','x','u0','u1','s0'],
  'edges':[('d0','x'),('d1','x'),('x','u0'),('x','u1'),('d0','s0'),('s0','u0')]},
 {'name':'empty_wings_ordered_S','labels':['x','s0','s1','s2'],
  'edges':[('s0','s1')]},
 {'name':'two_point_antichain_sharpness','labels':['x','s0'],'edges':[]},
]

def fstr(f):
    return str(f.numerator) if f.denominator==1 else f'{f.numerator}/{f.denominator}'

results=[]
for case in CASES:
    P=Poset(case['labels'],case['edges'])
    _,D,U,S,C=blowup(P,1)
    eD=P.induced(D).count();eU=P.induced(U).count();eS=P.induced(S).count()
    eout=P.induced([a for a in P.labels if a!='x']).count()
    A=Fraction(eout,eD*eS*eU)
    m=len(S)
    thresh=Fraction(m)*(3*A-1)
    nonstrict=(thresh.numerator+thresh.denominator-1)//thresh.denominator
    strict=thresh.numerator//thresh.denominator+1
    # Small enumeration checks every original-labeled extension and projection.
    projections=[verify_direct_projection(P,k) for k in [1,2,4]]
    ks=sorted(set([1,2,4,8,16,nonstrict,strict]))
    rows=[]
    for k in ks:
        Q,D,U,S,C=blowup(P,k)
        total,atoms,delta,bestpairs,states=exact_statistics(Q,S,C)
        denom=eD*eS*eU*comb(k+m,m)
        atom_numer_bound=eout*comb(k+m-1,m-1)
        eta=A*Fraction(m,k+m)
        assert total>=denom
        for y,h in atoms.items():
            assert max(h)<=atom_numer_bound
            assert Fraction(max(h),total)<=eta
        bound=Fraction(1,2)-eta/2 if eta<=Fraction(1,2) else None
        if bound is not None:assert delta>=bound
        if k>=nonstrict:assert delta>=Fraction(1,3)
        if k>=strict:assert delta>Fraction(1,3)
        rows.append({'k':k,'labeled_ideal_states':states,'ePk':total,'denominator_lower_bound':denom,'eta':fstr(eta),
                     'max_atom':fstr(Fraction(max(max(h) for h in atoms.values()),total)),
                     'delta':fstr(delta),'delta_bound':fstr(bound) if bound is not None else None,
                     'best_pairs':[list(p) for p in bestpairs[:8]],'J_histograms':atoms})
    # Exact direct enumeration and independent ideal DP must agree.
    for p in projections:
        row=next(r for r in rows if r['k']==p['k'])
        assert row['ePk']==p['enumerated_extensions']
    result={**case,'D':D,'U':U,'S':S,'eD':eD,'eS':eS,'eU':eU,'eP_minus_x':eout,'A':fstr(A),
            'threshold_real':fstr(thresh),'nonstrict_integer_threshold':nonstrict,'strict_integer_threshold':strict,
            'direct_projection_audit':projections,'exact_rows':rows}
    results.append(result)

# Sharpness of the actual 1/k error along the even-k subsequence.
sharpP=Poset(['x','y'],[])
for k in range(1,21):
    Q,D,U,S,C=blowup(sharpP,k)
    total,atoms,delta,bestpairs,states=exact_statistics(Q,S,C)
    assert total==k+1
    assert atoms['y']==[1]*(k+1)
    assert delta==Fraction((k+1)//2,k+1)

summary={'status':'all_assertions_passed','scope':'fixed finite base poset, one autonomous chain replacement only',
         'no_literature_novelty_claim':True,'cases':results}
(OUT/'exact_results.json').write_text(json.dumps(summary,indent=2)+'\n',encoding='utf-8')
lines=['All exact labeled checks passed.','']
for r in results:
    lines += [f"{r['name']}: D={r['D']}, S={r['S']}, U={r['U']}; A={r['A']}; threshold >= {r['nonstrict_integer_threshold']} / > {r['strict_integer_threshold']-1}."]
    for row in r['exact_rows']:
        lines += [f"  k={row['k']}: e={row['ePk']}, eta={row['eta']}, max atom={row['max_atom']}, delta={row['delta']}, bound={row['delta_bound']}"]
(OUT/'exact_summary.txt').write_text('\n'.join(lines)+'\n',encoding='utf-8')
print('\n'.join(lines))
