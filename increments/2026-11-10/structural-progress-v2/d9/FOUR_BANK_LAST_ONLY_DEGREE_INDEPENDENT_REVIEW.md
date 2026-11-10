# Independent parameter audit: only the reference-last degree is needed

2026-11-10. **PASS**. This supersedes the weaker first-degree-free parameter observation. No D9 ledger increment is implied.

## Exact strengthened statements

For four distinct labels with equal FULL strict downsets in a finite original poset, fix a physical reference x1,x2,x3,x4. If ONLY x4 has full incomparable degree at most nine, then

    Pr(x2 before x1)+Pr(x3 before x2)+Pr(x4 before x3)>1.

There are no degree bounds on x1,x2,x3. The same conclusion holds for the dominant-downset gate: the four marks form an antichain and D(xi) is contained in D(x1) for i=2,3,4, again requiring only the reference-LAST label's degree at most nine. The first label is still the predecessor-dominant label; the last label is the degree-bounded label. These two roles must not be confused.

## Exact pair law and full path audit

In the equal-downset case, fix an actual exterior word, shift past the last common predecessor, and sort the four finite upper gaps h1<=h2<=h3<=h4. These sorted indices are counting names only. The physical reference is an arbitrary permutation of them. Write

    a=(h1+2)/(h2+2), b=(h2+3)/(h3+3), c=(h3+4)/(h4+4).

The already independently derived insertion formula remains valid without cap-six bounds on all labels: 0<a,b,c<=1, and for sorted i<j the probability j precedes i is half the product of the intervening a,b,c. Exact conditional insertion weights remain uniform; actual exterior words need not be equally likely.

Let C(w) be the physical adjacent-reversal sum for a permutation w of sorted indices. The following table displays exact expressions for 2(C(w)-1). I independently generated all eighteen expressions directly from the pair formula and algebraically checked their expansions. Every listed decomposition is strictly positive for 0<a,b,c<=1, except the explicitly separated first row ending at 3.

| Physical reference w | Exact expression for 2(C(w)-1) |
|---|---|
|2341|b(1-ac)+c|
|2431|(1-ab)+(1-c)+bc|
|3241|(2-b)+bc(1-a)|
|3421|(2-a)+c(1-b)|
|4231|(2-ab)+b(1-c)|
|4321|4-a-b-c|
|1342|ab+c(1-b)|
|1432|(1-b)+(1-c)+abc|
|3142|(2-b)+b(1-a)(1-c)|
|3412|a+c(1-ab)|
|4132|(2-b)+ab(1-c)|
|4312|(2-c)+a(1-b)|
|1243|a-c(1-b)|
|1423|b(1-c)+abc|
|2143|(1-a)+(1-c)+abc|
|2413|ab+bc(1-a)|
|4123|a+b(1-ac)|
|4213|(1-a)+(1-bc)+ab|

Thus when the physical LAST label has sorted rank 1 or 2, all six possible paths are strictly above one with no cap bound at all. This includes 1432, where strictness comes from abc>0 even if b=c=1.

When that label has sorted rank 3, its degree-nine hypothesis gives h3<=6 (three of its incomparable partners are the other marks). Hence

    a+b-1 >= 2/(h2+2)+(h2+3)/9-1
           = ((h2-2)^2+2)/(9(h2+2)) > 0.

For the sole exceptional path 1243, a-c(1-b)>=a+b-1>0 since c<=1. The other five paths already have the explicit strict decompositions above. This argument is continuous in h2 and does not enumerate integer profiles.

When the physical LAST label has sorted rank 4, its cap is at most six and hence all four caps are at most six. The already independently reviewed continuous four-label base proof applies to every physical reference. These four sorted-last-rank cases exhaust every reference, including tied caps under arbitrary fixed tie breaking.

Consequently every actual exterior-word fibre has strict bank sum above one. Summing the unnormalized strict margins with the true completion counts proves the original-P statement. Finite upper gaps ensure a,b,c>0; no uniform positive slack independent of the other degrees is asserted.

## Dominant-downset lift

The stopping-prefix proof is unchanged. Stop at the first marked label or completion of S=D(x1). In a marked-first cell, that mark cannot be x1 and its preceding reference neighbor is still absent, forcing one charged adjacent reversal to equal one. In an S-first cell, all four marks are remaining minima; the fixed-prefix suffix law is uniform over the actual remaining poset. The reference-last mark still has incomparable degree at most nine, since deletion cannot increase it. Apply the strengthened equal-downset base result above, without imposing any degree bound on the other three marks.

An S-first cell has positive original mass because S is an ideal disjoint from the marks; if S is empty the branch occurs immediately. Actual prefix-count averaging is therefore strict. No conditional NB inheritance or adaptive choice of reference is used.

## Scope and limitations

This is stronger than requiring degree nine for the last three labels. In an ambient degree-ten poset it is enough that the chosen dominant-first reference ends at a label of degree at most nine. It is not a theorem for four unrestricted degree-ten labels or a whole-D10 balanced-pair theorem.

The existing actual cap-seven control (0,1,3,7), with sorted physical reference, has last degree ten and bank 65/66<1. It remains a valid stopping line for relaxing the last-label bound, while already containing balanced pairs. It is not NB and does not contradict the present theorem.

The already reviewed D9 source rows satisfy the stronger hypothesis automatically. No ledger count changes, no new structural phase closure is claimed, and no external destination was modified.
