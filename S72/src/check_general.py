"""Optional exhaustive checks of the finite hypotheses of S72.
Enumerates natural-labelled posets up to six points, not an infinite proof.
"""
from collections import Counter
from itertools import combinations
from math import comb
import json,time

def closed_orders(n):
    edges=list(combinations(range(n),2)); seen=set()
    for mask in range(1<<len(edges)):
        up=[0]*n
        for e,(i,j) in enumerate(edges):
            if mask>>e&1:up[i]|=1<<j
        for i in range(n-1,-1,-1):
            for j in range(i+1,n):
                if up[i]>>j&1:up[i]|=up[j]
        tup=tuple(up)
        if tup not in seen:
            seen.add(tup);yield tup

def extensions(up):
    n=len(up); down=[sum(1<<j for j in range(n) if up[j]>>i&1) for i in range(n)]
    out=[]
    def rec(word,mask):
        if len(word)==n:out.append(word);return
        for i in range(n):
            if not mask>>i&1 and down[i]&~mask==0:rec(word+(i,),mask|1<<i)
    rec((),0)
    return down,out

def main(nmax=6):
    stats=Counter(); start=time.time(); largest_b=0
    for n in range(2,nmax+1):
        for up in closed_orders(n):
            stats['posets']+=1
            down,ex=extensions(up); E=len(ex)
            for x in range(n):
                for y in range(n):
                    if x==y or down[x]!=down[y]:continue
                    Ymask=(1<<y)|(up[y]&~up[x]);Y=[i for i in range(n) if Ymask>>i&1]
                    Y_chain=not any(not (up[u]>>v&1) for u,v in zip(Y,Y[1:]))
                    B=[y]
                    while True:
                        yy=B[-1]
                        zz=next((z for z in range(yy+1,n) if down[z]==(down[yy]|1<<yy) and up[yy]==(up[z]|1<<z)),None)
                        if zz is None:break
                        B.append(zz)
                    A=[x]+[i for i in range(n) if up[x]>>i&1 and not up[y]>>i&1]
                    b=len(B);L=len(A);largest_b=max(largest_b,b)
                    stats['admissible_pairs']+=1
                    if b>=2:stats['nontrivial_blocks']+=1
                    q=[0]*(len(Y)+1);wordweights=Counter()
                    abset=set(A+B)
                    for w in ex:
                        pos={v:k for k,v in enumerate(w)}
                        q[sum(pos[v]<pos[x] for v in Y)]+=1
                        abword=''.join('A' if v in A else 'B' for v in w if v in abset)
                        wordweights[abword]+=1
                    if Y_chain:
                        assert all(u>=v for u,v in zip(q,q[1:])),(up,x,y,q)
                        stats['chain_tail_pairs']+=1
                    for w,nw in wordweights.items():
                        for p in range(len(w)-1):
                            if w[p:p+2]=='AB':
                                other=w[:p]+'BA'+w[p+2:]
                                assert nw<=wordweights[other],(up,x,y,w,nw,other,wordweights[other])
                    for k in range(1,b+1):
                        F=sum(w.index(x)<w.index(B[k-1]) for w in ex)
                        den=comb(L+b,k);num=comb(b,k)
                        assert F*den<=E*(den-num),(up,x,y,k)
                        stats['cdf_bounds']+=1
                    if Y_chain and b>=2 and 3*b*b-(4*L+3)*b-2*L*L+2*L>=0:
                        assert any(2*E<=5*sum(q[:k])<=3*E for k in range(1,len(Y)+1))
                        stats['two_fifths_cases']+=1
    result={**stats,'largest_b':largest_b,'nmax':nmax,'seconds':round(time.time()-start,3)}
    print(json.dumps(result,indent=2))
    return result
if __name__=='__main__':main()
