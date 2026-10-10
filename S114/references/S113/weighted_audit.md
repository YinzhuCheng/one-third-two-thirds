# Independent audit: seven-block weighted survivor

Date: 2026-10-10. Verdict: **PASS** for the frozen claims and implementation.

## 1. Scope and frozen inputs

The audited quotient has covers `0<3; 1<2,4; 2<3,6; 3<5; 4<5`.
Weights are `(u,a,b,c,t,d,v)=(w0,w1,w2,w3,w4,w5,w6)` and each
positive-weight block is a chain, with all interblock comparisons inherited
from the quotient. All probability statements concern the uniform law on
complete linear extensions of this actual chain inflation.

The five source files are copied unchanged into `frozen/`. Their SHA-256
digests are recorded in `results.json` and `SHA256SUMS.txt`. The audited
`ANALYTIC_RESULT.md` includes Sections 8–10, namely the two unrestricted
corollaries and the bounded rejection-menu summary. Its frozen statement
that audit was pending is a historical status note, superseded by this audit.
`explore.py` is not part of the audited source package.

The mathematical claims pass without a substantive correction. There is one
cosmetic wording issue: the validation-code comment calls the B0-first bound
“Strict lower bound”, whereas the proved bound and code assertion are weak
`>=` bounds. The necessary counterexample inequalities are nevertheless
strict, correctly, because the forbidden balance interval is closed. The
comment also uses `d` where its intended outside-window variable is `h`.

## 2. Independent computation and reproducibility

Run from this directory:

```sh
python audit.py > run.log
sha256sum -c SHA256SUMS.txt
```

No third-party packages are needed. The oracle in `audit.py` independently
constructs the quotient's Boolean transitive closure and then its actual
labelled chain-inflation ideal DAG. A state records how many labels have
appeared from each of the seven chains. Adding label `(i,r)` is permitted
exactly when it is the next label of its chain and all predecessor blocks
are exhausted. This is a compact representation of actual labelled ideals,
not a random-order model on seven quotient vertices.

Total counts come from backward recursion on the ideal DAG. Pair numerators
come from a separate forward/backward edge count: when the later tested
label is appended, sum the number of prefix extensions times the number of
suffix extensions, provided the earlier tested label is already present.
This does not use the author's split formula or its extra-comparison-edge
DP. For the smallest menu survivor, explicit enumeration of all 1,121
complete labelled extensions supplies a further independent check.

Verified results:

- Every one of the 2,187 vectors in `{1,2,3}^7`: total count, all four
  reported endpoint numerators, duality, and six lower bounds (three bounds
  and their duals). There are 13,122 independently counted pair numerators,
  2,187 total counts, and 13,122 bound checks.
- 4,725 auxiliary deletion vectors with `u,a,d,v` in `{0,1,2,3}`, at least
  one of those four zero, and `b,c,t` in `{1,2,3}`. The induced-deletion
  oracle retains quotient transitive comparisons before removing labels.
- 160 additional seeded vectors with positive weights at most 9; seed
  `20261010`. These are implementation spot checks, not a theorem over that
  entire larger box.
- Exact reproduction of the author's standalone and cumulative rejection
  counts, all 25 residual vectors, the smallest residual, all its seven
  balanced unordered pairs, and both balance-maximizing pairs.
- Both original author programs are rerun in an isolated temporary copy;
  both original JSON outputs reproduce byte for byte.
- Four-ray cone boundary checks for `1<=t<=100` agree with the proof below.
- Explicit insertion-fiber checks in four small examples validate the
  conditional law, the window lengths, and the conditional binomial
  numerator. All four examples have unequal outside fiber sizes; this
  directly detects why a uniform-outside shortcut would be invalid.

Every equality case found at the linear or binomial rejection thresholds
is rejected, correctly: 99 equality vectors for each of the three linear
tests, and 90 for each of the two binomial tests in the positive box. No
tested endpoint probability hits its exact `1/3` or `2/3` threshold in that
box; correctness there follows from exact integer comparison and the
closed balanced interval, not from a numerical tolerance.

## 3. Count and endpoint identities

The split immediately after the top of block 2 is unique in every complete
extension. If `i` block-0 labels and `j` block-4 labels precede that top,
the prefix has:

- all `a` block-1 labels;
- `b-1` earlier block-2 labels shuffled with `j` block-4 labels after block 1;
- `i` block-0 labels inserted before the fixed terminal block-2 label.

These choices give precisely the two binomial factors in `F(i,j)`. In the
suffix, the remaining block-0 labels followed by block 3 are one chain;
the remaining block-4 labels are a second chain; all block-5 labels follow
both chains; and block 6 is free to shuffle with that whole suffix. This
gives `G(i,j)`. Thus the `(u+1)(t+1)`-term identity is exact.

Setting `a=0` means deleting the whole block 1 from the induced poset, and
setting `d=0` means deleting block 5. The same split proof still works:
the initial or final chain is simply empty. The retained blocks 2,3,4 are
nonempty, so all binomial arguments remain valid. The implemented extra
allowance `u=0` and/or `v=0` also works by deleting the corresponding
pendant chain. This audit does not claim arbitrary zero patterns involving
blocks 2,3,4 are supported. In particular, the author's `dp_oracle` is
intended for positive vectors; zero-block comparisons here use the new
induced-deletion oracle, not that routine.

There are only two original minimal labels, B0 and B1. Therefore B1<B0 is
equivalent to B1 being first. Deleting that first label gives exactly the
extension count with `a` replaced by `a-1`, including `a=1`. The only
maximal labels are T5 and T6; dually, T6<T5 means T5 is last, giving the
count with `d-1`, including `d=1`.

The event T0<T2 holds exactly when the split has `i=u`. Reversal plus the
quotient involution `(0 6)(1 5)(2 3)` sends weights to
`(v,d,c,b,t,a,u)` and this event to B3<B6 in the original poset. This is a
bijection between weighted extension sets, and does not suppose arbitrary
weight vectors are self-dual. All four event identities therefore pass.

## 4. Good-pair implications and strictness

The external theorem was checked directly in the primary source:
[Imed Zaguia, arXiv:1610.00809v3, Definition 1 and Theorem 2](https://arxiv.org/html/1610.00809).
For an incomparable ordered pair `(x,y)`, the structural conditions
`D(x) subset D(y)` and `U(y) minus U(x)` a chain imply the following:
if `p(x<y)<=1/2`, the theorem guarantees a balanced pair somewhere in the
poset. If `1/2<p(x<y)<=2/3`, the displayed pair itself is balanced.
Consequently a poset with no balanced pair must have `p(x<y)>2/3`.
The dual argument supplies the upper-rule forced orientations.

The needed quotient arrows, with chain-inflation endpoint lifts, are:

- B1 to B0: equal empty downsets and `U(0) minus U(1)` empty.
- T6 to T5: the dual arrow.
- T2 to T0: `U(0) subset U(2)` and `D(2) minus D(0)={1}`.
- B6 to B3: `D(6) subset D(3)` and `U(3) minus U(6)={5}`.
- B2 to B4: equal downsets `{1}` and `U(4) minus U(2)` empty.

The within-block tails/prefixes in these endpoint lifts are chains and
remain in the required ordinal order with the quotient differences.
Thus the hypotheses hold for every positive weight vector. No
cardinality-minimality hypothesis is needed. A rejection via the theorem
promises some balanced pair, not necessarily the endpoint pair tested.

All complementary-event inequalities are strict in a counterexample.
Equality at `1/3` or `2/3` is balanced and is excluded. This justifies
every strict sign in the author's exact integer rejection tests.

## 5. Conditional insertion law and bounds

Fix a complete outside extension after deleting one chain module of length
`k`. All predecessors precede all successors, so there is one insertion
window, containing `h` outside labels. There are exactly `binom(h+k,k)`
legal insertions, each yielding one complete extension. Conditional on
this fixed outside extension under the original uniform complete-extension
law, these insertions are equiprobable. Outside extensions themselves have
probability proportional to this insertion count, and are not assumed
equiprobable.

The probability the inserted chain is first in the window is `k/(k+h)`.
For block 0, the outside extension starts with B1, the window ends before
B3, and its length is at most `a+b+t+v`. Hence
`p(B0<B1)>=u/(u+a+b+t+v)`. The forced complement is less than `1/3`,
yielding `2u<a+b+t+v`. Duality yields `2v<u+c+t+d`.

For block 4, the window starts after T1 and ends before B5. It contains
all of blocks 2 and 3, and at most all of blocks 0 and 6, so its length is
at most `u+b+c+v`. Being first in this window implies B4<B2; it is not
necessary to assert equivalence. Therefore
`p(B4<B2)>=t/(t+u+b+c+v)`, and the forced B2-to-B4 arrow yields
`2t<u+b+c+v`.

For block 0, if T2 is the `k`th outside label in its window, all `u`
inserted labels precede T2 in exactly `binom(k+u-1,u)` insertions out of
`binom(h+u,u)`. Here `k>=a+b` and `h<=a+b+t+v`. The numerator increases
with `k` and the denominator increases with `h`, giving the claimed
pointwise lower bound. Averaging under the correct reweighted outside law
preserves this lower bound. Combining it with the strict forced threshold
gives exactly the stated binomial inequality and its dual.

These bounds are weak pointwise/unconditional lower bounds followed by a
strict counterexample requirement. They do not claim the bounds are sharp.

## 6. Finite tails and both unrestricted corollaries

Write `A=a+b+t`, `B=c+d+t`. Integrality gives
`2u-v<=A-1` and `2v-u<=B-1`. Adding once gives
`u+v<=A+B-2`; taking twice the first plus the second gives
`3u<=2A+B-3`, and the dual combination gives
`3v<=A+2B-3`. These prove the displayed finite bounds after all five
central weights are fixed. They do not bound those five weights.

The already audited port-cycle argument forces `u,v>=2`: when `u=1`,
the chain B0 to B2 to T2 to T0=B0 is impossible in a strong-majority
order; when `v=1`, its dual is impossible. Internal steps can be weak
when the intermediate chain is a singleton, but interblock steps are
strict, so those singleton edge cases do not evade the contradiction.

If all five central weights equal 1, then `A=B=3` and the finite bounds
give `u,v<=2`. With the port restriction, only `(u,v)=(2,2)` remains.
That inflation has 315 extensions and `p(B1<B0)=202/315`, inside the
closed balanced interval. This proves the claimed exclusion of every
positive `(u,v)`, an actual infinite-family reduction.

If only `a=b=c=d=1`, put `s=u+v` and `r=u-v`. The three integral cone
conditions become

```text
s >= 2t-1,
s + 3|r| <= 2t+2,
s and r have the same parity.
```

When `s=2t-1`, parity and the bound force `r=1` or `-1`; when `s=2t`,
they force `r=0`; `s=2t+1` is impossible; and `s=2t+2` forces `r=0`.
Thus exactly the four stated forms remain:
`(u,v)=(t,t-1),(t-1,t),(t,t),(t+1,t+1)`, additionally requiring
`u,v>=2`. This argument is for every positive integer `t`; the numerical
checks are not being extrapolated. It is a necessary restriction only.

## 7. Exact bounded screen and boundary of the result

The independently recovered cumulative survivor counts are:

```text
972 -> 927 -> 883 -> 874 -> 847 -> 829 -> 616 -> 441 -> 42 -> 25.
```

The smallest surviving vector is `(2,1,1,1,2,1,2)` of order 10. It has
1,121 extensions and the four tested endpoint numerators
`766,766,315,315`, all passing their strict requirements. Its actual
balance constant is `454/1121`; for example,
`p((2,1)<(4,1))=667/1121`. There are exactly seven balanced unordered
pairs. These statements were checked by both ideal-DAG counts and explicit
complete-extension enumeration.

The 25 vectors therefore survive only this short menu. The smallest one
already fails the full forced-orientation requirement at another known
arrow, B2 to B4. The result does not claim a counterexample, completeness
of this four-probability menu, exclusion of every point on the four rays,
an all-weight theorem for the core, or a global bound on core size or
total cardinality. The user-relevant mathematical shrinkage is the proved
cone, finite pendant ranges for fixed central weights, the unrestricted
five-singleton-central exclusion, and the four-ray restriction.
