#!/usr/bin/env python3
"""Exact verification for the fixed N-base and its A1/Bj common mixture.

Standard library only. The formula, direct state DP, and fully expanded
element enumeration are separate implementations. No external services.
"""
from fractions import Fraction
from functools import lru_cache
from itertools import product
from math import comb
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent


def C(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def mixture(a, b, c, d):
    tail = [C(c-k+d-1, c-k) for k in range(c+1)]
    weights = [C(a+b+k, a+k) * tail[k] for k in range(c+1)]
    E = sum(weights)
    # A1 after Bj requires the first j prefix letters to be B.
    ps = [Fraction(E-sum(C(a+b+k-j, a+k)*tail[k]
                        for k in range(c+1)), E)
          for j in range(b+2)]
    h = sum(Fraction(weights[k], E)*Fraction(a+k, a+b+k)
            for k in range(c+1))
    coarse_h = Fraction(a+c, a+b+c)
    j = min(range(1, b+1), key=lambda x: (abs(ps[x]-Fraction(1,2)), x))
    return E, ps, h, coarse_h, j


def state_dp(a, b, c, d):
    """Count legal extensions directly, without any k-decomposition."""
    target = (a,b,c,d)
    @lru_cache(None)
    def suffix(s):
        if s == target:
            return 1
        i,j,k,l = s
        ans = 0
        if i < a: ans += suffix((i+1,j,k,l))
        if j < b: ans += suffix((i,j+1,k,l))
        if k < c and i == a: ans += suffix((i,j,k+1,l))
        if l < d and i == a and j == b: ans += suffix((i,j,k,l+1))
        return ans
    E = suffix((0,0,0,0))
    # Before A1 the only eligible elements are B1,B2,... .
    ps = [Fraction(0)] + [Fraction(E-suffix((0,j,0,0)),E)
                         for j in range(1,b+1)] + [Fraction(1)]
    return E, ps


def expanded_enumeration(a, b, c, d):
    """Enumerate labeled-element topological sorts, not block states."""
    lengths=(a,b,c,d)
    elems=[(v,i) for v,m in enumerate(lengths) for i in range(1,m+1)]
    index={x:i for i,x in enumerate(elems)}
    base={(0,2),(0,3),(1,3)}
    pred=[]
    for v,i in elems:
        mask=0
        for u,j in elems:
            if (u==v and j<i) or (u,v) in base:
                mask |= 1 << index[(u,j)]
        pred.append(mask)
    full=(1 << len(elems))-1
    E=0
    nums=[0]*(b+1)
    a1=index[(0,1)]
    bs=[index[(1,j)] for j in range(1,b+1)]
    order=[]
    def visit(mask):
        nonlocal E
        if mask==full:
            E+=1
            pos={x:i for i,x in enumerate(order)}
            for j,bj in enumerate(bs,1):
                nums[j] += pos[a1] < pos[bj]
            return
        for i in range(len(elems)):
            bit=1 << i
            if not mask & bit and pred[i] & mask == pred[i]:
                order.append(i)
                visit(mask | bit)
                order.pop()
    visit(0)
    return E, [Fraction(0)]+[Fraction(nums[j],E) for j in range(1,b+1)]+[Fraction(1)]


def serialize_example(a,b,c,d,t=None):
    E,ps,h,H,j=mixture(a,b,c,d)
    out={"lengths":[a,b,c,d], "extensions":E, "selected_pair":["A1",f"B{j}"],
         "j":j, "p_A1_before_Bj":str(ps[j]),
         "pair_balance":str(min(ps[j],1-ps[j])), "exact_max_jump":str(h),
         "exact_lower_bound":str(Fraction(1,2)-h/2),
         "coarse_lower_bound":str(Fraction(1,2)-H/2)}
    if t is not None: out["t"]=t
    return out


def main():
    dp_cases=0
    probability_checks=0
    boundary_checks=0
    for a,b,c,d in product(range(1,8),range(1,10),range(1,5),range(1,5)):
        E,ps,h,H,j=mixture(a,b,c,d)
        E2,ps2=state_dp(a,b,c,d)
        assert E==E2 and ps==ps2, (a,b,c,d)
        jumps=[ps[x]-ps[x-1] for x in range(1,b+2)]
        assert max(jumps)==h==ps[1]
        assert all(x>=y for x,y in zip(jumps,jumps[1:]))
        assert h < H  # c>0, all mixture weights positive, b>0
        assert min(ps[j],1-ps[j]) >= Fraction(1,2)-h/2
        assert Fraction(1,2)-h/2 >= Fraction(1,2)-H/2
        if c==1:
            S=d*(a+1)+a+b+1
            for k in range(b+2):
                expected=1-(1-Fraction(k,S))*Fraction(C(a+b-k,a),C(a+b,a))
                assert ps[k]==expected
            assert h==Fraction(a,a+b)+Fraction(b,(a+b)*S)
        if c==d==1:
            assert h==Fraction((a+1)*(2*a+b),(a+b)*(2*a+b+2))
            assert h <= Fraction(a+1,a+b+1)
        # Exact stochastic-effect check when D gets one extra element.
        _,pnext,hnext,_,_=mixture(a,b,c,d+1)
        assert all(pnext[k]<ps[k] for k in range(1,b+1))
        assert hnext<h
        dp_cases+=1
        probability_checks+=b
        boundary_checks+=2
    enum_cases=0
    enum_extensions=0
    for a,b,c,d in product(range(1,4),range(1,4),range(1,3),range(1,3)):
        E,ps,*_=mixture(a,b,c,d)
        E2,ps2=expanded_enumeration(a,b,c,d)
        assert E==E2 and ps==ps2
        enum_cases+=1
        enum_extensions+=E
    examples=[]
    for c,d in [(1,1),(3,2)]:
        for t in range(5):
            examples.append(serialize_example(2**t,2*3**t,c,d,t))
    summary={"status":"PASS", "arithmetic":"integers and fractions.Fraction only",
             "dp_parameter_ranges":{"a":[1,7],"b":[1,9],"c":[1,4],"d":[1,4]},
             "dp_cases":dp_cases,"actual_pair_probability_checks":probability_checks,
             "sentinel_boundary_checks":boundary_checks,
             "expanded_element_enumeration_ranges":{"a":[1,3],"b":[1,3],"c":[1,2],"d":[1,2]},
             "expanded_element_enumeration_cases":enum_cases,
             "enumerated_extensions":enum_extensions,
             "checks":["total E", "all A1/Bj probabilities", "common mixture",
                       "decreasing grid jumps", "sharp jump identity", "claimed lower bounds",
                       "deterministic witness", "c=1 closed form", "D-length stochastic tilt"],
             "examples":examples}
    (ROOT/"verification.json").write_text(json.dumps(summary,indent=2,ensure_ascii=False)+"\n")
    print(json.dumps({k:v for k,v in summary.items() if k!="examples"},indent=2,ensure_ascii=False))
    print("\nExact witness examples:")
    for x in examples:
        print(x)


if __name__=="__main__": main()
