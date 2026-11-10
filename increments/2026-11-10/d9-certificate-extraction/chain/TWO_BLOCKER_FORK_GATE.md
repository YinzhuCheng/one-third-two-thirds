# A degree-free two-blocker fork gate, and its exact three-event stopping line

2026-11-10. Author analytic result; internal independent review PASS in TWO_GATE_INDEPENDENT_REVIEW.md. This is an analytic replacement mechanism for source banks in Kevin Fathi v22 §24.4.1, not a new ordinary-balance class or whole-phase closure. It uses the already-employed actual first-exterior-cut method, not a new probability law.

## FG1. Uniform gate theorem (expanded contract)

Let Q be an ORIGINAL ideal of a finite poset P with labels a,b,u,v and an induced tail H. The complete relations inside Q are:

- a<u and a<v; b is incomparable with a,u,v;
- every element of H is above u (hence above a) and incomparable with v;
- the internal order on H is arbitrary;
- b may lie below any up-closed subset of H, and there are no other relations.

Assume every exterior label lies above v (and hence above a). Write B_H={h in H:b<h} for the common tail and C_H=H\B_H for its private ideal. Impose either of two structural gates:

(D) **Delayed common tail:** no minimal element of H lies above b; OR
(M) **Supported common tail:** all but at most two elements y of B_H can be matched to distinct elements x of C_H with x<y.

Both permit arbitrary |H| and are generally incomparable. The small-tail case |H|<=2 with arbitrary b-to-H relations is a COROLLARY of(M), not a third disjoint gate or an additive coverage count.

Then the uniform extensions of this SAME original P satisfy

    2 Pr(u before b) + Pr(v before u) >= 1.             (FG1)

There is no degree, width or exterior-size restriction. The two named events are fixed before any exterior word or prefix cell is sampled. Whenever a candidate strict-two-thirds order has b before u before v, both are reverse events and FG1 excludes that reference under ORIGINAL NB.

### Actual-prefix proof

If the exterior is nonempty, condition on I, the exact Q set before the first exterior letter, and the entire literal suffix starting at that letter. This yields a uniform word on the induced ideal I with no arbitrary reweighting. If the exterior is empty take I=Q. In every cell a,v belong to I.

If u is absent, v before u has probability1 and pays. If u is present but b absent, u before b has probability1 and pays. Otherwise I contains a,b,u,v and an ideal K of H, of size k.

Fix one linear extension sigma of K. Let j be the rank in sigma of its first b-successor, or j=k+1 if there is no b-successor. Delete b. The resulting marked word is a,u followed by sigma, with v in one of the k+2 positions after a. Count b insertion slots exactly, rather than treating deletion words as uniformly distributed.

- If v is before u (one position), there are n=j+3 legal b slots, of which j put u before b. The v-before-u event holds for all n. The contribution to2K_ub+K_vu-N is2j.
- If v is after u but before the first b-successor (j positions), n=j+3 and K_ub=n-2=j+1. Each such word contributes j-1.
- If v is after the first b-successor (k+1-j positions), n=j+2 and K_ub=j. Each such word contributes j-2.

The convention j=k+1 handles the absence of a b-successor: all k+1 positions after u are in the second case and n=k+4. Summing gives the exact fixed-sigma margin

    M(k,j) = (k+4)j - 2(k+1).                         (FG2)

For the small-tail corollary, j>=1 gives M(k,j)>=2-k>=0. Under(D), if a b-successor occurs in K it has an H-predecessor, which also belongs to the ideal K. Thus the first such successor has j>=2 and M(k,j)>=6. If no successor occurs, j=k+1 and M=(k+1)(k+2)>0. This includes k=0 separately, with margin2.

Under(M), put r=|K intersect B_H| and c=|K intersect C_H|, so k=c+r. Every matched common point in the ideal K brings its distinct private predecessor with it. At most two common points were unmatched. Hence r<=c+2 for EVERY such K.

Here is the elementary rank estimate needed to sum FG2:

    E_sigma J >= (k+1)/(r+1),                         (FG3)

where sigma is a uniform linear extension of K and J its first common rank (J=k+1 when r=0). This uniform sigma is used only to express the sum of raw margins; it is NOT the induced b-deletion law.

To prove FG3, first note that any ideal C of size c in a k-element poset has first-letter probability at least c/k. Fix the two internal color words. From a legal shuffle starting in the other color, mark any of its c C-letters, exchange its color with the first color and restore both internal orders. All named C-letters move weakly earlier and the other letters weakly later; since C is an ideal, legality is preserved. The output starts in C, and the marked other-color position gives at most r inverse choices. Thus c*N_other-first<=r*N_C-first, giving the asserted bound after summing actual counts.

After a particular initial private prefix of length t, the remaining private set is still an ideal of size c-t in a uniform remaining extension on k-t letters. Therefore

    Pr_sigma(J>t) >= (c)_t/(k)_t,   0<=t<=c.

Summing tails and using (c)_t/(k)_t=binom(k-t,r)/binom(k,r) yields

    E_sigma J >= sum_(t=0..c) (c)_t/(k)_t
              = binom(k+1,r+1)/binom(k,r)
              = (k+1)/(r+1).

The r=0 case is exactly J=k+1. Consequently the average of FG2 is at least

    (k+1)(c-r+2)/(r+1) >= 0.

Sum the raw margins over sigma and then over the actual prefix/suffix cells. This proves FG1 without a uniform-deletion assumption or NB on a helper. The color/depletion argument is the same established ideal-first-color mechanism, not a newly claimed probability principle.

### Why one matching checks every prefix ideal

Condition(M) is equivalent to r_K-c_K<=2 for every ideal K of H. One direction is the matched-predecessor argument above. Conversely take any subset S of B_H and let K be its full down-closure inside H. The private vertices of K are exactly the private predecessor neighborhood N(S), and K contains S, so |S|-|N(S)|<=r_K-c_K<=2. Hall's theorem after adjoining two dummy private vertices adjacent to every common vertex gives a matching leaving at most two common vertices unmatched. This is equivalence for this prefix-count sufficient condition, NOT equivalence to all possible ways the bank might pay.

The gates(D),(M) are not nested: one private minimal label below four common leaves satisfies(D) but has matching deficiency3; two common minimal labels satisfy(M) but violate(D).

A still more general exact sufficient condition is: for every possible K,

    (k+4) sum_(sigma in LE(K)) j(sigma) >= 2(k+1)e(K).

This is a combinatorial average of the integer margin above, NOT an assertion that sigma has a uniform induced deletion law. No further general satisfaction of this condition is claimed.

### Full-support special case and sharpness

If b is below every label of H, each nonempty K has j=1. For each fixed K-word the exact counts reduce to

    N=e(K)(3k+8), K_ub=e(K)(k+3), K_vu=4e(K),
    2K_ub+K_vu-N=e(K)(2-k).

Thus the r<=2 bound is sharp for THIS full-b-support subclass and this bank: P=Q with three tail labels gives margin -e(H). This does not refute the two unrestricted-size gates: a three-label full common tail violates both(D) and(M).

### Reading this gate from a larger remembered state

Let Q_mark be the currently retained original ideal and suppose v is genuinely exhausted (or its marked incomparable degree already equals the full degree bound). Then every actual exterior label is above v. Set

    Q_v=Q_mark\U_Q_mark(v)=P\U_P(v).

This is a full ORIGINAL ideal. The removed marked successors of v may be included in the actual exterior of this auxiliary ideal because they really are above v. If Q_v has the displayed a,b,u,v,H structure, FG1 applies in the same P. This is analytical conditioning only: it does not delete remembered marks from the phase state, change the original P, or license forgetting later pivot constraints.

### Source coverage and deduplication

SUPPORTED_GATE_CENSUS.py and SUPPORTED_GATE_REPLACEMENTS.json identify62 existing source bank rows meeting(D) or(M), all in phase0, mode1. Of these25 already lie in the353 single-frontier replacements,33 lie in the1018 minimum-two-frontier family, and four additional rows on (0,0,1,1,5,7,7) have minimum frontier size3. Thus the **net addition is37**, and the union with the former353 is390, not415. Metadata audit is reported separately; payment is the uniform analytic argument above, not a cap-profile enumeration.

The earlier34-row delay/small-tail census (25 old plus9 new) is a proper preliminary subset and is NOT added again. The small-tail condition is already subsumed by(M).

For example, the terminal shape(0,0,1,1,7,7) has two reference words, interchanging4,5, and both source banks are exactly2Pr(u<b)+Pr(v<u)>=1. The mixed b-support shape(0,0,1,1,5,7) is also covered. In every mapped row the charged original events u<b and v<u reverse the same stored T; no change of event after seeing the exterior word is allowed.

## FG2. Genuine six-point obstruction to retaining only the original two-blocker summary

Take P=Q=(0,0,1,1,7,7). This is a real six-point poset, with precisely two minima a,b, private ideal P\up(a)={b}, maximum incomparability degree4, and empty exterior. Thus it is genuinely terminal at v, not an invented mixture or an h=0 switch.

For the reverse anchor x=v=3,y=u=2,

    D(x)=D(y)={a},
    max(D(x)\D(y))=empty,
    min(U(y)\U(x))={s,t}={4,5}.

Its actual extension counts are

    N=28,
    K_(v<u)=8,
    K_(s<v)=K_(t<v)=9,
    K_(s<v and t<v)=6.

Every one of these three reverse comparisons, and even their blocker intersection, has probability strictly less than1/3. Therefore NO nonzero nonnegative bank supported only on (v<u,s<v,t<v), or on those plus the intersection treated as another event known below1/3, can reach one-third on all posets of this exact interface: this ONE actual poset already defeats it. Any true correlation constraint using only this summary must admit this point, so cannot imply that one of the three comparisons is balanced. This is stronger than a bad cross-poset mixture.

The good-side swap-failure count is0. The exact swap identity reads

    2*8+9+9-6=28.

Thus remembering the exact joint blocker intersection or the good-side failure alone does not repair the lost1/3 payment. The ordinary union-bound bank value is34/28=17/14, below the required4/3 for total weight4.

FG1 escapes by adding the different original event u<b, whose count here is10. The resulting bank is exactly tight:2*10+8=28. In this poset s,t are fair twins and several other comparisons are balanced. This is NOT an NB or ordinary-balance counterexample.

The elementary count is the k=2 instance in FG1. Separately, TWO_BLOCKER_REAL_CONTROLS.py reconstructs all full words and exact swap failures. It also records a mixed lower/upper-frontier control on (0,0,1,1,5,7), with N33 and counts9,8,10 on(v<b,b<a,5<v), all below11, joint blocker count3 and zero good-side swap failure. Neither construction changes any external service.

## FG4. Exact degree-nine stopping line at matching deficiency3

This is a COMMON-BANK obstruction, not a failure of ordinary balance or an individual NB law. Keep the same seven marked physical labels

    Q pred=(0,0,1,1,7,7,7),

so H is a three-element common antichain above b,u, with no private H points and matching deficiency3. Add the SAME six exterior physical labels as a chain z1<...<z6. Realize x<zj exactly when h_x<j, taking transitive closure. Two actual thirteen-point completions are

    P0: h=(0,0,0,0,0,0,0),
    P1: h=(0,0,6,0,6,6,6).

Both have precisely two minima a,b, singleton private branch{b}, and all exterior above v. Their actual full-poset counts, for A={u before b}, B={v before u}, are

    P0: N102,  KA36,   KB24,   Delta5;
    P1: N6948, KA1728, KB4284, Delta9.

The exact full ideal-subset counter is SUPPORTED_GATE_DEFECT3_CONTROL.py; it reconstructs the relations and degrees rather than just accepting a probability table. In the convex mixture of the two NORMALIZED extension laws with weights4/5,1/5,

    Pr_mix(A)=5448/16405,
    Pr_mix(B)=5111/16405,
    max=1/3 - 61/49215 < 1/3.

Therefore no nonzero nonnegative bank on ONLY these two fixed original events can pay at one-third simultaneously on the two real degree<=9 completions. In particular the supported-tail lemma cannot be extended to arbitrary matching-defect3 tails merely by retuning its two coefficients. This excludes a uniform bank based only on the larger interface, not every possible exact structural extension of the theorem: retaining more original information or adding events could still work.

The two components are different original posets. Their mixture is not shown to be any single original P law and no NB assertion is made. Each component has obvious fair pairs in the three twin tail labels, so this is not a counterexample to ordinary balance. The numerical weights are weights of extension LAWS, not weights of deadline vectors or uniform choices of deletion words.
