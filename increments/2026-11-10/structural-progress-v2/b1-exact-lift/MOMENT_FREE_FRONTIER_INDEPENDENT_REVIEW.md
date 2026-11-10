# MF1 independent mathematical review

Date: 2026-11-10 UTC. Reviewer: audit_alpha2_four, not involved in deriving MF1.

## Initial verdict and required correction

MF1 itself passes: its two stated frontier conditions suffice without OLD moment. The general displayed B-certificate must be explicitly restricted to m>=1. For m0 the correct separate bound is3K-N>=48e(C)+2X+Y. The initial manuscript SHA256 is `fe5d6ee174cfb4f05ede77c9cfa8a61f0a99d1cb357a55e7eeb5730738774ae9`; acceptance of its unrestricted general strong inequality is withheld pending this correction.

This is a real quantifier issue, not just a missing proof: take E empty and C a three-point antichain, consisting of one yz-signature point and two full-signature points. Then m0,k1, actual Delta<=5, and r2,d10 are legal choices. Each C label is equally likely first, so mean hx=1/3, hy=hz=0, and mean F=50. Also X=Y=0 because every C point requires y,z. But the defined B(2,10;0,1)=48+6(9/11)=582/11>50. Hence the general strong inequality is false at this m0 input. The claimed fixed-pair balance at m0 is unaffected because F>=48 always.

## Mathematical audit for m>=1

### Actual deadlines and word multiplicity

Distinct selected full C-minima are pairwise incomparable. For one selected point, every retained gamma label preceding its first successor is incomparable with it: it has no predecessor at all in C. Adding the other r-1 selected minima gives d_c+r-1<=d. This uses its original point degree, not a degree recomputed in C-S. Consequently D=d-r+1>=0 and every actual deadline is at most D. Full-signature labels are comparable with all outside-C labels in this original lift, so full Delta10 indeed permits d10. Equality of degrees is unnecessary.

Fixing gamma and selected order pi partitions actual words. Inserting selected points at positions s1<...<sr corresponds uniquely to gaps g_j=s_j-j, which are nondecreasing. Legality is exactly g_j<=d_(pi_j). Thus every feasible tuple has multiplicity one, including selected points placed in the same gap. The unselected suffix beyond the first D gamma positions has no choices left. If gamma is shorter, padding to D with fixed formal tokens creates no extra feasible insertion because every deadline is bounded by the original length. These tokens may be removed bijectively. The all-selected-first tuple is always feasible.

### Lattice stochastic comparison

The increasing r-tuples in[1,D+r] form a finite distributive lattice under coordinatewise min and max: strict adjacent separation is preserved by both operations, and distributivity is inherited coordinatewise. Uniform positive mass is log-supermodular with equality. The FKG positive-association theorem therefore applies to arbitrary increasing real functions. The feasibility set is decreasing in this lattice. For an increasing event A={s1-1>=t}, association of1_A and -1_feasible gives

    P(A intersect feasible)<=P(A)P(feasible).

After dividing by the positive feasibility probability, the claimed conditional first-hit stochastic domination follows. This use of FKG is valid even though the feasible set has nonidentical coordinate deadlines; no symmetry among these deadlines is needed. The proof uses FKG as a standard mathematical dependency, not a computational assertion.

### Kernel comparison

For fixed h, increasing q by1 changes48+(6-8q)h+4q(q-1) by8(q-h)<=0 throughout the allowed range q<h. Removing9(hy+hz) is a lower bound. Let g(h) be the resulting expression with q=min(m,h). For h<=m, g(h)=48+2h-4h^2 and its forward difference is-8h-2; for h>=m its slope is6-8m<0. Thus g is nonincreasing for every m>=1, including the transition. Since actual hx<=min(k,H), the pointwise F>=G(H) bound follows. Conditional stochastic domination then implies each genuine fiber average is at least the same B. Multiplication by its actual cardinality and summation proves the general margin bound for m>=1. There is no moment at any stage and no equal weighting of fibers.

### First-hit law and constants

For an unrestricted r-subset, H=t means its first selected position is t+1; choose the remaining r-1 positions from D+r-t-1 choices. This proves the displayed binomial law directly. Independent exact rational evaluation of this closed finite identity gives numerators210,86 over55 for(r,m,k)=(2,6,6),(2,5,7), and3622 over165 for(3,7,7). The unclaimed cells yield-42/55 and-90/55. This arithmetic is evaluation of the analytic identity, not an object search or CA positivity certificate.

For fixed h, increasing m cannot increase the relaxed kernel, by the same q difference. Increasing k cannot increase it because g(h) is decreasing. Hence(6,6) dominates all m<=k<=6, (5,7) dominates all m<=5,k<=7, and(7,7) dominates the entire three-minimum domain. Cases m0 are covered separately by F>=48. Positive margins and the inherited universal5/9 upper bound prove the exact stated MF1 conclusion. Negative constants in the two excluded cells imply no counterexample.

## Realizability and non-moment control

For every m<=k<=7, take all k missing-x labels in one yz-signature chain, with E its first m labels, and add three full isolated C labels. This realizes the three-minimum premise with E an ideal. A full label has degree k+2<=9; an E label has only x,u and the three full labels as incomparable neighbors, hence degree5; a missing label outside E has degree4. Together with x degree k+3, u degree m+3 and the fixed root budgets, actual Delta10 holds, including empty E or empty missing set. This demonstrates feasibility, not new ordinary-population coverage.

The separate old-moment-failing control was independently checked by component shuffling. For the parallel E four-chain, three full points, and empty-signature two-chain, e(C)=7560. Missing-x length before the first full point has mean6/4; missing-y and missing-z lengths each have mean2/8. Hence A3=45360 and A2=30240. After removing the empty two-chain, R0 has ten labels and1680 extensions: A3=1260,A2=420,A1=A0=0. Inserting v1 first and v2 into one of11 subsequent positions gives A0=18480. Putting the first R0 root first, v1 second, and v2 into one of10 later positions gives A1=16800. Thus the OLD margin is-55440 exactly. The displayed degree list is consistent: empty-signature points have ten incomparable neighbors; E labels have seven; full labels eight; roots and u meet the stated bounds. This is a genuine actual Delta10 seed outside OLD moment and covered by MF1. Its fair twins remain, so it is not a new ordinary balanced-pair population or NB result. The author's diagnostic DP is unnecessary for these shuffle derivations and was not run for this review.

## Scope

Except for the explicit m0 quantifier correction above, no mathematical gap found. MF1 is a selected-frontier sufficient condition for the original fixed pair, not full B1, a full D10 result, a sharp frontier classification, or a claim of novelty beyond old guards. This is an internal independent audit, not external peer review or formal verification. No object enumeration or external write was used.

## Corrected-version binding and final verdict

The revised manuscript SHA256 is `ee284d443736573468786cc11060d9eff3447938f9930ad6136d158e6fac5a48`, independently verified. It explicitly restricts both the B definition as a certificate and the displayed margin inequality to m>=1, supplies the separate unconditional m0 bound, and retains the actual countercontrol in a correction appendix. This resolves the quantifier issue. **Final verdict: PASS MF1 and its corrected general frontier certificate as stated in this revised version.** The initial issue and its witness above remain part of the review record; they do not change the accepted two-/three-minimum sufficient conditions or the actual non-moment example.
