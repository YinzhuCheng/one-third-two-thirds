# Independent five-class, one-nonsingleton-family audit

Verdict: PASS. For each frozen C08, C09, C11, C14 and C15, every positive-integer chain inflation with at most one nonsingleton block has a balanced pair. A no-balanced inflation of one of these five cores therefore has at least two nonsingleton blocks and order at least 10. This is separate from the C13 support theorem and does not exclude arbitrary support or prove sharpness.

## Identity and frozen scope

Author THEOREM.md SHA256: 1480dcbeab1bf5f6eb80989a13e7aaea1482f64a76460ab65b1b70b35e4209b8.

Author certificate.json SHA256: e07d48091d22ad661cfaa7292a6d9a96fec9840deae9be2ef9b3cd7056a50997.

All author-manifest entries were verified before copying. The exact five original class labels, strict relation tuples, and cover lists were compared with the earlier independently frozen catalogue. Each relation tuple also occurs exactly once among the original orbit audit's eight-point representatives. Covers were independently reconstructed. No author implementation was imported, no source was edited, and no external state was changed.

The audit uses the previously established core catalogue and necessary structural inequalities as prior dependencies. It does not rerun the original core classification or reprove the external good-pair theorem.

## Direct, symbolic reconstruction of count polynomials

For each relevant variable block, this audit literally enumerates all linear extensions of the seven-element outside poset. It computes the last predecessor position L and first successor position R, verifies L<R, and checks that every element strictly within the legal insertion window is incomparable with the block. With h=R-L-1, the number of legal insertions of a t-element chain is f_h(t)=binomial(t+h,h).

For an outside-outside pair, each fiber contributes either f_h or zero according to its outside order. For chain-before-outside endpoints, a singleton x left of the window contributes zero, and x right of it contributes f_h. At interior outside rank r, the bottom contributes f_h-f_(h-r), while the top contributes f_(r-1). If the chain is the second pair member, subtract its reverse orientation from f_h. These formulas include moving top endpoints. They are exact counts, not probabilities averaged under a uniform outside law.

Summing these fiber contributions reproduces every stored denominator and numerator coefficient exactly in the f_0,...,f_7 basis, for all 36 fixed-pair families and the rank-crossing family's two endpoint polynomials. This directly proves the count identities as polynomials of degree at most seven. The original verifier's alternative eight-point interpolation principle is sound because of that degree bound, but the audit does not rely solely on sampled evaluations.

Independently, a separately implemented occupancy recurrence recounts the total and both actual-element pair orientations at each t=1,...,8. All 296 family/length instances agree. The recurrence blocks the second member of a queried pair until the first has appeared; it never samples core extensions or treats outside extensions as uniform.

## Infinite integer-tail certificates

Every supplied Newton coefficient was independently reconstructed by forward differences. Both sides of each Newton expansion were additionally converted to the ordinary monomial basis with exact rational coefficients and compared symbolically. All 74 polynomial identities hold, and all stored Newton coefficients used for inequalities are nonnegative.

For integers t>=K, binomial(t-K,k)>=0, including zero when k>t-K. Hence these expansions prove the two balance inequalities throughout the full infinite tail. Thirty-four fixed-pair families start at K=2. The C09/block-2 and C09/block-7 families start at K=3; their t=2 witnesses were separately recounted. Their denominators are positive extension counts for every t>=1.

## Three inequality-bounded families

For C09/block-6, C14/block-6 and C15/block-6, the audit independently reconstructs the full structural bottom/top witness sets and coefficient rows from the core relation, and compares them with the prior audited rules. All three have incomparable outside mass five. The strict integer inequality is 2t<5, so a hypothetical no-balanced case with t>=2 has only t=2 remaining.

The recounted balanced pairs have counts 137/400, 131/374, and 239/374 respectively. Both orientations sum to the denominator. The C15 witness uses the actual top element of the doubled block, not an indistinguishable block symbol.

## Universal adjacent-rank gap proof and the exceptional family

The rank-gap lemma is valid for every legal window. Condition on a particular outside extension under its true marginal distribution. Within that fiber, the h outside positions in the t+h window form a uniformly selected h-subset. If x is its r-th outside element, the event that exactly k chain elements precede x implies that window position k+r is outside. Thus its probability is at most h/(t+h), and hence at most M/(t+M) when h<=M. If x is outside the window, the adjacent-rank difference is zero. Averaging the pointwise bounds with the true fiber weights preserves the inequality. No uniform-outside averaging occurs.

Because p_k=Pr(c_k<x) is decreasing, p_1>=2/3 and p_t<=1/3 together with t>=2M yield an actual balanced rank: an endpoint equality already suffices; otherwise the first drop from above 2/3 to at most 2/3 is of size at most 1/3 and cannot overshoot below 1/3. This argument is all-weight and does not require one fixed rank or endpoint to work for the whole family.

For C09/block-1, the audit confirms comparison vertex 3, incomparable set {2,3,5,6,7}, M=5, and K=10. The three exact fiber polynomial vectors and both threshold Newton vectors match the certificate. All eight t=2,...,9 witnesses are independently recounted. Therefore the finite prefix and infinite rank-crossing tail cover every t>=2.

Supplemental validation, not a substitute for the proof, checks 7,728 exact shuffle gap inequalities for h<=7 and 2<=t<=24. It also recounts every comparison with vertex 3 for every actual chain rank at t=10,11,12,20,40,100. All actual rank probabilities satisfy the monotonicity, gap bound, endpoint thresholds, and balanced-rank conclusion. These checks do not introduce a cutoff into the theorem.

## Exhaustiveness and reproducibility

Every one of the 40 class/block combinations is covered once: 36 fixed-pair infinite tails with complete finite prefixes, three inequality-bounded families, and one rank-crossing family. All five zero-support cases are recounted. There are 18 finite/zero-support witness certificates in total and 644 separately imposed pair orientations across the interpolation grids and these witnesses. The C11 all-singleton witness is exactly at the allowed boundary 212/318=2/3, which is correctly treated as balanced.

Run python audit.py or python -O audit.py. All checks use explicit exceptions and remain active under optimization. Both executions passed and generated byte-identical audit_results.json and logs. All independent symbolic vectors, witnesses, and supplemental actual-rank numerators are retained in that results file.

Run python verify_snapshot.py for manifest verification, isolated normal and optimized reproduction, and intentional-tamper rejection. The author's assert-based verifier is preserved as a source artifact; its execution under -O is not used as evidence.

No mathematical defect was found in this separate theorem.
