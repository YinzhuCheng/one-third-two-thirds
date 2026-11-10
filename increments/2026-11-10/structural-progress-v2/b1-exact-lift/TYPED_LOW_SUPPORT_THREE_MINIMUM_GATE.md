# TL1: a typed three-minimum gate without OLD moment

Date: 2026-11-10 UTC. Analytic author candidate, uninvolved audit requested. Exact original B1 private-predecessor lift, actual full Delta10, 0<=m<=k<=7. No OLD seed moment.

## Theorem and ordinary consequence
Suppose C has two distinct C-minima c,d strictly above x and another C-minimum f missing x with old T-support of size at most1. Then the original fixed pair (u,b) satisfies

    3K-N >=(84/23)e(C)+2X+Y>0,
    1/3<Pr(u<b)<=5/9.

If m0, the separate unconditional F>=48 proves the displayed bound as well. Consequently EVERY actual exact-D10 lift with at least two x-containing C-minima has an ordinary balanced pair without OLD moment: three or more are paid by MF2; with exactly two, either a support<=1 C-minimum exists and TL1 applies (if it contains x, HF1 already pays), or every C-minimum has support>=2 and TB2 pays the physical three-pair bank. This is not a fixed-u/b conclusion in the TB2-only branch and not full B1 or net-new ordinary population.

## 1. Original degree caps and actual fibers
The selected points are an antichain of C-minima. Actual full Delta10 gives degC(c),degC(d)<=10. The low-support f is outside E, lies above u, and has at least two missing old roots; hence degC(f)<=8. It misses x and is not in E.

Delete c,d,f and fix a genuine retained word gamma and one genuine selected relative order pi. No selected point has a retained predecessor. Its legal insertion deadline is the number of gamma letters before its first retained successor. The other two selected minima are incomparable, so original degrees give deadlines at most8 for c,d and6 for f. There are no inherited degrees on a deleted object.

Legal gaps0<=g1<=g2<=g3 are coordinate-upper constrained with these typed caps. Pad short gamma to length8 using formal end placeholders, as in reviewed MF1; actual deadlines exclude placements after any placeholder. Each actual insertion word belongs to exactly one gamma/pi fiber. The uniform typed baseline is a finite distributive lattice under coordinate min/max. Actual deadline conditioning is a nonempty decreasing event, so FKG makes all increasing gap functions stochastically smaller. The kernel lower functions below are coordinatewise nonincreasing, which gives their baseline means as lower bounds on every actual fiber. Multiply by EACH actual fiber size before summing; different tails and orders are not equally weighted.

## 2. Typed kernel functions
Use the exact original F=48+(6-8q)h_x+9(h_y+h_z)+4q(q-1). Discard the nonnegative 9-term. If q0, F>=48. If q>=1, increasing h and then q within q<=h only decreases the remaining expression.

If f precedes the first of c,d, it is the first selected token. Let a=g1, b=g2. Then h_x<=min(k,b+1), since f also misses x; q<=a, since f is outside E. The worst m,k<=7 lower function is

    Psi(a,b)=48                        if a0,
             48+(6-8a)min(7,b+1)+4a(a-1) if a>=1.

Here0<=a<=6, a<=b<=8, so a<=min(7,b+1). Psi is nonincreasing in both coordinates: increasing b has coefficient6-8a<0 when a>=1; increasing a has difference8(a-h)<=0; the step from a0 to1 drops by2h. Thus F>=Psi for every actual word, with the correct direction under FKG.

If a selected x-containing point precedes f, let a=g1. Then h_x<=min(k,a), and the worst m,k<=7 lower function is

    G(a)=48+2a-4a^2,

because the low-point cap forces a<=6. This is nonincreasing for integer a0,...,6. No full signature for c,d is needed: containing x already stops h_x. Actual earlier gamma successors can only improve these bounds.

## 3. Three baseline sums, all positive
The two named x-points have symmetric caps, leaving three typed-order cases (each occurs for two named orders).

1. f first:0<=a<=6, a<=b<=8, b<=g3<=8. The exact lower mean is

    sum_(a=0)^6 sum_(b=a)^8 (9-b)Psi(a,b)
      /sum_(a=0)^6 sum_(b=a)^8 (9-b)
      =588/161=84/23.

2. f middle:0<=a<=b<=6, b<=g3<=8. The exact lower mean is

    sum_(a=0)^6 sum_(b=a)^6 (9-b)G(a)
      /sum_(a=0)^6 sum_(b=a)^6 (9-b)
      =4116/140=147/5.

3. f last:0<=a<=b<=g3<=6. The exact lower mean is

    sum_(a=0)^6 binom(8-a,2)G(a)/binom(9,3)
      =2772/84=33.

These displayed finite polynomial sums are exact elementary identities, not an object enumeration or a computer-assisted positivity table. Each actual gamma/pi fiber has average F at least84/23. True weighted summation and 3K-N=sum_beta F+2X+Y prove TL1.

## 4. Residual and proof boundaries
For ordinary existence, combining TL1 with reviewed TB2/HF1/MF2 removes the whole two-or-more-x-minimum sector. Therefore a still-unpaid exact-D10 lift has at most one x-containing C-minimum, not merely two saturated full ones. This is a necessary residual restriction and does not assert residual nonemptiness or NB failure. It does not pay arbitrary zero/one-frontier objects.

The typed hypotheses are genuinely consistent, though the following illustration is already old-twin guarded: E an m-chain yz, f a y-signature label, and two isolated full-signature C labels, all four components parallel; m<=6. Then k=m+1, f has C-degree m+2<=8, selected full degrees m+2<=8, and all actual full degrees<=10. Nonvacuity is not new ordinary coverage and is not a sharpness claim.

No moment is used, even at the final sum. No arbitrary completion weights, deleted-object probability witness, original-poset scan is involved.
