# OP1: opposite singleton minima pay with their original prefix weight

2026-11-10 UTC. Analytic author candidate, uninvolved review requested. Exact original B1 lift, actual full Delta10,0<=m<=k<=7, no OLD moment.

## Theorem
If C has two C-minimal labels f_y,f_z of complete old signatures y and z respectively, then the ORIGINAL fixed pair(u,b) satisfies

    3K-N>=(79/36)e(C)>0, Pr(u<b)<=5/9.

This consumes original2X+Y inside the proof; it is NOT an F-only bound and no extra prefix credit is added afterward. The constant is conservative, not a sharp probability claim. The selected labels are fixed physical labels, not word-dependent choices.

## 1. Exact single retained word and shared gap weights
Delete f_y,f_z and fix an actual retained gamma. They are incomparable C-minima of original C-degree<=8, so their genuine insertion deadlines R,S are<=7. Do NOT condition on or equalize their relative orders. Let a,b be their respective gaps. Every pair0<=a<=R,0<=b<=S gives one genuine word if a!=b and two if a=b. Thus

    W(R,S)=(R+1)(S+1)+min(R,S)+1<=72.

Let h be gamma's initial missing-x length and q its initial E run. Both removed labels miss x, so h<=k-2<=5, and0<=q<=min(m,h). Their exact restored runs are

    H=h+1_(a<=h)+1_(b<=h), Q=min(q,a,b).

If q0, all actual C words have F>=48 and nonnegative prefix credit, already stronger than the theorem. Hence assume q>=1, so gamma starts with a yz-signature E label and h>=1.

If min(a,b)>=1 the C word starts with E, so hy=hz0 and X/Y kernels vanish. If min(a,b)=0, its first C point is a selected singleton. The opposite missing-root run is EXACTLY1, whether the other selected point shares gap0 or comes later (the first E point then supplies that root). Therefore the two non-x runs are0 and1. The exact original prefix kernels x_beta=hy hz+min(hy,hz), y_beta=Hx hz+min(Hx,hz)+Hx hy+min(Hx,hy) give2x_beta+y_beta=H+1. Thus the ORIGINAL full margin kernel in either selected order is

    B_q(h;a,b)=48+(6-8Q)H+4Q(Q-1)
                 +1_(min(a,b)=0)(H+10).

The9(hy+hz) term and prefix credit have been retained exactly. The kernel is symmetric in a,b because the singleton types are opposite. Increasing q to h only lowers the kernel (positive-Q forward difference8(Q-H)<=0; at min0 it is unchanged). Put B_h=B_q with q=h. It suffices to bound the actual gamma-fiber lower sum

    T_h(R,S)=sum_(a=0)^R sum_(b=0)^S(1+1_(a=b))B_h(h;a,b).

No FKG, independent-coordinate probability, or equal weighting of selected orders is used here. The diagonal factor2 is literal original word multiplicity.

## 2. Uniform bound for1<=h<=4
If a,b>=1, increasing h increases H and Q=min(h,a,b). Since Q>=1, increasing H and then Q lowers the kernel. Thus B_h(h;a,b)>=B_4(4;a,b) for h<=4. If a=b0, H>=3 and the full kernel58+7H is>=79. If exactly one gap is0, H>=2 and the kernel is>=72.

It remains to bound the weighted interior rectangle sum of B_4. Split positive indices into the core1,...,4 and exterior5,...,7.

- Core-core entries depend on i=min(a,b) and equal v_i=(36,-4,-36,-60). For a p-by-q prefix rectangle,0<=p<=q<=4, the weighted core sum is sum_(i=1)^p(p+q-2i+2)v_i. For p0 it is0; for p1 it is36(q+1); for p2 it is32q+72; for p3 it is140-4q; for p4,q4 it is0. Hence every weighted core prefix is nonnegative.
- A core-exterior column has entries(38,6,-18,-34) down its core. Every prefix sum is at least-8 (its cumulative sums are38,44,26,-8). There are at most three exterior columns in each direction, contributing at least-48 in total.
- Exterior-exterior entries are all-8. There are at most3*3 entries and at most3 diagonal extras, contributing at least-96.

Therefore EVERY weighted interior prefix rectangle has sum>=-144. If R,S>=1, the gap-zero rows contribute at least158+72(R+S)>=302, leaving T_h>=158. If either R or S is0, no interior exists and the gap-zero terms already give T_h>=158. This proves the desired bound for h<=4 by explicit closed sums, not a sampled table.

## 3. Bound for h5
For positive core indices1,...,5, the entries depend on i=min(a,b) and are

    v_i=90-60i+4i^2=(34,-14,-54,-86,-110).

For core-exterior indices (one index6/7), they are

    w_i=84-52i+4i^2=(36,-4,-36,-60,-76),

with cumulative sums W_p=(0,36,32,-4,-64,-140), p0,...,5. Exterior-exterior entries equal-42. The gap-zero entries are107 when the other gap<=5 and100 otherwise, including B_5(0,0)=107.

By symmetry assume R<=S. First take R=p,S=q<=5. Then

    T_5(p,q)=214+107(p+q)
               +sum_(i=1)^p(p+q-2i+2)v_i.

For fixed p the q slopes are107+sum_(i=1)^p v_i:107,141,127,73,-13,-123 for p0,...,5. For p<=3, minimum q occurs at q=p. The diagonal value is

    D_p=(p+1)[214+(154/3)p-18p^2+(2/3)p^3].

The bracket is concave on[0,5], since its second derivative is-36+4p<0, and has endpoint values214,104. Thus D_p>=104(p+1)>=312 for p>=2; D0=214 and D1=496. For p4 the negative q slope puts the minimum at q5, with T_5(4,5)=D4-13=857. For p5 only q5 occurs, with D5=624. All core rectangles therefore have T_5>=214.

Next let R=p<=5,S=5+v with v1 or2. The exact sum is

    T_5(p,5+v)=T_5(p,5)+v(100+W_p).

The added slopes are100,136,132,96,36,-40. For p<=4 they are nonnegative; for p5 the minimum is624-80=544. Hence these rectangles also have total>=214.

Finally take R=5+u,S=5+v with1<=u<=v<=2. The exact sum is

    T_5=624-40(u+v)-42[uv+min(u,v)].

It decreases in both u,v, so it is at least its value at2,2, namely212. Thus all h5 fibers have total>=212, which is stronger than158.

## 4. Actual summation
For every actual retained gamma with q>=1, its ORIGINAL full margin sum is>=T_h>=158 and its word count W<=72. Its actual mean is therefore>=79/36. For q0 it is>=48. Multiply by EACH actual gamma-fiber size and sum. The exact original identity3K-N=sum(F+2x_beta+y_beta) proves the theorem. No prefix credit is counted twice and no moment enters.

Small bounded gap diagnostics suggested this proof; the displayed rectangle decomposition and polynomial inequalities are its analytic justification, not a finite computational positivity certificate or an original-poset scan.

## 5. Ordinary consequences and residual boundary
Every actual zero-x-frontier object with no empty-signature C-minimum is ordinary-balanced: all C-minima have signatures y,z,yz. If both singleton types occur OP1 pays fixed u/b. If either singleton type is absent, every C-minimum shares the other root, so every C label lies above it; that root and b have equal original upper set C, with private lower sets{a}/empty, an OLD dual-VG configuration. This does not assert fixed-u/b payment in the dual-VG branch.

Every actual m4k7 object with at least one x-frontier is also ordinary-balanced. At least two frontiers are covered by TL1. For a unique frontier, reviewed RC1/FS1 pay unless c is full C-degree10 and no empty minimum exists. Then every other C-minimum has signature y,z,yz, and the same OP1/common-root dual-VG dichotomy pays. This closes the entire single-frontier m4k7 branch, not the zero-frontier empty-minimum branch.

Consequently the zero-frontier residual still has six parameter cells, but ALL must contain an empty-signature C-minimum. MP1 and LM1 then force a unique low minimum, empty, in m3k7,m4k6,m5k6,m6k7. In m4k7,m5k7 at most two low missing-x minima can remain, including an empty one. Single-frontier residual parameters reduce to m5k7,m6k7.

For a remaining full single frontier in those two cells, no-empty is paid by the same OP1/common-root dichotomy. Thus a full residual frontier must have C-degree10 AND an empty C-minimum (degree<=9 with empty was already SG1B-paid). For a nonfull frontier, its signature is xy or xz, C-degree9, and no empty minimum is allowed by SG1B. OP1 excludes both singleton low types; a same-root singleton type would make that root common to every C-minimum. Therefore only opposite singleton low minima can remain: all z if c has xy, all y if c has xz. These are necessary patterns only, not certified realizability or NB controls.

No object avoiding all original VG/dual-VG/twin guards is constructed here. All claims retain original point degrees, full-word multiplicities and actual tail weights. No LE DP or unrelated computational output occurred.
