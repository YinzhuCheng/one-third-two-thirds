"""Standard-library bounded checks, not the proof of the infinite exclusion."""
from functools import lru_cache
from itertools import product
from math import comb
from pathlib import Path
import json

def require(condition, message):
    if not condition:
        raise AssertionError(message)

COVERS=((0,3),(1,2),(1,4),(2,3),(2,6),(3,5),(4,5))

def terms(w):
    u,a,b,c,t,d,v=w
    for i in range(u+1):
        for j in range(t+1):
            yield i,j,comb(b+j-1,j)*comb(a+b+i+j-1,i)*comb(u-i+c+t-j,t-j)*comb(u-i+c+t-j+d+v,v)

def z(w):return sum(n for _,_,n in terms(w))
def dual(w):
    u,a,b,c,t,d,v=w
    return v,d,c,b,t,a,u

def oracle(w,extra=None):
    offsets=[sum(w[:i]) for i in range(7)];n=sum(w);pred=[0]*n
    for i,m in enumerate(w):
        for r in range(1,m):pred[offsets[i]+r]|=1<<(offsets[i]+r-1)
    for i,j in COVERS:pred[offsets[j]]|=1<<(offsets[i]+w[i]-1)
    if extra:
        (i,r),(j,s)=extra
        pred[offsets[j]+s-1]|=1<<(offsets[i]+r-1)
    full=(1<<n)-1
    @lru_cache(None)
    def f(mask):
        if mask==full:return 1
        return sum(f(mask|(1<<i)) for i in range(n) if not (mask>>i)&1 and pred[i]&mask==pred[i])
    return f(0)

def main():
    count=oracles=prefixes=middle=bounds=0
    for u,a,t,v in product(range(1,6),repeat=4):
        w=(u,a,1,1,t,1,v);den=z(w)
        require(den==oracle(w), 'den==oracle(w)');oracles+=1
        qs=[den]
        for i in range(1,a+1):
            val=z((u,a-i,1,1,t,1,v))
            require(val==oracle(w,((1,i),(0,1))), 'val==oracle(w,((1,i),(0,1)))')
            oracles+=1;prefixes+=1;qs.append(val)
        gaps=[qs[i]-qs[i+1] for i in range(a)]
        require(all(gaps[i]>=gaps[i+1] for i in range(a-1)), 'all(gaps[i]>=gaps[i+1] for i in range(a-1))')
        for i,gap in enumerate(gaps):
            require(gap==z((u-1,a-i,1,1,t,1,v)), 'gap==z((u-1,a-i,1,1,t,1,v))')
        H=1+t+v
        require(qs[a]*comb(H+a+u,u)<=den*comb(H+u,u), 'qs[a]*comb(H+a+u,u)<=den*comb(H+u,u)');bounds+=1
        if a>=2:
            require(qs[a]*(H+u+1)*(H+u+2)<=den*(H+1)*(H+2), 'qs[a]*(H+u+1)*(H+u+2)<=den*(H+1)*(H+2)');bounds+=1
        lo=sum(n for _,j,n in terms(w) if j==0)
        hi=sum(n for _,j,n in terms(dual(w)) if j==0)
        require(lo==oracle(w,((2,1),(4,1))), 'lo==oracle(w,((2,1),(4,1)))');oracles+=1
        require(hi==oracle(w,((4,t),(3,1))), 'hi==oracle(w,((4,t),(3,1)))');oracles+=1
        require(lo*(v+t+2)<=den*(v+2), 'lo*(v+t+2)<=den*(v+2)')
        require(hi*(u+t+2)<=den*(u+2), 'hi*(u+t+2)<=den*(u+2)');middle+=2
        count+=1
    # Pure algebra implications; this loop does not substitute for their proof.
    cone_points=0
    for u,t,v in product(range(2,101),range(1,51),range(2,101)):
        if not(2*t<u+2 and 2*v<u+t+2):continue
        H=1+t+v
        require(4*H<=5*u+9, '4*H<=5*u+9')
        require(3*(H+1)*(H+2)<2*(H+u+1)*(H+u+2), '3*(H+1)*(H+2)<2*(H+u+1)*(H+u+2)')
        require(87*u*u+90*u-221>0, '87*u*u+90*u-221>0')
        cone_points+=1
    result={
      'status':'PASS',
      'weight_family':'(u,a,1,1,t,1,v)',
      'exact_grid':'u,a,t,v independently in {1,2,3,4,5}',
      'weight_vectors':count,
      'independent_labelled_ideal_DP_counts':oracles,
      'prefix_probabilities_checked':prefixes,
      'middle_bound_checks':middle,
      'prefix_insertion_bound_checks':bounds,
      'algebra_grid':'2<=u,v<=100; 1<=t<=50; 2t<u+2 and 2v<u+t+2',
      'algebra_cone_points':cone_points,
      'infinite_claim_status':'Direct proof in SINGLE_OUTER_SPINE_EXCLUSION.md; independent generalized-middle-bound audit is a stated dependency.'
    }
    Path(__file__).with_name('verification.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
