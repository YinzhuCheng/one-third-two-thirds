# Bounded exact weighted-seven-core obstruction census

Date: 2026-10-10. Scope: positive chain weights `(u,a,b,c,t,d,v)` on the quotient with covers

`0<3; 1<2,4; 2<3,6; 3<5; 4<5`.

## Result and status

All **2,767** integer weight vectors in the stated necessary pendant cone with
`a,b,c,d ∈ {1,2,3}` fail at least one of the **18 structural forced endpoint arrows**.
Every one also has a balanced actual-label pair, verified by a separate labelled
ideal DP. The nested `{1,2}^4` spine scope contains **165** cone vectors and also
has zero survivors. Maximum total orders are respectively 52 and 32.

These finite exact facts are established by the supplied reproducible programs.
The generalized-cone proof has now received frozen independent **PASS**
(proof SHA-256 `e522a13a63f73a58c1af862e603c3b90c46084a1f83b3b79da7e6bd3d6b0a8d3`).
Thus this is a complete finite reduction for *every positive pendant triple*
for each of these 81 fixed spines, using the previously audited good-pair/port
prerequisites. See `cone_audit.json` for the exact proof and audit hashes.
A fresh independent computational peer audit of this census is still requested;
the separate state-representation checks below are author verification, not a
peer audit. The analytic-only rank diagnostic additionally awaits its proof
supplement's final frozen audit.

No result for arbitrary spine weights or a counterexample is asserted. In
particular, numerical survival of any shorter menu is never a counterexample.

## Exact finite region

Write `s=b+c`, `alpha=a+b-1`, `beta=c+d-1`,

`U=floor((2 alpha+beta)/3)`, `V=floor((alpha+2 beta)/3)`,
`T=s-1+min(U,V)`.

The region enumerated is exactly

- `u,v >= 2`, `t >= 1`;
- `2u < a+b+t+v`, `2v < u+c+t+d`;
- `2t < b+c+u`, `2t < b+c+v`.

The final two inequalities follow from the independently audited and frozen
middle shuffle bounds and counterexample forced orientations. The original
weaker inequality `2t<u+b+c+v` is redundant here.

The optimized enumerator loops over

- `1 <= t <= T`;
- `lo=max(2,2t-s+1)`;
- `lo <= u <= t+U`;
- `max(lo,2u-t-alpha) <= v <= floor((u+t+beta)/2)`.

A separately written enumerator uses the weaker outer bounds

`2t <= a+d+3b+3c-4`,
`u <= floor((2(a+b+t)+(c+d+t)-3)/3)`,
`v <= floor(((a+b+t)+2(c+d+t)-3)/3)`

and filters the four original strict inequalities directly. Its output set is
identical, with no repeated vectors. No symmetry quotient was used to reduce
coverage. All dual vectors are present and independently counted.

## All structural endpoint arrows

Each displayed orientation must have probability strictly greater than `2/3`
under the assumption that there is no balanced pair. Every comparison is made
under the uniform law on complete extensions of the actual chain inflation.

Bottom arrows:

`B0<B2`, `B0<B4`, `B0<B6`, `B1<B0`, `B2<B4`,
`B4<B3`, `B4<B6`, `B6<B3`, `B6<B5`.

Top arrows, in the original order rather than the dual order:

`T1<T0`, `T2<T0`, `T4<T3`, `T0<T4`, `T2<T4`,
`T6<T5`, `T0<T6`, `T3<T6`, `T4<T6`.

The quotient structural criterion is reconstructed by code: incomparable
`i,j`, `D(i) ⊆ D(j)`, and `U(j)\U(i)` is a chain. These give bottom arrows;
applying the same criterion to the dual and reversing the orientation gives
top arrows.

These are sufficient to check all structural good-pair arrows of the actual
inflation, not merely a selection of quotient arrows. Indeed, for incomparable
blocks, `D(x) ⊆ D(y)` forces `x=B_i`: a non-bottom `x` has a predecessor inside
its own incomparable block which is not below `y`. The condition on the upper
set difference reduces to the quotient chain condition. The target can be any
rank of block `j`; among those requirements, `P(B_i<B_j)>2/3` is strongest by
rank monotonicity. The dual reasoning reduces every upper structural arrow to
one of the top endpoint arrows above.

An arrow is rejected exactly when `3N <= 2Z`, including equality. Failing a
forced arrow proves that some balanced pair exists by the good-pair theorem;
it does not necessarily identify that arrow itself as balanced.

## Which arrows actually matter in this finite scope?

The old menu comprises `B1<B0`, `T6<T5`, `T2<T0`, `B6<B3`.

| Spine scope | Cone vectors | Old-four survivors | Old-four plus two middle arrows | All 18 survivors |
|---|---:|---:|---:|---:|
| `{1}^4` | 2 | 0 | 0 | 0 |
| `{1,2}^4` | 165 | 1 | 0 | 0 |
| `{1,2,3}^4` | 2,767 | 21 | 0 | 0 |

The two middle arrows are `B2<B4`, `T4<T3`.
On the largest scope, applying the six tests in the order

`B1<B0, T6<T5, T2<T0, B6<B3, B2<B4, T4<T3)`

leaves respectively `923, 425, 27, 21, 1, 0` weights.

Exhaustive finite set cover on the 18 rejection sets finds exactly **two**
minimum menus, both of size **5**:

1. `B1<B0, T6<T5, B2<B4, T4<T3, T2<T0)`;
2. `B1<B0, T6<T5, B2<B4, T4<T3, B6<B3)`.

This is a finite covering result, not a claim of universal logical independence.
On `{1,2}^4`, the minimum size is 4, with eight minimum menus recorded in JSON.

There are finite-scope exclusive rejection witnesses establishing that the
following four arrows must occur in any covering sub-menu of these 18:

- `B1<B0`: e.g. `(3,1,2,2,2,2,3)`, probability `5551/8720`;
- `T6<T5`: the dual example;
- `B2<B4`: `(4,2,3,2,3,2,3)`, probability `1218468/1837711`;
- `T4<T3`: dual vector `(3,2,2,3,3,2,4)`, the same probability.

Every other one of the 18 arrows satisfies its forced threshold at the
respective exclusive witness. In particular one cannot remove either middle
orientation and expect the other 17 alone to exclude this entire box.

## The smallest old-menu survivor

The unique old-menu survivor in `{1,2}^4` is

`w=(3,1,2,2,3,1,3)`, total order 15, `Z=142680`.

Its old four numerators, in the old menu order above, are

`95536, 95536, 105335, 105335`.

All exceed `2Z/3`. Nevertheless,

`P(B2<B4)=P(T4<T3)=90360/142680=753/1189`,

so these are concrete balanced pairs. Independent all-pair labelled DP gives

`delta(P)=1700/3567`.

The maximizing unordered pairs are `((0,3),(4,2))` and
`((4,2),(6,1))`, each with forward numerator `74680`.
All 21 old-menu surviving weight vectors, all their incomparable-pair counts,
all actual balanced pairs, all maximizing pairs and exact deltas are saved in
`census.json`. There are no full-menu survivors requiring additional rank-pair
screening within this scope.

## Analytic-only diagnostic

A separate file preserves the stronger rank-chain constraints being established
by the outer-spine work. In any counterexample these require

`P(T1<B0)>2/3` and `P(T6<B5)>2/3`.

The reported universal upper bounds give the necessary binomial filters

`3 binom(b+t+v+u,u) > 2 binom(a+b+t+v+u,u)`,
`3 binom(c+t+u+v,v) > 2 binom(d+c+t+u+v,v)`.

The old top/binomial lower bounds give

`3 binom(a+b+u-1,u) < binom(a+b+t+v+u,u)`,
`3 binom(d+c+v-1,v) < binom(d+c+t+u+v,v)`.

For the same already finite cone, these four analytic filters leave

- 2 weights for singleton spine;
- 27 weights for spine in `{1,2}^4`;
- **185** weights for spine in `{1,2,3}^4`.

On the largest scope the rank filters leave 723 then 185 vectors. The two old
binomial lower bounds remove no further vectors after those rank filters.
The smallest analytic survivor is `(2,1,1,1,1,1,2)`, already a known balanced
example. Thus these particular universal bounds do not yet produce an
analytic-only empty region, even in this small spine scope.

Adding the old four *exact probability* tests to those four binomial filters
leaves **exactly one** vector throughout the largest scope:
`(3,1,2,2,3,1,3)` above. A middle-arrow exact count excludes it.
There is only one analytic survivor with both outer spine weights at least 2:
`(2,2,3,3,3,2,2)`, whose actual delta is `11317/25818`.
These are diagnostic targets for sharpening universal inequalities; none is an
unresolved balanced-pair case after the exact census.

`analytic_filters.json` records every analytic survivor, every bounding rational,
its failed exact arrows, actual delta and maximizing pairs. Its universal
interpretation depends additionally on the rank-chain proof audit.

## Verification and timings

Primary endpoint computation uses an ideal DAG whose states are seven actual
chain-prefix lengths. A transition adds one eligible actual element. Forward
and backward path counts compute every endpoint numerator; this does not use a
uniform quotient law. For an event `x<y`, summing

`prefix_count(I) * suffix_count(I union {x})`

over ideals where `x` is eligible and `y` has not appeared counts every desired
extension exactly once, at the transition which inserts `x`.

For every one of the 2,767 vectors:

- denominator agrees with the independent double-binomial formula;
- all old four endpoint counts agree with their binomial/deletion formulas;
- dual weight transformation `(u,a,b,c,t,d,v) -> (v,d,c,b,t,a,u)` gives all
  18 exact reversed endpoint probabilities;
- a separately coded DP over actual-labelled-element bitmasks agrees on the
  denominator and every endpoint numerator;
- every actual incomparable pair is counted in this second DP;
- both middle numerator formulas agree with the labelled DP.

Totals: **49,806** endpoint comparisons across independent state representations,
**341,222** actual incomparable-pair counts, **63,876** concrete balanced pairs,
and **5,534** middle-formula comparisons. All pass.
The primary DAGs contain 990,547 ideal states in aggregate.

The minimum delta **inside the enumerated cone only** is `3/7`, attained uniquely
at `(2,1,1,1,1,1,2)`. No such delta lower bound is claimed outside this cone;
for example known vectors excluded before cone enumeration can have smaller
delta.

Observed wall-clock times in this environment: primary census 5.172 s,
full independent-state-representation verification 8.546 s,
analytic diagnostic 0.046 s. Exact counts do not depend on these timings.
The programs use only Python's standard library and integer/rational arithmetic
for mathematical assertions and filters. Elapsed-time metadata uses floating
point. No external services, uploads, unbounded search, or extra spine boxes
were used.
