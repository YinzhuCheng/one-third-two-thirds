# Three initial fork labels: analytic replacement of the 978-profile ordering step

2026-11-10. Candidate corollary of the independently reviewed four-equal-downset bank. Separate from the seven-phase two-fork packet and its current replacement ledger; no numerical increment is claimed here.

## Original-P contract

Let a,b be the only minimal elements of an original finite poset P. Let u,v,w be three distinct labels with full strict predecessor sets all equal to {a}, and suppose b is incomparable with u,v,w. Assume each of b,u,v,w has full incomparability degree at most nine. This is satisfied in Fathi v22 Section24.4, pp.283–284, at the start of the three-minimum branch. In that application every exterior label is above a; the proof below only needs that a,b are the only minima.

Fix any physical reference order of {b,u,v,w} in which b is not first. If its successive labels are y1,y2,y3,y4, then

    Pr_P(y2<y1)+Pr_P(y3<y2)+Pr_P(y4<y3)>1.         (TF)

Consequently, once u,v,w are named in their strict two-thirds reference order, the three relevant inequalities are

    Pr(b<u)+Pr(v<b)+Pr(w<v)>1,
    Pr(v<u)+Pr(b<v)+Pr(w<b)>1,
    Pr(v<u)+Pr(w<v)+Pr(b<w)>1.

These are the same three banks Fathi establishes by counting 978 profiles, with weak >=1 in the paper. They exclude every placement of b after u in that reference.

## Proof by the actual first letter

The first letter of an original extension is either a or b. Partition the original extensions into these two disjoint, actual cells.

In the b-first cell, let yj=b with j>=2 in the fixed reference. Its preceding reference label y_(j-1) is one of u,v,w, so the charged reversal b<y_(j-1) holds with probability one. The other two charged indicators are nonnegative. The sum of indicators is therefore at least one in every word of this cell.

In the a-first cell, deleting that first a is a bijection onto ALL linear extensions of the actual induced poset P minus {a}. Conversely every extension of P minus {a} can be prefixed by the minimal a. Thus the conditional remaining-word law is exactly uniform, not an artificially chosen deletion distribution.

In P minus {a}, the four physical labels b,u,v,w have identical empty full predecessor sets. Deletion does not increase their incomparability degrees. Apply FOUR_EQUAL_DOWNSET_ANALYTIC.md in that actual remaining poset, to the SAME fixed physical reference. Its three adjacent-reversal probabilities have sum strictly greater than one. This application needs no NB hypothesis on the conditioned law; it is a direct unconditional counting inequality.

Both a and b are minimal, so the a-first cell is nonempty. Summing the strict a-first count inequality and the weak b-first pointwise inequality with their actual cell sizes proves (TF) strictly in original P. No profile-dependent events or weights are chosen.

## Attribution and limits

This is an analytic proof compression of Fathi's already used initial ordering conclusion in the three-fork branch, using the newly supplied continuous proof of the earlier four-minima/equal-downset bank. It does not claim a new balanced-poset class. It removes the need for the three initial profile-bank verifications on that 978-profile domain, but does not replace the subsequent 174-word three-fork canonical-prefix tree or its 1,820,185 integer inequalities. It also is not one of the 3,469 occurrences in the separate two-fork seven-phase packet, so it must not be added to that ledger.

The proof requires the actual only-two-minima condition, not merely that a,b happen to be the only marked minima. It does not infer NB after deleting a. If other original minima may occur first, this two-cell proof does not cover those cells without an additional argument.

## Later unification

REFERENCE_FIRST_DOWNSET_DOMINANT_FOUR_GATE.md gives a stronger stopping-prefix proof covering this corollary without the only-two-minima restriction. The present first-letter proof remains valid under its stated contract, but is no longer the main reusable mechanism. Neither this auxiliary three-fork application nor the intermediate three-equal-downset map is an additional count beyond that generalized gate's properly de-duplicated source rows.
