# Independent analytic audit of EP1

2026-11-10. **PASS.** Source `EMPTY_MINIMUM_FIRST_HIT_PREFIX_CREDIT.md`, SHA256
`7943626ce8d7e9b9effab1ff98dbf432f43f7dc4dc4a76c7587fd9abc05fcceb`.

I did not participate in the derivation. I independently reconstructed the prefix kernels, genuine deletion/insertion fiber, first-slot credit, endpoint argument and residual consequence. No mathematical gap was found. This is internal independent review, not external peer review or formal verification. No object enumeration or computational positivity certificate was used.

## 1. Exact prefix counts and true single-label fibers

For each actual beta in LE(C), an old word whose only initial T root is x is formed by inserting y,z in positive beta gaps before their first successors. There are h_y h_z gap choices plus one additional order for each equal gap, hence x_beta=h_y h_z+min(h_y,h_z). The analogous initial-y and initial-z counts sum to the stated y_beta. These are bijective complete old-R-word counts even when beta starts with an empty-signature C label. Summing gives exactly X,Y in the inherited original event identity.

The selected empty-signature C-minimum f has three outside-C incomparable roots x,y,z. It is outside E and is above u; thus original full Delta10 gives deg_C(f)≤7. After deleting f, every retained letter before its first successor is incomparable with it, giving a true insertion deadline d≤7. The legal gaps 0,...,d represent all actual words of that gamma fiber once each; no residual completion weighting is omitted.

If gamma has initial missing-x run h and E run q, then h≤k−1≤5 and q≤min(m,h). Reinserting the missing-x, non-E f at gap j gives H_j=h+1_(j≤h) and Q_j=min(q,j). This remains true when h is the entire gamma length. If q=0, every resulting word has Q_j=0 and its full contribution is at least48, so the stronger direct branch is valid.

For q≥1, gamma begins in E. At j0 the original runs are exactly h_x=h+1,h_y=h_z=1. Therefore x_beta=2 and y_beta=2(h+2). Together with the discarded9(h_y+h_z)=18, the credit is exactly

    18+2*2+2(h+2)=2h+26.

For every j≥1 the first beta label is in E, so h_y=h_z=0 and both prefix kernels vanish. Thus the first-slot credit occurs exactly once. In this q≥1 branch the displayed b_j plus this credit is actually the exact full contribution sum, not a substitution of a freely chosen prefix mass.

## 2. Endpoint minimization and all arithmetic

For fixed h,q≥1, the sequence b_j is nonincreasing until q, constant through h, then jumps upward at h+1 and is constant thereafter. Adding the positive credit only to its first term preserves the nonincreasing first segment. Prefix means are therefore nonincreasing through endpoint h; after that, repeated addition of one constant makes their direction fixed (or leaves them constant). Hence the minimum over all d=0,...,7 lies at h or7. Evaluating this larger syntactic range is harmless when the actual deadline or retained word length is smaller: it proves a lower bound on every actual feasible prefix.

Increasing q decreases b_j pointwise, since the increment in the relaxed kernel is8(Q_j−H_j)≤0. The credit is independent of q. Thus the worst allowed q is min(3,h).

For h1, b_0,b_1 are60,44 and the six later terms are46; adding28 gives endpoint totals132 and408. For h2 the first three terms are66,42,26 and the five later terms are36; adding30 gives164 and344. Their denominators are respectively2/8 and3/8, so every endpoint mean exceeds1.

For3≤h≤5, q3, direct summation gives

    S_h=38+84h−18h²,
    S_7=S_h+(7−h)(72−18h)=542−114h.

The credited totals are64+86h−18h² and568−112h. The first polynomial is concave, with values160 at h3 and44 at h5, so its value is at least44 and its denominator at most6. The second is decreasing, with minimum8 at h5 and denominator8. Thus both endpoint means are at least1. No intermediate deadline was left unverified by the argument, and no computational table is needed.

## 3. Summation and residual interpretation

Every actual gamma fiber has at least one word and total original contribution at least its cardinality d+1. Summing the disjoint fibers yields

    3K−N=sum_beta(F+2x_beta+y_beta)≥e(C)>0.

The source correctly does not append an additional2X+Y after this summation: those exact counts have already been consumed once in the first-slot credit. The original upper cap5/9 supplies strict fixed-(u,b) balance, without any seed moment. The bound is not asserted sharp.

Finally L=C−(U(y) union U(z)) is a C ideal. Any nonempty L therefore contains a C-minimum, whose signature is empty or {x}. In the zero-x-frontier m3k6 domain, the latter is excluded by zero frontier, and the former is paid by EP1. Thus a still-unpaid object in that domain must have L empty; its RC1-forced low-support missing-x minima have singleton y/z signatures. NP1's lower active ports then reduce to x alone. This is a valid necessary residual deduction, not an existence result or a statement that the remaining upper ports cannot defeat VG.

The proof adds no original-poset scan, finite computational dependency, full-B1 assertion or new-population credit. No external repository was modified.
