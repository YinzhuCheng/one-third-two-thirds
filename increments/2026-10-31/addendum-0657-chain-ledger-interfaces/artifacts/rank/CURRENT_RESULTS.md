# A-side signed-defect research: current result pointer

Status: the base rank-budget proof and deadline-collision correction have passed the parent-arranged independent review; see the audit files beside these notes. The late-c2 partial injection was independently reviewed by the parent and additionally checked word by word on the alpha2/beta2 witness. These are internal research results, not a priority claim or complete C2 solution. Only `/tmp` was modified in this subtask.

## 1. Structural partial cancellation
For any finite C2 with A\U(d)={s} and U(s) subset U(e), swapping (c1,d),(s,e) bijects
  E_L={v<c1<s<d and some r in A intersect U(e) precedes c2}
to the explicitly characterized G_A subset of the reverse bad event G. It does not require e<F or b incomparable s. The exact residual ledger is
  2p_d=1+q0+Pr(E_A^early union E_F)-Pr(G\G_A).
Full proof: `A_LATE_PARTIAL_INJECTION.md`. This is partial compensation, not universal control of the residual mass.

## 2. T13 extension: rank budgets, with first-target collision correction
Retain the T13 lower gate: A\U(d)={s}, b<s, e<F. Put R=A intersect U(e), k=|A\({s} union R)|. Let
  alpha=min_{f in F}|D(f) intersect R|,
  beta=min_{u in U(s)}|D(u) intersect R|,
with an empty target set assigned |R|; require alpha,beta>=1. The R predecessors may differ from target to target. No fixed/common anchor set is required.

Define
  Phi(H)=2H^2+(7-2alpha)H-4alpha beta-4min(alpha,beta)
         -4alpha * 1_{alpha<beta}.
If max(Phi(1),Phi(k+1))<=0, then p_d<=(1+q0)/2. If both values are negative, the inequality is strict. This gives the inherited fixed-menu conclusion with the usual C2 basic bounds. There is no global degree or size assumption.

Read `RANK_BUDGET_PROOF.md` for the full common fiber identity and rank step, then `RANK_COLLISION_ADDENDUM.md` for the correction. The corrected endpoint criterion **replaces** the uncorrected hypothesis 4; it is not an extra simultaneous assumption. The old T13 common-anchor theorem is subsumed, not counted again as a separate result. The independently reviewed worst-fiber bound is attainable; attainment does not imply a global probability counterexample.

## 3. Two finite separating witnesses
These verify applicability/nonredundancy only, not the general proof or literature priority.

| File | alpha,beta,k | Common anchors | N | R0 | K=#(c1<d) | E | G |
|---|---:|---:|---:|---:|---:|---:|---:|
| candidate.json | 2,2,1 | 1 | 117501 | 33398 | 69853 | 1750 | 12943 |
| sharp_rank_witness.json | 1,3,1 | 0 | 168366 | 49873 | 104621 | 2690 | 11687 |

Both have |A|=5, Delta=9, no primal/dual very-good pair, no S112 mixed cycle, and no proper nontrivial autonomous module. The second also defeats the *uncorrected rank criterion* Phi_old(2)=2, while its corrected endpoints are -13,-2. Neither defeats the old unsigned **numerical** error budget; the structural theorem avoids counting that budget separately for each instance.

Run `python check.py candidate.json` and `python check.py sharp_rank_witness.json`. `check_injection.py` independently enumerates all 117501 words of the first witness and verifies the 680-source/680-image bijection and exact target characterization.

## Boundaries
- No claim of complete C2, maximum-degree-9, or general 1/3–2/3 closure.
- The partial injection is not a bound on all unmatched error.
- No claim every older tool fails on the witnesses; historical and literature overlap remain unverified.
- `collision_candidate*.json` are development trials; only number 7 equals the final sharp witness. Earlier failed trials must not be used as nonredundancy evidence.
