# Independent review: predecessor rank-gap insertion bound

2026-11-10. PASS for the lemma and the two new mapped source occurrences. No ledger or external repository was changed.

## Statement and proof audit

Let P be any finite poset and x,y incomparable. Write D(x),U(x) for strict down/upsets, and let d be the full incomparable degree of x. Assume D(x) is contained in D(y). If D(x) is nonempty, set

    r = min over a in max D(x) of |{z : a<z<y}|.

If D(x) is empty, set r=|D(y)|. Then the uniform original-P extension law satisfies

    Pr(x before y) >= (r+1)/(d+1).

Fix a literal extension w of P minus x. All extensions restricting to w arise by inserting x in the consecutive slots after its last predecessor and before its first successor, with absent boundaries replaced by the start/end. If there are n legal slots, n<=d+1: every letter strictly between those boundaries is incomparable with x. Given w, these n insertions are equiprobable.

If y is before the first successor, it is after the last predecessor because D(x) is contained in D(y). For nonempty D(x), that last predecessor a is maximal in D(x). All at least r labels strictly between a and y in P occur after a and before y in w. Thus at least r+1 legal slots precede y. If D(x) is empty, all |D(y)| predecessors of y precede y in w, again giving at least r+1 slots. Consequently the conditional probability is at least (r+1)/n >= (r+1)/(d+1).

If y is after the first successor, all legal slots precede y and the conditional probability is one. To verify that this also dominates the claimed bound, observe that every z with a<z<y for maximal a in D(x) is incomparable with x: z<x contradicts maximality of a, whereas x<z implies x<y. Together with y these give r+1<=d. In the empty-downset case all predecessors of y are likewise incomparable with x, so the same inequality holds. Thus no hidden bound greater than one occurs.

Finally the deletion word w is NOT sampled uniformly: its actual probability is n(w)/sum_w n(w). Since the bound holds for every conditional insertion law, averaging with exactly these weights proves the original-P result. No NB, ideality, degree-nine or helper-law assumption is needed for this lemma itself. It is a non-strict lower bound, not by itself a two-sided balanced-pair theorem.

## Ideal/memory application

When Q is an actual original ideal containing x,y, their full downsets are exactly their Q downsets. Hence r is fully determined inside Q. If every exterior element lies above x, the full incomparable degree equals its internal degree. In the source tree this is justified for an exhausted memory/current-terminal pivot and its predecessors, not merely by a conditioned deadline zero. Otherwise the full degree-nine bound can be used. Endpoint predecessor counts remain explicitly checked at most eight.

A reverse-T event with probability at least one third contradicts the corresponding strict-T candidate. This uses the original reference orientation, not an assumed orientation on deletion fibres.

## Independent source census

RANK_GAP_INDEPENDENT_CHECK.py independently loops over all 3,469 non-switch packet occurrences using order comparisons, reconstructs each eligible pair and its maximal predecessors, and compares the complete eligible key set with RANK_GAP_REPLACEMENTS.json. Source SHA256:

    31d4fd6c3c8b9f02ade216df030037978b8a71af3021be423246aa02c7a52fa1

Result: 11 eligible source occurrences, 9 already covered, exactly 2 new relative to the 400 earlier analytic rows plus the 2 now-reviewed Q8 rows. This is metadata bookkeeping for a uniform lemma, not a probability-profile positivity certificate.

Both new occurrences have phase 0, terminal mode 1, predecessor masks

    (0,0,1,1,7,23,23),

and words 0124356 and 0124365. Take x=3=v and y=4. Then D(x)={0}, max D(x)={0}, D(y)={0,1,2}, and the sole intervening label above 0 and below 4 is 2. Thus r=1. Terminal exhaustion of v makes its full incomparable degree exactly five. The bound is 2/6=1/3. The original bank [[4,1]] is independently decoded: pair index 4 is (4,3), both words put 4 before 3, so its reverse event is exactly 3 before 4. No different bank or source orientation was silently substituted. The endpoint predecessor counts are one and three, within the M8 limit.

Adoption therefore adds exactly two to the reviewed 402 pure analytic rows, giving 404 and leaving 3,065 original banks unchanged. This review does not alter structural phase coverage, establish the whole D9 theorem analytically, or claim novelty of deletion/insertion counting. Main ledger update is left to the parent after adoption.
