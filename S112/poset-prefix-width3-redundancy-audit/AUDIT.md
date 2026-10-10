# Scope correction: guarded width-three templates are subsumed by very-good pairs

Date: 2026-10-10. **Verdict: the balanced-pair existence exclusions for all three displayed guarded templates, including every claimed ordinal-prefix and finite-tail extension, already follow from Zaguia's very-good-pair criterion. They are not additional structural exclusions of possible 1/3–2/3 counterexamples.** The exact prefix tables, LP certificates, adaptive finite menus, and their stated quantitative bounds are not invalidated. Their novelty beyond existing results has not been established by this audit.

This is a scope addendum to the original exact-certificate audit, not a replacement or mutation of its frozen historical files. No remote write was made.

## 1. Primary source and the implication actually used

Imed Zaguia, *The 1/3-2/3 Conjecture for ordered sets whose cover graph is a forest*, [arXiv:1610.00809v3](https://arxiv.org/pdf/1610.00809v3), Definition 5 (PDF page 3) and Theorem 2 (PDF page 2); published in *Order* 36 (2019), 335–347, [DOI 10.1007/s11083-018-9469-0](https://doi.org/10.1007/s11083-018-9469-0).

Write D(x) and U(x) for strict lower and upper sets. Definition 5 calls a distinct pair (x,y) very good if, in the poset or its dual, D(x)=D(y), while each of U(x)\U(y) and U(y)\U(x) is a chain, possibly empty. Either orientation has comparison probability at most 1/2; with equal lower sets and both difference chains, that orientation meets Definition 1's good-pair conditions. Theorem 2 then supplies a balanced pair somewhere in the poset.

The forest theorem is not needed. The very-good pair itself need not be balanced, so lawful completions where that pair's probability exceeds 2/3 do not contradict this reduction.

## 2. Guard-preservation lemma

Let P be finite and C an initial ideal of size n. Suppose no outside element occurs in the first n−1 positions of any linear extension. Equivalently, every outside z has at least n−1 strict predecessors in P: its earliest possible rank is |D(z)|+1, obtained by extending its predecessor ideal and then placing z.

**Claim.** Every nonmaximal element x of C is below every z outside C.

**Proof.** Otherwise choose a minimal element t of the nonempty set of outside elements at or below z. Minimality makes every strict predecessor of t belong to C. Also x is not below t, since x<t≤z would contradict the choice of z. Since x is nonmaximal in C, choose y in C with x<y. Neither x nor y can belong to D(t): y<t would again imply x<t. Hence D(t) is contained in C\{x,y}, giving |D(t)|≤n−2, contrary to the guard. This proves the claim.

Consequently, for any nonmaximal x in C,

- D_P(x)=D_C(x), because C is initial;
- U_P(x)=U_C(x) union (P\C).

For two such elements x,y, both upper-set differences are therefore exactly their core differences. Every very-good pair in C whose endpoints are nonmaximal survives in P. This conclusion requires no restriction on the size, width, shape, or number of components of the finite tail.

A useful equivalent view: a minimal outside element t has D(t) contained in C and of size at least n−1. Thus D(t) is either C or C\{m} for a maximal m of C. In either case it contains every nonmaximal core element.

## 3. The exact surviving pairs

All sets below are strict. They were independently reconstructed from the displayed Hasse edges.

| Template | Very-good pair | Both lower sets | First upper difference | Second upper difference |
|---|---|---|---|---|
| six-boundary | (a,b) | empty | {c,e}, with c<e | empty |
| six-triangle | (a,b) | empty | {c,e}, with c<e | {d} |
| seven-three-minima | (a,c) | empty | {d,g}, with d<g | empty |

Each listed endpoint is nonmaximal. The preceding lemma preserves these data in every guarded completion. Each such completion already has a balanced pair by Zaguia's result.

For clarity, in six-boundary U(a)={c,d,e,f} and U(b)={d,f}; in six-triangle U(a)={c,e,f} and U(b)={d,f}; in seven-three-minima U(a)={d,f,g} and U(c)={f}.

## 4. The weakest exact cut-support formulation used by the existing audit

The original audit also permits a completion whose actual rank-(n−1) prefix ideals are verified directly to be exactly J_m=C\{m}, with the displayed induced cut orders. This does not escape the reduction.

There are three distinct omitted maximal labels in each displayed template, so the union of these actual ideals is C. A union of order ideals is an order ideal. Thus initiality of C follows, rather than needing to be separately assumed. Every actual prefix set at that rank is contained in C. If an outside point could occur earlier, extend that prefix to length n−1; the resulting actual cut state would contain an outside point, a contradiction. Therefore the guard follows as well.

The induced core order is also recovered from the labeled cut orders: for every two core labels at least one of the three states contains them both. Its induced order determines their comparability. Hence the same preservation proof applies under this directly verified, exact labeled-support premise.

This argument is about actual shared labeled prefix states and induced orders. An abstract equality of numerical count tables, or a merely isomorphic table without a consistent common labeling and verified support, is not by itself the structural premise used here. The general LP transfer method may apply elsewhere; this audit only resolves the three displayed template families.

## 5. Arbitrary common lower blocks

Let C=H⊕T be the stated initial ideal, with arbitrary finite H and one displayed core T, and apply the guard at |H|+|T|−1. The same listed endpoints are nonmaximal in C. Their strict lower sets are now both H; their strict upper differences remain precisely the chains in the table. The preservation lemma applies to this larger C, so every lawful finite completion again has a very-good pair and is already excluded by Zaguia's criterion.

The direct cut-support formulation is equally covered: the actual states are H union (T\{m}); their union is C, and the preceding argument recovers the guard. Arbitrary common ordinal prefixes therefore do not provide additional counterexample exclusions beyond the known theorem.

## 6. What survives, and what must be corrected

Retain the exact arithmetic, all-orientation LP certificates, finite adaptive pair menus, positive-completion fixed-pair failures, quantitative interval bounds, and the genuine vertex-only negative control. These establish useful facts beyond merely checking three isolated core posets. A narrower-menu or quantitative statement is logically stronger than unqualified balanced-pair existence, but this audit does not certify that such refinements are new in the literature.

Remove or qualify any claim that these three guarded families newly narrow the possible counterexample class beyond existing very-good-pair reductions. Existence of a balanced pair for every completion in each family is already known by the structural criterion above.

## 7. Independent finite checks

`check_redundancy.py` imports no author implementation. It reconstructs transitive closures from the Hasse edges and checks the exact pairs and upper differences. For each core, both alone and above a two-element antichain, it enumerates all naturally ordered guarded tails with zero through three added vertices. The respective counts are 1, 4, 23, and 190, for 218 cases per family and 1,308 cases in all. Every case verifies the guard-preservation conclusion, the very-good pair, and the exact full rank-cut support. These finite checks supplement, rather than replace, the unbounded proof.

Both `python check_redundancy.py` and `python -O check_redundancy.py` pass. All checks use explicit exceptions, so optimized Python does not disable them. Results are in `checks.json`; normal and optimized logs are included. `SHA256SUMS` freezes this addendum and its checker/output files.
