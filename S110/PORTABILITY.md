# Portable publication and audit binding

Date: 2026-10-10. This note concerns metadata and file identity only. It does not add a mathematical claim or substitute for proof review.

## Fixed proofs

- `bounded_cut_profiles.md` is byte-identical to the audited source, SHA-256 `06cb5f863b4055a5779160a7a07bf18908f089f7a54de872d6cd4f1e067acd31`.
- `local_decay/local_probability_decay.md` is byte-identical to the audited source, SHA-256 `7eaf6b449270286010b98b2e0725b8fbaec21bbe641dcd0e270fcc4a4628c14b`.
- `single_splice_stability.md` has one portability-only change: its Section 5 reference to the cut-profile source now uses the bundle-relative `bounded_cut_profiles.md`. No other byte changed. The original audited SHA-256 is `d537434e9bfc71e6c94cad9148e78e37b8075d40239face596fef96308737a22`; the portable published SHA-256 is `3e06cfd29b5a09a3f0c67b2522d1fe8d360ea556ba6fa11204283ac6ff9baa76`.

An independent publication-side comparison reconstructed the single path replacement from the fixed original and verified the complete resulting bytes: **PASS, metadata-only, mathematical content unchanged**. This is a portability rebinding, distinct from the original mathematical audit. References to the original hash in the retained audit reports identify their original input, rather than claiming that hash equals the portable copy.

`splice_independent_audit/proof_audited_snapshot.md` receives the same replacement and is byte-identical to the portable main proof. Its textual relative source reference is interpreted from the S110 bundle root, as in the main copy. The audit directory's current `SHA256SUMS` binds its portable files.

`finite_epsilon_representative.md` is byte-identical to its final independently passing proof, SHA-256 `3cc5606209bad491a52c3591e2ed337f04748b4e4f267e7298aa3b84327ebfe5`. Its audit snapshot is also byte-identical.

## Logs and historical audit metadata

Only the printed JSON output destinations in `s110_checks.log` and `independent_audit/supplied_checker_rerun.log` were shortened to portable filenames. Their counts, conclusions and historical timings are unchanged. The historical audited-source hashes remain recorded in `independent_audit/independent_audit.md`; the original `audit_manifest.json` is preserved as a record of that audit's exact input and output. The publication-wide manifest gives the hashes of the current portable log copies.

The Python checkers are unchanged. Publication-side runs used an isolated copy of the portable bundle. Timings are run-specific metadata, not mathematical evidence. See `PUBLICATION_CHECKS.md` for actual rerun scope and comparisons. Top-level `MANIFEST.json` and `SHA256SUMS` identify the final published bundle.
