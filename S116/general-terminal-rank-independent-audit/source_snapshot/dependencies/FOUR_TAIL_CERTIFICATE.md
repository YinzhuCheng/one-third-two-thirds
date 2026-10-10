# An exact three-probability certificate for a four-element terminal chain

Date: 2026-10-10. Status: direct proof supplied; independent audit requested.

## 1. Theorem and scope

Let the quotient have covers

0<3; 1<2,4; 2<3,6; 3<5; 4<5.

Inflate its vertices by nonempty chains with weights (u,a,b,1,t,1,4). Every such inflation has a balanced incomparable pair under the uniform law on complete linear extensions of the actual inflated poset.

This is an unbounded theorem in all four positive integers u,a,b,t. It uses the structural good-pair theorem, but no finite cone, minimal-counterexample assumption, or quotient-uniformity assertion. It is a separate next result: it does not modify any earlier frozen proof or publication scope.

Together with the separate rank obstruction for v>=5 and the integral obstruction for v>=t+1, it reduces the single-inner-spine family (u,1,b,1,t,1,v) to v in {2,3}, subject to the already known residual inequalities. It does not settle either of those remaining unbounded slices or the general seven-weight family.

## 2. Correct conditional law and triangle monomials

Write x for C3, z for C5, and F1<F2<F3<F4 for C6. Use uniform volume on the actual order polytope. Each actual complete linear extension has volume 1/N!, so this is exactly the requested uniform extension law.

Condition on all coordinates of C1 and C2. If r and s are their respective top coordinates, then 0<r<s<1. Integrating the C0 and C4 coordinates gives joint density proportional to

x^u (z-r)^t,     s<x<z<1.

The C6 coordinates are an independent sorted sample of four uniform points in (s,1). Its constant volume factor does not alter the displayed density.

Put h=(x-s)/(1-s), y=(z-s)/(1-s). On 0<h<y<1 the density is a positive linear combination of monomials h^k y^ell, with nonnegative integer k,ell, because both factors

[s+(1-s)h]^u and [s-r+(1-s)y]^t

have nonnegative coefficients. Consequently the conditional law is a probability mixture of the normalized triangle laws with density proportional to h^k y^ell. There is no assumption about the induced distribution of r,s; all bounds below are uniform in their values and are averaged under their actual law.

For one triangle monomial, put n=k+ell. Its normalizing integral is 1/((k+1)(n+2)). Its moments are

M_j = E[h^j] = (k+1)/(k+j+1) * (n+2)/(n+j+2),
E[y^j] = (n+2)/(n+j+2).                                  (1)

Let R be the number of C6 vertices below x. Conditional on h, R has the Binomial(4,h) law. Thus

A := Pr(F3<x) = Pr(R>=3) = 4M_3-3M_4,
B := Pr(x<F4) = Pr(R<=3) = 1-M_4,
C := Pr(F4<z) = E[y^4] = (n+2)/(n+6).                    (2)

The C6 sample is independent of (h,y), which is essential for these identities.

## 3. The certificate

For every normalized triangle monomial with integer k,ell>=0,

12 A + 15 B + C < 56/3.                                  (3)

Since (3) is linear in probabilities, it holds for every mixture in Section 2, then unconditionally for every inflated poset in Section 1.

Proof: by (1)-(2), the difference between the right and left sides of (3) is

11/3 - 48M_3 + 51M_4 - C.

Multiplying by the positive denominator 3(k+4)(k+5)(n+5)(n+6) gives exactly

P(k,n) = 17k^2 n^2 + 19k^2 n + 102k^2
         -27k n^2 -657k n -18k
         +52n^2 +524n +3480.                             (4)

Substitute n=k+ell. For k=0,1,2,3,4 respectively, this polynomial is

k=0: 4(13ell^2+131ell+870),
k=1: 6(7ell^2-5ell+582),
k=2: 6(11ell^2-75ell+448),
k=3: 4(31ell^2-133ell+408),
k=4: 72(3ell^2-ell+18).

The k=0 expression has positive coefficients. The four remaining quadratics have positive leading coefficients and discriminants -16271, -14087, -32903, -215, respectively. All five expressions are strictly positive for ell>=0.

For k>=5, put d=k-5. The polynomial becomes

17d^4 + 34d^3 ell +332d^3
 +17d^2 ell^2 +475d^2 ell +1927d^2
 +143d ell^2 +1647d ell +3376d
 +342ell^2 +1134ell +3060,

which is strictly positive for d,ell>=0. This proves (3) for every integer k>=0. The polynomial calculations are exact identities, not a finite extrapolation. QED.

## 4. Two small rank gaps

Marginalizing h^k y^ell over y gives

h^k(1-h^(ell+1))/(ell+1)
 = (1-h)/(ell+1) * sum_(j=0)^ell h^(k+j).

Hence h is a probability mixture of Beta(m+1,2) laws with integer m>=0. Under such a law, the Binomial(4,h) mixture has atom

p_j(m) = (5-j) binom(m+j,j) / binom(m+6,4).

For consecutive m,

p_j(m+1)/p_j(m)
 = (m+j+1)(m+3)/((m+1)(m+7)),

and the numerator minus denominator is (j-4)m+3j-4. Thus at j=1 the sequence decreases and its maximum is p_1(0)=4/15. At j=2 it increases from m=0 to m=1, ties at m=1,2, and thereafter decreases; its maximum is p_2(1)=p_2(2)=9/35. Both are strictly below 1/3. Averaging twice yields

Pr(R=1)<=4/15<1/3,
Pr(R=2)<=9/35<1/3.                                      (5)

The rank-3 atom need not be below 1/3. The certificate in Section 3 addresses that actual obstacle instead of extending a false rank bound.

## 5. Contradiction under absence of balanced pairs

The established good-pair theorem supplies these strict orientations in any poset with no balanced pair:

Pr(F1<x)>2/3,
Pr(x<F4)>2/3,
Pr(F4<z)>2/3.                                            (6)

For completeness, the first follows from D(F1) subset D(x) and U(x) minus U(F1)={z}, a chain. The second follows from U(F4) subset U(x) and D(x) minus D(F4)=C0, a chain. The third follows from equal empty upsets and D(F4) minus D(z)={F1,F2,F3}, a chain. These are statements about actual inflated vertices.

Let a_i=Pr(F_i<x). These probabilities decrease with i, and a_i-a_(i+1)=Pr(R=i). Since a_1>2/3 and no a_i lies in [1/3,2/3], the first bound in (5) forces a_2>2/3: a direct jump below 1/3 would have size greater than 1/3. The second bound then forces a_3>2/3.

Thus A=a_3, B=Pr(x<F4), and C=Pr(F4<z) are all strictly larger than 2/3. They imply

12A+15B+C > (12+15+1)*2/3 =56/3,

contradicting (3). The theorem follows. A failed orientation in (6) can locate balancedness elsewhere via the structural theorem; no fixed pair is claimed balanced for all weights.

## 6. Dependencies and verification

The sole external structural dependency is the already used good-pair theorem (Zaguia, Definition 1 and Theorem 2, https://arxiv.org/html/1610.00809). The conditional law, moment formulas, rank bounds, and polynomial certificate are proved in this note.

The accompanying standard-library verifier builds the actual labelled poset independently, counts complete extensions and the relevant rank events, checks the three actual-vertex structural conditions, and verifies the certificate and small atom bounds on a stated finite box. It also checks exact rational monomial moments, the polynomial identity, the five small-k reductions, and the nonnegative shifted polynomial. Its finite calculations validate implementation; the unbounded theorem rests on Sections 2-5.

The previous inequality Pr(x<F4)+2Pr(F4<z)<=2 is not asserted here. Its failed extension to v<=t is unrelated to the valid three-probability certificate (3).
