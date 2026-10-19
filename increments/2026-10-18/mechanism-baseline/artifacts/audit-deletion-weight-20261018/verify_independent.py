#!/usr/bin/env python3
"""Independent deletion multiset audit. No producer imports or sampling."""
from collections import Counter
from fractions import Fraction
from functools import lru_cache
from itertools import combinations
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parent


def natural_posets(n):
    if n==0:
        yield ()
        return
    for p in natural_posets(n-1):
        for s in range(1<<(n-1)):
            if all(not(s>>v&1) or p[v]&s==p[v] for v in range(n-1)):
                yield p+(s,)


def extensions(p, deleted=None):
    n=len(p); total=(1<<n)-1
    if deleted is not None: total ^= 1<<deleted
    ans=[]
    def visit(rem, seq):
        if not rem:
            ans.append(tuple(seq)); return
        for v in range(n):
            if rem>>v&1 and not(p[v]&rem):
                seq.append(v); visit(rem^(1<<v),seq); seq.pop()
    visit(total,[])
    return ans


def inspect(p,x,save=False):
    n=len(p); P=extensions(p); Q=extensions(p,x)
    D=[v for v in range(n) if p[x]>>v&1]
    U=[v for v in range(n) if p[v]>>x&1]
    I=[v for v in range(n) if v!=x and v not in D and v not in U]
    maxD=[d for d in D if not any(p[e]>>d&1 for e in D)] or [None]
    minU=[u for u in U if not any(p[u]>>v&1 for v in U)] or [None]
    forced={(d,u): [z for z in I if (d is None or p[z]>>d&1) and (u is None or p[u]>>z&1)] for d in maxD for u in minU}
    prediction=1+min(map(len,forced.values()))
    direct=Counter(tuple(v for v in L if v!=x) for L in P)
    ww=[]
    for L in Q:
        pos={v:j+1 for j,v in enumerate(L)}
        w=min((pos[u] for u in U),default=n)-max((pos[d] for d in D),default=0)
        assert direct[L]==w,(p,x,L,direct[L],w)
        ww.append(w)
    assert min(ww)==prediction,(p,x,ww,prediction)
    assert max(ww)==len(I)+1,(p,x,ww)
    structural=all(p[z]>>d&1 for d in D for z in I) and all(p[u]>>z&1 for u in U for z in I)
    assert (min(ww)==max(ww))==structural,(p,x,ww,structural)
    # Check every extremal-boundary pair is individually attainable, not just minimizer.
    realized={}
    for d,u in forced:
        candidates=[]
        for L,w in zip(Q,ww):
            ds=[v for v in L if v in D]; us=[v for v in L if v in U]
            if (ds[-1] if ds else None)==d and (us[0] if us else None)==u:
                candidates.append(w)
        assert candidates and min(candidates)==1+len(forced[d,u]),(p,x,d,u,candidates,forced[d,u])
        realized[str((d,u))]=min(candidates)
    E=len(Q); W=len(P)
    assert sum(ww)==W
    probabilities=[]
    for a,b in combinations([v for v in range(n) if v!=x],2):
        C=sum(L.index(a)<L.index(b) for L in Q)
        WC=sum(w for L,w in zip(Q,ww) if L.index(a)<L.index(b))
        PP=sum(L.index(a)<L.index(b) for L in P)
        assert WC==PP
        covariance=Fraction(WC,E)-Fraction(C*W,E*E)
        assert Fraction(PP,W)-Fraction(C,E)==covariance/Fraction(W,E)
        R=Fraction(max(ww),min(ww)); probP=Fraction(PP,W); probQ=Fraction(C,E)
        assert probQ <= R*probP/(1-probP+R*probP)
        assert probQ >= probP/(R*(1-probP)+probP)
        if save:
            probabilities.append({'a':a,'b':b,'pP':str(probP),'pQ':str(probQ),'covariance':str(covariance)})
    if save:
        return {'predecessor_masks':p,'delete':x,'D':D,'U':U,'I':I,'extensions_P':len(P),'extensions_Q':len(Q),'weights': [{'order':L,'weight':w} for L,w in zip(Q,ww)],'predicted_min':prediction,'max':max(ww),'constant_structure':structural,'boundary_pair_minima':realized,'pair_checks':probabilities}


def build(names, edges):
    n=len(names); idx={v:i for i,v in enumerate(names)}; p=[0]*n
    for a,b in edges: p[idx[b]]|=1<<idx[a]
    for _ in range(n):
        for v in range(n):
            for u in range(n):
                if p[v]>>u&1:p[v]|=p[u]
    assert not any(p[v]>>v&1 for v in range(n))
    return tuple(p)

if __name__=='__main__':
    summary=[]
    for n in range(1,7):
        count=0
        for p in natural_posets(n):
            count+=1
            for x in range(n):inspect(p,x)
        summary.append({'n':n,'naturally_labeled_posets':count,'deletion_instances':n*count})
        print(summary[-1],flush=True)
    examples={}
    cases=[('positive_bridge_nonconstant', ['d','x','u','z','v'], [('d','x'),('x','u'),('d','z'),('z','u')], 'x'),
           ('empty_D_positive_bridge', ['x','u','z','v'], [('x','u'),('z','u')], 'x'),
           ('empty_U_positive_bridge', ['d','x','z','v'], [('d','x'),('d','z')], 'x'),
           ('both_boundaries_empty', ['x','a','b','c'], [('a','b')], 'x'),
           ('constant_nontrivial_diamond', ['d','x','z','u'], [('d','x'),('x','u'),('d','z'),('z','u')], 'x'),
           ('constant_nonchain', ['d','x','z','v','u'], [('d','x'),('x','u'),('d','z'),('z','u'),('d','v'),('v','u')], 'x'),
           ('strict_threshold_boundary', ['x','a','b','z'], [('x','a'),('a','b'),('x','z')], 'x'),
           ('autonomous_chain_endpoint', ['c1','c2','v'], [('c1','c2')], 'c1'),
           ('autonomous_chain_interior', ['c1','c2','c3','v','w'], [('c1','c2'),('c2','c3'),('v','w')], 'c2')]
    for name,names,edges,x in cases:
        r=inspect(build(names,edges),names.index(x),True); r['labels']=names;examples[name]=r
    # Pure bounded-density distributions realize both odds bounds and threshold equality.
    distribution_checks=[]
    for R in [Fraction(1),Fraction(3,2),Fraction(2),Fraction(5)]:
        beta=1/(1+2*R); q=Fraction(1,3)
        p=q/(q+R*(1-q))
        assert p==beta
        distribution_checks.append({'R':str(R),'pP':str(p),'pQ':str(q)})
    result={'scope':'All posets on up to six vertices, one natural labeling per compatible total order; exhaustive over all naturally labeled posets, hence all unlabeled isomorphism types occur. No conjecture or classification search.', 'summary':summary,'total_deletions':sum(r['deletion_instances'] for r in summary),'status':'all assertions passed','examples':examples,'threshold_equality_distribution_checks':distribution_checks}
    (ROOT/'independent_results.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print('PASSED',result['total_deletions'],flush=True)
