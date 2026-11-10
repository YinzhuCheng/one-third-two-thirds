# Independent review: two-blocker first-cut gate and actual summary obstruction

2026-11-10. Internal independent mathematical review and separately implemented metadata audit, not external peer review or formal verification. **PASS** with the exact scope below.

## Gate statement checked

Let Q be an original induced ideal of a finite P, with labels {a,b,u,v} union H. Its relations on the four special labels are exactly a<u,a<v; every element of H is above u and incomparable with v. The induced H is arbitrary, and b may precede any upper-closed subset of H. Assume every original exterior label lies above v. Suppose either no minimal element of H lies above b, or the following Hall condition holds: all but at most two members of R=H intersect U(b) can be matched to distinct strict predecessors in C=H minus U(b). The small-tail condition |H|<=2 is included in the Hall condition. Then under the uniform extension law of this same original P,

    2 Pr(u precedes b) + Pr(v precedes u) >= 1.

This is a fixed two-event bank, total weight3, hence an exact one-third bank. It excludes any candidate strict-two-thirds reference placing b before u before v. No other reference is asserted excluded by this particular bank. There is no degree, width or exterior-size restriction in the lemma.

## Independent proof audit

Condition on the exact set I preceding the first exterior label and on the entire literal suffix from that label onwards. If the exterior is empty use I=Q. Every such nonempty-exterior cell contains a,v because v precedes all exterior labels and a<v. The internal I word is uniform: all e(P[I]) orders followed by the fixed suffix are legal, and no extra weight is assigned. This is the pre-existing first-exterior-cut mechanism, not a new probability law.

If u is absent from I, v<u holds deterministically. If u is present and b absent, u<b holds deterministically. Otherwise I={a,b,u,v} union K, with K an ideal of H and k=|K|. Fix one extension w1,...,wk of K and sum counts over its placements with a,b,u,v. After deleting b, the word without v is a,u,w1,...,wk. The possible v positions are s=0,...,k+1 after a, where s=0 puts v before u and s>=1 puts v after u and after s-1 tail labels.

Let j be the first index with b<w_j, or j=k+1 if there is no such index. For s<=j, the number n of b slots is j+3; for s>j it is j+2. This includes the no-successor case: all s then satisfy s<=j, and n=k+4. The rank of u in the deletion word is3 if s=0 and2 otherwise. Thus the contribution to 2K_(u<b)+K_(v<u)-N is n(1+1[s=0])-2 rank(u). It is respectively2j, j-1, j-2 on s=0, 1<=s<=j, s>j. The full contribution for this fixed internal K word is exactly

    2j + j(j-1) + (k+1-j)(j-2)
      = (k+4)j - 2(k+1).                              (*)

For k<=2 and j>=1 this is at least2-k>=0. For arbitrary k, if there is no b-successor the value is(k+1)(k+2)>0. Otherwise, under the no-common-minimum hypothesis, the first b-successor w_j has a predecessor in H. Since K is an ideal, that predecessor lies in K and appears earlier in the fixed word. Hence j>=2 and (*)>=6. This proves the unbounded-tail extension, including k=0, without a finite case table.

The argument proves the bank separately for each fixed K word, so there is no assumption that different K words or different prefix/suffix cells have equal probability. Summing their actual completion counts and then summing the actual cells gives the original-P bank. No NB assumption is made on a conditioned helper.

## Rank-average/Hall extension independently checked

For a fixed prefix ideal K write c=|K minus U(b)| and r=|K intersect U(b)|, so k=c+r. Let J be the first common-label rank in a uniformly sampled internal extension of K, with J=k+1 if r=0. This is an auxiliary uniform internal-order average for summing the signed counts in (*), NOT the marginal law of K-orders in the original P after inserting b and v.

The private subset C_K=K minus U(b) is an ideal. In any finite poset of size k with an ideal C_K of size c, Pr(first label lies in C_K)>=c/k. To verify this, fix the internal orders of the ideal and its complement. Legal color shuffles are closed under moving the ideal color earlier, since there is no relation from the complement down into the ideal. From a legal shuffle starting with the other color, mark any of the c ideal-color positions, exchange its color with the first color, and restore the two internal orders. The result is legal and starts with the ideal color. Mark the exchanged other-color position in the output. The marked output uniquely determines the input; there are r possible output marks. Thus c*N_other <= r*N_ideal, proving the bound in each fixed-internal-order class and hence overall.

Conditioning on any literal first t labels all in C_K leaves a uniform residual poset whose remaining private set is an ideal of size c-t. Iterating the bound therefore gives

    Pr(J>t) >= (c)_t/(k)_t  for 0<=t<=c,
    E J >= sum_(t=0)^c (c)_t/(k)_t = (k+1)/(r+1).

The final finite-sum identity is the mean first-success rank in the uniform shuffle of c private and r common letters; equivalently it follows by the standard binomial tail sum. It also includes r=0 with the specified sentinel J=k+1.

Averaging (*) over the e(K) internal orders now gives a signed-count lower bound per internal order of

    (k+4)E J - 2(k+1)
       >= (k+1)(c+2-r)/(r+1).

Consequently r<=c+2 for every prefix ideal K suffices, without a tail-size bound. The stated Hall matching implies this: each matched common element of K has its distinct matched private predecessor in K, since K is ideal; only the at-most-two globally unmatched common labels can remain unpaired.

In fact this matching condition is equivalent to the cardinal condition r_K-c_K<=2 for every ideal K of H. Hall deficiency is max_(S subset R)(|S|-|N(S)|), with N(S) all private predecessors of S. A violating S has an ideal downward closure K whose private part is exactly N(S) and whose common part contains S, giving an ideal violation. Conversely the matching implies the bound in every ideal as above. This equivalence concerns the sufficient count condition, NOT necessity of the bank itself. The no-common-minimum condition can pay by pointwise J>=2 even when the Hall condition fails, so those two analytic sufficient conditions should not be conflated.

## Independent source-tree mapping

TWO_GATE_INDEPENDENT_MAPPING.py independently searched the unchanged seven-phase packet, reconstructing each full downset/upset. For each structurally exhausted or degree-saturated potential v it took Q_gate=Q_source minus U_Q_source(v), which is exactly the part not already above v. It checked all four special-label roles, the tail relations, the no-common-minimum condition or an explicit maximum predecessor matching, and the same-reference inversion condition b before u before v. Taking this subideal is legal: every omitted marked label and every genuine original exterior label is above v.

Output: TWO_GATE_INDEPENDENT_MAPPING.json. The script independently rederived the full3469-row minimum-frontier classification directly from the source packet: no eligible pair2075, minimum0 in23 rows, minimum1 in330, minimum2 in1018, minimum3 in23. It does not rely on TWO_FRONTIER_ROWS.json for the33/4 split.

- **62** existing bank rows meet one of these gate conditions.
- **25** already belong to the353 single-frontier replacements.
- **37** are genuinely additional:33 belong to the1018 minimum-two-frontier group, and four have three frontiers.
- All37 new rows are terminal v rows; maximum source ideal size is10. Their bank endpoints a-independent b,u,v have full predecessor counts0,1,1, preserving M8 locality.
- The four new three-frontier rows are on predecessor array(0,0,1,1,5,7,7), with its four stored references satisfying b before u before v.
- Therefore the deduplicated union has**390** source bank occurrences, NOT353+62. The earlier nine-row result for only small-tail/no-common-minimum criteria is subsumed and must not be added.

These are metadata identities, not deadline-profile arithmetic. Formula(*) plus the ideal-color rank bound pays all actual completions in the structural class, including arbitrary-size H under either condition. No new row count alone proves structural phase coverage.

## Independent actual-P obstruction to the original three-event library

TWO_GATE_INDEPENDENT_CONTROL.py enumerates all6! permutations independently and keeps those extending the six-label poset with predecessor masks(0,0,1,1,7,7). Take P=Q, so the exterior is empty and terminality is genuine. For x=v=3,y=u=2 the lower swap frontier is empty and the upper frontier is{4,5}. The exact counts are

    N=28,
    K_(v<u)=8, K_(4<v)=9, K_(5<v)=9.

All three are strictly below N/3. Consequently no nonnegative one-third bank supported solely on these three events can hold across even this actual structural class. This is not a speculative mixture and does not require combining laws from different P. It does not refute ordinary balance or the original tree: K_(u<b)=10 and K_(4<5)=14, so there are already balanced pairs, and adding the event u<b gives precisely2*10+8=28, the new gate bank at equality.

For clarity about joint information, the two upper blocker events intersect in6 words. There are no good-side swap failures here, and

    2K_(v<u)+K_(4<v)+K_(5<v)=N+6=34,

which is still below the4N/3 threshold required by that total-weight4 template. True joint-event information therefore does not repair this particular three-event library; a different event, such as u<b, is necessary for this example. Global NB is not claimed for P.

## Independently verified deficiency-three stopping line

TWO_GATE_DEFECT3_INDEPENDENT.py constructs two complete13-point posets on the SAME seven-label ideal Q with predecessor masks(0,0,1,1,7,7,7) and the SAME six exterior chain labels z1,...,z6. Put x<z_j exactly when h_x<j, plus the chain relations, with no extra comparisons. The two deadline vectors are

    P0: h=(0,0,0,0,0,0,0),
    P1: h=(0,0,6,0,6,6,6).

Both exteriors are genuinely above v, and the tail consists of three common antichain labels and no private tail labels, so Hall deficiency is exactly3. The independent full-poset forward ideal DP gives, for A={u before b}, B={v before u},

    P0: N102, K_A36, K_B24, Delta5, 2K_A+K_B-N=-6;
    P1: N6948, K_A1728, K_B4284, Delta9, margin792.

Their event probability vectors are(6/17,4/17) and(48/193,119/193). The convex mixture with law weights4/5 and1/5 gives

    (Pr(A),Pr(B))=(5448,5111)/16405,

and both coordinates are strictly below1/3 (3*5448=16344<16405 and3*5111=15333<16405). Therefore no fixed nonnegative one-third bank supported only on A,B can work across these two genuine same-Q degree-nine completions. In particular a universal enlargement of the sufficient Hall-deficiency cutoff2 to3 is false, and the original2A+B bank already fails at P0 itself.

This is a mixture of two actual extension LAWS, not a claimed law of one original P and not an NB counterexample. Each component has a balanced comparison. In fact the three tail leaves are twins in each component, so every tail-leaf pair remains fair even in the mixture; a full event library has an immediate common bank. The obstruction is specifically to retaining only A,B, not to full-Q payment, the D9 theorem, or every structural class with deficiency above2. The separate no-common-minimum sufficient condition can still apply when the matching deficiency is large.

## Source and status discipline

The fixed source is Kevin Fathi v22, https://zenodo.org/records/23933091, especially the occupied-position swap/direct-blocker mechanism in Theorem2.3 and the first-cut/original-law reasoning used in §24. The gate is an analytic reorganization using these existing tools, not a historical originality claim. It is an additional37-row payment replacement within the supplied tree after deduplication, not full seven-phase or all-D9 analytic closure.
