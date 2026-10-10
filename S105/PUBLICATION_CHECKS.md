# S105 publication checks and scope

The publication copy contains the 54-point primary counterexample, the 72-point discovery record, their independent all-pair audits, relevant counting sources, and the independently reviewed two-tail subclass theorem. No claim of globally minimum counterexample size is made.

## Checks rerun for publication

- `python check_full_mc3_root.py`: original generating-relation ideal DP reproduces the n=72 total and all five event counts, verifies all five strict premise/failure differences, and finds a genuine balanced pair outside the menu.
- `python check_full_mc3_root.py mc3_coupled_search/shrunk_0.json`: same independent recurrence reproduces the n=54 counts and strict differences; it finds (c1,y) with count 70352578296 out of 132985636140.
- In `mc3_coupled_search`, `python verify_certificate.py` and `python verify_certificate.py shrunk_0.json`: independent vertex-bitmask ideal DP, each of five comparison events and all five complements added separately. Structural minima/avoidance/chain checks and all counts agree.
- `python mc3_counterexample_audit.py --input mc3_coupled_search/MC3_COUNTEREXAMPLE_high.json --outdir . --stem mc3_counterexample_audit`: independent all-pair forward/backward ideal-DAG counts. PASS, n=72, 1092 ideals, 2584 transitions, 2556 complementary pairs, 81 balanced unordered pairs.
- `python mc3_counterexample_audit.py --input mc3_coupled_search/shrunk_0.json --outdir . --stem mc3_counterexample_n54_audit`: PASS, n=54, 816 ideals, 1930 transitions, 1431 complementary pairs, 64 balanced unordered pairs. Both runs also cross-check the method on 16 small posets by literal permutations.
- `python verify_two_tail_rescue.py`: all supplied symbolic checks PASS. The theorem's separate independent audit records the self-contained all-parameter proof and its own generic-DP/finite-grid diagnostics; that broader diagnostic grid was not rerun for publication.
- `python verify_gated_family_binomial.py`: PASS, the self-contained n=72 prefix/suffix binomial partition reproduces E, all five menu counts, the coupling identity and the actual balanced (c1,y) count. It imports no DP/search implementation.

These runs use the original complete-linear-extension law and exact integers. Finite diagnostics do not prove a universal theorem. An exact real-poset counterexample does disprove the universal fixed-menu assertion; mathematical scope and structural hypotheses are verified separately in the reports.

## Source preparation

The original-recursion check was made portable with a file-relative default input and optional input argument. Nonmathematical authoring-machine paths were removed from distributed text/logs. No mathematical counts or inequalities were changed. Search intermediates, compiled executables, caches, unrelated information and internal task state are excluded.

`SHA256SUMS` lists every S105 distributed file other than the manifest itself, with paths relative to repository root. It can be checked from the repository root with `sha256sum -c S105/SHA256SUMS`. Root navigation/dependency files are listed in the companion S104 manifest. Final GitHub/Notion read-back receipts are reported separately after publication; this document does not pre-claim remote success or CI results.

Current state: MC3 fixed menu REFUTED; HALF/L REFUTED; MAIN33/WIDTH3/TEN40 OPEN; U58 UNDER_AUDIT. S99 conditional reductions, S103 square, S104 double conditioning and label identities retain their stated scopes. The two-tail theorem covers its explicit subclass only.
