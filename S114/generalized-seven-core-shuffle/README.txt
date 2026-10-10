Generalized seven-core shuffle bounds
Frozen author artifact, 2026-10-10

Contents
- GENERALIZED_SHUFFLE_BOUND.md: universal proofs, exact cone, and endpoint formula.
- verify_generalized_shuffle.py: self-contained standard-library exact verifier.
- verification.json: deterministic verification output.
- MANIFEST.sha256: SHA-256 integrity manifest.

Reproduce
  python verify_generalized_shuffle.py
  python -O verify_generalized_shuffle.py
Both modes retain every verification check and produce identical results.

Proved scope
For every positive seven-chain weight vector, strict upper bounds hold for
Pr(B2<B4) and Pr(T4<T3). With the preceding structural prerequisites, these
give an exact finite integer relaxation for the three pendant lengths once
the four spine lengths are fixed. Its sharp cap and a new endpoint-count
formula are proved. The universal all-seven-weight balance question remains
open; no global finite bound on spine lengths is claimed.

Dependencies
The structural forced-arrow prerequisites and singleton-port filter were
established and audited in the preceding research packages. The earlier
local source documents are:
  /workspace/shared/weighted-surviving-core/ANALYTIC_RESULT.md
  /workspace/shared/four-ray-exclusion/FOUR_RAY_EXCLUSION.md
The new probability bounds and arithmetic proofs are self-contained here.

Independent audit
The independently maintained audit_generalized_shuffle_bounds worker has
received the frozen source hashes. Its final audit report is a separate
artifact; this author freeze does not claim audit completion.
