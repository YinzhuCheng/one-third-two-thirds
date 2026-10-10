"""Independent exact audit. No author imports; checks survive python -O.

Two independent actual-extension constructions:
  (1) chain-prefix ideal states;
  (2) positive Dirichlet/simplex moment expansion.
"""
from functools import lru_cache
from fractions import Fraction as F
from itertools import product
from math import comb, factorial
from pathlib import Path
import argparse
import json

EDGES = ((0,3),(1,2),(1,4),(2,3),(2,6),(3,5),(4,5))
PREDS = tuple(tuple(p for p,q in EDGES if q == i) for i in range(7))

def check(ok, detail):
    if not ok:
        raise RuntimeError(str(detail))

def extension_histogram(w):
    def children(s):
        for i in range(7):
            if s[i] < w[i] and all(s[p] == w[p] for p in PREDS[i]):
                yield i, s[:i] + (s[i]+1,) + s[i+1:]
    @lru_cache(None)
    def total(s):
        if s == w:
            return 1
        return sum(total(t) for _,t in children(s))
    @lru_cache(None)
    def rank(s):
        hist = [0]*(w[6]+1)
        for i,t in children(s):
            if i == 3:
                hist[s[6]] += total(t)
            else:
                for j,c in enumerate(rank(t)):
                    hist[j] += c
        return tuple(hist)
    hist=rank((0,)*7)
    check(sum(hist)==total((0,)*7), ('rank partition',w))
    return hist

@lru_cache(None)
def ternary_power(m):
    """Integer coefficients of (x+y+z)^m."""
    return tuple((i,j,m-i-j,comb(m,i)*comb(m-i,j))
                 for i in range(m+1) for j in range(m-i+1))

def simplex_histogram(w):
    """Integrate 0<r<s<x<z<1 in gaps g0,...,g4.

    N! times event volume is integer numerator / denominator below.
    """
    u,a,b,one,t,one2,v = w
    check(one==one2==1, ('singleton restriction',w))
    facts = [factorial(i) for i in range(sum(w)+1)]
    hist=[]
    for j in range(v+1):
        numerator=0
        for p,q,l,c in ternary_power(u):
            for d,e,f,c2 in ternary_power(t):
                front=c*c2*facts[a-1+p]*facts[b-1+q+d]*facts[j+l+e]
                for k in range(v-j+1):
                    numerator += front*comb(v-j,k)*facts[f+k]*facts[v-j-k]
        denominator=facts[a-1]*facts[b-1]*facts[u]*facts[t]*facts[j]*facts[v-j]
        quotient,remainder=divmod(numerator,denominator)
        check(remainder==0, ('nonintegral simplex count',w,j))
        hist.append(quotient)
    return tuple(hist)

def beta_atom(n,j,k):
    # Integrate binomial(n,h) against normalized h^k(1-h).
    return F(comb(n,j)*(k+1)*(k+2)*factorial(j+k)*factorial(n-j+1),
             factorial(n+k+2))

def formula_atom(n,j,k):
    return F((n-j+1)*comb(k+j,j),comb(k+n+2,n))

def conditional_polynomial(u,t,r,s):
    coeff=[F(0)]*(u+t+1)
    for i in range(u+1):
        alpha=comb(u,i)*s**(u-i)*(1-s)**i
        for ell in range(t+1):
            beta=F(comb(t,ell),ell+1)*(s-r)**(t-ell)*(1-s)**ell
            for m in range(ell+1):
                coeff[i+m]+=alpha*beta
    return coeff

def rational_polynomial_value(coeff,h):
    return sum(c*h**k for k,c in enumerate(coeff))

def structural_arrows(w):
    labels=[(i,j) for i,m in enumerate(w) for j in range(m)]
    reach=[[False]*7 for _ in range(7)]
    for p,q in EDGES:
        reach[p][q]=True
    for k in range(7):
        for p in range(7):
            for q in range(7):
                reach[p][q] = reach[p][q] or (reach[p][k] and reach[k][q])
    def lt(p,q):
        return p[0]==q[0] and p[1]<q[1] or reach[p[0]][q[0]]
    def down(x):return {y for y in labels if lt(y,x)}
    def up(x):return {y for y in labels if lt(x,y)}
    def chain(c):return all(p==q or lt(p,q) or lt(q,p) for p in c for q in c)
    bot,x,top,z=(6,0),(3,0),(6,w[6]-1),(5,0)
    check(not lt(bot,x) and not lt(x,bot), ('bottom incomparable',w))
    check(not lt(top,x) and not lt(x,top), ('top incomparable',w))
    check(down(bot)<=down(x), ('lower inclusion',w))
    check(up(x)-up(bot)=={z}, ('lower difference',w))
    check(up(top)<=up(x), ('upper inclusion',w))
    check(down(x)-down(top)=={p for p in labels if p[0]==0}, ('upper difference',w))
    check(chain(up(x)-up(bot)) and chain(down(x)-down(top)), ('chain differences',w))


def main(output):
    count=0;crossings=0;worst=F(0);location=None;examples=[]
    grid=[(u,a,b,1,t,1,v) for u,a,b,t in product(range(1,5),repeat=4)
          for v in (5,6,7,8)]
    extra=[(u,a,b,1,t,1,v) for u,a,b,t,v in (
        (1,1,1,1,20),(10,1,2,3,5),(1,5,8,2,6),(6,3,2,7,8),
        (15,1,2,1,5),(1,1,2,15,5),(1,1,1,30,5),(30,1,1,1,5),
        (2,8,2,3,12),(2,2,10,3,12))]
    failure_cases=[]
    for w in grid+extra:
        hist=extension_histogram(w)
        simplex=simplex_histogram(w)
        check(hist==simplex, ('independent simplex mismatch',w,hist,simplex))
        structural_arrows(w)
        total=sum(hist);v=w[6]
        for j in range(1,v):
            p=F(hist[j],total)
            check(p<F(1,3), ('interior bound',w,j,p))
            if count<len(grid) and p>worst:
                worst=p;location=[list(w),j]
        q=[];partial=0
        for j in range(v):
            partial+=hist[j];q.append(F(partial,total))
        endpoints=3*hist[0]<total and 3*hist[-1]<total
        if endpoints:
            i=next(i+1 for i,p in enumerate(q) if p>=F(1,3))
            check(2<=i<=v-1 and q[i-1]<F(2,3), ('internal crossing',w,i,q))
            if count<len(grid):crossings+=1
        else:
            failure_cases.append({'weights':list(w),'rank_histogram':list(hist),
                                  'extension_count':total,'x_to_C6_probabilities':[str(p) for p in q]})
        if count>=len(grid):
            examples.append({'weights':list(w),'extension_count':total,'rank_histogram':list(hist)})
        count+=1
    beta_checks=0
    for n in range(5,61):
        for k in range(6*n+1):
            for j in range(1,n):
                p=beta_atom(n,j,k)
                check(p==formula_atom(n,j,k), ('beta formula',n,j,k))
                check(p<F(1,3), ('beta bound',n,j,k))
                beta_checks+=1
        for j in range(1,n):
            # The exact ratio sign proves this finite candidate set locates
            # the maximum over every k>=0, including all untested tail k.
            critical=F(3*j-n,n-j)
            lo=max(0,critical.numerator//critical.denominator)
            candidates=range(max(0,lo-1),lo+3)
            maximum=max(beta_atom(n,j,k) for k in candidates)
            check(maximum<F(1,3), ('all-k exact maximum',n,j,critical))
        max_last=F(4*n*(2*n-1),3*(3*n-2)*(3*n-1))
        check(beta_atom(n,n-1,2*n-3)==max_last, ('last maximum',n))
        check(beta_atom(n,n-1,2*n-2)==max_last, ('last plateau',n))
    check(beta_atom(4,3,5)==F(56,165)>F(1,3), 'n4 sharpness')
    conditional_checks=0
    for u,t in product(range(1,7),repeat=2):
        for r,s in ((F(1,5),F(2,5)),(F(1,7),F(6,7)),(F(2,3),F(3,4))):
            coeff=conditional_polynomial(u,t,r,s)
            check(all(c>0 for c in coeff), ('positive polynomial',u,t,r,s))
            mass=sum(c/F((k+1)*(k+2)) for k,c in enumerate(coeff))
            mixing=[c/F((k+1)*(k+2))/mass for k,c in enumerate(coeff)]
            check(sum(mixing)==1, ('mixture normalization',u,t,r,s))
            for h in (F(1,5),F(1,2),F(4,5)):
                direct=(s+(1-s)*h)**u * sum(F(comb(t,l),l+1)*(s-r)**(t-l)*(1-s)**l*(1-h**(l+1)) for l in range(t+1))
                poly=(1-h)*rational_polynomial_value(coeff,h)
                check(direct==poly, ('conditional density identity',u,t,r,s,h))
            for n in (5,6,10):
                probs=[sum(m*beta_atom(n,j,k) for k,m in enumerate(mixing)) for j in range(n+1)]
                check(sum(probs)==1 and all(p<F(1,3) for p in probs[1:-1]), ('conditional rank distribution',u,t,r,s,n))
                conditional_checks+=1
    out={'status':'PASS','actual_weight_vectors':count,'author_grid_vectors':len(grid),
         'independent_simplex_histogram_matches':count,'structural_arrow_pairs_checked':2*count,
         'author_grid_endpoint_crossings':crossings,'author_grid_largest_interior_atom':str(worst),
         'author_grid_largest_atom_location':location,'exact_beta_integral_formula_and_bound_checks':beta_checks,
         'conditional_positive_mixture_checks':conditional_checks,'large_asymmetric_examples':examples,
         'endpoint_failure_examples':failure_cases,'checks_use_assert':False,
         'scope':'Finite implementation audit only; infinite theorem independently audited in AUDIT.md.'}
    Path(output).write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if not k.endswith('examples')},indent=2))

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--output',required=True)
    main(parser.parse_args().output)
