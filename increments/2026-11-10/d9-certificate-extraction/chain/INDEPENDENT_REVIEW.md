# Independent audit: frontier swap bank and 353 D9 replacements

2026-11-10. Internal independent mathematical and metadata review, not external peer review or formal verification. The proof is analytic; finite metadata checking only establishes which existing tree records meet its hypotheses. The author draft SINGLE_FRONTIER_ANALYTIC_REPLACEMENT.md was read after the independent argument and mapping check. Source tree: Kevin Fathi v22, https://zenodo.org/records/23933091, §24.4.1, locally retained ORIGINAL_V_FIRST_PACKET.json.

## Verdict

PASS for the general frontier inequality and its original-law application. Independently checked 353 distinct existing bank occurrences out of 3469 in the supplied seven-phase packet. This does not replace the other 3116 banks, the phase coverage proof, private-chain trees, or all D9 certificates.

For incomparable x,y in any finite P let D,U denote strict downsets and upsets, and set

    L = maximal elements of D(x) minus D(y),
    H = minimal elements of U(y) minus U(x).

In the uniform linear-extension law of this same P,

    2 Pr(x before y) + sum_(z in L) Pr(y before z)
                        + sum_(t in H) Pr(t before x) >= 1.       (F)

There is no degree or width restriction on (F).

Theorem 2.3 of that source was also directly read: it already gives exactly the occupied-position swap and maximal/minimal direct-blocker mechanism. The present use is analytic re-extraction for the §24 tree, not a novelty claim. Its largest-minority setup is not needed for the elementary union-bound inequality (F).

## Independent proof and frontier check

Consider a word with y before x. Swapping their two positions is legal unless either a predecessor of x lies between y,x or a successor of y lies between y,x. Moving x left cannot violate an x-successor relation, and moving y right cannot violate a y-predecessor relation; incomparability of x,y takes care of their mutual relation.

A predecessor z of x between the endpoints cannot precede y in P, hence belongs to D(x) minus D(y). Extend it upward to a maximal z' in this difference. The word still has y before z' before x. Thus the lower obstruction is witnessed by an element of L, not merely by an arbitrary element of the full difference. Dually, a successor t of y in the interval belongs to U(y) minus U(x), and choosing a minimal element t' of that difference below it leaves y before t' before x. Thus the upper obstruction is witnessed by H.

The swappable bad words inject into the good words by the involutive position swap. All other bad words lie in the union of the events charged in (F). Hence N_bad <= N_good + sum obstruction counts, which gives (F). Every charged comparison is genuinely incomparable: for example z<y contradicts z in D(x) minus D(y), and y<z<x contradicts x incomparable y. The upper case is dual.

When |L|+|H|=1 the bank has total weight three, so (F) gives the exact one-third bank threshold. When both frontiers are empty, it gives Pr(x before y)>=1/2, stronger than the required one-third. If every charged event reverses the same fixed candidate strict two-thirds order, the row is excluded under the ORIGINAL no-balanced-pair assumption. No NB assertion on a helper poset is made.

The coefficient bound is sharp. For the poset consisting of y<t and an isolated x, both Pr(x before y) and Pr(t before x) equal 1/3.

## Why the full frontiers are known from the marked ideal

Let Q be an ORIGINAL ideal containing x,y. Both full downsets are already in Q. If every exterior label is above x, no exterior label belongs to U(y) minus U(x). Thus all sets and frontiers in (F) are computed from the marked induced order without discarding any original obstruction. Exterior-above-x follows either from actual pivot exhaustion, remembered exhaustion, or from d_Q(x)=9 under the degree-nine hypothesis, since an exterior element cannot be below x by ideality and cannot be incomparable by saturation.

For a certificate's formal gap profiles the same conclusion holds conditionally whenever h_x=0: realize the fixed exterior word as a chain. Then x is below that entire chain, so (F) applies to that exact completion count. This observation proves the stated bank for every admissible profile, not just a convenient actual mixture. It does NOT justify a structural pivot switch from a zero in only one conditioned word.

A fixed bank is selected from the marked state/reference before the exterior word is sampled. Its count inequality can therefore be summed with the original completion multiplicities. No uniform profile averaging or changed-event averaging is involved.

## Independent metadata audit

INDEPENDENT_FRONTIER_MAPPING.py independently reconstructed each downset/upset, frontier, reversed-event orientation, incomparability, packet row identity and saturation/exhaustion reason. It did not call the discovery script. Output: INDEPENDENT_FRONTIER_MAPPING.json.

- 353 distinct matching packet bank records; all match original mode and old bank.
- 182 unconditional rows use d_Q(x)=9.
- 171 terminal rows use x equal to that phase's pivot.
- Frontier sizes: 15 empty/empty, 323 empty/one-upper, 15 one-lower/empty.
- By phase: 347 in phase 0, four in phase 2, one in phase 4, one in phase 6.
- All named bank events are reversed in the stored reference order and incomparable in Q.
- Maximum full predecessor count among every positively charged endpoint is six, preserving the M8 locality restriction.
- Independently checked the four final-phase seed references on arrays (0,0,1,1,3,7,7), its 39 extension, and its 55 extension: x=4,y=3 has L={1}, H=empty; the common bank is 2 Pr(4 before 3)+Pr(3 before 1)>=1. All four references place 1 before 3 before 4. No whole-phase closure is inferred.

The mapping audit is structural metadata enumeration, not rechecking millions of deadline inequalities. The analytic lemma removes those inequalities for these occurrences.

## Separate one-sided cyclic injection

The proposed auxiliary statement D(x) subset D(y), k=|U(y) minus U(x)| implies Pr(x before y)>=1/(k+2) is also valid. In a bad word y ... x, list y=z0 followed by all U(y) labels z1,...,zr in the interval. Move x to y's position and each zi to the next listed position, the last to the old x position. x crosses no predecessor. Every zi crosses no unlisted successor, since such a successor would be in U(y) and in the interval. Each zi is incomparable with x: zi<x would imply y<x, and x<zi contradicts the original word. Given the output and final moved label zr, the selected labels and rotation are uniquely recoverable. There are at most k+1 possible final labels, giving bad <=(k+1)good. The bound is sharp for y below an antichain of k labels and an isolated x.

The 58 single-defect rows split into 29 upper-one-defect, 15 lower-one-defect, and 14 zero-defect rows. The 15 lower-defect rows require the order-dual version, as the final author draft correctly specifies. The literal one-sided formula alone covers only 43. All 58 are subsumed in the 353 frontier replacements and must not be added to their count.

## SF6 additional independent audit: genuine D10 four-chain control

PASS with the stated stopping-line scope. Read the author SF6 and D10_N4_REAL_CONTROL.py/.json. Independently reconstructed both full 14-label predecessor arrays directly from the seven-chain construction, checked their transitive closure, and counted original extensions with a forward ideal-subset DP that charges ba when a is inserted and vc when c is inserted. This differs from the author's added-edge backward counting implementation. The independent code and exact output are INDEPENDENT_D10_N4_CONTROL.py/.json.

For h_u=0 the original full counts are N=4282, K_ba=1577, K_vc=1197 and margin -242. For h_u=1 they are N=8564, K_ba=3154, K_vc=2394 and margin -484. Thus -242 is BOTH the original h_u=0 margin and the increment from zero to one; these are distinct verified facts, not a replacement of one by the other.

The doubling also has a structural explanation: in the h_u=1 poset, u and z1 have the same strict downset {a} and the same strict upset {z2,...,z7}. They are twins. Adding u<z1 gives the h_u=0 poset, and the twin-swap involution splits all counts involving only a,b,v,c equally between the two orientations.

Both posets have exactly minima a,b, maximum incomparable degree 10, and private ideal P minus up(a) exactly {b<c<d<e}. The fraction Pr(b before a)=1577/4282 is strictly between 1/3 and 2/3 in both. Hence a,b are already balanced. This is a real countercontrol to the D10 cap transfer of the old bank and to unnormalized u-axis monotonicity in the enlarged cap domain; it is NOT an NB example, not an example with minority private-root probability below one third, and not a counterexample to ordinary balance.
