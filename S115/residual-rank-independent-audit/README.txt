Independent proof and exact-computation audit of the v>=5 rank obstruction.
Verdict: PASS. Read AUDIT.md first.
Scope: arbitrary positive (u,a,b,1,t,1,v), v>=5.
This belongs to the next package, not frozen S114. Nothing was published.

Reproduce independent checks:
  python independent_check.py --output rerun.json
  python -O independent_check.py --output rerun_optimized.json

The original-source replays live in author-normal/ and author-optimized/.
Their output equals frozen/verification.json byte-for-byte.
independent_normal.json and independent_optimized.json are identical.
SHA256SUMS is the final relative-path deliverable hash manifest.
