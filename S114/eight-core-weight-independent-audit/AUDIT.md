# Independent audit of the eight-core weight filters

Date: 2026-10-10. Verdict: **PASS for the stated necessary inequalities, complete singleton-section classification, and 17 restricted infinite-family exclusions.** No entire unrestricted weight region is excluded.

## Executive result

The independently reconstructed rules contain 57 distinct inequalities, witnessed 38 times from below and 38 times from above. All 2,336 singleton sections are accounted for bijectively: 23 have exact nonnegative integer infeasibility certificates and 2,313 have integer feasible witnesses. All 17 unrestricted linear regions have the witness `(2,2,2,2,2,2,2,2)`.

For each original port-forced set F, the family in which all weights outside F equal 1 is completely excluded. Exact entrywise-nonnegative inverse matrices bound every variable coordinate; this is a genuine finite reduction of the initially unbounded family. Exactly 22 integer vectors remain over all classes, and each has a balanced pair. All pairs of these 22 inflated posets were independently recounted, including both orientations with separate precedence-edge recurrences.

The strongest resulting cardinality restriction is four nonsingleton blocks for C07. Six classes require at least three, five require at least two, and five require at least one. These are class-specific necessary bounds, not a uniform three-block theorem and not claims of sharpness.

## 1. Inputs, labels, and scope

The exact input is the 17 order-eight entries C02–C18 of the frozen `all_survivor_singleton_constraints.json`. C01 is the order-seven class and is not included. The labels were not reindexed into C01–C17. Every input representative, cover list, class ID, and original singleton certificate was compared with the frozen source.

The 17 relation tuples were also matched, as complete tuples rather than by array index, with the original independent orbit audit. They are exactly its 17 eight-point representatives, each once. This matters because that audit has a different class ordering. This audit does not rerun the original enumeration of all order-eight cores: it uses the previously independently verified finite catalogue and verifies exact membership and label preservation.

The scripts import no author's implementation and use only the Python standard library. The original source and author directories were read-only throughout. Copied certificate inputs, exact outputs, code, proof, and provenance are in this audit package.

## 2. Insertion-window proof, including the two important edge cases

Let P be a chain inflation of any finite core Q, with positive integer chain lengths w. Fix a block C_i of length a=w_i and remove it. Let σ be any linear extension of the outside poset.

Let L be the position of the last outside predecessor of C_i, or the start sentinel if none exists. Let R be the position of the first outside successor, or the end sentinel if none exists. Every predecessor of C_i lies below every successor, by transitivity through C_i, so L<R. Let h be the number of outside elements strictly between these boundaries. Each is incomparable with the entire block, whence h≤M_i, where M_i is the sum of weights of core vertices incomparable with i.

The legal insertions of C_i are exactly the shuffles of its a ordered elements with the h-element fixed outside word. There are `binom(a+h,a)` such shuffles. Conditional on this σ under the uniform full-extension law, they are equiprobable. The fraction with a chain element first in the window is a/(a+h); the same fraction has a chain element last. This remains valid for h=0.

Crucially, σ itself has probability proportional to `binom(a+h,a)`, and is generally not uniform over outside extensions. All following inequalities hold pointwise in σ, so averaging under this induced, correctly weighted law preserves them.

Suppose i and j are incomparable and D(i)⊆D(j). Every predecessor of C_i precedes B_j. Therefore B_j is after L. It has two possible locations:

1. Inside the insertion window. If C_i contributes the first window element, then B_i precedes B_j. Thus the conditional probability is at least a/(a+h).
2. After the window. Every inserted element of C_i precedes B_j, so the conditional probability is 1.

B_j cannot be the right-boundary vertex, since that vertex is in a successor block of i, whereas j is incomparable with i. The weaker “inside or at/after the right boundary” case split also gives the same correct bound. **No inclusion involving U(i), U(j) is needed.** Consequently

`Pr(B_i < B_j) ≥ E[a/(a+h)] ≥ a/(a+M_i)`.

If B_j is the r-th outside element of the window, a more precise conditional count is

`Pr(B_i < B_j | σ) = 1 − binom(a+h−r,a)/binom(a+h,a)`.

This formula is used in the supplemental direct-fiber audit. Order reversal gives the upper version: U(i)⊆U(j) implies `Pr(T_j<T_i) ≥ a/(a+M_i)`.

### From structural arrows to strict integer inequalities

The external ingredient is Zaguia's good-pair theorem: under its structural lower-pair hypotheses, probability at most one half implies some balanced pair in the poset. Hence, in a hypothetical counterexample, a structural lower pair has probability strictly greater than two thirds. Its dual gives the corresponding upper statement. The theorem does not assert that the structural pair itself must be balanced. [Zaguia, Definition 1 and Theorem 2](https://arxiv.org/html/1610.00809v3).

If D(i)=D(j) and U(i)\U(j) is a chain, the inflated endpoints form the structural lower pair (B_j,B_i): their downsets satisfy the required inclusion, and the upset difference is the remaining tail of C_i followed by the inflated chain U(i)\U(j). Equal strict downsets for distinct vertices imply incomparability.

Thus a counterexample requires `Pr(B_i<B_j)<1/3`. The insertion inequality forces

`2 w_i < Σ_{k incomparable with i} w_k`.

For integers this is exactly `2 w_i − Σ w_k ≤ −1`, with the same incomparable-index set. Replacing −1 with 0 would lose the strict endpoint exclusion. Equal upsets and chain D(i)\D(j) give the identical inequality by duality.

## 3. Independent finite checks and exact certificates

`audit.py` reconstructs all rules directly from strict relation sets, derives the original endpoint graph, and tests its transitive-closure cyclicity for all 256 singleton patterns of every core. It independently recovers the original forced sets.

For each singleton section it checks that the fixed singleton set is disjoint from F, all other variable lower bounds are correct, and the complete power-set coverage has neither missing nor duplicate sections. A feasible section supplies a positive integer vector satisfying every integer-sharpened row. An infeasible section supplies nonnegative integer row multipliers whose combined free coefficients are nonnegative but whose combined right side is negative. This is an exact contradiction over the nonnegative translated variables; no floating-point solver verdict is used.

The only minimal additional singleton clauses are:

- C06: at least one of `{1,2,4,6}` is nonsingleton, in addition to F=`{0}`.
- C10: at least one of `{1,4,6,7}` is nonsingleton, in addition to F=`{5}`.
- C13: each of `{1,2,4,6}` and `{4,5,6,7}` contains a nonsingleton, in addition to F=`{0,3}`.

The same new block 4 or 6 can satisfy both C13 clauses. The clauses do not by themselves require four nonsingleton blocks in C13.

### Exact extension oracle

The independent all-pair oracle represents a prefix by the tuple of numbers already taken from each chain. A block can supply its next element exactly when all predecessor blocks have been exhausted. A recursive counting semiring returns both the suffix extension count and all unordered-pair favorable counts. At each first-element branch, it adds the child's vector and the suffix count for each pair whose first member is the newly chosen element. Every extension has a unique such block-symbol word, establishing bijective coverage.

This differs from the author's labelled-vertex predecessor-mask, forward/backward ideal DP. For every restricted-family vector, a second scalar occupancy recurrence blocks the second member of a tested pair until the first member has been placed. Both directions are counted separately for every unordered pair, and their sum equals the total. This also tests comparable pairs, whose probabilities must be exactly 0 or 1.

| Independent audit check | Exact count |
|---|---:|
| Distinct linear inequalities | 57 |
| Bottom / top witnesses | 38 / 38 |
| Singleton-port patterns | 4,352 |
| Complete singleton sections | 2,336 |
| Exact infeasibility certificates | 23 |
| Integer feasible witnesses | 2,313 |
| Binary-weight inflations, all balanced | 4,352 |
| All unordered-pair counts in that binary box | 291,584 |
| Occupancy states in that binary box | 258,032 |
| Lower / upper insertion bounds checked | 58,880 / 58,880 |
| Actual lifted good-pair hypotheses | 19,456 |
| Restricted-family surviving vectors | 22 |
| All unordered pairs in those 22 vectors | 1,098 |
| Separate precedence-edge counts for those pairs | 2,196 |

The complete pair matrices are preserved in the text-only file `all_pair_counts.json`. The binary box and restricted-family records are distinguished by `scope`; a vector that belongs to both has one record under each scope.

### Direct outside-fiber check

`audit_windows.py` literally enumerates outside extensions for every core and each distinguished block, assigning that block length 1, 2, or 4 and all others length 1. Across 408 inflation instances, it checks 24,240 outside fibers and 690 complete mixture probabilities against the independent oracle. It observes 21,162 inside-window and 12,915 after-window comparisons.

It also preserves a concrete warning against a uniform outside law. In C02 with all weights 1, removing block 0 leaves 48 outside extensions with insertion multiplicities 2 through 6. For target 0 and witness 1, incorrectly averaging uniformly over those outside extensions gives `205/576`; the true full-extension probability is `63/194`. The exact reweighted mixture gives the latter. Thus the proof's conditioning qualification is substantive rather than cosmetic.

## 4. Certified finite reduction of the restricted infinite families

Fix the original forced set F, set all outside weights to 1, and let x contain the weights in F. Every member of F is a verified inequality target. Its row is

`2x_i − Σ_{j in F, j incomparable with i} x_j ≤ |I(i)\F|−1`.

Write these rows as Ax≤b. Every stored inverse H is verified exactly as rational numbers, including both HA=I and AH=I, and every entry of H is nonnegative. Componentwise order is therefore preserved on multiplication: x=HAx≤Hb. Flooring each rational coordinate gives a valid integer upper bound. Together with x_i≥2, this gives the complete finite box; if a bound is less than 2, the family is empty. For F empty there is no variable and exactly one all-singleton vector.

The audit reconstructs the full bounded Cartesian product, applies every relevant rule, and compares the ordered accepted-vector list exactly with the certificates. It also verifies the recorded Cartesian cardinality. This handles potential unboundedness, omitted corners, duplicated vectors, and strict-integer mistakes without a numerical LP.

| Class | Original F | Integer bounds on F | Surviving vectors | Necessary nonsingleton count |
|---|---|---|---:|---:|
| C02 | 7 | 2 | 1 | 2 |
| C03 | 0,5 | 3,3 | 2 | 3 |
| C04 | 0 | 2 | 1 | 2 |
| C05 | 5,7 | 3,3 | 2 | 3 |
| C06 | 0 | 1 | 0 | 2 |
| C07 | 0,3,6 | 3,3,4 | 3 | 4 |
| C08 | empty | none | 1 | 1 |
| C09 | empty | none | 1 | 1 |
| C10 | 5 | 1 | 0 | 2 |
| C11 | empty | none | 1 | 1 |
| C12 | 0,6 | 2,2 | 1 | 3 |
| C13 | 0,3 | 1,1 | 0 | 3 |
| C14 | empty | none | 1 | 1 |
| C15 | empty | none | 1 | 1 |
| C16 | 5,6 | 2,2 | 1 | 3 |
| C17 | 6 | 2 | 1 | 2 |
| C18 | 0,7 | 4,4 | 5 | 3 |

The 22 surviving orders have histogram `{8:5, 9:3, 10:5, 11:3, 12:4, 14:1, 15:1}`. Thus 21 lie at order at most 14 and exactly one has order 15.

For C07, A has rows `(2,0,−1)`, `(0,2,−1)`, `(−1,−1,2)` and b=`(2,2,2)`. Its inverse has rows `(3/4,1/4,1/2)`, `(1/4,3/4,1/2)`, `(1/2,1/2,1)`. The certified upper vector is `(3,3,4)`. The only accepted triples are `(2,2,2)`, `(2,2,3)`, and `(3,3,4)`.

The final triple yields the sole order-15 vector `(3,1,1,3,1,1,4,1)`. The independent count is 125,565 extensions; 48,995 put B0 before B1. Its balance check is the exact integer comparison `125565 ≤ 146985 ≤ 251130`.

The existing published preprint reports the conjecture through order 14. This audit does not claim that frontier as new, rely on it instead of recounting the 21 small vectors, or infer the order-15 case from it. The single order-15 certificate is directly verified here; it is not exhaustive verification of all order-15 posets. [Gupta, arXiv:2607.23926v2](https://arxiv.org/abs/2607.23926v2).

## 5. Corrections and limits

No defect was found in the author's final mathematical statement or stored certificates. The following scope safeguards are essential:

1. The nonsingleton conclusion is **|F|+1 for that class**. In particular, C08, C09, C11, C14, and C15 only get the bound one from this theorem.
2. C13 requires at least three, already implied by its sharper linear clauses; one extra block at 4 or 6 can satisfy both clauses.
3. The insertion lemma assumes only the relevant downset or upset inclusion. Requiring an extra opposite-side inclusion would incorrectly discard valid witnesses; presuming B_j always lies inside the window would leave a proof gap.
4. The unrestricted linear regions are feasible. Their all-2 witness must not be described as a counterexample, and the regions must not be called infeasible.
5. The finite `{1,2}^8` tests are validation only. Infinite-family coverage comes from the proved insertion inequality, exact nonnegative inverse bound, and exhaustive bounded reconstruction.
6. No conclusion is made about larger core sizes, arbitrary weight support, global finite representative bounds, or the full conjecture.

## 6. Reproduction

From this directory, run:

    python audit.py
    python audit_windows.py

Both need only Python 3 and the standard library. `audit.py` writes `audit_results.json` and deterministic `all_pair_counts.json`; `audit_windows.py` writes `window_results.json`. Only the top-level `elapsed_seconds` field of `audit_results.json` is nondeterministic. The corresponding timing printed in `audit.log` is also nondeterministic. No other substantive result field is ignored in comparison.

`verify_snapshot.py` checks the initial manifest, copies the full package to a fresh temporary directory, reruns both commands there, and compares exact outputs after removing only that one timing field. It checks the full text pair-count file byte for byte. The audit does not regenerate or alter the input certificate files.
