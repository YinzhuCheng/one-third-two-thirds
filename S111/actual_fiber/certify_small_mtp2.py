#!/usr/bin/env python3
"""Sufficient exact triangle-Bernstein certificates for actual MTP2.
P is m! f on s<=t in x=s,y=t-s,z=1-t homogeneous degree m.
The numerator P P_st-P_s P_t has degree 2m-2.
Nonnegative monomial coefficients in x,y,z>=0 certify it is >=0.
We test the transpose too. Diagonal jump in d_s log f is nonnegative
because equal-rank kernels are positive multiples of survival(max(s,t)).
"""
from test_exact_fiber_mtp2 import *
from pathlib import Path

def add(A,B,scale=1):
    C=collections.Counter(A)
    for k,v in B.items():C[k]+=v*scale
    return {k:v for k,v in C.items() if v}
def deriv(A,i):
    C={}
    for k,v in A.items():
        if k[i]:
            j=list(k);j[i]-=1;j=tuple(j);C[j]=C.get(j,0)+v*k[i]
    return C

def mul(A,B):
    C=collections.Counter()
    for a,u in A.items():
        for b,v in B.items():C[tuple(x+y for x,y in zip(a,b))]+=u*v
    return {k:v for k,v in C.items() if v}
def ds(A):return add(deriv(A,0),deriv(A,1),-1)
def dt(A):return add(deriv(A,1),deriv(A,2),-1)

def poly(C,m):
    P=collections.Counter()
    for (p,q),count in C.items():
        # p>=q makes X_(q)>=t the only constraint; expand (x+y)^a.
        if p>=q:
            for a in range(min(q,m+1)):
                for i in range(a+1):P[i,a-i,m-a]+=count*math.comb(m,a)*math.comb(a,i)
        else:
            for i in range(min(p,m+1)):
                for j in range(min(q-i,m-i+1)):P[i,j,m-i-j]+=count*math.comb(m,i)*math.comb(m-i,j)
    return dict(P)

def log_cross(P):return add(mul(P,ds(dt(P))),mul(ds(P),dt(P)),-1)

def certify(C,m):
    failures=[]
    for swap in (False,True):
        Cp={(q,p) if swap else (p,q):c for (p,q),c in C.items()}
        delta=log_cross(poly(Cp,m))
        neg={k:v for k,v in delta.items() if v<0}
        if neg:failures.append((swap,neg))
    return failures

if __name__=='__main__':
    import sys
    m=int(sys.argv[1]) if len(sys.argv)>1 else 5
    seen=set();nc=0;bad=[];start=time.time()
    for out,D,U,V,exts in exhaustive_cases(m):
        nc+=1;C=rank_histogram(exts,D,U,V,m);key=tuple(sorted(C.items()))
        if key in seen:continue
        seen.add(key);fail=certify(C,m)
        if fail:bad.append(dict(out=out,D=D,U=U,V=V,histogram=[[*pq,c] for pq,c in key],negative_coefficients=[(s,{str(k):v for k,v in n.items()}) for s,n in fail]))
    R=dict(m=m,cases=nc,distinct_histograms=len(seen),certified=len(seen)-len(bad),not_certified=bad,elapsed_seconds=time.time()-start)
    json.dump(R,open(Path(__file__).resolve().parent/f'bernstein_mtp2_m{m}.json','w'),indent=2)
    print({k:v for k,v in R.items() if k!='not_certified'});print('first uncertified',bad[:1])
