# Independent audit: general-poset geometric log-concavity and mean comparison

**Verdict:** the general reference-distribution statement, its Prékopa proof, and the ensuing reference mean equivalence are correct for every finite poset K and every nonempty subset L. No chain, rooted-forest, or upper-ideal hypothesis is needed for this analytic statement. The stated application to an external poset Q still requires its full window and cross-incomparability hypotheses and yields a sufficient condition only.

Audited source: `GENERAL_PREKOPA_MEAN_DRAFT.md`.

## 1. Primary literature verified independently

I independently opened the original journal PDF of András Prékopa, *On logarithmic concave measures and functions*, Acta Scientiarum Mathematicarum 34 (1973), 335–343, and checked **Theorem 6 on printed page 342**, including its proof. It states the required preservation of log-concavity when a jointly log-concave nonnegative function is integrated in some variables over a fixed convex domain. The argument below uses this classical result, not a newly proved marginalization theorem. [Original journal PDF](https://acta.bibl.u-szeged.hu/14411/1/math_034_335-343.pdf); [journal repository record](https://acta.bibl.u-szeged.hu/14411/).

Additional targeted searches combining order polytopes, Prékopa, logarithmic transforms, and survival functions did not establish an exact prior formulation of this particular poset corollary. That limited search does not establish novelty or priority. Related rank-log-concavity results should not be conflated with the present continuous geometric-survival statement without a precise equivalence.

## 2. Change of variables: every direction and factor

Use the closed order polytope; replacing weak comparisons by strict ones changes only a null set. Write V=vol O(K)>0. Under the uniform volume law, the density is 1/V on this polytope.

For every coordinate set z_i=log(1−x_i), away from the null boundary x_i=1. Then
- x_a≤x_b becomes 1−x_a≥1−x_b, hence **z_a≥z_b**;
- 0≤x_i<1 becomes −infinity<z_i≤0;
- the absolute Jacobian is **exp(sum z_i)**, not its reciprocal;
- min_{l∈L}x_l>1−exp(s) becomes z_l<s for every l∈L.

For finite s≤0, replacing the final strict thresholds by ≤ changes a finite union of coordinate hyperplanes and hence no probability. The joint set
C={(s,z): s≤0; z_i≤0; z_a≥z_b for a<_K b; z_l≤s for l∈L}
is an intersection of affine halfspaces in the full (s,z) space, so it is convex. No nonlinear order constraint remains after the transformation.

Consequently f(s,z)=exp(sum z_i)*1_C(s,z) is jointly log-concave: its log is affine on a convex support and is extended by minus infinity outside. Zero values on the complement are permitted by the classical theorem.

## 3. Integrability, normalization, and boundaries

Every finite s≤0 slice has positive finite integral. Finiteness follows by domination by exp(sum z_i) on the negative orthant, whose integral is 1. Positivity follows, for example, by putting all coordinates in a small strictly ordered region below s. Equivalently, the event that all x coordinates lie above 1−exp(s) already has positive volume.

The unbounded negative support is not an obstacle to marginalization. One may also intersect the z domain with the increasing cubes [−A,0]^n, apply the theorem there, and pass to the monotone pointwise limit of the log-concavity inequalities. For a fixed finite s the limits are eventually positive.

Even if a version requiring global joint integrability is desired, it holds here for nonempty L after imposing s≤0: for fixed z the allowed s interval has length −max_{l∈L}z_l, at most −z_{l0} for any fixed l0∈L. The exponential negative-orthant integral of this bound is finite. No additional normalizing factor depending on s is introduced.

Let g(s)=integral f(s,z)dz. The variable transformation gives exactly
g(s)=V*T(exp(s)),
and g(0)=V, since the L thresholds at s=0 are redundant. Prékopa gives log-concavity of g, and division by the fixed positive constant V preserves it. Thus log T(exp(s)) is concave on (−infinity,0]. No value at u=0 or z=−infinity is used.

For L empty, the main nonempty-set formulation is inapplicable but the separate convention X=1 gives T(u)=1 on 0<u≤1 and a trivial comparison. Its atom at 1 must not be confused with the continuous nonempty-L case.

## 4. Elasticity and the exact mean equivalence

For arbitrary K and L, partitioning the order polytope into equal-volume extension simplices expresses the first-L coordinate as a finite mixture of Beta(r,n−r+1) laws, with r the first-L rank in that extension. Hence T is a positive smooth polynomial on (0,1). Concavity in s implies
η(u)=uT'(u)/T(u)
is nonincreasing in u.

For any real m>0, compare the survival of X with (1−t)^m. The derivative of the log ratio is
[m−η(1−t)]/(1−t).
Its sign changes at most once, from positive to negative. The ratio starts at 1 when t=0, so the survival difference is either of one sign or first nonnegative and then nonpositive. Flat/equality cases are included. Its integral from 0 to z is therefore monotone or first increasing then decreasing.

If its total integral is nonnegative, every initial integral is nonnegative. Conversely the all-truncation comparison includes the total means at any cutoff z≥1. For z≤0 both variables give the same constant. Thus

for all real z, E[min(X,z)]≥E[min(Beta(1,m),z)]
**if and only if** E[X]≥1/(m+1).

The ratio may have a zero or infinite limit at t=1; this does not affect the proof because the survival difference is bounded and integrable. The conclusion concerns increasing-concave/truncated-mean comparison, not necessarily first-order stochastic dominance.

## 5. Do not retain the old arbitrary-L elasticity bound

The new general theorem does not imply η≤|L| for arbitrary L. In an n-chain, take L to consist only of the minimum point: X~Beta(1,n), so η=n although |L|=1. The manuscript correctly removes that bound.

One can replace L by its upward closure without changing min_L x: every extra descendant is at least one original L coordinate, and all original L points remain included. This explains why upper-ideal formulations had a different cardinality parameter. No cardinality bound is required for the mean-equivalence proof.

## 6. Actual-window application and subsumption of earlier results

The previously audited arbitrary-poset window-coupling lemma applies to the actual induced K and M, regardless of their internal shapes. Under full K–M cross-incomparability and the two full external union/intersection inclusions, their actual windows are ordered around a common reference interval. The uniform reference M minimum is Beta(1,|M|), while the reference K first-L law is the general law just analyzed.

If its mean passes the condition, the all-truncation result applies at the fixed external C cutoff, including cutoffs outside the reference interval after affine scaling and empty C. Integration must use the true external marginal law. The coordinate/first-rank identity then gives the desired first-occurrence sum inequality.

Necessity does not transfer to actual Q: favorable actual windows can make the first-occurrence comparison hold even when the reference mean condition fails. K–M cross-incomparability and full external dominance have not been removed. C2 still requires the entire actual L and M. The known 15-point obstruction e<f0 but e incomparable with a1 continues to rule out every such full-K certificate.

This general analytic theorem **does subsume** the earlier chain, arbitrary barrier, independent-branch, and rooted-forest reference comparison results. Their explicit rank budgets and rational polynomial recursions remain useful ways to certify or compute the reference mean without enumerating extensions; the general result does not automatically make mean computation easy.

The previous cross-branch counterexample is consistent with the general theorem: for K=h1<l1<h2<l2 and L={l1,l2}, the actual reference mean is 2/5, below the required 1/2 for m=1. Arbitrary internal cross-edges are now allowed only with the actual K mean recalculated; the old independent-branch capacity cannot be retained after destroying its decomposition.

The general theorem permits L that is not an upper ideal. Therefore any imported necessary **upper** prefilter relying on upper-ideal status must retain that extra assumption. The necessary lower prefilter, and specifically the 15-point e/a1 obstruction, do not require upper-ideal status.

## 7. Independent finite checks and scope

`independent_general_poset_check.py` exhaustively generates all 357 five-point poset closures with a fixed topological labeling and checks all 31 nonempty subsets L, without requiring them to be upper ideals. From actual extension rank histograms it forms exact rational T polynomials and checks the elasticity derivative at u=1/10,…,9/10. All 11,067 instances and 99,603 exact sign checks pass. These computations are a separate consistency check, not a replacement for the unrestricted Prékopa proof.

No counterexample to the stated theorem was found. The proof is a direct application of a classical theorem; this audit does not claim a new Prékopa theorem, historical priority for the corollary, full C2 closure, or any resolution of the general balanced-pair conjecture.

Only local /tmp artifacts were written. No repository or remote was modified.
