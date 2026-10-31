# Optional strengthening: first-target collision correction (draft, pending review)

This strengthens the same T13 rank-budget proof, not a separate mechanism. Retain every hypothesis and definition of `RANK_BUDGET_PROOF.md`, with alpha,beta>=1. In the b-first branch, write
  D(H,I,J)=4HJ+2HI+11H-4IJ-4min(I,J).
If alpha<beta, the preceding proof's extremal point I=H+alpha,J=H+beta cannot occur: the first F letter is not an R letter, and would consume an additional position before the first U(s) letter.

Precisely:
- If I<J, the first F letter lies in positions H,...,J-1 and is outside R. At least beta distinct R predecessors of the first U(s) letter also lie there. Hence J>=H+beta+1. Together with I>=H+alpha and monotonicity,
  D<=D(H,H+alpha,H+beta+1)=f(H)-4alpha.
  This remains true if U(s) is empty: J is the final sentinel, all R lie before it, and the first F letter is an additional non-R letter. If F is empty, I is the final sentinel and the branch I<J is impossible.
- If I>=J, then I,J>=H+beta. Monotonicity gives
  D<=D(H,H+beta,H+beta)=f_beta,beta(H).
  For delta=beta-alpha>=1,
  [f_alpha,beta(H)-4alpha]-f_beta,beta(H)
    =delta(2H+4beta+4)-4alpha
    >=2H+8>0,
  where the final inequality is minimized at delta=1, beta=alpha+1. Thus this branch has an even smaller upper bound.

Consequently replace f in the endpoint criterion by
  f_sharp(H)=2H^2+(7-2alpha)H-4alpha beta-4min(alpha,beta)
             -4alpha * 1_{alpha<beta}.
No improvement is claimed for alpha>=beta, where the original extremal deadline assignment can be feasible. The corrected polynomial remains convex in H, so only endpoints H=1,k+1 are needed.

For A5,k=1,alpha=1,beta=3, the uncorrected endpoint f(2)=2 is inconclusive, but f_sharp(1)=-13 and f_sharp(2)=-2 prove the strict menu upper bound. The other useful pairs (2,2),(3,1) remain covered.

Finite applicability note: two trial alpha1/beta3 configurations were checked (`collision_candidate*.json`); they contain old VG/mixed structures. They are not nonredundancy witnesses and must not be presented as such. The independent rank2/rank2 witness remains the verified nonredundancy example for the broader rank mechanism. No exhaustive claim is made that alpha1/beta3 is either new global coverage or entirely old-filter redundant.
