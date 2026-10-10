# S110: One buffered splice preserves actual pair probabilities approximately

Date: 2026-10-10. Status: a proved sufficient one-splice lemma, not a uniform finite-counterexample theorem. This file is independent of any conjectural point bound.

## 1. Precise statement and the essential qualification

Fix an integer D >= 1. Set

- R = 2D - 1 (incomparability span),
- h = R + D = 3D - 1 (observation/output-rank guard),
- K = h + D = 4D - 1 (reference-label buffer half-width).

Let P be a finite poset of maximum incomparability degree at most D, with a fixed reference linear extension labelled 1,...,n. Let a < b be reference cuts, with

  a >= K,   b + K <= n,   L = b - a >= 2K + 1.

These assumptions deliberately exclude overlapping buffers and cuts whose buffers would extend beyond the physical endpoints (touching them is allowed). The large separation is a convenient sufficient hypothesis, not an optimized one; Section 9 shows why a separation condition cannot simply be dropped when preserving all surviving actual pairs. Require that translation by L identifies the complete induced relation patterns on

  U_a = [a-K+1,a+K],     U_b = [b-K+1,b+K].

In particular every comparison/incomparability between two offsets in these intervals agrees. One may also require the finite legality automaton to have the same state at cuts a,b; under the buffer assumption above the direct legality proof below already suffices.

At output rank r, let F_r(S) and B_r(S) be the true numbers of prefix extensions and suffix completions at the legal ideal state S, as in bounded_range_frontiers.txt. Use relative window coordinates [-D+1,D] to identify states. These vectors are indexed by all legal size-r ideal states; every such coordinate is positive. Write hat F and hat B for their separate l1 normalizations.

The profile hypothesis needed by this theorem is the following BUFFERED hypothesis, not merely central matching of F_a,F_b and B_a,B_b:

  (1-eta) hat F_(a-h)(S) <= hat F_(b-h)(S) <= (1+eta) hat F_(a-h)(S),
  (1-eta) hat B_(a+h)(S) <= hat B_(b+h)(S) <= (1+eta) hat B_(a+h)(S),

for every corresponding legal coordinate, where 0 <= eta <= 1/2. Local buffer equality makes both pairs of supports identical. Thus a sufficient fixed-dimensional cut profile is

  Psi(c) = (hat F_(c-h), hat B_(c+h), relation pattern on U_c).

Matching all profiles at every offset |t| <= h is an alternative, stronger condition. The theorem does NOT assert that central matching alone implies the buffered hypothesis. Such an assertion would require a separate observability argument; nonnegative transfer matrices cannot in general be inverted to deduce it.

Delete the R-local encoding symbols at positions a+1,...,b and decode the remaining word, as specified in Section 2, to obtain P' on n-L new reference labels. Give its retained labels their actual identities by

  rho(i) = i if i <= a, and rho(i) = i+L if i > a.

Then:

1. P' is a genuine poset with maximum incomparability degree <= D and with 1,...,n-L as a reference extension.
2. All relations within either retained side agree with P on the corresponding actual identities.
3. For any actual surviving incomparable pair entirely on the left or entirely on the right, its directional probability under the UNIFORM law on extensions of P' differs from its directional probability under the original UNIFORM law on extensions of P by at most eta. (In fact all same-side pair events obey the bound.)
4. Every new incomparable pair u <= a < v of P' has a genuine incomparable comparison witness (u,v) in P, both labels in U_a, and its directional probability differs from this witness's original probability by at most eta. Here the witness label v need not be a retained actual identity: its retained replacement has original identity v+L. This distinction is necessary and explicit.

Consequently, if every incomparable pair of P has min(p,1-p) < 1/3 - gamma and eta < gamma, then P' again has no balanced pair. Without a uniform positive gamma, this gives no uniform size bound.

## 2. Exactly what is spliced

Encode each position j by its comparison/incomparability bits with j-t, 1 <= t <= R; distances greater than R are forced comparable in increasing reference order. Beginning padding is unchanged because a >= K. Delete the symbols a+1,...,b, interpret the surviving bits at their new distances, and force every new-label pair at distance > R comparable.

This is an encoding splice, NOT generally the induced subposet obtained by simply deleting vertices. For pairs on one retained side, offsets and bits are unchanged, so their old relations persist. Across the seam, short-range bits are transplanted, and new incomparabilities may appear. The original actual endpoints of such a new pair were separated by L and hence were comparable in P. Ignoring this would miss precisely the potentially dangerous new witnesses.

Let Q be the relation obtained by this decoding. Any local relation near the seam agrees with the relation in P around a under the numerical-label map i -> i, or with the relation around b under i -> i+L, as appropriate. In particular, for any two new labels in [a-K+1,a+K], their Q relation is the old P relation between those same numerical labels: on the left this is literal, on the right it follows from buffer translation, and across the seam the encoded bits at b+q equal those at a+q by buffer equality.

Legality can be checked directly. Reference order prevents directed cycles. A transitivity violation i<j<k with i<_Q j<_Q k but i parallel_Q k must have k-i <= R, because longer pairs are forced comparable. If its labels lie on one side, it would already violate P. If it crosses the seam, its labels lie in [a-R+1,a+R], where the relation is a copy of a genuine P relation, impossible.

For degree, a vertex with no new cross-seam neighbour sees exactly its old-side neighbours and possibly fewer than before. A vertex incident to a new cross-seam incomparability lies in [a-R+1,a+R]. All of its potentially incomparable neighbours lie in [a-2R+1,a+2R], which is within the matched buffer because K >= 2R. Its entire new incomparability neighbourhood is therefore a copy of the neighbourhood in P around the corresponding vertex near a. Its degree is at most D. Thus Q=P' is legal.

## 3. Exact transfer and identity matching, including output-rank drift

Let T_r be P's true ideal-state transfer at output rank r, and T'_r the corresponding transfer for P'. Every transition inspects only reference labels in

  [r-D+1,r+D+1].

Labels farther to the left have already been output; labels farther to the right cannot yet be output. It follows from the same-side identity and the matched relation buffer that

  T'_r = T_r                       for 0 <= r < a+h,
  T'_r = T_(r+L)                   for a-h <= r < n-L,

with the appropriate relative-window state identifications. The two formulas overlap. In this overlap T_r=T_(r+L), exactly because all inspected labels fall within the matched buffers. The boundary bounds are exact: the last prefix transfer r=a+h-1 inspects no label greater than a+h+D=a+K; the first suffix transfer r=a-h inspects no label less than a-h-D+1=a-K+1.

Initial and final states are the unchanged actual endpoint states. Hence, putting c=a-h and d=a+h,

  F'_d = F_d,
  B'_d = B_(d+L),
  F'_c = F_c,
  B'_c = B_(c+L).

These are exact counts, not normalized substitutes. In particular

  e(P') = F_d dot B_(d+L) = F_c dot B_(c+L).

All coordinates and both denominators are positive. There is no resetting of the conditional law at the seam.

Identity handling for observables is as follows.

- In a prefix through output rank d, every output reference label is <= d+D=a+K. Under the first transfer identity, it corresponds to the same numerical label in the original P. Labels <=a are the same actual vertices; labels >a are local clones for this comparison.
- In a suffix after output rank c, every vertex not already output has reference label >= c-D+1=a-K+1. Under the second transfer identity it corresponds to the old numerical label plus L. Labels >a are the same actual retained vertices; the possible labels <=a are local clones.
- A vertex of new reference label i is output at a rank in [i-D,i+D]. This holds in both P and P', since each has degree <=D. Therefore a same-side left pair is fully observed by d. A right pair's two vertices are not output before or at c, since their least reference label is >=a+1 and a+1-D>c. A new cross-seam incomparable pair satisfies v-u<=R, hence v<=a+R, so both endpoints have been output by d=a+R+D.

These guard statements are why the theorem uses buffered endpoint profiles. No direction fact about a fixed actual pair is forgotten or silently assigned to a moving window position.

## 4. Reweighting lemma with the common completion weights retained

Let an original finite probability law have atoms omega with nonnegative weights w(omega). Give the same atoms new weights w(omega) t(omega), where m <= t(omega) <= M and 0<m<=M. For any event A, the difference of normalized probabilities is at most

  (sqrt(M)-sqrt(m))/(sqrt(M)+sqrt(m)).

Proof: write p for the old event probability, u and v for the conditional averages of t on A and its complement. Then q=pu/(pu+(1-p)v). Its largest possible upward displacement takes u=M,v=m; maximize over p. The downward bound is the same with the roles reversed. Null events cause no issue.

For m=1-eta and M=1+eta, this upper bound is

  eta/(1+sqrt(1-eta^2)) <= eta.

A simpler bound sufficient for eta<=1/2 is |q-p|<=eta/[2(1-eta)]<=eta, obtained from |u-v|<=2eta and p(1-p)<=1/4.

Apply this first at d. The old atom is an entire prefix extension of length d ending at state S, with its true weight B_d(S). Its new weight is B_(d+L)(S). The profile hypothesis gives a common scalar beta>0 such that

  B_(d+L)(S)/B_d(S) = beta t(S),    1-eta <= t(S) <= 1+eta.

The scalar beta cancels only after normalizing the complete law. The factor B_d(S) is retained throughout. Every prefix event, including a pair direction, thus changes by at most eta.

Apply the same argument at c to entire suffix extensions. The common exact suffix is the original suffix at c+L. The old weight of a suffix starting at S is F_(c+L)(S); the new one is F_c(S). Their coordinatewise ratio lies, after a common scalar is removed, in [1/(1+eta),1/(1-eta)]. This has the same ratio M/m and hence the same error bound as above. Every suffix event changes by at most eta.

Combining the output-rank and identity checks in Section 3 proves assertions 3 and 4. All comparisons use actual uniform-extension laws with their actual completion weights. There is no assertion that arbitrary independently chosen normalized profiles are realizable.

## 5. Absolute meshes: an explicit O_D(eta) version

The independent bounded-cut-ratio lemma gives

  C_D=(2D)!/D!,    N_D=binom(2D,D),
  m_D=1/[1+(N_D-1)C_D],

and every positive coordinate of either l1-normalized unmarked profile is at least m_D. See bounded_cut_profiles.md.

If the two required normalized profile pairs are within eta in coordinatewise absolute distance, their relative error is at most eps=eta/m_D. Therefore, for eta <= m_D/2, the theorem gives every stated probability error at most

  A_D eta,    A_D=1+(N_D-1)C_D.

The proof uses unmarked profiles only. It does not incorrectly apply C_D to direction-refined coordinates, which may vanish.

The cut data used here have at most 2N_D real coordinates, plus finitely many relation and legality types. Thus a finite mesh exists for every fixed (D,eta). This is a compactness/approximation statement, not an exact pumping statement.

## 6. Why this does not finish the finite-counterexample route

The one-splice error compares the original law with one shortened law. Repeating the splice is a new comparison, so errors can add. For k splices with errors eps_1,...,eps_k, tracing each final incomparable pair through actual original-side pairs or genuine cross-seam witnesses at each stage gives a direction-consistent ancestry and total error at most sum eps_i. The function p -> min(p,1-p) is 1-Lipschitz, so the same bound applies to balance.

A sufficient additional assumption is a known original strict balance gap gamma together with an authorized sequence of valid splices whose total certified error is <gamma. For example, a fixed bound k<=k_0 and per-step error <gamma/k_0 suffices; alternatively a summable schedule with sum eps_i<gamma suffices. Neither follows just from a fixed finite grid. Refining the mesh at every stage can make the error summable, but the number of grid cells then grows, so this does not yield a size bound depending only on D.

Even one splice preserving strict unbalance requires eta below the original instance's gap, unless one proves a sharper sign-preserving inequality. Such a gap may depend on unbounded extension counts. We prove neither a uniform positive gap nor a uniform bound on the required number of splices, and draw no uniform finite-counterexample conclusion.

## 7. Optional separate observation: uniformly positive long transfer blocks

For any two genuine legal states J at rank r and K at rank r+2D, the drift guards give

  J subset [r+D] subset K.

There is at least one extension of K\J, so every entry of the 2D-step transfer product, between its legal supports, is positive (and is at most (2D)!). This supplies a possible independent mixing route. It does not permit inversion of a transfer block and does not make a fixed-length buffer's nonzero mixing error equal to O(eta) as eta tends to zero. Any use of mixing to replace the buffered hypothesis must state and prove its own quantitative dependence on buffer length.


## 8. Exact rational actual-poset experiment

Files: check_single_splice.py and single_splice_exact_check.json in this directory. This is a validation example, not an exhaustive theorem proof or a new verified range of the balance conjecture.

Take the genuine connected path-incomparability poset P_40 with i<_P j iff j-i>=2, so D=2. Choose a=9,b=26. Then R=3,h=5,K=7,L=17, and all separation/interior hypotheses hold. The spliced input is exactly P_23. Original and new extension counts are respectively 165580141 and 46368.

There are two legal interior states, with masks (-1,0) and (-1,1). The normalized forward profiles at ranks 4 and 21 are

  (5/8,3/8),    (17711/28657,10946/28657).

The normalized backward profiles at ranks 14 and 31 are

  (196418/317811,121393/317811),    (55/89,34/89).

Neither pair is identical. Their exact maximal relative errors are

  eta_F=1597/85971,    eta_B=1597/10803977.

An ideal-state DP computes all counts using integers and all probabilities with exact rational arithmetic. Its answers were independently cross-checked against the Fibonacci identities

  e(P_n)=F_(n+1),
  Pr_(P_n)(i+1 before i)=F_i F_(n-i)/F_(n+1).

All 22 incomparable pairs of P_23 satisfy their appropriate one-splice bounds. The maximum observed probability error is

  140282077/7677619977888 ~ 0.000018271557775,

at new pair (10,11), whose surviving actual identities are old (27,28).

The new cross-seam pair (9,10) has old actual identities (9,27), which were comparable. Its correct old comparison witness is the genuine old incomparable pair (9,10). Its old-witness reversal probability is 45773146/165580141, its new reversal probability is 6409/23184, and their exact difference is

  1493195/3838809988944 ~ 0.00000038897340694.

This is an explicit test of the distinction between actual retained identities and comparison witnesses, rather than an experiment that accidentally treats the splice as an induced subposet.

## 9. Independent audit and an overlap negative control

An independent implementation in splice_independent_audit/check_splice.py, with exact output splice_independent_audit/exact_checks.json, verified the separated theorem on five periodic actual-poset cases with D=2,2,4,4,6, including every new cross-seam pair.

The same audit found and checked a negative control if the large-separation requirement is removed. Let P_101 have incomparable reference gaps exactly 1 and 3, and comparable gaps 2 and every gap >=4. This is a genuine poset of maximum incomparability degree 4: the smallest sum of two positive comparable gaps is 2+2=4, also comparable. Choose a=50,b=51, deleting one encoded symbol. All interior local buffers repeat, and the normalized buffered profiles are within relative error approximately 7.4109865e-7. But the old actual pair (49,52), formerly incomparable at gap 3, survives as new labels (49,51), now comparable at gap 2. Its old probability of 49 before 52 is approximately 0.8924256574; its new probability is 1. The change is approximately 0.1075743426.

Thus one cannot drop separation and still claim that all surviving OLD actual incomparable pairs retain their probabilities, even with tiny buffered-profile discrepancies and identical periodic local patterns. This counterexample does not refute the stated separated theorem and does not by itself decide the different central-only-profile question under the separated hypotheses.
