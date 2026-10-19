from fractions import Fraction as F
from collections import Counter
from math import comb
import json


def sf(x):
    return str(x)

def summarize_pmf(pmf, k, ell):
    M=max(pmf, default=0)
    p=[sum((v for j,v in pmf.items() if j>=i), F(0)) for i in range(M+1)]
    def tail(i):
        return p[i] if i<=M else F(0)
    nbu=all(tail(i+j)<=tail(i)*tail(j) for i in range(M+1) for j in range(M+1))
    r=sum((v*min(j,k) for j,v in pmf.items()),F(0))
    s=sum((v*min(j,ell) for j,v in pmf.items()),F(0))
    product=sum((v*min(j,k)*min(j,ell) for j,v in pmf.items()),F(0))
    cov=product-r*s
    bound=r*(r+1)
    stronger=r*(1+r-tail(k))
    N=product+r
    Tgap=r*s+r*r+2*r-N
    Cgap=bound-cov
    assert Tgap==Cgap
    if nbu:
        assert cov<=stronger<=bound
    return dict(nbu=nbu, r=sf(r), s=sf(s), product=sf(product), cov=sf(cov), bound=sf(bound), stronger_bound=sf(stronger), gap=sf(Cgap), pmf={str(j):sf(v) for j,v in sorted(pmf.items())})


def linear_extensions(a,b,edges):
    n=a+b
    predecessors=[set() for _ in range(n)]
    for i in range(a-1):
        predecessors[i+1].add(i)
    for i,j in edges:
        predecessors[a+j].add(a+i)
    out=[]
    def visit(word, used):
        if len(word)==n:
            out.append(tuple(word)); return
        for x in range(n):
            if x not in used and predecessors[x]<=used:
                visit(word+[x],used|{x})
    visit([],set())
    return out


def actual(a,b,k,ell,edges):
    extensions=linear_extensions(a,b,edges)
    K=len(extensions)
    A=set(range(k,a)) | set(range(a,a+b))
    B=set(range(ell,a)) | set(range(a,a+b))
    Js=Counter()
    pairs=Counter()
    for beta in extensions:
        J=next(i for i,x in enumerate(beta) if x>=a)
        R=next(i for i,x in enumerate(beta) if x in A)
        T=next(i for i,x in enumerate(beta) if x in B)
        assert (R,T)==(min(J,k), min(J,ell))
        Js[J]+=1
        pairs[R,T]+=1
    pmf={j:F(c,K) for j,c in Js.items()}
    summary=summarize_pmf(pmf,k,ell)
    for j in range(a+1):
        measured=sum((v for t,v in pmf.items() if t>=j),F(0))
        assert measured==F(comb(a+b-j,a-j),comb(a+b,a))
    summary.update(a=a,b=b,k=k,ell=ell,edges=edges,K=K,joint_pmf={str(pair):sf(F(count,K)) for pair,count in sorted(pairs.items())})
    return summary

# Fixed diagnostic examples only: no generation of new posets or parameter sweep.
abstract=[
    dict(name='deterministic zero',k=0,ell=0,**summarize_pmf({0:F(1)},0,0)),
    dict(name='capped geometric, q=1/2, cap=3',k=2,ell=3,**summarize_pmf({0:F(1,2),1:F(1,4),2:F(1,8),3:F(1,8)},2,3)),
    dict(name='Binomial(3,1/2)',k=1,ell=3,**summarize_pmf({0:F(1,8),1:F(3,8),2:F(3,8),3:F(1,8)},1,3)),
    dict(name='non-NBU necessity control',k=1,ell=3,**summarize_pmf({0:F(9,10),3:F(1,10)},1,3)),
]
actual_cases=[
    dict(name='empty chain',**actual(0,2,0,0,[])),
    dict(name='full filter at k=0',**actual(3,2,0,3,[(0,1)])),
    dict(name='nontrivial, V chain',**actual(3,2,1,3,[(0,1)])),
    dict(name='same a,b, V antichain',**actual(3,2,1,3,[])),
    dict(name='equal filters at k=ell=a',**actual(3,2,3,3,[])),
    dict(name='fork V',**actual(4,3,2,4,[(0,1),(0,2)])),
    dict(name='same a,b, V chain',**actual(4,3,2,4,[(0,1),(1,2)])),
]
assert actual_cases[2]['joint_pmf']==actual_cases[3]['joint_pmf']
assert actual_cases[5]['joint_pmf']==actual_cases[6]['joint_pmf']
assert abstract[-1]['nbu'] is False
assert F(abstract[-1]['cov'])>F(abstract[-1]['bound'])
result=dict(abstract=abstract,actual=actual_cases,passes=True)
with open('/workspace/shared/audit-nbu-prefix-20261018/exact_controls.json','w') as f:
    json.dump(result,f,ensure_ascii=False,indent=2)
print(json.dumps(result,ensure_ascii=False,indent=2))
