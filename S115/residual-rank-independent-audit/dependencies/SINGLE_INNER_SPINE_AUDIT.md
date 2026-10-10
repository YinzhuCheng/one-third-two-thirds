# Independent audit: the singleton-upper-spine integral obstruction

Date: 2026-10-10. Verdict: **PASS** for the frozen author theorem and its stated consequences, with a strictly stronger actual-law inequality established below. The residual region is not excluded.

## 1. Scope and source

The quotient has covers 0<3; 1<2,4; 2<3,6; 3<5; 4<5. Every vertex is inflated by a nonempty labelled chain, with weights (u,a,b,c,t,d,v). All probabilities below concern uniform complete linear extensions of that actual inflated poset.

The frozen author source is `author_snapshot/SINGLE_INNER_SPINE_RESULT.md`, SHA256 `8047925c9eec0257ef24ebd74875f4eab559c6aa61af87c9f5e174a522091d8c`. Its companion hardened verifier, frozen output, and README are also snapshotted. The proof has been read in full; the author verifier is replayed independently. No remote files are changed.

Accepted claims:

1. If c=d=1 and v>=t+1, then q+2r<=2, where q=Pr(B3<T6) and r=Pr(T6<T5). In fact q+2r<2 in the positive-integer domain.
2. Both q,r must exceed 2/3 in a hypothetical counterexample, so this entire unbounded family is excluded, for arbitrary positive u,a,b.
3. Every inflation (u,a,b,1,1,1,v) has a balanced pair, including v=1 by a separate structural cycle.
4. For the target (u,1,b,1,t,1,v), any counterexample requires 2<=v<=t; with the independently audited shuffle inequality it requires 2<=v<=t<=b and 2t-b<=v.
5. The genuine order-reversal dual gives the corresponding a=b=1, u>=t+1 exclusion.
6. With the separately independently audited theorem excluding all b=c=1 inflations and the singleton-port prerequisite, any counterexample based on this seven-point core needs at least four nonsingleton blocks.

The last claim is explicitly dependent on those separate structural results. It is not a standalone consequence of the integral inequality, and it is not a theorem for every arbitrary seven-vertex quotient or every width-three poset.

## 2. Independent reconstruction of the conditioned law

Let N be the number of actual elements. The order polytope is the subset of (0,1)^N satisfying the actual poset comparisons. Each complete labelled extension corresponds to one open coordinate-order simplex of volume 1/N!. Thus uniform Lebesgue measure on the polytope induces exactly the desired uniform extension law; equality hyperplanes have measure zero.

Assume c=d=1. Write x=C3, z=C5, and F=T6. Condition on every coordinate of C0,C1,C2, and write A=T0, s=T1, r=T2 for the fixed top coordinates. For almost every feasible fiber,

0<s<r<1, 0<A<1.

The remaining constraints are precisely

max(A,r)<x<z<1;
s<C4_1<...<C4_t<z;
r<C6_1<...<C6_v<1.

There is no C4/C6 relation and no other relation between either chain and x,z. In particular C4 may partly precede r; integrating it over (s,z), rather than (r,z), is essential. Its volume is (z-s)^t/t!. The C6 volume is (1-r)^v/v!, which is constant in x,z. The fiber therefore factors into an independent ordered C6 simplex and an (x,z,C4) factor. Integrating C4 gives (x,z) density proportional to (z-s)^t on its stated triangle. Consequently

Pr(F<f | fixed coordinates)=((f-r)/(1-r))^v, r<=f<=1,

independently of x,z.

Set X=(x-r)/(1-r), Z=(z-r)/(1-r), alpha=max(0,(A-r)/(1-r)), and delta=(r-s)/(1-r). Then 0<=alpha<1 and delta>0. The x,z Jacobian is the constant (1-r)^2; the C4 volume contributes the constant factor (1-r)^t. All these factors disappear in normalization. The scaled density is exactly proportional to (Z+delta)^t on alpha<X<Z<1, and the independently scaled F has CDF g(f)=f^v.

Every feasible interior triangle has positive volume. Fibers with r=1, A=1, s=r, or tied coordinates are outside the almost-sure domain; no claim about a conditional probability on a zero-volume boundary is needed. One may define boundary limits, but averaging uses only the actual induced law on positive-volume fibers. That outer law is not asserted uniform.

It follows exactly, with no deletion-law assumption, that

q_fiber=1-E[X^v], r_fiber=E[Z^v].

## 3. Independent analytic proof, including endpoints and strictness

More generally let 0<=alpha<1, delta>=0, t>=1, and v>=t+1. Put h(z)=(z+delta)^t, g(z)=z^v, G(z)=integral_alpha^z g(x) dx, and

H(z)=(z-alpha)(2g(z)-1)-G(z).

Writing D=integral_alpha^1 (z-alpha)h(z) dz>0, the desired inequality 2E[g(Z)]-E[g(X)]<=1 is equivalent to integral_alpha^1 h(z)H(z) dz<=0.

First, the reference integral is exactly zero:

integral_alpha^1 g'(z)H(z) dz=0.

Indeed, integrating (z-alpha)d(g^2-g) and integrating G dg yields cancellation: the first boundary vanishes since g(1)=1 and z-alpha=0 at the other endpoint; the remaining expression is integral g-G(1)=0. This identity does not require g(alpha)=0.

Second, H has exactly one interior sign change, negative to positive. We have H(alpha)=0,

H'(z)=g(z)-1+2(z-alpha)g'(z),
H''(z)=3g'(z)+2(z-alpha)g''(z)>0 for z>alpha,
H'(alpha)=g(alpha)-1<0,
H(1)=(1-alpha)-G(1)>0.

Strict convexity on the open interval therefore gives a unique z0 in (alpha,1) with H<0 on (alpha,z0) and H>0 on (z0,1).

Third, for z>0,

rho(z)=h(z)/g'(z),
(log rho)'=t/(z+delta)-(v-1)/z<=0.

Let kappa=rho(z0), which is finite because z0>0. The sign-change comparison gives

[h(z)-kappa g'(z)]H(z)<=0

throughout the open interval. Both hH and g'H are polynomials and integrable at zero. Thus this formulation avoids any need to assume rho bounded when alpha=0. Integration and the zero-reference identity give integral hH<=0.

The equality cases within this lemma are exactly delta=0 and v=t+1: then h=g'/v. Otherwise rho is strictly decreasing, and the displayed product is strictly negative on both nonempty open sign intervals. Hence integral hH<0.

In the actual conditioned poset law, delta>0 almost surely because every element of C1 precedes every element of the nonempty C2 chain. Thus every almost-sure fiber has

2E[Z^v]-E[X^v]<1,

and averaging gives the strict actual-law result **q+2r<2**. The author's weaker <= statement is therefore valid. There is no assumption of a uniform positive gap across fibers: a bounded nonnegative random variable that is positive almost surely has positive expectation.

The exponent restriction is substantive. With alpha=0, delta=1/1000, t=v=2, exact integration gives 2E[Z^v]-E[X^v]=10024015/9024018>1. This is a conditional-lemma counterexample outside the stated range, not a poset counterexample.

## 4. Actual structural edges and duality

The previously audited dual good-pair consequence says that, for incomparable y,w, U(w) subset U(y) and D(y) minus D(w) a chain force Pr(y<w)>2/3 in any poset with no balanced pair. The underlying literature result is Zaguia, Definition 1 and Theorem 2, https://arxiv.org/html/1610.00809. Its general implication is a dependency already audited in the project; here the specific actual-vertex hypotheses are checked afresh.

For x and F, U(F) is empty, U(x)={z}, and D(x) minus D(F)=C0. For F and z, both upsets are empty and D(F) minus D(z)=C6 without F. Both differences are chains, including the empty case. Hence q>2/3 and r>2/3 would be necessary, contradicting q+2r<2.

If v=1, F=B6=T6. Besides the x->F dual edge, the lower structural rule gives F->x because D(F) subset D(x) and U(x) minus U(F)={z}. This directly excludes v=1 for every u,a,b,t. In particular t=1 is entirely excluded: v>=2 uses the integral theorem and v=1 uses this cycle.

The quotient involution (0 6)(1 5)(2 3), fixing 4, reverses complete extensions and changes weights to (v,d,c,b,t,a,u). Crucially the two event images are

original B3<T6  <->  dual B0<T2,
original T6<T5  <->  dual B1<B0.

Bottom/top endpoints must reverse within their blocks. Thus the dual probability inequality is Pr(B0<T2)+2Pr(B1<B0)<2 for a=b=1 and u>=t+1. It is valid for arbitrary other positive weights in that dual family. Actual-label DP verifies these exact event correspondences.

## 5. Corollaries and dependency boundaries

For (u,1,b,1,t,1,v), ports require v>=2, while this theorem requires v<=t in any counterexample. The audited shuffle bound supplies 2t<b+1+v; integer conversion gives 2t<=b+v. Therefore

2<=v<=t<=b and 2t-b<=v.

No point of the remaining region is asserted to be a counterexample, and no complete exclusion for arbitrary b,t is claimed.

For the support-size corollary, the separate port theorem supplies nonsingleton C0 and C6. If there were at most three nonsingleton blocks, there could be at most one among C1,C2,C3,C4,C5. If b=c=1, the independently audited five-parameter theorem excludes the vector even with arbitrary a,t,d. Otherwise the sole remaining nonsingleton must be b or c. In the b case a=c=t=d=1, so the all-t=1 integral corollary applies; the c case is its exact dual. These cases are exhaustive. Thus at least four nonsingleton blocks are required.

The dependency sources are the singleton-port catalogue audit, the generalized shuffle independent audit, and the separate b=c=1 exclusion and its rank-chain independent audit. This support-size conclusion is not derived solely from the seven-core catalogue's old singleton graph, which by itself only forced the two ports nonsingleton.

## 6. Independent exact integration versus actual-label DP

The standalone standard-library `audit.py` imports no author implementation, previous project code, or numerical integration package. Its oracle uses predecessor bitmasks for every actual labelled element. Adding an actual-label comparison edge and recounting ideals gives an exact numerator.

A second, independent exact method integrates the full order polytope, not merely the conditional inequality. After integrating the C0 chain up to x and the interior C1,C2,C4,C6 coordinates, its total volume is

1/[(a-1)!(b-1)!u!t!v!] times
integral_(0<s<r<x<z<1) s^(a-1)(r-s)^(b-1)x^u(z-s)^t(1-r)^v ds dr dx dz.

For the F<x numerator replace (1-r)^v with (x-r)^v. For F<z replace it with (z-r)^v. Binomial expansion reduces each to rational monomial integration using

integral_(0<s<r<x<z<1) s^p r^q x^h z^k
=1/[(p+1)(p+q+2)(p+q+h+3)(p+q+h+k+4)].

For every tested vector the volume times N! equals the independently counted number Z of extensions, and both ratios agree exactly with the DP probabilities. This explicitly audits the Jacobian, chain factorials, support, and actual full-law interpretation.

Results in `results.json`:

- 1,024 vectors with u,a,b,t,k in {1,2,3,4}, c=d=1, v=t+k, plus six larger asymmetric vectors up to 44 actual elements. Each has six actual-label DP calls (including dual events) and three exact full-polytope volume integrals: 6,180 DP counts and 3,090 exact integrals altogether.
- All 1,030 vectors satisfy the strict probability inequality, with the actual structural set differences also checked.
- 1,728 exact rational conditional-density tests over t=1,...,8, v=t+1,...,t+6, six alpha values including 0 and 999/1000, and six delta values including 0, 1/1000, and 10000. There are 1,680 strict cases and 48 equality cases exactly as predicted.
- 120 exact zero-reference identities including v=1, alpha=0 and near-one alpha.
- 256 actual v=1 structural-cycle checks.
- All 64 abstract singleton/nonsingleton support patterns with at most three nonsingletons are covered by the stated dependency cases; this tests the corollary's case split, not the independent theorems themselves.
- 10,725 finite arithmetic checks of the combined shuffle corollary.

Normal Python and python -O produce byte-identical `results.json`, and all checks use explicit exceptions. The author verifier also passes replay in both modes and reproduces its frozen JSON byte-for-byte. Its own bounded evidence is supplementary: 1,024 vectors, 3,072 actual-label counts, 2,048 structural-edge checks, 81 v=1 cycles, 384 rational conditional tests, and 32 exact boundary identities.

Finite tests are implementation evidence. The unbounded theorem and the strict strengthening are established by the arguments above.

## 7. Reproduction

From this audit directory:

- `python audit.py`
- `python -O audit.py`
- `python author_replay/verify_single_inner_spine.py`
- `python -O author_replay/verify_single_inner_spine.py`

Each independent run rewrites `results.json`; each author replay rewrites only `author_replay/verification.json`. Compare it byte-for-byte with `author_snapshot/verification.json`. Outputs are deterministic; no elapsed-time keys are present or permitted in these JSON comparisons. Logs and the manifest record the successful frozen replay.
