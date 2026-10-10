#!/usr/bin/env python3
"""One reproducible independent check: domain, word recurrence, labelled ideals.
Python standard library + preinstalled C++/GMP; no author module imports.
"""
from pathlib import Path
from math import prod
from functools import lru_cache
from collections import Counter
from fractions import Fraction
import json, subprocess, time
HERE=Path(__file__).resolve().parent
SOURCE=HERE.parent/'full-seven-core-resolution'
V={1:3,2:9,3:29,4:43}
def require(q,msg):
    if not q:raise RuntimeError(msg)
@lru_cache(None)
def prod_ok(k,h,x):
    return 3*prod(x+i for i in range(k+1))<prod(x+h+i for i in range(k+1))
@lru_cache(None)
def inner_limit(k,h):
    # Forward scan to the first excluded integer, independently of author bisection.
    for x in range(1,(k+1)*h+1):
        if not prod_ok(k,h,x):return x-1
    raise RuntimeError('missing excluded inner bracket')
@lru_cache(None)
def rank_ok(k,h,s):
    return 3*prod(s+i for i in range(1,k+1))>2*prod(s+h+i for i in range(1,k+1))
def domain():
    ports=old=nonempty=0; intervals=[]; vectors=set(); families=Counter()
    # Broad symmetric global cap; every specialized case cap is checked explicitly.
    for a in range(1,182):
      for d in range(a,182):
        if a+d>184:continue
        if a<=3 and d>{1:50,2:92,3:181}[a]:continue
        if a==4 and d>36:continue
        if a>=5 and a+d>41:continue
        for u in range(2,V.get(a,108)+1):
          for v in range(2,V.get(d,108)+1):
            if u+v>110:continue
            if 16*(a*u+d*v)>=60*(u+v)+25*min(u,v)+25*(a+d):continue
            if a<=4 and d>=5 and (16*d-60)*v>=25*d+25*a+(85-16*a)*u:continue
            ports+=1
            if d<=3:old+=1;continue
            bm,cm=inner_limit(a,u),inner_limit(d,v)
            if not bm or not cm:continue
            m=min(u,v)
            def passes(b,c,t):
                return (t>=1 and 2*u<a+b+t+v and 2*v<u+c+t+d and
                        2*t<b+c+m and rank_ok(a,u,b+t+v) and rank_ok(d,v,c+t+u))
            def possible(b,c):return passes(b,c,(b+c+m-1)//2)
            if not possible(bm,cm):continue
            any_interval=False
            for b in range(1,bm+1):
                if not possible(b,cm):continue
                # Find first c by monotonicity, checking original conditions at top t.
                left,right=0,cm
                while left+1<right:
                    mid=(left+right)//2
                    if possible(b,mid):right=mid
                    else:left=mid
                for c in range(right,cm+1):
                    high=(b+c+m-1)//2
                    require(passes(b,c,high),'nonmonotone c possibility')
                    # Find first t from original strict inequalities, no rank thresholds.
                    left,right=0,high
                    while left+1<right:
                        mid=(left+right)//2
                        if passes(b,c,mid):right=mid
                        else:left=mid
                    low=right
                    require(passes(b,c,low),'bad lower endpoint')
                    require(low==1 or not passes(b,c,low-1),'bad predecessor boundary')
                    require(not passes(b,c,high+1),'bad upper endpoint')
                    intervals.append((u,a,b,c,d,v,low,high));any_interval=True
                    for t in range(low,high+1):
                        w=(u,a,b,c,t,d,v)
                        require(w not in vectors,'duplicate candidate');vectors.add(w);families[a,d]+=1
            if any_interval:nonempty+=1
    given_intervals={tuple(map(int,line.split())) for line in (SOURCE/'domain_intervals.txt').read_text().splitlines()}
    require(len(given_intervals)==len(intervals),'duplicate author interval or interval count mismatch')
    require(set(intervals)==given_intervals,'independent domain mismatch')
    rows={}
    for line in (SOURCE/'exact_counts.txt').read_text().splitlines():
        z=tuple(map(int,line.split()));require(len(z)==9,'bad exact row')
        w=z[:7];require(w not in rows,'duplicate author exact count');rows[w]=z[7:]
    require(set(rows)==vectors,'author count vector coverage mismatch')
    (HERE/'independent_intervals.txt').write_text(''.join(' '.join(map(str,r))+'\n' for r in sorted(intervals)))
    stats=dict(port_tuples=ports,prior_covered=old,ports_with_intervals=nonempty,ports_without_new_intervals=ports-old-nonempty,intervals=len(intervals),vectors=len(vectors),maximum_order=max(map(sum,vectors)),families={str(k):v for k,v in sorted(families.items())})
    print('DOMAIN',json.dumps(stats),flush=True)
    return rows,stats

def dual(w):
    u,a,b,c,t,d,v=w
    return v,d,c,b,t,a,u

def labelled(w):
    # Full actual-label bitmask ideals. No word split, binomial, or occupancy formula.
    offsets=[0]
    for x in w:offsets.append(offsets[-1]+x)
    chains=[((1<<w[i])-1)<<offsets[i] for i in range(7)]
    predecessors=[set() for _ in w]
    covers=((0,3),(1,2),(1,4),(2,3),(2,6),(3,5),(4,5))
    for x,y in covers:predecessors[y].add(x)
    for _ in range(7):
        for y in range(7):
            predecessors[y]|=set().union(*(predecessors[x] for x in tuple(predecessors[y])))
    pred=[]
    for i in range(7):
        outside=sum(chains[j] for j in predecessors[i])
        pred.extend(outside|(((1<<r)-1)<<offsets[i]) for r in range(w[i]))
    t0=1<<(offsets[1]-1);t2=1<<(offsets[3]-1)
    b3=1<<offsets[3];b6=1<<offsets[6]
    # Three counts per state: all, T0<T2, B3<B6 (dual endpoint).
    layer={0:(1,1,1)};states=0;max_layer=0
    for degree in range(sum(w)):
        states+=len(layer);max_layer=max(max_layer,len(layer));nxt={}
        for mask,(z,n,nd) in layer.items():
            for chain in chains:
                rest=chain&~mask
                if not rest:continue
                bit=rest&-rest;idx=bit.bit_length()-1
                if pred[idx]&mask!=pred[idx]:continue
                nn=0 if bit==t2 and not mask&t0 else n
                nnd=0 if bit==b6 and not mask&b3 else nd
                new=mask|bit
                if new in nxt:
                    az,an,ad=nxt[new];nxt[new]=(az+z,an+nn,ad+nnd)
                else:nxt[new]=(z,nn,nnd)
        layer=nxt
    require(len(layer)==1,'labelled terminal layer')
    return next(iter(layer.values())),states+1,max_layer

def main():
    tic=time.time(); rows,stats=domain()
    subprocess.run(['g++','-std=c++17','-O2',str(HERE/'recurrence.cpp'),'-lgmpxx','-lgmp','-o',str(HERE/'recurrence')],check=True)
    subprocess.run([str(HERE/'recurrence'),str(SOURCE/'exact_counts.txt'),str(HERE/'recurrence_counts.txt')],check=True)
    minimum=min(rows,key=lambda w:Fraction(rows[w][1],rows[w][0]))
    maxorder=max(rows,key=lambda w:(sum(w),w))
    # Deterministic coverage: minimum, max order, and shortest vector in each family.
    sample={minimum,maxorder}
    for pair in {(w[1],w[5]) for w in rows}:
        sample.add(min((w for w in rows if (w[1],w[5])==pair),key=lambda w:(sum(w),w)))
    sample|={dual(w) for w in tuple(sample)}
    checks=[]
    for w in sorted(sample,key=lambda x:(sum(x),x)):
        result,nstates,width=labelled(w)
        expected=rows.get(w)
        if expected:require(result[:2]==expected,('actual-label count mismatch',w))
        wd=dual(w); ed=rows.get(wd)
        if ed:require((result[0],result[2])==ed,('dual actual-label count mismatch',w))
        require(result[0]>0,'no extensions')
        checks.append(dict(weights=w,order=sum(w),Z=str(result[0]),N02=str(result[1]),N36=str(result[2]),ideal_states=nstates,max_layer=width))
        print('IDEAL',w,'states',nstates,'width',width,flush=True)
    # a=d=4 census is invariant as a set under full reversal.
    for w,(z,n) in rows.items():
        if w[1]==w[5]:require(dual(w) in rows and rows[dual(w)][0]==z,('same-outer dual mismatch',w))
    report=dict(status='PASS',domain=stats,recurrence_vectors=len(rows),exact_integer_comparisons=2*len(rows),all_strictly_above_half=all(2*n>z for z,n in rows.values()),minimum=dict(weights=minimum,probability=str(Fraction(rows[minimum][1],rows[minimum][0]))),labelled_sample=checks,labelled_states=sum(x['ideal_states'] for x in checks),elapsed_seconds=time.time()-tic)
    (HERE/'results.json').write_text(json.dumps(report,indent=2)+'\n')
    print('PASS',len(rows),'vectors;',len(checks),'actual-label cases;',report['labelled_states'],'ideal states',flush=True)
if __name__=='__main__':main()
