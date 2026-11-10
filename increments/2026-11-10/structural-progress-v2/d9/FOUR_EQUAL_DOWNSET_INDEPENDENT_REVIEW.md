# Independent audit: four equal full downsets

2026-11-10. **PASS** for FOUR_EQUAL_DOWNSET_ANALYTIC.md, its thirty-row application, and the specific cap-seven stopping control below. No main ledger or external destination was changed.

## Mathematical audit

I independently derived the sorted insertion representation and pair probabilities before reading the author's completed proof. If the four labels share their full strict downset, no two are comparable. For a fixed literal word of the other labels they have the same lower boundary, after their last predecessor. Every exterior letter after that boundary and before the first successor of a given mark is incomparable with it. Three incomparable partners are the other marks, leaving at most six such letters under degree nine. This justifies upper gaps in [0,6] even when the common downset is nonempty or the four-mark set is not an ideal. An absent first successor means the word end and causes no exception.

Sort caps d_i for counting only. On inserting the i-th mark, all earlier inserted marks are before its exterior upper boundary because their caps are no larger. Thus there are exactly L_i=d_i+i slots, independent of earlier choices. The construction is bijective with legal full insertions; consequently independent uniform slot choices give exactly the uniform conditional extension law. This is not a uniform distribution on deadline vectors.

For i<j, the current absolute rank of mark i within the shifted segment increases in conditional expectation by the factor (1+1/L_k) at each intermediate insertion k: exactly its current rank many slots precede it. Its initial mean rank is (L_i+1)/2. Dividing by L_j gives the exact q_ij formula, and the product of adjacent r_k telescopes to the same expression. Subsequent insertions preserve the pair order.

The auxiliary partition argument is valid specifically for four labels. For a fixed partition into B consecutive blocks the reference score is (4-R)/2+d. Every block occurs, so R>=B. If d=0 then R=B; otherwise B>=2 and R-B<=4-B<=2<=2d. Hence sorted-reference cost is minimal for every partition and therefore in expectation. The physical reference remains fixed across exterior words and sorted-cap changes. This argument must not be extended to arbitrarily many marks without a new bound on R-B.

The strict lower bound is a genuine continuous inequality, not a finite profile table. Multiplying the proposed lower bound minus two by positive 10xy gives the stated quadratic. Its negative discriminant H is positive on [3,9]: the expansions at 7 are correct, and for 0<=s<=4, -s^4-10s^3>=-56s^2 gives the displayed positive quadratic 67s^2-60s+124. Thus all conditional reference sums exceed one. Summing their count margins with the actual original exterior-word counts proves the original-P theorem. There is no NB assumption on a helper and no unproved independence of marks in the original law.

## Independent DP corroboration and a real stopping line

FOUR_EQUAL_DOWNSET_INDEPENDENT_CHECK.py builds the actual four-mark-plus-exterior-chain poset and counts extensions and six pair events by forward subset DP. It does not use the insertion formula to generate these counts. For all 210 sorted cap quadruples in [0,6], all six exact pair probabilities match the formula, and all 24 physical reference orders obey the proved bound. The diagnostic minimum sum is 141/140 at caps (0,2,4,6). These finite checks corroborate the proof; they are not its positivity dependency, and the observed sharp minimum is not asserted as a proved sharp analytic constant here.

A real cap-seven control uses caps (0,1,3,7), four minimal marked labels, and an exterior chain of length seven; mark i precedes exactly the exterior suffix starting after its cap. All four downsets are empty. Its maximum incomparable degree is ten (the marked degrees are 3,4,6,10; each exterior degree is at most four). Independent DP gives N=198 and sorted-adjacent reversal counts (66,66,63), so the bank sum is 65/66<1. This refutes extension of THIS fixed adjacent bank to uniform cap seven / degree ten. It is not a counterexample to the D10 balanced-pair conjecture or to an NB theorem: the first two adjacent probabilities are exactly one third, already balanced.

## Independent mapping and de-duplication

I independently scanned the unmodified original packet, grouping labels by equal transitive predecessor mask, retaining groups of size at least four with predecessor count at most eight. For every non-switch source record I selected four such physical labels and oriented the three adjacent events opposite their order in the stored reference. Equal Q masks give equal full original downsets because Q is an ORIGINAL ideal; that implication would not hold for a merely induced, nonideal marked set.

Exactly thirty occurrences qualify, all phase 0 mode 0 with masks (0,0,1,1,7,7,7,7) and labels 4,5,6,7. Every endpoint has three predecessors. The complete independently reconstructed rows are saved in FOUR_EQUAL_DOWNSET_INDEPENDENT_MAPPING.json. Their keys are disjoint from the 400 earlier analytic rows, the two reviewed Q8 rows, and the two new rank-gap rows. Thus adoption adds 30 to 404, giving 434 analytic replacements and leaving 3,035 of the 3,469 original bank occurrences unchanged. This changes no structural coverage argument or whole-D9 claim.

## Independent rejection of the exclusive-upper ratio strengthening

RANK_EXCLUSIVE_RATIO_CONTROL.md/.py is also correct. For masks (0,0,2,6,6,6,2,2,2,2), x is isolated, a is the unique minimum after deleting x, and y must precede three of the remaining eight labels. The four distinguished positions occupied by y and those three successors are uniform among the eight positions, with y in their minimum. Its expected rank there is 9/5, so its full deletion-word rank is 14/5. Inserting isolated x into ten equiprobable gaps gives Pr(x<y)=7/25.

A separate forward DP, rather than the author's recursive forbidden-event DP, reproduces N=100800 and K=28224. Here r=1, k=3, and full maximum incomparable degree is nine, so 7/25<1/3 disproves the suggested (r+1)/(r+k+2) bound. The actual rank-gap bound 2/10 remains valid. This is a rejected-route control only: it adds no ledger rows and is not NB or a counterexample to D9 balance.

## Source-attribution correction

A direct check of fixed-v22 §24.4.1 confirms that Fathi already explicitly states the identical-strict-predecessor-set application of Proposition24.4. Consequently the present theorem does not enlarge his scope: it supplies a continuous analytic replacement for the original74-vector positivity count. The30-row proof-style census and mathematical review are unaffected.
