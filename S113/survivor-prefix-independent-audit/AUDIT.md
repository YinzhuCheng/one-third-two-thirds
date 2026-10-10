# Independent audit: surviving-core guarded-prefix certificates

Date: 2026-10-10. **Verdict: PASS within the exact guarded-prefix and structural-separation scope below.** No remote changes were made. This is separate from the earlier three guarded templates, whose balanced-pair existence conclusions remain subsumed by very-good-pair reductions.

The independent implementation imports no author implementation, uses only the Python standard library, performs all arithmetic with integers or rational fractions, and retains all checks under optimized Python. Its 36 independently reconstructed profiles match the author's frozen outputs. All 76 selected-menu bad-cell LP optima and primal/dual certificates pass. The audit also constructs and individually verifies **8,384 explicit full-menu orientation dual certificates**. All selected optima are strictly negative; the largest is −2/219.

A stronger, non-vacuous separation from the specified structural filters is established by the author's 23-vertex witness and an infinite family. The universal-top completions alone do **not** provide that stronger separation.

## 1. Scope, source freeze, and independent methods

The inputs comprise the 18 classes in the independently audited n≤8 prime-core catalogue: one seven-vertex class and seventeen eight-vertex classes. Each class is tested in both its presented order and its dual. These are **36 labelled presentations**, not 36 nonisomorphic orders.

The exact catalogue representatives are frozen in `catalogue_snapshot/orbit_and_singleton_audit.json`. This audit verifies every class/direction correspondence but does not repeat the catalogue's exhaustive enumeration of all natural posets. Its independent enumeration audit is included as background in `catalogue_snapshot/AUDIT.md`.

The author files are snapshotted in `author_snapshot/`. The repaired earlier verifier's supplied hash was checked as

`4d35c66632ff9f1f89cecccf18e5aaf02f8a94a18c217f1823b5e9e01a721451`.

No code from that verifier, the author research scripts, or the catalogue generator is imported into this audit.

Independent methods include:

- Transitive closure from displayed Hasse edges; exact predecessor/upset, maxima, Hasse-reduction and complete cut-support checks.
- Exhaustive permutations of every core and every cut ideal, independently recomputing every F and A entry, not just selected rows.
- An independent rational simplex solver: vertex extrema for one-row cells, plus exact row-crossing intersections and an independently minimized dual for the two-row/two-state cases.
- Explicit extension of each selected-menu certificate to every full-menu L/H mask, followed by fresh checks of all dual dimensions, signs, normalizations and equalities.
- Fresh construction of the full actual-vertex structural forced graph in each poset, using both lower and upper predicates, together with Kahn acyclicity and validation of every supplied cycle.
- Actual extension enumeration for concrete completions, independently checking cut support, continuation counts, total extensions and pair probabilities.
- Exact module-closure and automorphism checks; an additional exhaustive test of all 512 subsets of the nine-vertex quotient; independent chain-tail finite controls at k=1,2,3,4,15,31.

The normal and optimized outputs match byte-for-byte. Thirteen corrupted-input controls are rejected, including missing or duplicated orientation cells, altered F/A counts, missing cut/pair states, incorrect dual signs/dimensions/equalities, positive bounds, infeasible primal data, a floating-point rational, and a wrong catalogue orientation. Explicit exceptions, rather than assertions, enforce every check.

## 2. The theorem actually certified

Let P be a **finite** poset, and let C be an **initial order ideal** whose induced order is one of the 36 presented cores. Write n=|C| and r=n−1. Require that no vertex of P outside C can occur among the first r positions of any linear extension.

This guard is equivalent to

`|D_P(z)| ≥ n−1 for every z outside C`.

Indeed, the earliest possible rank of z is |D_P(z)|+1: first extend its predecessor ideal, then put z next, then extend the resulting ideal to all of P.

The actual rank-r ideal states are exactly J_m=C minus {m}, for maximal m in C. The guard places every actual state inside C; deleting a maximal element gives every possible size-(n−1) ideal in C; initiality makes each J_m an ideal in P, so all listed states really occur.

Define F_m=e(C[J_m]), B_m=e(P minus J_m), and A_im as the number of extensions of J_m placing the selected incomparable pair x_i before y_i. The selected endpoints belong to every J_m. Each B_m is a positive integer, and independent concatenation at an ideal cut gives

`p_P(x_i<y_i) = (Σ_m A_im B_m)/(Σ_m F_m B_m) = Σ_m q_im μ_m`,

where q_im=A_im/F_m and μ_m=F_m B_m/(Σ_j F_j B_j)>0, with Σ_m μ_m=1.

The checked certificates cover the **whole closed simplex**, which is a sufficient relaxation of the actual positive continuation vectors. They do not assume that every simplex point or every positive continuation vector is realizable by a finite tail. No tail-size, tail-width, tail-height, degree or continuation-ratio bound is needed. The balanced interval includes both endpoints, 1/3 and 2/3.

Consequently every such finite guarded completion has a balanced selected pair. Thirty-four presented profiles have a fixed pair that works for all their guarded completions; the remaining two isomorphic profiles use a two-pair menu. This is a forbidden **guarded initial configuration** statement, not a forbidden arbitrary induced subposet theorem.

The same count-table argument applies whenever the actual labelled cut states and induced orders are directly verified to be exactly the displayed states. It also permits an arbitrary common finite lower ordinal block H: for initial H⊕C guarded at |H|+n−1, every F and A entry is multiplied by e(H), so all ratios and certificates remain unchanged. These variants do not eliminate the guard or authorize arbitrary chain inflation of the individual core vertices.

## 3. Exact strict bad-cell coverage

For a selected pair row q_i, define

- L: h_i=1/3−q_i;
- H: h_i=q_i−2/3.

A strict bad cell requires h_i·μ>0 for all i. Its common-slack LP maximizes unrestricted ε subject to μ≥0, Σμ=1 and ε≤h_i·μ for every selected row.

The audited dual convention is

`λ_i≥0, Σ_i λ_i=1, η_m≥0, Σ_i λ_i h_im + η_m = ν`.

This implies ε≤ν. The checked primal reaches ν, establishing the reported selected-menu optimum. All 76 selected-menu values are negative.

For every orientation of the **complete** fully observed pair menu, project to the selected rows and insert zeros for the unused λ coordinates. All 8,384 resulting full-menu certificates are saved explicitly in `results.json`. Each has a valid nonpositive upper bound. **These are full-menu infeasibility certificates, not assertions that their bounds are optimal for the larger full-menu LP.** Full-menu reoptimization is unnecessary for complete strict-bad-cell exclusion.

## 4. The adaptive profile and its exact certificate

Use class `n8c15-primal`, with predecessor masks

`(0,0,3,2,15,11,2,107)`

and covers

`0<2,5; 1<2,3,6; 2<4; 3<4,5; 5<7; 6<7`.

The two maxima are 4 and 7. Columns omit 4 and 7 respectively. The independently reconstructed complete table is:

| Pair | A, omit 4 | A, omit 7 |
|---|---:|---:|
| F | 48 | 73 |
| 0<1 | 15 | 25 |
| 0<3 | 34 | 55 |
| 0<6 | 38 | 62 |
| 2<3 | 9 | 22 |
| 2<5 | 23 | 56 |
| 2<6 | 15 | 40 |
| 3<6 | 31 | 51 |
| 5<6 | 14 | 24 |

No row is balanced in both columns. The selected rows (2,5) and (2,6) suffice, so the smallest full-simplex menu has exactly two pairs. The other adaptive presentation, `n8c13-dual`, is isomorphic. The unique isomorphism from the current labels to that presentation is

`(0,1,2,3,4,5,6,7) → (4,7,1,5,0,3,6,2)`.

The exact selected-cell optima, in LL,LH,HL,HH order, are

`−7/48, −1433/5502, −401/5502, −26/219`.

For both mixed cells the primal is μ=(552/917,365/917), λ=(825/1834,1009/1834), and η=(0,0). LL has μ=(1,0), λ=(1,0), η=(0,1009/3504). HH has μ=(0,1), λ=(0,1), η=(275/1168,0). Every equality was independently checked.

Two actual guarded completions show that neither selected pair works uniformly over **all** lawful completions:

- One new vertex above C minus {7}: B=(1,2), e(P)=194, p(2<5)=135/194>2/3. This completion has the top very-good pair (7,8), and is not a structural-funnel separation.
- A 15-chain above C minus {4}: B=(16,1), e(P)=841, p(2<6)=280/841<1/3. This completion passes the specified structural funnel, as detailed next.

The general omit-one-maximum chain construction can amplify any column without changing the guard. Thus a row outside the balanced interval at a simplex vertex also fails on some finite lawful completion. This observation concerns the unrestricted guarded-completion family; it does not establish two-pair necessity within every narrower structural subfamily.

## 5. Actual 23-vertex separation

Append z1<...<z15, labelled 8,...,22, with every zj above all core vertices except 4, and incomparable with 4. Its seven core predecessors guarantee the rank-seven guard.

The independent audit enumerates all 841 actual full-poset extensions, verifies exactly the two cut states and B=(16,1), and obtains

- p(2<5)=424/841, balanced;
- p(2<6)=280/841, unbalanced.

All **27** incomparable-pair probability entries in the final author witness were independently reconstructed; exactly eight unordered pairs are balanced. The full structural graph and every lower/upper rule edge also match exactly.

This witness has:

- connected comparability and incomparability graphs;
- every proper nontrivial autonomous module a chain;
- automorphism group of order one;
- width 3, height 19, and maximum incomparability degree π=18;
- two minima and two maxima;
- a cyclic cover graph;
- no very-good pair in either direction;
- an acyclic full actual-vertex forced graph.

A full graph topological order is

`1,0,3,6,2,5,4,7,8,9,...,22`.

The full graph includes actual order comparisons and every valid lower/upper structural arrow, not merely a quotient approximation. These predicates follow the good-pair theorem and very-good-pair definition in [Zaguia, arXiv:1610.00809v3, Definition 1, Theorem 2, Definition 5](https://arxiv.org/html/1610.00809). In a hypothetical poset without a balanced pair, each structural arrow must have comparison probability greater than 2/3, and all such arrows agree with the resulting total strong-majority order. Hence a cycle is a valid exclusion. Acyclicity alone does not assert existence of a counterexample.

The finite witness therefore gives genuine separation from this specified set of structural filters, while the prefix certificate explicitly finds a balanced pair. This is not a claim of novelty against all published balanced-pair criteria.

## 6. Symbolic infinite family, with exact cutoff safeguards

For any positive integer k, let P_k be the same completion with a k-vertex chain. The eight core vertices stay singleton vertices. Only the new tail block varies.

The nine-vertex quotient Q obtained by contracting that chain has predecessor masks

`(0,0,3,2,15,11,2,107,239)`.

The audit checks all its subsets and finds no proper nontrivial module, so Q is prime. Its nine (strict down-count, strict up-count) pairs are

`(0,5),(0,7),(2,2),(1,4),(4,0),(3,2),(1,2),(5,1),(7,0)`.

They are distinct, proving rigidity. Both graphs are connected, and the full graph is acyclic in order 1,0,3,6,2,5,4,7,8. Its formal two-port graph is also directly checked acyclic.

### Why every proper module of P_k is a chain

If a module M meets more than one quotient block, the blocks it meets form a module of Q: every disjoint block has a uniform relation to M. Primality forces M to meet all nine blocks. It then contains every singleton core vertex. Any omitted tail vertex would see core vertex 4 as incomparable and the other core vertices as below, contradicting autonomy. Therefore M=P_k. Every proper module is confined to a single block, and the only nonsingleton block is a chain. Within that chain, its modules are intervals.

### Why rigidity and forced-graph acyclicity persist for every k

The core down/up degree pairs become

`(0,k+4),(0,k+6),(2,k+1),(1,k+3),(4,0),(3,k+1),(1,k+1),(5,k)`.

The j-th tail vertex has degree pair (j+6,k−j), for 1≤j≤k. All these pairs are distinct, proving rigidity for every k without finite extrapolation.

For incomparable blocks A,B, an actual lower structural arrow x→y requires x to be bottom(A); otherwise an earlier element of A belongs to D(x) but not D(y). Its other conditions imply exactly the lower quotient predicate. Dually an actual upper arrow projects to an upper quotient predicate and has y at top(B). Actual comparison edges either project to quotient comparisons or stay forward inside a chain. Thus every interblock arrow projects into the acyclic full graph of Q. A cycle upstairs would give a cycle downstairs, unless it stayed inside one block, where chain order forbids it. Expanding the tail in the displayed quotient order therefore gives a topological order for every P_k. In particular none has a very-good pair.

### Remaining invariants and exact probabilities

Both graphs stay connected: tail vertices connect comparably to 7 and incomparably to 4. An antichain containing a tail vertex can contain at most vertex 4 besides it, so width remains 3. The longest core chain ending at 7 has four vertices, and height is k+4. The unchanged cover cycle 0−2−4−3−5−0 rules out a forest. Vertex 4 has exactly k+3 incomparable neighbors; every other old vertex has at most five, and each tail vertex has just vertex 4. Consequently

`π(P_k)=max(5,k+3)`.

The exact continuation and probability formulas are

`B=(k+1,1), e(P_k)=48k+121`,

`p(2<5)=(23k+79)/(48k+121)`,

`p(2<6)=(15k+55)/(48k+121)`.

The first probability is balanced for every k≥1. The second is below 1/3 exactly when k≥15. Thus the narrow one-chain family has a fixed balanced pair, even though the theorem over arbitrary guarded tails needs the adaptive menu.

The family passes the specified connectedness/module/rigidity/width/height/π/full-forced-graph funnel for **k≥4**. The cases k=1,2,3 still satisfy π≤6 and must not be presented as escaping that known cutoff. If one also invokes the previously reported n≤14 computational exclusion, restrict to **k≥7**, so |P_k|=k+8≥15. This audit does not rerun or independently re-prove that published small-order computation. The explicit k=15 witness is beyond both cutoffs.

Independent finite controls at k=1,2,3,4,15,31 verify these identities and structural assertions. The all-k conclusion follows from the preceding proof, not extrapolation from those tests.

## 7. Redundancy classification and unresolved scope

The 36 profiles divide as follows:

- **22** have a directed forced cycle entirely among nonmaximal core vertices. All their guarded completions are already rejected by the structural graph.
- **10** admit the supplied nonempty universal-top completion with an acyclic full forced graph. The audit verifies every such example. However, their core is a proper nonchain module and their incomparability graph is disconnected, so these examples alone do not separate the entire structural funnel.
- The remaining **4** profiles are `n8c03-primal`, `n8c04-dual`, `n8c09-dual`, `n8c14-primal`. The author's limited simple-tail test supplied no acyclic completion for them. No universal nonexistence statement is inferred, and this audit does not expand that tail search.

To justify the first item for arbitrary finite tails, the guard forces every nonmaximal x of C below every outside z. Otherwise choose a minimal outside t≤z. All predecessors of t lie in C. If x is not below t, neither is any core successor of x, leaving at most n−2 possible predecessors, contrary to the guard. Therefore all nonmaximal core vertices acquire exactly the same outside upset, with their downsets unchanged. Both structural predicates among them are preserved, as are their cycles.

The adaptive chain-tail family supplies the stronger entire-funnel separation that universal-top examples lack. The precise scope is actual singleton core vertices plus the verified guard. There is no uniform exclusion of arbitrary positive chain weights on all eight core vertices, no global bound on core size, no exhaustive tail classification, and no proof of the general 1/3–2/3 conjecture. No literature-priority claim is made.

## 8. Reproduction and frozen artifacts

From this directory, using Python 3 only:

```sh
python check.py > check.log
python -O check.py > check_optimized.log
cmp results.json results_optimized.json
python check_family.py > family.log
python -O check_family.py > family_optimized.log
cmp family_results.json family_results_optimized.json
python check_final_witness.py > final_witness.log
python -O check_final_witness.py > final_witness_optimized.log
cmp final_witness_results.json final_witness_results_optimized.json
sha256sum -c SHA256SUMS
```

`results.json` contains all reconstructed profiles, all 76 selected certificates and all 8,384 full-menu duals, every author concrete completion, the exact fixed-pair failures, structural witnesses and corruption tests. `family_results.json` contains the prime-quotient exhaustive subset result, adaptive isomorphism, complete finite family controls and formulas. `final_witness_results.json` checks the final exported complete 23-vertex pair table, quotient, graph, and π artifacts. `SHA256SUMS` freezes the report, independent sources, inputs and outputs.
