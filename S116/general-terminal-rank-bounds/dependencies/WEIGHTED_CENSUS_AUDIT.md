# Independent audit: weighted seven-core census

Date: 2026-10-10. **Final verdict: PASS for the frozen sources and precise scope below.**

The quotient has covers `0<3; 1<2,4; 2<3,6; 3<5; 4<5`, and its positive
chain lengths are `(u,a,b,c,t,d,v)`. All probabilities use the uniform law
on complete extensions of the actual labelled chain inflation.

## 1. Accepted conclusion and limits

**Every positive chain inflation with `a,b,c,d` each in `{1,2,3}` has a
balanced incomparable pair, with no upper restriction on `u,t,v`.**

This is a finite-computation-assisted infinite-family conclusion. The
previously proved universal necessary inequalities put any hypothetical
counterexample in a finite cone; the independent exact computation below
rejects every point of that cone. It is not an extrapolation from testing
small pendant weights.

The complete cone contains 2,767 vectors, with maximum order 52. The nested
spine scope `{1,2}^4` contains 165 vectors, with maximum order 32. All 18
forced orientations were counted directly at every vector; none survives.
No symmetry or duality quotient was used to reduce either enumeration or
probability computation.

There is no claim for arbitrary spine weights, no global bound on order or
core size, and no new global lower bound for the balance parameter. The
minimum `delta=3/7` reported here is only inside this necessary-condition
cone. Cone points are candidates of a relaxation, not counterexamples.

## 2. Complete passage from infinite families to finite computation

The structural good-pair theorem, in the exact form already audited in the
prior packages listed in the manifest, gives the following implication:
for incomparable `x,y`, if `D(x)` is contained in `D(y)` and
`U(y)\U(x)` is a chain, then any poset with no balanced pair must have
`Pr(x<y)>2/3`. For probabilities at most `1/2`, this is the contrapositive
of the good-pair theorem; probabilities in `(1/2,2/3]` are themselves
balanced. Order reversal supplies the upper version.

The port restriction can also be seen directly from the reconstructed
arrows. If `u=1`, then `T0=B0`. The events `B0<B2` and `T2<T0=B0` are
disjoint because `B2<=T2`, yet both would be forced above `2/3`. If `v=1`,
the same contradiction uses `B6<B3` and `T3<T6=B6`. Hence a counterexample
must have `u,v>=2`; no cardinality-minimality assumption is needed.

The audited outer insertion argument gives

`2u<a+b+t+v`, `2v<u+c+t+d`.

Indeed, deleting C0 and conditioning on a complete outside extension
leaves a uniform insertion window of length at most `a+b+t+v`.
Thus `Pr(B0<B1)>=u/(u+a+b+t+v)`, while its structurally forced opposite
is above `2/3`. The first inequality follows, and reversal gives the second.
This argument conditions under the original extension law; it does not
make outside extensions equiprobable.

The frozen generalized-shuffle theorem gives

`Pr(B2<B4)<(b+c+v)/(b+c+v+t)`,
`Pr(T4<T3)<(b+c+u)/(b+c+u+t)`.

Combining these bounds with the respective forced probabilities above
`2/3` gives `2t<b+c+v` and `2t<b+c+u`.

For an independent completeness bound, add the integer forms of the two
outer inequalities and the two middle inequalities:

`u+v<=a+b+c+d+2t-2`,
`u+v>=4t-2b-2c+2`.

Consequently `2t<=a+d+3b+3c-4<=20`, so `t<=10`. Since `a+b,c+d<=6`,
the outer inequalities imply `2u<=15+v` and `2v<=15+u`. Twice the first
plus the second gives `u<=15`; reversing them gives `v<=15`.

The independent enumerator therefore checks the entire rectangular box

`a,b,c,d in 1..3; u,v in 2..15; t in 1..10`,

which has exactly 158,760 candidates, and retains precisely those satisfying
the four original strict inequalities. It does not use the author's sharper
floor expressions or interval generator. Its resulting set equals all
2,767 author records, with no duplicates or missing vectors. The unique
order-52 point is `(15,3,3,3,10,3,15)`.

Every positive vector outside this rectangle or failing a necessary
condition is already excluded by the universal arguments. Every vector
inside the resulting cone is excluded by the exact forced-arrow checks.
These two disjoint parts exhaust all positive pendant triples in the stated
81-spine scope.

## 3. Structural orientations, endpoint compression, and thresholds

The independent code reconstructs the quotient transitive closure from its
seven covers. It then searches every ordered incomparable quotient pair
for downset inclusion and a chain upset difference. It obtains exactly:

- Bottom: `B0<B2`, `B0<B4`, `B0<B6`, `B1<B0`, `B2<B4`, `B4<B3`,
  `B4<B6`, `B6<B3`, `B6<B5`.
- Top, in the original order: `T1<T0`, `T2<T0`, `T4<T3`, `T0<T4`,
  `T2<T4`, `T6<T5`, `T0<T6`, `T3<T6`, `T4<T6`.

The top list is reconstructed by applying the criterion to the reversed
relation and then reversing the orientation. It is not the unreversed list
of bottom arrows on the dual.

For incomparable blocks, `D(x) subset D(y)` forces x to be the bottom of
its block: otherwise an earlier element in that block is not below y.
For a bottom x, the upper difference is a tail of y's block followed by the
inflations of the quotient upper difference. It is a chain exactly when
the quotient predicate holds. The target y may be any rank, and its bottom
is the strongest probability requirement by rank monotonicity. Reversal
gives the analogous top compression. Thus no additional structural
good-pair rank requirements were omitted from this endpoint menu.

For total extension count Z and orientation numerator N, rejection is
exactly `3N<=2Z`. The accepted hypothetical-counterexample threshold is
strictly `3N>2Z`. Equality is rejected; no floating-point tolerance is used.
There happen to be no exact `2/3` endpoint equalities among these 49,806
checks. A failed forced orientation guarantees a balanced pair somewhere;
it need not itself be the balanced pair.

## 4. Independent oracle and verification strength

`audit.py` imports no author implementation and does not run it. It builds
every actual labelled element and its full transitive predecessor mask
directly from the independently reconstructed quotient order. It generates
all reachable labelled ideals and all one-element extension transitions.
The masks' numeric order is topological because adding an element strictly
increases the mask.

The denominator is the number of paths from the empty ideal to the full
ideal. To count `x<y`, the oracle counts extensions of the augmented poset:
it discards every original ideal containing y but not x. Once x is present,
the added condition is satisfied and the original suffix count applies;
before either element appears, it sums the allowed child counts. This
constrained path recurrence differs from the author's forward/backward
transition-event accumulation and from its binomial formulas.

Each full extension contributes one unique ideal path; the surviving paths
are exactly those with x before y. This proves the numerator recurrence.
All top and bottom orientations are counted at each original vector;
duality is checked only afterward as an additional cross-check.

Independent results:

- 2,767 denominator equalities and 49,806 individual endpoint numerator
  equalities against the frozen census.
- 990,547 actual ideal states in aggregate, also matching every published
  per-vector state count.
- 341,222 actual incomparable-pair numerators independently computed.
  Every published per-vector pair count, balanced-pair count, delta, and
  complete maximizer list agrees.
- All individual pair numerators published for the 21 old-menu survivors
  agree, including their actual labels and orientations.
- 63,876 concrete balanced pairs found in total; each of the 2,767 vectors
  has at least one independently verified actual balanced pair.
- Every vector's dual is present, with equal denominators and every
  correctly reversed endpoint probability equal. No dual values were used
  as replacements for direct counts.

The unique minimum delta inside this cone is `3/7`, at
`(2,1,1,1,1,1,2)`. This is deliberately not promoted to a global statement.

## 5. Rejection menus and finite optimality

The old four tests are `B1<B0,T6<T5,T2<T0,B6<B3`. For spine maxima 1, 2,
and 3, their survivor counts are respectively 0, 1, and 21. In the largest
scope, successively adjoining those four and then `B2<B4,T4<T3` leaves

`923, 425, 27, 21, 1, 0` vectors.

The independent set-cover universe is **every cone vector**, not merely
the subset rejected by the full menu. All subsets of sizes 0 through 5
of the 18 arrows are tested: 12,616 subsets altogether. There is no cover
of size at most 4 and exactly two covers of size 5:

1. `B1<B0, T6<T5, B2<B4, T4<T3, T2<T0`.
2. `B1<B0, T6<T5, B2<B4, T4<T3, B6<B3`.

The `{1,2}^4` scope has minimum size 4 with exactly eight minimum menus,
all reproduced in results.json.

Exclusive rejection examples are independently reproduced:

- `(3,1,2,2,2,2,3)`: only `B1<B0` fails, with probability `5551/8720`.
- Its dual: only `T6<T5` fails.
- `(4,2,3,2,3,2,3)`: only `B2<B4` fails, with probability
  `1218468/1837711`.
- `(3,2,2,3,3,2,4)`: only `T4<T3` fails, with the same probability.

Thus the four common arrows are mandatory in any covering sub-menu of these
18 within this finite scope. This is a finite covering fact, not universal
logical independence.

## 6. Analytic diagnostic and the old-menu survivor

The audited rank-chain proof independently supplies the stronger necessary
orientations `Pr(T1<B0)>2/3` and `Pr(T6<B5)>2/3`. The exact binomial
upper-bound filters and the two old binomial lower-bound filters were
recomputed with integer arithmetic over the entire independently generated
cone. Their largest-scope cumulative survivor counts are

`723,185,185,185`.

The complete set of 185 analytic survivors agrees with the frozen JSON.
The nested singleton and maximum-spine-2 counts are respectively 2 and 27.
There are 18 equality cases for each old binomial lower filter, all correctly
excluded by its strict inequality; the two rank filters have no equality
cases in this cone. The old lower bounds remove nothing further once the
two rank upper filters are applied.

The analytic survivors intersect the old four exact tests in exactly

`w=(3,1,2,2,3,1,3)`.

Independent counts give `Z=142680` and old-four numerators
`95536,95536,105335,105335`. Both middle numerators are `90360`, hence
both middle probabilities are `753/1189`, in the closed balanced interval.
Its actual delta is `1700/3567`; the maximizing unordered labelled pairs
are `((0,3),(4,2))` and `((4,2),(6,1))`, each with forward numerator 74680.

Only one analytic survivor has both outer spine weights at least 2:
`(2,2,3,3,3,2,2)`. Its reported delta `11317/25818` also agrees.

These analytic diagnostics measure limitations of these particular bounds.
They leave no unresolved balance case in the enumerated scope, and the
rank-filter proof is not needed for the main exhaustive 18-arrow exclusion.

## 7. Frozen inputs, status wording, and reproduction

The author's complete `MANIFEST.sha256` is checked before computation. Its
`census.json` SHA-256 is
`d8d05b8e2e8f3a7b39e0ea7a92d368208fbc3bcb86f197528bd32ab1c8b1ec09`.
The generalized-shuffle proof SHA-256 is
`e522a13a63f73a58c1af862e603c3b90c46084a1f83b3b79da7e6bd3d6b0a8d3`.
All author, prerequisite, and audit artifact hashes are recorded in
`MANIFEST.json` and `SHA256SUMS.txt`.

The author's frozen prose and cone_audit.json retain historical statements
that the rank supplement and census peer audit were pending. Those status
notes are superseded by the frozen rank supplement and this audit. No
substantive mathematical correction to the census was needed, and no
original file was modified.

From this audit directory, run:

```sh
python audit.py --output results.reproduced.json > run.reproduced.log
python -O audit.py --output results.optimized.reproduced.json > run.optimized.reproduced.log
cmp results.json results.reproduced.json
cmp results.json results.optimized.reproduced.json
sha256sum -c SHA256SUMS.txt
```

Normal Python and `python -O` were both run successfully, and their complete
result files agree byte for byte. Validation uses explicit exceptions, so
optimization cannot disable it. The independent result contains no elapsed
time, timestamp, or other nondeterministic output keys; **no ignored JSON
keys are needed for reproduction**. The author sources are read-only inputs
and are not replayed into their original directory. No remote write or
external upload was performed.
