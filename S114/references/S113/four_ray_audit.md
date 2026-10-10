# Independent audit: exclusion of all four weighted rays

Date: 2026-10-10. Verdict: **PASS** for the frozen proof and its claimed three-parameter family theorem. No substantive correction is needed.

## Audited conclusion and exact scope

Let the seven-block quotient have covers

`0<3; 1<2,4; 2<3,6; 3<5; 4<5`.

Replace each block by a nonempty chain of lengths
`(u,1,1,1,t,1,v)`. Under the uniform law on complete linear extensions of this actual labelled poset, the new proof establishes

`Pr(B2<B4) < (v+2)/(v+t+2)`

for every positive integer `u,t,v`. The weak inequality alone suffices for the application. Together with the previously audited cone and singleton-port filters, and three explicitly checked small cases, this proves that **every inflation in this entire three-parameter family has a balanced pair**.

This is a new unrestricted family theorem. It is not an all-seven-weight theorem, a full proof of the 1/3–2/3 conjecture, or a claim that the tested pair itself is always balanced. The previous result only restricted potential counterexamples to four rays; this result excludes every point on those rays.

The exact author inputs are preserved in `frozen/`. The prior proof and independent audit used as dependencies are preserved in `dependencies/`. Digests for all frozen inputs and the audit files are in `SHA256SUMS.txt`.

## 1. Conditional-law audit: no omitted factors

Use `A=C0`, `C=C4`, `F=C6`, and singletons `r=B1`, `s=B2`, `x=B3`, `z=B5`. Condition on:

- `i`, the number of A-labels before r;
- `f`, the number of F-labels before z;
- the relative order S of s, x, and those first f labels of F.

Every label outside A is above r, so the prefix before r is exactly the unique A-prefix of length i. Every label outside F is below z, so the suffix after z is exactly the unique F-suffix of length v−f. Both statements hold also at their endpoints `i=0,u` and `f=0,v`.

The conditioned relative order S starts with s, because s precedes x and every F-label. Its length is `k=f+2`, and x has some rank `q` with `2<=q<=k`. Conversely, f and q determine the entire internal S-order, because the F-labels are a fixed chain.

Strictly between r and z, the labels are exactly A's remaining `a=u−i` labels, all t C-labels, and the k labels of S. The original poset imposes no relation between A and C, no relation between C and S, and no relation between A and the F-labels. The only remaining cross-relation is that all A-labels precede x=S_q. All internal relations of S are imposed by the conditioning itself.

Thus every allowed three-chain shuffle gives exactly one complete extension with these fixed data, and every such complete extension arises once. The conditional distribution on these shuffles is uniform. There is no additional prefix/suffix multiplicity and no use of a uniform distribution on quotient extensions or on deletion extensions.

Fix a binary shuffle of S and C, and let R be the rank of S_q. There are R insertion gaps before S_q. Distributing a ordered A-labels among them gives exactly

`W(R)=binom(a+R−1,a)`.

This is the entire fiber multiplicity. For `a=0`, it is identically one. For arbitrary a, it is positive and nondecreasing in R.

## 2. Stochastic domination and reweighting

This is a pointwise coupling, not a comparison of mean ranks. Let `n=k+t`, with `k,t>=1`. On the n−1 positions `{2,...,n}`, draw a uniform k-subset U. Delete a uniformly selected member to obtain V, a uniform (k−1)-subset. To verify this marginal exactly: each V has t possible missing positions that form a U; all pairs `(U,deleted member)` have the same probability, so every V has equal probability.

The binary word with S-positions U has the uniform law conditional on its first letter being C. The word with S-positions `{1} union V` has the uniform law conditional on its first letter being S.

For `q=1`, the S-first rank is 1 and the C-first rank is at least 2. For `2<=q<=k`, the ranks are `V_(q−1)` and `U_q`. Removing one member gives

`V_(q−1) <= U_q`

pointwise: the left side is either `U_(q−1)` or `U_q`. This includes q=k and the singleton k=1 endpoint through the separate q=1 case.

Write E for the event that S is first and let its unweighted probability be `p=k/(k+t)`. The coupling and monotonicity of W give

`alpha=E[W(R)|E] <= beta=E[W(R)|not E]`.

Both are positive. The weighted probability is exactly

`p*alpha / (p*alpha + (1−p)*beta) <= p`.

Therefore each conditional fiber from Section 1 has

`Pr(s<B4 | i,f,q) <= (f+2)/(f+t+2) <= (v+2)/(v+t+2)`.

Averaging under the actual probabilities of the conditioning data proves the bound. No distributional assumption about those data is needed. The last inequality is strictly increasing in f because t>0.

The author's strictness claim also passes: the concrete extension

`A^u, r, s, x, C^t, z, F^v`

is legal and belongs to f=0. Since v>=1, this positive-probability fiber has a strictly smaller uniform upper bound than `(v+2)/(v+t+2)`. Thus the full probability is strictly below that final bound, regardless of whether individual three-chain inequalities can be equalities.

## 3. Good-pair implication and four-ray deduction

The relevant dependency was rechecked in the primary source:
[Zaguia, arXiv:1610.00809v3, Definition 1 and Theorem 2](https://arxiv.org/html/1610.00809).
For the ordered pair `(B2,B4)`, the strict downsets are both `{r}`. Its upper-set difference `U(B4) minus U(B2)` is exactly the remaining tail of C4, hence a chain, including when t=1 and the tail is empty. If `Pr(B2<B4)<=1/2`, the good-pair theorem supplies a balanced pair. If its probability lies in `(1/2,2/3]`, the displayed pair is itself balanced. Consequently a poset with no balanced pair would require the strict inequality `Pr(B2<B4)>2/3`.

The prior independently audited necessary conditions in this specialization are

`u,v>=2`,
`2u<t+v+2`,
`2v<u+t+2`,
`2t<u+v+2`.

They imply exactly the four candidate forms

`(u,v)=(t+1,t+1),(t,t),(t,t−1),(t−1,t)`.

For completeness, u,v<=t+1 follows from combining the first two linear inequalities and integrality. Setting `x=t+1−u` and `y=t+1−v` then gives nonnegative integers with `y<=2x`, `x<=2y`, and `x+y<=3`. Their only solutions are `(0,0),(1,1),(1,2),(2,1)`.

Every candidate therefore has v<=t+1. For t>=3,

`Pr(B2<B4) <= (t+3)/(2t+3) <= 2/3`.

The final comparison is exactly `t>=3`, so its equality boundary at t=3 is included. This contradicts the required strict orientation and excludes every candidate ray point with t>=3.

For t=2, only `(u,v)=(2,2),(3,3)` remain; the mixed ray points have a forbidden unit port. For t=1, only `(u,v)=(2,2)` remains. Independent integer counts give:

- `(u,t,v)=(2,1,2)`: `Z=315`, `N(B1<B0)=202`; the probability `202/315` is balanced.
- `(u,t,v)=(2,2,2)`: `Z=1121`, `N(B2<B4)=667`; the probability `667/1121` is balanced.
- `(u,t,v)=(3,2,3)`: `Z=7626`, `N(B2<B4)=4908`; the probability `818/1271` is balanced.

No remaining positive t case exists. Notice that in the first small case `Pr(B2<B4)=26/35` is not balanced, so using B1,B0 there is genuinely necessary for this particular proof. The author uses the correct witness.

## 4. Independent reproducible arithmetic

Run:

```sh
python audit.py > run.log
sha256sum -c SHA256SUMS.txt
```

Only the Python standard library is needed. `audit.py` does not import any author counting code. Its chain-height oracle first computes the quotient's transitive predecessor sets, then constructs the DAG of actual labelled ideals. Backward counts give total extension counts. A separate forward pass computes a pair numerator by summing prefix-count times suffix-count over edges placing the later label after the earlier one is present. This is neither the author's binomial sum nor its added-comparison-edge DP.

Results in `results.json`:

- All 1,728 vectors with `1<=u,t,v<=12`: the full-probability bound holds by exact integer arithmetic. No equality occurs.
- All 27 vectors with `1<=u,t,v<=3`: explicit enumeration of 73,261 complete extensions, grouped by `(i,f,q,binary base word)`, checks all 8,307 nonempty insertion fibers. Every fiber multiplicity is exactly `binom(a+rank(S_q)−1,a)`, including all empty-A and endpoint-prefix cases.
- 241,669 pointwise coupling comparisons for `1<=k,t<=7`, all q, and all subset/deletion outcomes. Uniformity of the deleted-subset marginal is checked by counting its equally sized preimages.
- 1,568 exact weighted binary-shuffle checks with `1<=k,t<=7`, every q, and `0<=a<=7`.
- All three small-case witness totals and numerators, independently recovered from the ideal DAG.
- 348,550 cone-membership checks for `1<=t<=100`, confirming the four-ray algebra and its closed-boundary exclusion logic.

These finite computations check the implementation and expose possible missing conditioning factors. The infinite theorem rests on the bijection, coupling, monotone reweighting, and exact cone argument above. No sampled computation or asymptotic estimate is used to infer it.

## 5. Freeze boundary

The accepted new claim is the complete three-parameter family exclusion, including the stronger strict probability bound. Prior snapshots that state only a four-ray restriction remain historical records; this audit does not edit or retroactively relabel them. A later research checkpoint should add this theorem as a new result with the prior cone/port filters and Zaguia's theorem listed as dependencies.
