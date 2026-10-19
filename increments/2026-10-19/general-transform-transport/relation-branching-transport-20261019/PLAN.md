# Frozen proof controls: 2026-10-19

These seven actual finite posets are fixed before any computation. No generated/search pool will be used. Compute uniform linear-extension counts exactly by dynamic programming over ideals; adding a target relation gives the desired event numerator. All tests concern specified certificates, never assert failure of the 1/3–2/3 conjecture.

1. A3: three-element antichain x,y,z. Edit x<y. Check common pair x,z in both branches.
2. Low-menu loss: chain z<u<v, with x,y isolated. Edit x<y. Select plus witness x,z and minus witness y,z.
3. High-menu loss: dual chain u<v<z, with x,y isolated. Same edit; select plus witness y,z and minus witness x,z.
4. Rare-branch double loss: chains x<a2<a3 and b1<b2<y, and isolated z. Edit x<y. Check two endpoint witnesses in P-minus and their original probabilities.
5. Ordered distinct-endpoint-target overlap: disjoint chains A19, C10, B2. x=A10, w=C5, z=C6, y=B1. Edit x<y. Test plus (x,z), minus (x,w), with w<z and p<1/3.
6. Dominant-branch double-endpoint: disjoint chains A19, B19, isolated z. x=A10, y=B8. Edit x<y. Test p<1/3 and both (x,z),(y,z) balanced in P-minus.
7. Ordered-target boundary without the needed order: antichain x,y plus chain w<z. Edit x<y. This checks that reversing the target-order condition creates no automatic certificate; record plus x,w and minus x,z (both 1/2), with original x,w=1/3 and x,z=2/3, closed endpoints.

Budget: 7 actual controls, maximum 39 vertices. Large examples are three-chain posets with polynomially many reachable ideals, not permutation searches. If an expected certificate in control 5 or 6 fails, report that failure rather than substitute a new control.

## Addendum before running control 8

Control 5 did not satisfy its planned plus-branch bound: q-plus(A10<C6)=71758/103385>2/3. It remains in the evidence; it is not a theorem counterexample. Its other directional checks and exact mixture identities passed.

Freeze one additional control, not a generated search: replace A19 in the same three-chain construction by A99 and x=A50, keeping C10 with w=C5<z=C6 and B2 with y=B1. The mechanism is analytic: for X~Beta(k,k), conditioning X<Y with Y~Beta(1,2) weights by (1-X)^2; as k grows X concentrates at 1/2 and its tilt vanishes. Both central C10 target probabilities tend to 193/512 and 319/512, strictly in the band. Thus sufficiently large k must work. Control 8 uses k=50, 111 vertices and 3300 reachable original ideals. No more controls are planned. New total 8≤12.
