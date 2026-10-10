"""Independent exact checks of the long-final-chain rank obstruction.
Standard library only; no imports from prior poset implementations.
"""
from functools import lru_cache
from fractions import Fraction
from itertools import product
from math import comb
from pathlib import Path
import json

COVERS=((0,3),(1,2),(1,4),(2,3),(2,6),(3,5),(4,5))

def require(condition,context):
    if not condition: raise RuntimeError(repr(context))

def labelled_poset(weights):
    blocks=[];n=0
    for m in weights:
        blocks.append(tuple(range(n,n+m)));n+=m
    pred=[0]*n
    for c in blocks:
        for a,b in zip(c,c[1:]):pred[b]|=1<<a
    for a,b in COVERS:pred[blocks[b][0]]|=1<<blocks[a][-1]
    return blocks,pred

def rank_counts(weights):
    blocks,pred=labelled_poset(weights);n=len(pred);full=(1<<n)-1
    x=blocks[3][0];tailmask=sum(1<<i for i in blocks[6])
    @lru_cache(None)
    def count(mask):
        if mask==full:return 1
        return sum(count(mask|1<<i) for i,p in enumerate(pred)
                   if not mask>>i&1 and p&mask==p)
    total=count(0)
    hist=[0]*(weights[6]+1)
    layer={0:1}
    while layer:
        nxt={}
        for mask,prefix in layer.items():
            for i,p in enumerate(pred):
                if not mask>>i&1 and p&mask==p:
                    child=mask|1<<i
                    if i==x:hist[(mask&tailmask).bit_count()]+=prefix*count(child)
                    else:nxt[child]=nxt.get(child,0)+prefix
        layer=nxt
    require(sum(hist)==total,('rank partition',weights,total,hist))
    return total,hist

def beta_binomial(n,j,k):
    return Fraction((n-j+1)*comb(k+j,j),comb(k+n+2,n))

def main():
    checked=0;crossings=0;worst=Fraction(0);worst_at=None
    for u,a,b,t in product(range(1,5),repeat=4):
        for v in (5,6,7,8):
            w=(u,a,b,1,t,1,v)
            z,hist=rank_counts(w)
            for j in range(1,v):
                p=Fraction(hist[j],z)
                require(3*hist[j]<z,('interior rank bound',w,j,p))
                if p>worst:worst=p;worst_at=(w,j)
            if 3*hist[0]<z and 3*hist[-1]<z:
                cumulative=0;found=False
                for j in range(v):
                    cumulative+=hist[j]
                    if z<=3*cumulative<=2*z:found=True
                require(found,('endpoint crossing',w,hist))
                crossings+=1
            checked+=1
    bchecks=0
    for n in range(5,61):
        for k in range(0,6*n+1):
            for j in range(1,n):
                require(beta_binomial(n,j,k)<Fraction(1,3),('beta atom',n,j,k))
                bchecks+=1
        maximum=Fraction(4*n*(2*n-1),3*(3*n-2)*(3*n-1))
        for k in (2*n-3,2*n-2):
            require(beta_binomial(n,n-1,k)==maximum,('last rank maximum',n,k))
    require(beta_binomial(4,3,5)==Fraction(56,165),('n4 obstruction',))
    require(beta_binomial(4,3,5)>Fraction(1,3),('n4 countercheck',))
    out={'status':'PASS','actual_labelled_vectors':checked,
         'weight_scope':'u,a,b,t each 1..4; c=d=1; v in 5,6,7,8',
         'endpoint_crossing_vectors':crossings,'largest_actual_interior_rank_atom':str(worst),
         'largest_atom_location':worst_at,'exact_beta_binomial_checks':bchecks,
         'generic_n4_countercheck':'p(4,3,5)=56/165>1/3',
         'scope':'Unbounded theorem v>=5; finite checks only validate implementation.'}
    Path(__file__).with_name('verification.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))
if __name__=='__main__':main()
