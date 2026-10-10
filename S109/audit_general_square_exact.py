#!/usr/bin/env python3
"""Independent finite checks of the Ball-fiber shared-downset theorem.
No import from the proposed proof's tests. Exact integer/rational arithmetic only.
Finite checks supplement, and do not establish, the general theorem.
"""
from itertools import combinations
from fractions import Fraction
from functools import lru_cache
from collections import Counter
from pathlib import Path
import json, hashlib

OUT=Path(__file__).resolve().parent

def all_natural_posets(n):
    pairs=list(combinations(range(n),2)); seen=set()
    for bits in range(1<<len(pairs)):
        rows=[0]*n
        for q,(i,j) in enumerate(pairs):
            if (bits>>q)&1: rows[i]|=1<<j
        for i in range(n-1,-1,-1):
            for j in range(i+1,n):
                if (rows[i]>>j)&1: rows[i]|=rows[j]
        key=tuple(rows)
        if key not in seen:
            seen.add(key); yield key

def pred(rows):
    return tuple(sum(1<<j for j,r in enumerate(rows) if (r>>i)&1) for i in range(len(rows)))

def extensions(rows,remove=0):
    n=len(rows); pp=pred(rows); total=(1<<n)-1
    def rec(done,seq):
        if done==total:
            yield seq; return
        for v in range(n):
            if not (done>>v)&1 and not pp[v]&~done:
                yield from rec(done|(1<<v),seq+(v,))
    return rec(remove,())

def count_pair(rows,u,y,exts):
    h=hr=ru=ry=0; pp=pred(rows)
    for ext in exts:
        pos={v:i for i,v in enumerate(ext)}
        new=dict(pos); new[u],new[y]=new[y],new[u]
        legal=all(new[i]<new[j] for i,r in enumerate(rows) for j in range(len(rows)) if (r>>j)&1)
        forward=pos[u]<pos[y]
        blocker=any(pos[v]<pos[y] for v in range(len(rows)) if (rows[u]>>v)&1)
        reverse_blocker=any(pos[v]<pos[u] for v in range(len(rows)) if (rows[y]>>v)&1)
        if pp[u]==pp[y]:
            assert legal == (not (blocker or reverse_blocker))
        if forward:
            if legal:h+=1
            else:ru+=1
        else:
            if legal:hr+=1
            else:ry+=1
    assert h==hr
    return h,ru,ry

def fiber_counts(rows,u,y):
    # Exact integral on each standard simplex of the deletion order polytope.
    # E[(sum of k gaps)^2]/2 = k(k+1)/(2*n*(n-1)).
    # E[(sum of k gaps)*(disjoint sum of j gaps)] = k*j/(n*(n-1)).
    # Its simplex volume 1/(n-2)! yields denominator n!, exactly.
    n=len(rows); pp=pred(rows); h=ru=ry=0; fibers=0
    for ext in extensions(rows,(1<<u)|(1<<y)):
        fibers+=1
        rank={v:i+1 for i,v in enumerate(ext)}
        low=max([rank[d] for d in rank if (pp[u]>>d)&1],default=0)
        upper_u=min([rank[v] for v in rank if (rows[u]>>v)&1],default=n-1)
        upper_y=min([rank[v] for v in rank if (rows[y]>>v)&1],default=n-1)
        k=min(upper_u,upper_y)-low
        assert k>=1
        h+=k*(k+1)//2
        if upper_u<upper_y:ru+=k*(upper_y-upper_u)
        else:ry+=k*(upper_u-upper_y)
    return (h,ru,ry),fibers

def closure_general(rows):
    rows=list(rows)
    for k in range(len(rows)):
        for i in range(len(rows)):
            if (rows[i]>>k)&1:rows[i]|=rows[k]
    assert not any((r>>i)&1 for i,r in enumerate(rows))
    return tuple(rows)

def normalized_transfer(rows,u,y,exts):
    pp=pred(rows)
    assert pp[y]==0 and not ((rows[u]>>y)&1) and not ((rows[y]>>u)&1)
    D=pp[u]; qr=list(rows)
    for d in range(len(rows)):
        if (D>>d)&1:qr[d]|=1<<y
    qr=closure_general(qr); qq=pred(qr)
    assert qq[u]==qq[y]==D and qr[u]==rows[u]
    qexts=list(extensions(qr)); filtered=[]
    p=U=0
    for e in exts:
        pos={v:i for i,v in enumerate(e)}
        if all(pos[d]<pos[y] for d in range(len(rows)) if (D>>d)&1):filtered.append(e)
        p+=pos[u]<pos[y]
        U+=any(pos[v]<pos[y] for v in range(len(rows)) if (rows[u]>>v)&1)
    assert set(qexts)==set(filtered)
    assert sum(e.index(u)<e.index(y) for e in qexts)==p
    assert sum(any(e.index(v)<e.index(y) for v in range(len(rows)) if (qr[u]>>v)&1) for e in qexts)==U
    assert len(qexts)*U<=p*p
    return int(bool(D))

report={'scope':'All naturally labelled finite posets n=2..6, exact complete-extension counts. Separate normalized-transfer checks n<=5.','by_n':[]}
for n in range(2,7):
    stats=Counter(n=n); first_nonchain=None
    for rows in all_natural_posets(n):
        stats['posets']+=1
        pp=pred(rows); exts=list(extensions(rows))
        for u,y in combinations(range(n),2):
            if (rows[u]>>y)&1 or (rows[y]>>u)&1:continue
            if pp[u]==pp[y]:
                stats['shared_downset_pairs']+=1
                true=count_pair(rows,u,y,exts)
                calc,fibers=fiber_counts(rows,u,y)
                assert true==calc,(rows,u,y,true,calc)
                h,ru,ry=true
                assert h>0 and 2*h+ru+ry==len(exts)
                assert h*h>=ru*ry,(rows,u,y,true)
                stats['deletion_fibers']+=fibers
                stats['two_positive_private_counts']+=bool(ru and ry)
                stats['nonempty_downset_pairs']+=bool(pp[u])
                neutral=[v for v in range(n) if v not in (u,y) and not ((pp[u]>>v)&1) and not ((rows[u]>>v)&1) and not ((rows[y]>>v)&1)]
                nc=any(not ((rows[a]>>b)&1 or (rows[b]>>a)&1) for a,b in combinations(neutral,2))
                stats['nonchain_neutral_pairs']+=nc
                stats['nonchain_neutral_two_positive_private_counts']+=bool(nc and ru and ry)
                if nc and ru and ry and first_nonchain is None:
                    first_nonchain={'strict_upper_masks':rows,'pair':[u,y],'H_Ru_Ry':true,'extensions':len(exts),'common_neutral':neutral}
            if n<=5:
                for x,z in ((u,y),(y,u)):
                    if pp[z]==0:
                        stats['normalized_transfer_pairs']+=1
                        stats['normalized_transfer_nonempty_D']+=normalized_transfer(rows,x,z,exts)
    result=dict(stats)
    if first_nonchain:result['nonchain_two_wing_example']=first_nonchain
    report['by_n'].append(result)
    print(json.dumps(result),flush=True)

# Independent exact model calibrations for the analytic normalization.
# Uniform rectangle f=1_[0,a]x[0,b]: K is that same rectangle (unnormalized).
a,b=Fraction(2),Fraction(3)
h=min(a,b)**2/2; ru=a*max(b-a,0); ry=b*max(a-b,0)
assert (h,ru,ry)==(2,2,0)
# f(s,t)=(1-s-t)_+ from A(z)=z, B(z)=1-z on Omega=[0,1].
# H=integral_0^{1/2} t(1-2t)dt=1/24; each wedge=1/12.
h=Fraction(1,24); wedge=Fraction(1,12); rp=wedge-h
assert rp==h and rp*rp==h*h
# Ball radial integral for v in first quadrant: 2 int r(1-c*r)_+ dr=1/(3c^2).
# Thus K: |s|+|t|<=1/sqrt(3), a^2=1/12, h=a^2/2=1/24.
assert Fraction(1,12)/2==h
# Non-log-concave mixing negative control: equal atoms (A,B)=(1,4),(4,1).
# h=1/2, Ru=Ry=3/2. This violates the conclusion, so arbitrary mixtures are invalid.
hmix=Fraction(1,2); rmix=Fraction(3,2)
assert hmix*hmix<rmix*rmix
report['analytic_exact_calibrations']={
 'uniform_rectangle':{'A':2,'B':3,'H':'2','Ru':'2','Ry':'0'},
 'sharp_affine_complement':{'Omega':'[0,1]','A':'z','B':'1-z','H':'1/24','Ru':'1/24','Ry':'1/24','diagonal_a_squared':'1/12','equality':True},
 'arbitrary_mixture_negative_control':{'atoms':[[1,4],[4,1]],'weights':['1/2','1/2'],'H':'1/2','Ru':'3/2','Ry':'3/2','violates_square':True}}
report['status']='PASS'
(OUT/'audit_general_square_exact.json').write_text(json.dumps(report,indent=2)+'\n')
print('ALL EXACT CHECKS PASS',flush=True)
