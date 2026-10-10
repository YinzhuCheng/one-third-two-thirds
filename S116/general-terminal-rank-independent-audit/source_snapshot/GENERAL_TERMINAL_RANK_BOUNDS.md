# General terminal-rank bounds and a five-parameter balanced family

Date: 2026-10-10. Status: author proof and exact reproducibility; independent audit is separate. This is a new result and does not change any previously frozen package.

## 1. Statements

Let Q have covers 0<3; 1<2,4; 2<3,6; 3<5; 4<5. Replace its vertices by nonempty chains of lengths (u,a,b,c,t,d,v). All probabilities below refer to uniform complete linear extensions of this actual labelled poset.

**Theorem A (terminal-rank exclusions).** The poset has a balanced incomparable pair whenever any one of the following holds:

- d=1 and v>=4;
- d=2 and v>=10;
- d=3 and v>=30.

All five other weights are unrestricted positive integers. The d=1,v>=5 part is a direct generalization of the earlier singleton-C3 rank proof. The d=1,v=4 part explicitly uses the previously proved triangle certificate.

**Theorem B (exact product obstruction).** In any counterexample,

3 (c)_v < (c+d+1)_v,                                      (1)

where (x)_m=x(x+1)...(x+m-1). Equivalently,

3 product_(i=0)^d(c+i) < product_(i=0)^d(c+v+i).             (2)

This restriction is independent of u,a,b,t. It is a necessary condition, not a sufficient test for a counterexample.

The order-reversing quotient involution sends (u,a,b,c,t,d,v) to (v,d,c,b,t,a,u). Thus Theorem A also excludes a=1,u>=4; a=2,u>=10; a=3,u>=30. The dual of (1) is 3(b)_u<(b+a+1)_u.

**Corollary C (all five free weights).** Every positive chain inflation

(u,1,b,c,t,1,v)

has a balanced incomparable pair, for arbitrary positive integers u,b,c,t,v. This corollary depends on the already independently PASS finite-computation-assisted theorem for all spine weights a,b,c,d in {1,2,3}. A fresh 41-vector exact check is also supplied here. It is not an extrapolation from bounded tests.

**Corollary D (bounded region when a,d<=3).** A counterexample with a,d in {1,2,3} must satisfy u,v<=29, b,c<=90, t<=104, and therefore total order N<=348. More sharply, a=1,2,3 forces (u,b)<=(3,3),(9,19),(29,90), respectively, and d gives the corresponding bounds on (v,c). This is a finite reduction, not an exclusion of that entire class.

No all-seven-weight balance theorem is claimed.

## 2. The correct general conditional law

Use uniform volume on the actual order polytope. Every complete labelled extension has coordinate-simplex volume 1/N!, so this gives exactly the actual uniform extension law.

Condition on every coordinate in C1 and C2, and let r,s be their top coordinates. Almost surely 0<r<s<1. Write x=T3, z=B5, L=1-s, h=(x-s)/L, and y=(z-s)/L.

C6 is an independent ordered uniform v-sample in (s,1) on each such fiber. In particular, if R is its number of vertices before x, then R conditional on h is Binomial(v,h).

After integrating C0 and the first c-1 elements of C3, their factor depending on h, up to a positive constant, is

A_c(h)=sum_(i=0)^u binom(u,i) s^(u-i) L^i i!/(i+c-1)! h^(i+c-1).   (3)

For c=1, this is (s+Lh)^u. For c>=2, integrate the bottom C3 coordinate q after rescaling: the integral is

integral_0^h (s+Lq)^u (h-q)^(c-2)/(c-2)! dq.

Expanding the first factor and using the beta integral gives exactly (3). The omitted common factors include chain-volume factorials and powers of L, all independent of h,y.

Integrating C4 gives (s-r+Ly)^t, and integrating the d-1 C5 coordinates above z gives (1-y)^(d-1), again up to positive constants. Consequently the joint fiber density of (h,y) is proportional to

A_c(h)(s-r+Ly)^t(1-y)^(d-1),          0<h<y<1.             (4)

To marginalize h, substitute y=h+(1-h)q. Then

integral_h^1 (s-r+Ly)^t(1-y)^(d-1)dy
 = (1-h)^d integral_0^1 [s-r+Lq+L(1-q)h]^t(1-q)^(d-1)dq.

The integral on the right is a polynomial B(h) with nonnegative coefficients, because all its displayed coefficient factors are nonnegative. In fact its coefficients are positive on every interior fiber. Formula (3) has the form h^(c-1) times a positive-coefficient polynomial. Therefore

f_H(h) is proportional to h^(c-1)(1-h)^d P(h),             (5)

where P is a nonzero polynomial with nonnegative coefficients and degree at most u+t. Equivalently H is a positive probability mixture of

Beta(c+k,d+1),               0<=k<=u+t.                    (6)

The mixture weight of a monomial p_k h^k in P is proportional to p_k B(c+k,d+1); normalization uses the beta integral, not its reciprocal. No uniformity assumption on the induced r,s law is made or needed.

## 3. Actual-vertex structural prerequisites

Use the established consequence of Zaguia's good-pair theorem: in a poset without any balanced pair, each incomparable ordered pair (p,q) satisfying either

- D(p) subseteq D(q), with U(q) minus U(p) a chain; or
- U(q) subseteq U(p), with D(p) minus D(q) a chain

must have Pr(p<q)>2/3. This follows by the good-pair theorem when that probability is at most 1/2, and by balancedness of the pair itself when it lies in (1/2,2/3].

Put C6=(F1<...<Fv) and x=T3. Then

D(F1)=C1 union C2 subset D(x),
U(x) minus U(F1)=C5,
D(x) minus D(Fv)=C0 union (C3 minus {T3}),
U(Fv)=empty subset U(x).

The third displayed set is a chain: every element of C0 precedes every element of C3. Thus absence of a balanced pair forces

Pr(F1<x)>2/3 and Pr(x<Fv)>2/3.                            (7)

These comparisons are actually incomparable. For v=1 they contradict each other, so a counterexample necessarily has v>=2; order reversal gives u>=2.

When d=1 and z is the unique C5 element, U(Fv)=U(z)=empty and

D(Fv) minus D(z) = C6 minus {Fv},

also a chain. Thus the same hypothesis additionally forces

Pr(Fv<z)>2/3.                                            (8)

For d>1 this last comparison is with T5, not generally with B5. We do not use (8) with B5 when d>1.

## 4. General beta-binomial rank lemma

Let H have Beta(alpha,beta) law, alpha,beta positive integers, and R conditional on H have Binomial(n,H) law. Then

p_j(alpha)=Pr(R=j)=binom(n,j)(alpha)_j(beta)_(n-j)/(alpha+beta)_n.  (9)

For fixed n,j,beta and 1<=j<=n-1,

p_j(alpha+1)/p_j(alpha)
 = (alpha+j)(alpha+beta)/(alpha(alpha+beta+n)).             (10)

Its comparison with one is governed by (j-n)alpha+j beta. This gives a finite exact maximizing location over every integer alpha>=1, with no cutoff assumption.

For beta=2,3,4, respectively, put N_beta=5,10,30. For all n>=N_beta, all alpha>=1, and all 1<=j<=n-1,

p_j(alpha)<1/3.                                          (11)

Proof at j=1: since n>=N_beta>beta+1, (10) is strictly decreasing from alpha=1, so its maximum is

n beta/[(n+beta-1)(n+beta)].                              (12)

This is below 1/3 at the three starting values, and decreases with n there. One elementary proof of decrease uses the sign beta(beta-1)-n^2 of its real derivative.

For j=n-1, the maximizing integers are alpha=beta(n-1) and beta(n-1)+1. The common maximum is

L_beta(n)= n beta^2/(beta+1)
           * product_(r=1)^(beta-1)(beta n-r)
           / product_(r=1)^beta((beta+1)n-r).             (13)

The strict inequality L_beta(n)<1/3 is exactly P_beta(n)>0, where

P_beta(n)=(beta+1) product_(r=1)^beta((beta+1)n-r)
          -3 beta^2 n product_(r=1)^(beta-1)(beta n-r).

Write n=N_beta+z. The three polynomials, with coefficients listed from constant term upward, are

beta=2: 6+15z+3z^2;
beta=3: 96+1202z+249z^2+13z^3;
beta=4: 603960+1425418z+140683z^2+4718z^3+53z^4.

Every coefficient is positive, proving (11) at this rank for all z>=0.

For n>=6 and 2<=j<=n-2, every binomial mixture is bounded by its maximum conditional binomial atom

binom(n,j)(j/n)^j(1-j/n)^(n-j) <= 80/243 <1/3.

For completeness, this binomial peak is symmetric in j and decreases toward the middle: its consecutive ratio is

(1+1/j)^j / (1+1/(n-j-1))^(n-j-1).

The function m -> (1+1/m)^m increases. Hence the largest middle peak occurs at j=2 or n-2. Its value 2(n-1)/n (1-2/n)^(n-2) decreases for real n>2, since its logarithmic derivative is

1/[n(n-1)]+log(1-2/n)+2/n < 1/[n(n-1)]-2/n^2 <0.

The only n=5 case needed is beta=2: at j=2 the all-alpha maximum is 3/14, and at j=3 it is 5/21, by (10). This completes the unbounded proof of (11).

By (6), (11) applies conditionally to R at beta=d+1, hence also unconditionally. Define q_i=Pr(x<F_i)=Pr(R<i). From (7), q_1<1/3 and q_v>2/3. At the first i with q_i>=1/3,

q_i=q_(i-1)+Pr(R=i-1)<2/3.

Thus (x,F_i) is balanced. This proves Theorem A for d=1,v>=5; d=2,v>=10; and d=3,v>=30. This particular witness conclusion assumes both endpoint inequalities; if either fails, the structural theorem supplies a balanced pair, possibly elsewhere.

## 5. The four-tail lift when d=1

When d=1, (4) is a positive mixture of triangle monomials h^k y^ell on 0<h<y<1, now with k>=c-1. The frozen four-tail certificate applies to all integers k,ell>=0, so it applies to this subset without modification.

Precisely, for v=4 set

A=Pr(F3<x), B=Pr(x<F4), C=Pr(F4<z).

Every such monomial, and therefore every mixture, satisfies

12A+15B+C <56/3.                                        (14)

The same triangle representation gives Pr(R=1)<=4/15 and Pr(R=2)<=9/35. If there were no balanced pair, (7) and these two small gaps force Pr(F3<x)>2/3. Also B>2/3 by (7) and C>2/3 by (8). This contradicts (14). Therefore d=1,v=4 is excluded for arbitrary c, completing Theorem A.

This is a direct lifting of the exact polynomial certificate in the dependency FOUR_TAIL_CERTIFICATE.md, Sections 3-5. It does not claim the false generic rank-3 atom bound for v=4. The dependency's independent review is frozen alongside it.

## 6. Product obstruction and the five-parameter corollary

For Beta(alpha,beta), E[H^v]=(alpha)_v/(alpha+beta)_v. At fixed beta,v this strictly increases with alpha, because every factor (alpha+i)/(alpha+beta+i) does. Every component in (6) has alpha>=c. Hence

Pr(Fv<x)=E[H^v] >= (c)_v/(c+d+1)_v.                       (15)

The second forced orientation in (7) says the left side is below 1/3. This proves (1). Cancellation of factorials gives (2).

Now assume a=d=1 and suppose there is no balanced pair. Theorem A and its dual, together with the port restrictions, give

2<=u,v<=3.

In this setting (2) is

3c(c+1)<(c+v)(c+v+1).                                   (16)

The ratio c(c+1)/[(c+v)(c+v+1)] increases with c. For v=2 it already equals 2/5>1/3 at c=3, so c<=2. For v=3 it equals 5/14>1/3 at c=4, so c<=3. Thus c<=v<=3. Applying the dual argument gives b<=u<=3.

Consequently all four spine weights (a,b,c,d)=(1,b,c,1) lie in {1,2,3}. The previously independently audited weighted-seven-core census theorem states that every positive pendant triple (u,t,v) with these spine bounds has a balanced pair. That theorem applies directly, contradicting our supposition and proving Corollary C.

An especially small independent finite recheck is available. The earlier universal inequalities also give

2u<1+b+t+v, 2v<u+c+t+1,
2t<b+c+u, 2t<b+c+v.                                    (17)

With u,v in {2,3}, b<=u,c<=v, these force t<=4. Exactly 41 vectors satisfy them; their maximum order is 18, with counts 7,7,7,20 by (u,v)=(2,2),(2,3),(3,2),(3,3). The companion program reconstructs all 41, directly counts uniform actual extensions, and records a balanced pair and a failed structurally forced arrow at each. This small certificate is a fresh reproducibility check; the declared dependency for Corollary C remains the independently PASS all-spines-at-most-three theorem.

### Further bounded consequence for a,d<=3

For d=1,2,3, Theorem A bounds v by V=3,9,29, respectively. The left side of the product ratio in (2) increases with c and decreases with v. At v=V the largest permissible c is, respectively, M=3,19,90. Exact boundary values are

(d,V,M)=(1,3,3): ratio at M is 2/7; at M+1 it is 5/14;
(d,V,M)=(2,9,19): ratio at M is 19/58; at M+1 it is 308/899;
(d,V,M)=(3,29,90): ratio at M is 83421/250954; at M+1 it is 3049501/9078630.

In each line the first is below 1/3 and the second above 1/3. Monotonicity proves the stated c bounds without extrapolation. Duality gives the corresponding bounds on b from a. Thus if a,d<=3, u,v<=29 and b,c<=90. From the universally necessary shuffle inequalities (17), in their general form 2t<b+c+min(u,v), one gets 2t<209 and hence t<=104. Adding the seven bounds gives N<=29+3+90+90+104+3+29=348. This proves Corollary D. Only the special subcase a=d=1 is excluded completely in Corollary C.

## 7. Sharpness and limits of the generic atom method

The thresholds 5,10,30 are sharp thresholds for the unrestricted positive-integer-alpha atom statement (11). One step below them, the last interior atoms are

beta=2,n=4,alpha=6: 56/165 >1/3;
beta=3,n=9,alpha=24: 1755/5236 >1/3;
beta=4,n=29,alpha=112: 1432049/4294719 >1/3.

These are beta-binomial examples, not poset counterexamples. The four-tail certificate bypasses the first obstruction.

For every fixed beta>=5, no sufficiently-large-n threshold can make all these last-rank atoms below 1/3. Formula (13) gives

lim_(n->infinity) L_beta(n) = (beta/(beta+1))^(beta+1).

This limit increases with beta: its logarithmic derivative is 1/beta-log(1+1/beta)>0. At beta=5 it equals 15625/46656>1/3. Thus the generic maximum exceeds 1/3 for all sufficiently large n for every beta>=5. An exact large finite witness is beta=5,n=1000,alpha=4995, for which

Pr(R=999)=9282007064732500/27702065542505871>1/3.

This blocks extension of the uniform interior-atom method to d>=4. It does not block a different rank witness, a multi-probability certificate, or an all-weight balance theorem.

## 8. Dependencies and reproducibility

The only external structural theorem used is Zaguia's good-pair theorem, Definition 1 and Theorem 2, https://arxiv.org/html/1610.00809 . Its precise conditional-probability use was independently checked in the earlier rank audit.

The four-tail lift explicitly depends on the frozen triangle-monomial certificate and its independent proof review. Corollary C explicitly depends on the independently PASS weighted-seven-core census theorem. Source copies and hashes in dependencies identify these inputs; they are not changed by this note.

verify_general_terminal_rank.py uses only the Python standard library. It checks the beta formulas and all-alpha maximizing candidates, polynomial identities, positive conditional-mixture moments, actual labelled rank distributions, endpoint set conditions, the four-tail lifted inequality, the product obstruction, duality, and the complete 41-vector recheck. Its finite tests validate the implementation. The unbounded parts are the proofs in Sections 2-6 and the explicitly cited audited dependencies.

The verifier uses explicit exceptions rather than assert statements; normal and python -O outputs are compared. MANIFEST.json records sources, scope, and counts. SHA256SUMS freezes the deliverables except itself.
