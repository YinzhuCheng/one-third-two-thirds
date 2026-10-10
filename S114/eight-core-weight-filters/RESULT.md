# Exact linear filters for the 17 surviving eight-vertex prime cores

Date: 2026-10-10. Scope: frozen classes C02–C18 only, with the same vertex labels as `input_cores.json`. No larger core enumeration and no remote writes were performed.

## Results

1. A general insertion-window inequality, with a proof using the correct reweighted outside law, yields 57 distinct necessary linear inequalities. It strictly strengthens the suggested upset-inclusion template: chain differences suffice.
2. Combining these inequalities with the independently rechecked singleton-port constraints produces additional nonsingleton requirements in C06, C10, and C13. All 17 global linear regions remain feasible; the exact witness is w=(2,2,2,2,2,2,2,2).
3. An exact bounded-family argument proves more: in every one of the 17 classes, a counterexample must have a nonsingleton block outside the originally port-forced set. Only 22 weight vectors remain after certified bounds in these initially unbounded families, and each has an explicitly counted balanced pair. The largest checked inflation in this argument has order 15.
4. A separate implementation check covers all 4,352 inflations with weights in {1,2}^8. This finite box is validation only and is not the proof of any infinite-family claim.

These are necessary restrictions, not a classification of counterexamples. No whole eight-core class is excluded for every positive weight vector.

## 1. Notation and external theorem

For an eight-point core Q, let D(i), U(i), and I(i) be its strict downset, strict upset, and set of incomparable vertices. Replace vertex i by a nonempty chain C_i of positive integer length w_i. Its endpoints are B_i and T_i. Every probability below is with respect to the uniform law on complete linear extensions of the actual inflated poset P.

We use Zaguia's good-pair theorem, Definition 1 and Theorem 2 of [The 1/3–2/3 Conjecture for ordered sets whose cover graph is a forest](https://arxiv.org/html/1610.00809). A structural lower pair (a,b) has D(a)⊆D(b) and U(b)\U(a) a chain. In a poset with no balanced pair, it must satisfy Pr(a<b)>2/3: the theorem excludes probability ≤1/2, and balance excludes the remaining interval through 2/3. The dual implication is used for upper pairs. This is exactly the use established in the supplied structural reductions.

For core vertices j∥i with D(j)⊆D(i) and U(i)\U(j) a chain, the actual endpoints (B_j,B_i) meet those structural hypotheses for every positive weight vector. Indeed, the upset difference consists of the tail of C_i followed by the chain inflation of U(i)\U(j), and is a chain. The dual lift applies to tops. A good pair need not itself be the balanced pair supplied by the theorem.

## 2. General insertion-window lemma

Remove the whole chain C_i, and fix an extension σ of the outside poset. Let the insertion window be the segment strictly between the last outside predecessor of C_i and its first outside successor. Empty predecessor/successor sets give the beginning/end boundary. Write h for the number of outside elements in this window.

Every such element is incomparable with C_i, so h≤M_i:=Σ_{k∈I(i)}w_k. There are exactly binom(h+w_i,w_i) ways to insert C_i, and, conditional on this particular σ under the uniform full-extension law, these insertions are equiprobable. The probability that C_i supplies the first window element is w_i/(w_i+h), including h=0. The same is true for the last window element.

The outside extension itself is NOT uniform: its induced weight is proportional to binom(h+w_i,w_i). The following argument conditions first and then averages under precisely this induced law.

If i∥j and D(i)⊆D(j), then B_j lies after the window's left boundary in every σ. It may be within the window or after it. Therefore the event that C_i supplies the first window element implies B_i<B_j, giving

Pr(B_i<B_j) ≥ E[w_i/(w_i+h)] ≥ w_i/(w_i+M_i).   (W-B)

Dually, if i∥j and U(i)⊆U(j), then T_j lies before the right boundary. The event that C_i supplies the last window element implies T_j<T_i, giving

Pr(T_j<T_i) ≥ w_i/(w_i+M_i).                 (W-T)

These probability bounds require neither primeness nor a counterexample hypothesis.

### Necessary linear rule

If i≠j satisfy

D(i)=D(j), and U(i)\U(j) is a chain,            (L)

then j→i is a structural lower arrow. In a counterexample Pr(B_i<B_j)<1/3; combining with (W-B) yields

2 w_i < Σ_{k∈I(i)} w_k.                       (L_i)

Equal downsets imply incomparability. Thus no separate incomparability assumption is missing. The suggested special case U(i)⊆U(j) is included, but is unnecessarily restrictive: the full difference may be any chain.

Dually, the same inequality follows whenever

U(i)=U(j), and D(i)\D(j) is a chain.            (T)

Here the counterexample's forced top orientation is T_i→T_j, and (W-T) bounds its opposite orientation. Because weights are integers, L_i is equivalent to 2w_i−Σ_{k∈I(i)}w_k≤−1. The strict threshold matters; equality is rejected.

## 3. Complete inequality catalogue

Every line below is a necessary condition for a counterexample. Duplicates arising from different witnesses or from both lower and upper proofs are listed once. The JSON and CSV give every witness and exact coefficient row.

### C02

Core covers: 0<2, 1<2, 1<3, 1<7, 2<6, 3<5, 4<5, 4<7, 5<6.

- 2w0 < w1 + w3 + w4 + w5 + w7. Lower witness j: 1,4; upper witness j: none.
- 2w2 < w3 + w4 + w5 + w7. Lower witness j: none; upper witness j: 5.
- 2w4 < w0 + w1 + w2 + w3. Lower witness j: 1; upper witness j: none.
- 2w7 < w0 + w2 + w3 + w5 + w6. Lower witness j: none; upper witness j: 6.

### C03

Core covers: 0<3, 1<2, 1<5, 2<3, 2<4, 3<6, 4<6, 4<7, 5<6.

- 2w0 < w1 + w2 + w4 + w5 + w7. Lower witness j: 1; upper witness j: none.
- 2w5 < w0 + w2 + w3 + w4 + w7. Lower witness j: 2; upper witness j: 3.
- 2w7 < w0 + w3 + w5 + w6. Lower witness j: none; upper witness j: 6.

### C04

Core covers: 0<3, 0<6, 1<2, 1<5, 2<3, 2<4, 4<6, 5<6, 5<7.

- 2w0 < w1 + w2 + w4 + w5 + w7. Lower witness j: 1; upper witness j: none.
- 2w3 < w4 + w5 + w6 + w7. Lower witness j: none; upper witness j: 6.
- 2w5 < w0 + w2 + w3 + w4. Lower witness j: 2; upper witness j: none.
- 2w7 < w0 + w2 + w3 + w4 + w6. Lower witness j: none; upper witness j: 3,6.

### C05

Core covers: 0<2, 1<2, 1<3, 1<5, 2<4, 3<4, 3<7, 4<6, 5<6.

- 2w0 < w1 + w3 + w5 + w7. Lower witness j: 1; upper witness j: none.
- 2w5 < w0 + w2 + w3 + w4 + w7. Lower witness j: 3; upper witness j: 4.
- 2w7 < w0 + w2 + w4 + w5 + w6. Lower witness j: none; upper witness j: 6.

### C06

Core covers: 0<3, 0<5, 1<2, 1<6, 2<3, 2<4, 3<7, 4<5, 6<7.

- 2w0 < w1 + w2 + w4 + w6. Lower witness j: 1; upper witness j: none.
- 2w5 < w3 + w6 + w7. Lower witness j: none; upper witness j: 7.
- 2w6 < w0 + w2 + w3 + w4 + w5. Lower witness j: 2; upper witness j: 3.

### C07

Core covers: 0<3, 0<5, 1<2, 1<6, 2<3, 2<4, 4<5, 5<7, 6<7.

- 2w0 < w1 + w2 + w4 + w6. Lower witness j: 1; upper witness j: none.
- 2w3 < w4 + w5 + w6 + w7. Lower witness j: none; upper witness j: 7.
- 2w6 < w0 + w2 + w3 + w4 + w5. Lower witness j: 2; upper witness j: 5.

### C08

Core covers: 0<3, 0<5, 1<2, 1<4, 2<3, 3<7, 4<5, 4<6, 6<7.

- 2w0 < w1 + w2 + w4 + w6. Lower witness j: 1; upper witness j: none.
- 2w2 < w0 + w4 + w5 + w6. Lower witness j: 4; upper witness j: none.
- 2w5 < w2 + w3 + w6 + w7. Lower witness j: none; upper witness j: 7.
- 2w6 < w0 + w2 + w3 + w5. Lower witness j: none; upper witness j: 3.

### C09

Core covers: 0<1, 0<5, 1<4, 2<3, 2<6, 3<4, 3<5, 5<7, 6<7.

- 2w0 < w2 + w3 + w6. Lower witness j: 2; upper witness j: none.
- 2w4 < w5 + w6 + w7. Lower witness j: none; upper witness j: 7.
- 2w6 < w0 + w1 + w3 + w4 + w5. Lower witness j: 3; upper witness j: 5.

### C10

Core covers: 0<1, 0<5, 1<4, 2<3, 2<6, 3<4, 3<5, 4<7, 6<7.

- 2w0 < w2 + w3 + w6. Lower witness j: 2; upper witness j: none.
- 2w5 < w1 + w4 + w6 + w7. Lower witness j: none; upper witness j: 7.
- 2w6 < w0 + w1 + w3 + w4 + w5. Lower witness j: 3; upper witness j: 4.

### C11

Core covers: 0<2, 0<6, 1<2, 1<3, 1<5, 3<6, 3<7, 4<5, 4<7, 5<6.

- 2w0 < w1 + w3 + w4 + w5 + w7. Lower witness j: 1,4; upper witness j: none.
- 2w2 < w3 + w4 + w5 + w6 + w7. Lower witness j: none; upper witness j: 6,7.
- 2w4 < w0 + w1 + w2 + w3. Lower witness j: 1; upper witness j: none.
- 2w7 < w0 + w2 + w5 + w6. Lower witness j: none; upper witness j: 6.

### C12

Core covers: 0<3, 0<5, 1<2, 1<6, 2<3, 2<4, 3<7, 4<5, 4<7, 6<7.

- 2w0 < w1 + w2 + w4 + w6. Lower witness j: 1; upper witness j: none.
- 2w5 < w3 + w6 + w7. Lower witness j: none; upper witness j: 7.
- 2w6 < w0 + w2 + w3 + w4 + w5. Lower witness j: 2; upper witness j: 3.

### C13

Core covers: 0<3, 0<5, 1<2, 1<4, 2<3, 2<5, 2<6, 4<5, 5<7, 6<7.

- 2w0 < w1 + w2 + w4 + w6. Lower witness j: 1; upper witness j: none.
- 2w3 < w4 + w5 + w6 + w7. Lower witness j: none; upper witness j: 7.
- 2w4 < w0 + w2 + w3 + w6. Lower witness j: 2; upper witness j: none.
- 2w6 < w0 + w3 + w4 + w5. Lower witness j: none; upper witness j: 5.

### C14

Core covers: 0<1, 0<5, 1<4, 1<7, 2<3, 2<6, 3<4, 3<5, 5<7, 6<7.

- 2w0 < w2 + w3 + w6. Lower witness j: 2; upper witness j: none.
- 2w4 < w5 + w6 + w7. Lower witness j: none; upper witness j: 7.
- 2w6 < w0 + w1 + w3 + w4 + w5. Lower witness j: 3; upper witness j: 5.

### C15

Core covers: 0<2, 0<5, 1<2, 1<3, 1<6, 2<4, 3<4, 3<5, 5<7, 6<7.

- 2w0 < w1 + w3 + w6. Lower witness j: 1; upper witness j: none.
- 2w4 < w5 + w6 + w7. Lower witness j: none; upper witness j: 7.
- 2w6 < w0 + w2 + w3 + w4 + w5. Lower witness j: 3; upper witness j: 5.

### C16

Core covers: 0<2, 0<5, 1<2, 1<3, 1<6, 2<4, 3<4, 3<5, 4<7, 6<7.

- 2w0 < w1 + w3 + w6. Lower witness j: 1; upper witness j: none.
- 2w5 < w2 + w4 + w6 + w7. Lower witness j: none; upper witness j: 7.
- 2w6 < w0 + w2 + w3 + w4 + w5. Lower witness j: 3; upper witness j: 4.

### C17

Core covers: 0<2, 0<5, 1<2, 1<3, 1<6, 2<4, 2<7, 3<4, 3<5, 5<7, 6<7.

- 2w0 < w1 + w3 + w6. Lower witness j: 1; upper witness j: none.
- 2w4 < w5 + w6 + w7. Lower witness j: none; upper witness j: 7.
- 2w6 < w0 + w2 + w3 + w4 + w5. Lower witness j: 3; upper witness j: 5.

### C18

Core covers: 0<5, 1<3, 1<6, 2<3, 2<4, 2<7, 3<5, 4<5, 4<6.

- 2w0 < w1 + w2 + w3 + w4 + w6 + w7. Lower witness j: 1,2; upper witness j: 3.
- 2w1 < w0 + w2 + w4 + w7. Lower witness j: 2; upper witness j: none.
- 2w6 < w0 + w3 + w5 + w7. Lower witness j: none; upper witness j: 5.
- 2w7 < w0 + w1 + w3 + w4 + w5 + w6. Lower witness j: 4; upper witness j: 5,6.

## 4. Singleton-port constraints and complete linear-section certificates

The old port filter forces w_i≥2 for every i in the set F below. This was independently recomputed from set-defined good pairs and all 256 singleton-port identifications per core, including verification of each stored directed cycle.

The additional linear clauses are:

- C06: F={0}, and at least one of {1,2,4,6} is nonsingleton.
- C10: F={5}, and at least one of {1,4,6,7} is nonsingleton.
- C13: F={0,3}; each of {1,2,4,6} and {4,5,6,7} must contain a nonsingleton.

For example, in C06, setting all four listed weights to 1 gives 2w0<4, contradicting w0≥2. The other three clauses have the same one-row exact certificate. In C13 an additional block in {4,6} can meet both clauses; otherwise separate additional blocks from the two disjoint remaining parts are needed.

There are no other minimal forbidden singleton sets from these 57 inequalities together with the old mandatory nonsingletons. This completeness statement is certified over all 2,336 possible singleton subsets disjoint from F. Each section sets those weights equal to 1, imposes w_i≥2 for i∈F and w_i≥1 elsewhere, and uses the integer-sharpened linear rows. For 2,313 sections an exact integer weight witness satisfies every row. For the remaining 23 an integer nonnegative Farkas combination gives a negative constant upper bound on a nonnegative expression. The 23 certificates reduce to the four minimal clauses above. A verifier checks only integer arithmetic; the optimizer used to discover certificates is not part of their validity.

All 17 full weight regions are nonempty: w_i=2 for every i satisfies the port constraints and every strict linear inequality. Every target has at least three incomparable core vertices, so the right side is at least 6 while the left side is 4. Feasibility says nothing about realizing the required endpoint probabilities and is not evidence of a counterexample.

## 5. Excluding the families with no additional nonsingleton block

Fix a class and its old mandatory set F. Suppose every vertex outside F has weight 1. A counterexample must have w_i≥2 for i∈F. Each i∈F is a target of one of the above inequalities, so on the variable vector x=(w_i:i∈F), these rows become

A x ≤ b,

where A_ii=2, A_ij=−1 if distinct i,j∈F are incomparable, and A_ij=0 otherwise. The right side is b_i=|I(i)\F|−1. The −1 is the exact integer strictness correction.

For every nonempty F here, the displayed finite matrix is invertible and A^−1 is entrywise nonnegative. Consequently x≤A^−1b componentwise. `minimal_support_family_certificates.json` contains each exact matrix, its rational inverse, the identity A^−1 A=I, and the resulting integer upper bounds. Thus the originally unbounded family has a rigorous finite exhaustive range. For F empty there is only the all-singleton vector.

Within these exact upper bounds, require w_i≥2 and all 57 applicable linear conditions. Across all 17 classes only 22 vectors survive. For each, the same file records an actual incomparable pair, e(P), and its exact favorable-extension numerator. Every recorded numerator lies in the closed balance interval. A second independent recurrence verifies each numerator by adding the tested precedence edge and counting linear extensions again.

| Class | Old forced F | Upper bounds on weights in F | Feasible vectors in this family | Necessary nonsingleton blocks after exclusion | Necessary total order |
|---|---|---|---:|---:|---:|
| C02 | 7 | 2 | 1 | 2 | 10 |
| C03 | 0,5 | 3,3 | 2 | 3 | 11 |
| C04 | 0 | 2 | 1 | 2 | 10 |
| C05 | 5,7 | 3,3 | 2 | 3 | 11 |
| C06 | 0 | 1 | 0 | 2 | 10 |
| C07 | 0,3,6 | 3,3,4 | 3 | 4 | 12 |
| C08 | empty | none | 1 | 1 | 9 |
| C09 | empty | none | 1 | 1 | 9 |
| C10 | 5 | 1 | 0 | 2 | 10 |
| C11 | empty | none | 1 | 1 | 9 |
| C12 | 0,6 | 2,2 | 1 | 3 | 11 |
| C13 | 0,3 | 1,1 | 0 | 3 | 11 |
| C14 | empty | none | 1 | 1 | 9 |
| C15 | empty | none | 1 | 1 | 9 |
| C16 | 5,6 | 2,2 | 1 | 3 | 11 |
| C17 | 6 | 2 | 1 | 2 | 10 |
| C18 | 0,7 | 4,4 | 5 | 3 | 11 |

These final cardinality lower bounds are necessary, not asserted sharp for true counterexamples. The new precise singleton clause in each class is: at least one index outside F must have weight at least 2. For C06, C10 and C13 this broad clause is already implied by their narrower linear clauses. For the other classes it is an additional consequence of the bounded-family certificates.

Two illustrative certificates:

- C07 allows only variable triples (w0,w3,w6)=(2,2,2),(2,2,3),(3,3,4) in this family. For the last, P has 125,565 extensions and Pr(B0<B1)=48,995/125,565, a balanced pair. Thus C07 requires at least four nonsingleton blocks in any counterexample.
- C11 with all weights 1 has Pr(B0<B3)=212/318=2/3 exactly. The endpoint belongs to the closed balanced interval and is correctly rejected.

This proves exclusions for whole originally unbounded families. It does not extrapolate a finite box or assume that every point in a linear region realizes a counterexample's probabilities.

## 6. Independent finite validation

`validate_inflations.py` constructs the actual labelled inflated poset for all 17×256=4,352 vectors in {1,2}^8. A predecessor-mask ideal DP computes integer extension and pair counts. It imports no filter implementation and uses neither the quotient extension law nor a uniform outside law. It verifies:

- 58,880 general lower-window bounds and 58,880 general upper-window bounds;
- 19,456 lifted actual good-pair hypotheses;
- an actual balanced pair in all 4,352 finite examples;
- 258,032 visited ideal states in total.

The linear filter rejects 863 examples in that box; the old singleton-port filter rejects 2,016, with overlap. The JSON reports per-class cumulative survivors. These finite examples validate implementation only.

`verify.py` separately reconstructs the 57 inequalities from set relations, all 4,352 singleton-port patterns, and every linear-section certificate. `verify_families.py` checks the inverse-matrix identities, reconstructs the complete bounded candidate lists, and checks all 22 balanced-pair certificates with 44 independent predecessor-edge extension counts.

## 7. Reproduction and boundaries

The portable verification path needs only Python's standard library:

    python verify.py
    python validate_inflations.py
    python verify_families.py

To regenerate discovery output, `build_filters.py` additionally needs NumPy and SciPy. Its solver outputs are never accepted without an exact certificate; verification does not depend on either package. `check_minimal_support_families.py` regenerates the finite-family certificate with exact Fractions and the independent all-pair oracle.

Input classes and labels are copied from the frozen catalogue, with input-file SHA256 provenance in `PROVENANCE.json`. The frozen source and independent audit were read-only. No unweighted automorphism exclusion, new core enumeration, weight-preserving-law assumption, LP-to-probability inference, or all-weight class exclusion is used.
