#!/usr/bin/env python3
"""Prepare fixed objects/filters, verify C++ DP, run and summarize exact tests."""
from __future__ import annotations
from collections import Counter
from fractions import Fraction
from itertools import product
import importlib.util
import json
from pathlib import Path
import random
import subprocess
import sys
import time

OUT=Path(__file__).resolve().parent
OBJECT_SEED=2026101801
FILTER_SEED=2026101802


def edges_of(case):
    lengths=case['lengths'];offsets=[];s=0
    for n in lengths:offsets.append(s);s+=n
    edges=[(off+i,off+i+1) for off,n in zip(offsets,lengths) for i in range(n-1)]
    edges += [(offsets[a]+p,offsets[b]+q) for a,p,b,q in case['cross']]
    return s,edges,offsets


def valid(t,cross):
    return all(t[b]<=q or t[a]>p for a,p,b,q in cross)


def filter_mask(t,lengths):
    mask=0;off=0
    for a,n in zip(t,lengths):
        mask |= ((1<<n)-(1<<a))<<off
        off+=n
    return mask


def pool(case,rng,cap=112):
    L=case['lengths'];k=len(L);cross=case['cross']
    allstates=[t for t in product(*(range(n+1) for n in L)) if valid(t,cross)]
    keep=[];seen=set()
    def add(t):
        t=tuple(t)
        if len(keep)<cap and t not in seen and valid(t,cross):
            keep.append(t);seen.add(t)
    add([0]*k);add(L)
    for f in [Fraction(1,100),Fraction(1,20),Fraction(1,10),Fraction(1,4),Fraction(1,2),Fraction(3,4),Fraction(9,10),Fraction(19,20),Fraction(99,100)]:
        add([int(f*n) for n in L])
    # Near full and near empty, including single-chain suffix filters.
    for c,n in enumerate(L):
        for x in sorted({0,1,min(2,n),n//4,n//2,3*n//4,max(0,n-2),n-1,n}):
            t=list(L);t[c]=x;add(t)
            t=[0]*k;t[c]=x;add(t)
    # Actual principal upsets, using full reachability, then their complements.
    n,edges,offsets=edges_of(case);succ=[0]*n
    for a,b in edges:succ[a]|=1<<b
    # The element labels need not be topological when cross-relations are present.
    for z in range(n):
        for a in range(n):
            if succ[a]>>z&1:succ[a]|=succ[z]
    for c,length in enumerate(L):
        for x in sorted({0,1,min(2,length-1),length//4,length//2,3*length//4,max(0,length-2),length-1}):
            v=offsets[c]+x;s=(1<<v)|succ[v];t=[]
            for off,m in zip(offsets,L):
                one=next((j for j in range(m) if s>>(off+j)&1),m)
                assert all(s>>(off+j)&1 for j in range(one,m))
                t.append(one)
            add(t)
    # Fill the fixed-size candidate pool by uniform sampling of legal ideals.
    for t in rng.sample(allstates,min(len(allstates),cap*4)):
        add(t)
    assert all(valid(t,cross) for t in keep)
    return keep,len(allstates)


def random_cross(L,count,rng):
    # First construct a shuffled linear extension of the disjoint chains.
    live=[0]*len(L);order=[]
    while any(a<n for a,n in zip(live,L)):
        c=rng.choice([c for c in range(len(L)) if live[c]<L[c]])
        order.append((c,live[c]));live[c]+=1
    rank={v:i for i,v in enumerate(order)}
    candidates=[]
    for a in range(len(L)):
        for b in range(a+1,len(L)):
            for p in range(L[a]):
                for q in range(L[b]):
                    u=(a,p);v=(b,q)
                    if rank[u]<rank[v]:candidates.append((a,p,b,q))
                    else:candidates.append((b,q,a,p))
    return sorted(rng.sample(candidates,min(count,len(candidates))))


def cases():
    result=[];rng=random.Random(OBJECT_SEED)
    def add(name,L,cross=()):result.append(dict(name=name,lengths=list(L),cross=[list(e) for e in cross]))
    for L in [(1,19),(1,49),(1,99),(1,199),(2,198),(5,195),(20,180),(50,150),(100,100),(10,40),(20,20)]:
        add('disjoint2_'+'_'.join(map(str,L)),L)
    for L in [(1,1,18),(1,1,198),(1,9,190),(2,18,180),(10,10,180),(20,60,120),(66,67,67),(10,10,10),(20,20,20),(30,30,30)]:
        add('disjoint3_'+'_'.join(map(str,L)),L)
    L=(20,180)
    add('joined2_20_180_one_gate',L,[(0,9,1,90)])
    add('joined2_20_180_opposing_gates',L,[(0,4,1,90),(1,134,0,15)])
    add('joined2_20_180_random14',L,random_cross(L,14,rng))
    L=(100,100)
    add('joined2_100_100_one_gate',L,[(0,49,1,50)])
    add('joined2_100_100_middle_barrier',L,[(0,49,1,50),(1,49,0,50)])
    add('joined2_100_100_random20',L,random_cross(L,20,rng))
    for L in [(10,10,180),(20,60,120),(66,67,67)]:
        barrier=[(a,L[a]//2-1,b,L[b]//2) for a in range(3) for b in range(3) if a!=b]
        add('joined3_'+'_'.join(map(str,L))+'_middle_barrier',L,barrier)
        add('joined3_'+'_'.join(map(str,L))+'_random20',L,random_cross(L,20,rng))
    assert len(result)==33
    return result


def write_input(objects,path):
    with path.open('w') as f:
        print(len(objects),file=f)
        for c in objects:
            print(c['name'],len(c['lengths']),*c['lengths'],len(c['cross']),file=f)
            for e in c['cross']:print(*e,file=f)
            print(len(c['filters']),file=f)
            for t in c['filters']:print(*t,file=f)


def load_rows(path):
    return [json.loads(x) for x in path.read_text().splitlines() if x]


def verify():
    # These tiny cases are validation fixtures only, not new stress evidence.
    cs=[dict(name='check_1_2',lengths=[1,2],cross=[]),
        dict(name='check_2_2_gate',lengths=[2,2],cross=[[0,0,1,1]]),
        dict(name='check_2_2_1',lengths=[2,2,1],cross=[[0,0,1,1],[2,0,0,1]]),
        dict(name='check_3_2_2',lengths=[3,2,2],cross=[[0,0,1,1],[1,0,2,1],[2,0,0,2]])]
    for c in cs:c['filters']=[t for t in product(*(range(n+1) for n in c['lengths'])) if valid(t,c['cross'])]
    write_input(cs,OUT/'verification_input.txt')
    subprocess.run([str(OUT/'stress'),str(OUT/'verification_input.txt'),str(OUT/'verification_cpp.jsonl')],check=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    spec=importlib.util.spec_from_file_location('old','/workspace/shared/actual-slot-covariance-20261018/test_actual_slots.py')
    old=importlib.util.module_from_spec(spec);spec.loader.exec_module(old)
    rows=load_rows(OUT/'verification_cpp.jsonl');report=[];totalpairs=0
    for c in cs:
        n,edges,_=edges_of(c);pred=[0]*n
        for a,b in edges:pred[b]|=1<<a
        les=[]
        def visit(seq,mask):
            if len(seq)==n:les.append(seq);return
            for v in range(n):
                if not mask>>v&1 and pred[v]&mask==pred[v]:visit(seq+[v],mask|(1<<v))
        visit([],0)
        fs=[filter_mask(t,c['lengths']) for t in c['filters']]
        data=old.ideal_dp(n,edges);means,products,unionmeans=old.moments(data,fs)
        assert data['le']==len(les)
        slots=[[next((i for i,v in enumerate(le) if s>>v&1),n) for s in fs] for le in les]
        tested=0
        for row in rows:
            if row['type']!='pair' or row['case']!=c['name']:continue
            a,b=row['i'],row['j'];yy=[v[a] for v in slots];zz=[v[b] for v in slots]
            direct=[sum(yy),sum(zz),sum(x*y for x,y in zip(yy,zz)),sum(min(x,y) for x,y in zip(yy,zz)),sum(x*x for x in yy),sum(x*x for x in zz)]
            got=[int(row[k]) for k in ['sum_Ry','sum_Rz','sum_product','sum_min','sum_Ry2','sum_Rz2']]
            prior=[means[a],means[b],int(products[a,b]),unionmeans[fs[a]|fs[b]],int(products[a,a]),int(products[b,b])]
            assert direct==got==prior,(c['name'],a,b,direct,got,prior)
            tested+=1
        report.append(dict(name=c['name'],n=n,complete_LE_count=len(les),legal_filters=len(fs),verified_pairs=tested,three_way_agreement=True))
        totalpairs+=tested
    (OUT/'verification.json').write_text(json.dumps(dict(fixtures=report,verified_pairs=totalpairs,passed=True),indent=2)+'\n')
    print('Three-way small-fixture verification passed:',totalpairs,'pairs',flush=True)


def main():
    if len(sys.argv)>1 and sys.argv[1]=='--verify-only':verify();return
    verify()
    objs=cases();rng=random.Random(FILTER_SEED)
    for c in objs:
        fs,ns=pool(c,rng);c['filters']=fs;c['legal_ideal_count']=ns
    (OUT/'objects.json').write_text(json.dumps(dict(object_seed=OBJECT_SEED,filter_seed=FILTER_SEED,objects=objs),indent=2)+'\n')
    write_input(objs,OUT/'input.txt')
    with (OUT/'run.log').open('w') as log:
        p=subprocess.run([str(OUT/'stress'),str(OUT/'input.txt'),str(OUT/'raw_results.jsonl')],stderr=log)
    if p.returncode not in (0,2):raise RuntimeError(f'executable returned {p.returncode}')
    print('Executable complete, return',p.returncode,flush=True)

if __name__=='__main__':main()
