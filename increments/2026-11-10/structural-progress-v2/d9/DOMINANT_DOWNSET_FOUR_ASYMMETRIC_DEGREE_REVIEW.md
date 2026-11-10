# Independent addendum: only the last three degree bounds are needed

Superseded in parameter strength by FOUR_BANK_LAST_ONLY_DEGREE_INDEPENDENT_REVIEW.md: only the reference-last label needs degree at most nine. The results below remain valid special cases and add no count.

2026-11-10. **PASS**. This strengthens the parameter contract of the four-label base bank and its dominant-downset lifting, without changing the D9 source ledger.

## Strengthened statements

For a fixed physical reference x1,x2,x3,x4 on four labels with identical full strict downsets in a finite original poset, it suffices to require full incomparable degree at most nine for x2,x3,x4. There is NO degree bound on x1. The three adjacent reversal probabilities still sum strictly above one.

The same asymmetric degree assumption suffices for the dominant-downset version: the four labels form an antichain and D(xi) is contained in D(x1) for i=2,3,4. The first label must still be first in the reference; no assertion is made for an arbitrary permutation of labels with different degree bounds.

## Base inequality audit

Fix an actual exterior word and shift past the last common predecessor, just as in FOUR_EQUAL_DOWNSET_ANALYTIC.md. The last three physical labels have integer upper gaps at most six because each already has the other three marks as incomparable partners. The first label has an arbitrary FINITE nonnegative upper gap. All legal insertions retain unit count weight.

If the first label's gap is not maximal, one of the other three gaps is at least as large, so all four gaps are at most six. The already reviewed continuous four-label proof applies without change.

Otherwise sort the gaps nondecreasingly, breaking maximum ties so that the first PHYSICAL reference label is LAST in this counting order. The exact sorted-slot formula remains valid for any finite upper gaps: L_i=h_i+i, r_i=(L_i+1)/L_(i+1) in (0,1], and the reversed probability for sorted i<j is one half the product of intervening r's. Neither that formula nor the auxiliary independent-cut representation used an upper bound of six.

For a particular auxiliary partition into B consecutive blocks, the physical reference begins in the highest block. If B>=2, the four-label reference visits every block and therefore has at least one descending block transition, d>=1. With R its number of block-name runs, the reference's conditional block score is

    (4-R)/2+d >= 1,

since R<=4. This argument does not assume the other three physical labels appear in sorted order. If B=1, the score is exactly 3/2. The probability of B=1 is r1*r2*r3>0, because all finite slot counts are positive. Therefore the true conditional adjacent bank is at least

    1 + (r1*r2*r3)/2 > 1.

The auxiliary partitions are used solely to represent the pair probabilities of the same uniform insertion law. They do not replace actual exterior-word weights. Summing the strict conditional count inequalities over actual original exterior words proves the original-P statement. The argument establishes strictness for each finite poset; it does not promise a uniform positive slack independent of the unrestricted first degree.

## Dominant-downset lifting audit

Use the unchanged stopping-prefix proof with S=D(x1). Before S is complete, a first encountered mark cannot be x1 and forces one charged reversal to equal one. When S completes before any mark, all four marks are minima of the actual remaining poset. Conditional on the literal prefix, the suffix is uniform over all extensions of that remaining poset. The incomparable degrees of x2,x3,x4 remain at most nine, while x1 may retain any degree. Apply the strengthened base inequality above. The S-completes-first branch has positive mass because S is an ideal disjoint from the four marks, including the S-empty case. Actual prefix-count averaging therefore gives the same strict original-P bank.

No degree bound on x1 is used at any step. No NB assumption is inherited through a prefix, and the physical reference stays fixed.

## Scope and bookkeeping

This can apply in a degree-ten setting when the chosen reference's last three labels individually have degree at most nine, with its first label satisfying the dominant-downset condition. It does NOT establish the four-label bank for four unrestricted degree-ten labels, or a whole-D10 balanced-pair theorem. It also does not remove the dominant-first reference condition.

All labels in the existing D9 census already have degree at most nine, so this parameter strengthening alone adds no source rows and changes no ledger count. No main ledger or external destination was modified.

## Correction to the proposed Y_x width remark

The proposed set Y_x={y: x precedes y in T, y incomparable with x, D(y) contained in D(x)} is automatically an antichain. Indeed, if distinct y,z in Y_x satisfied y<z, then y belongs to D(z), hence to D(x), contradicting y incomparable with x. Thus the previously proposed comment that long chains can belong to this Y_x is false and should be removed.

Under the original strict two-thirds reference hypothesis, the dominant-downset gate correctly implies |Y_x|<=2 (and hence width<=2) in degree nine. Three members would automatically form an antichain and supply the forbidden dominant-first reference. With the asymmetric strengthening it is enough that the members being counted individually have degree at most nine; x itself needs no degree bound. This remains a consequence under the stated original reference hypothesis, adds no ledger rows, and does not by itself close a pivot phase.
