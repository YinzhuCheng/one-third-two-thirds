# SP1: the two remaining single-frontier types retain enough prefix credit

Date: 2026-11-10 UTC. Analytic author candidate for independent review. Exact original B1 private-predecessor lift, actual full Delta10,0<=m<=k<=7, no OLD seed moment. Small bounded gap arithmetic suggested the inequalities below; their proof is the displayed analytic endpoint argument, not a computed positivity table or original-object enumeration.

## Two fixed-pair gates

Select actual distinct C-minima c,f in either of these types:

A. c has full xyz signature and f has empty signature.
B. c has signature xy and f has singleton z, or symmetrically c has xz and f singleton y.

Then the original fixed pair(u,b) is strictly balanced. The conservative full-margin bounds are

    A: 3K-N >= (128/77)e(C)>0;
    B: 3K-N >= (99/80)e(C)>0.

The universal upper cap is5/9. The bounds already consume the original prefix credit2X+Y and do not assert any additional such term. Uniqueness of c is not needed in these two gates.

## 1. Exact shared gamma and restored runs

Delete c,f and fix an actual gamma, keeping both selected orders with their genuine multiplicities. Both selected points are C-minimal and incomparable. Their original degrees give actual successor deadlines R,S with R<=9,S<=6 in A and R<=8,S<=7 in B. Each gap pair gives one original word off the diagonal and two on it. The total fiber size is

    W(R,S)=(R+1)(S+1)+min(R,S)+1,

at most77 in A and80 in B. Short-word padding, if needed to describe the rectangle, preserves actual deadline legality and adds no words.

Let h and q be gamma's initial missing-x and E runs. Only f was removed from Mx, so h<=k-1<=6, with q<=min(m,h). If q0, every reconstructed word has Q0, hence F>=48 and nonnegative prefix credit, stronger than both conclusions. Assume q>=1. Then gamma starts with a yz-signature E label and1<=h<=6.

In the f-first order, f has gap a and c gap b with a<=b. The restored runs are EXACTLY

    H=min(h,b)+1_(a<=h), Q=min(q,a).

In the c-first order, c has gap a and f gap b with a<=b; then

    H=min(h,a), Q=min(q,a).

For positive first gap the word starts in E, so hy=hz0 and the prefix kernels vanish. Increasing retained q to h only weakens the kernel, because Q<=H and its forward Q difference is8(Q-H)<=0.

If f is first at gap0, its next C symbol is either the first E point or c in the same gap. In A the two other missing-root runs are exactly1,1. The original full margin kernel F+2x_beta+y_beta is therefore72+8H. In B the two runs are1,0 (or0,1), giving58+7H. These use the exact original prefix kernels, not an extra approximate credit. If c is first at gap0, the full kernel is48 in A; it is57 in B, because the root missing from c appears at the immediately following f or E point. All prefix kernels then vanish in this c-first case.

Thus the two orders at gap(0,0) have different genuine weights, and are retained separately rather than averaged as exchangeable labels.

## 2. One lower rectangle for every retained h

For positive first gaps, both restored H and Q (after relaxing q to h) are nondecreasing as h increases. Q>=1, so first raising H and then Q weakens the kernel. Hence the interior can be bounded below by h6. Define

    G(a)=48+2min(6,a)-4min(6,a)^2,

whose values at a0,...,6 are48,46,36,18,-8,-42,-84 and which stays-84 thereafter. For f-first positive a define

    Psi(a,b)=48+(6-8min(6,a))H*+4min(6,a)(min(6,a)-1),
    H*=min(6,b)+1_(a<=6).

In particular at a7 (possible only in B), H*=6 and Psi(7,b)=-84, NOT-126. Retaining this distinction is essential.

The zero-axis terms increase with h, so bound them instead by h1. In A, f-first at a0 contributes80 for b0 and at least88 for b>=1, while the entire c-first a0 row contributes48 per word. In B those constants are65,72,57. Introduce L=88,C=48,O=80 in A and L=72,C=57,O=65 in B. A lower bound for the total ORIGINAL full margin in the gamma fiber is

    T(R,S)=O+LR+C(S+1)
      +sum_(a=1)^S sum_(b=a)^R Psi(a,b)
      +sum_(a=1)^R (S-a+1)_+G(a).

All same-gap multiplicities remain represented by the two sums. This is not FKG on their union and does not use an artificial moment.

## 3. Endpoint reduction in R

For s<=6, let P_s(t) denote the sum of the positive-a polynomial Psi_a at held run t, together with the artificial a0 term48. At t7 its values for s0,...,6 are

    48,82,68,14,-72,-182,-308.

For s<=3 these remain positive whenever1<=t<=7. Put ell=L-48, namely40 in A or24 in B. Increasing R from n-1 to n adds the f-first column with axis entry L, and, if n<=S, the c-first row. For n1,...,4 when S>=4, the increments are

    92+46S+ell, 80+36S+ell, 68+18S+ell, 64-8S+ell,

all positive. For S<=3 all increments are positive, by these early formulas when n<=S and by P_S+ell afterward.

For S4, the n5 increment is-16+ell>0, and all n>=6 increments are-72+ell<0. For S>=5 the n5 increment is76-42S+ell<0. At n6 the row-present increment is112-84S+ell<0, while the row-absent increment is P_S(7)+ell<0. At n7 in case A only a row-absent negative P_S(7)+ell can occur. In case B, S7 requires special treatment: the added a7 contribution uses-84 rather than-126 and the new c-first row also uses-84, giving the negative increment-452. For S<=6 the n7 increment is again P_S(7)+ell<0. Later increments are negative; specifically in case B with S7 the n8 increment is-368, and otherwise they are P_S(7)+ell. This exhausts the relevant caps R9,S6 or R8,S7.

Therefore T either increases throughout R or increases and then decreases. Its minimum is at R0 or at the corresponding maximum9/8. The first endpoint is

    A: T(0,S)=128+48S>=128;
    B: T(0,S)=122+57S>=122.

## 4. Case A upper endpoint

Set U(S)=T(9,S),0<=S<=6. Here U0=80+9*88+48=920. For1<=s<=6, adding the new f-first row and c-first column gives

    U(s)-U(s-1)=sum_(b=s)^9 Psi(s,b)+sum_(a=0)^sG(a).

Since sum_(b=s)^9 min(7,b+1)=49-s(s+1)/2, ordinary polynomial summation gives

    D_s=822-(1304/3)s+44s^2-(4/3)s^3.

For s1,...,5, D_(s+1)-D_s=-4(s-7)(s-14)<0. Thus U is discretely concave. Its other endpoint is

    U6=920+430+118-122-298-418-490=140.

Hence U>=140 and the complete rectangle has T>=128. With W<=77 this gives the first claimed mean128/77.

## 5. Case B upper endpoint

Set V(S)=T(8,S),0<=S<=7, with V0=65+8*72+57=698. For1<=s<=6, the c-first zero entry is57 rather than48, and the arithmetic-series sum for the f-first row uses42-s(s+1)/2. Thus

    V(s)-V(s-1)=741-(1124/3)s+40s^2-(4/3)s^3.

Its successive differences are-4(s-7)(s-12)<0 for s1,...,5. Consequently V is concave through S6, with

    V6=698+405+141-59-203-299-355=328.

This gives V>=328 on S0,...,6. At s7, the f-first row has two terms-84, while the c-first prefix sum is57+46+36+18-8-42-84-84=-61. Therefore the final increment is-168-61=-229, giving V7=99. No concavity across that final step is asserted or needed. Combining the endpoints proves T>=99 over the whole case B rectangle. With W<=80 the mean is at least99/80.

## 6. True summation and ordinary consequence

For q>=1, the preceding lower rectangles apply to each actual retained gamma; q0 fibers are stronger. Multiply each mean bound by its actual fiber size and sum the original full-margin kernel. This proves both fixed-pair inequalities with prefix credit used exactly once. Arbitrary actual retained tails and their extension multiplicities are retained throughout.

Conditional on independent acceptance of SP1, the reviewed OP1/SG1/RC1/RG1 reduction has no remaining single-x-frontier branch: its full degree10 plus empty-minimum type is gate A, and its nonfull degree9 plus opposite singleton type is gate B. The earlier gates already cover the other one-frontier forms and all two-or-more-frontier objects. Thus every actual exact-D10 lift with at least one x-containing C-minimum is ordinary-balanced without OLD moment. This ordinary conclusion uses the earlier bank/old-guard alternatives and does not assert universal fixed-u/b balance across those alternatives.

Zero-x-frontier cells are not paid by this theorem. No remaining screened object is asserted to exist, no NB claim is made, and no net-new ordinary-population credit beyond prior guards is assigned. The theorem neither deletes tail weights nor imports a moment into a conditioned or deleted poset. No original-poset scan, LE DP, or unreviewed finite positivity certificate is a proof dependency.
