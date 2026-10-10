> S117 publication note: this proof/review text records the completed research run. This lean edition retains proof texts, replay sources and selected small results; large generated ledgers, duplicate source snapshots, historical manifests and checksums are not bundled. For the exact retained/generated distinction, portable commands and prior proof links, use [the S117 guide](../README.zh-CN.md), [reproduction instructions](../REPRODUCE.md) and [dependency map](../DEPENDENCIES.md). Historical statements about material being stored refer to that research run; the package contents are listed in the guide.

# Independent audit: both outer spine weights at most two

Date: 2026-10-10. **Final verdict: PASS for the frozen author theorem, complete finite reduction, and exhaustive exclusion. No correction was required.**

## 1. Exact scope

The quotient has covers 0<3; 1<2,4; 2<3,6; 3<5; 4<5. Each vertex is replaced by a nonempty chain with weights (u,a,b,c,t,d,v). The proposed theorem says that **every such inflation with a,d in {1,2} has a balanced incomparable pair, with all five other positive weights unrestricted**. Balanced means probability in the closed interval [1/3,2/3], under uniform complete linear extensions of the actual labelled poset.

This is an infinite-family theorem assisted by a finite certificate, not extrapolation from an arbitrary box. Universal necessary conditions first bound every hypothetical counterexample. The finite computation excludes the complete bounded necessary region. It does not prove the arbitrary-seven-weight statement, the class a,d<=3, any stronger uniform balance constant, or that a particular endpoint is balanced in every case.

The audit program imports no author implementation. Its independent oracle uses occupancy tuples, whereas the author enumerator uses a split double sum and its companion verifier uses labelled-element bitmasks.

## 2. Structural hypotheses and exact orientations

The external good-pair theorem was checked against [Zaguia, Definition 1 and Theorem 2](https://arxiv.org/html/1610.00809). Its consequence is that an incomparable ordered pair satisfying the lower structural condition must have probability greater than 2/3 if the poset has no balanced pair: probability at most 1/2 invokes the theorem, and the remaining range up to 2/3 is already balanced. Order reversal supplies the upper structural condition.

Here are actual-label checks for all six exact arrows. A superscript + or - denotes a chain with its bottom or top removed.

- B1<B0: both downsets are empty; U(B0) minus U(B1) is C0+.
- T6<T5: both upsets are empty; D(T6) minus D(T5) is C6-.
- T2<T0: U(T0) is contained in U(T2); D(T2) minus D(T0) is the chain C1 followed by C2-.
- B2<B4: both downsets are C1; U(B4) minus U(B2) is C4+.
- B6<B3: D(B6)=C1 union C2 is contained in D(B3); U(B3) minus U(B6) is C3+ followed by C5.
- T4<T3: both upsets are C5; D(T4) minus D(T3) is C4-.

Each displayed pair is incomparable, including singleton-block cases. Thus all six tested orientations really are forced above 2/3. The independent implementation also reconstructs all 18 quotient bottom/top arrows and verifies their full actual-label set conditions in 2,188 weight vectors, including all {1,2,3}^7 and the order-83 extremum. These computations validate the implementation; the displayed set arguments establish the six universal implications.

The port restrictions have a particularly direct proof. With F1=B6, Fv=T6, and x=T3, both F1<x and x<Fv satisfy the appropriate structural condition. For v=1 these are complementary events and cannot both have probability greater than 2/3. Hence v>=2, and reversal gives u>=2.

A failed forced orientation guarantees some balanced pair. It need not make the tested pair itself balanced. The audit and theorem preserve this distinction.

## 3. Independent reconstruction of the infinite-to-finite reduction

The audited general terminal-rank theorem excludes d=1,v>=4 and d=2,v>=10 for arbitrary other weights, and gives the necessary product inequality

3 product_(i=0)^d(c+i) < product_(i=0)^d(c+v+i).

Its order dual gives the corresponding a,u,b facts. The source proof is pinned at f5f62c0bf2e1224926c80f895b954e274bda134dfc025202a77935262f2cdefa and its final independent PASS audit at 95bf3d1c020ce4d566837f4ff3d4ef7cead3c317830bf1ed7db3804b742ee92b. The d=1,v=4 part uses the explicitly retained frozen four-tail certificate. No unaudited extension of the generic atom argument is used.

Thus u<=3 for a=1 and u<=9 for a=2; similarly v<=3 or 9 according to d. Each factor (c+i)/(c+v+i) strictly increases with c and decreases with v. At maximal v the boundary ratios are:

- d=1,v=3: c=3 gives 2/7<1/3; c=4 gives 5/14>1/3.
- d=2,v=9: c=19 gives 19/58<1/3; c=20 gives 308/899>1/3.

Consequently c<=3 or 19 according to d, and b<=3 or 19 according to a. Monotonicity proves the caps for all larger integers; this is not a tested-cutoff assumption.

The established conditional insertion bound gives 2u<a+b+t+v and its dual gives 2v<u+c+t+d. The independently audited middle-shuffle bound gives 2t<b+c+u and 2t<b+c+v. Therefore

t <= floor((b+c+min(u,v)-1)/2) <= 23.

Every hypothetical counterexample is now inside the explicit rectangle a,d in {1,2}, u,v in {2,...,9}, b,c in {1,...,19}, t in {1,...,23}. Its size is 2,125,568. Our audit iterates this whole rectangle and directly applies the terminal caps, both product inequalities, and all four linear inequalities. It does not reuse the author's nested truncated enumeration or symmetry quotient.

The independent set agrees with every author candidate, has no repetitions, is closed under the genuine dual transformation (u,a,b,c,t,d,v) -> (v,d,c,b,t,a,u), and contains exactly 62,109 vectors. The counts by (a,d)=(1,1),(1,2),(2,1),(2,2) are 41,1,609,1,609,58,850. Its maximum order is 83, uniquely attained at (9,2,19,19,23,2,9). The complete rectangle rejection partition is retained in normal/summary.json. The bounds remain valid even though many vectors in the rectangle or prerequisite set already have balanced pairs.

## 4. Independent reconstruction of the four analytic filters

Let qi=Pr(C1_i<B0), with q0=1. For 1<=i<=a, the event is precisely the initial word C1_1,...,C1_i, since before T1 only C0 and C1 are available. Importantly, it is not claimed that every element before B0 belongs to C1 after T1 has appeared.

For 0<=i<a, the gap qi-q(i+1) counts the prescribed prefix C1_1,...,C1_i,B0. Deleting this prefix gives the original total count with u decreased by one and a decreased by i. Prepending a new bottom C1 label injects extensions with the shorter remaining C1 chain into those with the longer chain, so the gaps decrease with i. Since q1>2/3, every gap is below 1/3. Every C1_i is incomparable with B0, so absence of balanced pairs prevents a rank probability from crossing from above 2/3 to below 1/3. Hence Pr(T1<B0)>2/3.

Delete C0 and condition on the complete outside extension. Its insertion window has h<=a+b+t+v elements and starts with all a C1 elements. There are binom(h+u,u) equally likely insertions within this fiber; exactly binom(h-a+u,u) put all C1 before B0. Their ratio increases with h, yielding

Pr(T1<B0) <= binom(b+t+v+u,u)/binom(a+b+t+v+u,u).

Reversal gives precisely Pr(T6<B5), not merely Pr(T6<T5), and the second upper ratio in the certificate. Both upper ratios must exceed 2/3.

For the first lower ratio, let k be the outside-window position of T2. Then k>=a+b, h<=a+b+t+v, and exactly binom(k+u-1,u) of the insertions put T0 before T2. Thus

Pr(T0<T2) >= binom(a+b+u-1,u)/binom(a+b+t+v+u,u).

The forced complement T2<T0 makes this lower bound strictly below 1/3. Reversal gives the B3<B6 lower bound. The two lower tests are valid but redundant after the two rank upper filters in this census.

All four statements are fiberwise bounds averaged with the correct induced outside law. Outside extensions need not have equal multiplicities. No uniform deletion law or uniform seven-vertex quotient law is assumed.

We recomputed all 248,436 candidate-bound numerator/denominator pairs using factorial quotients rather than the author's binomial implementation. The successive analytic survivors are 13,028, 2,285, 2,285, 2,285. There are five equality cases for each lower test in the full prerequisite region, all correctly rejected by those tests; none survives the upper filters. Strictness is handled by exact integer arithmetic throughout.

## 5. Actual-label occupancy oracle and complete reason ledger

An occupancy state q=(q0,...,q6) specifies the initial qi labels already taken from each chain. A legal transition increments qi exactly when that chain is unfinished and every predecessor block is exhausted; the latter need only be checked when starting a chain. These are precisely all reachable labelled ideals. Each complete path selects every actual label in a unique order and corresponds bijectively to one complete labelled linear extension.

The independent program builds layers in increasing total occupancy. Forward counts F(q) count prefix extensions. Reverse-layer counts S(q) count completions. It verifies F(w)=S(0). For a requested event x<y, it sums F(q)S(q+e_i) over transitions appending y when x already belongs to q. Every desired complete extension is counted once at its unique y-transition. The author verifier instead uses bitmasks and transitions appending x when y is absent; neither oracle uses the author's split double sum.

For all 2,285 analytic survivors, our oracle checks all 18 endpoint probabilities and all four actual analytic events. It compares every author denominator and all six published exact numerators, as well as all analytic-bound directions and the full first-rejection ledger. Totals are:

- 11,511,843 reachable occupancy states overall, at most 11,560 for one vector;
- 41,130 endpoint counts;
- 13,710 primary-formula numerator comparisons;
- 9,140 actual analytic-bound checks.

There is no blind enumeration of 2^83 subsets. No vector is sampled or omitted from the analytic-survivor set.

All author ledger entries agree. Applying B1<B0, T6<T5, T2<T0, B2<B4 in that order leaves 2,254, 2,232, 1, 0 vectors. The two further published exact arrows also agree but are unnecessary to conclude exclusion. The first-rejection partition is 49,081 at the first rank bound; 10,743 at the second; 31 at B1<B0; 22 at T6<T5; 2,231 at T2<T0; and 1 at B2<B4. These sum to 62,109. normal/reason_ledger.json records every vector, its exact analytic data, exact count data when applicable, and its first rejection. normal/occupancy_counts.json retains all independently counted endpoint and analytic-event numerators.

The split-formula proof also checks directly: split each extension just after T2, with i C0 labels and j C4 labels on its left. The prefix count is binom(b+j-1,j)binom(a+b+i+j-1,i); the suffix count is the product of the two displayed shuffle factors. Deleting the first B1 or final T5 gives the first two endpoint numerators, including the a=1 and d=1 deletion boundary cases. Restricting i=u counts T0<T2. Requiring the C2/C4 prefix shuffle to start with C2 gives the middle numerator, with H_b(0)=1 and H_1(j)=0 for j>0. The independent actual-label checks validate these formulas throughout the required domain.

## 6. Diagnostic vector and author-verifier comparison

The sole vector surviving the first three exact tests is (3,1,2,2,3,1,3). Its total is 142,680 and its six exact numerators, in certificate order, are 95,536;95,536;105,335;90,360;105,335;90,360. In particular Pr(B2<B4)=753/1189 is balanced.

A separate all-pair occupancy count agrees with all 57 incomparable-pair counts from the author's diagnostic mask DP, with all 13 balanced pairs, and with delta=1700/3567. Its two maximizing pairs are (0,3) versus (4,2), and (4,2) versus (6,1), where the second coordinate is a one-based within-chain rank. Each displayed orientation has numerator 74,680, and its smaller orientation has numerator 68,000. This diagnostic confirms the old short-menu limitation without leaving an unresolved poset.

compare_author.py independently compares all 41,130 author mask-DP endpoint numerators, all 9,140 analytic-event numerators, every reachable-state count, every failed-arrow list, and the special all-pair result against our own output. The full matched diagnostic pair table is included in author_comparison.normal.json.

## 7. Reproducibility and dependency discipline

The programs use Python's standard library and explicit check functions; optimization does not erase validation. The intended replay commands, after frozen source copying, are:

    python audit.py --source source_snapshot/census.json --output normal
    python -O audit.py --source source_snapshot/census.json --output optimized
    python compare_author.py --author source_snapshot/verification.json --independent normal --output author_comparison.normal.json
    python -O compare_author.py --author source_snapshot/verification.json --independent optimized --output author_comparison.optimized.json

Normal and optimized reports, complete reason ledgers, occupancy counts, and author comparisons must agree byte-for-byte. SOURCE_INTEGRITY.json records exact source checksums, equality of frozen source copies, declared dependency identities, and author replay-output consistency. The audit MANIFEST.json identifies precise theorem scope and accepted dependencies; SHA256SUMS freezes all audit artifacts except itself.

The final theorem verdict is issued only after the author package is frozen and the necessary terminal, shuffle, rank-chain, and weighted-count proof dependencies are independently PASS at the source hashes actually used. General terminal Corollary C's separate weighted-spine census dependency is not needed here: this proof uses the general terminal caps/product theorem, then its own complete finite calculation.

## 8. Final source binding and conclusion

All 26 frozen author files, including its checksum list, have identical copies in source_snapshot/. All 11 declared dependency files match their pinned originals, and every required proof review has a final PASS verdict. The principal hashes are:

- Author THEOREM.md: e0c8d1fd018d9bb23e50f5179e31f26dfd441c9bb642aa243120c8bd4932b3d6.
- Author census.py: 7c25a479de26b9b56e3f3c6f05254c5200619dc3b70a9a9c887695651df02eb7.
- Author verify_census.py: 5ccb21c8cddf18828fe102b2321c3f0d69db4dcd564b0f38bda9272682e1eefd.
- Author census.json: 96ba8c3a6d3a687c9ef9d844c5f1db0ee95ad416d132b6ea59308fec8b80e295.
- Author verification.json: 97c1b72c911e67f4c0dd003dc502c0f8da83be4fd2948a76fd0dace6f8ea832e.

Both independent replay modes completed successfully and reproduced the entire summary, 62,109-vector reason ledger, 2,285-vector occupancy ledger, and complete author-verifier comparison byte-for-byte. The source author's published normal/optimized data and logs were also checked to be identical. The latter is an output-consistency check, not a claim that this audit freshly executed the author's companion verifier.

With these dependencies and finite checks frozen, the accepted conclusion is unconditional within its stated class: every positive chain inflation of this seven-core quotient with a,d<=2 has a balanced pair. The remaining five weights are genuinely unrestricted. This conclusion does not rely on the separate all-spines-at-most-three census, and does not settle unbounded a,d.
