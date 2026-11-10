# Independent review: private-root bounded-rank gate

2026-11-10. PASS for PRIVATE_ROOT_RANK_GATE.md, the unified replacement for the earlier DH/multiple-head/one-defect presentations. This is an analytic sufficient condition for the existing two-event bank, not a finite profile certificate.

## Original-P proof audit

The exact FG1 ideal/exterior contract is retained. It supplies a legitimate partition into actual first-exterior-prefix ideals and complete literal suffixes, so raw prefix extension counts give the true original completion weights. When the exterior is empty, the single prefix is the entire marked ideal. Cells missing u or b pay by a forced event. All remaining cells have the previously independently audited per-internal-word signed count (k+4)J-2(k+1).

A chosen private minimum p of H is fixed at the original structural level. As p is minimal, R=H minus ({p} union U_H(p)) is exactly its set of incomparable partners within H. For an ideal K lacking p, every member of K belongs to R: containing any successor of p would force p into K. Therefore k<=r<=2, and the pointwise lower bound 2-k is sufficient.

For K containing p, let r_K=|K intersect R|. Only those r_K labels can precede p. Moving p to the front preserves all other relative orders, and cannot violate a predecessor condition because p is minimal in K. It also cannot violate a successor condition, because p moves earlier. Given an image beginning in p, a preimage is uniquely determined by the old position of p, and every legal old position is at most r_K+1. Thus the map from all K words to p-first K words has multiplicity at most r_K+1, including the identity preimage. This proves the first-letter probability bound in exactly the direction required.

The word-first event implies J>=2 because p is private; all words have J>=1. If no common point occurs, the sentinel J=k+1 still respects these inequalities. The resulting average margin is exactly bounded below by [6-r_K(k-2)]/(r_K+1). It is nonnegative directly for k<=2, and for k>2 follows from r_K<=r, k<=|H|, and r(|H|-2)<=6. The r=0 case causes no division or size-bound problem.

The uniform LE(K) notation merely divides the sum of the exact per-word raw margins by e(K). It is not an assumption that deleting b induces uniform internal K words. Summing those nonnegative raw sums over the actual prefix/suffix cells proves the fixed original-P bank 2Pr(u<b)+Pr(v<u)>=1. Neither the physical events nor their coefficients depend on the selected cell. No NB inheritance or exterior-word reweighting occurs.

The regimes r=0 (arbitrary tail size), r=1 (tail size at most eight), and r=2 (tail size at most five) are correct. The previously audited two-head gate, its two-common-head corollary, and the one-domination-defect proposal all lie inside this one condition. Their source counts must not be added separately.

## Independent packet reconstruction

PRIVATE_ROOT_RANK_INDEPENDENT_CENSUS.py scans the original seven-phase packet without using the author's replacement list. It derives actual exhausted/saturated v witnesses, forms Q_mark minus U(v), checks the complete root pattern and tail, then searches its private minima and verifies r<=2 and r(|H|-2)<=6. It also checks the source reference b<u<v and records the fixed physical events' endpoint depths.

The independently reproduced counts are:

    applicable: 102;
    overlap with baseline404: 53;
    overlap with separately mapped four-equal-downset30: 0;
    new beyond434: 49;
    prospective combined union: 483;
    remaining original bank occurrences: 3469-483=2986.

The new rows comprise nineteen phase-zero terminal rows and thirty phase-zero degree-saturated nonterminal rows. Every charged endpoint b,u,v has at most one full predecessor. The six newly gained rows relative to the old DH union are all terminal and have r=2. The other forty-three new rows are the previously audited DH contribution. Expanded applicability to old rows adds no further count.

The independent source records and witnesses are saved in PRIVATE_ROOT_RANK_INDEPENDENT_CENSUS.json. This audit does not substitute for the separate reviewer's approval of the four-equal-downset theorem; it verifies zero overlap with its exact thirty-row map. The live ledger remains the parent's responsibility.

## Actual D9-class r=2 stopping control

Independently checked the ten-label original poset Q=P with full predecessor masks (0,0,1,1,5,7,7,119,119,119). Its tail has private minimum p, two common minima h1,h2, and three mutually incomparable upper labels each above all three tail minima. Thus r=2 and |H|=6, violating precisely the size-five condition for r=2. The full maximum incomparability degree is eight, so this is genuinely within the D9 class, not a higher-degree surrogate.

Forward subset event DP and direct enumeration of all original words independently agree: N=1044, K_(u<b)=432, K_(v<u)=156, hence 2K_(u<b)+K_(v<u)-N=-24. Independently, H has 3!3!=36 extensions, and its first common rank has mean 4/3, giving 36[(6+4)(4/3)-2(6+1)]=-24 via FG2. This confirms that the r=2 tail-size cutoff cannot be replaced blindly by six for this same fixed bank, even within D9. The event u<b has probability 432/1044=12/29, already balanced; no NB or general balance counterexample is claimed. See PRIVATE_ROOT_RANK_CUTOFF_INDEPENDENT.py/.json.
