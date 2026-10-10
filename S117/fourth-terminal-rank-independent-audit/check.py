#!/usr/bin/env python3
"""Independent exact d4 check. Standard library only; no author-code imports."""
from fractions import Fraction as F
from functools import lru_cache
from math import comb, prod, factorial
from pathlib import Path
import json


def require(ok, message):
    if not ok:
        raise RuntimeError(message)


def rising(a, n):
    return prod(range(a, a+n))


def atom(a, beta, n, j):
    return F(comb(n,j)*rising(a,j)*rising(beta,n-j), rising(a+beta,n))


def component_tail(a, n):
    q=prod((F(a+i,a+n+i) for i in range(5)),start=F(1))
    return q, F(5*n,a+n-1)*q


def tail_bound(q, p, n):
    # Exact equivalent of p <= f_n(q), without roots or floating point.
    # Rearrangement gives q^(1/5) <= [5nq-(n-3)p]/[5nq+3p].
    numerator=5*n*q-(n-3)*p
    denominator=5*n*q+3*p
    return numerator>=0 and q*denominator**5<=numerator**5


checks=0
for n in (4,5,10,43,44,45,100,1000):
    alphas=list(range(1,101))+[n,2*n,5*n-5,5*n,10*n,100*n]
    for a in alphas:
        q,p=component_tail(a,n)
        require(q==atom(a,5,n,n),'component q formula')
        require(p==atom(a,5,n,n-1),'component p formula')
        require(q < F(a+2,a+n+2)**5,'strict geometric-mean inequality')
        require(tail_bound(q,p,n),'component nonlinear bound')
        checks+=1

mixture_checks=0
for n in (4,43,44,45,100,1000):
    for c in (1,2,10,100,500):
        for weights in ((1,1,1),(1,2,7),(100,1,1),(1,1,100)):
            pars=(c,c+n, c+7*n)
            components=[component_tail(a,n) for a in pars]
            q=sum((w*x[0] for w,x in zip(weights,components)),F(0))/sum(weights)
            p=sum((w*x[1] for w,x in zip(weights,components)),F(0))/sum(weights)
            require(tail_bound(q,p,n),'mixture nonlinear bound')
            mixture_checks+=1

first_checks=0
middle_checks=0
for n in range(44,151):
    first_max=F(5*n,(n+4)*(n+5))
    require(first_max<F(1,3),'first-atom threshold')
    for a in (1,2,3,5,10,20,100,1000):
        require(atom(a,5,n,1)<=first_max,'first-atom integer-alpha maximum')
        first_checks+=1
    for j in range(2,n-1):
        peak=F(comb(n,j)*j**j*(n-j)**(n-j),n**n)
        require(peak<=F(80,243)<F(1,3),'middle binomial peak')
        middle_checks+=1

# Exact finite threshold, followed by the analytically proved monotonicity in n.
threshold44=223**5-3*179**5
require(threshold44==175086646>0,'threshold44 arithmetic')
require(218**5-3*175**5==-32912557<0,'same envelope does not certify n43')

# Boundary and polynomial checks are integer/rational identities.
polynomial=[comb(5,j)*(5**j*223**(5-j)-3*4**j*179**(5-j)) for j in range(6)]
require(polynomial==[175086646,226795165,19429030,642530,9515,53], 'threshold polynomial coefficients')
require(component_tail(172,43)[0]==F(2207480,6660009)<F(1,3), 'c172 boundary')
require(component_tail(173,43)[0]==F(1480015,4440006)>F(1,3), 'c173 boundary')


def beta(a,b):
    return F(factorial(a-1)*factorial(b-1),factorial(a+b-1))


def mono_moment(k,ell,d,j):
    return F(k+1,k+j+1)*F(rising(k+ell+2,j),rising(k+ell+d+2,j))


def component_mixture_stats(parts,d,n):
    # parts lists (k, ell, unnormalized full component mass).
    total=sum((mass for _,_,mass in parts),F(0))
    moments=[sum((mass*mono_moment(k,ell,d,j) for k,ell,mass in parts),F(0))/total
             for j in range(n+1)]
    q=moments[n]
    p=n*(moments[n-1]-moments[n])
    C=sum((mass*F(k+ell+d+1,k+ell+d+n+1) for k,ell,mass in parts),F(0))/total
    return moments,q,p+q,C


mono=component_mixture_stats([(491,0,F(1))],5,100)
require(mono[1:]==(F(646396283,1951717773), F(256619324351,384488401281), F(497,597)),
        'd5 monomial values')
s=F(999,1000)
r=F(1,2)
fiber=[]
for k,coeffk in ((491,s),(492,(1-s)/492)):
    for ell,coeffell in ((0,s-r),(1,1-s)):
        fiber.append((k,ell,coeffk*coeffell*beta(k+ell+2,5)/(k+1)))
fiber_stats=component_mixture_stats(fiber,5,100)
require(fiber_stats[1:]==(F(5975039402610052100339,18040870122675452479134),
                        F(14627871733570465872739291,21916650387363562186734621),
                        F(368290882408147051,442393380631568301)), 'genuine d5 fiber values')
require(fiber_stats[1]<F(1,3) and fiber_stats[2]>F(2,3) and fiber_stats[3]>F(2,3),
        'genuine d5 fiber obstruction inequalities')


def unconditional_parts(weights):
    u,a,b,c,t,d,v=weights
    parts=[]
    for i in range(u+1):
        for ell in range(t+1):
            mass=(comb(u,i)*F(factorial(i),factorial(i+c-1))*comb(t,ell)
                  *beta(a,b+t-ell)*beta(a+b+t-ell+u-i,i+ell+c+d+v+1)
                  *beta(c+i+ell+1,d)/F(c+i))
            parts.append((c+i-1,ell,mass))
    return parts


# Full actual-labelled-poset ideal recurrence, using no beta-mixture assumptions.
COVERS=((0,3),(1,2),(1,4),(2,3),(2,6),(3,5),(4,5))


def labelled_rank_histogram(weights):
    offsets=[]
    n=0
    for w in weights:
        offsets.append(n)
        n+=w
    predecessors=[0]*n
    for block,w in enumerate(weights):
        for j in range(1,w):
            predecessors[offsets[block]+j]|=1<<(offsets[block]+j-1)
    for i,j in COVERS:
        predecessors[offsets[j]]|=1<<(offsets[i]+weights[i]-1)
    full=(1<<n)-1
    x=offsets[3]+weights[3]-1
    tailmask=((1<<weights[6])-1)<<offsets[6]
    bins=weights[6]+1
    @lru_cache(None)
    def suffix(mask):
        if mask==full:
            return 1
        ans=0
        for element in range(n):
            bit=1<<element
            if not mask&bit and predecessors[element]&mask==predecessors[element]:
                ans+=suffix(mask|bit)
        return ans
    @lru_cache(None)
    def rank(mask):
        # Stop when x is available and count its insertion as one choice;
        # all other available labelled choices recurse separately.
        out=[0]*bins
        for element in range(n):
            bit=1<<element
            if not mask&bit and predecessors[element]&mask==predecessors[element]:
                nxt=mask|bit
                if element==x:
                    out[(mask&tailmask).bit_count()]+=suffix(nxt)
                else:
                    vals=rank(nxt)
                    for i,v in enumerate(vals):
                        out[i]+=v
        return tuple(out)
    histogram=rank(0)
    total=suffix(0)
    require(sum(histogram)==total,'actual rank bins sum to extension count')
    return histogram,total,suffix.cache_info().currsize


actual=[]
for weights in ((1,1,1,1,1,4,44),(2,1,2,3,2,4,44),
                (3,2,1,2,3,4,45),(1,3,4,1,2,4,44),
                (2,2,1,10,2,4,44),(1,1,1,100,1,4,44)):
    histogram,total,states=labelled_rank_histogram(weights)
    n=weights[6]
    moments,*_=component_mixture_stats(unconditional_parts(weights),4,n)
    reconstructed=[comb(n,j)*sum(((-1)**h*comb(n-j,h)*moments[j+h] for h in range(n-j+1)),F(0))
                   for j in range(n+1)]
    require(reconstructed==[F(h,total) for h in histogram], 'unconditional coefficient formula, all ranks')
    q=F(histogram[-1],total)
    p=F(histogram[-2],total)
    require(tail_bound(q,p,n),'actual poset nonlinear tail bound')
    require(F(histogram[1],total)<=F(5*n,(n+4)*(n+5)),'actual first atom')
    require(all(F(h,total)<=F(80,243) for h in histogram[2:-2]),'actual middle atoms')
    cdf=0
    balanced=[]
    for i in range(1,n+1):
        cdf+=histogram[i-1]
        if total<=3*cdf<=2*total:
            balanced.append(i)
    endpoint_assumptions=(3*histogram[0]<total and 3*histogram[-1]<total)
    if endpoint_assumptions:
        require(bool(balanced),'balanced x-F_i witness given endpoints')
    if q<=F(1,3):
        require(q+p<F(2,3),'actual tail threshold consequence')
    actual.append(dict(weights=weights,extension_count=str(total),visited_ideals=states,
                       Q=str(q),P=str(p),endpoint_assumptions=endpoint_assumptions,
                       balanced_tail_indices=balanced))

result=dict(verdict='PASS',component_checks=checks,mixture_checks=mixture_checks,
            first_atom_checks=first_checks,middle_peak_checks=middle_checks,
            threshold44_integer_margin=threshold44,
            threshold_polynomial=polynomial,
            d5_monomial_Q_A_C=[str(x) for x in mono[1:]],
            d5_genuine_fiber_Q_A_C=[str(x) for x in fiber_stats[1:]],
            unconditional_formula_histogram_checks=sum(x['weights'][6]+1 for x in actual),
            actual_posets=actual)
Path(__file__).with_name('results.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
