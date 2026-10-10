#!/usr/bin/env python3
"""Exact standard-library checks. Proof quantifiers are in the companion note."""
from collections import defaultdict
from fractions import Fraction as F
from functools import lru_cache
from itertools import product
from math import comb, factorial, prod
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent
COVERS = ((0,3),(1,2),(1,4),(2,3),(2,6),(3,5),(4,5))
Q = [[False]*7 for _ in range(7)]
for i,j in COVERS: Q[i][j] = True
for k in range(7):
    for i in range(7):
        for j in range(7): Q[i][j] = Q[i][j] or (Q[i][k] and Q[k][j])
PRED = [tuple(i for i in range(7) if Q[i][j]) for j in range(7)]

def require(test, message):
    if not test: raise RuntimeError(message)

def rising(a,n): return prod(range(a,a+n))
def beta(a,b): return F(factorial(a-1)*factorial(b-1), factorial(a+b-1))
def bb(n,j,a,b): return F(comb(n,j)*rising(a,j)*rising(b,n-j), rising(a+b,n))
def bb_integral(n,j,a,b): return comb(n,j)*beta(a+j,b+n-j)/beta(a,b)
def lastmax(n,b):
    return F(n*b*b,b+1)*F(prod(b*n-r for r in range(1,b)),prod((b+1)*n-r for r in range(1,b+1)))

def pmul(a,b):
    out=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): out[i+j]+=x*y
    return out

def polyprod(factors):
    out=[1]
    for f in factors: out=pmul(out,f)
    return out

def padd(a,b):
    out=[0]*max(len(a),len(b))
    for i,x in enumerate(a): out[i]+=x
    for i,x in enumerate(b): out[i]+=x
    return out

def shifted(a,N):
    return [sum(a[i]*comb(i,j)*N**(i-j) for i in range(j,len(a))) for j in range(len(a))]

def verify_beta():
    maxima=0; identities=0
    starts={2:5,3:10,4:30}
    shifts={2:[6,15,3],3:[96,1202,249,13],4:[603960,1425418,140683,4718,53]}
    for b,N in starts.items():
        p=[(b+1)*z for z in polyprod([[-r,b+1] for r in range(1,b+1)])]
        q=[0]+[-3*b*b*z for z in polyprod([[-r,b] for r in range(1,b)])]
        require(shifted(padd(p,q),N)==shifts[b],('polynomial',b))
        require(all(z>0 for z in shifts[b]),('positivity',b))
        for n in range(N,81):
            require(lastmax(n,b)<F(1,3),('lastbound',n,b))
            require(lastmax(n,b)==bb(n,n-1,b*(n-1),b),('lastformula',n,b))
            for j in range(1,n):
                threshold=F(j*b,n-j)
                floor=threshold.numerator//threshold.denominator
                candidates=sorted({max(1,floor),max(1,floor+1)})
                peak=max(bb(n,j,a,b) for a in candidates)
                require(peak<F(1,3),('all-alpha-maximum',n,j,b,candidates,peak))
                maxima+=1
                for a in candidates:
                    p0=bb(n,j,a,b)
                    require(p0==bb_integral(n,j,a,b),('integration',n,j,a,b))
                    require(bb(n,j,a+1,b)/p0==F((a+j)*(a+b),a*(a+b+n)),('ratio',n,j,a,b))
                    require((a+j)*(a+b)-a*(a+b+n)==(j-n)*a+j*b,('ratio-sign',n,j,a,b))
                    identities+=1
    sharp=[]
    for b,n,a,expected in [(2,4,6,F(56,165)),(3,9,24,F(1755,5236)),(4,29,112,F(1432049,4294719)),(5,1000,4995,F(9282007064732500,27702065542505871))]:
        p=bb(n,n-1,a,b)
        require(p==expected and p>F(1,3),('sharp',b,n,a,p))
        sharp.append({'beta':b,'n':n,'alpha':a,'last_interior_atom':str(p)})
    require(F(5,6)**6>F(1,3),'asymptotic-beta5')
    return {'all_alpha_maximum_checks':maxima,'integration_ratio_checks':identities,'sharpness':sharp,'positive_shift_coefficients':shifts}

def conditional_moments(u,c,t,d,r,s,m):
    L=1-s; B=s-r
    aa={i+c-1:comb(u,i)*s**(u-i)*L**i*F(factorial(i),factorial(i+c-1)) for i in range(u+1)}
    by={ell:comb(t,ell)*B**(t-ell)*L**ell for ell in range(t+1)}
    # Positive direct triangle integration, independently of the marginal expansion.
    def direct_moment(power):
        return sum(av*bv*beta(e+power+ell+2,d)/F(e+power+1) for e,av in aa.items() for ell,bv in by.items())
    dz=direct_moment(0)
    direct=direct_moment(m)/dz
    # Positive marginal polynomial after y=h+(1-h)q.
    bc={}
    for ell in range(t+1):
        bc[ell]=comb(t,ell)*L**ell*sum(comb(t-ell,q)*B**(t-ell-q)*L**q*beta(q+1,d+ell) for q in range(t-ell+1))
    coeff=defaultdict(F)
    for e,av in aa.items():
        for ell,bv in bc.items(): coeff[e+ell]+=av*bv
    require(all(e>=c-1 and x>0 for e,x in coeff.items()),'positive-supported-mixture')
    weights={e+1:cv*beta(e+1,d+1) for e,cv in coeff.items()}
    mz=sum(weights.values())
    mixture=sum(w*F(rising(a,m),rising(a+d+1,m)) for a,w in weights.items())/mz
    require(dz==mz,'marginal-normalization')
    require(mixture==direct,('conditional-moment',u,c,t,d,r,s,m))
    require(mixture>=F(rising(c,m),rising(c+d+1,m)),('moment-support-bound',u,c,t,d,m))
    return mixture

def verify_mixture():
    checks=0
    for u,c,t,d in product(range(1,4),range(1,5),range(1,4),range(1,5)):
        for r,s in [(F(1,5),F(2,5)),(F(1,4),F(3,4)),(F(2,7),F(4,7))]:
            for m in range(7): conditional_moments(u,c,t,d,r,s,m);checks+=1
    return checks

def less(x,y): return (x[0]==y[0] and x[1]<y[1]) or Q[x[0]][y[0]]
def labels(w): return [(i,j) for i in range(7) for j in range(1,w[i]+1)]
def chain(S): return all(x==y or less(x,y) or less(y,x) for x in S for y in S)
def forced_arrows(w):
    V=labels(w)
    D={x:{z for z in V if less(z,x)} for x in V}
    U={x:{z for z in V if less(x,z)} for x in V}
    return [(x,y) for x in V for y in V if x!=y and not less(x,y) and not less(y,x) and ((D[x]<=D[y] and chain(U[y]-U[x])) or (U[y]<=U[x] and chain(D[x]-D[y])))]

def closed_total(w):
    u,a,b,c,t,d,v=w
    return sum(comb(b+j-1,j)*comb(a+b+i+j-1,i)*comb(u-i+c+t-j,t-j)*comb(u-i+c+t-j+d+v,v) for i in range(u+1) for j in range(t+1))

def count_poset(w, all_pairs=False):
    w=tuple(w); zero=(0,)*7
    @lru_cache(None)
    def transitions(s):
        out=[]
        for i in range(7):
            if s[i]<w[i] and all(s[j]==w[j] for j in PRED[i]):
                z=list(s);z[i]+=1;out.append((i,tuple(z)))
        return tuple(out)
    @lru_cache(None)
    def suffix(s):
        if s==w: return 1
        return sum(suffix(z) for _,z in transitions(s))
    Z=suffix(zero)
    pref={zero:1}
    # suffix visited precisely every reachable state, but expose via explicit layers.
    layers={zero}
    hist=[0]*(w[6]+1); cv=0; counts=defaultdict(int)
    for step in range(sum(w)):
        nxt=set()
        for s in sorted(layers):
            for i,z in transitions(s):
                nxt.add(z);pref[z]=pref.get(z,0)+pref[s]
                ways=pref[s]*suffix(z)
                if i==3 and z[3]==w[3]: hist[s[6]]+=ways
                if i==5 and z[5]==w[5] and s[6]==w[6]: cv+=ways
                if all_pairs:
                    x=(i,z[i])
                    for j in range(7):
                        if j==i or Q[i][j] or Q[j][i]: continue
                        for q in range(s[j]+1,w[j]+1): counts[(x,(j,q))]+=ways
        layers=nxt
    require(pref[w]==Z and sum(hist)==Z,('extension-count',w))
    require(Z==closed_total(w),('independent-closed-total',w))
    return Z,hist,cv,counts,suffix.cache_info().currsize

def verify_structural(w):
    V=labels(w);x=(3,w[3]);f1=(6,1);fv=(6,w[6])
    D=lambda z:{q for q in V if less(q,z)}
    U=lambda z:{q for q in V if less(z,q)}
    require(D(f1)<=D(x),'bottom-inclusion')
    require(U(x)-U(f1)=={q for q in V if q[0]==5},'bottom-difference')
    require(D(x)-D(fv)=={q for q in V if q[0]==0 or(q[0]==3 and q[1]<w[3])},'top-difference')
    require(chain(D(x)-D(fv)) and U(fv)<=U(x),'top-criterion')
    if w[5]==1:
        z=(5,1)
        require(U(z)==U(fv)==set(),'last-empty-upsets')
        require(D(fv)-D(z)=={(6,j) for j in range(1,w[6])},'last-chain-difference')

def verify_actual():
    cases=set(product(range(1,3),repeat=7))
    # Arbitrary non-singleton C3 at every theorem threshold.
    for u,a,b,c,t,d in product(range(1,3),range(1,3),range(1,3),range(1,5),range(1,3),range(1,4)):
        cases.add((u,a,b,c,t,d,{1:5,2:10,3:30}[d]))
    # Four-tail certificate lifted to arbitrary c, on a broader asymmetric box.
    for u,a,b,c,t in product(range(1,4),range(1,3),range(1,3),range(1,5),range(1,4)):
        cases.add((u,a,b,c,t,1,4))
    maxstates=0;four=0;atom=0;cross=0;dual=0
    largest=None
    for w in sorted(cases):
        Z,h,C,_,states=count_poset(w);maxstates=max(maxstates,states)
        verify_structural(w)
        n=w[6];c=w[3];d=w[5]
        require(F(h[n],Z)>=F(rising(c,n),rising(c+d+1,n)),('actual-product',w))
        if d in {1,2,3} and n>={1:5,2:10,3:30}[d]:
            require(all(3*z<Z for z in h[1:n]),('actual-rank-atoms',w))
            atom+=1
            peak=max(F(z,Z) for z in h[1:n])
            if largest is None or peak>F(largest['value']):largest={'value':str(peak),'weights':w}
            if 3*(Z-h[0])>2*Z and 3*(Z-h[n])>2*Z:
                q=[sum(h[:i]) for i in range(1,n+1)]
                witnesses=[i+1 for i,z in enumerate(q) if Z<=3*z<=2*Z]
                require(any(2<=i<=n-1 for i in witnesses),('rank-crossing',w));cross+=1
        if d==1 and n==4:
            A=sum(h[3:]);B=Z-h[4]
            require(3*(12*A+15*B+C)<56*Z,('four-tail-certificate',w))
            require(F(h[1],Z)<=F(4,15) and F(h[2],Z)<=F(9,35),('four-tail-atoms',w));four+=1
        if max(w)<=2:
            wd=(w[6],w[5],w[3],w[2],w[4],w[1],w[0])
            Zd,_,_,_,_=count_poset(wd)
            require(Zd==Z,('duality',w));dual+=1
    return {'vectors':len(cases),'maximum_reachable_states':maxstates,'threshold_vectors':atom,'endpoint_crossings':cross,'four_tail_vectors':four,'duality_checks':dual,'largest_threshold_interior_atom':largest}

def reduced_vectors():
    return [(u,1,b,c,t,1,v) for u,v in product((2,3),repeat=2) for b in range(1,u+1) for c in range(1,v+1) for t in range(1,5) if 2*u<1+b+t+v and 2*v<u+c+t+1 and 2*t<b+c+u and 2*t<b+c+v]

def verify_reduced():
    vectors=reduced_vectors();require(len(vectors)==41,'reduced-count')
    require(max(map(sum,vectors))==18,'reduced-max-order')
    records=[];port_counts=defaultdict(int)
    for w in vectors:
        Z,h,C,pairs,_=count_poset(w,True)
        balanced=[(x,y,N) for (x,y),N in pairs.items() if Z<=3*N<=2*Z]
        require(bool(balanced),('reduced-balanced',w))
        balanced.sort(key=lambda r:(abs(2*r[2]-Z),r[0],r[1]))
        fail=[(x,y,pairs[(x,y)]) for x,y in forced_arrows(w) if 3*pairs[(x,y)]<=2*Z]
        require(bool(fail),('reduced-forced',w))
        x,y,N=balanced[0];fx,fy,fn=fail[0]
        records.append({'weights':w,'extensions':Z,'balanced_pair':[x,y],'probability':str(F(N,Z)),'failed_forced_arrow':[fx,fy],'forced_arrow_probability':str(F(fn,Z))})
        port_counts[f'{w[0]},{w[6]}']+=1
    require(dict(port_counts)=={'2,2':7,'2,3':7,'3,2':7,'3,3':20},'port-counts')
    (HERE/'reduced_41_certificate.json').write_text(json.dumps(records,indent=2,sort_keys=True)+'\n')
    return {'vectors':41,'maximum_order':18,'counts_by_ports':dict(port_counts),'balanced_pair_witnesses':41,'failed_forced_arrow_witnesses':41}

def verify_small_outer_spine_caps():
    records=[]
    for d,V,M in [(1,3,3),(2,9,19),(3,29,90)]:
        at=F(rising(M,d+1),rising(M+V,d+1))
        after=F(rising(M+1,d+1),rising(M+1+V,d+1))
        require(at<F(1,3)<after,('finite-cap-boundary',d,V,M))
        records.append({'outer_spine':d,'terminal_cap':V,'adjacent_spine_cap':M,'ratio_at_cap':str(at),'ratio_after_cap':str(after)})
    require((90+90+29-1)//2==104,'middle-chain-cap')
    require(29+3+90+90+104+3+29==348,'total-order-cap')
    return {'bounds':records,'maximum_middle_chain':104,'maximum_total_order':348,'scope':'Necessary region for a,d <= 3, not an all-balanced theorem.'}

def main():
    result={'beta_checks':verify_beta(),'conditional_moment_checks':verify_mixture(),'actual_extension_checks':verify_actual(),'five_parameter_reduction':verify_reduced(),'small_outer_spine_caps':verify_small_outer_spine_caps()}
    (HERE/'verification.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(json.dumps(result,indent=2,sort_keys=True))
if __name__=='__main__': main()
