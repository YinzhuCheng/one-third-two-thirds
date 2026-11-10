# Reference-first predecessor-dominant four-label gate

2026-11-10. Internal independent theorem and mapping review PASS in DOMINANT_DOWNSET_FOUR_INDEPENDENT_REVIEW.md. A stopping-prefix lifting of the analytically re-proved four-minima bank. 123 net source rows are included in the live606 ledger.

## Exact original-P statement

Let x1,x2,x3,x4 be a fixed ordered antichain of four labels in a finite original poset P. Suppose

    D_P(xi) subset D_P(x1)=S,   i=2,3,4,

and each of the four labels has full incomparability degree at most nine. Then

    Pr_P(x2<x1)+Pr_P(x3<x2)+Pr_P(x4<x3)>1.           (DD4)

The labels and their reference order are fixed before any conditioning. The predecessor-dominant label must be FIRST in this reference. No condition is imposed on the size, order, or number of minima of the remaining original poset. In particular no pivot exhaustion or exterior-above-a condition is needed.

## Proof by an actual stopping prefix

In each original linear extension, stop at the first occurrence of either event:

1. one of the four marked labels appears;
2. all labels of S have appeared.

The empty S case stops immediately by event 2. Since the four marked labels form an antichain, none belongs to S. Consequently the two stopping events cannot first occur at the same letter.

If a marked label appears before S has been completed, it cannot be x1, since every member of S precedes x1. Thus that first marked label is xj for some j>=2. Its preceding reference label x_(j-1) has not appeared yet, because no marked label appeared earlier. The charged reversal xj<x_(j-1) therefore holds in every completion of this prefix. The three-indicator sum is at least one pointwise in this branch.

Otherwise S has completed and no marked label has appeared. Fix the entire literal stopping prefix. Its set I is an original ideal, contains S, and is disjoint from the four marks. Every D_P(xi) is contained in S, so all four marks have empty full predecessor sets in the actual induced remainder P minus I. Their incomparability degrees have not increased.

The original completions of this fixed literal prefix are in bijection with ALL linear extensions of P minus I. Hence the conditional suffix is exactly uniform on that remaining poset. Apply FOUR_EQUAL_DOWNSET_ANALYTIC.md to the same four physical labels in the same fixed reference: the three adjacent-reversal probabilities sum strictly above one. This is an unconditional counting theorem on the actual remainder; no NB property is assumed for the conditional law.

The second branch has positive original mass. Indeed S is an ideal disjoint from the marked antichain; any linear extension of S can be followed by an extension of its complement, producing a word whose first |S| letters are exactly S. For S empty this branch has full mass. Summing the weak pointwise inequality in the first branch and the strict inequalities in the positive-mass second branch, with the actual prefix completion counts, proves (DD4) strictly in original P.

## Structural recognition, predecessors, and locality

For four labels contained in an actual marked ideal Q, their predecessor masks in Q are their full original predecessor sets. To recognize the gate on a source reference, select four labels in their reference order and check that the first mask contains the other three, and that none of the selected labels belongs to that first mask. These tests also imply the four labels are an antichain: any comparability between selected labels would put one of them into a selected predecessor set, hence into the first mask.

The theorem itself has no predecessor-count bound. The source census additionally restricts the charged labels to at most eight full predecessors to preserve the M8 application. Its actual maximum is six.

## Relation to existing structures and literature

- Four identical full downsets satisfy the hypothesis in every reference order. The thirty-row four-equal-downset gate is therefore a special case, not an additive second application of this larger gate.
- Three labels with common downset S and a fourth y with D(y) subset S satisfy the gate whenever their reference puts a common-S label first. Equivalently y is not first, unless it too has downset S. The earlier THREE_EQUAL_DOWNSET_EARLY_LABEL_CENSUS is an intermediate subfamily, not an extra ledger contribution.
- In Fathi v22 Section24.4, pp.283–284, D(u)=D(v)=D(w)={a}, D(b)=empty. The three references ubvw, uvbw, uvwb satisfy this gate and yield the paper's three initial ordering banks on 978 profiles. This supplies an analytic replacement of that positivity step, not of the subsequent three-fork canonical-prefix tree. It is outside the separate 3,469-occurrence two-fork ledger.

The base four-minima/equal-downset structural fact is already explicitly in Fathi; its former positivity calculation used Proposition24.4's 74 profiles. The continuous proof supplied locally removes that finite step. The stopping-prefix argument above is an additional structural lifting mechanism. No claim of literature originality or new whole-D9 coverage is made.

## Independently audited full-packet census

REFERENCE_FIRST_DOWNSET_DOMINANT_FOUR_CENSUS.py/.json independently reconstructs the source packet against the current 483-row union and finds:

    applicable155; overlap483=32; net new123;
    prospective union606; remaining3469-606=2863.

Every new row is unconditional (mode0): phase0 has116, phase2 has4, phase4 has2, phase6 has1. The charged endpoint predecessor count is at most six. This includes, and must not be added to, the intermediate three-equal-downset gate's net64 rows. The theorem and every source key have independent approval; the live ledger records606 analytic replacements and2863 original banks unchanged.

## A reference-conditioned cardinality consequence

Under original NB in a degree-nine poset, let T be its strict two-thirds reference order. For any x define

    Y_x={y: x precedes y in T, y incomparable with x, D(y) subset D(x)}.

The set Y_x has at most two elements. First, Y_x is automatically an antichain: if y<z both belonged to Y_x, then y belongs to D(z) subset D(x), contradicting y incomparable with x. If there were three members, put them after x in their T order. DD4 applies and contradicts the three strict reverse-reference probabilities being below1/3. Thus both width(Y_x)<=2 and |Y_x|<=2 hold. It is a structural consequence of the same gate and adds no ledger occurrence by itself. No claim is made that this test eliminates a complete pivot phase or any of the source's mode-two switches.

## Independently audited asymmetric degree strengthening

FOUR_BANK_LAST_ONLY_DEGREE_INDEPENDENT_REVIEW.md strengthens the degree contract: only the reference-LAST label x4 needs full incomparability degree at most9; x1,x2,x3 may have arbitrary finite degrees. The reference-FIRST label x1 remains the predecessor-dominant label. The proof has18 explicit structural path decompositions and the already reviewed continuous base bound, followed by the same true-prefix lifting. This changes no D9 source count and does not prove full D10.
