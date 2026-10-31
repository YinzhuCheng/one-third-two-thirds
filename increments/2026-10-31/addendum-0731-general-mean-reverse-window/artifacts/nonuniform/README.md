# Stage 4: the actual nonuniform-window obstruction

Only `/tmp` was written. Main proof file: `REVERSE_CRITICAL_WINDOW_LEMMA.md` (submitted for independent review). This is a reverse application of the familiar critical-pair interval comparison, with a retained common cutoff and an explicit lower-gap certificate; it is not claimed as an unrelated original theorem.

## Established by the draft derivation
For M={m}, if some a in L satisfies D_Q(a) subset D_Q(m), U_Q(m) subset U_Q(a), and a incomparable m, then B>=Z for the genuine shared-cutoff first-hit targets. Strictness needs an explicit surviving-cutoff condition, supplied in the paper.

In the exact 15-point residual, a=a1,m=f0 give real intervals
  a1:[d,min(a4,f2)], f0:[e,f2], cutoff f1,
and retained relations force d<e<min(a4,f2) and e<f1. Every nondegenerate external fiber has a strictly positive reverse expected gap. A quantitative part of that gap yields
  B-Z >= e(Q_gap)=699 > 568,
where 568 is the previously verified menu allowance. The 12-point Q_gap has a paper count 420+279 and a standalone DP verification `verify_gap.py`. This structurally explains why the e/f0 versus a1 mismatch cannot support the old bridge/menu, without recomputing the original B=12891,Z=9101 table.

## Important limits
- This does not rule out other balanced pairs or all nonuniform-window techniques.
- The Q comparison does not lift unchanged to original P. In P, p(a1<f0)=144124/201453>2/3.
- A shifted lower endpoint destroys the old mean-only truncated comparison: even Beta(2,1) versus Uniform[1/4,1] has larger full mean but fails at cutoff 1/4.
- `NONUNIFORM_WINDOW_BOUNDARY.md` gives an exact cutoff-aware shifted-Beta criterion instead of making that false extension.
- Reselecting M must preserve BOTH first-hit targets. Here their minimal frontiers are {f0,f1} and {a1,a2,f1}; f1 is genuinely shared and cannot simply be moved out of C.

## Files
- `REVERSE_CRITICAL_WINDOW_LEMMA.md`: full general and instance proofs, cutoff/weight/strictness details, 699 calculation, smallest three-point warning.
- `LOWER_GAP_WITNESS.json`: complete 12-point generating relations and expected count.
- `verify_gap.py`: exact independent-to-paper DP count.
- `NONUNIFORM_WINDOW_BOUNDARY.md`: mean trap, exact shifted-window condition, safe first-frontier reduction and deletion-measure warning.

Independent review status should be updated only on receipt of the parent's actual audit; the author derivation and the small exact checks alone are not labeled an external review.
