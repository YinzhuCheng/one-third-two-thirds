# Independent audit: rooted-forest elasticity and exact mean criterion

**Verdict:** the elasticity induction and the claimed equivalence for the uniform-window rooted-forest reference law are valid. The resulting criterion for a genuinely externally constrained Q remains sufficient only. This audit does not extend the result to arbitrary posets or establish novelty/residual coverage.

Audited source: `ROOTED_FOREST_EXACT_MEAN_DRAFT.md`, including its appended A5 example.

## 1. Independent counterexample search before checking the draft proof

I independently generated the actual first-L rank distributions for 873 topologically indexed rooted forests with at most six points and all 18,815 nonempty upper ideals L. From these distributions I formed exact rational coefficient polynomials T(u)=Pr(X>1−u). At u=1/10,…,9/10 I checked the sign of
T*T' + u*T*T'' − u*(T')²,
which is T² times the derivative of uT'/T. All 169,335 exact derivative checks are nonpositive.

I also independently inspected all 357 topologically indexed five-point general poset orders and their 4,467 nonempty upper ideals, without finding a counterexample at these test points. This second observation is expressly **not** evidence of a general theorem: neither finite checking nor the rooted-forest argument establishes arbitrary-poset elasticity monotonicity.

Reproducible script: `independent_elasticity_search.py`.

## 2. Basic cases, product signs, and open endpoints

For a nonempty burden set, the reference first-burden coordinate is continuous with full relevant support inside (0,1); T(u)>0 on (0,1], and it is a polynomial. Thus the logarithmic derivative is well defined on (0,1). No division by T(0)=0 is used.

If a whole subtree is burden, its first coordinate has rank 1, so T=u^n and η=n. For an empty burden set, the actual coordinate variable is the constant 1; on the stated domain 0<u≤1 its T is 1 and η=0. If one assigns an endpoint value at u=0, it should be a separate limiting convention: strict survival at t=1 has a jump for this degenerate case. The proof requires no value there.

Independent reference components give T=product T_i. Taking logarithmic derivatives gives η=sum η_i, so both nonnegativity and nonincreasingness are preserved, as is the bound by the total number of burden vertices. Constant-1 components cause no problem. The upper-ideal assumption makes the all-burden and anchor-root alternatives exhaustive.

## 3. Anchor-root formula and the critical η_new≤η_old bound

The independent root decomposition already audited in the capacity proof gives X=R+(1−R)Z with R~Beta(1,n) independent of normalized Z. The draft's formula
T_X(u)=u^n[1+n∫_u^1 T_Z(v)v^(−n−1)dv]
and its derivative identity
η_X=n(1−T_Z/T_X)
are correct. The natural coupling X≥Z gives T_X≥T_Z and hence η_X≥0.

For fixed u, set c=η_Z(u). The induction provides 0≤c≤|L|≤n−1<n. Since η_Z is nonincreasing, integrating it from u to v gives T_Z(v)/T_Z(u)≤(v/u)^c, and integrating to 1 gives T_Z(u)≥u^c. Both inequality directions in the manuscript are correct. Substituting these bounds yields
T_X/T_Z ≤ n/(n−c) − c*u^(n−c)/(n−c) ≤ n/(n−c).
Because η_X is increasing in T_X/T_Z, this implies η_X≤c. The c=0 case is legitimate and gives η_X=0; there is no zero denominator.

Finally,
uη_X' = −n(T_Z/T_X)(η_Z−η_X)≤0.
The minus sign and ratio differentiation are correct. This completes the invariant induction, including the numerical bound η_X≤η_Z≤|L|.

### Separate corroborating derivation

Writing A=1−R and conditioning on A gives
T_X(u)=u^n+∫_u^1 n a^(n−1)T_Z(u/a)da.
Differentiation cancels the boundary contribution because T_Z(1)=1. Hence
uT_X'(u)=∫_u^1 n a^(n−1)T_Z(u/a)η_Z(u/a)da.
Since u/a≥u, monotonicity gives η_Z(u/a)≤η_Z(u). Dividing by T_X proves η_X≤η_Z(u) directly. This independent route confirms the critical comparison rather than merely checking its algebra.

## 4. Why the mean condition is necessary and sufficient here

For real m>0 define R(t)=T(1−t)/(1−t)^m on 0≤t<1. Its logarithmic derivative has sign m−η(1−t). As t increases, η(1−t) is nondecreasing, so that sign can change only from positive to negative. Starting at R(0)=1, the ratio may stay on one side of 1 or cross 1 once from above to below; it cannot cross from below to above. Flat/equality cases are harmless.

The survival difference therefore has at most the corresponding positive-then-negative pattern. Its integral from 0 to z is monotone or increases then decreases. If the total integral at 1 is nonnegative, all intermediate integrals are nonnegative. This is exactly the all-truncation comparison. Necessity follows by taking any cutoff z≥1. Negative cutoffs give identical constants. Possible divergence of the survival ratio as t approaches 1 is immaterial: the survival difference is bounded and integrable. No unspecified endpoint sign or differentiability at the endpoint is required.

Thus for this reference law, and arbitrary real m>0,
all truncated means dominate Beta(1,m) iff E[X]≥1/(m+1).
For empty L, X=1 and the same comparison is trivially true; the main nonempty-L statement and recursive empty convention are consistent.

## 5. Exact polynomial computation

The recursive polynomial claim is correct. Child T_Z has degree at most n−1. Every term of T_Z(v)*v^(−n−1) therefore has exponent at most −2, never −1. Integrating and multiplying by u^n yields only rational polynomial terms, with no logarithmic resonance. In coefficients,
T_Z(u)=sum_{d=0}^{n−1} a_d u^d
implies
T_X(u)=sum_d [n*a_d/(n−d)]u^d + [1−sum_d n*a_d/(n−d)]u^n.
This also verifies T_X(1)=1. Integrating the resulting T over [0,1] gives E[X] exactly. This procedure is structural integration, not extension enumeration; the independent finite checks used enumeration only for verification.

## 6. Conditional application and limits

The previously audited general-window coupling is applicable under the full union/intersection conditions, inherited root-forest structure, and full K–M cross-incomparability. C is external and becomes a fixed scalar cutoff; all-real truncation handles its position relative to the reference interval. Integrating the actual external marginal preserves the uniform extension law through the order-polytope identity.

The **equivalence** belongs to the reference X distribution versus Beta(1,m). For actual constrained Q the aligned windows can be more favorable, so failure of the reference mean condition does not prove failure of the actual first-occurrence inequality. Actual C2 requires full L and full M, not chosen subsets. Cross-branch comparisons, shared descendants, or non-rooted induced orders are outside this proof. The finite general-poset search above does not authorize removing any of these hypotheses.

The earlier capacity criterion implies this mean condition, since its comparison gives E[X]≥1/(κ+1). The new condition may be strictly stronger, as the examples below show. This is a refinement of the same reference-window mechanism, not automatically an independent historically new technique.

## 7. Independent checks of both separating examples

### Six independent two-chains

Each burden tip is Beta(2,1), independently. Their minimum has survival (1−t²)^6. Exact binomial integration gives E[X]=1024/3003>1/3, while the old additive capacity is 3>2. Thus the m=2 separation is genuine. This is not an A5 example.

### Appended A5/Δ9 example

I independently reconstructed the 13-point poset from its full stated roots and Q relations. The transitive closure has complete C2,
A={a0,x1,x2,x3,x4},
L={x1,x2,x3,x4}, M={f0,f1}, C=empty.
The maximum incomparability degree is exactly 9, attained at c2,a0,x4. The full degrees are:
v:2,c1:4,c2:9,b:7,d:8,e:8,a0:9,x1:6,x2:6,x3:8,x4:9,f0:8,f1:8.

Q is the disjoint union of the four-chain d<e<x1<x2, two-chain a0<x3, singleton x4, and two-chain f0<f1. Thus e(Q)=3780. The K survival is the product
(1−4t³+3t⁴)(1−t²)(1−t)
=(1−t)^4(1+3t+5t²+3t³).
Exact integration gives 43/120>1/3. The previous capacity is 2/3+1/2+1=13/6>2. Independent enumeration gives B=12600 and Z=13545, agreeing with the mean calculation.

The example has explicit proper nontrivial autonomous modules, including {d,e}. Therefore it separates sufficient mathematical conditions within A5/Δ9, but is not a no-module or fully screened residual witness. No claim that all prior numerical tools fail is warranted.

Script: `independent_mean_separation_check.py`.
Results: `MEAN_SEPARATION_INDEPENDENT_RESULT.json`.

All audit artifacts were written only under /tmp; no repository or remote was modified.
