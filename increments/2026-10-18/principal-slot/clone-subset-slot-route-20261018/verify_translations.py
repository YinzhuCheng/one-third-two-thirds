from functools import lru_cache
from itertools import combinations
from fractions import Fraction

def close(n, pairs):
    up=[0]*n
    for i,j in pairs: up[i]|=1<<j
    for k in range(n):
        for i in range(n):
            if up[i]>>k&1: up[i]|=up[k]
    return tuple(up)

def count_tools(up):
    n=len(up); full=(1<<n)-1
    pred=[sum(1<<i for i in range(n) if up[i]>>j&1) for j in range(n)]
    @lru_cache(None)
    def e(mask):
        if not mask:return 1
        return sum(e(mask^(1<<i)) for i in range(n) if mask>>i&1 and not(pred[i]&mask))
    mins=[i for i in range(n) if not pred[i]]
    def event(A,B):
        # Count first in A, second in B, with no normalization.
        total=0
        for i in A:
            if pred[i]: continue
            rem=full^(1<<i)
            for j in B:
                if rem>>j&1 and not(pred[j]&rem): total+=e(rem^(1<<j))
        return total
    def upper(A):
        bits=sum(1<<i for i in A)
        for i in A: bits|=up[i]
        return [i for i in range(n) if bits>>i&1]
    return e,full,event,upper,mins

def extensions(up):
    n=len(up)
    pred=[sum(1<<i for i in range(n) if up[i]>>j&1) for j in range(n)]
    out=[]
    def rec(rem, seq):
        if not rem:out.append(seq);return
        for i in range(n):
            if rem>>i&1 and not(pred[i]&rem):rec(rem^(1<<i),seq+(i,))
    rec((1<<n)-1,())
    return out

counts={'pairs':0,'posets':0}
for n in range(5):
    pairs=list(combinations(range(n),2)); posets=set()
    for bits in range(1<<len(pairs)):
        posets.add(close(n,[x for i,x in enumerate(pairs) if bits>>i&1]))
    for up in posets:
        counts['posets']+=1
        filters=[S for S in range(1<<n) if all(not(S>>i&1) or not(up[i]&~S) for i in range(n))]
        les=extensions(up); eu=len(les)
        for sy in filters:
            for sz in filters:
                counts['pairs']+=1
                vals=[]
                for f in les:
                    R=next((j for j,v in enumerate(f) if sy>>v&1),n)
                    T=next((j for j,v in enumerate(f) if sz>>v&1),n)
                    vals.append((R,T))
                r=sum(R for R,T in vals);s=sum(T for R,T in vals)
                N=sum(R*T+min(R,T) for R,T in vals)
                d=sum(T for R,T in vals if R==0)
                z=sum(R for R,T in vals if T==0)
                alpha=sum(T*(T+1) for R,T in vals if R==0)
                base=tuple(up)+(sy,sz)
                e,full,K,upper,mins=count_tools(base)
                a,b=n,n+1
                G=[x for x in mins if x<n]
                assert K([a],[b])==eu
                assert K([a],upper([a]))==d
                assert K([b],upper([b]))==z
                assert K([a],G)==s-d
                assert K([b],G)==r-z
                assert K(G,upper(G))==N-r-s+d+z
                assert e(full)==N+r+s+2*eu
                # Third clone allU, empty, or a duplicate of z.
                for kind,sc in [('all',(1<<n)-1),('empty',0),('z',sz)]:
                    cp=tuple(up)+(sy,sz,sc)
                    e2,ff,K2,upper2,mins2=count_tools(cp)
                    c=n+2
                    if kind=='all':
                        assert K2([c],upper2([c]))==N
                        assert K2([a],[b])==eu
                        assert K2([a],[c])==s+eu
                        assert K2([b],[c])==r+eu
                        assert K2([a,b],upper2([a,b]))==2*eu
                    elif kind=='empty':
                        assert K2([a],upper2([a]))==(n+1)*d
                        assert K2([b],upper2([b]))==(n+1)*z
                        assert K2([c],upper2([c]))==0
                        assert K2([a],[b])==(n+1)*eu
                        assert K2([a],[c])==s+eu
                        assert K2([b],[c])==r+eu
                    else:
                        assert K2([a],upper2([a]))==alpha
                        assert K2([b],upper2([b]))==0
                        assert K2([c],upper2([c]))==0
                        assert K2([a],[b])==s+eu
                        assert K2([a],[c])==s+eu
                        assert K2([b],[c])==r+eu
print('All exact event identities verified.',counts)
