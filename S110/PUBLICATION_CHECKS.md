# S110 publication-side checks

Date: 2026-10-10. All seven Python commands below ran successfully against an isolated copy of the portable final bundle. They use only the Python standard library. These finite calculations corroborate the proofs; they do not prove the general theorems, settle the main conjecture, or establish novelty.

Run from this S110 directory:

1. `python check_s110.py --max-n 7 --fiber-max-n 6 --output s110_checks.json`
2. `python independent_audit/independent_matrix_audit.py`
3. `python check_single_splice.py`
4. `python splice_independent_audit/check_splice.py`
5. `python local_decay/independent_audit/check_local_decay.py`
6. `python finite_representative_tests/check_encoding_compression.py`
7. `python finite_epsilon_audit/check_compression.py`

Commands regenerate their own output JSON files; run them in a copy if preserving the original historical bytes matters.

## Exact comparisons and actual coverage

- Cut-profile author and independent checker outputs agree with the included JSON after excluding only `elapsed_seconds`. All counts and assertions agree. The author checker covers 101,660 naturally labelled posets through seven points; its direct deletion-fiber checks go through six points. The separate relation-matrix/permutation implementation covers 5,232 naturally labelled posets through six points and tests loose degree bounds and actual insertion fibers.
- The single-splice author output and independent output reproduce their included JSON byte-for-byte. The independent checks include five positive examples with 689 incomparable pairs and the overlapping-cut actual-identity negative control.
- The local-decay independent output reproduces its included JSON byte-for-byte: 5,232 small posets, 1,357 positive transfer blocks and 73 actual-poset comparisons, including 45 induced-window comparisons. Counts and exact rational inequalities are independent of display-only floating point values.
- The finite-representative author and independent outputs reproduce their included JSON byte-for-byte. They test encoding, legal decoding, marked and unmarked path shortening, actual local witnesses and physical endpoint flags, including the zero-edge path case. The independent check verifies 4,727 final incomparable-pair witnesses. Structural tests with deliberately small radii do not claim those radii meet the theorem's epsilon-decay prescription.

The proof files remain bound to their independently reviewed versions. Only the one source-reference path and two historical output destinations described in `PORTABILITY.md` were sanitized. No mathematical expression or theorem was altered in making the portable publication. All files outside S110 are preserved by the publication commit's base tree. Complete fixed-commit byte readback and the exact old-tree comparison are retained separately as the publication receipt.
