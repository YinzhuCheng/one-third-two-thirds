# HF1 and LS1: heterogeneous frontier payment and low-support budgets

Date: 2026-11-10 UTC. Author candidate for uninvolved audit. Uses the exact original B1 lift, actual Delta10, m<=k<=7, and the corrected MF1 kernel/FKG mechanism. No OLD seed moment is needed for HF1 or the degree lemmas. No original-object scan or LE DP was used.

## HF1: two x-minima with only one degree slack

Suppose c,d are two distinct C-minimal labels strictly above x. If deg_C(c)<=9 and deg_C(d)<=10, then

    3K-N >= (22/27)e(C)+2X+Y >0

for m>=1. For m0 use the separate bound48e(C)+2X+Y. Thus the original fixed pair is strictly above1/3 and at most5/9 without OLD moment.

### Exact fibers and heterogeneous stochastic comparison

Delete c,d, fix an actual retained word gamma, and fix their order pi. Each point is incomparable with the other selected minimum. Its deadline is therefore bounded by its original C-degree minus1. The two deadlines have upper bounds8 and9. As in MF1, pad a short gamma formally to length9 if needed; actual deadlines remain at most its original length, so this does not change any real fiber.

Represent positions by gaps0<=g1<=g2<=9; equivalently strictly increasing positions s1=g1+1,s2=g2+2. If the lower-degree point comes first, the baseline feasible lattice has g1<=8,g2<=9. If it comes second, the baseline has g1<=9,g2<=8, equivalently0<=g1<=g2<=8. Each baseline set is closed under componentwise meet and join, hence a finite distributive lattice. Uniform mass is log-supermodular. Further conditioning on the actual coordinate deadline constraints is a decreasing event in that baseline lattice. FKG thus makes the first gap H=g1 stochastically no larger than the baseline H. This is the same argument as MF1 but starting from the heterogeneous cap sublattice, not the unrestricted r-subset lattice.

For m>=1 the actual kernel is bounded below by G_(m,k)(H), and monotonicity in m,k bounds this below by G_(7,7)(H). Here

    G_(7,7)(t)=48+2h-4h^2, h=min(t,7),
    values at t0,...,8: 48,46,36,18,-8,-42,-84,-134,-134.

These first-gap functions are nonincreasing, so the stochastic comparison has the required direction. When the lower-degree point is first, fixing H=t leaves10-t choices for the second gap, t0,...,8. Thus the baseline average is

    [sum_(t=0)^8 (10-t)G_(7,7)(t)] / [sum_(t=0)^8 (10-t)]
       =44/54=22/27.

When it is second, fixing H=t leaves9-t choices, t0,...,8. Its average is298/45, the already-known B(2,9;7,7). Therefore every actual gamma/pi fiber has average F at least22/27. Multiplying each actual fiber cardinality and summing gives HF1 from the exact full-event identity. No relative weighting of the two selected orders is assumed; each order is paid separately. Same-gap selected orders are different fibers, with their true multiplicities retained.

This uses only two closed finite sums evaluating an analytic formula, not a search over posets or a computer-assisted certificate.

## Consequence for the unpaid frontier

Combined with the earlier three-x-minimum and one-degree<=6 gates, any still-unpaid object can have at most two x-containing C-minima. Each has C-degree>=7. If there are two, HF1 forces BOTH C-degrees to equal10. Actual Delta10 then forces both signatures to be full xyz: an x-containing label lies above u,a,b, and each missing T root would consume a further degree outside C. This strengthens the previous necessary condition that merely one of the two was full and saturated.

This is a necessary condition for escaping these fixed-pair sufficient gates, not a claim that such residual objects exist or fail payment.

## LS1: low-support minimal-point budgets

Let v be a C-minimum with T-signature of size at most1. It is outside E. It is incomparable with all E: v cannot be below an E point because E is an ideal, and an E point cannot be below v because v is minimal. It lies above u in the lift, and its outside-C incomparable neighbors are exactly its missing T roots. Hence

    deg_C(v)<=7+|signature(v)|.

If v does not contain x, then v belongs to Mx minus E, so k>=m+1. Still assuming v does not contain x, if there are r x-containing C-minima, v is incomparable with all r, because they are distinct C-minima. Thus

    m+r <=7+|signature(v)|,

and the number of its additional incomparable C labels outside E and those r minima is at most7+|signature(v)|-m-r. If v instead contains x, it is itself among those r minima, so the corresponding general bound is m+r-1<=7+|signature(v)|. Uniformly the left side is m+r-1_(x in signature(v)). These are budgets on the original full object, not synthetic residual degrees.

If k=m, no such v missing x can exist. Every support-at-most1 C-minimum must then have signature exactly{x}. Its C-degree is at most8. HF1 therefore pays any k=m object having this low-support minimum and a second x-containing C-minimum. Accordingly, if an unpaid k=m object has a low-support C-minimum, it must have exactly one x-containing C-minimum, namely this signature{x} point, and that point has C-degree7 or8. It is also the unique support-at-most1 C-minimum, since any second would itself be x-containing. This conclusion does not assume simultaneous realizability of the unpaid constraints.

For m>=6, a signature-empty C-minimum allows at most7-m x-containing minima; a signature-y or signature-z minimum allows at most8-m, additionally requiring k>=m+1. These inequalities may be combined with CB3 on A,B, but they alone do not force a contradiction or transfer the OLD moment. A low-signature minimum can lie below many other non-E labels; those labels need not all be incomparable with it. Treating them all as blockers would be an invalid stronger route.

## Status and scope

HF1 is a new analytic sufficient fixed-pair gate awaiting independent audit. LS1 consists of elementary necessary original-degree consequences, also submitted for audit. This does not show the remaining contract is nonempty, does not infer a whole-object counterexample from a negative profile, and does not claim new ordinary balanced-pair population beyond existing twin/VG guards. The old-moment-failure and A0+A1>7e(C) assumptions are not needed in these lemmas; their role, if established separately, is to supply the low-support minimum to which LS1 applies.
