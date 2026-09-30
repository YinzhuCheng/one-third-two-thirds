"""Exact small-instance exploration of the ten-parameter seed inflation.
No assertion of an infinite result follows from these computations.
"""
from functools import lru_cache
from fractions import Fraction
from itertools import accumulate

def distribution(main=(1,)*6, outer=(1,)*4):
    if len(main)!=6 or len(outer)!=4 or min(*main,*outer)<1:
        raise ValueError('six positive main lengths and four positive outer lengths required')
    cuts=list(accumulate(main)); a,b,c,d=outer
    end=(cuts[-1],a+d,b+c)
    @lru_cache(None)
    def succ(s):
        i,j,k=s; out=[]
        if i<end[0] and (i!=cuts[1] or j>=a) and (i!=cuts[4] or k>=b+c):
            out.append((0,(i+1,j,k)))
        if j<a or (j<end[1] and i>=cuts[3] and k>=b):
            out.append((1,(i,j+1,k)))
        if (k<b and i>=cuts[0]) or (b<=k<end[2] and j>=a):
            out.append((2,(i,j,k+1)))
        return tuple(out)
    @lru_cache(None)
    def suffix(s):
        if s==end:return 1
        return sum(suffix(t) for _,t in succ(s))
    start=(0,0,0); E=suffix(start)
    # H[q][r][j][i] counts i elements of chain r before q_j in full extensions.
    H={(q,r):[[0]*(end[r]+1) for _ in range(end[q])] for q in range(3) for r in range(3) if r!=q}
    layer={start:1}
    for _ in range(sum(end)):
        nxt={}
        for s,f in layer.items():
            for q,t in succ(s):
                nxt[t]=nxt.get(t,0)+f
                count=f*suffix(t)
                for r in range(3):
                    if r!=q:H[q,r][s[q]][s[r]]+=count
        layer=nxt
    pairs=[]
    for q in range(3):
        for r in range(q+1,3):
            for j,row in enumerate(H[q,r]):
                cdf=0
                for i,v in enumerate(row[:-1]):
                    cdf+=v
                    pairs.append(((q,j+1),(r,i+1),cdf))
    best=max(pairs,key=lambda v:min(v[2],E-v[2]))
    stats=dict(total=E,best=best,delta=Fraction(min(best[2],E-best[2]),E),states=suffix.cache_info().currsize)
    return stats,H

if __name__=='__main__':
    import random,json,time
    rng=random.Random(72930); t0=time.time(); results=[]
    for t in range(150):
        main=tuple(rng.randint(1,5) for _ in range(6)); outer=tuple(rng.randint(1,6) for _ in range(4))
        st,_=distribution(main,outer)
        results.append((float(st['delta']),main,outer,str(st['delta']),st['best']))
    print('seconds',time.time()-t0)
    print(json.dumps(sorted(results)[:12],ensure_ascii=False,indent=2))
