# S111 publication-side checks

Date: 2026-10-10. These are release reproducibility checks, separate from the three mathematical audits. All commands below were actually rerun against a separate copy of the portable files; all returned exit code 0. The published files were not overwritten by the reruns.

## Executed commands

From `actual_fiber/`:

```sh
python reproduce_candidate.py
python certify_small_mtp2.py 2
python certify_small_mtp2.py 3
python certify_small_mtp2.py 4
python certify_small_mtp2.py 5
```

From `independent_audit/`:

```sh
python audit_actual_fiber_independent.py
python audit_small_minimality_independent.py
python certify_all_branches.py
python check_kernel_boundaries.py
python compare_proposal_coefficients.py
```

From `barrier_audit/`:

```sh
python audit_realizability.py
```

This command also reruns `source_snapshot/verify_realizability_barrier.py` and asserts its stdout matches the saved source log byte-for-byte.

From `recurrence_audit/`:

```sh
python audit_section5.py --max-m 5 --literal-partition-max-m 5
```

## Output comparisons

Fourteen generated JSON artifacts were compared with the publication snapshot:

- Nine were identical byte-for-byte: the source actual-counterexample result; all seven independent core-audit result/certificate files; the realizability audit result.
- Five were identical as parsed JSON after removing only the top-level `elapsed_seconds` field: four `bernstein_mtp2_m*.json` summaries and `recurrence_audit/section5_exact_checks.json`.
- The realizability audit's source-hash field binds the portable source set, including the explicitly scoped excerpt. Mathematical output is unchanged.
- `compare_proposal_coefficients.py` also checks every source stored coefficient record against the independent records, including transposition canonicalization.

The finite minimum uses exact complete coefficient certificates and the proved diagonal/endpoint argument. The optional historical `exhaustive_m5.json` and `exhaustive_m6_grid.json` are retained as clearly bounded grid observations; those optional grid runs were not rerun for publication and are not used to prove global MTP2 or minimality. In particular the m=6 coarse grid misses the actual n=8 counterexample.

## Scope, portability and dependency checks

- The two source excerpts were independently compared with the original source section boundaries (1 to 2, and 7 to 8). They are verbatim apart from surrounding blank-line normalization. The added definitions were checked separately. Omitted sections are not included or implicitly certified.
- Source changes are confined to paths, neutral publication wording, the labeled excerpt, manifest/result source-hash metadata, and explicit publication-binding notes; no checker arithmetic or predicates were altered.
- All master and nested checksum entries use relative public paths and were checked against their files.
- The publication contains no private workspace paths, raw conversation, private publication receipts, caches, source PDFs, or installed software packages.
- Standard-library-only scripts remain so. `audit_actual_fiber_independent.py`, `audit_realizability.py`, and the source symbolic verifiers require SymPy; no dependency is bundled.

No finite test here proves the unrestricted dimension-sharp conjecture or any global balanced-pair conjecture. The all-n restricted theorem and recurrences rely on their supplied proofs; the finite exhaustive runs support, rather than replace, those proofs. This package makes no novelty, external-peer-review or formal-verification claim.
