# Independent analytic audit of SP1

2026-11-10. **PASS: both fixed-pair gates and the stated ordinary-existence consequence.**

Source `SINGLE_FRONTIER_TYPED_PREFIX_CREDIT_CLOSURE.md`, SHA256
`a319bc30c9e2bb73c6f8839fd92af40df5f4e0313a2f1df851cd617887b0dc7b`.

I did not participate in SP1 or the parent's parallel derivation. I independently reconstructed the exact runs, complete original prefix contributions, rectangle inequalities and dependency stitching after reading the frozen source. No gap was found. This is internal independent review, not external peer review, formal verification or a literature-originality claim. Diagnostic tables are not used as proof; no original-poset enumeration or LE DP was performed.

## 1. Actual degree caps and multiplicities

The selected c,f are incomparable C-minima. For a fixed genuine gamma after deleting them, each insertion deadline counts retained letters preceding the first successor, all incomparable with the selected point. Charging the other deleted minimum gives R≤9,S≤6 in A: full c has C-degree≤10 and empty f has C-degree≤7. In B, c of signature xy misses one root and has C-degree≤9; f of signature z misses two and has C-degree≤8, giving R≤8,S≤7. The symmetric xz/y type is identical.

For every pair of allowed retained gaps there is one word if the gaps differ and two actual orders if they coincide. Thus the complete gamma fiber has W=(R+1)(S+1)+min(R,S)+1, bounded by77 or80 respectively. Selected labels are never made exchangeable. Padding short gamma words leaves the actual deadlines unchanged and adds no feasible placement. Any retained suffix beyond the maximum deadline is fixed, not assigned an independent completion weight.

Only f is missing x, and neither selected point is E. Hence h≤k−1≤6 and q≤h. When q0 all reconstructed E runs vanish and the original full kernel is at least48, sufficient for both mean bounds. When q≥1, gamma starts in E, giving the typed identities below. The premise itself implies m≤k−1, so potentially infeasible m=k cells cause no hidden additional case.

## 2. Exact restored runs and prefix credit

For f-first gaps a≤b, the missing-x run is H=min(h,b)+1_(a≤h) and the E run Q=min(q,a). For c-first gaps a≤b, the runs are H=min(h,a), Q=min(q,a). These formulas include equal gaps and the boundary at a=h. For instance, at a>h in f-first, f no longer extends the original missing-x run; this explains why the a7 case differs.

If the first selected gap is positive, beta still begins in E; h_y=h_z=0 and both original prefix kernels vanish. At f-first gap0, type A has h_y=h_z=1, even when c follows f in the same gap. Using x_beta=h_y h_z+min(h_y,h_z) and the two analogous terms for y_beta gives

    F+2x_beta+y_beta=72+8H.

For type B, the non-x runs are1,0 (or0,1), giving58+7H. At c-first gap0, type A has all runs zero and contributes48. Type B has H=0 and just one other missing-root run equal1, because the next C label is f or the first E point. Both prefix kernels vanish and the contribution is57. These calculations confirm every zero-axis constant, including the unequal weights at gap(0,0).

For positive first gaps, increasing q to h weakens the relaxed kernel: increasing Q by one changes it by8(Q−H)≤0. As retained h increases from1 to6, both relaxed H,Q are nondecreasing. First increasing H weakens the kernel since Q≥1; then increasing Q weakens it since Q≤H. This justifies the common h6 interior lower bound without coupling it incorrectly to the axis bound.

On the axes the exact expressions instead increase with h, so h1 yields f-first constants80/88 in A and65/72 in B, for b0/b≥1; the c-first constants remain48/57. Mixing these lower bounds is legitimate pointwise, and does not require that their simultaneous extremal values be realizable in one gamma.

The resulting T formula retains every word once, including both diagonal orders. In particular, at f-first a7 one has H*=6,Q*=6 and Psi=−84, not−126. This exceptional row is essential and correctly handled.

## 3. R endpoint argument, including all exceptional rows

At held run7, the artificial P_s sums for s0,...,6 are correctly48,82,68,14,−72,−182,−308. For s≤3 their slopes in run are nonpositive and their run7 values positive. The change in an R column replaces the artificial a0 value48 by L, hence adds ell=L−48, namely40 or24.

When S≥4, direct addition at n1,...,4 gives

    92+46S+ell, 80+36S+ell, 68+18S+ell, 64−8S+ell.

All are positive on both stated rectangles. For S≤3, these early formulas and the positive P_S+ell beyond S show monotone increase throughout R.

For S4, n5 has value−16+ell>0, and n≥6 gives−72+ell<0. For S≥5, n5 is76−42S+ell<0. At n6, the row-present value is112−84S+ell<0; if absent, P_S(7)+ell is negative. At n7 in A the row is absent and the same negative bound applies. In B with S7, the column equals P6(7)+Psi(7,7)+ell=−308−84+24=−368, and the new c-first row contributes another−84, giving−452. At n8,S7 only the−368 column remains. For S≤6, later columns are P_S(7)+ell<0.

Thus each R sequence increases throughout or increases then decreases; its minimum lies at0 or the cap9/8. The lower endpoint is128+48S in A,122+57S in B. No unverified internal minimum remains.

## 4. Upper endpoints, reconstructed arithmetic

For A, U0=80+9*88+48=920. At s1,...,6 the added f-first row uses sum h*=49−s(s+1)/2 and the c-first prefix includes G0=48. The resulting cubic is exactly

    822−(1304/3)s+44s²−(4/3)s³.

Its values are430,118,−122,−298,−418,−490; its adjacent differences are−4(s−7)(s−14)<0 for s1,...,5. Hence U is concave and U6=140, giving U≥140. Together with the lower endpoint this proves T≥128.

For B, V0=65+8*72+57=698. The analogous row uses42−s(s+1)/2 and the c-first zero value57 instead of48. For s1,...,6 this gives

    741−(1124/3)s+40s²−(4/3)s³,

with values405,141,−59,−203,−299,−355 and differences−4(s−7)(s−12)<0. Thus V≥328 through S6, with V6=328. At s7 the two f-first terms are−84 each. The c-first prefix is57+46+36+18−8−42−84−84=−61. The final change is−229 and V7=99. No unjustified concavity across this last step is used. Together with the R0 endpoint this proves T≥99.

All these are consequences of the displayed exact sums and analytic sign arguments, not acceptance of a diagnostic positivity table.

## 5. Original full-margin summation

Each genuine gamma fiber has total original full-margin kernel at least128 or99, and W≤77 or80. Its mean is therefore at least128/77 or99/80. Weighting by each actual fiber cardinality and summing yields exactly the two claimed bounds for3K−N. The original2X+Y has been consumed in the axis terms and is not added again. No moment is imposed, transferred or averaged across fibers. The inherited original upper cap5/9 completes strict balance for the specified pair in the two typed gates.

## 6. Ordinary-existence stitching

I also read the reviewed OP1, SG1 and RG1 statements and use their already accepted conclusions, along with RC1 and the earlier at-least-two-frontier closure, as dependencies rather than claiming new independent audits of all those proofs.

For a unique x-containing C-minimum c, RC1 pays unless some missing-x support≤1 minimum exists. The four possible signatures of c are x,xy,xz,xyz.

- Signature x is paid by SG1 (or RC1 in the absent-low-minimum alternative).
- Signature xy/xz with an empty minimum is paid by SG1; with an opposite singleton minimum it is paid by SP1-B.
- Signature full with an empty minimum is paid by SP1-A.
- In the remaining no-empty branches, opposite singleton minima are paid by OP1. If only one singleton type occurs and it shares a root with c, that root is below every C-minimum, hence below all C. Its upper set equals U(b)=C, and its private lower difference from b is {a}; this is an original dual-VG configuration. The case of no singleton minimum is already RC1. These cases exhaust full c and the same-root alternatives for nonfull c.

Thus no unique-frontier branch remains. Combining with the accepted closure for at least two frontiers gives ordinary balance whenever an actual x-containing C-minimum exists. The proof of this ordinary conclusion includes bank/old-guard alternatives; it does not imply a uniform fixed-(u,b) theorem across all those alternatives. Repeated-low-minimum restrictions in RG1 are consistent but not needed to strengthen this direct case exhaustion.

No zero-frontier cell is closed by this stitching, and no screened residual is asserted realizable. This is neither an NB result nor a net-new-population or full-B1 claim. No external repository was modified.
