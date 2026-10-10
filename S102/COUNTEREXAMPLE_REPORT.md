# Exact seven-point terminal-fork counterexample

This falsifies the proposed stronger sibling-balance statement, not the 1/3–2/3 conjecture or S99 Theorem D.1.

Labels: u, s, t, y, a, b, c.
Hasse relations: u<s, u<t, u<a, y<a, t<b, y<b, b<c.
No other relations except transitivity.

## Exact checks

- E=62 linear extensions, counted by order-ideal DP and independently by filtering all 7!=5040 permutations.
- y is minimal; its incomparable elements are exactly u,s,t.
- P(u<y)=42/62=21/31 >2/3, and <7/9.
- P(s<y)=10/62=5/31 <1/3; P(t<y)=18/62=9/31 <1/3.
- a,b,c are above y, so their before-y probabilities are all zero.
- u is the only y-incomparable majority point, hence poset-maximal in that set.
- Its private Hasse covers are exactly s,t; a is another cover of u but lies above y.
- D(u) is empty, hence d=1 >2p−5/9 =223/279.
- The chain partition (u,s), (y,a), (t,b,c) proves width≤3. The antichain {s,t,y} proves width=3.
- P(s<t)=17/62 <1/3 (3×17=51<62); equivalently P(t<s)=45/62 >2/3.

## Full original-law probability matrix

Every entry is numerator/62; row label precedes column label. Diagonal entries are zero.

| |u|s|t|y|a|b|c|
|---|---|---|---|---|---|---|---|
|u|0|62|62|42|62|62|62|
|s|0|0|17|10|36|34|48|
|t|0|45|0|18|51|62|62|
|y|20|52|44|0|62|62|62|
|a|0|26|11|0|0|28|45|
|b|0|28|0|0|34|0|62|
|c|0|14|0|0|17|0|0|

## Scope

The search was seeded random sampling of n=5–12 posets with explicit two- or three-chain decompositions and extra forward relations; it stopped at its first counterexample (iteration 35, counting from zero). This was not exhaustive and not canonical unlabeled enumeration. The 11-point witness was exhaustively reduced over all induced subposets retaining its designated y,u,s,t: seven is the smallest size within that reduction, not a claim of global minimality. All 62 extensions of the seven-point witness are supplied in terminal_fork_minimal_induced.json.

Nine-point candidate supplied independently was also verified by all 9!=362880 permutations: E=132, p_u=p_a=90/132, q_s=40/132, q_t=28/132, P(s<t)=90/132. Its full matrix is in nine_point_verified.json.
