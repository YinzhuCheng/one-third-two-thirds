# Optional strengthening: first-target collision correction (draft, pending review)

This strengthens the same T13 rank-budget proof, not a separate mechanism. Retain structural hypotheses 1–3 and the definitions of `RANK_BUDGET_PROOF.md`, with alpha,beta>=1; replace the original endpoint hypothesis 4 by the corrected endpoint test below. In the b-first branch, write
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

## Exact nonredundancy witness, limited to the named filters

`sharp_rank_witness.json` (same relations as `collision_candidate7.json`) has 15 points and is reproducible with `python check.py sharp_rank_witness.json`.
- C2, A5, Delta9; R={r,t,u} is an antichain; K={w}.
- The R lower signatures outside the common core are respectively empty, {w}, and {b,w}. The two F points outside U(s) have R predecessor signatures {r,u} and {t}; every U(s) target has all three R predecessors.
- alpha=1,beta=3 and there is no common R anchor below all F. Old T13 common-anchor hypotheses fail, and the uncorrected independent-rank endpoint f(2)=2 is inconclusive. The corrected f_sharp endpoints are -13 and -2.
- The exact structural check finds no primal/dual very-good pair, an acyclic S112 mixed graph, and no proper nontrivial autonomous module.
- N=168366, R0=49873, Kcount=104621, E=2690, G=11687, E-G=-8997. The partial late-c2 cancellation matches 908 words, leaving 1782 A-error words.
The unsigned numerical budget does hold here: E=2690 < N/3-R0=6249. Thus the structural proof replaces per-instance error counting; do not claim every existing tool fails. Trial candidates 1 through 6 failed old static filters and are not used as evidence of nonredundancy. Historical/literature priority remains unchecked.
