#!/usr/bin/env python3
"""Exact replay for FOURTH_RANK_TRADEOFF.md; Python standard library only."""
from fractions import Fraction as F
from functools import lru_cache
from math import comb, factorial, prod
import json


def check(condition, message):
    if not condition:
        raise RuntimeError(message)


def beta(a, b):
    check(a >= 1 and b >= 1, 'invalid beta arguments')
    return F(factorial(a-1)*factorial(b-1), factorial(a+b-1))


def moment(k, ell, d, j):
    # Cancel factorials in the rising-factorial ratio; only d factors remain.
    m = k+ell+2
    return F(k+1, k+j+1)*F(prod(m+i for i in range(d)),
                               prod(m+j+i for i in range(d)))


def monomial(k, ell, d, n):
    moments = [moment(k, ell, d, j) for j in range(n+1)]
    atoms = [comb(n,j)*sum((-1)**l*comb(n-j,l)*moments[j+l]
                          for l in range(n-j+1)) for j in range(n+1)]
    C = F(k+ell+d+1, k+ell+d+n+1)
    check(sum(atoms) == 1 and min(atoms) >= 0, 'bad rank law')
    return atoms, C


def actual_mixture(weights):
    u,a,b,c,t,d,n = weights
    entries = []
    for i in range(u+1):
        for ell in range(t+1):
            k = c+i-1
            weight = (comb(u,i)*F(factorial(i),factorial(i+c-1))
                      *comb(t,ell)*beta(a,b+t-ell)
                      *beta(a+b+t-ell+u-i,i+ell+c+d+n+1)
                      *beta(c+i+ell+1,d)/F(c+i))
            atoms,C = monomial(k,ell,d,n)
            entries.append((weight,atoms,C))
    total = sum(w for w,_,_ in entries)
    return ([sum(w*atoms[j] for w,atoms,_ in entries)/total
             for j in range(n+1)], sum(w*C for w,_,C in entries)/total)


PREDS = ((), (), (1,), (0,2), (1,), (3,4), (2,))


def actual_dp(weights):
    """Counts actual labelled extensions independently by consumed-chain states."""
    states = set()
    zero = (0,)*7
    def successors(state):
        for j in range(7):
            if state[j] < weights[j] and all(state[p] == weights[p] for p in PREDS[j]):
                nxt = list(state); nxt[j] += 1
                yield j,tuple(nxt)
    @lru_cache(None)
    def suffix(state):
        states.add(state)
        if state == weights:
            return 1
        return sum(suffix(nxt) for _,nxt in successors(state))
    denominator = suffix(zero)
    forward = {zero:1}
    ranks = [0]*(weights[6]+1)
    c_count = 0
    for state in sorted(states,key=sum):
        prefixes = forward.get(state,0)
        for j,nxt in successors(state):
            forward[nxt] = forward.get(nxt,0)+prefixes
            completions = prefixes*suffix(nxt)
            if j == 3 and nxt[3] == weights[3]:
                ranks[state[6]] += completions
            if j == 5 and nxt[5] == weights[5] and state[6] == weights[6]:
                c_count += completions
    check(sum(ranks) == denominator, 'DP rank partition')
    return [F(x,denominator) for x in ranks],F(c_count,denominator),len(states)


def exact_proof_checks():
    # The shifted polynomial certifies all n>=44, not a finite extrapolation.
    coefficients = [comb(5,j)*(5**j*223**(5-j)-3*4**j*179**(5-j))
                    for j in range(6)]
    check(coefficients == [175086646,226795165,19429030,642530,9515,53],
          'threshold polynomial identity')
    check(all(x>0 for x in coefficients), 'threshold polynomial positivity')
    check(218**5-3*175**5 < 0, 'n43 centered bound diagnostic')
    check(5**5>3*4**5 and 6**6<3*5**6, 'asymptotic barrier')
    check(F(80,243)<F(1,3), 'middle atoms')
    # Rational replay of the component identity and derivative identity.
    for n in (4,6,43,44,100,1000):
        for alpha in (1,2,5,20,100,492):
            m=alpha+2
            q=F(prod(alpha+i for i in range(5)),
                prod(alpha+n+i for i in range(5)))
            check(q < F(m,m+n)**5, 'centered product bound')
            for h in (1,2):
                lhs=F(m,m+n)**2-F(m-h,m+n-h)*F(m+h,m+n+h)
                rhs=F(h*h*n*(2*m+n),(m+n)**2*((m+n)**2-h*h))
                check(lhs==rhs and rhs>0,'pairwise identity')
        a,b=1-F(3,n),F(3,n)
        for z in (F(1,10),F(1,2),F(4,5),F(9,10),F(99,100)):
            D=a+b*z
            # Differentiate f'=5(1-z)/D-z/D^2 in z, then divide by dq/dz=5z^4.
            derived=(-6/D**2+2*b*z/D**3)/(5*z**4)
            stated=-(6*a+4*b*z)/(5*z**4*D**3)
            check(derived==stated and stated<0,'concavity identity')
        check(1+5*(1-F(1))/(a+b)-F(1)/(a+b)**2==0,'G derivative at one')
    lo=F(prod(172+i for i in range(5)),prod(215+i for i in range(5)))
    hi=F(prod(173+i for i in range(5)),prod(216+i for i in range(5)))
    check(lo==F(2207480,6660009)<F(1,3),'c172 boundary')
    check(hi==F(1480015,4440006)>F(1,3),'c173 boundary')
    return coefficients


def obstruction():
    ranks,C=monomial(491,0,5,100)
    Q,A=ranks[-1],sum(ranks[-2:])
    check(Q==F(646396283,1951717773), 'monomial Q')
    check(A==F(256619324351,384488401281), 'monomial A')
    check(C==F(497,597),'monomial top C')
    check(Q<F(1,3) and A>F(2,3) and C>F(2,3),'monomial obstruction')
    s,r=F(999,1000),F(1,2)
    entries=[]
    for k,ac in ((491,s),(492,(1-s)/492)):
        for ell,bc in ((0,s-r),(1,1-s)):
            weight=ac*bc*beta(k+ell+2,5)/(k+1)
            qs,ctop=monomial(k,ell,5,100)
            entries.append((weight,qs[-1],sum(qs[-2:]),ctop))
    W=sum(e[0] for e in entries)
    Q,A,C=[sum(e[0]*e[j] for e in entries)/W for j in (1,2,3)]
    check(Q==F(5975039402610052100339,18040870122675452479134),'actual-fiber Q')
    check(A==F(14627871733570465872739291,21916650387363562186734621),'actual-fiber A')
    check(C==F(368290882408147051,442393380631568301),'actual-fiber top C')
    check(Q<F(1,3) and A>F(2,3) and C>F(2,3),'actual-fiber obstruction')
    return {'Q':str(Q),'A':str(A),'C':str(C)}


def main():
    coefficients=exact_proof_checks()
    vectors=[(1,1,1,1,1,1,1),(2,1,2,1,2,1,3),(1,2,1,2,1,2,3),
             (2,1,1,1,1,4,2),(2,1,3,2,2,4,3),(2,3,2,3,1,5,3),
             (3,2,2,2,3,4,4),(1,1,1,1,1,4,44)]
    total_states=0
    for weights in vectors:
        atoms,C,count=actual_dp(weights)
        ma,mc=actual_mixture(weights)
        check(atoms==ma and C==mc,'actual law mismatch: '+str(weights))
        total_states+=count
    report={'status':'PASS','theorem':'d=4, v>=44 is excluded; dual a=4, u>=44',
            'threshold_shifted_coefficients':coefficients,
            'actual_law_vectors':len(vectors),'reachable_states':total_states,
            'd5_actual_fiber_obstruction':obstruction(),
            'scope':'Analytic proof is unbounded; DP checks validate exact-law implementation.'}
    print(json.dumps(report,indent=2))


if __name__=='__main__':
    main()
