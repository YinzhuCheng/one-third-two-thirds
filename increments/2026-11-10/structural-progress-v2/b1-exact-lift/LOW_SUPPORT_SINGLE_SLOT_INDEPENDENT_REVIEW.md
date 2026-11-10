# FH1 independent mathematical review

Date: 2026-11-10 UTC. Reviewer: audit_alpha2_four, not involved in FH1 derivation.

**PASS.** Source `LOW_SUPPORT_SINGLE_SLOT_FIRST_HIT_GATE.md`, SHA256 `1d8e91425459d99fedad5e9589620022f543565bc67e2df8b4999212222f2964`, independently verified. Fixed-pair margins46/9 and38/9 hold in the respective typed domains without OLD moment. The larger ordinary domains use the separately reviewed RC1 alternative rather than asserting universal fixed-u/b payment.

## Original single-label insertion

The support<=1 missing-x C-minimum f is outside E and above u. Its missing T-root neighbors number at least2, giving original C-degree<=8. Each retained gamma label before the first successor of f is incomparable with f because f is minimal. Legal positions are precisely the consecutive gaps0,...,d with d<=8. There is one actual word for each gap, and each original word has a unique gamma/gap decomposition.

Gamma has at most k-1 missing-x points, so h<=6. If f is placed at or before the gap after its initial h missing-x labels, it lengthens that initial run by one; otherwise it does not. Thus H_j=h+1_(j<=h), including the no-successor case, is exact. Since f is not in E, insertion truncates the E-prefix to min(q,j), also exactly. Removing9(hy+hz)>=0 gives the asserted b_j lower bound. Actual gamma fibers are uniform in their own gap labels and have cardinality d+1, but different fibers need not have equal weights.

## Prefix minimum argument

For q0, b_j=48+6H_j>=48. For q>=1, the pre-jump sequence through h is nonincreasing: H is fixed at h+1, and increasing Q changes the kernel by8(Q-H)<=0. Beyond q it is constant until h. At j=h+1, H drops by one while Q stays q, causing an upward jump8q-6>0. Every subsequent term equals the same constant. A mean of prefixes of a nonincreasing sequence decreases up to h. After h it is (S_h+tL)/(h+1+t), whose successive differences have constant sign. Thus its minimum over all d0,...,8 is at h or8. Here h<=6, so both indices are in the comparison interval. If gamma is too short for a gap8, the artificial continuation is merely a numerical lower-envelope comparison and is not counted as an actual word; minimizing over this larger interval remains valid.

For fixed h and j, Q=min(q,j)<=H_j. Increasing q therefore weakens b_j, using the same forward difference. The endpoint comparisons may consequently relax to q2 in A whenever h>=2, even if actual m1, and to q=h in B even if actual m<h. These are lower bounds, not new realizability assertions or equal weighting over run profiles.

## Independent polynomial checks

For h1,q1, the terms through h are60,44, totaling104; the seven later terms are46, giving426 through8. For h>=2,q2, the first terms are54+6h,46-2h, followed by h-1 copies of46-10h through h. Their sum is54+60h-10h^2. Later terms are56-10h, so the sum through8 is502-76h. On2<=h<=6 the first sum is concave and at least54; division by h+1<=7 yields at least54/7>46/9. The second sum is at least46. The stated A bound follows, with h0 and m0 stronger separately.

For q=h, summing the terms48+(6-8j)(h+1)+4j(j-1), j0,...,h, gives (h+1)[54+(2/3)h-(8/3)h^2]. Its mean is at least14 for h0,...,4 by concavity. Each subsequent term is48+2h-4h^2. Adding8-h such terms gives438+(68/3)h-36h^2+(4/3)h^3. Its second derivative is-72+8h<0 on[0,4], and its smaller endpoint value is38 at h4. This proves the B bound38/9. These are direct closed-form sums; no numerical positivity table or object enumeration is needed.

## Summation and RC1 alternative

Apply the corresponding uniform mean bound to each actual gamma fiber, multiply by its actual d+1 words, and sum. The exact margin identity gives the two fixed-pair claims and the inherited5/9 cap gives strict balance. No moment is assumed locally or globally.

If no missing-x support<=1 C-minimum exists and Mx is nonempty, every minimum of the ideal Mx is a C-minimum and must have signature yz. Every Mx point lies above one such minimum, so it also has signature yz. This verifies exactly the stated root-cover hypothesis for RC1. Empty Mx is covered by m0. Hence the union m<=2 or k<=5 is ordinary-paid, although the RC1-only branch need not use fixed u/b.

No mathematical gap found. The theorem does not assume an x-containing C-minimum or uniqueness of f, and does not address the remaining cells or interpret negative relaxations as counterexamples. No new ordinary-population novelty, NB, or full-B1 conclusion is asserted. This is an internal independent audit, not external peer review or formal verification. No original-poset search, LE DP, moment transfer, or external modification was used.
