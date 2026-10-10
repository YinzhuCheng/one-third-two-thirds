#!/usr/bin/env python3
"""Exact rational evaluations of TRUE shared-downset order-polytope fibers.
No finite-order-map surrogate. At s=i/Q,t=j/Q, return m! Q^m f(s,t)
as an integer via uniform-order-statistic kernels and all deletion extensions.
"""
import argparse, collections, functools, itertools, json, math, random, time

def closure(m,edges):
    out=[0]*m
    for i,j in edges: out[i]|=1<<j
    for k in range(m):
        for i in range(m):
            if out[i]>>k&1: out[i]|=out[k]
    return out

def predecessors(out):
    m=len(out)
    return [sum((1<<i) for i in range(m) if out[i]>>j&1) for j in range(m)]

def ideals(pred):
    return [S for S in range(1<<len(pred)) if all(not(S>>v&1) or pred[v]&S==pred[v] for v in range(len(pred)))]

def extensions(pred):
    m=len(pred); full=(1<<m)-1
    def rec(S,prefix):
        if S==full:
            yield tuple(prefix);return
        for v in range(m):
            if not(S>>v&1) and pred[v]&S==pred[v]:
                yield from rec(S|1<<v,prefix+[v])
    return rec(0,[])

def rank_histogram(exts,D,U,V,m):
    C=collections.Counter()
    for seq in exts:
        a=0;b=c=m+1
        for i,v in enumerate(seq,1):
            if D>>v&1:a=i
            if b==m+1 and U>>v&1:b=i
            if c==m+1 and V>>v&1:c=i
        assert a<b and a<c,(seq,D,U,V)
        C[b-a,c-a]+=1
    return C

@functools.lru_cache(None)
def kernel(m,p,q,i,j,Q):
    if p>q:return kernel(m,q,p,j,i,Q)
    if i>=j:
        return sum(math.comb(m,a)*i**a*(Q-i)**(m-a) for a in range(min(p,m+1)))
    # p <= q and i < j; counts before i <= p-1 and before j <= q-1.
    return sum(math.comb(m,a)*math.comb(m-a,b)*i**a*(j-i)**b*(Q-j)**(m-a-b)
               for a in range(min(p,m+1)) for b in range(min(q-a,m-a+1)))

def fiber_grid(C,m,Q):
    return [[sum(c*kernel(m,p,q,i,j,Q) for (p,q),c in C.items()) for j in range(Q+1)] for i in range(Q+1)]

def mtp2_failure(T):
    Q=len(T)-1
    # Positive in the open square, so adjacent grid minors imply all grid minors.
    for i in range(Q):
        for j in range(Q):
            det=T[i][j]*T[i+1][j+1]-T[i+1][j]*T[i][j+1]
            if det<0:return i,j,det,[T[i][j],T[i][j+1],T[i+1][j],T[i+1][j+1]]
    return None

def count_integrals(C):
    E=F=G=H=0
    for (p,q),v in C.items():
        r=min(p,q); h=r*(r+1)//2
        f=h+p*(q-p) if p<=q else h
        g=h+q*(p-q) if q<=p else h
        E+=v*(f+g);F+=v*f;G+=v*g;H+=v*h
    return dict(E=E,F=F,G=G,H=H)

def random_cases(m,rng,k):
    for trial in range(k):
        density=rng.choice([.08,.15,.25,.4,.6])
        out=closure(m,[(i,j) for i in range(m) for j in range(i+1,m) if rng.random()<density]); pred=predecessors(out)
        lows=ideals(pred)
        candidates=[D for D in lows if sum(bool(D>>v&1) and not(out[v]&D) for v in range(m))>=2]
        if not candidates:continue
        D=rng.choice(candidates)
        common=((1<<m)-1)^D
        for v in range(m):
            if D>>v&1:common&=out[v]
        # All upper ideals contained in common strict upper set.
        uppers=[((1<<m)-1)^S for S in lows if (((1<<m)-1)^S)&~common==0]
        if len(uppers)<2:continue
        exts=list(extensions(pred))
        for _ in range(8):
            U,V=rng.choice(uppers),rng.choice(uppers)
            if U==V:continue
            yield out,D,U,V,exts

def exhaustive_cases(m):
    # Exhaust all naturally labeled DAGs, deduplicating transitive closures.
    es=list(itertools.combinations(range(m),2)); seen=set()
    for S in range(1<<len(es)):
        out=tuple(closure(m,[e for k,e in enumerate(es) if S>>k&1]))
        if out in seen:continue
        seen.add(out);pred=predecessors(out); lows=ideals(pred)
        exts=None
        for D in lows:
            if sum(bool(D>>v&1) and not(out[v]&D) for v in range(m))<2:continue
            common=((1<<m)-1)^D
            for v in range(m):
                if D>>v&1:common&=out[v]
            uppers=[((1<<m)-1)^T for T in lows if (((1<<m)-1)^T)&~common==0]
            if exts is None:exts=list(extensions(pred))
            for U,V in itertools.combinations(uppers,2):
                yield out,D,U,V,exts

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--m',type=int,default=6);ap.add_argument('--grid',type=int,default=12);ap.add_argument('--trials',type=int,default=1000);ap.add_argument('--seed',type=int,default=110);ap.add_argument('--exhaustive',action='store_true');ap.add_argument('--out',default='result.json');args=ap.parse_args()
    start=time.time();rng=random.Random(args.seed);nc=0;histset=set(); smallest=None
    source=exhaustive_cases(args.m) if args.exhaustive else random_cases(args.m,rng,args.trials)
    for out,D,U,V,exts in source:
        nc+=1;C=rank_histogram(exts,D,U,V,args.m);key=tuple(sorted(C.items()))
        if key in histset:continue
        histset.add(key);T=fiber_grid(C,args.m,args.grid);bad=mtp2_failure(T)
        if bad:
            result=dict(status='MTP2_COUNTEREXAMPLE_EXACT',args=vars(args),out=out,D=D,U=U,V=V,histogram=[[*pq,v] for pq,v in sorted(C.items())],failure=bad,cases=nc,distinct_histograms=len(histset),integrals=count_integrals(C));break
        if nc%100==0:print('progress',nc,len(histset),round(time.time()-start,2),flush=True)
    else:result=dict(status='NO_FAILURE_ON_EXACT_GRID',args=vars(args),cases=nc,distinct_histograms=len(histset))
    result['elapsed_seconds']=time.time()-start
    with open(args.out,'w') as f:json.dump(result,f,indent=2)
    print(json.dumps(result,indent=2),flush=True)
if __name__=='__main__':main()
