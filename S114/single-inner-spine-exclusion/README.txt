Singleton-upper-spine analytic exclusion
Date: 2026-10-10

Main theorem: for chain weights (u,a,b,1,t,1,v) with v>=t+1,
Pr(B3<T6)+2 Pr(T6<T5)<=2. Two structural-good-pair forced arrows
then exclude every possible counterexample in this unbounded family.

In particular all (u,a,b,1,1,1,v), for arbitrary positive u,a,b,v,
have a balanced pair somewhere. For the requested (u,1,b,1,t,1,v)
family, any remaining counterexample must satisfy 2<=v<=t.

SINGLE_INNER_SPINE_RESULT.md contains the complete proof, law/conditioning
justification, dependencies, and explicitly conditional further corollaries.
verify_single_inner_spine.py is an independent standard-library verifier.
verification.json records the exact checks and their bounded scope.

Reproduce: python verify_single_inner_spine.py

Status: author's proof and checks complete; independent mathematical audit
requested. No claim that the entire single-inner-spine family is excluded.
