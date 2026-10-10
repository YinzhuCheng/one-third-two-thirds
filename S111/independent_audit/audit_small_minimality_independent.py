#!/usr/bin/env python3
"""Independent n<=7 certificate. Natural posets by recursively adding an ideal,
not DAG-closure enumeration. No imports from proposal's programs. Exact integers.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations,product
from pathlib import Path
import json,math,time
BASE=Path(__file__).resolve().parent

def natural_posets(m):
    if m==0:
        yield ();return
    for old in natural_posets(m-1):
        for I in range(1<<(m-1)):
            if all(not I>>v&1 or old[v]&~I==0 for v in range(m-1)):
                yield old+(I,)

def exts(pred):
    def rec(mask,prefix):
        if len(prefix)==len(pred):yield prefix
        for v,ps in enumerate(pred):
            if not mask>>v&1 and ps&~mask==0:
                yield from rec(mask|1<<v,prefix+(v,))
    return list(rec(0,()))

def sub(A,B):
    result=dict(A)
    for e,c in B.items():result[e]=result.get(e,0)-c
    return {e:c for e,c in result.items() if c}

def diff(A,k):
    result={}
    for e,c in A.items():
        if e[k]:
            f=list(e);f[k]-=1;f=tuple(f)
            result[f]=c*e[k]
    return result

def mul(A,B):
    result=Counter()
    for p,c in A.items():
        for q,d in B.items():result[tuple(a+b for a,b in zip(p,q))]+=c*d
    return dict(result)

def deriv_s(A):return sub(diff(A,0),diff(A,1))
def deriv_t(A):return sub(diff(A,1),diff(A,2))

def P_from_hist(hist,m):
    # Uniform single formula for all ranks (not branch used by proposal).
    ans=Counter()
    for (p,q),count in hist.items():
        for i in range(m+1):
            for j in range(m-i+1):
                k=m-i-j
                if i<p and i+j<q:
                    ans[i,j,k]+=count*math.factorial(m)//(math.factorial(i)*math.factorial(j)*math.factorial(k))
    return dict(ans)

def certify(hist,m):
    result=[]
    for swap in (False,True):
        P=P_from_hist({((q,p) if swap else (p,q)):c for (p,q),c in hist.items()},m)
        ds=deriv_s(P); dt=deriv_t(P)
        delta=sub(mul(P,deriv_s(dt)),mul(ds,dt))
        assert all(c>=0 for c in delta.values()),(hist,m,swap,delta)
        assert all(sum(e)==2*m-2 for e in delta)
        result.append({'swap':swap,'delta_terms':[[*e,c] for e,c in sorted(delta.items())]})
    return result

rows=[];records=[]
for m in range(0,6):
    npos=cases=degen=0; seen={}
    for pred in natural_posets(m):
        npos+=1
        successors=[sum(1<<v for v in range(m) if pred[v]>>w&1) for w in range(m)]
        linear=None
        for D in range(1<<m):
            if any(D>>v&1 and pred[v]&~D for v in range(m)):continue
            maxima=[v for v in range(m) if D>>v&1 and not successors[v]&D]
            if len(maxima)<2:continue
            common=sum(1<<v for v in range(m) if pred[v]&D==D and not D>>v&1)
            uppers=[]
            for U in range(1<<m):
                if U&~common:continue
                if any(U>>v&1 and successors[v]&~U for v in range(m)):continue
                uppers.append(U)
            degen+=len(uppers)
            if linear is None:linear=exts(pred)
            for U,V in combinations(uppers,2):
                cases+=1;hist=Counter()
                for seq in linear:
                    pos={v:k+1 for k,v in enumerate(seq)}
                    a=max([pos[v] for v in range(m) if D>>v&1],default=0)
                    b=min([pos[v] for v in range(m) if U>>v&1],default=m+1)
                    c=min([pos[v] for v in range(m) if V>>v&1],default=m+1)
                    assert min(b,c)>a
                    hist[b-a,c-a]+=1
                key=tuple(sorted(hist.items()))
                if key not in seen:
                    cert=certify(hist,m)
                    seen[key]=True
                    records.append({'m':m,'representative_pred':pred,'D':D,'U':U,'V':V,'histogram':[[p,q,c] for (p,q),c in key],'certificate':cert})
    rows.append({'m':m,'n':m+2,'natural_posets':npos,'distinct_UV_configurations':cases,'U_equals_V_configurations':degen,'distinct_histograms':len(seen),'all_histograms_certified':True})
summary={'status':'PASS','scope':'All n=2..7 shared-downset incomparable pairs, conditional only on supplied analytic cases and diagonal argument audited in accompanying report.','enumeration':'Independent recursive-ideal predecessor enumeration; no proposal imports.','by_m':rows,'certificate_records':len(records)}
(BASE/'small_minimality_independent_summary.json').write_text(json.dumps(summary,indent=2)+'\n')
(BASE/'small_minimality_full_coefficients.json').write_text(json.dumps(records,indent=2)+'\n')
print(json.dumps(summary,indent=2))
