General terminal-rank bounds, 2026-10-10

Read GENERAL_TERMINAL_RANK_BOUNDS.md for the proof.

Main results for seven-core chain weights (u,a,b,c,t,d,v):
1. Balancedness for d=1,v>=4; d=2,v>=10; d=3,v>=30, with all other weights unrestricted.
2. Every hypothetical counterexample satisfies 3(c)_v<(c+d+1)_v and its dual.
3. Every (u,1,b,c,t,1,v) is balanced. This explicitly depends on the independently PASS all-spines-at-most-three census; a fresh complete 41-case reduced certificate is included.
4. If a,d<=3, any counterexample has u,v<=29,b,c<=90,t<=104,N<=348. This is a finite necessary region, not an exclusion of that entire class.
5. The unrestricted beta-binomial uniform-atom method cannot extend to d>=4, shown by an analytic limit and an exact n=1000 witness. This is not a poset counterexample.

Reproduce with Python 3 and its standard library only:
  python verify_general_terminal_rank.py
  python -O verify_general_terminal_rank.py

Both runs regenerate verification.json and reduced_41_certificate.json.
The frozen normal and optimized outputs agree byte-for-byte. All checks use explicit exceptions, not assert statements.

No remote write or publication was attempted. The independent peer audit is maintained separately. SHA256SUMS covers every deliverable except itself.
