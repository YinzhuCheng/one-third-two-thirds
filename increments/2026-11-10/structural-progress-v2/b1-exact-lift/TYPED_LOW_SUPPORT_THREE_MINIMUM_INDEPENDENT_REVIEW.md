# TL1 independent mathematical review

Date: 2026-11-10 UTC. Reviewer: audit_alpha2_four, not involved in TL1 derivation.

**PASS.** Reviewed source `TYPED_LOW_SUPPORT_THREE_MINIMUM_GATE.md`, SHA256 `884e39375674a6f7dd0db66985a8a5f02980ab59a76bbcad05ac97ac7c648ebe`, independently verified. This is an analytic fixed-pair sufficient gate, with a separate ordinary-bank consequence using the already-reviewed TB2/HF1/MF2 dependencies.

## True degrees and fibers

The three selected C-minima are distinct and form an antichain. Since f has support at most1, it is outside E and above u. Its at least two missing T roots are outside-C incomparable neighbors, so deg_C(f)<=8. The two other selected minima have C-degree<=10. Every retained gamma label before a selected point's first successor is incomparable with it, since the selected point is C-minimal. Charging the other two selected minima gives the typed deadlines8,8,6 exactly as claimed. These caps use original degrees, not new degrees after deletion.

Fixing gamma and the named selected order pi partitions all actual C words. Nondecreasing selected gaps encode every insertion once, including all same-gap orders via pi. Coordinate upper bounds are exactly the remaining legality constraints; all-selected-first is always legal. Formal padding to eight retained letters is count-preserving because actual deadlines prohibit crossing the placeholders. Gamma's further suffix, when present, is fixed after the insertions. Thus the proof retains arbitrary real retained orders, not a chosen finite tail family.

The typed baseline of gap tuples is a distributive sublattice under coordinatewise min and max. Uniform mass is log-supermodular. Further actual deadline constraints define a nonempty down-set inside it. Finite FKG implies that conditioning decreases every increasing gap statistic, or increases the expectation of every decreasing one. This applies to the joint typed kernel, not only the first coordinate. Different gamma/pi fibers need not have equal sizes; the proof correctly multiplies by each actual size.

## Typed pointwise kernel

When f is first selected, the first selected x-containing label is second. Before it there are exactly b gamma labels and f, so hx<=min(k,b+1). Since f is not in E, the initial E run is at most a. Put h*=min(7,b+1); feasibility gives a<=6 and a<=h*. For q>=1, first increase actual hx to h*, which lowers the kernel because6-8q<0, and then increase q to a, which lowers it because the forward q difference is8(q-h*)<=0. Discarding the nonnegative hy/hz term is valid. If q0, F>=48; Psi<=48 on this domain, so the same lower bound holds. At a0, q0 and Psi48 is exact as a lower bound. This verifies F>=Psi without incorrectly assuming actual hx>=a.

Psi decreases in b when a>=1 and is constant in b when a0. At fixed b the positive-a forward difference is8(a-h*)<=0 for feasible adjacent a; the0-to1 difference is-2h*. Thus it is decreasing on the entire typed lattice. If an x-containing point is first selected, hx<=a and the standard MF kernel gives G(a); nondecreasing gaps and f's deadline force a<=6 even when f is last. The displayed G is therefore valid on every remaining type. Neither c nor d needs full signature: only stopping hx is used.

## Independent algebraic evaluation

The three baseline sums were independently evaluated by reversing the author's summation order and using closed polynomial sums, not by enumerating original words or posets. For f first, at fixed b put n=min(6,b), h*=min(7,b+1). Summing Psi over a0,...,n gives

    48(n+1)+h*(2n-4n^2)+(4/3)n(n+1)(n-1).

Multiplying by9-b and summing b0,...,8 gives588; the corresponding count sum(9-b)(n+1) is161. For the other two types use

    sum_(a=0)^b G(a)
       =48(b+1)+b(b+1)-(2/3)b(b+1)(2b+1).

Multipliers9-b and7-b over b0,...,6 give4116 and2772, with counts140 and84. Hence the means are84/23,147/5,33, and the smallest is84/23>0. These are elementary finite polynomial identities; exact rational calculation only checks their evaluation and is not a computer-assisted positivity-table dependency.

Every genuine fiber therefore has average F>=84/23. Summing actual sizes and using3K-N=sum F+2X+Y proves the margin. The m0 branch separately has F>=48, which is stronger. The original universal upper cap completes fixed-pair strict balance.

## Ordinary consequence and feasibility

With at least three x-containing minima, MF2 pays. With exactly two, if a support<=1 minimum misses x it is a distinct third point and TL1 applies. If such a point contains x, it is necessarily signature{x}, has C-degree<=8, and HF1 applies with the other minimum's degree<=10. If no low-support minimum exists, all C-minima have support>=2 and the already-reviewed TB2 bank applies. These alternatives are exhaustive and establish ordinary existence throughout the two-or-more-x-minimum sector, not fixed-u/b payment in the TB2-only branch. A remaining unpaid object consequently has at most one x-containing C-minimum.

The supplied parallel-component example is feasible: with m-chain E, singleton signature-y f, and two full singleton components, k=m+1; f has C-degree m+2 and full degree m+4<=10 for m<=6, the selected full points have degree m+2, E points degree5, x degree m+4, and u degree m+3. Fixed root budgets also fit. The full singleton labels are twins, so the example supplies no new ordinary-population credit. No statement that the ultimate residual is nonempty follows.

No mathematical gap found. This audit is internal and independent, not external peer review or formal verification. It uses no OLD moment, object enumeration, LE DP, freely chosen completion weights, altered original degrees.
