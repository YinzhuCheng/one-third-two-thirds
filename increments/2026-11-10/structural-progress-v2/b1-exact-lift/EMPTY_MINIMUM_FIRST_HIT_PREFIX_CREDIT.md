# EP1: exact old-prefix credit at an empty minimum

2026-11-10 UTC. Analytic author candidate, independent review requested. Exact original B1 lift, actual full Delta10, m<=3,k<=6, no OLD moment. Suppose C has an empty-T-signature C-minimal label f. Then the ORIGINAL fixed pair(u,b) has

    3K-N>=e(C)>0, Pr(u<b)<=5/9.

The e(C) margin is conservative, not a sharp probability claim. This is not a full parameter theorem without the displayed empty-minimum premise.

## 1. Keep the exact old-prefix counts
For a true beta in LE(C) with root-missing runs hx,hy,hz, literal insertion of the two noninitial private roots in positive gaps gives

    x_beta=hy hz+min(hy,hz),
    y_beta=hx hz+min(hx,hz)+hx hy+min(hx,hy).

Their sums are exactly X and Y from the original event identity. The min terms count the extra order when the two inserted roots share a gap. Thus the exact full margin is the sum over beta of F(beta)+2x_beta+y_beta, not just F. All these are counts of genuine old R words, not free interface masses.

Delete f and fix a genuine retained gamma. Its legal f gaps are j0,...,d with d<=7, since f has three missing old roots and its original C-degree<=7. As in FH1, let h<=k-1<=5 and q<=min(m,h) be gamma's initial missing-x and E runs. Reinsertion gives H_j=h+1_(j<=h),Q_j=min(q,j). Put

    b_j=48+(6-8Q_j)H_j+4Q_j(Q_j-1).

If q0, every original fiber word already has F>=48 and nonnegative prefix credit, so the theorem is stronger than required. Assume q>=1. Then gamma starts in E, whose signature is yz.

At gap0, f is first and has empty signature. Consequently hx=h+1,hy=hz=1 EXACTLY. The extra part discarded in b_0 is

    9(hy+hz)+2x_beta+y_beta
      =18+4+2(h+2)=2h+26.

At every j>=1, beta starts with an E label, so hy=hz0 and both prefix kernels vanish. Therefore the entire genuine gamma fiber margin is at least

    sum_(j=0)^d b_j +(2h+26).

Different gamma fibers keep their actual cardinalities. There is no conditional moment or arbitrary completion weighting.

## 2. Prefix-average endpoints with exact first-slot credit
For q>=1, b_j decreases through j=q, stays constant through h, jumps upward at h+1, then stays constant. Adding the positive credit2h+26 to the first term preserves this form for prefix-average minimization. The smallest prefix mean over d0,...,7 therefore occurs at d=h or7, exactly as in FH1.

At fixed h the b_j are nonincreasing in q, while the added credit is independent of q. Thus use q=min(3,h).

For h1,q1, the two endpoint total sums INCLUDING credit are132 and408, with denominators2 and8. For h2,q2, they are164 and344, with denominators3 and8. All these means exceed1.

For3<=h<=5,q3, elementary summation gives

    S_h=sum_(j=0)^h b_j=38+84h-18h^2,
    S_7=S_h+(7-h)(72-18h)=542-114h.

Including credit gives

    S_h+2h+26=64+86h-18h^2>=44,
    S_7+2h+26=568-112h>=8.

The first inequality uses concavity and endpoint values160,44 on[3,5]. Its denominator h+1<=6, hence its mean is>1. The second denominator is8, giving mean>=1. Thus every actual gamma fiber, at its actual d, has ORIGINAL total margin per C word at least1.

Summing by true fiber cardinality yields3K-N>=e(C). This argument uses the full exact prefix credit once and does not add it a second time after summation. No leftover+2X+Y is claimed in the theorem. Closed finite sums are analytic; diagnostic rational arithmetic is not a computer-assisted proof dependency.

## 3. Consequence for the remaining zero-frontier m3k6 cell
The zero-x-frontier m3k6 ordinary residual cannot contain an empty-signature C-minimum. Its RC1-forced missing-x low-support minima must therefore have singleton y/z signatures. Moreover L=C-(Uy union Uz) is an ideal: any nonempty L would have a C-minimum of signature empty or{x}; empty is now paid, and{x} contradicts zero x-frontier. Hence L is empty in that remaining cell, and NP1 lower distinguishing ports reduce to the original x alone.

This is only a necessary residual condition, not a nonemptiness or NB claim. In other domains existing FH/CT gates may already pay the premise. Original twins/VG may still pay any illustrative input; no net-new ordinary-population claim or unguarded control is supplied.

No original-poset scan, LE DP or unrelated computational output was used.
