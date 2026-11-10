# Independent audit of MF2: x-frontier extension

2026-11-10. **PASS for the corrected frozen manuscript.**

Source: `MOMENT_FREE_X_FRONTIER_EXTENSION.md`, SHA256
`d9c413ea06f0648a22734cde0f6a56e35dd302d6b385df9b289cf9c2a62b6a56`.

This reviewer did not participate in MF2's derivation. I read the source, corrected MF1 source `ee284d443736573468786cc11060d9eff3447938f9930ad6136d158e6fac5a48`, and its independent review `MOMENT_FREE_FRONTIER_INDEPENDENT_REVIEW.md`. I independently checked the hypothesis weakening and reconstructed the counting, stochastic comparison and arithmetic below. This is internal independent review, not formal verification, external peer review, originality certification or an original-poset search. 

## 1. Hypothesis weakening is legitimate

Select r distinct C-minima satisfying x<c, not necessarily y<c or z<c. They form an antichain. Deletion and insertion depend only on their C-order: they have no retained C predecessors, so their legal gap deadlines are their first retained successors in a fixed actual gamma in LE(C−S). Every gamma label before that successor is incomparable with the selected point. The other r−1 selected minima are also incomparable with it. Therefore each deadline is at most d−r+1 using its **original C degree**, with no recomputation or inheritance assumption for a deleted poset.

For the kernel step only x<c is needed: the first selected point terminates the x-missing initial run. Thus h_x≤min(k,H), where H is the number of retained gamma labels before that first selected point. The full signature was not otherwise used. In particular, partial signatures do not invalidate any insertion count in C and are accounted for by the original exact kernel's additional nonnegative 9(h_y+h_z) term.

## 2. Genuine fibers and FKG

For fixed actual gamma and selected relative order pi, let D=d−r+1. The legal full C words correspond bijectively to strictly increasing selected positions s_1<...<s_r in [1,D+r] with s_j−j no larger than the selected label's individual deadline. Same-gap placements have exactly one representation for each actual pi. If gamma is shorter than D, fixed terminal placeholders add no placements because all deadlines remain bounded by the real gamma length. If gamma is longer, its suffix beyond D is fixed after all selected labels. No suffix multiplier is lost.

The unrestricted increasing tuples form a distributive lattice under coordinatewise min/max; uniform measure is log-supermodular. Feasibility is a decreasing, nonempty event. FKG applied to an increasing event {s_1−1≥t} and the increasing function minus the feasibility indicator gives the upper-tail domination after conditioning. This is a legitimate negative correlation between an increasing and decreasing event, not an assertion that arbitrary conditioned variables are independent.

Consequently the feasible H is stochastically no greater than the unrestricted first-selected-gap distribution

    P(H=t)=binom(D+r−t−1,r−1)/binom(D+r,r).

At fixed h, increasing q by one changes the relaxed kernel by 8(q−h)≤0. For m≥1 its minimum at q=min(m,h) is decreasing in h: below m it is 48+2h−4h², with forward difference −8h−2; after m the slope is 6−8m<0. Hence actual F is at least the decreasing MF1 G(H), and stochastic comparison gives the stated B lower bound on each genuine fiber average.

Crucially, one then multiplies by each fiber's actual number of words. Summing these disjoint fibers gives sum_beta F≥B e(C), not an equally weighted average of gamma/pi classes. The original complete event law adds the nonnegative 2X+Y. No OLD moment, conditional moment, deleted-object probability law, or selected wordwise pair is used.

At m=0, the separate F≥48 bound is correct and necessary; the stronger syntactic B formula is not imported from the erroneous initial MF1 quantifier.

## 3. Exact constants and strictness

For m≥1, B is nonincreasing in both m and k by the preceding pointwise kernel comparisons. The hardest cell is m=k=7. Direct evaluation of the analytic finite binomial identity gives:

- r=1,d=6,D=6: weighted summands 48,46,36,18,−8,−42,−84; sum 14, denominator 7, B=2.
- r=2,d=9,D=8: summands 432,368,252,108,−40,−168,−252,−268,−134; sum 298, denominator 45, B=298/45.
- r=3,d=10,D=8: summands 2160,1656,1008,378,−120,−420,−504,−402,−134; sum 3622, denominator 165, B=3622/165.

These are evaluations of a proved finite sum, not an enumeration of posets or a computer-assisted positivity certificate. All are positive, and e(C)>0 for every finite C. Thus 3K−N>0 strictly in every stated case, with no endpoint exclusion requiring a moment. The universal original K/N≤5/9 then supplies the other endpoint.

## 4. Original full degrees and automatic partial-signature case

A selected point is outside E because its signature contains x. In the exact lift u<x<c, and a,b<c. Its only possible outside-C incomparable labels are the missing roots in T. Therefore

    deg_(P+)(c)=deg_C(c)+3−|signature(c)|.

Actual Delta10 gives precisely the manuscript's degree cap. A non-full selected signature has at least one missing root, so each of two such labels has C-degree≤9; the second sufficient condition applies even when their signatures differ. The third condition permits any three selected x-frontier labels, full or partial, since their C-degrees are at most 10.

## 5. Real contracts and correction history

The chain-plus-isolated-full-label family is valid for every m≤k≤7 in the two- and three-point conditions. E is the initial m-segment of a k-chain of yz signature. A selected label has C-degree k+r−1. A chain point in E has full degree r+2, and one outside E has r+1. Root degrees are x:k+3, u:m+3, y=z:4, b:5, a:1. Thus all actual degree budgets hold, including empty E or empty missing chain. For r=1 the degree≤6 condition is realized for k≤6. It cannot hold for k=7: every C-minimum above x is incomparable with all k missing-x labels, since a predecessor would contradict C-minimality and a successor would be above x. This is correctly acknowledged, not a missing endpoint construction.

The initial source `0ab876d64d1368b116255452ddfa9c08b688926efe7b842c5e555ce6bdb9b07e` had an imprecise/incorrect full-degree description for the two x-only label example. I independently flagged it; the author concurrently corrected it. In the reviewed version, the exact degree list is correct: both C labels have C-degree 1 and full degree 3; x,u have 3; b has 5; y,z have 6; a has 1. Hence actual Delta is 6, and the example legally realizes the automatic non-full case. The correction changes no theorem or proof.

## 6. Scope

MF2 is an analytic extension of MF1 to a weaker selected-signature hypothesis, not a different population classification or a sharp necessary frontier condition. Patterns outside its sufficient conditions are not thereby counterexamples; individual cases may still be paid by m=0 or other mechanisms. The original pair (u,b) is fixed throughout. No new ordinary-population coverage, NB consequence, unrestricted B1 result, or computer-assisted dependency is established or needed. The canonical reviewed entry is the source named above, not the separate collaborative `X_MINIMAL_FRONTIER_EXTENSION.md`.
