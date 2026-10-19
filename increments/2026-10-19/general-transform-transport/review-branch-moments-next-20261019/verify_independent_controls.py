"""Four fixed controls, independent direct LE enumeration, no poset search."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
from math import comb
import json

ROOT = Path(__file__).resolve().parent

def closure(names, edges):
    r = {(a,b) for a,b in edges}
    while True:
        nxt = r | {(a,d) for a,b in r for c,d in r if b == c}
        if nxt == r: break
        r = nxt
    assert all(a != b for a,b in r)
    return r

def words(names, edges):
    pred = {v: {a for a,b in edges if b == v} for v in names}
    out = []
    def visit(prefix, rem):
        if not rem:
            out.append(tuple(prefix)); return
        for v in sorted(rem):
            if not (pred[v] & rem): visit(prefix+[v], rem-{v})
    visit([], set(names))
    return out

def probability(ws, a, b):
    return F(sum(w.index(a)<w.index(b) for w in ws), len(ws))

def acyclic(names, edges):
    reach = set(edges)
    while True:
        nxt = reach | {(a,d) for a,b in reach for c,d in reach if b == c}
        if nxt == reach: break
        reach = nxt
    return all((v,v) not in reach for v in names)

def branch_case(names, edges, x, y):
    P = closure(names, edges)
    assert (x,y) not in P and (y,x) not in P
    base = words(names,P)
    plus = words(names,closure(names,P|{(x,y)}))
    minus = words(names,closure(names,P|{(y,x)}))
    p = probability(base,x,y)
    assert p < F(1,3)
    def menu(ws, center):
        return {z for z in names if z not in {x,y} and F(1,3)<=probability(ws,center,z)<=F(2,3)}
    A,B,C,D = menu(plus,x),menu(minus,x),menu(plus,y),menu(minus,y)
    G = P|{(y,x)}|{(a,x) for a in A}|{(x,b) for b in B}|{(y,c) for c in C}|{(d,y) for d in D}
    leq=lambda a,b: a==b or (a,b) in P
    rectangles = [[(b,a) for b in B for a in A if leq(b,a)],
                  [(c,d) for c in C for d in D if leq(c,d)],
                  [(b,d) for b in B for d in D if leq(b,d)]]
    assert acyclic(names,G) == (not any(rectangles))
    for a in A:
        assert (a,x) not in P and (x,a) not in P and (y,a) not in P
    for b in B:
        assert (b,x) not in P and (x,b) not in P and (b,y) not in P
    for c in C:
        assert (c,y) not in P and (y,c) not in P and (c,x) not in P
    for d in D:
        assert (d,y) not in P and (y,d) not in P and (x,d) not in P
    return dict(n=len(names), e=len(base), p=str(p), menus={k:sorted(v) for k,v in zip('ABCD',[A,B,C,D])},
                rectangles=rectangles, graph_acyclic=acyclic(names,G))

def run(w, I):
    for i,v in enumerate(w):
        if v not in I: return i
    return len(w)

def C(n,r):
    return comb(n,r) if n >= r >= 0 else 0

def mean(values):
    values=list(values)
    return sum(map(F,values))/len(values)

def marker_case():
    names=['a','b','c','d','e']
    P=closure(names,{('a','c'),('b','d')})
    K={'a','b'}; L={'a','b','c','e'}
    base=words(names,P)
    pairs=[(run(w,K),run(w,L)) for w in base]
    n=len(names)
    q={(i,j):F(sum(x>=i and y>=j for x,y in pairs),len(base)) for i in range(n+1) for j in range(i,n+1)}
    enames=names+['u','v']
    Q=closure(enames,P|{('u','v')}|{('u',a) for a in set(names)-K}|{('v',a) for a in set(names)-L})
    ext=words(enames,Q)
    counts={(i,j):sum(w.index('u')==i and w.index('v')==j+1 for w in ext) for i,j in q}
    assert all(counts[ij] == len(base)*v for ij,v in q.items())
    a=[sum(q[i,j] for j in range(i,n+1)) for i in range(n+1)]
    b=[sum(q[i,j] for i in range(j+1)) for j in range(n+1)]
    for i in range(n+1):
        assert a[i] == sum(F((y-i+1)*(x>=i)) for x,y in pairs)/len(base)
        assert b[i] == sum(F((min(x,i)+1)*(y>=i)) for x,y in pairs)/len(base)
    for seq in [a,b]:
        assert all(seq[i]**2>=seq[i-1]*seq[i+1] for i in range(1,n))
    weights={w:sum(tuple(v for v in z if v not in {'u','v'})==w for z in ext) for w in base}
    for w,(x,y) in zip(base,pairs):
        assert weights[w] == (x+1)*(y+1)-x*(x+1)//2
    assert len(set(weights.values())) > 1
    AA=[a[0]]+[sum(F(C(i-1,r-1))*a[i] for i in range(r,n+1)) for r in range(1,n+2)]
    BB=[F(1)]+[sum(F(C(j-1,r-1))*b[j] for j in range(r,n+1)) for r in range(1,n+2)]
    for r in range(1,n+2):
        assert AA[r] == mean((y+1)*C(x,r)-r*C(x+1,r+1) for x,y in pairs)
        assert BB[r] == mean((x+1)*C(y,r)-C(x,r+1) for x,y in pairs)
    for seq in [AA,BB]:
        assert all(seq[r]**2>=seq[r-1]*seq[r+1] for r in range(1,len(seq)-1))
    ps=[]
    for x,y in pairs:
        w=(x+1)*(y+1)-C(x+1,2)
        u=y*C(x+1,2)-2*C(x+1,3)
        d=C(y+2,3)-C(y-x+1,3)
        v=C(y,2)*C(x+1,2)-2*(y-1)*C(x+1,3)+3*C(x+1,4)
        ij=list((i,j) for i in range(x+1) for j in range(i,y+1))
        assert [w,u,d,v] == [len(ij),sum(i for i,j in ij),sum(j-i for i,j in ij),sum(i*(j-i) for i,j in ij)]
        ps.append((w,u,d,v))
    ew,eu,ed,ev=[mean(z[k] for z in ps) for k in range(4)]
    assert ew*ev <= eu*ed
    ijQ=[(w.index('u'),w.index('v')-1) for w in ext]
    covQ=mean(i*(j-i) for i,j in ijQ)-mean(i for i,j in ijQ)*mean(j-i for i,j in ijQ)
    assert covQ == (ew*ev-eu*ed)/ew**2
    marker_checks=[]
    for m in [1,2]:
        ms=[f'm{k}' for k in range(m)]
        E=P|{(ms[k],ms[k+1]) for k in range(m-1)}|{(z,t) for z in ms for t in set(names)-L}
        mw=words(names+ms,closure(names+ms,E))
        Z=mean(C(y+m,m) for x,y in pairs)
        assert len(mw)==len(base)*Z
        tails=[]
        for i in range(n+1):
            predicted=mean(C(y-i+m,m) if x>=i else 0 for x,y in pairs)/Z
            actual=F(sum(run(w,K)>=i for w in mw),len(mw))
            assert predicted==actual
            tails.append(actual)
        assert all(tails[i]**2>=tails[i-1]*tails[i+1] for i in range(1,n))
        marker_checks.append(dict(m=m,e=len(mw),tails=list(map(str,tails))))
    return dict(n=n,e=len(base),e_extended=len(ext),a=list(map(str,a)),b=list(map(str,b)),
                A=list(map(str,AA)),B=list(map(str,BB)),
                fixed_rank_counts={str(k):v for k,v in counts.items()}, deletion_weights=sorted(set(weights.values())),
                covariance_Q=str(covQ), covariance_polynomial_gap=str(eu*ed-ew*ev),marker_checks=marker_checks)

out={
 'branch_acyclic':branch_case(list('abxyz'),{('a','b'),('b','x')},'x','y'),
 'branch_acyclic_despite_balanced_parent':branch_case(['a1','x','a3','y','b2','c1','z','c3'],
                            {('a1','x'),('x','a3'),('y','b2'),('c1','z'),('z','c3')},'x','y'),
 'branch_cyclic_shared_witness':branch_case(['a1','x','a3','y','b2','z'],
                            {('a1','x'),('x','a3'),('y','b2')},'x','y'),
 'dual_marker':marker_case(),
}
(ROOT/'independent_controls.json').write_text(json.dumps(out,indent=2))
print(json.dumps(out,indent=2))
