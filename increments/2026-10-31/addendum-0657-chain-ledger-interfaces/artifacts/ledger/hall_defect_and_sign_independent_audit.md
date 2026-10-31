# Independent audit: block-defect ledger and cardinality-sign examples

**Verdict: the general ledger proof, its stated 15-point calculation, and both 12-point sign examples pass independent audit.** This receipt records work already completed before packaging; it is not a substitute for the underlying proof or an assertion of complete C2 coverage.

## General ledger

Audited source: `hall_block_defect_ledger.md`.
At every cutoff k, use its actual definitions: S avoids M1∪M0∪C; T avoids L1∪M0∪C; A avoids L1∪L0∪C. All are sets of actual extensions of Q. The interval-component swap is an involution on permutation words. Its forward action on S is legal by the external inclusion hypotheses. On T, all selected components have the reverse orientation, and the reversed word has the correct S avoidance condition; its only possible defect is illegality as a Q extension. Consequently its exact image is T\\G_block, where G_block is the set of targets whose reverse swap is illegal.

The local illegality criterion is complete: some selected pair interval contains a fixed external point in D_R(l)\\D_R(m) or U_R(m)\\U_R(l). Internal chain/block relations remain ordered by the component construction. These are union events; overlapping witnesses must not be added repeatedly.

Therefore |S|=|T|−|G_block|. With Hplus=T\\A and Hminus=A\\T, elementary set differences give |T|−|A|=|Hplus|−|Hminus|. Summing over cutoffs proves B−Z=Hplus−Hminus−G_block for arbitrary finite instances satisfying the hypotheses. This is a genuine general counting argument, not an extrapolation from enumeration. It supplies no universal estimate on the net budget.

The asserted upper-ideal property of L1 and lower-ideal property of M1 follows from the external inclusion conditions and full L–M cross-incomparability, with all unmatched vertices included in R.

## Independent 15-point verification

I independently computed transitive closure and enumerated all 2,301 Q extensions. For each cutoff I explicitly constructed S,T,A and the actual forward image, checking legality and injectivity. G_block was counted as the actual set difference T\\image(S), not inferred from the proposed weighted blocker formula. Every missing target was also checked by its inverse swap and its lower/upper interval blocker.

Results:
- B=12,891; Z=9,101; B−Z=3,790.
- a2↔f0: Z1=14,952; Hplus=5,851; Hminus=0; G_block=2,061. Lower blockers:1,374; upper:1,287; both:600; upper-only:687.
- a4↔f0: Z1=14,959; Hplus=5,858; Hminus=0; G_block=2,068. Lower blockers:1,706; upper:930; both:568; upper-only:362.
- With N=201,453 and R0=66,867, the allowed menu net budget is 568, so the actual 3,790 exceeds it by 3,222.

Portable independent script: `block_defect_15_independent.py`.
Results: `block_defect_15_independent_validation.json`.
The script currently reads the explicit EXAMPLE.json at the original local path; adjust only that input path when relocating the artifact. The original script's integer division 2*N//3 happens to be exact here because N is divisible by 3; a general implementation should retain rational arithmetic or cross-multiply.

## Independent audit of the two 12-point examples

Audited source: `cardinality_sign_examples.md`. I independently formed the full transitive closure from its shared root edges and its two alternatives. The essential v<f edge is present; thus f is not accidentally an additional incomparable point of v. Both examples have complete C2, A={a1,…,a5}, L={a4<a5}, M={f}, C empty, and maximum incomparability degree exactly 9.

For the seven-chain plus singleton Q, there are exactly 8 extensions. The singleton occupies each of the 8 positions once, giving B=36. The first L point is the sixth chain point and has mean position 6*9/8=27/4, giving Z=54. Hence B/Z=2/3.

For the independent chains of lengths 3,2,2 plus singleton, Q has 8!/(3!*2!*2!)=1,680 extensions. A specified chain's positions form a uniform subset because the number of extensions on the remaining independent components is constant for every position choice. Thus mean singleton position is 9/2 and mean first position of the L two-chain is 9/3=3, giving B=7,560, Z=5,040, B/Z=3/2.

Independent exact enumeration reproduced all four B,Z integers. These calculations use uniform LE(Q) only to express the unweighted sums defining B and Z; they do not falsely assign equal probability to distinct insertion fibers of P. Both examples have nontrivial autonomous modules. They prove only that |L|=2,|M|=1, even with A5 and Δ9, does not determine the sign of B−Z; they are not filtered-residual counterexamples.

## Empty-M boundary

The additional claim M=empty,L nonempty implies B>Z is also correct under C2. Since C⊆F=U(c2) and L⊆A is disjoint from U(c2), no C point can lie below any L point. For any l∈L, the down-ideal D_Q(l)∪{l} is disjoint from C and can be the first block of a complete extension, producing strict first(C)>first(L∪C). Other extensions give the weak inequality. If C is empty, its sentinel is |Q|+1 and strictness holds on every extension. This uses C2 stratification and the B/Z insertion identities, not merely arbitrary disjoint sets.

No repository or remote was modified in these audits.
