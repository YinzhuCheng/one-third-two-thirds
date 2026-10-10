# Exact structural reductions for a minimum-order 1/3–2/3 counterexample

Date: 2026-10-10. Scope: finite posets with the original uniform law on complete linear extensions. The elementary proofs below are self-contained. No claim is made that an arbitrary induced restriction has its own uniform law, or that a quotient by a chain module is itself a counterexample.

## 1. Definitions and quantifiers

Write L(P) for the set of linear extensions, e(P)=|L(P)|, and p_P(x,y)=Pr[x precedes y] under uniform L(P). A balanced pair has p_P(x,y) in the closed interval [1/3,2/3]. A counterexample is a nonchain P with no balanced pair.

Assume a counterexample exists and choose P of minimum cardinality among all nonchain counterexamples. More generally, the reductions below needing minimality only assume that every proper induced nonchain subposet of P has a balanced pair in its own uniform law. Merely saying that each one-vertex deletion is not a counterexample is not the hypothesis used here.

A nonempty subset M is an autonomous module if every x outside M is either below every member of M, above every member, or incomparable to every member. A nontrivial proper module has 2≤|M|<|P|. A prime poset has no such module. A chain module is an autonomous module whose induced order is a chain.

The comparability graph joins comparable distinct vertices; the incomparability graph joins incomparable vertices. Let π(P) be maximum incomparability degree when that parameter is used.

## 2. Uniform laws that genuinely lift

### 2.1 Autonomous internal law

For every module M, the restriction of a uniform extension of P to M is uniform on L(M).

Proof. Fix the ordered outside labels and the set of slots occupied by M in an extension. Because every outside vertex sees all of M in the same way, replacing the internal order in those slots by any other member of L(M) preserves validity. Thus every internal extension occurs once over each admissible outside-and-slot skeleton. The number of preimages is independent of the internal extension. In particular, p_P(x,y)=p_M(x,y) for x,y in M. This does not assert a uniform outside restriction or a uniform quotient law.

Consequence for minimum-order P: every proper nontrivial module is a chain. Otherwise a balanced pair of the smaller nonchain M lifts unchanged to P.

### 2.2 Ordinal sums

If P=P1⊕⋯⊕Pr, extensions are concatenations of independently chosen extensions of the factors, and e(P)=∏e(Pi). Each factor has its original uniform law.

If the incomparability graph is disconnected, its components admit a total order and P is their ordinal sum. To see this, cross-component vertices are comparable. Along an incomparability edge x∥x′, a vertex y in another component cannot lie strictly between x and x′, so the direction of comparison with y is constant. Connectivity propagates this to entire components; transitivity totally orders the components.

If all components are singletons, P is a chain. Otherwise a proper nonchain component supplies a balanced pair by minimality. Therefore the incomparability graph of a minimum-order counterexample is connected.

In particular there is no universally comparable vertex, no least or greatest vertex, and there are at least two minimal and at least two maximal vertices. In a finite poset a unique minimal vertex would be a least vertex, and dually.

### 2.3 Disjoint unions

For P=P1⊔⋯⊔Pr, choosing an extension of each factor and then a shuffle of the resulting fixed words gives every extension exactly once. If ni=|Pi| and n=Σni, then

  e(P)=n! ∏(e(Pi)/ni!).

Every component, and every union of components, has its original uniform internal law.

If the comparability graph of a minimum-order counterexample is disconnected, each component must therefore be a chain. Two nonempty disjoint chains always have a balanced cross pair; an elementary proof follows, avoiding any appeal to the width-two theorem.

Let their lengths be a≥b≥1, with labels A1<⋯<Aa and B1<⋯<Bb. Define

  qi=Pr[Ai precedes B1]=binom(a+b−i,b)/binom(a+b,b).

This event means that the first i letters in a uniform binary shuffle are all A. We have q1=a/(a+b)≥1/2. If q1≤2/3 we are done. Otherwise let i be the first index with qi≤2/3. Such an index satisfies i≤a−b+1, since

  q_(a−b+1)=binom(2b−1,b)/binom(a+b,b)≤1/2.

Also i≥2 and

  qi/q_(i−1)=(a−i+1)/(a+b−i+1)≥1/2.

Hence qi>1/3. This balanced pair in a union of two components lifts to all of P. Therefore the comparability graph is also connected.

## 3. Canonical strong-majority order and rigidity

These statements need no minimality: they hold for every hypothetical counterexample.

Define x≺y iff p_P(x,y)>2/3. Absence of a balanced pair makes this a strict total orientation. It is transitive: if x≺y and y≺z, the union bound gives

  p_P(x,z) ≥ p_P(x,y)+p_P(y,z)−1 > 1/3.

As p_P(x,z) cannot be in [1/3,2/3], it must exceed 2/3. Thus ≺ is a strict total order extending P.

Consequently every counterexample admits a unique canonical labelling v1,…,vn such that

  p_P(vi,vj)>2/3 for every i<j.

This sequence is itself a linear extension. Equivalently, counterexample search can use an all-forward strong-majority orientation after existentially choosing this canonical labelling. An arbitrary preselected reference extension need not have this property. Restricting a search to one all-forward cell without allowing the canonical relabelling would be unsound.

Every automorphism of P preserves extension probabilities, hence preserves ≺, hence fixes each vertex. Thus every counterexample is rigid.

The usual incomparable-twin exclusion is a special case: if distinct x,y have identical strict downsets and strict upsets, they are incomparable and their transposition is an automorphism. A direct swap bijection gives p_P(x,y)=1/2.

Two cautions:

- Equality of strict downsets alone does not force balance or probability 1/2. In C4⊔C1 the two minimal vertices share the empty strict downset, but the bottom of C4 precedes the isolated point with probability 4/5.
- A two-element autonomous chain is not a swappable twin pair. Its contraction requires the analysis below.

## 4. Exact weighted-prime representation

For a minimum-order counterexample P, let M1,…,Mr be its maximal chain modules, including singleton blocks when necessary.

### 4.1 They form a partition

Every vertex is in a chain module. If two chain modules A,B intersect, A∪B is a module: any outside vertex has the same relation to both modules because that relation agrees on a shared point. Their union is also a chain. Indeed, for x in A\B and y in B\A, choose z in A∩B. Since y and z are comparable, module A forces y to have that same comparison type with x. Thus x and y are comparable. Maximal chain modules therefore cannot overlap unless equal.

### 4.2 Their quotient Q is prime

Define i<j in Q iff every member of Mi is below every member of Mj. Relations between modules are uniform, so P is exactly the chain inflation

  P = Q(C_w1,…,C_wr),  wi=|Mi|≥1.

If a proper nontrivial subset S of quotient vertices were a module of Q, its union N=⋃_(i∈S)Mi would be a proper nontrivial module of P. If Q[S] is nonchain then N is nonchain, excluded by minimality. If Q[S] is a chain then N is a chain module strictly containing each participating maximal block, also impossible. Therefore Q is prime.

Both graphs of Q are connected. Comparability disconnectedness would lift to P; an incomparability component separation would also lift to P because every block is internally a chain. Since both graphs are connected and P is nonchain, r≥4. For this canonical maximal-chain partition, Aut(P) is isomorphic to the weight-preserving subgroup of Aut(Q). Indeed, an automorphism of P permutes maximal chain modules, preserves their sizes, and induces a quotient automorphism; on each finite chain the image is uniquely determined by ranks. Conversely a weight-preserving quotient automorphism lifts rank-by-rank and preserves every order relation. Since P is rigid, the weighted quotient has no nonidentity weight-preserving automorphism. Q itself may have automorphisms that the weights break.

This is a necessary representation, not an assertion that every such inflation is a counterexample, or that the unweighted Q is a counterexample.

### 4.3 Width and maximum degree

An antichain takes at most one point from each chain block, and the participating blocks form an antichain in Q. Conversely any antichain of Q lifts by choosing one vertex in each block. Therefore

  width(P)=width(Q).

Every vertex in block i has incomparability degree

  di=Σ_(j∥_Q i) wj,

so π(P)=max_i di. In a search with π(P)≤D, impose the exact linear constraints Σ_(j∥i)wj≤D. Every quotient vertex i has an incomparable neighbor j, because its incomparability graph is connected. The constraint for j contains wi, so each wi≤D. These constraints do not bound r or |P|; no such global size bound has been proved here.

### 4.4 Exact uniform-word search

Each extension of the chain inflation corresponds to exactly one word with wi copies of symbol i, such that all copies of i precede all copies of j whenever i<j in Q. Reconstructing the first, second, … occurrence of i as the corresponding chain labels is inverse to the word map. Uniform valid words are precisely uniform full extensions of P; no extra multinomial weight is inserted.

A suffix-count DP uses vectors a=(a1,…,ar), 0≤ai≤wi. A symbol i is enabled iff ai<wi and aj=wj for every predecessor j<i in Q. Then

  Z(w)=1,
  Z(a)=Σ_(enabled i) Z(a+ei).

Starting at a=0 gives e(P)=Z(0). Choosing the next enabled symbol with probability Z(a+ei)/Z(a) samples the original uniform law exactly. Let A(a) count valid prefixes reaching a, with A(0)=1 and A(a+ei)+=A(a) for each enabled step. For actual labels (i,r) and (j,s), i≠j, the exact numerator is

  N[(i,r)<(j,s)]
    = Σ_{a: i enabled, ai=r−1, aj<s} A(a) Z(a+ei).

Every full word is counted exactly at its unique insertion of the rth i, and aj<s is precisely the event that the sth j has not yet occurred. Divide by Z(0) for the pair probability. Use integer tests Z(0)≤3N≤2Z(0) for the closed balanced interval, avoiding floating-point thresholds. The canonical order of Section 3 concerns individual occurrences, not necessarily contiguous quotient blocks.

## 5. What chain-module contraction actually does

Let M={m1<⋯<mk} be a chain module of P, k≥2, and Q=P/M its contraction to m. Put R=P\M. Let L be the outside vertices below M and U those above M. For an extension σ of R, define a as the position of the last L vertex (a=0 if L is empty) and b as the position of the first U vertex (b=|R|+1 if U is empty). Put dσ=b−a−1. All dσ vertices in this window are incomparable to M. There are dσ+1 available quotient gaps.

A chain of length k can interleave in the window in exactly

  Wk(dσ)=binom(dσ+k,k)

ways. Thus

  e(P)=Σ_(σ∈L(R)) Wk(dσ),
  e(Q)=Σ_(σ∈L(R)) (dσ+1).

For any outside pair x,y,

  p_P(x,y)=Σ_σ Wk(dσ) 1[x<σy] / Σ_σ Wk(dσ),
  p_Q(x,y)=Σ_σ (dσ+1) 1[x<σy] / Σ_σ (dσ+1).

This is the exact reweighting. For a general nonchain module of size k, the first extension-count formula acquires the factor e(M), which cancels in outside probabilities.

### 5.1 A precise law-preserving contraction criterion

Retain a fixed rank mj and delete the other k−1 module labels. For a quotient extension η obtained by putting m after t of the dσ window outsiders, the fiber size of this deletion map is

  Fj(η)=binom(t+j−1,j−1) binom(dσ−t+k−j,k−j).

The first factor interleaves m1,…,m_(j−1) with the t outsiders before m; the second does the analogous job afterward. All quotient extensions have positive fibers.

The pushforward of uniform L(P) by this fixed-representative contraction is uniform on L(Q) if and only if Fj(η) is constant over η∈L(Q). This is an exact necessary-and-sufficient condition for preserving the entire uniform law, and is a sufficient condition for preserving lack of balance: each pair of Q then corresponds to an actual fixed pair of P with the same probability. If Q is nonchain, such a contraction yields a strictly smaller counterexample and is excluded by minimum order.

More generally a particular quotient pair is preserved iff its Fj-weighted and unweighted means agree. Thus full-law preservation is sufficient, not necessary, for transferring absence of balanced pairs. Nonconstant fibers alone do not disprove every possible global chain-inflation closure theorem.

If dσ=0 always, Fj=1 always, recovering the familiar forced-block/ordinal case. Beyond law-preserving cases, one must either compute the quotient law or prove an additional balance-transfer theorem; minimality alone does not authorize contraction.

### 5.2 Random representatives are not enough

Choosing j uniformly from {1,…,k} independently of a uniform extension of P gives a quotient extension whose weight depends on σ through Wk(dσ)/(dσ+1), and is uniform among the dσ+1 gaps conditional on σ. This follows from

  Σ_(j=1)^k Fj(σ,t)=binom(dσ+k,k−1)=k Wk(dσ)/(dσ+1),

independent of t. For k≥2 the ratio Wk(d)/(d+1) is strictly increasing in d, so this random-representative pushforward is uniform on L(Q) exactly when dσ is constant over L(R).

Even then p_Q(m,y) is the average of the k probabilities p_P(mj,y), and an average may be balanced while every individual summand is unbalanced.

### 5.3 Two exact warnings

Example A. P consists of a<m1<m2 and an isolated b. M={m1,m2} is an autonomous chain. There are four extensions, giving p_P(a,b)=3/4. The contraction Q has a<m and isolated b; its three extensions give p_Q(a,b)=2/3. A balanced quotient pair entirely outside the module has changed to an unbalanced pair upstairs.

Example B. P=C2⊔C3 with M={m1<m2} and y the middle vertex of C3. There are ten extensions, and

  p_P(m1,y)=7/10,  p_P(m2,y)=3/10.

The contraction Q=C1⊔C3 has four extensions and p_Q(m,y)=1/2. Here dσ=3 is constant, so a random representative produces a uniform quotient, but neither individual lift of this particular pair is balanced.

Both P examples still have other balanced pairs. They refute these simple pairwise lifting arguments, not the entire conjecture or every conceivable global closure claim.

## 6. Duality

Reversing every extension gives a bijection L(P)→L(P*), with p_(P*)(x,y)=1−p_P(x,y). Thus balance, counterexample status, cardinality-minimality, both graph connectedness conditions, chain-module structure, width, and π are dual-invariant. A search may keep one representative modulo isomorphism and duality. It may not impose self-duality. Under duality the canonical strong-majority order reverses.

## 7. Literature boundary

The internal-module uniformity and chain-inflation factorization agree with Lemmas 1–2 of Dolores-Cuenca, Guzmán-Sáenz, and Kim, [The Gold Partition Conjecture and the Lexicographic Sum of Posets, arXiv:2410.12494v2](https://arxiv.org/html/2410.12494v2), dated 26 September 2026. Their balance corollary inherits from an internal substituted factor, not the outer quotient. Section 3 explicitly retains prime/indecomposable skeletons with positive-integer chain inflations; the older v1 final remark omitted that proviso. Use v2. Its discussion of outside-pair reweighting is consistent with Section 5 above. This note claims no novelty for the structural facts.

The source confirms why a prime skeleton with weights is the safe target. It does not establish a general unweighted-prime counterexample reduction. Width≤2 and bounded-thinness literature exclusions are deliberately not reproved here and should be attached separately with their exact verified hypotheses.

## 8. Finite identity checks

The standard-library script `minimal-counterexample-reductions/check_reductions.py` exhausts all naturally labelled posets on 1–5 vertices (407 total). Its exact rational/integer checks passed for 3,612 internal-module laws, 366 chain-module fiber laws, and 98 eligible weighted-prime decompositions/word DPs. It also verifies both numerical examples. `check_results.json` records the output. These are implementation/identity checks on a finite range, not a substitute for the proofs or an assertion about all counterexamples.

## 9. Safe combined target

If a counterexample exists, some minimum-order counterexample is a rigid poset P with both graphs connected, at least two minima and maxima, every proper nontrivial module a chain, and a unique canonical all-forward strong-majority extension. It admits an exact weighted-prime representation Q(C_w1,…,C_wr), r≥4, with both graphs connected, no nontrivial weight-preserving quotient symmetry, and exact uniform-word law. Any additional established restrictions on width or π can be imposed through width(Q) and the linear inequalities above.

The two main remaining gaps are global size control and a mechanism forcing an actual balanced pair in every surviving weighted-prime candidate. Neither is supplied by these reductions.

## 10. Source-backed forced-orientation filter and weight-independent exclusions

This addendum uses one literature theorem rather than only the elementary arguments above. In [Zaguia, The 1/3–2/3 Conjecture for ordered sets whose cover graph is a forest](https://arxiv.org/html/1610.00809), Definition 1 and Theorem 2 state that a good pair guarantees a balanced pair somewhere in the poset. The relevant good-pair hypotheses are D(a)⊆D(b), U(b)\U(a) a chain, and p_P(a,b)≤1/2; the dual case is included. Definition 5 calls equal downsets with both upper differences chains a very good pair, again allowing duality. Empty chains are permitted.

### 10.1 Forced graph on actual vertices

For incomparable a,b satisfying the two structural good-pair conditions, a counterexample must have p_P(a,b)>2/3: p≤1/2 invokes the theorem, and 1/2<p≤2/3 is itself balanced. Applying the same argument in the dual gives the second rule below.

Define F(P) on the actual vertices by these directed edges x→y:

1. x<y in P;
2. x∥y, D(x)⊆D(y), and U(y)\U(x) is a chain;
3. x∥y, U(y)⊆U(x), and D(x)\D(y) is a chain.

If P is a counterexample, every edge of F(P) points forward in its canonical strong-majority order. Therefore F(P) must be acyclic. A cycle is an exact structural rejection certificate requiring no extension counts. If F(P) is acyclic, only its topological orders can be canonical strong-majority reference extensions. Acyclicity is necessary, not sufficient.

### 10.2 Lifting to endpoint ports of chain blocks

For a chain inflation P=Q(C_wi), write Bi for the bottom of block i and Ti for its top; identify them if and only if wi=1.

Suppose a∥b in Q with D_Q(a)⊆D_Q(b) and U_Q(b)\U_Q(a) a chain. Then

  D_P(Ba)=⋃_(i<_Q a) Ci ⊆ ⋃_(i<_Q b) Ci=D_P(Bb),

and

  U_P(Bb)\U_P(Ba)
    = (Cb\{Bb}) ⊕ Q[U_Q(b)\U_Q(a)](corresponding chains),

which is a chain. Therefore the quotient lower rule forces the actual edge Ba→Bb for every positive weight vector. The dual quotient rule similarly forces Ta→Tb.

Safe endpoint constraints therefore include:

- Ba→Bb for each lower-rule quotient edge a→b;
- Ta→Tb for each upper-rule quotient edge a→b;
- Ti→Bj whenever i<j in Q;
- Bi→Ti when wi>1.

Any directed cycle in this actual endpoint graph excludes that weight vector. There is also a stronger weight-independent test: retain two distinct formal ports Bi,Ti for every quotient vertex and include a formal edge Bi→Ti for every i, without knowing wi. Interpret this internal edge as a weak inequality between canonical ranks, since Bi=Ti is possible when wi=1. Every interblock edge is strict. Any directed cycle of the formal graph must contain an interblock edge, because internal edges alone only run from B to T and cannot cycle. It would therefore give a weakly increasing closed walk with at least one strict step, impossible. Hence a directed cycle in the full formal two-port graph rejects every positive weight vector. Separate all-bottom/all-top cycle tests are valid but potentially weaker.

For a fixed weight vector, identifying singleton ports can supply additional cycles. Do not identify Bi and Ti for an unspecified or larger weight merely because they belong to the same quotient vertex: such arbitrary merging can invent an invalid cycle. Keeping the two formal ports and treating the internal edge as weak avoids this problem.

### 10.3 No very-good pair in the prime quotient

If Q has distinct a,b with equal downsets and with U_Q(a)\U_Q(b) and U_Q(b)\U_Q(a) both chains, both lower directions lift, producing Ba→Bb→Ba. Dually, the equal-upsets version produces a top-port two-cycle. Thus a prime skeleton containing a very-good pair cannot underlie a counterexample for any positive weights. This strengthens twin-freeness and does not rely on any uniform contraction law. The theorem guarantees a balanced pair somewhere in P; it need not be the displayed bottom or top pair.

These filters strengthen the combined target in Section 9: require no very-good pair in Q, and acyclicity of the valid actual/endpoint forced graph. They do not establish a global size bound or prove that all surviving candidates have a balanced pair.
