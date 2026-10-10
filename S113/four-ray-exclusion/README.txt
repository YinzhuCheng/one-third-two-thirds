Four-ray exclusion, 2026-10-10

Main result: every chain inflation of the seven-block survivor with weights
(u,1,1,1,t,1,v), for arbitrary positive u,t,v, has some balanced pair.

The new step is the proved upper bound
Pr(B2<B4) <= (v+2)/(v+t+2).
Together with the previously established four-ray reduction, it removes the
entire infinite tail; explicit exact witnesses settle the finite boundary.

Files:
- FOUR_RAY_EXCLUSION.md: full proof, dependency and scope statements.
- verify_four_ray_exclusion.py: exact arithmetic implementation checks.
- verification.json: recorded PASS output and boundary witnesses.

Run:
python /workspace/shared/four-ray-exclusion/verify_four_ray_exclusion.py

The verification script imports the frozen weighted_core_formula.py from the
sibling weighted-surviving-core directory. It does not modify that artifact.
Finite checks validate implementation; they do not replace the infinite proof.
Independent mathematical audit: PASS without substantive corrections.
See /workspace/shared/four-ray-exclusion-independent-audit/AUDIT.md.
