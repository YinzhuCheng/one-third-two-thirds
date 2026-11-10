# One falsifiable structural conjecture, not a theorem

## Adjacent-bank replacement conjecture (restricted D9/D10 marked-state version)

Let Q be an actual marked ideal of a finite poset with the two-fork singleton-private-root contract of Fathi v22 §24.4.1, with Q containing original a,b,u,v and preserving every previously exposed label. Let J be the actual set of exhausted pivots: every original exterior label is above every J label. Fix a candidate reference extension T of Q. For a degree budget D in {9,10}, use the same necessary upper-deadline domain as the proof: order-monotone h_x between 0 and D-deg_Q(x), h_a=h_J=0, min(h_b,h_u,h_v)=0, and at most D positive caps; add h_p=0 only for a terminal-row claim.

For a deadline vector h, let N(h) count the actual marked-gap placements, and K_xy(h) count placements with the reverse comparison y before x, where x is before y in T. The conjecture is the following conditional replacement statement:

If there is any nonnegative vector w on all reverse incomparable comparisons such that, for every h in the stated domain,

3 sum w_xy K_xy(h) >= (sum w_xy) N(h),

with sum w_xy>0, then there is such a vector supported only on pairs adjacent in T (and incomparable in Q).

This says adjacency loses no separation power when a bank already exists. It does NOT claim every state has a bank, does NOT claim the D10 tree terminates, and does NOT infer global balance from a profile-specific choice of weights. The vector must be fixed across all h in that state.

## Evidence and reasons for caution

The complete supplied v-first D9 two-fork tree contains 3469 bank occurrences. Its original 3456 already have adjacent-only support. The remaining 13 have explicit adjacent-only replacements, checked over all 55987 applicable profiles with the original exact integer replay. This establishes the conditional statement only for these supplied finite states, subject to the original state/verifier contracts.

No generator-independence claim is made. The data may reflect the author's optimization choices. The full conjecture over all possible actual marked states, and especially D10, remains untested. Outside this restricted class, knowing one nonadjacent inversion has mass at least1/3 does not force any adjacent inversion to reach1/3: the nonadjacent event can be covered by a union of several small adjacent inversions. Thus arbitrary probability-law arguments cannot prove the conjecture.

## Minimal decisive test

Do not enlarge the whole D9 replay. On the first genuinely unresolved D10 memory state, compare the exact separation cones for (a) all reverse pairs and (b) adjacent reverse pairs under exactly the same h-domain. If all-pair feasibility holds and adjacent feasibility fails, retain the exact dual mixture as a counterexample to this conjecture; then identify which actual realization constraint excludes or permits the mixture. If both are feasible, inspect a sparse adjacent solution for an injection/path-cut proof rather than simply adding it as another table row.

## Proven analytic primitive already obtained

The exact antichain-prefix path-cut identity in FOUR_EVENT_STEM_ANTICHAIN.md is a genuine parameter-uniform mechanism: for a selected subset K on an h-label path, its conditional adjacent-inversion lower charge is

C(K)=(|K|+number_of_selected_runs)/2-1[first_label_selected].

The earliest contiguous prefix is extremal. This yields a four-event analytic compression of the paper's explicit stem2/four-antichain-tail example, with no degree or exterior-size restriction. General tails are not antichains, so their internal comparisons need not contribute1/2; that missing exchange symmetry is the precise obstacle to automatic extension.
