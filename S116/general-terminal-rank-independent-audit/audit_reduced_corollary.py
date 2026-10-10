"""Fresh exact check of all 41 reduced a=d=1 vectors; no author imports."""
from functools import lru_cache
from fractions import Fraction
from itertools import product, combinations
from pathlib import Path
import argparse,json

EDGES=((0,3),(1,2),(1,4),(2,3),(2,6),(3,5),(4,5))
REACH=[[False]*7 for _ in range(7)]
for i,j in EDGES:REACH[i][j]=True
for k in range(7):
    for i in range(7):
        for j in range(7):REACH[i][j]=REACH[i][j] or REACH[i][k] and REACH[k][j]
def require(x,msg):
    if not x:raise RuntimeError(str(msg))
def audit_vector(w):
    vertices=[(i,j) for i,m in enumerate(w) for j in range(m)]
    def lt(x,y):return x[0]==y[0] and x[1]<y[1] or REACH[x[0]][y[0]]
    preds=[]
    for y in vertices:preds.append(sum(1<<k for k,x in enumerate(vertices) if lt(x,y)))
    FULL=(1<<len(vertices))-1
    @lru_cache(None)
    def children(mask):
        return tuple(mask|(1<<i) for i,p in enumerate(preds) if not mask>>i&1 and mask&p==p)
    @lru_cache(None)
    def total(mask):
        if mask==FULL:return 1
        return sum(total(m) for m in children(mask))
    def numerator(x,y):
        X,Y=1<<x,1<<y
        @lru_cache(None)
        def constrained(mask):
            if mask&Y and not mask&X:return 0
            if mask&X:return total(mask)
            return sum(constrained(m) for m in children(mask))
        return constrained(0)
    Z=total(0);balanced=[];failed=[];pairs=[]
    for i,j in combinations(range(len(vertices)),2):
        x,y=vertices[i],vertices[j]
        if lt(x,y) or lt(y,x):continue
        N=numerator(i,j)
        pairs.append([list(x),list(y),N])
        if Z<=3*N<=2*Z:balanced.append([list(x),list(y),N,str(Fraction(N,Z))])
        for p,q,M in ((x,y,N),(y,x,Z-N)):
            dp={z for z in vertices if lt(z,p)};dq={z for z in vertices if lt(z,q)}
            up={z for z in vertices if lt(p,z)};uq={z for z in vertices if lt(q,z)}
            def chain(S):return all(a==b or lt(a,b) or lt(b,a) for a in S for b in S)
            if (dp<=dq and chain(uq-up) or uq<=up and chain(dp-dq)) and 3*M<=2*Z:
                failed.append([list(p),list(q),M,str(Fraction(M,Z))])
    require(balanced and failed,('missing witness',w))
    return {'weights':list(w),'extensions':Z,'balanced_pairs':balanced,'failed_forced_arrows':failed,'all_incomparable_pair_numerators':pairs,'ideal_states':total.cache_info().currsize}

def main(path):
    vectors=[]
    for u,v in product((2,3),repeat=2):
        for b,c in product(range(1,u+1),range(1,v+1)):
            for t in range(1,5):
                if 2*u<1+b+t+v and 2*v<u+c+t+1 and 2*t<b+c+v and 2*t<b+c+u:
                    vectors.append((u,1,b,c,t,1,v))
    require(len(vectors)==41,'vector count')
    records=[audit_vector(w) for w in vectors]
    out={'status':'PASS','vectors':len(records),'maximum_order':max(sum(w) for w in vectors),'counts_by_ports':{str((u,v)):sum(w[0]==u and w[6]==v for w in vectors) for u,v in product((2,3),repeat=2)},'all_pair_checks':sum(len(r['all_incomparable_pair_numerators']) for r in records),'actual_balanced_pairs':sum(len(r['balanced_pairs']) for r in records),'checks_use_assert':False,'records':records}
    Path(path).write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k!='records'},indent=2))
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--output',required=True)
    main(p.parse_args().output)
