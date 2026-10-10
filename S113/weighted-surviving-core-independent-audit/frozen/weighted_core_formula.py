"""Exact counts for the seven-block survivor; standard library, integer arithmetic.

Public weight order is (w0,w1,w2,w3,w4,w5,w6).
Auxiliary zero lengths w0,w1,w5,w6 are allowed only for specified deletion counts.
"""
from functools import lru_cache
from itertools import product
from math import comb
import json
from pathlib import Path

COVERS=((0,3),(1,2),(1,4),(2,3),(2,6),(3,5),(4,5))


def dual_weights(w):
    u,a,b,c,t,d,v=w
    return v,d,c,b,t,a,u


def summands(w):
    u,a,b,c,t,d,v=w
    assert min(u,a,d,v)>=0 and min(b,c,t)>=1
    for i in range(u+1):
        for j in range(t+1):
            left=comb(b+j-1,j)*comb(a+b+i+j-1,i)
            right=comb(u-i+c+t-j,t-j)*comb(u-i+c+t-j+d+v,v)
            yield i,j,left*right


def count_formula(w):
    return sum(n for _,_,n in summands(w))


def endpoint_counts(w):
    u,a,b,c,t,d,v=w
    assert min(w)>=1
    z=count_formula(w)
    first1=count_formula((u,a-1,b,c,t,d,v))
    last5=count_formula((u,a,b,c,t,d-1,v))
    top0_before_top2=sum(n for i,j,n in summands(w) if i==u)
    bottom3_before_bottom6=sum(n for i,j,n in summands(dual_weights(w)) if i==v)
    return {
        'extensions':z,
        'bottom1_before_bottom0':first1,
        'top6_before_top5':last5,
        'top0_before_top2':top0_before_top2,
        'bottom3_before_bottom6':bottom3_before_bottom6,
    }


def dp_oracle(w, extra=None):
    """Independent actual-label ideal DP; extra is one required label comparison."""
    offsets=[sum(w[:i]) for i in range(7)]
    n=sum(w)
    pred=[0]*n
    for i,m in enumerate(w):
        for r in range(1,m): pred[offsets[i]+r]|=1<<(offsets[i]+r-1)
    for i,j in COVERS: pred[offsets[j]]|=1<<(offsets[i]+w[i]-1)
    if extra:
        (i,r),(j,s)=extra
        pred[offsets[j]+s-1]|=1<<(offsets[i]+r-1)
    full=(1<<n)-1
    @lru_cache(None)
    def f(mask):
        if mask==full:return 1
        return sum(f(mask|(1<<i)) for i in range(n) if not (mask>>i)&1 and pred[i]&mask==pred[i])
    return f(0)


def validate():
    checked=0
    for w in product(range(1,4),repeat=7):
        out=endpoint_counts(w)
        expected={
            'extensions':dp_oracle(w),
            'bottom1_before_bottom0':dp_oracle(w,((1,1),(0,1))),
            'top6_before_top5':dp_oracle(w,((6,w[6]),(5,w[5]))),
            'top0_before_top2':dp_oracle(w,((0,w[0]),(2,w[2]))),
            'bottom3_before_bottom6':dp_oracle(w,((3,1),(6,1))),
        }
        assert out==expected,(w,out,expected)
        assert count_formula(dual_weights(w))==out['extensions']
        u,a,b,c,t,d,v=w
        # Strict lower bound on B0-first, because outside windows have d<=a+b+t+v.
        z=out['extensions']; bottom0=z-out['bottom1_before_bottom0']
        assert bottom0*(u+a+b+t+v)>=u*z
        middle_first=dp_oracle(w,((4,1),(2,1)))
        assert middle_first*(t+u+b+c+v)>=t*z
        # Binomial lower bound for T0<T2.
        assert out['top0_before_top2']*comb(a+b+t+v+u,u)>=z*comb(a+b+u-1,u)
        checked+=1
    result={'status':'PASS','weight_vectors':checked,'weight_range':'each wi in {1,2,3}',
        'exact_oracle_counts':6*checked,'duality_checks':checked,'bound_checks':3*checked,
        'smallest_port_survivor':{'weights':[2,1,1,1,1,1,2],**endpoint_counts((2,1,1,1,1,1,2))}}
    Path(__file__).with_name('formula_validation.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__':validate()
