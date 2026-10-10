# Independent audit: exact weighted-prime core catalogue

Date: 2026-10-10. Verdict: **PASS, within the finite and theorem-conditional scope below.**

This audit independently verifies every naturally labelled poset of order at most eight, the resulting survivor sets, their complete isomorphism classification, and the claimed seven-vertex singleton-weight restrictions. It does not prove the 1/3–2/3 conjecture or a global bound on prime-core size or chain weights.

## 1. Verified counts

Here “natural” means every strict relation respects the fixed label order, not one representative per isomorphism class. “Prime” excludes every autonomous module of size 2 through n−1. Small degenerate prime counts use that definition literally; the counterexample reduction also requires both graphs connected.

| n | Natural posets | Prime | Prime, width ≥3 | Survive both-side VGP | Survive generic endpoint graph |
|---:|---:|---:|---:|---:|---:|
| 1 | 1 | 1 | 0 | 0 | 0 |
| 2 | 2 | 2 | 0 | 0 | 0 |
| 3 | 7 | 0 | 0 | 0 | 0 |
| 4 | 40 | 5 | 0 | 0 | 0 |
| 5 | 357 | 35 | 27 | 0 | 0 |
| 6 | 4,824 | 744 | 696 | 0 | 0 |
| 7 | 96,428 | 19,256 | 19,097 | 44 | 44 |
| 8 | 2,800,472 | 720,147 | 719,417 | 2,552 | 2,552 |

For n=6, 663 cores have a lower very-good pair and 663 have an upper very-good pair; their union is all 696 width-at-least-three prime cores. Thus the two separate counts are overlapping, not additive.

The complete surviving strict-relation sets match both the author's main Python output and its independent C++ output, not merely their aggregate counts. Our generator and predicates import no author code.

## 2. Independent algorithms and completeness

`audit_enumeration.cpp` constructs rows from highest label to lowest. Once the strict order on a suffix is fixed, it chooses each upward-closed subset as the new vertex's strict upset. Upward closure is exactly the remaining transitivity condition. Every naturally labelled strict partial order has a unique sequence of such rows, proving completeness and uniqueness of generation. The author's main generator instead appends a largest label with an ideal downset, and the author's other enumerator tests all relation masks directly.

Primality uses pair-generated module closure. Start with each pair. Whenever an outside vertex sees current members with different comparison types (below/above/incomparable), add it, then repeat. Every module containing the pair must contain every vertex so added. At termination the resulting set is itself a module, because every remaining outside vertex sees all its members uniformly. Therefore a proper nontrivial module exists exactly when some pair closure is proper. This avoids the author's exhaustive candidate-subset module predicate.

The width-at-least-three test searches directly for an incomparable triple. Endpoint acyclicity uses Kahn deletion. Our endpoint graph uses only top-to-bottom quotient comparison edges, with internal bottom-to-top links; the author's redundant all-port comparison edges have the same reachability.

`audit_orbits.py` generates **all linear extensions** of a surviving representative and records every naturally labelled order obtained by those relabellings. This is its complete isomorphism orbit among natural orders: every natural labelling of the same abstract poset comes from some extension. Distinct orbits are peeled from the full survivor set. For every class the script asserts that the entire orbit is present and that no already-removed orbit overlaps. Thus it verifies completeness rather than trusting a graph hash. If e is the extension count and m the number of distinct natural forms, e/m is the automorphism-group order. This method is independent of the author's degree-colour permutation canonicalization.

## 3. Seven-vertex result and exact witnesses

There is exactly **one** surviving seven-vertex isomorphism class. It has width 3, height 4, 44 linear extensions, and automorphism-group order 1. Its 44 natural forms comprise the complete survivor set. A representative has strict-up masks

`(40,124,104,32,32,0,0)`

and covers

`0<3; 1<2,4; 2<3,6; 3<5; 4<5`.

Let B_i and T_i denote the bottom and top of positive chain block i. The following quotient structural rules force arrows on actual endpoints in any hypothetical counterexample:

- B0→B2: D(0)=∅⊆{1}=D(2), and U(2)\U(0)={6} is a chain.
- T2→T0: U(0)={3,5}⊆{3,5,6}=U(2), and D(2)\D(0)={1} is a chain.
- T3→T6: U(6)=∅⊆{5}=U(3), and D(3)\D(6)={0} is a chain.
- B6→B3: D(6)={1,2}⊆{0,1,2}=D(3), and U(3)\U(6)={5} is a chain.

If w0=1, then T0=B0 and the cycle is

`B0 → B2 → T2 → T0=B0`.

If w6=1, then T6=B6 and the cycle is

`B3 → T3 → T6=B6 → B3`.

The internal steps are nondecreasing canonical ranks and the interblock steps are strictly increasing. The conclusion remains valid if block 2 or block 3 also has weight one; the corresponding internal step becomes an equality and can be omitted.

Hence **w0≥2 and w6≥2 are necessary** for a counterexample inflation of this core, giving at least nine actual vertices for this core. Every one of the 128 singleton patterns was checked: the graph is cyclic exactly when 0 or 6 is singleton. There are no additional singleton restrictions from this forced graph. Passing it is not sufficient for a counterexample.

## 4. Eight-vertex extension

The 2,552 survivors have exactly **17 isomorphism classes**. All are rigid. Sixteen have width 3 and one has width 4. Their natural multiplicities (in the audit's canonical order) are

`465,318,194,194,102,102,107,82,107,96,98,132,121,107,121,110,96`.

The width-4 class has height 3 and multiplicity 465. Among width-3 classes, one has height 3, fourteen have height 4, and one has height 5. Five classes have no forbidden singleton patterns under this filter. The remaining exact singleton restrictions are recorded per representative in `orbit_and_singleton_audit.json`.

Across all 18 surviving classes at orders 7 and 8, the audit compares contracted endpoint-graph cyclicity to a freshly built **actual-vertex** forced graph for every singleton pattern, taking each nonsingleton chain to have length 2: **4,480 checks, all PASS**. This finite check supports the endpoint identity; arbitrary positive chain lengths are covered by the mathematical endpoint-compression argument, not by extrapolation from length 2.

## 5. Theorem and quantifier audit

The primary source was checked directly: [Imed Zaguia, arXiv:1610.00809v3, Definition 1, Theorem 2, Definition 5](https://arxiv.org/html/1610.00809). The good-pair theorem guarantees a balanced pair somewhere in the whole poset; it does not say the displayed good pair itself is balanced.

For incomparable a,b with D(a)⊆D(b) and U(b)\U(a) a chain, a poset with no balanced pair must have p(a,b)>2/3. Otherwise either p≤1/2 triggers that theorem, or 1/2<p≤2/3 is already balanced. The dual rule has actual direction a→b when U(b)⊆U(a) and D(a)\D(b) is a chain. In a hypothetical counterexample these arrows and order comparisons must agree with its strict total strong-majority order.

For incomparable inflated blocks A,B, a lower structural arrow x→y is possible exactly when x is bottom(A) and the corresponding lower quotient predicate holds; y can be any rank of B. Any earlier A element would prevent D(x)⊆D(y). Once x is bottom, the upset difference consists of a terminal segment of B followed by the inflated quotient difference, so its chain condition is equivalent to the quotient chain condition. Dually an upper arrow has y=top(B), arbitrary x in A, and the upper quotient predicate. Thus all actual arrows factor through the endpoint graph, and each endpoint arrow is itself valid. Intermediate ranks create no extra cycle.

A quotient very-good pair produces opposite bottom arrows or opposite top arrows for **every positive integer weight vector**, so its exclusion is uniform in weights. In the generic formal two-port graph, an internal B_i→T_i step is weak when wi=1. Every cycle still contains a strict interblock step, since internal steps alone cannot cycle. Hence generic cycles also reject every positive weight vector. The audit does not identify B_i with T_i until that block is explicitly assigned singleton status.

The reductions therefore retain the positive chain weights. They do not treat the quotient's unweighted uniform-extension law as the inflated poset's law, and do not infer that the unweighted quotient is a counterexample.

## 6. Limits and wording safeguards

- This is exhaustive only through core order 8. It gives no bound on larger cores or on unrestricted chain weights.
- No numerical probability cutoff, bounded weight scan, or unweighted balance computation is used for the uniform exclusions.
- The width≥3 domain is explicit. To state a lower bound on all possible counterexample cores, attach the separately established width-two theorem with its hypotheses.
- The natural counts are not counts of all labelled orders and are not isomorphism counts. The latter are separately proved by complete orbit enumeration.
- The seven-vertex size lower bound of nine applies to that core. It does not by itself prove a global lower bound of nine, because some eight-vertex cores pass every singleton pattern.
- Generic bottom/top or full endpoint cycles add no exclusions beyond the very-good-pair filter through order 8. They remain valid potentially stronger tests at larger orders.
- Necessary endpoint acyclicity is not evidence that any survivor is a counterexample.

## 7. Reproduction

No third-party Python packages are required. A C++17 compiler and Python 3 suffice.

```sh
cd prime-core-catalogue-independent-audit
c++ -O3 -std=c++17 audit_enumeration.cpp -o /tmp/poset_core_independent_audit
/tmp/poset_core_independent_audit 8 > enumeration.json 2> enumeration.log
python audit_orbits.py > orbits.log
```

For the additional exact comparison to the author catalogue, use

```sh
python audit_orbits.py \
  --reference ../prime-core-catalogue/independent_catalogue_n8.json \
  --reference ../prime-core-catalogue/results/survivors.json > orbits.log
```

The independent output consists of `enumeration.json` and `orbit_and_singleton_audit.json`; the latter records every class and all minimal forbidden singleton subsets.
