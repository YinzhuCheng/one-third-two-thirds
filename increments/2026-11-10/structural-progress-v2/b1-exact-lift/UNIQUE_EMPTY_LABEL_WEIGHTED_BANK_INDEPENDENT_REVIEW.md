# WB4 independent mathematical review

2026-11-10 UTC. **PASS after the explicit lower-bound correction m>=1.** This is a non-blind internal mathematical review by a reviewer not participating in the derivation. It is not external peer review, formal verification, or an originality certificate.

Reviewed final source: `UNIQUE_EMPTY_LABEL_WEIGHTED_BANK.md`, SHA256 `69e027605aee876424b5aaf290a55d17c3d02c58c15cae8f394ef8f5500ae132`.

## Conclusion and correction record

The stated fixed original physical bank inequality is correct under the full displayed contract, notably **1<=m<=4** and **f is the only empty-signature label in all C**:

    4K_u+K_y+K_z-2N >= e(C)>0.

It gives ordinary strict balance for some member of the one fixed (4,1,1) bank on (u,b),(y,b),(z,b), using the accepted individual upper bounds. It does not close an entire remaining parameter cell.

The initial version `347822cc146633e65dc33b78aaa4e796ac1d74f40f00c4e1921de7b2a189e0bd` wrote only m<=4, permitting m=0,C={f}. Then gamma was empty and the proof's first-letter case split was undefined. The reviewer flagged this boundary. The author corrected the contract to 1<=m<=4, which leaves all intended m3/m4 residual applications intact. No mathematical counterexample to the payment target was found. The corrected version is what this PASS covers.

## 1. Exact kernel and literal deletion fibers

Adding the previously reviewed original F and G kernels independently yields

    F+G=76+(12-10Q)H+8(Y+Z)+5Q(Q-1)-y_beta-2a_beta.

In particular the X term cancels and the Y-prefix term does not: replacing the latter by zero would be an invalid shortcut, but the source retains it exactly.

Since f is an actual C-minimum, each true gamma in LE(C-f) has legal insertion gaps 0..d. Original Delta10 and f's three incomparable old roots imply d<=7. Deleting the missing-x point f leaves at most k-1<=6 missing-x labels, so h<=6. The original E initial run satisfies q<=min(m,h), but need not equal h. The source correctly keeps this distinction. Because m>=1, C-f is nonempty.

## 2. E-start fibers: valid monotone relaxation, arbitrary actual deadlines

For q>=1, inserting f first gives runs (h+1,1,1), and the exact positive-gap count gives A0_beta=A1_beta=2h+6. Later insertion leaves an E first label and therefore A0_beta=A1_beta=0. I recovered the source's T0 and Tj formulas from the original kernels.

For fixed H, increasing Q by one changes T by 10(Q-H). All replacements used remain in Q<=H, so increasing q gives a lower bound. Thus q may first be increased to min(4,h). For h<=5, increasing further to h is also a valid algebraic lower relaxation, even where h exceeds the actual m. No realizability of the enlarged q is asserted or needed.

For the relaxed q=h, the increments on gaps 1..h decrease with j; hence partial sums are concave over d=0..h and take their minimum at an endpoint. Later increments are constant, so the complete minimum over d=0..7 is attained among 0,h,7. This argument needs no unproved bound d>=h. The three displayed endpoint expressions are correct. For h<=4, their minimum is at least94 using the stated concavity bounds; for h=5 the endpoint totals are118,158,130, also above94.

At h=6, using q=4 yields exactly

    (T0,T1,...,T7)=(124,90,30,-20,-60,-60,-60,-32).

The first increments are positive and all increments after gap2 are negative, so the smallest prefix sum is at gap0 or gap7. The final sum is12. This direct evaluation of the seven explicit polynomial terms is a hand-checkable analytic endpoint calculation, not a computer-assisted positivity certificate. All E-start actual fibers therefore have total at least12 and size at most8.

## 3. Non-E-start fibers: the signature assumption is used precisely

Let c be the first gamma label. If c was already C-minimal, the unique-low-minimum and zero-x-frontier hypotheses force its signature to be yz. It is not in E by this case's premise. Every later f gap then leaves Q=0,Y=Z=0 and A0=A1=0, giving T=76+12H>=76.

If c was not C-minimal, its only possible C-predecessor is f, so f<c and d=0. The global unique-empty-label assumption ensures that c is nonempty even in this second branch. Thus the f-first beta has H,Y,Z>=1 and at least one run equal to1. This is the exact point where the stronger hypothesis, not merely uniqueness of the empty C-minimum, is necessary.

The previously reviewed literal root-gap identity applies and gives A0_beta=A1_beta. If H=1, substitution gives

    82+5(Y+Z)-2YZ-2min(Y,Z)>=58

under Y,Z<=6. If Y=1, independent substitution gives

    79+9H+6Z-3HZ-3min(H,Z).

Using min(H,Z)<=6 leaves the bilinear lower bound 61+9H+(6-3H)Z on [1,7]x[1,6]. Its four corner values are exactly73,88,109,34, proving the lower bound34. The Z=1 case is symmetric. These are full-original-root caps, not probability bounds imported from a smaller object.

Hence every non-E-start fiber contributes at least34 first and at least76 for each later legal gap. It exceeds its actual number of C words.

## 4. True-law summation and exact ledger effect

All fibers partition LE(C), each retaining the actual gamma order and all completion multiplicities. Each fiber contributes at least its actual cardinality, so summation proves the claimed e(C) margin. The same whole-object bank is used everywhere; the proof does not choose different pairs for different fibers, impose a conditional OLD moment, or double-use prefix credit.

The ledger statement is accurate. In m3k7 and m4k6 the accepted residual already has a unique low C-minimum f; if it remains unpaid after WB4, it must contain another empty-signature label. Every predecessor of such an empty label also has empty signature, so in a finite C its minimal ancestor must be the unique empty minimum f. Thus that extra label is genuinely above f. In m4k7 either another low C-minimum remains or the same nonminimal-empty obstruction is necessary. WB4 makes no claim for m5k7.

Consequently the parameter ledger remains the same four cells. This result narrows their necessary structure but does not establish nonemptiness, prime/all-history novelty, a universal fixed-u/b guarantee, or full B1/D10 payment. No object search, CURRENT_ADVANCE edit, or computational certificate was used in this review.
