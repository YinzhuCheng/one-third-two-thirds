# Independent analytic audit of RC1

2026-11-10. **PASS.** Source `ROOT_COVER_IDEAL_BANK_CLOSURE.md`, SHA256
`13f650fbbad5e963ca9d262d2231e8400d6decc4f365bb3b6b0f64497c3552b8`.

I did not participate in RC1's derivation. I independently checked its ideal, original degree, word counting, stochastic bound, small-cell stitching and control. This is internal independent review, not external peer review or formal verification. No object enumeration, LE DP or computational certificate was used.

## 1. Ideal and original degree

M=C−U(x) is a C ideal: t<s with x<t would imply x<s. All its labels have yz signature by hypothesis. Each is incomparable with x in the full original lift; an E label is additionally incomparable with u. Thus the original C-degree is at most9 (at most8 for E). Every gamma label before the first gamma successor of a fixed M label is incomparable with it, because an ideal has no predecessor outside itself. Therefore its insertion deadline really is at most9. This argument does not inherit degrees or moments from a deleted object.

Every C label has nonempty signature, so A0=0. No C label can have sole predecessor root y or sole predecessor root z: it either contains x or contains both y,z. Hence an old word with private prefix exactly one must begin with x.

## 2. Original K1 kernel

Fix beta in LE(C). Place x first, then place y,z in gaps after at least one C label and before their respective first successors. The allowed positive gaps have counts h_y and h_z. Unequal gaps specify their order uniquely; equal gaps allow two orders, producing

    a1(beta)=h_y h_z+min(h_y,h_z).

For k≥1, the first M label is above both y,z. Thus h_y,h_z≤H, where H counts beta labels before the first M label, and a1≤H(H+1). If beta starts in M, both h_y,h_z are zero, consistently. These are literal complete old-R-word fibers, not assumed independent choices with a changed weighting.

## 3. Inserting a non-antichain ideal

Fix actual tau in LE(M) and gamma in LE(C−M). Their interleavings uniquely parametrize the beta words in this fiber. All internal M comparisons are already respected by tau. The remaining necessary and sufficient restrictions are that each M letter occur no later than its first gamma successor, equivalently coordinate upper bounds on its gamma gap. This remains correct if an M successor in tau has an earlier deadline: increasing selected positions plus all individual deadlines automatically enforce the requisite earlier placements.

Every deadline is at most9. A fixed gamma suffix beyond its first9 letters comes after all M labels; when gamma is shorter, padding creates no choices because all original deadlines remain bounded by its actual length. Consequently the feasible interleavings are precisely a nonempty decreasing subset of the distributive lattice of k-subsets of9+k positions. All-M-first is feasible.

Uniform FKG association implies that an increasing function of the first selected gap has conditional mean no greater on this decreasing subset than on the whole lattice. Applying it to H(H+1) is valid even with unequal deadlines and arbitrary internal M order. It does not require M to be an antichain or infer independence after conditioning.

For the unrestricted first gap H0, the negative-hypergeometric factorial moments are

    EH0=9/(k+1),
    E[H0(H0−1)]=2*9*8/((k+1)(k+2)).

Adding twice the mean gives18(k+10)/((k+1)(k+2)). The same bound applies to each actual tau/gamma fiber. Weighting it by that fiber's actual size and summing proves the claimed A1/e(C) inequality. No moment is used.

## 4. Payment, small cells and residual inference

The rational function decreases for k≥1: its derivative has numerator −18(k²+20k+28). At k5 its value is45/7. For k≥5, the already independently reviewed original bank gate yields

    S−N≥14e(C)−2A1≥(8/7)e(C)>0.

The individual candidate upper bounds, not a mean upper bound, ensure that one physical bank member is strictly balanced.

For k≤3 the scalar Phi region includes every feasible m; at k4 it includes m≤3, allowing the closed m3 endpoint, and DG1 covers m=k4. At k0, F≥48 is the separate direct bound. These are ordinary-balance statements of the strength actually needed, without claiming all small-cell lower inequalities strict.

The consequence about missing-x low-support minima is valid. Every M label has an M-minimum below it, and minimal elements of the ideal M are C-minima. If every such minimum has support at least2, its signature is yz, and all M labels inherit yz. Therefore RC1 applies. In fact this inference does not need the number of x-containing minima to be at most one; restricting it to the already reduced zero/one-frontier domain is sound. A surviving unpaid object must have a missing-x C-minimum of support at most1. This remains only a necessary condition, not proof of an unpaid population.

## 5. Actual controls and scope

The seven-chain M parallel to the six-chain of x-only labels has k7,m6 with E the first six M labels. Full original degrees check exactly: a1,b5,x10,u9,y=z10, each E point8, last M point7, each V point9. The x-containing C-minimum has C-degree7, and E is a genuine ideal.

Uniform shuffling of chains gives mean initial M run7/(6+1)=1 and mean initial V run6/(7+1)=3/4. Thus A2/e(C)=2(1+3/4+3/4)=5 and A3/e(C)=6. Here h_y=h_z=H, the initial V run. Its factorial second moment is2*6*5/(8*9)=5/6, so A1/e(C)=5/6+2*(3/4)=7/3. The OLD margin is consequently −11/3 times e(C), as claimed. TB2 does not apply because of the x-only minimum; y,z nevertheless remain true full twins. These checks establish separation of hypotheses, not net-new ordinary coverage.

The general m≤k chain-plus-full-two-chain family also has the asserted actual maximum degree max(k+3,5) and valid initial E ideal. No object is asserted outside all previous guards.

RC1 is a valid analytic whole-ideal version of the root-cover counting mechanism. It does not imply unrestricted B1, a fixed-(u,b) guarantee for its whole class, or balanced-pair inheritance from an arbitrary induced order. No additional computational dependency is introduced.
