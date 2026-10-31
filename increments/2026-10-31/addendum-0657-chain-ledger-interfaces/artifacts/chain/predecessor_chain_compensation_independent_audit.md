# Full independent audit: predecessor-chain compensation

**Verdict: the general finite-poset sufficient theorem and its proof are valid as written.** No mathematical counterexample was found. This verdict does not establish novelty, filtered-residual applicability, or complete C2 coverage.

Audited source: `predecessor_chain_compensation.md`.

## 1. Finite-grid coupling and its limiting argument

For nondecreasing integer endpoint vectors a,b and a nonempty state space, a_i≤b_i for each i, so the vector a itself is a feasible initial state. In the proposed coordinate Gibbs update, both interval endpoints are monotone functions of the endpoint data and neighboring coordinates. Uniform distributions on two integer intervals whose left and right endpoints are ordered admit the common-quantile monotone coupling. Thus the paired update preserves coordinatewise order.

The irreducibility claim is correct: starting from any feasible x, change coordinates in order 1,…,h to their respective a_i. At step i, the preceding coordinate equals a_{i−1}≤a_i, and the next unchanged coordinate is at least the old x_i≥a_i. Bounds also remain satisfied. Every such update has positive probability. Each reversed step is feasible and has positive probability too, so every state communicates through a. A random-scan update has a positive self-loop at every state. The conditional update is the conditional law of the uniform counting measure, so that measure is stationary; finiteness, irreducibility, and aperiodicity give convergence to it. Starting the two systems at a≤a' and taking a joint subsequential limit therefore proves the finite coupling assertion.

The continuous limit also works. Use one common lattice mesh, round all lower endpoints upward and upper endpoints downward. These rounding maps preserve endpoint inequalities and nondecreasing sequences. Positive volume ensures nonempty lattice state spaces for all sufficiently fine meshes. The regions are bounded polytopes with boundary of Lebesgue measure zero, so their normalized lattice measures converge by Riemann sums to normalized volume. Compactness gives a joint weakly convergent subsequence; the coordinatewise-order relation is closed. Strict-order and equality boundaries are null sets. Zero-volume boxes are correctly excluded rather than assigned a fictitious uniform density.

## 2. Beta comparison

Verified independently in `beta_truncated_mean_independent_audit.md`: for q≥0,l,m>0 the displayed all-truncation comparison is equivalent to l≤m(q+1). The density-ratio proof is sound. Here the main theorem explicitly assumes q is a nonnegative integer and l,m positive integers, so no negative-parameter or zero-chain exception is hidden.

## 3. Conditional boxes and reference-window alignment

Use full transitive predecessor/successor sets. Along any chain, predecessor sets increase and successor sets decrease. Consequently both the lower-window endpoints and the upper-window endpoints are nondecreasing.

For almost every external coordinate vector with positive conditional volume, write the M windows as [α_i,β_i] and K windows as [γ_j,δ_j]. With [a,b]=[α_m,β_m], chain order gives α_i≤a and β_i≤b for all i. Positive conditional volume implies a<b.

The two endpoint inclusions have exactly the required directions:
- D_R(m_m)⊆D_R(k_1) gives a≤γ_1≤γ_j;
- U_R(k_1)⊆U_R(m_m) gives δ_1≥β_m=b, hence δ_j≥b.
Empty predecessor/successor sets are handled by the specified endpoints 0 and 1, and obey the same inequalities. The apparent reversed direction for upper sets is correct because the minimum over a smaller set is larger.

Full K–M incomparability ensures that, after fixing R coordinates, there are no remaining constraints joining the two chains. Their feasible regions are a Cartesian product and their conditional volume law factorizes. Even marginal stochastic domination alone would suffice for the subsequent expectation comparison. The proof does not assert that either actual chain is distributed as ordinary order statistics; only the two artificial uniform-window reference chains have the stated beta ranks.

## 4. Weighting, C, and the order-polytope identity

Every extension simplex has volume 1/|Q|!, so the extension induced by the uniform order-polytope law is uniform. Conditional on any one extension, sorted coordinates are ordinary uniform order statistics; a first occurrence at rank j has mean j/(|Q|+1). This proves the displayed first-occurrence/coordinate identity. When the set is empty, the constant minimum 1 and sentinel |Q|+1 agree exactly.

C⊆R makes z=min r_C a fixed scalar under the conditioning. It may be below, within, or above [a,b]; the beta lemma holds for every real cutoff, so the affine transformation remains legitimate in all three cases. Empty C gives z=1. Expectations are bounded, so integrating the pointwise conditional inequality against the actual external marginal density is valid without any reweighting or limiting interchange concern. Conditional boxes of zero volume contribute no probability mass. The proof never makes external words or coordinate fibers equiprobable.

## 5. C2 interface and redundancy boundary

To obtain B≤Z in the C2 application, M must be the full actual set F\\U(b), and the last l points of K must be the full actual L=A∩U(b). The q anchors must be genuinely additional vertices outside L∪M∪C. Choosing only a subchain of actual L would bound the wrong, larger first-occurrence sum and does not by itself prove B≤Z. Check K∥M and the endpoint inclusions in Q=P−{v,c1,b,c2}, using the resulting full strict relations, not only displayed generating edges or P-level root predecessor sets.

For **l≤m**, the conclusion is already implied by the existing block-swap mechanism under these endpoint assumptions: match all l points of L in order to the first l points of M; treat the q K-anchors and the remaining M tail as external. The strong endpoint inclusions imply the required coordinatewise external inclusions for this smaller equal-size block. Include the unused M tail in the fixed avoided set together with C. The block theorem bounds B by the first(L∪C∪unused-M) sum, which is at most Z. Thus this parameter range should not be presented as a new mechanism.

The potentially new structural sufficient range is l>m with q≥1 and l≤m(q+1). The theorem is a valid candidate extension there, but this audit does not identify a no-VG/no-mixed-cycle/no-module witness outside all older tools, nor establish historical novelty. The condition is sufficient, not necessary for arbitrary posets. Failure of a reference-chain inequality cannot by itself refute a more favorable actual conditioned geometry.

Cross-incomparability really matters: with R empty and one chain k1<k2<k3<m1, q=1,l=2,m=1 satisfies the numerical budget and vacuous external inclusions, but the unique extension has first(M)=4>2=first(L). This violates the conclusion when the excluded K–M relation is allowed.

## 6. Independent finite counterexample search

`audit_chain_compensation_small.py` independently enumerates all labeled six-point orders with fixed K={k1<k2<k3}, singleton M, and two external vertices (deduplicating their transitive closures). Of 1,090 distinct generated closures, 151 satisfy full cross-incomparability and the endpoint conditions. For each, all four external subsets C were checked, for **604 valid theorem instances**. The first-occurrence sums were computed independently as extension counts after adjoining a new minimal insertion label, not by beta approximation. All comparisons hold. This finite check supports but does not establish the general theorem; the proof above is the unrestricted argument.

No repository files or remote state were modified by this audit.

## 7. Equality boundaries

No general strict inequality is claimed, appropriately. At the rank-budget boundary q=1,l=2,m=1 with R=C empty and Q the disjoint union of a three-chain and a singleton, both first-occurrence sums equal 10. Even a strict numerical budget does not ensure strictness with arbitrary C: an external c below all K∪M, with C={c}, makes both first-occurrence variables identically first(c). Hence any later strictness claim requires an additional nontrivial-truncation/positive-measure argument.
