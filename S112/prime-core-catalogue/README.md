# Exact small prime-core catalogue for chain-inflation counterexample filters

## Scope and what the computation does not claim

This is a finite, reproducible catalogue of **naturally labelled** posets on
`{0,...,n-1}`, through `n=8`. Every comparability points from a smaller label to a
larger label. The main enumeration counts are not unlabelled-poset counts.
Only the surviving subset is subsequently canonicalized exactly up to order
isomorphism; order duals are not identified unless actually isomorphic.

A prime core has no autonomous subset of cardinality `2,...,n-1`. A subset M is
autonomous if every outside vertex has the same relation (below, above, or
incomparable) to every member of M. “Prime” is vacuous at orders 1 and 2; those
small conventions have no impact after requiring width at least 3.

The target is a chain inflation `P=Q(C_w0,...,C_w(n-1))`, with every `wi` a positive
integer. Every core-level rejection used below rules out **all** such weights.
The catalogue is conditional on the separate minimal-counterexample reduction
to weighted prime cores; it does not replace that reduction's proof.

Survival is only failure of these particular necessary tests. It does not show
that a counterexample exists, even for one weight vector. No upper bound on
core size, total inflated size, or chain weights is asserted. There is no
height-two shortcut, no unweighted automorphism exclusion for arbitrary weights,
and no premature identification of bottom and top ports.

## Exact results

The generated `COUNTS.md` gives all nested counts. Main results:

- Every prime core of width at least 3 through order 6 has a very-good pair on
  one side or the other, so none can support a counterexample chain inflation.
- At order 7, exactly 44 natural labellings remain, forming one isomorphism class.
  It has width 3 and height 4.
- At order 8, exactly 2,552 natural labellings remain, forming 17 isomorphism
  classes: 16 of width 3 and one of width 4.
- Neither the separate bottom/top cycle tests nor the generic two-port cycle
  test excludes any additional core beyond the very-good-pair test through
  order 8. Thus this catalogue does **not** demonstrate added strength from a
  genuinely longer uniform cycle certificate.
- All 18 surviving isomorphism classes are rigid as unweighted posets. This is
  reported data, not used as an all-weights rejection rule.

## Proof-backed filters

### F0. Primality

The explicit subset test is exactly the autonomous-module definition above.
The reason to restrict the search to these cores is the weighted-prime
minimal-counterexample reduction, not a computational observation.

### F1. Width at least 3

An antichain in P meets each substituted chain at most once and projects to an
antichain of Q. Conversely an antichain in Q lifts by choosing one point per
block. Thus `width(P)=width(Q)`. Width 1 gives a chain; the known width-two case
rules out a nonchain counterexample of width 2. Zaguia's introduction records
the width-two theorem and attributes it to Linial.

### F2. No very-good pair in either orientation

Source: Imed Zaguia, *The 1/3–2/3 Conjecture for ordered sets whose cover graph
is a forest*, Definition 5 and Theorem 2:
https://arxiv.org/html/1610.00809 . Definition 1 specifies the good-pair premise.
The theorem guarantees a balanced pair somewhere, not necessarily the pair
used as the certificate.

Write `D(a)={x:x<a}` and `U(a)={x:a<x}`. The structural very-good test is
`D(a)=D(b)`, with both `U(a)\U(b)` and `U(b)\U(a)` chains, allowing the empty
chain. Perform the test in Q and its dual separately.

Let Ba be the bottom of block a. Equal core downsets give equal downsets of
Ba,Bb. Their two upper-set differences are respectively the remainder of the
source chain followed by the chain inflation of the corresponding core
upper-set difference. Each is a chain. Thus a core very-good pair lifts at
bottom ports for every weight choice. The dual argument uses top ports.
One of the two orientations has probability at most one half, so the source's
good-pair theorem applies.

### F3. Separate forced-good cycle tests

In a poset with no balanced pair, define `a prec b` when its uniform extension
probability `Pr(a before b)>2/3`. This is a strict total order extending the
poset: for `a prec b prec c`, the union bound gives `Pr(a before c)>1/3`, and
absence of a balanced pair forces it above `2/3`. Hence every directed graph
whose edges are forced to point forward in this order is acyclic.

For incomparable a,b with `D(a) subseteq D(b)` and `U(b)\U(a)` a chain, the
source's good-pair theorem and absence of a balanced pair force
`Pr(a before b)>2/3`. In a chain inflation these hypotheses lift from Q to
bottom ports Ba,Bb: the lower-set containment persists, and the upper-set
difference is the remainder of block b followed by the inflated core chain.

The bottom graph consists of all Q comparabilities and these directed
structural-good edges. A directed cycle rejects every positive weight vector.
Apply the same construction separately to the dual Q*. Its edges use the
order of Q*; to interpret them on the actual top ports of P, reverse every
edge. Reversal preserves cyclicity. Bottom and top vertices are not combined.
A very-good pair already supplies a two-cycle, so F2 is logically subsumed by
F3, but retaining both stages makes their observed contributions explicit.

### F4. Generic two-port cycle test

Give each core vertex distinct *formal* ports Bi and Ti. Add:

1. `Bi -> Ti` for each i;
2. all interblock comparability edges between either source/target port;
3. `Ba -> Bb` for every lower structural-good edge of Q;
4. `Tb -> Ta` for every lower structural-good edge `a -> b` of Q*.

All interblock edges strictly increase the canonical order rank of the
corresponding actual endpoints in a hypothetical counterexample. Internal
`Bi -> Ti` edges are weakly increasing: equality occurs exactly when `wi=1`.
Every formal cycle contains an interblock edge, since internal edges alone
only point from B to T. A weakly increasing closed walk with at least one
strict step is impossible. Thus a cycle rejects **all** positive weights.

### F5. Singleton-pattern constraints on surviving cores

For a prescribed subset S of indices, assume `wi=1` for each i in S and
identify just those `Bi=Ti`. Omit the resulting internal weak self-loop, but
retain all interblock edges. A cycle excludes every weight vector satisfying
those singleton equalities. Exhaust all `2^n` subsets, retaining the
inclusion-minimal forbidden subsets. Each such subset S yields the necessary
clause: at least one `wi>=2` for i in S.

This is a weight-dependent refinement, not an all-weights core exclusion.
The file `all_survivor_singleton_constraints.json` records every minimal clause
and an exact directed-cycle certificate. Formal port `2i` means Bi and `2i+1`
means Ti. In a contracted certificate, a merged port is named by its even
representative. All superset singleton patterns of a forbidden set are also
forbidden: further contraction cannot remove every strict interblock step.

## The unique smallest surviving shape

A deterministic natural representative has strict upper-set masks
`(40,124,104,32,32,0,0)`, i.e. cover relations

`0<3; 1<2; 1<4; 2<3; 2<6; 3<5; 4<5`.

Its width is 3, its height is 4, it has 44 linear extensions, and its
unweighted automorphism group is trivial. No proper autonomous module exists.
It has no very-good pair in either orientation; all three generic port graphs
are acyclic.

Nevertheless, any potential counterexample inflation on this skeleton must
satisfy **w0>=2 and w6>=2**:

- If w0=1, the forced path `B0 -> B2 -> T2 -> T0` closes at `B0=T0`.
- If w6=1, the forced path `B6 -> B3 -> T3 -> T6` closes at `B6=T6`.

Those are exactly the two minimal forbidden singleton subsets. The other five
blocks may all be singleton without a port-cycle obstruction. The resulting
local necessary total-size bound is 9, not a claim that a 9-point
counterexample exists. No bound on arbitrary larger cores follows.

## Enumeration, canonicalization, and checks

`catalogue.py` adds the largest natural label as a maximal element with an
arbitrary order ideal of the old poset as its downset. Inductively this produces
each naturally labelled transitive relation once and only once. It never
canonicalizes or suppresses a relation during the main count.

`independent_catalogue.cpp` instead runs through every subset of the possible
strict comparabilities and retains transitive relations. Its module test
compares outside-vertex relation signs directly, and its cycle oracle uses
transitive closure rather than the Python DFS. It independently enumerates
through order 8 and produces the complete survivor list. The final crosscheck
compares every nested count and every surviving relation, not just totals.

`independent_tests.py` is a further set-based small oracle. It compares the
actual relation sets from both generators through order 6 and checks every
predicate there. It also checks all weight vectors in `{1,2}^n` for all natural
cores through order 4: 706 inflations, 6,592 forced-good lifts, 2,344 very-good
lifts, 706 width equalities, and 676 exact balanced-pair existence checks.
These finite checks supplement the proofs; they do not establish the
all-weights claims by themselves.

`canonicalize.py` acts only on surviving relations. It partitions vertices by
in/out-degree invariants, fixes a deterministic order of the classes, and
exhausts every permutation inside every class. The smallest resulting
adjacency tuple is an exact isomorphism key. This restriction is sound because
an isomorphism must preserve those invariants. It also counts automorphisms
and checks, for every class,

`natural-labelled multiplicity = number of linear extensions / |Aut(Q)|`.

The displayed representative is always the lexicographically least natural
upper-mask tuple of that class. The canonical adjacency itself may not be
naturally labelled. No duality quotient is taken.

## Reproduction

Requires Python 3.10+ (standard library only); the independent full oracle also
requires a C++17 compiler. No third-party package is needed.

```
python catalogue.py --max-n 8
python independent_tests.py
c++ -O3 -std=c++17 independent_catalogue.cpp -o /tmp/prime_core_oracle
/tmp/prime_core_oracle 8 > independent_catalogue_n8.json
python canonicalize.py
python build_report.py
python verify_package.py
```

`build_report.py` produces the final counts, exact crosscheck, survivor class
summary, and all singleton constraints. `verify_package.py` validates the saved mathematical results. Use
`python verify_package.py --hashes` to additionally check the frozen manifest.
A fresh enumeration records elapsed times that can differ without changing any
mathematical result; byte-for-byte manifest checks apply to the original freeze.

Original algorithms in this directory were written for this catalogue.
Earlier module/chain-inflation scripts in the accompanying structural-reduction
work were inspected read-only for definitions and independent comparison; no
third-party poset-generation software was used. No remote repository or
external account was modified.
