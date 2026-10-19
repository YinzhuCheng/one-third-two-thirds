from fractions import Fraction as F
from collections import Counter,defaultdict
from math import comb
import json
from pathlib import Path
OUT=Path(__file__).resolve().parent
D={'d'}; U={'u'}; I={'x','y','z'}
BASE=[('d','y'),('y','z'),('z','u')]

def words(m):
    C=[f'c{i}' for i in range(1,m+1)]
    V=sorted(D|U|I)+C
    rel=BASE+[(C[i],C[i+1]) for i in range(m-1)]+[(d,c) for d in D for c in C]+[(c,u) for c in C for u in U]
    pred={v:set() for v in V}
    for a,b in rel:pred[b].add(a)
    out=[]
    def rec(pre,remain):
        if not remain:out.append(tuple(pre));return
        used=set(pre)
        for v in sorted(remain):
            if pred[v]<=used:rec(pre+[v],remain-{v})
    rec([],set(V))
    return out

def stats(w,m,x):
    outer=tuple(v for v in w if not v.startswith('c'))
    a=max((outer.index(d) for d in D),default=-1)
    b=min((outer.index(u) for u in U),default=len(outer))
    K=b-a-1
    r=outer.index(x)
    R=0 if r<=a else (K+1 if r>=b else r-a)
    J=sum(w.index(f'c{i}')<w.index(x) for i in range(1,m+1))
    firstU=min((w.index(u) for u in U),default=len(w))
    S=1+sum(w.index(f'c{m}')<w.index(y)<firstU for y in I)
    return outer,K,R,J,S,m+K+1

def enc(v):
    if isinstance(v,F):return str(v)
    if isinstance(v,dict):return {str(k):enc(w) for k,w in v.items()}
    if isinstance(v,(list,tuple)):return [enc(w) for w in v]
    return v

allout=[]
for m in (1,2,3):
    old=words(m); new=words(m+1); N=len(old); NN=len(new)
    push=Counter(); top=Counter()
    for w in new:
        for j in range(1,m+2):
            u=[]
            for v in w:
                if v==f'c{j}':continue
                if v.startswith('c') and int(v[1:])>j:v=f'c{int(v[1:])-1}'
                u.append(v)
            push[tuple(u)]+=1
        top[tuple(v for v in w if v!=f'c{m+1}')]+=1
    fibers=Counter(tuple(v for v in w if not v.startswith('c')) for w in old)
    for w in old:
        outer,K,R,J,S,L=stats(w,m,'x')
        assert push[w]==L
        assert top[w]==S
        assert fibers[outer]==comb(m+K,K)
    per=[]
    for x in sorted(I):
        values=[stats(w,m,x) for w in old]
        EL=sum(F(v[5],N) for v in values)
        ES=sum(F(v[4],N) for v in values)
        EK=sum(F(v[1],N) for v in values)
        assert EL==(m+1)*ES
        assert ES==F(NN,N)
        for i in range(1,m+1):
            q=sum(F(v[3]>=i,N) for v in values)
            qnew=sum(F(w.index(f'c{i}')<w.index(x),NN) for w in new)
            qnewnext=sum(F(w.index(f'c{i+1}')<w.index(x),NN) for w in new)
            cov=sum(F(v[1]*(v[3]>=i),N) for v in values)-EK*q
            B=sum(F((i-1+v[2])*(v[3]==i-1),N) for v in values)
            C=sum(F((v[5]-i-v[2])*(v[3]==i),N) for v in values)
            covS=sum(F(v[4]*(v[3]>=i),N) for v in values)-ES*q
            assert qnew-q==(cov+B)/EL==covS/ES
            assert q-qnewnext==(C-cov)/EL
            assert (m+1-i)*B==i*C
            assert (m+1)*covS==cov+B
            assert q+cov/EL==F(m+1-i,m+1)*qnew+F(i,m+1)*qnewnext
            assert B>0 and C>0
            per.append(dict(x=x,i=i,q=q,qnew=qnew,qnewnext=qnewnext,EK=EK,EL=EL,ES=ES,CovK=cov,B=B,C=C,CovS=covS))
    allout.append(dict(m=m,total_old=N,total_new=NN,fiber_count=len(fibers),checks=per))
result=dict(status='PASS',scope='One fixed actual t=3 poset, chain d<y<z<u plus isolated x; D={d}, U={u}, I={x,y,z}. Independent full LE enumeration at m=1,2,3 and successor lengths. No search.',cover_relations=BASE,records=allout)
(OUT/'independent_transport_check.json').write_text(json.dumps(enc(result),indent=2)+'\n')
print(json.dumps(dict(status='PASS',cases=len(allout),pairs=sum(len(r['checks']) for r in allout),counts=[(r['m'],r['total_old'],r['total_new']) for r in allout])))
