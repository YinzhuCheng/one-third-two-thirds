# S104 publication checks

These checks establish the reproduced finite counts and publication contents. They do not replace analytical proof, external mathematical review, or the stated source assumptions.

## Checks actually rerun on the publication copy

- `python check_joint_square.py`: PASS, 406 naturally labelled posets, 1828 eligible incomparable pairs; all complete extension orders enumerated exactly.
- `python check_joint_conditioning_independent.py`: PASS, independent closure/extension-set verification on 406 posets and 2126 structural pairs, including 1828 neutral-chain pairs; six-point and rational relaxation examples exact.
- `python half_search/verify_counterexample.py`: PASS for the n=20 HALF example, E=13665 and all five counts, via full extension enumeration, event-added ideal DP and exact insertion fibers.
- `python half_search/verify_counterexample.py SMALLER_COUNTEREXAMPLE.json verified_smaller_counterexample.json`: PASS for n=16, E=1603 and all five counts, by the same three methods.
- `python half_search/prove_prefix_families.py`: PASS for the exact symbolic prefix identities, the all-parameter premise polynomials and independent DP comparisons at t=1,...,100 for each of the two families. SymPy is used for symbolic simplification; the derivation is in the report.
- `python check_lower_family_root.py`: PASS for the n=73 L example, all six counts from the original generating relations and event-added ideal DP; all three strict premises positive, L difference negative, opposite b pair balanced.
- `python verify_L_counterexample_independent.py`: PASS, exact structure/width/B checks, independent ideal and chain-prefix methods, 962 states in each underlying model, original and complementary comparison counts.
- `python general_family_probe.py`: PASS, integer binomial prefix count independently reproduces the n=73 certificate. The only publication-side source change is replacing an authoring-machine output path with a file-relative output path.
- `python mc3_search/verify.py`: PASS for the historical n=20 near-boundary example, E=175692, all five event counts by complete extension enumeration.
- `python check_label_resolved_slack.py`: PASS for 406 naturally labelled posets and 3656 eligible ordered pairs, plus the two five-point fixed-label certificates. This is a rerun of the supplied implementation, not a new independent algorithm.
- `python verify_L_family_symbolic_independent.py`: PASS for the independent eight-cell/binomial identities, normalized all-r polynomials and shifted sign checks of the infinite L-counterexample family; exact n=20 and n=73 instances also match.

Logs named `publication_*.log` record these runs. Generated caches and compiled executables are excluded.

## Deliberate limits

The earlier random search, targeted search, all n≤7 search and the 40000-trial Schur screen were not repeated for publication. Their saved summaries are historical evidence, with their original bounds and biases; the Schur audit documents its own exact replay. No old S62/S65 large certificate or the entire historical repository was rerun. Search absence is not a proof of a universal statement.

The frozen audit texts state their own mathematical coverage. In particular, finite counterexample verification is enough to refute HALF/L, while MAIN33/WIDTH3/TEN40 stay OPEN and U58 stays UNDER_AUDIT; the subsequent S105 example additionally refutes the fixed MC3 menu. An audit's source-snapshot hash identifies what that audit read; final distributed bytes, after nonmathematical editorial cleanup, are listed in SHA256SUMS.

## Publication scope

Only research texts, exact mathematical certificates, necessary reproducibility sources, bounded summaries and selected verification logs are included. In-progress drafts, intermediate target-search outputs, binary executables, caches, credentials and unrelated private information are excluded. Nonmathematical editing removes authoring-machine paths and task-coordination wording; mathematical statements and historical proof files are preserved.

The six root navigation/status/dependency files receive a latest-state prefix. Existing S99–S103 and earlier research files are unchanged. GitHub publication uses a single fast-forward commit based on the verified main head, with an expected-head lease and no forced update, deletion or access/security change. Remote read-back and commit-specific CI status are checked after publication and reported separately; this document does not claim a future check has already passed.
