# Targeted actual multigate tests for general chain-column interlacing

Date: 2026-10-19. Status: **no failure in a frozen finite budget**. This is computational support, not a theorem or a claim about all actual posets.

## 1. Exact scope and outcome

For each actual finite outside poset R=D⊔I⊔U, all D are below all U, no I point is below any D point, and no U point is below any I point. Add the autonomous chain D<C_m<U with every x∈I incomparable to every c_i. Uniformity is over all labeled linear extensions of the resulting actual poset. We tested

Q_i(m+1)>Q_i(m)>Q_{i+1}(m+1), where Q_i(m)=Pr(c_i<x).

The pre-frozen budget in BUDGET.md has 28 outer families: seven multigate schemas times four I-order templates. Each family was evaluated at t=|I|∈{3,4,5,6}, the three gate aspect ratios (3,3), (23,1), (1,23), and m∈{1,3,11,47,191,767}. Every eligible i and every x were checked.

Results:

- 336 actual labeled outside-poset instances, with 336 distinct literal labeled transitive relation sets. No claim is made that they are pairwise nonisomorphic.
- 2016 adjacent-length comparisons.
- 3,084,480 strict inequalities, all positive by integer cross multiplication.
- 84 tiny independent full-bitmask ideal-DP controls, all matching the grouped transfer calculation.
- 16 additional full-bitmask controls with a two-element antichain clone block, explicitly verifying labeled clone multiplicities, all matching.
- A separate generic full-bitmask ideal-DP check of both large-chain totals and all three relevant event counts for the smallest-gap certificate is provided in minimum_gap_independent_check.json.

The seven side schemas are independent two-chain gates with staggered cuts; ordinally joined antichain blocks; independent antichain clone gates; a chain plus an incomparable antichain gate; three ordinal gate blocks; crossed two-chain cuts; and asymmetric opposite-marker gates. I is respectively an antichain, a full chain, an alternating fence, or two disjoint chains. The actual gate cuts, side orders, labeled vertices, and **all strict transitive outside relations** appear in all_actual_relations.json. Thus these are actual posets, not free insertion-window coefficients or an arbitrary positive polynomial model.

## 2. Counting method

For an internal-I ideal S, let

A(S)=e(D∪S),
B(S)=e(U∪(I\S)),

with inherited actual relations and the already placed S removed for the suffix. A and B are computed by exact side ideal DP. A chain group of size n has one available next element; an antichain clone group with k elements already placed has n−k labeled choices. This produces labeled, unweighted actual LE counts.

Let H_0(S)=A(S), G_0(S)=B(S). Define the internal-I ideal-lattice recurrences

H_j(S)=H_{j−1}(S)+Σ_{x maximal in S} H_j(S\{x}),
G_j(S)=G_{j−1}(S)+Σ_{x minimal in I\S} G_j(S∪{x}).

The H recurrence is evaluated in increasing ideal size, the G recurrence in decreasing ideal size. These sum all possible I words in a gap between consecutive chain points. Consequently

Z_m=e(P_m)=Σ_S H_{m−1}(S)B(S),
N_{i,x}(m)=Σ_{S:x∉S} H_{i−1}(S)G_{m−i}(S),
Q_i(m)=N_{i,x}(m)/Z_m.

The first chain point follows any valid D∪S prefix; the last is followed by the actual B suffix. This avoids counting a pre-/post-chain I word more than once. No uniform-projection assumption is used: the A/B weights preserve the actual external-LE insertion tilt.

Each test compares the positive integers

N_{i,x}(m+1)Z_m−N_{i,x}(m)Z_{m+1},
N_{i,x}(m)Z_{m+1}−N_{i+1,x}(m+1)Z_m.

The independent controls build the full labeled poset from ordinary generating relations, use an unrelated bitmask-ideal recursion, and obtain event counts by imposing c_i<x or tracking the first of the two points. They do not call the grouped recurrence for their answers.

## 3. Smallest tested probability gap

The smallest gap over the frozen budget is the right-hand gap at case 22, t=6, I a full chain, staggered two-chain gates of sizes (23,1) on each side, m=767, i=767, x=x_0. Complete actual relations and cuts are in the certificate and relation manifest.

Z_767=201076840840212480,
Z_768=202600518647151936,
N_{767,x_0}(767)=576,
N_{767,x_0}(768)=4032,
N_{768,x_0}(768)=576.

The smaller right-hand gap is exactly

576/Z_767−576/Z_768
=23807465733429/1105096360735619317289822403520
≈2.1543339186802952×10^−17>0.

The unreduced integer cross difference is 877638416797126656. The tiny value is not rounded to zero: all decisions are exact. See minimum_gap_certificate.json and minimum_gap_independent_check.json.

## 4. Reproducible artifacts and boundary

- BUDGET.md: frozen structural budget.
- test_actual.py: own exact grouped ideal-DP/transfer implementation plus full-bitmask tiny controls.
- manifest.json: full parameter instances.
- all_actual_relations.json: all labeled outside vertices and complete strict comparability sets, with the unique recipe for adjoining C_m.
- all_exact_counts.jsonl.gz: **every tested pair of lengths**, its two exact totals, and the complete i×x numerator arrays at both lengths, as decimal integers. This is a data certificate, not executable code.
- results.json: per-instance/per-length exact minimum gaps.
- summary.json: counts and exact scope.
- minimum_gap_certificate.json, minimum_gap_independent_check.json: least-gap witness and unrelated full labeled DP verification.
- write_certificates.py, verify_minimum_independently.py: own certificate-writing and independent verification programs.
- run.log, certificates.log: execution summaries.

No failure appeared, so the instructed failure/minimization branch was not entered. The pool was not broadened after this frozen budget. This computation gives no conclusion for t>6, untested gates, untested lengths, or all actual posets. It also gives no statement about external pairs, global balance preservation, or a global safe-shortening landing point.
