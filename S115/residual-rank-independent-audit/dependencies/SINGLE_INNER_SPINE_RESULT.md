# An integral obstruction when the two upper spine blocks are singletons

Date: 2026-10-10. Status: direct proof supplied; independent audit requested.

## 1. Setup and theorem

The quotient has covers

0<3; 1<2,4; 2<3,6; 3<5; 4<5.

Inflate its vertices by nonempty chains of lengths

(u,a,b,1,t,1,v),

where all variable lengths are positive integers. Write x for the unique element of C3, z for the unique element of C5, and F=T6 for the top element of C6. All probabilities refer to the uniform law on complete linear extensions of this actual inflated poset.

**Theorem.** If v≥t+1, then

Pr(x<F) + 2 Pr(F<z) ≤ 2.                                    (1)

Consequently every such inflation with v≥t+1 has a balanced pair somewhere. The balanced pair is not asserted to be one of these two displayed pairs.

This conclusion uses only the structural-good-pair theorem already used in the project, together with the integral argument below. It does not depend on the generalized shuffle bound, any finite enumeration, minimality of a counterexample, or a uniform quotient/deletion law.

## 2. The two forced orientations

We use the established consequence of Zaguia's good-pair theorem: if incomparable y,w satisfy

U(w)⊆U(y) and D(y)\D(w) is a chain,

then a poset without any balanced pair must satisfy Pr(y<w)>2/3. Here D and U are strict downsets and upsets in the actual inflated poset; an empty chain is allowed. This is the dual good-pair rule.

For y=x and w=F:

- U(F)=empty⊆U(x)={z};
- D(x)\D(F)=C0, a chain.

Thus a hypothetical counterexample requires Pr(x<F)>2/3, for every positive u,a,b,t,v.

For y=F and w=z:

- U(z)=U(F)=empty;
- D(F)\D(z)=C6\{F}, a chain.

Thus it also requires Pr(F<z)>2/3. These two strict inequalities contradict (1).

The source is Zaguia, Definition 1 and Theorem 2, https://arxiv.org/html/1610.00809 ; the actual-vertex forced-edge implication is recorded in the project's structural reductions. No unproved claim that acyclicity suffices is used.

## 3. A two-variable integral lemma

Let 0≤α<1, δ≥0, and let t,v be positive integers with v≥t+1. Give (X,Z) the probability density proportional to

w(Z)=(Z+δ)^t

on the triangle α<X<Z<1. Then

2 E[Z^v] − E[X^v] ≤ 1.                                    (2)

### Proof

Put g(y)=y^v and

H(y)=∫_α^y g(x) dx,
K(y)=(y−α)(1−2g(y))+H(y).

The positive normalizing constant for the triangle density is

D=∫_α^1 (y−α)w(y) dy.

Integrating X first shows that (2) is equivalent to

∫_α^1 w(y)K(y) dy ≥ 0.                                    (3)

There are two ingredients.

**Zero integral against g'.** Integration by parts gives

∫_α^1 (y−α)g'(y) dy = 1−α−H(1),

∫_α^1 2(y−α)g(y)g'(y) dy = 1−α−∫_α^1 g(y)^2 dy,

∫_α^1 H(y)g'(y) dy = H(1)−∫_α^1 g(y)^2 dy.

Subtracting the second identity from the first and adding the third yields

∫_α^1 g'(y)K(y) dy = 0.                                  (4)

All identities use g(1)=1 and H(α)=0.

**One change of sign.** For α<y≤1, set

J(y)=K(y)/(y−α)=1−2g(y)+H(y)/(y−α).

Because g is increasing and convex,

0≤g(y)−H(y)/(y−α)≤(y−α)g'(y).

Hence

J'(y)=−2g'(y)+[g(y)−H(y)/(y−α)]/(y−α)≤−g'(y)<0

for y>α, apart from the harmless endpoint y=0. Also

lim_(y↓α) J(y)=1−g(α)>0,
J(1)=−1+H(1)/(1−α)<0.

Thus there is a unique y0∈(α,1) with K nonnegative to its left and nonpositive to its right.

Finally, for y>0 the ratio

ρ(y)=w(y)/g'(y)=(y+δ)^t/(v y^(v−1))

is nonincreasing: its logarithmic derivative is

t/(y+δ)−(v−1)/y≤[t−(v−1)]/y≤0.

Therefore (ρ(y)−ρ(y0))g'(y)K(y)≥0 on both sides of y0. Integrating and using (4) gives

∫_α^1 w(y)K(y)dy
 = ∫_α^1 (ρ(y)−ρ(y0))g'(y)K(y)dy ≥0.

At α=0, these statements apply for y>0 and the integrands wK and g'K remain integrable at zero. The displayed equality is therefore valid by taking a limit from positive lower endpoints in the final integrals, or directly by improper integration. This proves (3) and (2). QED.

## 4. Why the lemma has the correct extension law

Use the order-polytope realization: assign each actual element a coordinate in (0,1), subject to the poset inequalities, and choose uniformly from the resulting region. Each complete linear extension corresponds to a simplex of volume 1/N!, where N is the number of actual elements. Consequently the induced extension is exactly uniform. Equal-coordinate events have measure zero.

Condition on all coordinates of C0,C1,C2. Let

A = the coordinate of T0,
r = the coordinate of T1,
s = the coordinate of T2.

We have r<s. The remaining constraints are exactly:

- x>max(A,s), with x<z<1;
- the t coordinates of C4 form a chain between r and z;
- the v coordinates of C6 form a chain between s and 1.

The C4-coordinate volume is (z−r)^t/t!. The C6-coordinate volume is (1−s)^v/v!, independent of x,z. After integrating C4, the conditional density of (x,z) is therefore proportional to (z−r)^t on max(A,s)<x<z<1. Conditional on the fixed coordinates, the C6 coordinates are independent of (x,z); their top coordinate F has conditional CDF

Pr(F<f | fixed C0,C1,C2 coordinates)=((f−s)/(1−s))^v

for s≤f≤1.

Rescale every remaining relevant coordinate by y=(coordinate−s)/(1−s), and put

α=(max(A,s)−s)/(1−s),
δ=(s−r)/(1−s).

Then 0≤α<1 and δ>0, and the rescaled (X,Z) has exactly the density in the lemma. The independently rescaled F has CDF g(f)=f^v. Thus

Pr(x<F | fixed coordinates)=1−E[X^v | fixed coordinates],
Pr(F<z | fixed coordinates)=E[Z^v | fixed coordinates].

The lemma gives (1) for every conditioned fiber. Averaging over the actual induced law of the fixed coordinates proves (1) unconditionally. No uniformity is assumed for that induced law. QED.

## 5. Consequences for the requested single-inner-spine family

For weights (u,1,b,1,t,1,v), a hypothetical counterexample must have

2≤v≤t.                                                    (5)

The upper bound is the theorem. The lower bound can be checked without invoking a separate filter: when v=1, F is also B6, and the lower good-pair rule forces F<x because D(F)⊆D(x) and U(x)\U(F)={z} is a chain, whereas Section 2 forces x<F. These are incompatible strict-majority requirements.

In particular, **every inflation (u,a,b,1,1,1,v), with arbitrary positive u,a,b,v, has a balanced pair somewhere.** This is a genuine unbounded subfamily result, including every b in the requested family with t=1.

The quotient duality sends (u,a,b,c,t,d,v) to (v,d,c,b,t,a,u). Hence the dual conclusion excludes every vector with a=b=1 and u≥t+1, and gives the corresponding all-t=1 statement for the dual family. This is only the image of the proved theorem under reversal of complete extensions.

If the separately proposed generalized shuffle bound passes independent audit, its necessary inequality 2t<b+1+min(u,v) would combine with (5) to give

t≤b,   2t−b≤v≤t,

for the requested (u,1,b,1,t,1,v) family. This last combination is explicitly conditional here; the theorem and (5) are not.

### A further structural corollary, conditional on a separate theorem

Suppose the separately developed five-parameter theorem excluding every vector with b=c=1 (arbitrary positive u,a,t,d,v) is proved and audited, and the present theorem passes independent audit. Then a counterexample inflation of this seven-point core must have at least four nonsingleton blocks.

Indeed, the established singleton-port filter requires u,v≥2. With at most three nonsingleton blocks, there is at most one additional nonsingleton among a,b,c,t,d. If b=c=1, the separate five-parameter theorem excludes it. Otherwise that sole additional nonsingleton is b or c; in the b case a=c=t=d=1, and the all-t=1 consequence proved here excludes it. The c case is its dual. This corollary is not asserted independently of the separate five-parameter theorem and both audits.

## 6. Verification and limits

The companion standard-library script verifies exact labelled-ideal counts, the two structural edges, the probability inequality in a specified finite box, and exact rational instances of the integral lemma. Its arithmetic checks validate implementation and catch counterexamples to a claimed identity; they are not the proof of the unbounded statement.

The recorded run passed 1,024 vectors with u,a,b,t in {1,2,3,4} and v in {t+1,t+2,t+3,t+4}, using 3,072 independently implemented labelled-ideal counts and 2,048 actual-vertex forced-edge checks. It also passed 81 v=1 structural-cycle checks, 384 exact rational integral checks, and 32 exact boundary identities. An out-of-scope integral example (α,δ,t,v)=(0,0,2,2) has negative margin −1/36, confirming that the lemma is not being asserted for v≤t.

No all-b/all-t exclusion is claimed. The residual region 2≤v≤t remains open to this argument. No claim about the full width-three conjecture or all seven positive weights is made. Independent mathematical audit remains required before treating this as a frozen project theorem.
