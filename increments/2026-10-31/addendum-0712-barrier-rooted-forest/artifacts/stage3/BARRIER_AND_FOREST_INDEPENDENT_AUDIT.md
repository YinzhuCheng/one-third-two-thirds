# Independent audit: single-barrier and independent-branch compensation

**Verdict:** both sufficient theorems in `BARRIER_AND_FOREST_COMPENSATION.md` have valid proofs under their explicitly stated hypotheses. The multibranch statement is not merely numerically plausible: its independent-replacement argument proves it. This verdict does not establish filtered-C2 applicability or historical novelty.

## 1. Arbitrary-poset window monotonicity

The chain Gibbs argument extends correctly to a finite induced poset W, provided each endpoint function is order-preserving along W. Nonempty feasibility implies a_w≤b_w, and isotonicity makes the entire vector a a feasible point. To reach a from any feasible state, update vertices in a linear extension of W, setting each coordinate to a_w. All strict predecessors have already been lowered to at most a_w, and all successors remain unchanged at values at least the old x_w≥a_w. Bounds are maintained. The reversed path is also legal, and every update has positive heat-bath probability. Thus the finite lattice chain is irreducible; positive self-loops imply aperiodicity. Its conditional uniform updates preserve the uniform counting law.

Under ordered endpoint systems and ordered current states, both conditional interval endpoints are ordered because maxima and minima are monotone. A shared coordinate choice and shared quantile therefore preserve coordinatewise order. Start at the ordered a-vectors and take the stationary limit. Inward rounding on a common fine lattice preserves isotonicity and cross-system ordering; positive volume ensures eventual lattice feasibility. Normalized lattice counting converges to uniform volume by Riemann sums, and a joint subsequential weak limit preserves the closed order relation. All equality boundaries are null. No total-order assumption is hidden in this proof.

## 2. Complete external inclusions and aligned reference window

Let A_ext be the union of all external predecessor sets of M, and B_ext the intersection of all external successor sets of M. The proposed a=max r(A_ext), b=min r(B_ext), with defaults 0,1, is valid. When both sets are nonempty, each x∈A_ext precedes some m∈M, while every y∈B_ext succeeds that same m, so x<y. For compatible interior external coordinates this gives a<b; the empty-set cases also give strict positive interval length almost surely on positive-volume fibers.

Every actual M lower endpoint is ≤a. Since B_ext is contained in every M successor set, every M upper endpoint is ≤b. The first required union/intersection inclusion puts every x∈A_ext below every point of K, so all K lower endpoints are ≥a. The second inclusion puts each external successor of any K point into B_ext; thus every K upper endpoint is ≥b. The minimum-over-subsets direction here is important and is correct.

Actual window endpoint functions are automatically isotone on the induced posets because full predecessor sets increase and full successor sets decrease along comparabilities. Reference windows are constant and hence isotone. Therefore the general window lemma applies to M and K, not merely to chains. Complete K–M incomparability leaves no cross-coordinate constraints after fixing R; conditioning keeps the true product-domain volume law. Full transitive sets, not merely generating neighbors, are required.

## 3. Single barrier and labeled extension decomposition

For any finite reference poset W with all coordinates in the same interval, every labeled linear-extension simplex has the same volume. Conditional on a particular extension, the sorted coordinates are the ordinary uniform order statistics, independently of which extension label sequence was chosen. Therefore a statistic whose rank is fixed in every extension has that same order-statistic law even when W is not a chain.

For M, its overall minimum always has rank 1 among m points, hence Beta(1,m) after normalization. For K=H⊕L, every H point is before every L point, so the first L coordinate has rank q+1 among q+l points in every extension, hence Beta(q+1,l). Arbitrary internal orders on H,L,M do not alter these ranks. The cited beta truncated-mean comparison therefore applies exactly, including q=0.

If H were merely a collection of differently distributed ancestors, without every H point below every L point, the fixed-rank argument would not follow. The complete ordinal-sum hypothesis is essential to this proof.

## 4. Multibranch theorem and the sum budget

For the reference K that is the disjoint union of the induced K_i, its order-polytope domain is a Cartesian product. Uniform volume consequently makes the component coordinate arrays independent, regardless of the internal extension counts of the components. This is a statement about continuous reference coordinates, not an assertion that arbitrary global rank interleavings or original P fibers are independently/uniformly weighted.

Thus X_i=min normalized L_i has independent Beta(q_i+1,l_i) laws. Set μ_i=l_i/(q_i+1)>0. The independently audited beta lemma applies to real second comparison parameter μ_i, with equality in its mean condition, giving
E min(X_i,t)≥E min(Y_i,t) for all real t,
where Y_i has Beta(1,μ_i) law.

Choose all variables in a replacement argument independently. At each replacement, condition on the other component variables and the fixed cutoff; their minimum is a fixed scalar t for the current independent variable. The one-variable inequality therefore applies. Integrating and repeating yields
E min(X_1,…,X_s,z)≥E min(Y_1,…,Y_s,z).
This step requires independence; merely having each marginal truncated-mean inequality would not be enough.

The independent Y_i minimum has survival (1−t)^(sum μ_i), hence Beta(1,sum μ_i). If sum μ_i≤m, it stochastically dominates Beta(1,m). The stated direction of the final expectation inequality follows. All μ_i are positive, and the real-parameter use is legitimate; no integrality of μ_i is needed.

## 5. C, weighting, and scope

C⊆R makes its minimum a fixed cutoff after conditioning; empty C uses cutoff 1. After affine normalization this cutoff may lie outside [0,1], but the beta lemma covers every real cutoff. The box couplings preserve increasing functions such as coordinate minima and their capped versions. Integrating the conditional inequality against the actual R marginal density retains the original measure. The order-polytope first-occurrence identity then gives the claimed unweighted extension sums, including empty-set sentinels where relevant.

For C2, the L and M used in the theorem must be the entire actual T10 sets. All anchors must be additional vertices, the full K–M incomparability and all block-external conditions must be verified in Q, and the independent-branch partition must have no cross comparabilities. A selected subcollection of L does not automatically yield the desired full-L inequality.

These are structural extensions of the previously audited rank/window mechanism. No claim that they avoid every older structural/numerical tool, solve all residual C2, or are historically new has been verified. No strict conclusion follows solely from a strict budget: C may precede every relevant point and make both first-occurrence quantities identical.

## 6. Explicit failure if arbitrary cross-branch comparisons are allowed

Take two nominal branches H1={h1},L1={l1} and H2={h2},L2={l2}, with m=1 and M={m} independent of all four points. Add the cross relation l1<h2, giving
h1<l1<h2<l2.
Each branch still individually has q_i=l_i=1 and the proposed sum budget equals 1=m; R=C=empty so all external conditions are vacuous. But Q is now a four-chain plus an independent singleton, with exactly 5 extensions. Directly,
B=sum first(M)=15,
Z=sum first({l1,l2})=12.
The conclusion fails. Thus dropping cross-branch incomparability is not just a gap in the product proof; the unrestricted extension is false.

This is a counterexample only to that relaxed interface. It is not a counterexample to either correctly stated theorem or to any balanced-pair conjecture.

## 7. Independent finite search

`independent_barrier_small_check.py` independently enumerates transitive closures and computes each first-occurrence sum by adding a fresh minimal insertion label and counting extensions:
- one nonchain fork H={h}, L={l1,l2} with h<li, singleton M, and two external points: 217 valid orders, all four C choices, 868 tested instances;
- two independent two-point branches, singleton M, and one external point: 19 valid orders, both C choices, 38 tested instances.
All 906 valid instances satisfy the theorem. The same script independently verifies the cross-branch counterexample's 5,15,12 counts. These finite checks supplement, not replace, the general proof audit.

Only /tmp audit artifacts were written; no repository or remote was modified.
