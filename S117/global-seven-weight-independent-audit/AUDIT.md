> S117 publication note: this proof/review text records the completed research run. This lean edition retains proof texts, replay sources and selected small results; large generated ledgers, duplicate source snapshots, historical manifests and checksums are not bundled. For the exact retained/generated distinction, portable commands and prior proof links, use [the S117 guide](../README.zh-CN.md), [reproduction instructions](../REPRODUCE.md) and [dependency map](../DEPENDENCIES.md). Historical statements about material being stored refer to that research run; the package contents are listed in the guide.

# Independent audit: global seven-weight finite reduction

Date: 2026-10-10. **Final verdict: PASS for the stated global finite reduction and the final author source. No mathematical correction was required.**

## Accepted scope

For the quotient with covers 0<3; 1<2,4; 2<3,6; 3<5; 4<5, inflate the vertices by positive chains of lengths (u,a,b,c,t,d,v). If the actual uniform law on complete labelled linear extensions has no balanced incomparable pair, then

- a,d<=181 and a+d<=184;
- u,v>=2, u+v<=110, hence u,v<=108;
- b+c<=895, in particular b,c<=895, and t<=474;
- total order N<=1665.

The first line does not depend on the new fourth-terminal-rank theorem. The remaining lines use its core result d=4 => v<=43 and the dual a=4 => u<=43. These are deliberately loose, coherent bounds. No full census, all-seven-weight balance theorem, or conclusion for other quotients is established. The proof needs no sampled monotonicity or numerical extrapolation.

## 1. Audited inputs and strict gamma reduction

The actual-law terminal mixture, endpoint consequences, product inequalities, and caps V(1)=3,V(2)=9,V(3)=29 are independently PASS in `general-terminal-rank-independent-audit/AUDIT.md`. The stronger rank-chain probabilities and their binomial insertion bounds are independently PASS in `generalized-seven-core-shuffle-independent-audit/RANK_AND_INNER_SINGLETON_AUDIT.md`. The strict middle-shuffle bounds and original port inequalities are independently PASS in that directory's `AUDIT.md`. Earlier proof locations are resolved in the S117 dependency map.

These results give u,v>=2 and, writing B=b+c, m=min(u,v),

3 product_{i=0}^a(b+i) < product_{i=0}^a(b+u+i),
product_{r=1}^a(b+t+v+r)/(b+t+v+u+r) > 2/3,
2u<a+b+t+v, 2v<u+c+t+d, 2t<B+m,

as well as the dual product and rank-chain inequalities. The strict signs are essential because balancedness includes both endpoints 1/3 and 2/3. In particular, the stronger terminal comparison is T6<B5, not T6<T5. The source uses the correct audited stronger rank bound.

Set alpha_k=1/((3/2)^(1/k)-1), beta_k=1/(3^(1/(k+1))-1), gamma_k=alpha_k-2 beta_k-1. The product inequality implies

3 < product_{i=0}^a(1+u/(b+i)) <= (1+u/b)^(a+1),

hence b<beta_a u. For s=b+t+v, each rank-chain factor is at most (s+a)/(s+a+u), so its strict necessary product bound gives s+a>alpha_a u. Applying the actual-extension duality (u,a,b,c,t,d,v) -> (v,d,c,b,t,a,u), adding, and using the strict shuffle inequality gives

alpha_a u+alpha_d v < B+2t+u+v+a+d
 < 2B+u+v+m+a+d
 < (2 beta_a+1)u+(2 beta_d+1)v+m+a+d.

Therefore gamma_a u+gamma_d v<m+a+d. Every step has the necessary direction and strictness. This is an actual-poset necessary condition, not a claim that arbitrary quotient or deletion laws are uniform.

## 2. Elementary estimates for every integer k

The inequalities 1/x-1/2 < 1/(exp(x)-1) < 1/x-1/2+x/12 hold strictly for every x>0. An independent power-series proof of the lower bound uses

(x-2)exp(x)+x+2 = sum_{n>=3}(n-2)x^n/n! > 0.

For the upper bound, x^2-6x+12 is positive, and

(x^2-6x+12)(exp(x)-1)-12x
 = sum_{n>=5}(n-3)(n-4)x^n/n! > 0.

Thus there is no restricted small-x assumption hidden in the Bernoulli estimates.

Let A+=405466/10^6, L-=1098612/10^6, L+=1098613/10^6. Exact atanh-series bounds certify

405465/10^6 < log(3/2) < A+,
L- < log(3) < L+.

The independent checker uses 16 positive terms at z=1/5 or 1/2 and the geometric tail bound 2z^(2M+1)/((2M+1)(1-z^2)); the author's 12-term calculation also suffices. Define

C=1/A+ - 2/L-,
F(k)=Ck-2/L- -1/2-L+/(6(k+1)).

The preceding bounds give gamma_k>F(k). Exact rational checks prove C>16/25, F(2)>32/25-12/5, F(4)>11/50, and F(5)>87/100. Both F(k) and F(k)-(16k/25-12/5) increase for all k>=1: their discrete increments are their respective positive linear slopes plus L+/(6(k+1)(k+2)). At k=1, gamma_1=-sqrt(3)>-44/25, checked by 3*25^2<44^2. Consequently

gamma_k>16k/25-12/5 for every k>=1,
gamma_k>11/50 for k>=4,
gamma_k>87/100 for k>=5.

This establishes the infinite assertions analytically; it does not infer them from finitely many gamma evaluations.

## 3. Complete outer/port case division

Write S=a+d and P=u+v. All asymmetric cases can be reversed by the genuine full-extension duality, so no symmetry assumption about one fixed vector is needed.

If a,d>=5, subtract P/2 in the gamma inequality and use u,v>=2 with positive coefficients gamma_a-1/2,gamma_d-1/2. This gives 2(gamma_a+gamma_d-1)<S, hence 7S<290 and S<=41. Also (37/100)P<S, so 37P<4100 and P<=110. Thus each outer weight is at most 36 in this case.

If a<=3,d>=5, m<=u and the affine gamma estimates give

(16d-60)v < 25d+25a+(85-16a)u,
7d < 25a+120+(85-16a)u.

Here 85-16a>0, so substituting u<=V(a) is legitimate. The respective exact upper bounds on d are 50,92,181 for a=1,2,3. The resulting bound on v has form (25d+K)/(16d-60), with derivative (-1500-16K)/(16d-60)^2<0. At d=5 the strict bounds are 357/20,163/5,1273/20, giving v<=17,32,63. Thus the three (S,P) caps are (51,20),(94,41),(184,92).

If a=4,d>=6, m<=v gives gamma_4 u+(gamma_d-1)v<d+4. Both coefficients are positive. Using u,v>=2 yields 7d<259, so d<=36. The d=5 case and all d<=4 cases are immediate. These arguments already prove a,d<=181 and S<=184 without the fourth-rank theorem.

The only unbounded-port corner in this argument is (a,d)=(4,4). For a<=3,d=4, u is bounded and gamma_4>0 bounds v directly. For a=4,d>=5, writing out separately u>=v and v>=u shows

gamma_4 u+gamma_d v-min(u,v) > (9/100)max(u,v),

because gamma_4>22/100, gamma_d>87/100 and their sum exceeds 109/100. Thus this mixed case is already qualitatively port-bounded.

For the stated convenient explicit caps, the fourth-rank theorem gives V(4)=43. If a=4,d>=5, the preceding mixed-case rational inequality with u<=43 gives v<282/5, hence v<=56 and P<=99. If a,d<=4, P<=86. Together with the preceding cases, these cover every positive outer pair and prove P<=110. No all-outer-at-most-three census is needed for this finite reduction. The separately PASS outer-three exclusion can subsequently remove all a,d<=3; it does not repair or substitute for any part of this proof.

## 4. Inner and total-order bounds; integer endpoints

Set W=au+dv. The gamma line gives

16W<60P+25m+25S <= (145/2)P+25S.

Since log(3)>1 and exp(x)-1>x, beta_k<k+1. Therefore

B<W+P < (177/32)P+(25/16)S.

At P<=110,S<=184 the last expression is 895+15/16, so the integer B<=895. The strict inequality 2t<B+m with m<=55 gives 2t<=949 and t<=474. The stated individual b,c<=895 are safe (and loose).

Finally t<B/2+P/4 gives

N=P+S+B+t < (611/64)P+(107/32)S
 <=53293/32=1665+13/32.

Thus N<=1665. In particular, the final rational evaluation is 1665+13/32, not 1665+1/32. The audited final source has the correct value. No endpoint equality is inadvertently retained in any of these calculations.

## 5. Search-ready domain

The source's three branches with a<=d exhaust all outer pairs: a=1,2,3 with their respective d caps; a=4,d<=36; and 5<=a<=d,a+d<=41. The prescribed port caps and strict integer filter 16(au+dv)<60(u+v)+25min(u,v)+25(a+d) are necessary throughout.

For fixed (a,u), the product ratio product(b+i)/(b+u+i) increases strictly with b and tends to 1. The bound b<(a+1)u supplies a finite excluded upper bracket. Hence the allowed positive b values are exactly an initial integer interval, possibly empty. The analogous statement holds for c. For the rank filter, product(s+r)/(s+u+r) increases strictly to 1, so the least nonnegative passing integer R(a,u) exists; doubling and exact integer bisection can find it without irrational arithmetic.

Consequently the source interval

low=max(1,2u-a-b-v+1,2v-u-c-d+1,R(a,u)-b-v,R(d,v)-c-u),
high=floor((b+c+min(u,v)-1)/2)

is exactly the remaining set of integer t satisfying the indicated linear and rank-chain conditions. The +1 and -1 terms are correct. This is an exact domain for the listed necessary filters, not a sufficiency theorem for counterexamples. The paper accurately says it has not counted or exhausted the full seven-coordinate domain.

The subsequently added four-coordinate envelope counts are independently verified too. The audit enumerates both ordered outer pairs directly, rather than restoring duals from the author's a<=d list. It obtains 14,190 a<=d tuples, divided as 4,508 both-outer-at-most-four, 8,703 mixed, and 979 both-at-least-five. The direct ordered count is 25,526, divided as 6,400, 17,406, and 1,720. These count only (a,d,u,v) satisfying the declared necessary envelope and filters, not b,c,t choices or counterexamples.

## 6. Independent check and final status

`check.py` is a separate standard-library exact-arithmetic implementation, with no author imports and no floating point. Running `python check.py` reproduces `results.json`: **27 exact certificate checks PASS**. It verifies the rigorous logarithm intervals, all-k base inequalities, each case constant and strict floor, monotone rational port bounds, d=4 adjacent-product boundaries, final inner/middle caps, the exact N fraction, and the four-coordinate envelope counts. Finite arithmetic checks supplement the unbounded proofs above; they do not establish them by sampling.

Reviewed final source: `../global-seven-weight-reduction/GLOBAL_WEIGHT_BOUND.md`, together with `verify_global_bound.py`, the four-coordinate counting supplement and their result files. The author's final text accepts H4 as an established dependency; it no longer presents the global result as awaiting review.

The required independent fourth-rank audit is `../fourth-terminal-rank-independent-audit/AUDIT.md`, final verdict PASS. Its accepted theorem covers d=4,v>=44 with all five other weights arbitrary, and its genuine order-dual statement. It imports the previously PASS actual-law mixture and endpoint prerequisites, so there is no circular dependency on this global bound. Its ancillary d5 statements and mixture-coefficient formula are not inputs to the present theorem. The dependency chain is therefore complete.

This directory is the final concise audit record: `AUDIT.md`, `check.py`, and `results.json`. No full seven-coordinate census, remote write, archive layer, or repeated source replay is part of this audit.
