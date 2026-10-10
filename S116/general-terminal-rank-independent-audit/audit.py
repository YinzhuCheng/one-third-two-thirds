"""Independent exact audit: actual ideal DP and disjoint gap-simplex integrals.
No author imports. All checks use explicit exceptions and survive python -O.
"""
from functools import lru_cache
from fractions import Fraction as F
from itertools import product
from math import comb, factorial, prod
from pathlib import Path
import argparse, json

EDGES=((0,3),(1,2),(1,4),(2,3),(2,6),(3,5),(4,5))
PREDS=tuple(tuple(x for x,y in EDGES if y==i) for i in range(7))
def check(test, detail):
    if not test: raise RuntimeError(str(detail))

def extension_histograms(w):
    def children(s):
        for i in range(7):
            if s[i]<w[i] and all(s[p]==w[p] for p in PREDS[i]):
                yield i,s[:i]+(s[i]+1,)+s[i+1:]
    @lru_cache(None)
    def total(s):
        if s==w:return 1
        return sum(total(t) for _,t in children(s))
    def histogram(target):
        @lru_cache(None)
        def rec(s):
            result=[0]*(w[6]+1)
            for i,t in children(s):
                if (i,s[i])==target:result[s[6]]+=total(t)
                else:
                    for j,v in enumerate(rec(t)):result[j]+=v
            return tuple(result)
        result=rec((0,)*7)
        check(sum(result)==total((0,)*7),('DP histogram partition',w,target))
        return result
    return histogram((3,w[3]-1)),histogram((5,0)),total((0,)*7)

@lru_cache(None)
def powers(n,indices,dimension):
    if len(indices)==1:
        exps=[0]*dimension;exps[indices[0]]=n
        return ((tuple(exps),1),)
    result=[]
    for m in range(n+1):
        for exps,c in powers(n-m,indices[1:],dimension):
            e=list(exps);e[indices[0]]=m
            result.append((tuple(e),comb(n,m)*c))
    return tuple(result)

def multiply(poly,power):
    result={}
    for e,c in poly.items():
        for f,d in power:
            g=tuple(x+y for x,y in zip(e,f))
            result[g]=result.get(g,0)+c*d
    return result

def simplex_histogram(w):
    """Count N! times volume by expanding linear forms in simplex gaps.

    c=1: gaps of 0<r<s<x<z<1.
    c>=2: gaps of 0<r<s<p<x<z<1, p=bottom C3, x=top C3.
    z is bottom C5 in both cases. This is not the conditional-mixture code.
    """
    u,a,b,c,t,d,v=w
    dimension=5 if c==1 else 6
    base=[0]*dimension;base[0]=a-1;base[1]=b-1;base[-1]=d-1
    if c>=2:base[3]=c-2
    poly={tuple(base):1}
    poly=multiply(poly,powers(u,(0,1,2),dimension))
    poly=multiply(poly,powers(t,(1,2,3) if c==1 else (1,2,3,4),dimension))
    denom0=factorial(u)*factorial(a-1)*factorial(b-1)*factorial(t)*factorial(d-1)
    if c>=2:denom0*=factorial(c-2)
    result=[]
    for j in range(v+1):
        p=multiply(poly,powers(j,(2,) if c==1 else (2,3),dimension))
        p=multiply(p,powers(v-j,(3,4) if c==1 else (4,5),dimension))
        num=sum(coef*prod(factorial(x) for x in exps) for exps,coef in p.items())
        den=denom0*factorial(j)*factorial(v-j)
        value,rem=divmod(num,den)
        check(rem==0,('integral count noninteger',w,j,num,den))
        result.append(value)
    return tuple(result)

def beta(a,b):return F(factorial(a-1)*factorial(b-1),factorial(a+b-1))
def atom(n,j,a,b):return comb(n,j)*beta(a+j,b+n-j)/beta(a,b)
def rising(a,n):return prod(range(a,a+n))
def moment(a,b,n):return F(rising(a,n),rising(a+b,n))
def peak(n,j,b):
    critical=F(j*b,n-j)
    lo=critical.numerator//critical.denominator
    candidates={1,max(1,lo),max(1,lo+1),max(1,lo+2)}
    vals={a:atom(n,j,a,b) for a in candidates}
    return max(vals.values()),sorted(a for a,p in vals.items() if p==max(vals.values()))

def conditional_coeff(u,c,t,d,r,s):
    coefficients=[F(0)]*(u+t+1)
    L=1-s
    for i in range(u+1):
        A=comb(u,i)*s**(u-i)*L**i*F(factorial(i),factorial(i+c-1))
        for ell in range(t+1):
            B=comb(t,ell)*(s-r)**(t-ell)*L**ell*beta(ell+1,d)
            for j in range(ell+1):
                coefficients[i+j]+=A*B*comb(d+j-1,j)
    return coefficients

def structural(w):
    labels=[(i,j) for i,m in enumerate(w) for j in range(m)]
    reach=[[False]*7 for _ in range(7)]
    for x,y in EDGES:reach[x][y]=True
    for k in range(7):
        for x in range(7):
            for y in range(7):reach[x][y]=reach[x][y] or (reach[x][k] and reach[k][y])
    def lt(x,y):return (x[0]==y[0] and x[1]<y[1]) or reach[x[0]][y[0]]
    def down(x):return {y for y in labels if lt(y,x)}
    def up(x):return {y for y in labels if lt(x,y)}
    def chain(S):return all(x==y or lt(x,y) or lt(y,x) for x in S for y in S)
    F1,Fv,x,z=(6,0),(6,w[6]-1),(3,w[3]-1),(5,0)
    C5={p for p in labels if p[0]==5}
    C0C3={p for p in labels if p[0]==0 or p[0]==3 and p!=x}
    check(down(F1)<=down(x) and up(x)-up(F1)==C5 and chain(C5),('first endpoint',w))
    check(up(Fv)<=up(x) and down(x)-down(Fv)==C0C3 and chain(C0C3),('second endpoint',w))
    check(not lt(F1,x) and not lt(x,F1) and not lt(Fv,x) and not lt(x,Fv),('incomparability',w))
    if w[5]==1:
        check(up(Fv)==up(z)==set(),('third endpoint upsets',w))
        check(down(Fv)-down(z)=={(6,j) for j in range(w[6]-1)},('third endpoint difference',w))
    # Directly check quotient self-duality, not just weights permutation.
    sigma=(6,5,3,2,4,1,0)
    check(all(reach[i][j]==reach[sigma[j]][sigma[i]] for i in range(7) for j in range(7)), 'duality')

# Tiny exact polynomial arithmetic, including bivariate triangle identity.
def add(*ps):
    out={}
    for p in ps:
        for e,c in p.items():out[e]=out.get(e,F(0))+c
    return {e:c for e,c in out.items() if c}
def scale(p,c):return {e:c*x for e,x in p.items() if c*x}
def mul(*ps):
    out={(0,0):F(1)}
    for p in ps:
        out=multiply(out,tuple(p.items()))
    return {e:c for e,c in out.items() if c}
def lin(k=0,l=0,c=0):return {e:F(x) for e,x in [((1,0),k),((0,1),l),((0,0),c)] if x}
def shift_k(p,a):
    out={}
    for (i,j),c in p.items():
        for h in range(i+1):out[(h,j)]=out.get((h,j),F(0))+c*comb(i,h)*a**(i-h)
    return {e:c for e,c in out.items() if c}

def polynomial_checks():
    k=lambda c:lin(1,0,c)
    n=lambda c:lin(1,1,c)
    P=add(scale(mul(k(4),k(5),n(5),n(6)),11),
          scale(mul(k(1),n(2),k(5),n(6)),-144),
          scale(mul(k(1),n(2),k(4),n(5)),153),
          scale(mul(n(2),k(4),k(5),n(5)),-3))
    shifted=shift_k(P,5)
    check(all(x>0 for x in shifted.values()) and shifted[(0,0)]==3060,'triangle shifted polynomial positive')
    small=[]
    for a in range(5):
        q={j:sum(c*a**i for (i,j2),c in P.items() if j2==j) for j in range(3)}
        check(q[2]>0 and (a==0 and all(x>0 for x in q.values()) or q[1]**2-4*q[2]*q[0]<0),('triangle small k',a,q))
        small.append({str(j):str(v) for j,v in q.items()})
    results={}
    for B,N in ((2,5),(3,10),(4,30)):
        # P_B(n)=(B+1)product((B+1)n-r)-3B^2*n*product(Bn-r).
        lhs=scale(mul(*(lin(B+1,0,-r) for r in range(1,B+1))),B+1)
        rhs=scale(mul(lin(1,0,0),*(lin(B,0,-r) for r in range(1,B))),-3*B*B)
        q=add(lhs,rhs);shiftedq=shift_k(q,N)
        check(all(c>0 for c in shiftedq.values()),('threshold polynomial positivity',B,N))
        results[str(B)]={'threshold':N,'coefficients_ascending':[int(q.get((i,0),0)) for i in range(B+1)],'shifted_coefficients_ascending':[int(shiftedq.get((i,0),0)) for i in range(B+1)]}
    return results,small,{str(e):str(c) for e,c in sorted(shifted.items())}

def main(output):
    thresholds={1:5,2:10,3:30}
    grid=[(u,a,b,c,t,d,v) for u,a,b,t in product(range(1,3),repeat=4)
          for c in range(1,4) for d,vs in ((1,(4,5)),(2,(10,)),(3,(30,))) for v in vs]
    extras=[(1,1,1,8,1,1,4),(5,2,3,5,4,1,4),(2,3,4,7,2,1,5),
            (4,1,2,6,3,2,10),(1,2,1,12,1,3,30),(1,1,1,1,1,4,40),
            (10,1,2,2,1,1,4),(1,2,1,2,10,1,4),
            (2,1,2,2,2,1,2),(3,1,3,3,3,1,3)]
    records=[];triangle=0;atoms=0;crossings=0
    for w in grid+extras:
        h,z,Z=extension_histograms(w)
        check(h==simplex_histogram(w),('DP vs independent simplex integral',w,h,simplex_histogram(w)))
        structural(w)
        u,a,b,c,t,d,v=w
        lower=moment(c,d+1,v)
        check(F(h[-1],Z)>=lower,('product lower bound',w,F(h[-1],Z),lower))
        if d<=3 and v>=thresholds[d]:
            check(all(3*m<Z for m in h[1:-1]),('rank bound',w,h))
            atoms+=v-1
            if 3*h[0]<Z and 3*h[-1]<Z:
                prefix=0
                for i in range(v):
                    prefix+=h[i]
                    if 3*prefix>=Z:
                        check(3*prefix<2*Z,('rank crossing',w,i,prefix,Z));break
                crossings+=1
        if d==1 and v==4:
            A=F(h[3]+h[4],Z);B=1-F(h[4],Z);C=F(z[4],Z)
            check(12*A+15*B+C<F(56,3),('actual triangle certificate',w,A,B,C))
            check(F(h[1],Z)<=F(4,15) and F(h[2],Z)<=F(9,35),('small atoms',w))
            triangle+=1
        records.append({'weights':list(w),'extensions':Z,'top_C3_histogram':list(h),'bottom_C5_histogram':list(z),'product_lower_bound':str(lower)})
    maxima=[];peak_checks=0;ratio_checks=0
    for B,N in ((2,5),(3,10),(4,30)):
        for n in range(N,101):
            for j in range(1,n):
                p,where=peak(n,j,B)
                check(p<F(1,3),('all-alpha maximum',n,j,B,p,where));peak_checks+=1
            A=B*(n-1)
            last=F(n*B*prod(A+i for i in range(B)),prod(A+n-1+i for i in range(B+1)))
            check(last==atom(n,n-1,A,B)==atom(n,n-1,A+1,B),('last-rank product',n,B))
            check(last==peak(n,n-1,B)[0],('last-rank peak',n,B))
        n=N-1;p=atom(n,n-1,B*(n-1),B)
        check(p>F(1,3),('threshold sharpness',B,n,p))
        maxima.append({'beta':B,'preceding_n':n,'alpha':B*(n-1),'probability':str(p),'not_a_poset_counterexample':True})
    for n in range(2,26):
        for B in range(2,7):
            for j in range(1,n):
                for A in (1,2,5,13,41):
                    ratio=F((A+j)*(A+B),A*(A+B+n))
                    check(atom(n,j,A+1,B)==atom(n,j,A,B)*ratio,('ratio',n,j,A,B))
                    check((A+j)*(A+B)-A*(A+B+n)==j*B-(n-j)*A,'ratio sign');ratio_checks+=1
    check(peak(5,2,2)[0]==F(3,14) and peak(5,3,2)[0]==F(5,21),'n5 middle exceptions')
    check(peak(4,1,2)[0]==F(4,15) and peak(4,2,2)[0]==F(9,35),'n4 small atom exceptions')
    check(F(comb(6,2)*2**2*4**4,6**6)==F(80,243)<F(1,3),'binomial envelope base')
    check(F(5**6,6**6)>F(1,3),'beta5 limiting obstruction')
    check(atom(1000,999,4995,5)==F(9282007064732500,27702065542505871)>F(1,3),'beta5 finite obstruction')
    conditional=0
    for u,c,t,d in product(range(1,4),repeat=4):
        for r,s in ((F(1,5),F(3,5)),(F(1,7),F(6,7))):
            coeff=conditional_coeff(u,c,t,d,r,s)
            check(all(x>0 for x in coeff),('positive mixture',u,c,t,d,r,s))
            mass=sum(x*beta(c+i,d+1) for i,x in enumerate(coeff))
            mixing=[x*beta(c+i,d+1)/mass for i,x in enumerate(coeff)]
            check(sum(mixing)==1,'mixture normalization')
            for h in (F(1,5),F(1,2),F(4,5)):
                inner=sum(comb(u,i)*s**(u-i)*(1-s)**i*F(factorial(i),factorial(i+c-1))*h**(i+c-1) for i in range(u+1))
                outer=sum(comb(t,l)*(s-r)**(t-l)*(1-s)**l*sum((-1)**q*F(comb(d-1,q),l+q+1)*(1-h**(l+q+1)) for q in range(d)) for l in range(t+1))
                expected=h**(c-1)*(1-h)**d*sum(x*h**i for i,x in enumerate(coeff))
                check(inner*outer==expected,('direct integral vs positive polynomial',u,c,t,d,r,s,h))
            for n in (4,10):
                probabilities=[sum(m*atom(n,j,c+i,d+1) for i,m in enumerate(mixing)) for j in range(n+1)]
                check(sum(probabilities)==1,'conditional rank partition')
                check(probabilities[-1]>=moment(c,d+1,n),'conditional product lower bound')
            conditional+=1
    polynomials,small,shifted=polynomial_checks()
    # Exact boundary algebra for the outer-singleton corollary.
    for v,cap in ((2,2),(3,3)):
        check(moment(cap,2,v)<F(1,3) and moment(cap+1,2,v)>=F(1,3),('corollary integer cutoff',v,cap))
    finite_caps=[]
    for d,V,M in ((1,3,3),(2,9,19),(3,29,90)):
        at=moment(M,d+1,V);after=moment(M+1,d+1,V)
        check(at<F(1,3)<after,('finite region cap',d,V,M,at,after))
        finite_caps.append({'d':d,'v_cap':V,'c_cap':M,'ratio_at_cap':str(at),'ratio_after_cap':str(after)})
    check((90+90+29-1)//2==104 and 29+3+90+90+104+3+29==348,'finite region order bound')
    out={'finite_caps':finite_caps,'finite_region_t_cap':104,'finite_region_order_cap':348,'status':'PASS','independent_DP_simplex_matches':len(records),'structural_endpoint_vectors':len(records),'threshold_actual_atoms':atoms,'actual_rank_crossings':crossings,'actual_triangle_certificates':triangle,'all_alpha_peak_checks':peak_checks,'exact_ratio_checks':ratio_checks,'conditional_positive_mixture_checks':conditional,'threshold_polynomials':polynomials,'threshold_sharpness':maxima,'triangle_small_k_coefficients':small,'triangle_shifted_coefficients':shifted,'outer_singleton_corollary_caps':{'u,v':[2,3],'c_given_v2':2,'c_given_v3':3,'b_given_u2':2,'b_given_u3':3},'checks_use_assert':False,'records':records,'scope':'Finite exact implementation verification; unbounded proof and dependency review in AUDIT.md.'}
    Path(output).write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k!='records'},indent=2))

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--output',required=True)
    main(p.parse_args().output)
