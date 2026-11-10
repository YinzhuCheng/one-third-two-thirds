# OP1 independent mathematical review

Date: 2026-11-10 UTC. Reviewer: audit_alpha2_four, not involved in OP1's original opposite-signature rectangle derivation.

**PASS.** Reviewed source `OPPOSITE_SINGLETON_MINIMA_ORIGINAL_WEIGHT_CLOSURE.md`, SHA256 `10995bc6b2d5e5f1eeed58dbbfc672f9d07e0d3f458b9688a27cabe0adc0e55d`, independently verified. The conservative full-margin bound79/36 is valid. No sharp53/18 claim is needed or accepted as a proof dependency.

## Genuine rectangle and exact prefix credit

The two opposite singleton C-minima each have two missing T-root neighbors outside C, so their original C-degree is at most8. Charging the other selected minimum leaves actual deadlines R,S<=7. Since both are C-minimal, there are no retained predecessors; each assigned pair of allowed gaps reconstructs one original word off the diagonal and two on the diagonal. Thus W=(R+1)(S+1)+min(R,S)+1<=72 is exact. No independent-coordinate probability or equal weighting of selected orders is imposed.

Both removed points miss x, so retained h<=k-2<=5, with exact restored H=h+1_(a<=h)+1_(b<=h). Both lie outside E, giving Q=min(q,a,b). If q0 this remains zero for every insertion, so the original F>=48 and prefix credits are nonnegative. If q>=1, gamma begins with an E point of signature yz. For min(a,b)>=1 the restored word also starts in E, giving hy=hz0. For min(a,b)=0 it starts in one singleton; the other missing-root run is exactly1, stopped either by the opposite singleton in the same gap or by gamma's first E point. The non-x runs are therefore0,1 in some order. The exact prefix kernels give x_beta0 and y_beta=H+1, while9(hy+hz)=9. Thus the added full-kernel contribution is exactly H+10, including both equal-gap orders. This is not extra credit added a second time after summation.

Raising retained q to h only raises Q toward H and lowers the polynomial kernel, because its forward Q difference is8(Q-H)<=0. The indicator credit is unaffected. This proves the displayed B_h lower kernel for the complete original margin, not for F alone.

## Uniform h1 through4 bound

On positive gaps, increasing h increases both H and Q. Raising H first and then Q is a valid decreasing comparison since Q>=1 and Q<=H, so B_h>=B_4. At gap(0,0), H>=3 and the full kernel58+7H is at least79; on either zero axis away from the origin H>=2 gives at least72. Diagonal multiplicity makes the origin contribution at least158.

For B_4 the positive core entries36,-4,-36,-60 are obtained with H6 and Q=min(a,b). In a p-by-q core prefix with p<=q, counting minimum index i and its diagonal extra gives precisely p+q-2i+2 copies. Independent expansion yields0,36(q+1),32q+72,140-4q, and0 for the five p cases listed. Each is nonnegative on its permitted range. The core/exterior column values38,6,-18,-34 have prefix sums38,44,26,-8. There are at most three columns in each direction, hence at least-48 in total. The exterior square has at most nine cells and three diagonal extras, each-8, so is at least-96. These pieces partition every actual positive prefix rectangle, including rectangles with a short or empty core side.

Thus the positive interior contributes at least-144. When both R,S are positive, the zero axes contribute at least158+72(R+S)>=302, leaving at least158. If either deadline is zero there is no positive interior, and the origin alone gives158. This proves the complete h<=4 rectangle bound analytically.

## h5 bound

Direct substitution gives the claimed core values34,-14,-54,-86,-110, mixed-column values36,-4,-36,-60,-76, and exterior value-42. The zero-axis values are107 when the other index is at most5 and100 afterward; in particular the doubled origin is214.

For core p<=q<=5, the given minimum-index sum has q slope107 plus the prefix sum of v, yielding107,141,127,73,-13,-123. Thus p<=3 reduces to q=p, p4 to q5, and p5 already has q5. Independent expansion of the diagonal sum gives D_p=(p+1)[214+(154/3)p-18p^2+(2/3)p^3]. The bracket has negative second derivative throughout[0,5] and endpoint values214,104. This gives the claimed adequate bound for p2,3; D0=214 and D1=496 are exact. D4=870, so the p4,q5 endpoint is857; D5=624. Hence every core rectangle is at least214.

Adding v exterior columns to a p-by-five core adds exactly v(100+W_p), with slopes100,136,132,96,36,-40. No diagonal extra occurs in a mixed rectangle. For p5 the two-column minimum is544; other p values only increase. If both dimensions enter the exterior, each strip contributes-40 per new index and the exterior square contributes-42[uv+min(u,v)], including its diagonal extras. The exact expression624-40(u+v)-42[uv+min(u,v)] decreases to212 at u=v=2. These cases exhaust R,S0,...,7 by symmetry, so every h5 fiber is at least212, stronger than158.

The proof therefore uses closed rectangle decompositions and polynomial signs, not an empirical minimum from diagnostic gaps.

## Actual summation and ordinary consequences

Every q>=1 gamma fiber has full margin sum at least158 and actual size at most72, yielding mean79/36. The q0 fibers have mean at least48. Summation uses each actual gamma cardinality, proving3K-N>=(79/36)e(C). Prefix credit is already included; no additional2X+Y may be appended. The original5/9 cap completes fixed-pair balance.

For a zero-x-frontier object without empty minima, C-minima have signatures y,z,yz. Both singleton types give OP1; absence of one type gives a root lying below every C point. That root and b have equal full upper set C and private lower differences{a}/empty, a genuine original dual-VG. This establishes ordinary existence, not necessarily fixed-u/b balance in the dual-VG branch.

For m4,k7 with a frontier, the imported TL1/RC1/FS1 gates leave only the single full degree10 no-empty case. All other C-minima then again have signatures y,z,yz, and the full minimum contains both y,z. The same OP1/common-root dichotomy therefore closes that single-frontier sector. The empty-minimum zero-frontier branch is not included.

The residual patterns stated in the manuscript are consistent with the earlier reviewed gates: all zero-frontier residual cells require an empty minimum; MP1 and cardinality/LM1 restrictions give the claimed unique-empty versus at-most-two counts. The single-frontier cells remaining are m5,k7 and m6,k7. A full surviving frontier must have an empty minimum and degree10, while a nonfull surviving frontier must have signature xy/xz and degree9, with no empty minimum. Opposite singleton types together invoke OP1, and a singleton matching the frontier's existing root gives common-root dual-VG if no opposite type exists. Thus only the stated opposite-type low minima may remain. These are necessary conditions, not proof of simultaneous realizability or NB.

No gap found. This is an internal independent audit, not external peer review or formal verification. No OLD moment, original-poset enumeration, LE DP, free tail weights, external modification, sharp diagnostic claim, or new ordinary-population credit is used.
