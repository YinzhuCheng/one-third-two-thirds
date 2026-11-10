# Four equal-downset labels: a continuous analytic adjacent-inversion bank

2026-11-10. Internal independent review PASS in FOUR_EQUAL_DOWNSET_INDEPENDENT_REVIEW.md. Thirty net source rows are included in the current ledger. This analytically re-derives the four-minima part of Fathi Proposition24.4 and its already-stated identical-full-downset corollary in §24.4.1. Fathi §24.4.1 already explicitly states the identical-full-downset application. The new contribution here is a continuous analytic proof replacing his 74-vector count, not a new scope theorem, novelty claim, or extension of whole-D9 coverage.

## The original-P statement

Let x1,x2,x3,x4 be distinct labels of a finite original poset P with identical full strict downsets. They are therefore pairwise incomparable. Assume each has full incomparability degree at most nine. For ANY fixed physical reference order y1,y2,y3,y4 of these labels,

    Pr_P(y2<y1)+Pr_P(y3<y2)+Pr_P(y4<y3) > 1.       (F4)

In particular the four labels cannot have all their reverse-reference comparisons below 1/3. No exhaustion, exterior-size, NB inheritance, or special root structure is assumed.

## Fix the actual exterior word

Remove ONLY these four labels and fix an actual extension of the remaining original P. All four have the same predecessor set, so their common lower insertion boundary is immediately after the last such predecessor (or the word start). The first successor of each label gives its individual upper boundary. Every exterior label strictly between the common lower boundary and that first successor is incomparable with it. Three of its incomparable partners are already the other marked labels, so at most six exterior letters can occur there.

Shift the common lower gap to zero. Each label now has an integer upper gap d_i in [0,6]. Suffixes after all possible insertions contribute no choices. Each legal marked insertion has weight one; the original exterior word's mass is its actual number of such insertions, not a uniform mass assigned to the deadline vector.

For counting only, sort the labels by these d_i, breaking ties arbitrarily. Put L_i=d_i+i for i=1,2,3,4. Then 1<=L1, L_(i+1)>=L_i+1, and L4<=10. Inserting labels in this sorted order gives L_i equiprobable legal slots at step i. Hence the count is the product of the L_i, and the slot choices are independent uniforms in this representation.

## Pair formula and reference-order comparison

For sorted indices i<j, let q_ij be the conditional probability that label j precedes label i. Its position at its own insertion has mean (L_i+1)/2. Inserting an intermediate label k increases that expected position by a factor 1+1/L_k: conditional on its current position s, exactly s of the L_k insertion slots precede it. Therefore

    q_ij=(L_i+1)/(2L_j) product_(i<k<j)(1+1/L_k)
         =(1/2) product_(k=i..j-1) r_k,
    r_k=(L_k+1)/L_(k+1) in (0,1].                  (F5)

Later insertions do not change the relative order of i and j.

Introduce an AUXILIARY independent random cut at each of the three sorted-label boundaries, retaining that boundary uncut with probability r_k. This creates B consecutive blocks. Then q_ij is one half the probability i,j belong to the same block. For a fixed four-label reference, its adjacent-reversal sum is the expected following block score: 1/2 per adjacent pair in the same block, zero for a forward crossing between blocks, and one for a backward crossing.

For each particular partition, compress repeated consecutive block names in the reference, obtaining R runs, and let d be the number of downward steps between these runs. The score is (4-R)/2+d. Every one of the B blocks occurs, so R>=B. If d=0 the runs are strictly increasing, so R=B. If d>=1 and B>=2, then R-B<=4-B<=2<=2d. (When B=1 there is just one run.) Thus the score is always at least (4-B)/2, exactly the score of the sorted reference. Averaging over cuts proves that ANY physical reference has conditional adjacent sum at least

    q_12+q_23+q_34=(r1+r2+r3)/2.                  (F6)

The auxiliary partition is only a proof of this expectation inequality; it does not alter the original linear-extension law or select a bank after conditioning.

## Strict continuous lower bound

Write x=L2 and y=L3. Using L1+1>=2 and L4<=10,

    r1+r2+r3 >= 2/x+(x+1)/y+(y+1)/10.

Here 3<=y<=9 and x>0. The right side exceeds two exactly when

    10x^2+(y^2-19y+10)x+20y>0.

The leading coefficient is positive. Its negative discriminant is

    H(y)=800y-(y^2-19y+10)^2.

For y=7+t, 0<=t<=2,

    H=-t^4+10t^3+123t^2+60t+124>0,

since t^3(10-t)>=0. For y=7-s, 0<=s<=4,

    H=-s^4-10s^3+123s^2-60s+124
      >=67s^2-60s+124>0.

The last quadratic has negative discriminant 3600-4*67*124<0. Thus H>0 on the ENTIRE real interval [3,9], and the quadratic in x is positive on the entire real line. This proves the strict conditional sum >1 without enumerating integer caps, deadline orders, or coefficient tables.

Sum the strict count inequality over the actual exterior words to obtain (F4) with original-P probabilities. The physical reference events are fixed in advance; sorting is used only to derive a common lower bound for all references.

## Application scope

If four labels occur in an original marked ideal Q, their displayed predecessor sets are their full original predecessor sets. Hence four equal predecessor masks suffice to recognize this gate, without pivot memory. An independently checked source scan finds thirty unconditional rows of shape (0,0,1,1,7,7,7,7) among the 2,075 rows outside the single-frontier interface. The thirty rows have zero overlap with the preceding 404-row union. This gives 434 purely analytic source-bank replacements, with 3035 original banks unchanged.

## True degree-ten stopping control

Four minimal marked labels and a seven-label exterior chain, with upper gaps (0,2,5,7), give an actual original poset of maximum incomparability degree ten. Its sorted insertion-slot counts are (1,4,8,11). Independent forward subset DP and direct enumeration of all 352 full original words both give adjacent reversal counts (88,110,144). Thus the same three-event sum is 342/352=171/176<1, with signed count margin -10. The last adjacent pair has probability 144/352 in the balanced interval; this is not an NB counterexample. It only prevents extending this same degree-nine bank blindly to degree ten or changing the uniform upper-gap cap from six to seven. See FOUR_EQUAL_DOWNSET_D10_CONTROL.py/.json.

## Stronger parameter, separate addendum

FOUR_BANK_LAST_ONLY_DEGREE_INDEPENDENT_REVIEW.md proves that only the physical reference-LAST point needs degree<=9; the other three degree bounds may be dropped. That additional proof uses18 explicit structural path identities and is not a dependency of this original symmetric D9 proof or its30-row census. No additional row is counted.
