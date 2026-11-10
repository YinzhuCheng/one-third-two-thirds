# DG2: two actual low minima, one empty, pay the original fixed pair throughout exact D10

2026-11-10 UTC. Analytic author candidate, fresh uninvolved independent review requested. Original exact-lift contract only. No no original-poset scan, no computer-assisted positivity certificate. Small root-gap diagnostics suggested this proof; they are not dependencies.

## Theorem

In any actual exact-D10 lift, suppose C has two DISTINCT actual C-minima f,g, both missing x and of old T-support at most1, with f empty. Thus g is empty or singleton y/z. Then, with the original exact counts N=e(P+),K=#(u<b),

    3K-N >=3e(C)>0.                              (DG2)

The inherited upper bound K/N<=5/9 gives strict balance of the one ORIGINAL fixed pair (u,b). All other C relations, additional minima, E, and tail weights remain arbitrary subject to the original contract. No OLD moment is needed.

## 1. True two-slot fibers and the model prefix kernel

Delete only f,g and fix a genuine gamma in LE(C-{f,g}). Write h=h_x(gamma)<=k-2<=5 and q=q(gamma)<=h. If q0, every reinsertion beta also has Q0; the complete original fixed-pair kernel F_beta from WB5/WB6 is at least48. These fibers are automatically more than sufficient. The empty gamma is included in this q0 case.

Assume q>=1, so gamma starts in E. Both actual C-minima f,g are incomparable with every E point: an E predecessor would contradict their minimality; placing f or g below E contradicts the given E-ideal. Therefore their gamma deadlines A,B are at least1. The original C-degree caps are7 at f and at most8 at g. They are mutually incomparable, so after deleting the other minimum,

    1<=A<=6, 1<=B<=7.

Their full true fiber consists of all gap pairs (a,b) in [0,A]x[0,B], with one original word off the diagonal and TWO words on the diagonal. The two minima have no relation; before their first respective successors these are exactly all legal placements. Thus the true fiber size is

    W=(A+1)(B+1)+min(A,B)+1 <=63.                (1)

For the original beta the missing-x run is H=h+1_(a<=h)+1_(b<=h), while Q=min(q,a,b). The complete original F kernel is

    F=48+(6-8Q)H+4Q(Q-1)+9(Y+Z)+2x_beta+y_beta.

For fixed H it decreases as Q is raised: F(Q+1)-F(Q)=8(Q-H)<=0 when the other variables are fixed. Replace q by h for a lower bound, keeping the SAME actual gap pairs and multiplicities.

By y/z symmetry suppose g has singleton y signature. If g is actually empty, the following singleton model is still a pointwise LOWER bound: it only reduces the initial missing-y run, while leaving H,Q unchanged, and F is increasing in Y,Z including its exact prefix terms. No replacement poset or conditional law is asserted.

Let the base kernel be

    B_j(H)=48+(6-8j)H+4j(j-1),  j=min(h,a,b).

The exact extra over this base in the singleton model is:

- a=b=0, order f,g: 36+3(h+2);
- a=b=0, order g,f: 20+2(h+2);
- a=0,b>0: 26+2h+2*1_(b<=h);
- b=0,a>0: h+11+1_(a<=h);
- a,b>0:0.

For example f,g first gives (Y,Z)=(1,2), and g,f first gives (0,2); the old exact root-prefix counts x_beta=YZ+min(Y,Z), y_beta=H(Y+Z)+min(H,Y)+min(H,Z) yield the listed extras. All diagonal multiplicities are true original word multiplicities.

Write T_h(A,B) for the sum of this lower model over the full actual gap rectangle, diagonal counted twice. We prove T_h(A,B)>=204 for all integer1<=h<=5,1<=A<=6,1<=B<=7. With (1), this gives T_h(A,B)>=3W, proving DG2 after summing true gamma fibers.

## 2. Rectangle reduction: thin edge, small diagonal, or both deadlines >=h

For 0<=j<h and H>=h+1,

    B_(j+1)(H)-B_j(H)=8(j-H)<0.                (2)

Fix B and vary A within1..h. Up to A=min(B,h), each new-row increment is nonincreasing: every base entry either has fixed minimum b or increases its minimum a, and (2) lowers it; its diagonal duplicate also decreases. The b0 prefix extra is constant throughout a<=h. Consequently the total is concave on that interval and its minimum is at an endpoint. If B<h, after A=B and up to h, every new row is identical (no diagonal duplicate), so the total is linear there. Thus a minimum with A<=h reduces to A=1, A=B<=h, or A=h.

At A=h and B<h the same column argument reduces B to1 orh. At A>h,B<h, all rows after h are identical (no diagonal duplicate and all b<h), so varying A on[h,6] is linear, reducing to A=h or6. At A6 and B<h the column increments decrease, reducing B to1 orh. The symmetric cases are covered likewise.

Therefore the global minimum on the full rectangle of deadlines is attained in at least one of:

    min(A,B)=1; A=B=t<=h; or A,B>=h.            (3)

This reduction does not normalize or reweight a gamma fiber; it proves a scalar lower bound for every actual deadline pair.

## 3. Thin edge

If min(A,B)=1, then j<=1 in every model word and H<=h+2<=7. Hence B_j(H)>=48-2H>=34, and every extra is nonnegative. There are W>=6 words, so

    T_h(A,B)>=34W>=204.                        (4)

## 4. Small diagonal A=B=t<=h

All insertions are before the first gamma x-successor, so H=h+2 throughout. For minimum gap j there are exactly2(t-j+1) words (including the diagonal extra). Summing base and the listed prefix extras gives

    D(t,h)=[-8ht^3-6ht^2+47ht+51h
              +2t^4-12t^3+130t^2+624t+558]/3.   (5)

For t1 the coefficient of h is28, so h>=t gives D>=462. For t2 it is19, giving D>=792. For3<=t<=5 the coefficient of h is negative: its numerator -8t^3-6t^2+47t+51 is negative at3 and strictly decreasing thereafter. Thus use h5. The resulting quartic is

    R(t)=(2t^4-52t^3+100t^2+859t+813)/3.

It is concave on[3,5], since R''=8t^2-104t+200/3<0 there. Its endpoint values are1016 and786. Therefore every small-diagonal value is at least462>204.

## 5. Both deadlines >=h

Put d=A-h, e=B-h. The base sum over the h-by-h corner is

    B00(h)=2(h+1)(h+2)(30-h^2),

because the minimum j occurs with multiplicity2(h-j+1). Every new row or column outside that corner has base sum

    S(h)=-2(h+1)(4h^2-h-81)/3.

A cell with both gaps >h has base

    C(h)=48+2h-4h^2.

The total prefix extra is B(26+2h)+A(h+11)+66+8h. Thus the exact model sum is

    T_h(A,B)=P(h)+d[S(h)+h+11]+e[S(h)+2h+26]
                    +[de+min(d,e)]C(h),        (6)
    P(h)=-2h^4-6h^3+59h^2+225h+186.

For1<=h<=3, S(h)>0 and C(h)>0, so every extra contribution in (6) is nonnegative. Also P is B00 plus positive prefix extras, and B00>=2*2*3*(30-9)=252. Hence T>=252.

At h4, P=1134,S=70,C=-8, and 0<=d<=2,0<=e<=3. Raising d by1 changes (6) by at least85-8(3+1)=53>0; raising e by1 changes it by at least104-8(2+1)=80>0. Hence T>=1134.

At h5, P=786,S=-56,C=-42,0<=d<=1,0<=e<=2. Both coordinate increments are strictly negative. The minimum is at(d,e)=(1,2), where

    T>=786-40-40-3*42=580.

This completes the uniform T>=204 proof.

## 6. True-law sum and exact scope

Every q0 gamma fiber has F>=48 per original beta. Every q>=1 gamma fiber has original total at least T_h(A,B)>=204>=3W. Their deletion fibers partition LE(C) exactly, so 3K-N=sum_beta F_beta>=3e(C)>0. Prefix credit and diagonal multiplicity were used once, with no changed tail weights or conditional OLD moment.

In the current necessary residual list, the only two parameter cells are m4k7 and m5k7. UL1 has already independently closed their unique-low-C-minimum branches. The existing classification leaves at most two low C-minima, including an empty one; thus DG2 would close all their remaining two-low-minimum patterns. Combined with the earlier ordinary closures, this would prove ordinary balanced-pair existence for EVERY actual exact-D10 lift of the stated T3 private-predecessor construction, without OLD moment. It is NOT all B1, arbitrary T4, or a theorem about all degree-ten posets; the exact E-ideal/signature/lift contract remains essential. The final composition needs its own independent quantifier audit before that summary is adopted.
