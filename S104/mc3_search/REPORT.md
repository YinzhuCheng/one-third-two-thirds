> Subsequent status update: [S105](../../S105/REPORT.md) refutes the fixed MC3 menu, already for the two-step case, by a verified 54-point width-three poset. MAIN33/WIDTH3/TEN40 remain OPEN and U58 remains UNDER_AUDIT. Statements below that call MC3 OPEN describe the earlier S104 stage, not the current status. The auxiliary theorems and the HALF/L refutations retain their exact scopes.

> Historical finite-search snapshot. Subsequent S104 results refute HALF (n=16 and n=20) and the sufficient lower bound L (n=73). The reported finite runs remain historical observations, not current support for either universal implication. MC3 remains OPEN. See [current S104 report](../REPORT.md) and the exact counterexample audits.

# S104: exact search for MC3 with a two-element neutral chain

## Status and scope
No counterexample was found. MC3 and its unrestricted two-element case remain OPEN. This is a finite exact computation plus a bounded, nonexhaustive search, not a proof beyond the exhaustive range.

The tested statement is precisely: width(P) <= 3; x,y minimal; B=P\\(up(x) union up(y))={b1<b2}; both Pr(b1<x),Pr(b1<y)>2/3. At least one of (b1,x),(b1,y),(b2,x),(b2,y),(x,y) should have probability in [1/3,2/3]. Endpoints count as balanced. No uniform positive balance margin is asserted.

## Complete range: |P| <= 7
`exhaustive_small.py` recursively adjoins a new maximal element whose predecessor set is any order ideal of the existing naturally labeled poset. Thus every naturally labeled poset is generated exactly once. Every finite poset has a natural labeling, so the range is exhaustive up to relabeling (with much isomorphism redundancy). All minimal unordered pairs x,y are considered; menu symmetry makes ordering unnecessary. Width is checked by absence of a four-antichain. B is computed literally and checked to be a two-element chain. Full-poset subset-ideal DP computes every relevant pair count.

| n | Naturally labeled posets | Eligible structural pair instances | Strict dual-majority instances |
|---|---:|---:|---:|
|4|40|6|0|
|5|357|95|0|
|6|4824|1392|15|
|7|96428|21605|369|

In all 384 strict dual-majority instances, all three pairs (b2,x),(b2,y),(x,y) were balanced. The n<4 range cannot contain the four required distinct elements. This proves the finite n<=7 restriction by exhaustive computation, subject to ordinary implementation trust, not formal certification.

## Three-chain exact DP and bounded nonexhaustive search
`search.py` uses three chains beginning with x, y, and b1<b2. Arbitrary acyclic cross-chain edges are permitted except those violating the stated minima/B conditions; the third chain after b2 must belong to up(x) union up(y). Thus there is no neutral-backend restriction. Every accepted structure is independently checked by transitive closure for minimality and exact B. The provided chains certify width<=3.

Full-poset integer completion counts F(s) and prefix counts H(s), over three-chain ideals s, count each pair by summing H(s)F(s+v) at the transition choosing its first endpoint while its other endpoint is absent. No deletion projection is replaced with a uniform distribution. The total full extension count agrees with the terminal forward count.

The fixed random budget was 4800 models:
- 3000: chain lengths 1..6,1..6,2..7; 30 strict-premise instances
- 1500: chain lengths 1..14,1..14,2..15; 10 strict-premise instances
- 300: chain lengths 1..27,1..27,2..28; no strict-premise instance
All 4800 were valid. Thus the searched random parameter box has at most 82 vertices, not an exhaustive n<=82 statement.

`targeted.py` then spent a fixed 40 restarts × 500 proposed mutations, with chain lengths at most 11,11,15 (plus the 20-element seed). There were 11385 valid evaluations, including 237 strict-premise evaluations, with repeats possible. Its objective tested the stronger forbidden combination: dual majority; one x/y orientation >2/3; b2 before that favored minimal point <1/3. No such combination or MC3 counterexample was found. No unbounded sampling was performed.

## Independently checked near-boundary example
`closest_menu_boundary.json` has 20 vertices, chain lengths (2,7,11), and E=175692. In menu order (b1,x),(b1,y),(b2,x),(b2,y),(x,y), exact counts are

149042,117538,122392,59384,40590.

Only (b2,y) is balanced, with probability 14846/43923 (~0.338). `verify.py` independently enumerates every full linear extension and checks all five pair counts, with no three-chain DP and no deletion argument; see `independent_enumeration.json`. This is only a concrete boundary example, not a new asymptotic family, and does not supersede the previously established zero-margin guardrail.

## Extra quantitative candidate, replay only
For the quantitative candidate, `check_stronger.py` replayed the same random and local-search budgets, without expanding the sample set. In all 177 evaluations satisfying the dual-majority premise and an unbalanced x/y orientation, it checked

Pr(b2<favored minimal point) >= Pr(b1<favored minimal point)/2.

No failure occurred; equality occurred, and a complete equality certificate is in `stronger_summary.json`. This inequality is an unproved candidate; absence of a sampled counterexample is not evidence of certification.

## Reproduction
Run `python search.py`, `python targeted.py`, `python exhaustive_small.py`, `python verify.py`, and optionally `python check_stronger.py` in this directory. Fixed seeds are in the scripts. Runtime summaries and exact certificates are JSON. Scripts write only local artifacts.
