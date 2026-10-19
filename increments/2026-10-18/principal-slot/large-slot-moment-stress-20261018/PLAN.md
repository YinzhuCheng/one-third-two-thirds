# Fixed large-parameter exact stress plan

Recorded before executing the experiment, 2026-10-18 UTC.

Scope: only the two currently unproved actual uniform-LE slot-moment candidates T and C. This is neither a proof nor a test of the original global conjecture. Do not modify the earlier 35/55 material or the small batch.

Definitions: U is a union of 2 or 3 explicitly given chains, optionally joined by cross-chain relations. A legal filter is the complement of an actual ideal. R_S counts the elements strictly before the first S element in a uniform complete LE; R_empty=n. r=E R_y, s=E R_z.

Targets:
T: E[R_y R_z+min(R_y,R_z)] <= r s + min(r^2+2r,s^2+2s).
C: Cov(R_y,R_z) <= min(r(r+1),s(s+1)).

Fixed object seed: 2026101801. Fixed filter/pair seed: 2026101802.

Objects, without an ascending small-n sweep:
- Eleven disjoint two-chain objects with chain lengths (1,19), (1,49), (1,99), (1,199), (2,198), (5,195), (20,180), (50,150), (100,100), (10,40), (20,20).
- Ten disjoint three-chain objects with lengths (1,1,18), (1,1,198), (1,9,190), (2,18,180), (10,10,180), (20,60,120), (66,67,67), (10,10,10), (20,20,20), (30,30,30).
- Twelve joined-chain objects: width 2 on (20,180) with one gate, two opposing gates, or 14 fixed-seed random cross-relations; width 2 on (100,100) with one gate, a common middle barrier, or 20 random cross-relations; width 3 on each of (10,10,180), (20,60,120), (66,67,67) with a middle barrier or 20 random cross-relations.
Total: 33 objects, n=20..200. Chain decomposition gives the ideal grid; no 2^n subset enumeration.

Filter selection: at most 112 distinct legal filters per U, using extremal ideals, principal filters, single-chain suffix filters when legal, structured nested rays, and a fixed-seed sample of remaining ideals. Empty/full filters are retained as degenerate checks. Filter sampling is not a uniform sample of all legal filters.

Pair selection: all pairs among the candidate pool are scored from exact means. Select a bounded mixture prioritizing positive means with ratio >=10, nested distinct filters, nonnested overlapping filters, disjoint nonempty filters, high-overlap filters, diagonal checks, and random residual pairs. Target pair caps by legal ideal count: <=1,000: 240; <=15,000: 160; <=100,000: 64; otherwise: 16. Selection rules and all chosen filters/pairs will be preserved. This is sampled objects/filters/pairs, not a complete classification.

Hard budget: at most 33 prescribed objects, at most 30,000,000 selected-pair times ideal-state passes, and at most 12 minutes wall time for the executable. Stop immediately on a negative exact numerator for either candidate, or when the budget is reached. Do not append new batches if no counterexample appears.

Algorithm: precompute each legal-ideal DAG and complete-LE prefix/suffix counts with arbitrary-precision integers. For each chosen pair, run reward moment DP over every ideal and edge; first hit gets no reward, empty filters get all n rewards. Accumulate first moments, product, min, and both squares. No random LE, no Monte Carlo, no floating-point sign test. Report rational gaps and normalized pressure. First independently verify this recurrence against direct LE enumeration and the prior small-batch code on a few small fixtures, before any large case.

Evidence: save complete poset chain lengths/cross-relations, selected filter thresholds, total LE count, all integer moment sums, and exact numerator gaps. A counterexample will include a separate reproducible certificate and joint distribution when feasible; the DP itself remains a reproducible complete-count certificate. With no counterexample, report maximum pressure/minimum normalized gap, extreme mean ratios, budget usage, and sampling bias.
