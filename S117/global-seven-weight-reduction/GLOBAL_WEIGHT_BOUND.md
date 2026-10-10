> S117 publication note: this proof/review text records the completed research run. This lean edition retains proof texts, replay sources and selected small results; large generated ledgers, duplicate source snapshots, historical manifests and checksums are not bundled. For the exact retained/generated distinction, portable commands and prior proof links, use [the S117 guide](../README.zh-CN.md), [reproduction instructions](../REPRODUCE.md) and [dependency map](../DEPENDENCIES.md). Historical statements about material being stored refer to that research run; the package contents are listed in the guide.

# Finite reduction for all seven chain weights

Date: 2026-10-10. Status: complete direct author proof, using the audited structural, product, rank-chain, shuffle, and terminal-rank results. The fourth-terminal-rank theorem now has an independent PASS audit at `../fourth-terminal-rank-independent-audit/AUDIT.md`. The new global reduction has its own separate independent audit. No complete seven-core exclusion or exhaustive census is claimed here.

**Theorem. Every seven-core chain inflation without a balanced incomparable pair has total order at most 1665.** All seven chain weights are unrestricted in the theorem statement. This turns the entire seven-weight problem into an explicit finite domain; it does not exclude the points in that domain.

## 1. Setup and necessary inequalities

The quotient has covers 0<3; 1<2,4; 2<3,6; 3<5; 4<5. Its chain lengths are `(u,a,b,c,t,d,v)`, all positive integers. A counterexample means that the actual uniform complete-extension law has no incomparable pair with probability in the closed interval [1/3,2/3]. Write

- m=min(u,v), P=u+v, S=a+d, W=au+dv, B=b+c;
- A=log(3/2), L=log(3);
- alpha_k=1/(exp(A/k)-1), beta_k=1/(exp(L/(k+1))-1);
- gamma_k=alpha_k-2 beta_k-1.

Audited prerequisites, summarized in `../outer-three-census/THEOREM.md`, give u,v>=2 and

3 product_(i=0)^a(b+i) < product_(i=0)^a(b+u+i),
3 product_(i=0)^d(c+i) < product_(i=0)^d(c+v+i),             (1)

product_(r=1)^a (b+t+v+r)/(b+t+v+u+r) > 2/3,
product_(r=1)^d (c+t+u+r)/(c+t+u+v+r) > 2/3,                (2)

2u<a+b+t+v, 2v<u+c+t+d, 2t<B+m.                           (3)

The first three terminal-rank results say

V(1)=3, V(2)=9, V(3)=29;
 a<=3 => u<=V(a), d<=3 => v<=V(d).                       (4)

The order-reversing bijection sends `(u,a,b,c,t,d,v)` to `(v,d,c,b,t,a,u)`. Every use of symmetry below is this actual full-extension duality.

### Exact derivation of the gamma inequality

From (1),

3 < product_(i=0)^a(1+u/(b+i)) <= (1+u/b)^(a+1),

so b<beta_a u; similarly c<beta_d v. Put s=b+t+v. The factors (s+r)/(s+u+r) increase with r, so (2) implies

2/3 < [(s+a)/(s+a+u)]^a,

hence s+a>alpha_a u. Adding the dual inequality yields

alpha_a u+alpha_d v < B+2t+P+S
                        < 2B+P+m+S
                        < (2 beta_a+1)u+(2 beta_d+1)v+m+S.

Therefore every counterexample satisfies the strict necessary inequality

gamma_a u+gamma_d v < m+S.                                (5)

The proof uses the actual rank-chain probabilities through (2); it does not replace their induced outside-extension law by a uniform deletion law.

## 2. Elementary rational estimates for all gamma_k

For every real x>0,

1/x-1/2 < 1/(exp(x)-1) < 1/x-1/2+x/12.                   (6)

For completeness, set y=x/2. The left inequality is y cosh(y)>sinh(y), since the difference vanishes at zero and has derivative y sinh(y)>0. For the right inequality, multiply coth(y)<1/y+y/3 by 3y sinh(y). Its positive difference is

(3+y^2)sinh(y)-3y cosh(y)
 = sum_(n>=2) 4n(n-1)y^(2n+1)/(2n+1)! >0.

The following rational logarithm brackets suffice:

405465/10^6 < A < 405466/10^6,
1098612/10^6 < L < 1098613/10^6.                           (7)

They follow, with exact rational arithmetic, from the first twelve terms of

log(x)=2 sum_(j>=0) z^(2j+1)/(2j+1), z=(x-1)/(x+1),

and the remainder bound

0<R_M<2 z^(2M+1)/[(2M+1)(1-z^2)].

Here z=1/5 or 1/2 and M=12. The companion verifier checks both bounds without floating point.

Put A_+=405466/10^6, L_-=1098612/10^6, L_+=1098613/10^6 and C=1/A_+-2/L_-. Applying (6) gives, for every integer k>=1,

gamma_k > F(k) := Ck-2/L_- -1/2-L_+/[6(k+1)].             (8)

Exact rational checks give C>16/25,

F(2) > 32/25-12/5, F(4)>11/50, F(5)>87/100.              (9)

The function F(k) increases with k because C>0. Moreover F(k)-(16k/25-12/5) increases with k. Thus (9) proves the first bound below for every k>=2. At k=1, gamma_1=-sqrt(3)>-44/25=16/25-12/5, since 3*25^2<44^2. Consequently:

gamma_k > 16k/25-12/5                    for all k>=1;
gamma_k > 11/50                         for all k>=4;
gamma_k > 87/100                        for all k>=5.    (10)

These are proved uniform estimates, not numerical extrapolations or finite tests of an infinite assertion.

## 3. Unconditional bounds on the outer weights

### Both a,d>=5

Subtract m<=P/2 in (5). Since gamma_a-1/2 and gamma_d-1/2 are positive, u,v>=2 give

2(gamma_a+gamma_d-1) < S.

Using the first estimate (10),

(32/25)S-58/5 < S, hence 7S<290.

Thus S<=41. The last estimate (10) also gives

(37/100)P < S<=41,

hence P<=110. In particular each outer weight is at most 36 in this case.

### One outer weight a<=3 and the other d>=5

By duality it suffices to use this orientation. Since m<=u, (5) and (10) imply

(16d-60)v < 25d+25a+(85-16a)u.                           (11)

Using v>=2 gives

7d < 25a+120+(85-16a)u.                                  (12)

Substituting u<=V(a) gives the exact integer upper bounds

(a,V(a), maximum d) = (1,3,50), (2,9,92), (3,29,181).     (13)

For later use, the right-side bound on v in (11), after substituting V(a), is a decreasing function of real d>=5. Indeed (25d+K)/(16d-60) has derivative (-1500-16K)/(16d-60)^2<0. At d=5 this yields

(a, maximum v) = (1,17), (2,32), (3,63).                  (14)

These bounds are unconditional.

### One outer weight a=4

For d>=6, gamma_d-1>0 by (10), while gamma_4>11/50. Subtracting m<=v in (5) and using u,v>=2 gives

2 gamma_4 + 2(gamma_d-1) < d+4,

hence (7/25)d<259/25, or d<37. Thus d<=36. The cases d<=5 already satisfy this bound. By duality, any pair containing a 4 and an outer weight at least 4 has both outer weights at most 36. A pair (4,d) with d<=3 is already covered by the finite small side and, of course, has sum at most 7.

### Global unconditional conclusion

Every counterexample satisfies

a<=181, d<=181, S=a+d<=184.                              (15)

No fourth-terminal-rank assertion was used in proving (15).

In fact (5) already bounds every port pair except the corner a=d=4. For a<=3,d=4, (5) with gamma_4>11/50 and u<=V(a) bounds v. For a=4,d>=5, both gamma coefficients are positive and their sum exceeds 109/100; for any positive u,v,

gamma_4 u+gamma_d v-min(u,v) > (9/100)max(u,v).

This follows separately for u>=v and v>=u by evaluating the smaller coefficient in each linear expression. Since S<=40 in this case, both ports are bounded. The corner (4,4) is the only port-unbounded region left by this argument. This observation is qualitative; the full explicit rectangle below uses the new fourth-rank cap.

## 4. Full finite region using the fourth-terminal-rank theorem

Accepted theorem H4: every counterexample with d=4 has v<=43. Its dual says a=4 => u<=43. The proof source is `../fourth-terminal-rank-barrier/FOURTH_RANK_TRADEOFF.md`, and its independent PASS review is `../fourth-terminal-rank-independent-audit/AUDIT.md`. This is now a proved dependency, not an open hypothesis. The proof only needs its unrestricted d4 cap; ancillary d5 formulas are not required.

Define V(4)=43. For a=4,d>=5, the same calculation (11) applies, and its decreasing upper bound at d=5 gives v<282/5, so v<=56. Thus the casewise port-sum bounds are:

- a,d<=4: P<=86;
- a=1,d>=5: P<=20;
- a=2,d>=5: P<=41;
- a=3,d>=5: P<=92;
- a=4,d>=5: P<=99;
- a,d>=5: P<=110;

and their duals. Therefore, using H4,

P<=110, S<=184.                                         (16)

To bound the two inner weights without multiplying worst-case coordinate caps, use (5) and the uniform line in (10):

16W < 60P+25m+25S <= (145/2)P+25S.                       (17)

Since L=log3>1 and exp(x)-1>x for x>0, beta_k<(k+1)/L<k+1. The product consequence b<beta_a u, c<beta_d v then gives

B<W+P < (177/32)P+(25/16)S.                              (18)

The shuffle bound gives t<(B+m)/2 <= B/2+P/4. Consequently the total order N=P+S+B+t satisfies

N < (611/64)P+(107/32)S
  <= (611/64)*110+(107/32)*184
   = 1665+13/32.

As N is an integer, this proves the global bound

N<=1665.                                                (19)

One may also retain the convenient coordinate bounds u,v<=108, a,d<=181, b,c<=895, t<=474; they are deliberately loose. The coupled inequalities and casewise caps are much stronger than their Cartesian product.

This is a finite reduction of the entire seven-weight problem, not a proof that all vectors in the resulting finite region are balanced.

## 5. Exact search-ready domain

By full-extension duality it suffices to enumerate a<=d. The following outer and port domains are safe and complete using the accepted H4 theorem:

1. a=1,2,3 and a<=d<=50,92,181 respectively. Set 2<=u<=V(a). If d<=4, set 2<=v<=V(d); if d>=5, apply (11) exactly with integer arithmetic, or its weaker caps 17,32,63.
2. a=4 and 4<=d<=36. Set 2<=u<=43. For d=4, set 2<=v<=43; for d>=5, apply (11) or the weaker v<=56.
3. 5<=a<=d and a+d<=41. Set u,v>=2 and u+v<=110.

In every case impose the exact integer filter

16(au+dv) < 60(u+v)+25min(u,v)+25(a+d).                   (20)

For each (a,u), let M(a,u) be the largest positive b satisfying the first product inequality (1), or zero if there is none. Its existence and an exact binary-search bracket follow from b<(a+1)u. The product ratio is strictly increasing in b, so all possibilities are exactly 1<=b<=M(a,u). Likewise 1<=c<=M(d,v).

Let R(a,u) be the least nonnegative integer s with

3 product_(r=1)^a(s+r) > 2 product_(r=1)^a(s+u+r).

The left/right ratio increases strictly to 1, so R exists and is computable with integer products and doubling/binary search. For each a,d,u,v,b,c the permissible t interval from the original linear and rank-chain inequalities is exactly

low=max(1, 2u-a-b-v+1, 2v-u-c-d+1,
        R(a,u)-b-v, R(d,v)-c-u),
high=floor((b+c+min(u,v)-1)/2),
low<=t<=high.                                           (21)

Empty intervals contribute no candidates. This is an exact test of the indicated prerequisites. No irrational approximation is necessary in the eventual census. Additional forced probabilities can then be counted by the existing audited double-sum formulas. Equation (20), the casewise caps, and (21) should be retained rather than enumerating the coarse rectangle (19).

A small exact reconstruction of just the four-coordinate `(a,d,u,v)` envelope gives 14,190 tuples with a<=d: 4,508 with both outer weights at most four, 8,703 mixed, and 979 with both at least five. Restoring both outer orders gives 25,526 tuples: 6,400, 17,406, and 1,720 in the same three categories. `count_outer_port_domain.py` reconstructs these counts independently of any b,c,t census; normal and optimized runs agree. These are only necessary-envelope counts, not counterexample counts. The full seven-coordinate domain has not been counted here, and no large enumeration has been started.

## 6. Dependencies and reproducibility

The logical inputs are the audited prerequisites restated in Section 1, identified in the dependency manifest of `../outer-three-census/`, and the accepted fourth-terminal-rank theorem H4 where expressly stated. Its proof and independent audit are both identified above. The new content of this note is the exact gamma derivation, rational unbounded estimates, outer-weight reduction without H4, global order bound using H4, and search-ready finite domain.

`verify_global_bound.py` uses only exact integer/Fraction arithmetic. It verifies the logarithm enclosures from finite series plus rigorous remainder bounds, the rational inequalities used for the all-k argument, every stated case constant, and the final rational total-order calculation. Finite verifier checks support the arithmetic; the all-integer assertions are proved above.
