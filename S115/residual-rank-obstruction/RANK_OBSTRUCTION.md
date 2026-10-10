# A rank-gap obstruction for a long final chain

Date: 2026-10-10. Status: direct proof; independent audit requested.

## Theorem

Take the seven-vertex quotient with covers

0<3; 1<2,4; 2<3,6; 3<5; 4<5,

and replace its vertices by nonempty chains of lengths (u,a,b,1,t,1,v). If v>=5, this poset has a balanced pair. Here balanced means its probability in the uniform law on actual complete linear extensions lies in [1/3,2/3]. No weight-cone assumption, bound on the other four weights, quotient-uniformity assumption, or minimal-counterexample hypothesis is needed.

More specifically, if Pr(B6<x)>2/3 and Pr(x<T6)>2/3, where x is the unique vertex of C3, then x has a balanced pair with an internal vertex of C6. If either endpoint requirement fails, the existing structural good-pair theorem proves balancedness somewhere, without necessarily locating it on C6.

Together with the separate proved obstruction for v>=t+1, this reduces the residual single-inner-spine family (u,1,b,1,t,1,v) to v in {2,3,4}. It does not settle those three unbounded slices.

## 1. A discrete rank lemma

For integers n>=5 and k>=0, let H have the Beta(k+1,2) law, and conditionally on H let R have the Binomial(n,H) law. Then for every interior rank 1<=j<=n-1,

Pr(R=j)<1/3.                                                   (1)

Consequently (1) holds for every probability mixture of these laws over k.

The explicit probability is

p(n,j,k) = (n-j+1) binom(k+j,j) / binom(k+n+2,n).               (2)

For fixed n,j, its ratio at successive k is

p(n,j,k+1)/p(n,j,k)
  = (k+j+1)(k+3) / ((k+1)(k+n+3)).                            (3)

The numerator minus denominator in (3) is

(j-n)k+3j-n.                                                   (4)

For j=1 and n>=3, (4) is nonpositive, so the maximum is at k=0 (also k=1 when n=3). It equals

2n/((n+1)(n+2))<1/3 for n>=5.                                 (5)

For j=n-1, (4)=2n-3-k. Thus the two maximizing integers are k=2n-3 and 2n-2, and the maximum is

4n(2n-1) / (3(3n-2)(3n-1))<1/3 for n>=5.                      (6)

The final inequality is equivalent to n^2-5n+2>0.

For 2<=j<=n-2 and n>=6, bound the mixture by the maximum of its conditional binomial atom:

p(n,j,k) <= B(n,j)
  := binom(n,j)(j/n)^j(1-j/n)^(n-j).

For fixed n, B(n,j) is symmetric and decreases towards the middle. Indeed,

B(n,j+1)/B(n,j)
 = (1+1/j)^j / (1+1/(n-j-1))^(n-j-1),

and m -> (1+1/m)^m is increasing. Hence B(n,j)<=B(n,2) on these ranks. For real n>2,

B(n,2)=2(n-1)/n (1-2/n)^(n-2),

d(log B(n,2))/dn = 1/(n(n-1))+log(1-2/n)+2/n
 < 1/(n(n-1))-2/n^2 <0.

Thus B(n,j)<=B(6,2)=80/243<1/3 for n>=6. The remaining n=5 middle ranks follow directly from (3): at j=2 the maximum is 3/14 (k=1), and at j=3 it is 5/21 (k=2,3). This proves (1).

The threshold is sharp for this generic mixture lemma: n=4,j=3,k=5 gives 56/165>1/3. This is a counterexample to extending the rank-atom lemma to n=4, not a poset counterexample.

## 2. The correct conditional extension law

Use the order-polytope representation: assign all actual vertices coordinates in (0,1) subject to the poset inequalities and take uniform volume. Each complete linear extension occupies a simplex of equal volume 1/N!, so this representation gives exactly the uniform extension law.

Condition on all coordinates in C1 and C2. Let r be the top coordinate of C1 and s the top coordinate of C2; 0<r<s<1. Let x and z denote coordinates of the singleton blocks C3 and C5. Integrating the C0 and C4 coordinates gives the conditional joint density of (x,z), up to a positive constant,

x^u (z-r)^t,       s<x<z<1.                                   (7)

Indeed the respective chain volumes are x^u/u! and (z-r)^t/t!. The C6 coordinates form an independent sorted uniform v-sample from (s,1); their volume is constant with respect to x,z.

Rescale x=s+(1-s)h, z=s+(1-s)y. Integrating y, the marginal density of h is proportional to

[s+(1-s)h]^u integral_(h)^1 [s-r+(1-s)y]^t dy.                 (8)

Expand both powers by the binomial theorem. For each monomial y^ell, its integral is

(1-h)(1+h+...+h^ell)/(ell+1).

Therefore (8) is (1-h)P(h), where P(h) is a polynomial with nonnegative coefficients, of degree at most u+t, and is not zero. Write P(h)=sum_k c_k h^k. Because

integral_0^1 h^k(1-h) dh=1/((k+1)(k+2)),

the law of h is exactly a positive probability mixture of Beta(k+1,2) laws, with weights proportional to c_k/((k+1)(k+2)).

Let R be the number of vertices of C6 below x. Conditional on h, R is Binomial(v,h), since the unordered C6 coordinates are independent uniform samples from (s,1). Section 1 consequently proves

Pr(R=j | all C1,C2 coordinates)<1/3   (1<=j<=v-1),

with a uniform bound depending only on v. Averaging over the actual induced law of those coordinates gives the same strict bound unconditionally. No uniformity of the conditioned-coordinate law is claimed or used.

## 3. Forced endpoints and the rank crossing

Use the established structural consequence of the good-pair theorem: in a poset with no balanced pair,

- D(y) subset D(w) and U(w) minus U(y) a chain force Pr(y<w)>2/3;
- U(w) subset U(y) and D(y) minus D(w) a chain force Pr(y<w)>2/3.

For y=B6,w=x, D(B6)=C1 union C2 is contained in D(x), and U(x) minus U(B6)={z} is a chain. Thus Pr(B6<x)>2/3.

For y=x,w=T6, U(T6) is empty, and D(x) minus D(T6)=C0 is a chain. Thus Pr(x<T6)>2/3.

List C6 in increasing order as F1,...,Fv and put q_i=Pr(x<F_i)=Pr(R<i). The two requirements give q_1<1/3 and q_v>2/3. Choose the least i with q_i>=1/3. Then 2<=i<=v, and Section 2 gives

q_i=q_(i-1)+Pr(R=i-1)<1/3+1/3=2/3.

Thus (x,F_i) is balanced, a contradiction. This proves the theorem.

## 4. Verification and limits

The companion verification script independently enumerates actual labelled ideals to compute rank distributions and forced endpoint conditions, and checks the beta-binomial inequalities exactly. These finite computations check the implementation; the proof above is the unbounded result.

This note does not prove that every x-C6 pair family always contains a balanced pair without the endpoint assumptions. In some weight regimes all those pairs point strongly one way, and the structural theorem supplies a balanced pair elsewhere. Nor does it infer anything about v=2,3,4 merely from the positive-polynomial representation: the generic beta-binomial mixture bound fails in those lengths.
