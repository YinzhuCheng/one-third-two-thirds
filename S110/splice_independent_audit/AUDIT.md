# Independent audit: one separated, buffered splice

Date: 2026-10-10. Disposition: **PASS for the sufficient theorem as stated**, subject to the explicit interior, separation, local-pattern, and buffered-profile hypotheses. This is a mathematical audit and local exact check; nothing was published or uploaded.

Audited source: `single_splice_stability.md`, copied verbatim to `proof_audited_snapshot.md` when this audit was finalized. `SHA256SUMS` identifies the exact snapshot and every audit artifact.

## Scope of the approval

For D >= 1, write R = 2D-1, h = 3D-1, K = 4D-1. The theorem assumes a >= K, b+K <= n, and L = b-a >= 2K+1. The complete relation patterns on U_a = [a-K+1,a+K] and U_b = U_a+L must match. The two required profile comparisons concern normalized F at a-h versus b-h and normalized B at a+h versus b+h, coordinatewise to relative error eta <= 1/2.

Under those hypotheses the encoded splice produces a genuine poset P' with maximum incomparability degree at most D. Every surviving original incomparable pair is same-side because L > R, and its actual-identity direction probability changes by at most eta. Every new cross-seam incomparable pair has an explicit genuine original local witness whose direction probability changes by at most eta. A stronger common bound is

  delta(eta) = eta / (1 + sqrt(1-eta^2)).

For absolute coordinate error epsilon, the stated degree-dependent conversion is

  error <= A_D epsilon,
  A_D = 1 + (binom(2D,D)-1) (2D)!/D!,

provided epsilon <= 1/(2 A_D). This conversion uses the separately proved positive lower bound for unmarked legal profile coordinates.

The audit does not certify central-only profile matching, cuts closer to physical endpoints than K, overlapping-cut preservation of all old actual identities, the existence of a uniformly gapped counterexample, a sequence of useful splices, an effective cardinality bound, or a proof of the 1/3-2/3 conjecture.

## 1. Legality and degree

Decoding retains all same-side relations. P' is not generally an induced subposet: crossing short-range relation bits are transplanted. For every pair of numerical labels in U_a, the decoded relation agrees with P on those same numerical labels. This follows from literal equality on the retained left, translation equality on the retained right, and the original bit at the translated right endpoint across the seam. Both endpoints of every relevant short-range bit lie in the matched buffers.

Any transitivity failure would have an incomparable outer pair, hence diameter at most R. A failure crossing the seam therefore lies entirely in [a-R+1,a+R], which is an unchanged copy of a real P interval. Same-side failures are already excluded. Increasing reference labels exclude cycles.

A new cross-seam incomparable edge has endpoints in [a-R+1,a+R]. Every potential incomparable neighbor of one of those endpoints is in [a-2R+1,a+2R]. Because K >= 2R, this entire neighborhood is an original P neighborhood inside U_a. Its degree is at most D. A vertex with no cross-seam incomparable neighbor only retains same-side old neighbors, so its degree cannot increase. This is a full degree argument; transitivity alone would not suffice.

## 2. Exact counts and actual normalized laws

Let c = a-h and d = a+h. The matched prefix extends through reference label a+K, and the matched shifted suffix starts at a-K+1. These are the exact labels inspected by the extreme transition steps. Thus the common-path identities are

  F'_d = F_d,       B'_d = B_(d+L),
  F'_c = F_c,       B'_c = B_(c+L).

In particular e(P') = sum_S F_d(S) B_(d+L)(S) = sum_S F_c(S) B_(c+L)(S). No normalization is performed before these exact factorization identities. The finite state supports at the offset cuts match because their full 2D-label windows are contained in the matched relation buffers.

At d the atoms are entire genuine length-d prefix extensions. Their original weights are B_d(S), and their new weights are B_(d+L)(S). If normalized B profiles are relatively eta-close, their ratio is a single common scalar times a number in [1-eta,1+eta]. Therefore the actual original prefix law, including its original F_d(S)B_d(S) state masses, is reweighted by a bounded positive density. Dividing by the new total mass gives exactly the uniform P' prefix law.

At c use entire shifted suffix extensions, with original weights F_(c+L)(S) and new weights F_c(S). The bounded density lies, up to a common scalar, in [1/(1+eta),1/(1-eta)]. Its ratio of extreme values is the same as in the prefix argument.

For any original probability p and conditional density averages u,v, the reweighted event probability is pu/(pu+(1-p)v). Optimizing u,v over [m,M] and then p gives (sqrt(M)-sqrt(m))/(sqrt(M)+sqrt(m)). This proves the claimed common bound and verifies that the actual joint original law is normalized correctly.

There is no uniform-deletion assertion. There is no assumption that F and B independently specify an arbitrary realizable joint law. There is no use of a marked-direction coordinate lower bound.

## 3. Identity and guard audit

Every old left vertex has reference label <= a and has been output by d. Therefore each left-side actual pair event is a common-prefix event. Every new right vertex has label >= a+1 and has not yet been output at c, so each right-side actual pair event is a common-suffix event under translation +L.

For a new cross-seam incomparable pair u <= a < v, its span is at most R and therefore v <= a+R. Both endpoints have appeared by output rank d = a+R+D. The common-prefix comparison uses the genuine original numerical pair (u,v). The actual right endpoint retained by the splice is instead old vertex v+L. This identity distinction is indispensable.

Because L > R, no old incomparable pair can have one surviving actual endpoint <= a and another > b. Thus the same-side clauses really do cover all surviving old incomparable pairs under the theorem assumptions. New seam pairs are covered by separate genuine witnesses; their old actual endpoints need not have been incomparable.

The conditions a = K and b+K = n are allowed. The extreme inspected labels then equal 1 and n, with no out-of-range access. One exact positive case tests both equalities and the minimum permitted separation simultaneously. Cuts nearer physical endpoints than K are excluded, and no clipped-window extension is silently assumed. D=0 is not a missing nontrivial case: there are no incomparable pairs, and it is intentionally outside the theorem.

## 4. Independent exact checks

`check_splice.py` builds the comparison relation directly, checks its transitivity, and computes every ideal as a full vertex bitmask. It counts complete ideal paths with exact integers and computes direction probabilities by summing contributions from transitions emitting the first endpoint while the second remains absent. It imports no theorem transfer implementation and makes no deletion-law assumption.

For each positive case it verifies full local-buffer equality, legality and degree, the common entire-prefix and entire-suffix restrictions, same-side actual relations, all four raw endpoint F'/B' identities, matching profile supports, and every incomparable pair probability in P'. Each comparison is exact rational arithmetic. It also checks the sharp bound without square roots using 2e <= eta(1+e^2), equivalent to e <= delta(eta) for e in [0,1].

Five positive cases use translation-invariant natural posets with the listed incomparable differences:

- n=29, gaps {1}, D=2, cuts (7,22): eta approximately 0.1458981105; maximum error approximately 0.00032810923. This is a=K, b+K=n, L=2K+1.
- n=61, gaps {1}, D=2, cuts (14,40): eta approximately 0.000147794081; maximum error approximately 1.48559e-7.
- n=121, gaps {1,2}, D=4, cuts (32,80): eta approximately 1.22529e-6; maximum error approximately 9.57002e-11.
- n=121, gaps {1,3}, D=4, cuts (32,80): eta approximately 0.000330727746; maximum error approximately 1.02658e-6.
- n=181, gaps {1,2,3}, D=6, cuts (50,110): eta approximately 3.34187e-7; maximum error approximately 1.02859e-11.

Together these examine 689 incomparable pairs: 284 same-side left, 390 same-side right, and 15 newly crossing the seam. All inequalities pass. The finite tests are corroboration, not a substitute for the general proof. Exact fractions, extension counts, and maximizing witnesses are in `exact_checks.json`.

## 5. Overlapping-cut negative control

The separation assumption cannot simply be removed while continuing to promise preservation of every surviving original actual incomparable pair. An exact control makes the reason concrete.

Let P have 101 naturally labelled vertices and declare i <_P j exactly when j-i belongs to {2} union {4,5,6,...}. Equivalently, the only incomparable differences are 1 and 3. The allowed difference set is closed under addition, so this is a poset; its maximum incomparability degree is 4.

Set a=50, b=51. Then R=7, h=11, K=15. All local relation buffers agree by translation, and both cuts are far from physical boundaries. The required buffered forward/backward profile comparisons have maximum relative error

  eta = 3880519595145 / 5236171458247602613
      approximately 7.41098649287489e-7.

But old actual vertices (49,52) survive and are incomparable, with

  Pr_P(49 before 52)
    = 32748907489668290491508999 / 36696510480113363113711279
    approximately 0.8924256574045545.

After deleting one encoding symbol, old vertex 52 has new label 51. New labels (49,51) differ by 2 and are comparable, so their direction probability is 1. The actual-identity probability error is

  3947602990445072622202280 / 36696510480113363113711279
    approximately 0.10757434259544554 > eta.

This example fails the stated cut-separation condition and is not a counterexample to the audited theorem. It does not refute narrower overlapping-buffer conclusions about same-side pairs or genuine new local witnesses. Indeed its four exact endpoint-count identities still hold. Its purpose is to prevent the old cross-cut identity case from being silently absorbed into a local-witness argument.

## 6. Residual limitations

The profiles must be close at a-h versus b-h and a+h versus b+h. Nonnegative transfer cannot be inverted to infer those comparisons from central-profile closeness. This audit supplies no central-only counterexample or theorem under the separated hypotheses.

A finite mesh and one-splice continuity do not establish an n-independent strict balance gap, an admissible sequence of splices, uniformly controlled cumulative error, or an effective finite counterexample kernel. The draft's discussion of possible repeated-error summation is conditional bookkeeping only; no existence or termination claim is certified here.

No mathematical defect was found in the separated, buffered one-splice theorem or its stated absolute-error corollary.
