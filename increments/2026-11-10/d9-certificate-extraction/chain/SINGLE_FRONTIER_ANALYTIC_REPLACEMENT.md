# Single-frontier swap compression inside the D9 remembered-pivot tree

2026-11-10. Author proof and metadata mapping; independent review is a separate file. This is an application/re-extraction of the global occupied-position swap and direct-blocker mechanism already in Kevin Fathi, *Gold Certificates and Balanced Pairs*, fixed v22 https://zenodo.org/records/23933091, Theorem 2.3 and §24.4.1. No originality claim, no new balance class, no whole-D9 analytic proof, .

## Result and exact scope

One analytic lemma replaces the arithmetic payment tables in **353 of the 3469 bank occurrences** in the supplied v-first seven-phase tree: 182 unconditional rows and 171 terminal rows. This is a selection of existing states, not 353 new posets. All other rows and every structural coverage/canonical-prefix argument stay unchanged. The 353 replacements preserve the ordinary D9 contradiction and use endpoints with at most six predecessors, so do not damage the M8 locality target. These statements were obtained by source-packet metadata checks, NOT by re-enumerating deadline vectors.

The counts by zero-based source phase are: phase0 347, phase2 4, phase4 1, phase6 1. There are no replacements here in the three b-pivot phases. Of the 353 choices, 323 use one upper-frontier blocker, 15 use one lower-frontier blocker, and 15 are critical-pair cases with no blocker. The earlier 58 single-defect choices are a subset, not an additional count.

## SF1. Exact original-object inequality

Let P be any finite poset, x||y, with strict downsets D and upsets U. Put

    L=max_P(D(x)\D(y)),    H=min_P(U(y)\U(x)).

Here max/min are within the indicated induced difference, and the empty frontier is empty. Uniform original-P extensions satisfy

    2 Pr(x precedes y)
      + sum_(z in L) Pr(y precedes z)
      + sum_(t in H) Pr(t precedes x) >= 1.            (SF1)

No NB, degree, minimality or conditioning assumption is used in this lemma.

Proof. Let G be the set of words with x before y and B its complement. Exchange the occupied positions of x,y in a word of B. The exchange is legal unless it moves x across a predecessor or moves y across a successor. Common predecessors/successors cannot obstruct. If a member of D(x)\D(y) is after y, some maximal member z of that difference is after y too, so this word lies in {y before z}. If a member of U(y)\U(x) is before x, some minimal member t is before x too, so it lies in {t before x}. Conversely these blockers obstruct the exchange on B. Legal exchanges inject the remaining part of B into G. Thus

    |B| <= |G| + sum_L |{y before z}| + sum_H |{t before x}|.

Add |G| and divide by e(P). This proves SF1. Every blocker endpoint is incomparable with its other endpoint: e.g. z<x but z not<y, while y<z would imply y<x, impossible. The upper case is dual.

If |L|+|H|=1, SF1 is a nonnegative bank of total weight3 and lower bound1, exactly the 1/3 payment required by (179). If the frontiers are empty, 2Pr(x<y)>=1 and the singleton bank already pays. To contradict a candidate strict-two-thirds reference T, every displayed event must reverse T. That is an explicit tested condition, NOT automatic from the lemma. No individual pair balance is asserted from a one-direction lower bound alone.

## SF2. Reading the full frontiers from a remembered ideal

Let Q be an actual full induced ideal of the same P. Assume every original exterior label lies above x. Then D_P(x),D_P(y) are their marked downsets, and

    U_P(y)\U_P(x) = U_Q(y)\U_Q(x).

Hence SF1's two frontiers are computed exactly inside Q. The exterior-above-x condition is guaranteed by either:

1. x belongs to the genuinely exhausted permanent-memory set J;
2. a terminal row has x equal to the genuinely exhausted current pivot;
3. the full local degree of x is at most9 and its internal Q incomparable degree is already9.

Case3 leaves no exterior incomparable partner; ideality leaves no exterior predecessor, so all exterior labels are successors. The condition is NOT inferred from a zero in one arbitrary conditioned word. In the 353 mapped replacements, the classification is 182 degree-saturated unconditional rows and 171 actual-memory/terminal rows (with overlap possible in the reasons; the stated partition gives saturated priority).

The same swap also retains the literal order of all exterior labels, since it swaps two Q marks only. Thus SF1 can, if desired, be read as an exact count inequality separately in each actual exterior-word fibre, then summed with its actual completion counts. It is not a uniform mixture of deadline vectors. For the formal deadline outer domain, h_x=0 likewise realizes a synthetic exterior chain entirely above x, giving the same swap proof without any table.

## SF3. Mapping algorithm and source identity

Input is the unmodified local source packet

    ../d9-certificate-mining-20261110/ORIGINAL_V_FIRST_PACKET.json

SHA256 31d4fd6c3c8b9f02ade216df030037978b8a71af3021be423246aa02c7a52fa1.

SINGLE_FRONTIER_CENSUS.py loops over existing non-switch rows, not deadline profiles. It checks every marked incomparable pair oriented opposite the stored word T. It requires exterior-above-x by SF2, computes the exact marked frontiers, accepts only total frontier size<=1, and checks the blocker event(s) also reverse T. The first valid choice is stored, with its old bank for comparison, in SINGLE_FRONTIER_REPLACEMENTS.json. Source row type and all routes are retained. A critical case is stored as the harmless weight2 singleton, though weight1 also suffices.

Run:

    python SINGLE_FRONTIER_CENSUS.py

Expected metadata totals:

    total3469, proved353, mode0=182, mode1=171,
    stage0=347, stage2=4, stage4=1, stage6=1.

This classification is finite metadata bookkeeping, not a replacement certificate table: the mathematical payment is uniformly SF1, independent of all cap values and completion counts. Do not call this a proof of the remaining3116 bank rows, a new phase-termination theorem, or a replacement of structural coverage.

## SF4. Three final-phase seed terminal rows are one mechanism

At the starts of the label4 phases the seed arrays are

    (0,0,1,1,3,7,7),
    (0,0,1,1,3,7,7,39),
    (0,0,1,1,3,7,7,55).

Labels0,1,2,3 are a,b,u,v and label4 has full downset{a,b}. At terminality label4 has no exterior incomparable. Taking x=4,y=v gives

    D(4)\D(v)={b},    U(v)\U(4)=empty.

The unique lower-frontier event is v before b. Every surviving seed word puts b before v before4. Thus

    2Pr(4 before v)+Pr(v before b)>=1

excludes all four starting reference rows at once, including the two symmetric words of the seven-label seed. This replaces even the source's two-event row in the 39 seed without special weights. It uses the ORIGINAL event v before b, not a majority assumption on a conditioned helper.

## SF5. Optional bounded-cardinality companion

If D(x) subset D(y) and k=|U(y)\U(x)|, one also has

    Pr(x before y) >= 1/(k+2).                         (SF5)

To prove it, take a bad word y...x and list z0=y,z1,...,zr, the y-successors strictly between them. They all lie in U(y)\U(x), since none can be an x-successor before x. Move x to y's old position and shift each zi to the next listed position, with zr to x's old position. The move of x crosses no predecessor by D(x) subset D(y). No shifted zi crosses an unlisted successor, since such a successor would itself lie in U(y) between y,x and hence be listed. The result is legal and has x before y. Given the output and the last shifted label zr in {y} union(U(y)\U(x)), the reverse rotation is unique. Hence bad words inject into at most k+1 copies of good words. This proves SF5; the order-dual version interchanges lower and upper defects. It recovers58 source-row exclusions using at most one total individual defect, but the frontier version above subsumes all58 and more. Do not add their counts.

## Remaining private-chain diagnostic, NOT a new theorem

The exact 70-internal-word/gap count in N4_DIAGNOSTIC.py independently reproduces the n=4 source banks on5250 profiles, with minimum integer margins9 and124. This remains only a diagnostic replay. It observed positive unnormalized finite differences in the u deadline for both banks; no analytic monotonicity proof or whole n=4 replacement is claimed. Other coordinate differences have both signs, and probability-coordinate monotonicity also fails for several axes, so blanket corner/Jensen compression is unsupported. The n=2 private-chain tree and the full n=3 incidence-set payment still remain.

## SF6. Genuine D10 control against changing the four-chain caps

The n=4 old bank cannot be transferred by merely changing the two leaf caps4 to5 and the private-chain cap6 to7. Take the same seven-mark ideal a<u,v and b<c<d<e, and append an actual seven-chain z1<...<z7 with x<zj exactly when h_x<j, where

    h=(0,2,0,5,2,5,7) on (a,b,u,v,c,d,e).

Take transitive closure and no additional comparisons. This is a genuine14-point poset with exactly two minima, Delta10 and private ideal P\up(a) exactly the four-chain b<c<d<e. The independent full-poset ideal-subset recursion in D10_N4_REAL_CONTROL.py yields

    N=4282, K_ba=1577, K_vc=1197,
    3(K_ba+K_vc)-2N=-242.

Hence the old bank [ba]+[vc]>=2/3 itself fails on an actual degree10 object. Moreover increasing h_u from0 to1 doubles each displayed count, giving margin-484 and increment-242: the observed D9 u-axis monotonicity does NOT extend to the full D10 cap domain. This example has a balanced pair a,b (1577/4282 lies in the balanced interval); it is not NB, not a minority-private-four-chain counterexample and not a counterexample to ordinary balance. It only stops the mechanical bank/cap transfer and the stronger u-monotonicity claim.

## SF7. Next structural barrier, author metadata diagnostic only

For each existing row, minimize total frontier size among reverse pairs whose exterior-above-x condition is structurally available and whose entire frontier event library also reverses T. The resulting author diagnostic is:23 rows have minimum0,330 minimum1,1018 minimum2,23 minimum3,2075 have no eligible pair. Thus23+330=353 agrees with SF3, while the remaining3116 split as1041 multi-blocker rows and2075 rows outside this swap interface. This minimum statistic has not received the separate mapping audit applied to the353 replacement rows.

This is a useful stopping line, not another payment theorem. With two blockers the universal mechanism gives only2p+q+r>=1, whereas a total-weight4 one-third bank would require>=4/3. More application of the same union bound supplies no missing third. New information on the actual good-side swap failures, joint blocker events, or a different remembered interface is required.
