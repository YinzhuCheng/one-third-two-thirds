# Independent C13 all-weight support audit

Verdict: PASS for the theorem that every C13 chain inflation with at most three nonsingleton blocks has a balanced pair. Consequently a no-balanced inflation on this frozen core needs at least four nonsingleton blocks and has order at least 12. This does not establish existence with four blocks or exclude arbitrary supports.

## Frozen identity and dependencies

The audited author theorem SHA256 is 899a5bacb83ea3403f69f39dbd37bc8e4f7d9d152eeee8afd4f87015df7b0e78; its certificate SHA256 is aa6c75a0aba79e62602dda5167b571a7ea100a6fa74d8686faa8595c76eaa288. All original author manifest entries and all 22 prior independent-audit manifest entries were checked before copying. This package copies the theorem and relevant prior sources; it does not import any author or previous auditor implementation and did not edit those sources.

C13 retains original strict-up masks [168,252,232,0,160,128,128,0]. The full original record matches the earlier frozen catalogue; that relation tuple occurs exactly once among the original orbit audit's eight-point representatives. All ten cover edges were reconstructed from transitive reduction. The original core classification and external good-pair theorem remain explicit prior dependencies, rather than being reproved here.

## Independently reconstructed finite reduction

The four strict integer inequalities were recovered directly from equal-downset/equal-upset structural witnesses and the incomparable sets. Their targets are 0,3,4,6, with integer right side -1. All 256 singleton port patterns were independently tested by Kahn's algorithm, and the two original cycle certificates were checked edge by edge. Cyclicity occurs exactly when block 0 or 3 is singleton.

All 64 singleton sections compatible with these forced blocks were checked: 57 feasible exact integer witnesses and seven nonnegative-multiplier infeasibility certificates. Their only minimal additional forbidden-singleton sets are {1,2,4,6} and {4,5,6,7}. Thus a no-balanced support must contain {0,3} and hit both clauses. Exhausting all 93 supports of cardinality at most three leaves exactly {0,3,4} and {0,3,6}.

For each support, substituting all outside weights equal to one into the independently derived full inequalities gives exactly A=[[2,0,-1],[0,2,-1],[-1,-1,2]] and b=(2,2,1). Both left and right inverse identities and entrywise nonnegativity were checked using rational arithmetic. The exact product is A^-1 b=(5/2,5/2,3), whose integer floor is (2,2,3). Exhausting this mathematically derived finite box leaves only (2,2,2). No empirical cutoff is used.

The initial author version printed the valid but weaker rational upper bound (5/2,5/2,7/2). In response to this audit, the separate v2 package now states the exact product (5/2,5/2,3). Its certificate is byte-identical to the original; all integer bounds and final claims are unchanged. The original version and its audit remain frozen separately in sibling C13. This final snapshot binds to v2 and reproduces every independent check.

## Actual extension counts

Every labelled linear extension of both eleven-element candidates was explicitly enumerated, with every unordered-pair favorable count collected. This is literal exhaustive extension generation, not the author's predecessor-mask dynamic program. A second occupancy-based recurrence independently recounts both orientations of every unordered pair by enforcing actual-element precedence.

- Support {0,3,4}, weights (2,1,1,2,2,1,1,1): 2060 total; B0<B1 has 698 and the reverse has 1362. Balance: 2060 <= 2094 <= 4120.
- Support {0,3,6}, weights (2,1,1,2,1,1,2,1): 2060 total; B0<B1 has 742 and the reverse has 1318. Balance: 2060 <= 2226 <= 4120.

The pair is incomparable in both cases. All 110 unordered pairs and 220 independent precedence counts agree with explicit enumeration. Complete pair matrices are preserved in audit_results.json.

## Reproduction and optimization safety

Run python audit.py or python -O audit.py. All validation uses explicit require checks which raise exceptions, rather than Python assertions. Both executions passed and produced byte-identical audit_results.json; their stdout logs also agree. The author's own verifier uses assert, so its -O execution is not treated as evidence. This package's verifier is optimization-safe.

Run python verify_snapshot.py to verify the manifest and reproduce in isolated temporary copies under normal and optimized Python. The two theorem scopes in the parent audit directory are intentionally frozen separately.
