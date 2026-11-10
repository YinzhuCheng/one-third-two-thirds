# Independent review: dominant-downset four-label gate

2026-11-10. **PASS** for the general gate and the independent whole-packet mapping. This supersedes the narrower three-equal-downset stopping application; their counts must NOT be added together.

## Precise original-P theorem

Let x1,x2,x3,x4 be a fixed PHYSICAL reference on four pairwise incomparable elements of any finite original poset P. Assume each has full incomparable degree at most nine and

    D_P(xi) contained in S=D_P(x1), for i=2,3,4.

Then, under the uniform original extension law,

    Pr(x2 before x1)+Pr(x3 before x2)+Pr(x4 before x3)>1.

The downstream downsets need not equal one another or S. S may be any original ideal, including the empty ideal; other original minima are permitted. No pivot memory, only-two-minima condition, or NB hypothesis is required.

## Independent proof audit

Partition original extension words by their exact literal prefix ending at the first of: any marked label appears, or S has been completely placed. If S is empty, the stopping prefix is empty. No mark is in S, by the antichain assumption, so for nonempty S the two stopping conditions cannot first occur at the same letter. These prefixes are exhaustive and prefix-free.

If a mark appears before S completes, it cannot be x1 because all of S precedes x1. Thus the first appearing mark is xj with j>=2. Its preceding REFERENCE neighbor x_(j-1) has not appeared, since this is the first of all four marks. Hence the charged adjacent reversal xj before x_(j-1) equals one in every completion of this prefix. All other charged indicators are nonnegative, giving a sum at least one pointwise.

If S completes before any mark, then all four marks remain. Every predecessor of each has been removed by the downset containment assumption, so they are actual minima of the induced remaining poset. Conditional on the exact prefix, its legal suffixes are in bijection with all extensions of that remaining poset and are uniformly distributed. Their incomparable degrees cannot increase upon deleting prefix labels. The independently reviewed FOUR_EQUAL_DOWNSET_ANALYTIC.md applies to these four minima and the SAME reference, and gives a strict sum greater than one in every such cell.

This second kind of cell has positive mass. S is an original ideal disjoint from the marks, so any linear extension of S can be used as an initial prefix and extended to P. It reaches completion of S without encountering a mark. For S empty this holds immediately. Consequently averaging the weak first-kind and strict second-kind inequalities with their TRUE original cell sizes yields the strict original-P conclusion. Nothing assumes that the conditional remaining poset is NB, and nothing treats distinct prefix cells as equally likely.

These arguments explicitly cover complicated S, unequal downstream downsets, additional minima, the empty ideal, and all positions of the first encountered mark. The proof does not choose the reference, its three events, or their unit coefficients after seeing a prefix.

## Independent original-packet mapping

DOMINANT_DOWNSET_FOUR_INDEPENDENT_CHECK.py reconstructs the prior 483-row union from the saved constituent mappings, including the two promoted Q8 rows. It independently scans ALL 3,469 non-switch records, enumerates four-label antichains, restricts the stored physical reference to them, and tests whether its first label's predecessor mask contains the other three masks. Charged endpoints are also required to have at most eight predecessors.

Each marked Q in this source is an ORIGINAL ideal; this is why its predecessor masks give complete original downsets. Equal/contained downsets inside a merely induced, nonideal subset would not suffice. The full degree-nine assumption is inherited from the ambient theorem, not inferred from internal degrees or a conditioned deadline. No actual exhaustion is required, making the mode-0 applications legitimate.

The independent structural census gives:

- 155 applicable source occurrences;
- 32 already covered by the prior 483-row union;
- 123 new occurrences, all mode 0;
- new rows by stage 0,2,4,6: 116,4,2,1;
- maximal charged predecessor count six;
- prospective analytic union 606, leaving 2,863 original banks unchanged.

All rows and their reference-adjacent reverse events are retained in DOMINANT_DOWNSET_FOUR_INDEPENDENT_CHECK.json. This is metadata applicability checking, not a profile-probability positivity certificate. The continuous four-minima inequality and the stopping proof supply the mathematical payment uniformly.

## De-duplication and scope

The four-equal-downset gate and the narrower three-common-downset-plus-one-subset gate are special cases. Their former 30-row and prospective 64-row contributions must not be added again. The present union is computed directly against the actual prior 483 rows, not by stacking provisional counts. The separate three-private-head initial ordering step is another special case (first reference label has downset {a}, with b's downset empty). It removes that separate 978-profile payment dependency but is not an extra row of the 3,469-bank packet.

No structural phase-coverage theorem, later 174-word three-fork tree, or whole-D9 analytic closure is inferred. No novelty or external peer-review claim is made. No main ledger or external repository was modified by this independent review.

## Final author-document comparison

Read REFERENCE_FIRST_DOWNSET_DOMINANT_FOUR_GATE.md in full. Its statement, stopping proof, antichain recognition test and attribution/limits agree with this review. All 155 source keys in REFERENCE_FIRST_DOWNSET_DOMINANT_FOUR_CENSUS.json match the independently reconstructed key set exactly. The result applies to the specified dominant-first reference; it does not assert that every four-label reference satisfies the bank or, without an applicable majority reference, that these four labels always contain a balanced pair.
