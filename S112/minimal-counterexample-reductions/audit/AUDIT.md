# Independent audit of minimal-counterexample reductions

Date: 2026-10-10. Audited artifact: `minimal_counterexample_reductions_20261010.md`. Verdict: the module, weighted-prime, counting, rigidity and structural-good-pair claims are valid with the qualifications below. This is an independent proof audit and exact finite identity check, not a proof of the 1/3–2/3 conjecture.

## 1. Quantifiers and edge cases

- Minimality must mean minimum cardinality among counterexamples, or the weaker sufficient hypothesis that every proper induced nonchain subposet has a balanced pair in its own uniform law. Merely checking single-vertex deletions does not imply that premise.
- Every proper nonchain autonomous module is excluded. The whole poset remains an autonomous module and is not excluded by this statement. Singleton modules are chains.
- Define prime as having no proper module of cardinality between 2 and |Q|−1. This convention alone permits small degenerate orders, but both graph-connectedness conditions and nonchain status exclude them here: the resulting quotient has at least four vertices.
- The weighted quotient need have no weight-preserving nonidentity automorphism. It need not be rigid as an unweighted poset.
- The canonical >2/3 order labels individual vertices. No result here makes chain blocks contiguous in that order.

## 2. Checked proof mechanisms

The autonomous-module internal law is genuinely uniform: fixing outside order and module slots permits arbitrary replacement by any internal linear extension. This gives identical fibers for all internal extensions and does not assert a uniform outside or quotient law.

Intersecting chain modules have a module union and all cross-exclusive elements compare, so their union is again a chain module. Maximal chain modules therefore partition the vertex set. A proper nontrivial quotient module lifts to a proper module; if it is nonchain it violates minimality, while if it is a chain it contradicts maximality of the chain blocks. Thus the quotient is prime.

Connectedness is valid but requires a real argument in the disjoint-union-of-chains case. The note's binary-shuffle proof supplies it. For independent confirmation, if a≤b and x is the first element of C_a, then

  f_j = Pr[x < (jth element of C_b)]
      = 1 − binom(a+b−j,a)/binom(a+b,a).

The increments decrease, f_1≤1/2, and f_b≥1/2. At the first crossing of 1/3, either the first term is already in [1/3,1/2], or the increment is less than 1/3 and the resulting term is below 2/3. A balanced pair of the union of two components lifts by autonomous-module uniformity.

The strong-probability orientation is transitive because two probabilities >2/3 give a third >1/3 by the union bound, and the forbidden closed interval forces that third above 2/3. Its strict total order extends P, is canonical, and is preserved by all automorphisms. Hence every hypothetical counterexample is rigid.

Width, incomparability degree, valid-word uniformity, and the suffix DP are exact. The state transition appends one uniquely determined next chain element, so there is no multiplicity factor. The rank-pair numerator sums prefix-count times suffix-count exactly at insertion of the chosen rank; it counts each satisfying complete extension once. Under π(P)≤D, connectedness gives an incomparable neighbor for every block and hence w_i≤D. This does not bound the number of blocks.

The deterministic and random representative contraction formulas check out. Nonconstant fibers invalidate preservation of the full uniform law, but do not prove that every conceivable global chain-inflation closure theorem is false. The two supplied numerical examples only refute their specified pairwise transfer claims.

## 3. Source-backed filter and endpoint strengthening

Primary source: [Zaguia, arXiv:1610.00809v3](https://arxiv.org/html/1610.00809), Definition 1 and Theorem 2, with the structural special case in Definition 5. A good pair yields some balanced pair. It need not itself be balanced.

For distinct incomparable a,b, define a lower structural-good arrow a→b by

  D(a)⊆D(b), and U(b)\U(a) is a chain.

In a counterexample this forces Pr[a<b]>2/3. The dual gives the actual-orientation upper rule

  U(b)⊆U(a), and D(a)\D(b) is a chain.

The lower quotient rule lifts to bottom endpoints, and the upper quotient rule lifts to top endpoints. A very-good pair gives a two-cycle at the appropriate endpoints and excludes every positive weight vector. Empty chains in the differences are allowed.

### Exact compression, not just sufficient endpoint constraints

For incomparable chain blocks A,B, let x be any element of A and y any element of B.

- The lower structural-good condition on (x,y) holds exactly when x is bottom(A) and the quotient lower condition holds on (A,B). Indeed, an earlier A element could not belong to D(y), and after x is bottom the difference of upsets is the tail of B followed by the inflated quotient upset-difference chain. The rank of y is arbitrary.
- Dually, the upper condition holds exactly when y is top(B) and the quotient upper condition holds. The rank of x is arbitrary.

Thus all actual lower arrows follow from bottom(A)→bottom(B) followed by movement up B. All actual upper arrows follow from movement up A followed by top(A)→top(B). Order-comparability edges similarly follow from internal-chain edges and top(A)→bottom(B) for A<B.

Consequently the full actual forced graph is cyclic if and only if the endpoint graph is cyclic after identifying bottom(i)=top(i) precisely when w_i=1 and omitting identity edges. Intermediate ranks cannot create any additional cycle. This filter's dependence on the weights is only through singleton status.

### Generic two-port cycles reject all weights

Keep two formal ports L_i,U_i for every quotient vertex, even before weights are chosen. Add lower-rule edges L→L, actual upper-rule edges U→U, quotient comparabilities between corresponding ports (top→bottom suffices), and L_i→U_i.

For a hypothetical counterexample, interpret each interblock edge as a strict increase in the canonical probability rank and each internal L_i→U_i edge as a nondecrease; it is an equality only at weight one. Every directed cycle contains an interblock edge, because internal edges alone only move L→U. A weakly increasing closed walk with at least one strict increase is impossible. Therefore a generic two-port cycle excludes all positive weights. Singleton contractions erase only identity steps and cannot erase every interblock strict step. Collapsing all ports without conditioning on singleton weights remains unsound.

## 4. Optional sharp fixed-representative criterion

For module length k≥2 and retained rank j, the fiber

  F_j(d,t)=binom(t+j−1,j−1) binom(d−t+k−j,k−j)

is constant over all quotient extensions if and only if either:

1. Every outside window has d=0; or
2. Every outside window has d=1, k is odd, and j=(k+1)/2.

For d≥1, consecutive equality is equivalent to

  (j−1)d − (k−1)t − (k−j)=0.

If d≥2 it cannot hold at both t=0 and t=1 because k−1>0. If d=1 it forces 2j=k+1. The d=0 fiber equals 1, while the balanced-rank d=1 fiber is j≥2, so those window sizes cannot be mixed. This sharpens the note's constant-fiber criterion but is not needed for the main reduction.

## 5. Independent finite evidence

`independent_audit.py` enumerates transitive subsets of the natural order directly, using a topological extension generator rather than the other worker's closure-and-permutation implementation. It exhausts every naturally labelled poset of orders 1–6, covering every isomorphism type in that range.

Recorded in `audit_results.json`:

- 5,231 posets
- 52,214 uniform module fibers
- 57,501 intersecting chain-module unions
- 5,231 chain-word, DP and geometry cases
- 5,225 exact rank-pair numerator cases
- 1,320 prime quotients under the no-proper-nonchain-module hypothesis
- 5,050 two-chain crossing cases, chain lengths at most 100

`very_good_inflation.py` checks every natural-label base of size 2–5 with each weight in {1,2}. Recorded in `very_good_results.json`: 12,068 inflations of bases with a very-good pair and 52,008 lifted witness pairs, all PASS.

`endpoint_compression.py` checks exact actual-pair characterization, not just cycle status, for all natural-label bases of size 1–5 and all weights in {1,2}. Recorded in `endpoint_results.json`: 12,130 inflation cycle-equivalences and 592,018 actual ordered-pair characterizations, all PASS.

These tests support the audited identities; the general validity comes from the proofs above. No counterexample existence, global size bound, or uniform unweighted quotient-counterexample reduction is asserted.
