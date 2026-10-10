FOUR-TAIL INDEPENDENT AUDIT — 2026-10-10
Verdict: PASS. Read PROOF_REVIEW.md for the mathematical audit and scope.

Inputs are frozen under source_snapshot/. The independent audit uses only Python
standard-library modules and resolves inputs relative to audit.py.

Portable replay from this directory:
  python audit.py replay_normal.json > replay_normal.log
  python -O audit.py replay_optimized.json > replay_optimized.log
  python -c "from pathlib import Path; a=Path('replay_normal.json').read_bytes(); b=Path('replay_optimized.json').read_bytes(); print('IDENTICAL' if a==b else 'DIFFERENT'); raise SystemExit(a!=b)"
The *_vectors.json files are generated automatically and should also be identical.
Do not run source_snapshot/verify_four_tail.py directly if preserving the snapshot.
The source verifier can safely be rerun from its preserved execution copies:
  python source_normal/verify_four_tail.py > source_normal/run.log
  python -O source_optimized/verify_four_tail.py > source_optimized/run.log

Frozen independent outputs: normal.json, optimized.json, their logs and per-vector
JSON records. Frozen source replay outputs are in source_normal/ and
source_optimized/. Source directory integrity is recorded in SOURCE_INTEGRITY.json.
MANIFEST.sha256 binds every delivered audit file except the manifest itself.

No source edits or remote writes were performed. This audit does not itself
authorize a release or alter the earlier frozen publication scope.
