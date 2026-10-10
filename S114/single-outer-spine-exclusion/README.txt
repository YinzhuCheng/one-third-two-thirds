Seven-core chain-inflation research: both inner spine blocks singleton
2026-10-10

Main theorem:
  TWO_SINGLETON_INNER_BLOCKS_EXCLUSION.md
  All positive chain inflations (u,a,1,1,t,d,v) have a balanced pair,
  under the stated structural-good-pair and generalized-shuffle dependencies.

Baseline theorem:
  SINGLE_OUTER_SPINE_EXCLUSION.md
  All positive chain inflations (u,a,1,1,t,1,v) are excluded as counterexamples.

Reproduce the finite implementation checks:
  python verify_single_outer_spine.py
  python verify_two_singleton_inner_blocks.py

These scripts use only the Python standard library. They verify formulas using
an independent labelled ideal DP. Their finite results supplement the proofs;
they do not establish the infinite statements by sampling.

Verification results:
  verification.json
  two_singleton_inner_blocks_verification.json

The separate generalized-bound auditor is preparing the audit supplement.
The first pre-audit baseline hash 72b287... was superseded after correcting an
imprecise sentence about initial prefixes; the proof and identities are unchanged.
MANIFEST.sha256 identifies the final corrected sources in this folder.

explore.py is a preliminary local diagnostic, not part of the frozen theorem
or the reproduction manifest.
