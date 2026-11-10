# WB4: a unique empty label removes the m<=4 zero-frontier obstruction

2026-11-10 UTC. Analytic author candidate, independent review requested. This is a conditional ordinary payment theorem, not a closure of all remaining cells.

## Exact original contract

Use the complete original exact-D10 lift and kernels of WB5/WB6. Assume 1<=m<=4, k<=7, zero x-frontier, exactly one low C-minimum f, and its old T-signature is empty. Strengthen this last premise explicitly: **f is the only empty-signature label anywhere in C**, not merely the only empty C-minimum. All other C-minima consequently have signature yz. Let N,K_u,K_y,K_z have their full-original meanings.

The author claim is

    4K_u+K_y+K_z-2N >= e(C)>0.                 (WB4)

It uses the one fixed physical bank (ub,yb,zb) with weights (4,1,1)/6. Candidate-wise upper bounds supply a strictly balanced member. No OLD moment, free completion weights, object search, finite positivity certificate, or word-dependent pair choice is used.

## 1. Keep the exact old-prefix kernels

Use precisely F_beta and G_beta in ZERO_FRONTIER_M6_WEIGHTED_ROOT_BANK.md §3; their original sums are 3K_u-N and K_u+K_y+K_z-N. For runs H,Y,Z and Q=q(beta),

    F_beta+G_beta
      =76+(12-10Q)H+8(Y+Z)+5Q(Q-1)
          -y_beta-2a_beta,                   (1)

where y_beta=HZ+min(H,Z)+HY+min(H,Y), and a_beta is the original A0 count. This follows directly by cancelling the exact X terms, not by discarding prefix credit. Its sum is 4K_u+K_y+K_z-2N.

Delete only f, fixing a genuine gamma in LE(C-f), and let d be its actual f-gap deadline. Since f is a C-minimum, its legal gaps are 0..d; d<=7 from its three missing old roots and full original Delta10. Put h=h_x(gamma)<=k-1<=6 and q=q(gamma)<=min(m,h). All multiplicities of the original gamma order are retained.

## 2. Gamma begins in E

Here q>=1. At f-gap0 the exact runs are (h+1,1,1), so A0_beta=A1_beta=2h+6 by the literal positive-gap identity already independently reviewed for WB5/WB6. At later gaps gamma still begins in E, hence both A0_beta and A1_beta vanish. Therefore the exact T_j=F_beta+G_beta kernels are

    T_0=88+6h;
    T_j=76+(12-10Q_j)H_j+5Q_j(Q_j-1), j>=1,
    H_j=h+1_(j<=h), Q_j=min(q,j).

For fixed H, the change on raising Q to Q+1 is 10(Q-H)<=0 throughout this true run domain. Hence one may lower-bound every term using q=min(4,h), without changing any fiber weight or actual d.

For h<=5, lower further to q=h. Through j=1..h the increments are decreasing in j; the prefix total over gaps 0..d is therefore concave in d on 0..h. After h the increment is the constant c(h)=76+7h-5h^2 (for h1 it is positive too). Thus the minimum over d=0..7 is at d=0,h,or7. The three expressions are

    88+6h,
    B5(h)=88+(262h+6h^2-10h^3)/3,
    B5(h)+(7-h)c(h).

For 1<=h<=4, c(h)>=0 by quadratic concavity and B5(h)>=174 by cubic concavity on [1,4] (its endpoint values are174,256). For h5, B5=158,c=-14, yielding endpoint total130. All partial sums are therefore at least94.

For h6 use q<=4. At q4 the noninitial increments are

    T_1=90,T_2=30,T_3=-20,T_4=T_5=T_6=-60,T_7=-32,

with T0=124. The increments decrease until the plateau and are thereafter negative; hence the minimum prefix total is either T0 or the full sum. The full sum is 124+90+30-20-3*60-32=12. This seven-term polynomial evaluation is just the displayed exact finite sum, not a computer-assisted positivity table. Thus every actual gamma fiber beginning in E has total at least12. Since its size d+1<=8, its total exceeds its actual number of C words.

## 3. Gamma does not begin in E

Let c be its first label. If c is a C-minimum, zero x-frontier and the unique-low-C-min premise imply that c has signature yz. Then q=0, and beta at every f-gap j>=1 starts with this c. Its Y=Z=0, A0_beta=A1_beta=0, Q=0; consequently F_beta+G_beta=76+12H>=76.

If c is not a C-minimum, its only possible C-predecessor is the deleted f. Thus f<c and d=0: there are no later f gaps. In either case the f-gap0 word starts f followed by a nonempty-signature c. It therefore has all H,Y,Z>=1 and at least one of them equals1. The full original caps are H<=7,Y,Z<=6. The literal positive-gap identity yields

    a_beta=A1_beta=HY+HZ+YZ+min(H,Y)+min(H,Z)+min(Y,Z).

If H1, exact substitution into (1) gives

    F_beta+G_beta=82+5(Y+Z)-2YZ-2min(Y,Z)>=58.

If instead Y1 (or symmetrically Z1), it gives

    F_beta+G_beta=79+9H+6Z-3HZ-3min(H,Z)>=34.

For the latter bound, replace min(H,Z) by6. The remaining bilinear expression 61+9H+(6-3H)Z takes its minimum on the corners of [1,7]x[1,6], where the values are73,88,109,34. All bounds are original root-gap counts, not conditional root-probability estimates.

Thus every actual non-E-start gamma fiber has its f-first contribution at least34 and each further contribution (if present) at least76. In particular it exceeds its actual cardinality. Summing all disjoint true fibers proves (WB4).

## 4. Exact ledger effect and the remaining obstruction

This candidate closes only the displayed unique-empty-label subdomain. It would imply:

- In m3k7 and m4k6, where accepted prior results force a unique low C-minimum f, a genuinely unpaid residual must contain an additional nonminimal empty-signature label above f.
- In m4k7, either there is another low C-minimum (at most one, in addition to an empty one, by the existing classification), or the same nonminimal-empty obstruction must occur.
- No conclusion is added for m5k7 here.

A second empty label cannot simply be discarded: its presence can make all three root-missing runs at f-gap0 exceed1, so the A0=A1 identity used in Section3 no longer applies. The theorem explicitly excludes it. The remaining parameter list is still four cells, not three or fewer. No nonemptiness, prime/all-history novelty, fixed-u/b guarantee, or full B1/D10 claim is made.
