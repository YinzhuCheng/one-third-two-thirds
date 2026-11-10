> Historical component manuscript. Its current accepted use and exact final theorem scope are stated in EXACT_D10_ORDINARY_CLOSURE.md and the final composition review; earlier candidate labels are retained as provenance.

# Final independent audit: private-predecessor lift

Date: 2026-11-10 UTC. **PASS WITH THE EXACT SCOPE BELOW.**

Target: `PROOF_CANDIDATE.md`, SHA256
`0301a8d346f5c538d99445ebb2e95f6d0818effb816764c265ecd22418e84ed3`.

## Audit level

This audit was assigned to a new reviewer after the preceding reviewer contributed the full-event bound and rho criterion. I did not participate in that derivation. I read the final manuscript and independently reconstructed its word bijection, complete-P event counts, coefficient bounds, structural deadline maximum, direct recognition statement, and hand-counted separation example. This is a **nonblind internal independent mathematical audit**, not formal verification, external peer review, or a literature-originality certification. Inherited history disclosed the claims. Agreement alone is not the evidence: the reconstruction is given below.

I also checked the specified double-hole V2 lift's structural qualification and listed guard exclusions analytically against the frozen old object and its accepted base review. I did **not** run a new-poset enumeration or any new linear-extension/event DP. In particular, Section8's new21point numerical histogram, N, K, and H4 remain author-computed, not independently recounted by this audit. They are not needed for the accepted pure-structure payment of that object.

No author manuscript or external carrier was modified.

## 1. Exact construction and preserved original contract

The seed is a finite original B1 with minima a,b and a below every other label, private ideal T={x,y,z} a three-point antichain, and C=R−T. Empty C signatures are permitted. Let E be an ideal of C with every point's complete T-predecessor set exactly {y,z}.

Add u with a<u<x and u<C−E, taking closure. Its only old predecessor is a. Its old successors are exactly {x} union (C−E): a successor of x cannot belong to E, and no point in C−E can precede an E point because E is an ideal. Hence u remains incomparable with exactly b,y,z,E. The old P stays induced. The new private ideal is the four-point order u<x with y,z isolated from this chain and from each other. It still has three actual private a-children u,y,z.

The precise degree condition is:

- old Delta(P)<=d;
- each of b,y,z has old degree<=d−1, **also when E is empty**;
- every e in E has old degree<=d−1;
- m+3<=d, where m=|E|.

These conditions are necessary and sufficient for the lifted Delta<=d, because exactly those old degrees rise by one and deg(u)=m+3. This explicit wording removes any possible grammatical ambiguity in the manuscript's combined list quantified by e in E.

For intrinsic S={a,b} union T union Min(C), C and Min(C) do not change, and S+ adds u. Each old point outside J is above x, therefore above u. Old J membership cannot be lost under inducedness, and u is in J+ because strict U(u) excludes u. Thus **J+=J union {u}**, as physical induced orders, not merely a cardinality or isomorphism assertion.

## 2. Independent word table, including A0

Delete a,b and then u from an actual lifted word. This leaves one original word w of R. The legal u slots are exactly those before the first old letter in {x} union (C−E). Deletion recovers w and its slot uniquely.

Write I for old K=2 words whose initial pair contains x, J2=A2−I, X for old K=1 words beginning x, Y=A1−X. For a J2 word, ell is its consecutive E-run after initial y,z; L is the sum of ell over these actual full words. Necessarily 0<=L<=mJ2.

The complete table is:

- old K=0: first C is not in E; only slot0, new K=1;
- old K=1 beginning x: only slot0, new K=2;
- old K=1 not beginning x: two slots, both new K=2;
- old K=2 containing x at rank r=1 or2: r slots, all new K=3;
- old K=2 beginning y,z: three slots with new K=3, then ell slots with new K=2;
- old K=3, x at rank r=1,2,3: r slots, all new K=4.

The first C cannot be in E in the K=0 or1 cases: every E point needs both y,z. Conditional on a fixed initial T-set, first C letter, and remaining word, all permutations of that antichain prefix are legal. This proves the rank averaging used for I and A3 without averaging across different objects or arbitrary completion laws. It gives

    A0+=0, A1+=A0,
    A2+=X+2Y+L,
    A3+=3A2−3I/2,
    A4+=2A3.

The argument includes C empty, where A3=6, the other old counts vanish, and x's three possible ranks still have their usual multiplicities.

## 3. Recovering the true complete-P+ law

For a fixed lifted R+ word with initial private prefix k, restoring b into a followed by that word has k+2 legal slots, including b before a. If u occupies private-prefix rank r, precisely k−r+1 root slots give u<b. If u is after the first C, none do. This is a complete original-P+ count, not a probability assigned to deleted C or to a representative interface word.

For old K=3 and x-rank r, the event contribution is sum_(j=0)^(r−1)(4−j), whose values are4,7,9. Their mean is20/3. For old K=2 containing x, contributions at ranks1,2 are3,5, with mean4. For old K=2 excluding x the three early slots contribute3+2+1=6; the late ell slots contribute0. The K=1 contributions are2 for X and3 for Y. The K=0 contribution is1, while its denominator contribution is3.

Therefore the audited exact totals are

    N+=3A0+12A3+15A2−15I/2+4L+4X+8Y,
    K+=A0+20A3/3+6A2−2I+2X+3Y.

I independently obtain

    3K+−N+=8A3+3A2+3I/2−4L+2X+Y,
    5N+−9K+=6A0+21A2−39I/2+20L+2X+13Y>=0.

The second inequality follows since I<=A2, leaving at least3A2/2 from its two potentially competing terms. It proves the universal upper bound5/9 for this lift. No seed moment hypothesis is used for that upper bound.

## 4. Lower bounds and their quantifiers

The seed's three-point two-moment criterion is exactly A3>=A2+2A1+2A0. Put

    A3=I+J2+2X+2Y+2A0+S0, S0>=0.

In coordinates (I,J2,X,Y,A0,S0), the K+ coefficients are

    (32/3,38/3,46/3,49/3,43/3,20/3).

Replacing L by its maximum mJ2 gives an upper bound for N+ with coefficients

    (39/2,27+4m,28,32,27,12).

For integer m=0,1,2 the smallest coefficient ratio is38/(81+12m). All coordinates are nonnegative and the denominator is positive because A3>0. Hence

    38/(81+12m)<=Pr_(P+)(u<b)<=5/9.

In particular m<=2 gives[38/105,5/9], strictly inside the balance window. These are proved bounds, not asserted sharp constants. The marked pair u,b is fixed in the complete original lifted P+ throughout.

Without seed moments, L<=m(A2−I) instead gives

    3K+−N+ >= 8A3+(3−4m)A2+(3/2+4m)I+2X+Y.

Thus8A3>=(4m−3)A2 suffices for the closed lower bound1/3. This weaker input criterion is correct, including arbitrary A0, which cancels. It does not itself establish a sharp threshold or unrestricted m>=3 seed-moment closure.

The new four-private-point moment score is independently recovered from the histogram by weights(-16,-18,-14,-4,12):

    H4+=24A3−12A2+6I−14L−14X−28Y−18A0.

It need not be nonnegative for the fixed-pair theorem to apply.

## 5. Pure original-structure corridor theorem

For A subset T, C_A consists of all C points whose complete T-signature is contained in A. Each C_A is an ideal, since signatures increase under order. Set

    rho=max_(i!=j)(|C_empty|+|C_i|+|C_ij|).

For beta in LE(C), h_i is the number of letters before its first successor of i, capped at |C| when no successor appears. Sort roots by these first-hit positions as i,j,k, resolving ties arbitrarily. Before the first hit all supports are empty; before the second they are contained in {i}; before the third they are contained in {i,j}. Consequently

    h_i<=|C_empty|, h_j<=|C_i|, h_k<=|C_ij|.

Never-hit roots and simultaneous hits cause no exception: their pre-hit prefixes satisfy the same containments.

Conversely, for any ordered i,j, list the successive differences of the nested ideals C_empty subset C_i subset C_ij before the remaining C points. Such a complete extension exists because all three prefixes are ideals. It gives h_i>=|C_empty|, h_j>=|C_i| and h_k>=|C_ij|. This proves the exact maximum identity

    max_beta sum_i h_i(beta)=rho.

For each beta, K=3 allows exactly six T orders. A K=2 word missing root i from its initial pair is uniquely obtained by choosing either order of the other two roots and inserting i after j initial C letters, 1<=j<=h_i(beta). Thus

    A3=6e(C), A2=2 sum_beta sum_i h_i(beta),
    A2/A3<=rho/3.

If rho<=4 and m<=2, then

    8A3−(4m−3)A2 >= 8A3−5A2 >= (4/3)A3>0.

The pure original-structure theorem therefore proves

    1/3<Pr_(P+)(u<b)<=5/9

without seed moment or LE-count input. Under rho<=4, old deg(i)=3+|C_(T−i)|<=7 for each private child and deg(b)=4, so for D10 the only nonautomatic added-old-degree checks are deg(e)<=9 for e in E, besides the seed's complete Delta<=10.

## 6. Direct recognition in a supplied original object

The constructive theorem has the stated direct form. Suppose an original B1 has private ideal exactly {u,x,y,z}, whose only internal relation is u<x. Let E=C−U(u), assume |E|<=2 and every e in E is above both y,z. Then E is automatically a C ideal; e cannot be above x, since u<x<e would contradict e in E. Deleting u leaves a B1 with private antichain {x,y,z}; the complete old-T signatures of E are exactly {y,z}. The deletion preserves every comparison used in rho, and restoring u is precisely the audited lift.

Thus rho<=4, computed on the original C with respect to x,y,z, directly pays the original pair u,b. No fixed seed needs to be found, no NB assumption is inherited under deletion, and no new completion law is postulated.

## 7. Independent hand-check of the separating example

For y,z<e1,e2<w, the five-point component has2!*2!=4 words. Inserting isolated x into each of its six slots gives A2=A3=12. For the three K=2 slots, E={e1,e2} has consecutive initial runs1,2,2, so L=4*5=20 and I=X=Y=A0=0.

The lifted histogram is(20,36,24) at K+=2,3,4, hence M+=80, N+=404 and event numerator K+=152. Thus p=38/101. Direct arithmetic gives mu+=61/20 and Q2+=129/10, so its new moment slack is−17/30. This independently verifies a true original-object separation between the fixed-pair closure and the new moment criterion. The example has fair twins; no new-net-coverage conclusion is supported by it.

## 8. Specified V2 double-hole qualification and guard scope

Accepted base dependencies are the frozen V2 input `../b1-two-moment-residual-coverage-20261110/WIDER_RELEASE_V2_SCREEN.json`, SHA256 `6052f2570c677853da66fd21d9697f08e271c3856630bcb61c58ffff50050359`, and that directory's sealed base independent review. I used its already established Delta10, old J17, width5, primeness, rigidity and old guard exclusions; I did not silently re-certify the base by a new enumeration.

From the actual old signatures, with x=d1,y=d2,z=d3:

- C_empty is empty; C_x={l}; the other singleton ideals are empty;
- C_xy={l}, C_xz={l,k1,k2}, C_yz={h1,h2,h3,h4};
- rho=4;
- E={h1,h2} is a C-minimal antichain of exact support{y,z}.

Their old degrees are6 and9. Old degrees of b,y,z are4,6,4. The new complete object therefore has Delta10, exactly the same two minima/maxima, and J18. Its fixed pair is paid by the pure-structure theorem independently of the new numerical DP values quoted by the author.

New incomparable pairs involve u only with b,y,z,h1,h2. For u/b, the reverse chain-private difference contains the antichain E; the other direction has factor2. For u/y, its two private upper differences include respectively {x,k1,k2,l} and E, both nonchains. For u/z, one difference is the chain{x,l}, but the other is E. For u/h_i, the relevant private lower difference contains the antichain{b,y,z}. Hence no new VG or two-sided chain-private factor<=2 guard arises. Old failures persist because no old private difference or old incomparability is deleted. Same-D/U equalities cannot be newly created among old points.

The unique same-D triple is {u,y,z}, with missing sizes(2,4,2). Its u-only successors include x,l, excluding the first-two exchange hypothesis. A new equal-U triple involving u is impossible: U(u) contains x, so an old point with that same U would have to precede x; only a can, and U(a) also contains u. Thus the stated triple guards do not apply.

Using the old accepted avoiding reference, insert u between z and x:

    a,b,d3,u,d1,d2,h1,h2,l,k1,k2,h3,h4,g1,g2,g3,s,g4,q,r1,r2.

The only new primal anchors are(u,b),(u,d3),(h1,u),(h2,u), and the only new dual anchors are(h1,u),(h2,u). This reference reverses all of them; its old restriction is exactly the previously accepted reference. Old-pair anchors can only be lost, not newly created, because the old violating comparisons/private nonchains remain. This verifies the enumerated slot-bank exclusion.

For incomparability-graph primeness, any new proper module intersected with the old prime graph would be an old module. The only possible nonsingleton new modules are therefore{u,v}, or the entire old block. The latter is excluded because u's neighborhood is nonempty and not the entire old block. Its neighborhood is{b,y,z,h1,h2}. The only possible degree-matching twin candidates b,z,q have different neighborhoods (b has a, z has x, q has h4). So graph primeness persists, and consequently so does order-autonomous primeness.

The point x becomes the unique point with exactly two strict predecessors; u is its unique predecessor with one strict predecessor. Thus x,u are fixed by every automorphism, and old rigidity fixes all remaining points. Width remains5: the five-point induced I(u) is the three-point antichain{b,y,z} below the two-point antichain{h1,h2}, of width3. Any antichain containing u has at most4 points, while the old5point antichain remains. Old induced S3 and2+2 remain. The old cover4cycle is not subdivided, since no old lower endpoint of one of those edges is below u.

This is a relative exclusion of the guards just listed, not all historical theorems or external literature. The single-hole controls remain old-VG covered. I have not independently recounted the new21point LE numbers or extended the audit to all possible J18 or B1 objects.

## 9. Final scope

Accepted:

- exact arbitrary-seed original-word and full-P event identities, including A0;
- degree transport and physical J increase by exactly one;
- old-moment m<=2 fixed-pair interval;
- weaker original-count criterion and exact new-moment score;
- pure rho<=4 original-structure payment and its direct T4 recognition form;
- hand-counted separation from the new moment criterion;
- the specified double-hole V2 qualification and enumerated structural exclusions above.

Not established: all B1, all variable intrinsic J, arbitrary private-ideal shapes, an unrestricted m>=3 closure, sharpness of the lower constants, all-history net coverage, or an independent recount of author sample DP totals. Repeatedly applying the same lift is not automatically authorized mathematically: after one lift T is no longer the required three-point antichain.
