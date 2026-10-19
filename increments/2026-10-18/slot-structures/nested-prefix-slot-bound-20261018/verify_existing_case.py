"""Exact formula checks only: one saved case and one specified abstract mixture.
No poset, filter, linear-extension, or parameter-family enumeration is performed.
"""
from fractions import Fraction as Q
import json
from pathlib import Path

out = Path(__file__).resolve().parent

def f(x):
    return f"{x.numerator}/{x.denominator}"

# This is the pre-existing tight case in slot-coverage-union/RESULT.md section 4.
a, b, k, l = 10, 190, 7, 9
p = [Q(1)]
for j in range(a):
    p.append(p[-1] * Q(a-j, a+b-j))
p.append(Q(0))
r = sum(p[1:k+1], Q(0))
s = sum(p[1:l+1], Q(0))
H = sum((i*p[i] for i in range(1,k+1)), Q(0))
ERT = sum(((2*i-1)*p[i] for i in range(1,k+1)), Q(0)) + k*sum(p[k+1:l+1], Q(0))
N = ERT+r
cov = ERT-r*s
gap = r*(r+1)-cov
D1 = sum((s*p[i]-sum(p[i+1:l+1], Q(0)) for i in range(1,k+1)), Q(0))
D2 = r*(1+r-p[k])-H
assert r == Q(996464317,19032468455)
assert s == Q(6154163621889,117544525178080)
assert N == Q(234277819681,2137173185056)
assert gap == Q(6550878543122831207,11414094221988575803400)
assert r == Q(a-(a-k)*p[k], b+1)
assert s == Q(a-(a-l)*p[l], b+1)
assert D1 >= 0 and D2 >= 0
assert gap == r*p[k]+D1+D2
assert gap == r*s+r*r+2*r-N
existing = {
    "parameters": {"a":a,"b":b,"k":k,"l":l},
    "r":f(r), "s":f(s), "N":f(N), "covariance":f(cov),
    "T_and_Cov_gap":f(gap), "p_k":f(p[k]),
    "lower_gap_bound_r_p_k":f(r*p[k]), "D1":f(D1), "D2":f(D2),
    "all_saved_values_match":True,
}

# Parent-specified abstract random-cap control. It is not an actual-poset claim.
pmf = {0:Q(1,2),1:Q(1,4),2:Q(1,8),3:Q(1,8)}
tail = [sum((w for j,w in pmf.items() if j>=h), Q(0)) for h in range(7)]
assert all(tail[u+v] <= tail[u]*tail[v] for u in range(4) for v in range(4))
mean = sum((j*w for j,w in pmf.items()), Q(0))
second = sum((j*j*w for j,w in pmf.items()), Q(0))
var = second-mean*mean
r_mix = mean/Q(10)
cov_mix = var/Q(10)
bound_mix = r_mix*(r_mix+1)
excess = cov_mix-bound_mix
assert (mean,var,r_mix,cov_mix,bound_mix,excess) == (Q(7,8),Q(71,64),Q(7,80),Q(71,640),Q(609,6400),Q(101,6400))
mixture = {
    "scope":"Abstract random-cap control only; not claimed realizable by the specified poset filters.",
    "J_pmf":{str(j):f(w) for j,w in pmf.items()},
    "K_pmf":{"0":"9/10","3":"1/10"},
    "J_tail_is_NBU":True,
    "EJ":f(mean),"VarJ":f(var),"ER":f(r_mix),
    "Cov_R_T":f(cov_mix),"r_r_plus_1":f(bound_mix),"excess":f(excess),
}
(out/'existing_case.json').write_text(json.dumps(existing, ensure_ascii=False, indent=2)+'\n')
(out/'random_cap_control.json').write_text(json.dumps(mixture, ensure_ascii=False, indent=2)+'\n')
print(json.dumps({"existing_case":existing,"random_cap_control":mixture}, ensure_ascii=False, indent=2))
