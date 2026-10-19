# Active-threshold and slot consequences: independent review

Date: 2026-10-19. Final verdict: both new manuscripts PASS analytic independent review. No substantive gap remains; both source manuscripts have been locked after their authors incorporated the presentation clarifications noted below.

Scope: independently audit the new results in `../active-threshold-certificates-20261019/RESULT.md` and `../slot-theorem-consequences-20261019/RESULT.md`. The previously reviewed AU, all-coordinates-large effective threshold E, and general ideal-run/slot T are accepted dependencies, not re-reviewed here.

Risk notices already sent to both authors:

- Active thresholds: the old min-coordinate threshold cannot replace a max-active-coordinate threshold. A truncation plan must explicitly give a finite, non-circular construction and handle fixed-marker profiles uniformly.
- Slot propagation: t=2 endpoint preservation does not prove preservation of every entirely external pair. Parameters and 0-based slot conventions must match the earlier formulas; empty upper ideals require their own deterministic convention.

The review will distinguish an existence theorem, a finite certificate algorithm, and an algorithm that was actually run. It will not repeat older reviews or conduct enlarged finite searches.

## Independent preliminary algebra (not a verdict on the pending manuscripts)

For antichain I={y,z}, use the older 0-based slots p=E L_y, r=E L_z, q=E C_y, s=E C_z, and M=E[L_yL_z+min(L_y,L_z)], N=E[C_yC_z+min(C_y,C_z)]. Then t=m+1, B=p+r+q+s, A=M+N+ps+rq, and

T(t)=t²+(B+1)t+A,
1−Pr(c_1<y)=[(p+1)t+U]/T(t), U=M+ps+r+s+1.

The continuous derivative numerator is

G=(p+1)t²+2Ut+U(B+1)−(p+1)A.

Ordinary order-polytope FKG in the reversed D object gives M≥pr−1+(p+1)(r+1)/(|D|+1)≥pr−1. This lower bound is additional to the upper slot T. With N≤qs+s²+2s,

G≥(p+1)[(t+r)²+2rs+r+s(2t−1)+1]>0 for t≥1.

In particular the old m=1→2 difference numerator obeys

J_first=U(B+6)+(p+1)(6−A)
≥(p+1)(r²+2rs+6r+4s+7)>0.

A consequence stated for adjacent actual chain ranks requires m≥2; the expression max{1/(m+1),2m/((m+1)(m+2))} is ≤1/3 in that domain. At m=1 there is no adjacent rank pair, and same-side status must be treated separately.

## Active-threshold manuscript: final analytic verdict PASS

Reviewed the complete `active-threshold-certificates-20261019/RESULT.md` (the version submitted with §10 still awaiting review). No substantive gap found in Theorems M or A.

### A1. Effective mixed concentration

The support projection formula applies to both collapsed nonsupport intervals and genuine single markers. The optimization is performed solely on the support interval domain, so the prior full-endpoint uniqueness theorem applies without an invented marker exponent. The first-order optimality graph, positive length bound, endpoint rigidity, and neighboring-anchor quadratic gap all have the same finite real-closed-field encoding as the accepted E module.

The denominator cube has dimension 2|U|+|F|. With the manuscript's b,τ,ζ,λ, all comparison slacks remain positive after both cube displacement and anchor perturbation; nonsupport interval lengths remain at least a, and support lengths remain at least (1−σ)ℓ*. The fixed markers contribute their actual integration coordinates. The resulting loss budgets are gt/8 for support perturbation and gt/8 for lower exponents, against the numerator's gt gap. Thus Δ=ga/8 and c=g/2 are safe, and the stated finite T follows from exp(−x)≤1/x. No prior noneffective subsequence assertion is used to certify termination.

### A2. Finite bridges: the genuinely new effective branch

The bridge-marker domain K₀ has a uniform positive-volume cube because the compact top-chain weight family has uniform strict feasibility. Its perturbation symmetric difference lies in 2r coordinate boundary slabs; the bound 4rρ and the looser TV bound 8rρ/V₀ are valid. Conditioning on the top intervals and all pinned objects retains the true uniform marker law; mixing over the exceptional event gives the stated unconditional TV bound 2ξ, without independence.

The full coordinate projection has width at least α/s. The elementary two-cone volume argument yields a marginal density bound r/W≤rs/α=C. Therefore every median has half-mass on each side and lies at least 1/(2C) from the window endpoints. A median lying on an internal cut still permits an adjacent top interval within the marker's incomparable index range.

The selected integer rank is genuine even at θ=0 or 1. On the endpoint-good event, its conditional mean is within r_S+1/(n−1)≤η/2 of the reference median. Its conditional variance is at most 1/(4n). The threshold T_F makes the conditional Chebyshev error at most ξ; adding endpoint failure gives 2ξ. The final comparison bound is 6ξ+2Cη=5ε₀/16<ε₀. No large-sample Beta estimate is applied to a finite marker, and no unconditional cross-block independence is assumed.

### A3. Four branches and threshold dependencies

The four cases cover every nonempty top support: nonchain support; chain with an interval bridge; chain with only finite marker bridges; chain with no bridges. The bridge plan is completely computed before the required top-level precision. Pinned large exponents become conditional constants and are excluded from bridge lower-exponent budgets. Both empty-band loops have a prescribed finite number of levels and treat boundary ratios correctly. In the zero-bridge case, the active witness lies within a strictly smaller mixed ordinal-sum component, so the M recursion is well founded and its hypotheses survive.

The final min_U threshold dominates every recorded top, bridge, scanning, finite-marker, and smaller-object threshold. Hence every actual exponent vector with min_U n_u≥L is certified, including arbitrary relative scales.

### A4. Exact removal and finite truncation tree

Deleting nonactive original vertices is exact: these vertices form an entirely comparable ordinal-sum skeleton, and deleting their chain blocks leaves unchanged the uniform laws within all possible incomparable components. Every surviving original vertex is active. Replacing another old chain block by all its d real markers preserves each remaining interval's original incomparable witness.

At every truncation node, the mixed threshold L_ν is computed first from its already fixed finite profile. Its children then fix one of finitely many old blocks to one of finitely many d<L_ν values. Depth is at most the number of original active blocks. The internal M recursion decreases mixed object size; the external tree decreases the number of unfixed old blocks. These are separate terminating procedures, even though expanding a short block can increase mixed object size.

Every bad vector must choose a short-coordinate edge at each nonleaf node and therefore reaches a completely fixed leaf. Every coordinate fixed along that path is bounded by the finite root maximum B. The contrapositive establishes max_active n≥B+1⇒δ≥1/2−ε₀, and ε₀≤ε gives the requested theorem. The finite candidate box and optional exact minimal threshold follow from this certified infinite-tail exclusion rather than an unproved finite-box extrapolation.

Status boundary: this is an independently checked natural-language finite algorithm, not executed quantifier elimination, a numeric threshold, a complexity bound, or a novelty determination. No old experiment was repeated.

## Slot-consequences manuscript: final analytic verdict PASS

The complete submitted manuscript was checked, including all new consequences rather than only its endpoint statement. No substantive gap was found. Two small presentation clarifications were requested and incorporated in the locked final version: explicitly resetting the seven-class counts when the upper I point becomes the designated target, and giving the factorized 19/27 lower-bound certificate in the analytic cross family.

### S1. Exact conventions and transferable inputs

Every slot is 0-based: the number of elements before the first member of its upper ideal. An empty upper ideal gives the deterministic full-size run, so the new ideal-run theorem extends without inventing an empty principal filter. The finite-size quantity U_h(a,b), its one-sided gap Γ, and the factorial-moment bound V_h are the direct C3/C3a consequences with all h+1 and h+a+2 shifts retained.

The lower mixed-moment bound K−ab≥−1+(a+1)(b+1)/(h+1) follows from ordinary order-polytope FKG and the stated order-statistic identity. It is genuinely needed and is retained in the antichain-I proof. This is not an inference from the upper slot T alone.

### S2. Strict indexed interlacing

For antichain I, independently counting insertions with y before the i-th chain element gives exactly

(p+i)t+M+ps+i(r+s+1), t=m+1.

The derivative identity G_i=G_1+(i−1)R is correct. The lower left bound M≥pr−1 closes G_1; the two directed upper T bounds close R. Their displayed positive lower polynomials agree with independent expansion. The legal range is t≥i+1.

For I={y<z}, the ordered left/right moments must be redefined. Counting central slots gives the different numerator

(p+i)t+M_o+ps+is−i(i−1)/2,

against the half-quadratic total kernel. Although U_i can be negative, on t≥i+1 the derivative of its derivative numerator is strictly positive. The displayed value at t=i+1 after N_o≤s(s+1) has the correct coefficients and a strictly positive constant for i≥1. The upper target has a positive, t-independent complement count once its designated-target classes are used. Full order duality maps the right indexed inequality with j=m−i+1, producing exactly Q_i(m+1)>Q_i(m)>Q_{i+1}(m+1).

This strengthens endpoints only within chain–I columns; it does not cover entirely external pairs.

### S3. No-balanced-column shortening

The internal jump count H+L(m−i+1)+R₂(i+1) and the positive actual total give the claimed convex-combination maximum bound. The numerical ≤1/3 is correctly restricted to m≥2; m=1 has no adjacent rank. A strictly band-avoiding decreasing column cannot cross from >2/3 to <1/3 without a jump >1/3, so the same-side assertion is proved rather than assumed. Strict endpoint monotonicity then makes every shorter column retain its side with a strictly smaller maximal rare-direction probability. Closed band endpoints are handled correctly.

### S4. Exact cross criterion and finite-size left-defect budgets

The discrete first-difference numerator is

D(t)=β[t(t+1)−A]+F(2t+B+2),

and D(t+1)−D(t)=2β(t+1)+2F>0. Hence the all-integer criterion is exactly D(2)≥0, with the stated equality and strictness cases. It is not silently promoted to continuous monotonicity.

Both the e,λ defect identity and its separate continuous sufficient criterion expand correctly. The finite right gap Γ_R yields the claimed room for left defects; no general sign is assumed for e or λ.

For the mean-only certificate, the truncated left slot is again an actual upper-ideal slot in D^op. The identity H=M−M' is exact. Since β≤p<K=B+6, the coefficient K/β−1 is positive, allowing the lower bound on δ and upper bounds on δ' and N−qs to be substituted in the required directions. Formula (4.5) is correct and remains a sufficient, not necessary, criterion.

### S5. The analytic family and actual cross nonmonotonicity

For the stated antichain D family, J is uniformly distributed on 1,…,d. The displayed M,H,β and q,s values follow from its first two moments. Its δ and δ' attain precisely the lower and finite-size upper slot estimates, so the mean-only criterion equals the actual first-difference expression 6+8r/3−rn/3. The threshold n=8+36/(d−1), its strict/equality cases, and the d=3 comparison with the weaker 2−n certificate are correct.

The novel counter-control was independently checked using only the tiny cores, without reusing the author's slot calculation. Let D={a,b,c} be an antichain, a<z, D<C_m, and put every D,z,C_m element below a 30-point chain U; let y be completely isolated. Enumerating D+C_m+z gives 18 legal core words for m=1 and 24 for m=2. Append the fixed U chain and insert y in every slot. The actual totals are 648 and 888; the sums of the rank of a in those core words are 32 and 44, exactly the counts with y<a. Therefore the success probabilities are 616/648=77/81 and 844/888=211/222, with difference −1/5994. Data are in `independent_cross_control.json`.

This is an actual unweighted finite-poset counterexample to universal natural cross monotonicity. It is not a counterexample to the column theorem, a double-band example, or a global shortening obstruction. In fact the family's displayed high-side bound keeps this pair safely above 2/3.

### S6. The second block kernel and precise scope of safety

With D=W⊕V, the conditional insertion weights are affine in the appropriate block's left slot. Independent averaging gives the manuscript's V conditional weight and h(t)=(t+p+q+1)/T(t). Direct differentiation gives

h'(t)=−[(t+p+q+1)²+qs+s−N]/T².

Using the opposite directed T side N≤qs+q²+2q yields precisely the positive lower polynomial in (6.5). For V–z, the min-term loss is X_d, not zero; therefore H_d=β_d(p+1), F_d=β_d(p+q+1), and the failure probability is β_d h(t), as claimed. The older W kernel uses the other directed T side, so both remain valid with arbitrary U successor upsets.

The conditional block distributions are correctly described as linear tilts, not uniform projections. The common short-length inequalities in (7.1) control exactly the two named cross classes. Auxiliary internal probabilities inside the closed band make old safe block-internal pairs move farther along their existing side as the positive kernels grow under shortening. The explicitly remaining external categories are complete for this W/V structure; no V–y, U-internal, I–U, or I-pair claim is smuggled into the g/h theorem. The general t=2 remainder list is also correct.

Status boundary: the universal conclusions rest on the analytic proof, not on finite controls or agreement between agents. The independent computation here covers only the two stated tiny-core controls. No old enumeration or enlarged search was performed; no literature novelty determination is made.

## Locked final scope

Both new manuscripts are PASS. Their conclusions remain fixed-outer-chain-blowup effectivity and actual t=2 chain-column/cross-class consequences. This review does not certify novelty, prove arbitrary-external-pair preservation, or establish the global 1/3–2/3 conjecture.
