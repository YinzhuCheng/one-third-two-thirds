> S117 publication note: this proof/review text records the completed research run. This lean edition retains proof texts, replay sources and selected small results; large generated ledgers, duplicate source snapshots, historical manifests and checksums are not bundled. For the exact retained/generated distinction, portable commands and prior proof links, use [the S117 guide](../README.zh-CN.md), [reproduction instructions](../REPRODUCE.md) and [dependency map](../DEPENDENCIES.md). Historical statements about material being stored refer to that research run; the package contents are listed in the guide.

# Independent audit: complete outer-three exclusion

Date: 2026-10-10. **Final verdict: PASS for the stated finite-computation-assisted theorem and the frozen source identified in SOURCE_INTEGRITY.json. No mathematical correction was required.**

## Accepted result

For the quotient with covers 0<3; 1<2,4; 2<3,6; 3<5; 4<5, replace its vertices by positive chains of lengths (u,a,b,c,t,d,v). Every inflation with a,d in {1,2,3} and max(a,d)=3 has a balanced incomparable pair under the uniform law on actual complete labelled linear extensions. The other five weights are unrestricted in this theorem.

The separate final PASS audit in `../bounded-outer-spine-independent-audit/AUDIT.md` establishes all a,d<=2. Combining the two statements therefore establishes all a,d<=3. The present audit does not import that smaller census to prove its own max(a,d)=3 case. Neither result proves the arbitrary-seven-weight statement.

## 1. Why the infinite-to-finite reduction is valid

Assume there is no balanced pair. The established good-pair consequence forces an incomparable comparison x<y above 2/3 when either D(x) is contained in D(y) with U(y) minus U(x) a chain, or its order-dual condition holds. In particular, for x=T2,y=T0, U(T0) is contained in U(T2) and D(T2) minus D(T0) is C1 followed by C2 with its top removed. This is a chain. Thus P(T2<T0)>2/3, equivalently P(T0<T2)<1/3. This is an actual-label structural condition, not an assertion about a uniform quotient law.

The previously independently PASS terminal-rank theorem supplies u,v>=2; terminal caps V(1)=3,V(2)=9,V(3)=29; and strict product restrictions

3 product_{r=0}^a(b+r) < product_{r=0}^a(b+u+r),
3 product_{r=0}^d(c+r) < product_{r=0}^d(c+v+r).

At fixed outer weight the product ratio increases strictly in the adjacent inner weight and decreases strictly in the terminal weight. At the maximal terminal weights the last allowed/first excluded inner ratios are 2/7 and 5/14; 19/58 and 308/899; 83421/250954 and 3049501/9078630. Hence the adjacent caps M(1)=3,M(2)=19,M(3)=90 follow for every larger integer, not from a sampled cutoff.

The audited insertion and middle-shuffle inequalities give

2u<a+b+t+v, 2v<u+c+t+d,
2t<b+c+u, 2t<b+c+v.

Consequently t<=104 and N<=348. For fixed (u,a,b,c,d,v), these inequalities are exactly the inclusive integer interval

L=max(1,2u-a-b-v+1,2v-u-c-d+1),
H=floor((b+c+min(u,v)-1)/2), L<=t<=H.

The +1 and -1 terms correctly translate strict inequalities; empty intervals are excluded. No symmetry quotient is used. The relaxation attains N=348 at (29,3,90,90,104,3,29).

## 2. Rank filters, monotonicity and complete coverage

The rank-chain prerequisite is genuinely stronger than a single bottom arrow. With qi=P(C1_i<B0), before T1 only C0,C1 are available, so qi equals an initial-prefix probability. The gaps qi-q(i+1) are normalized residual extension counts, nonincreasing in i by prepending a C1 bottom. The initial forced arrow gives the first gap below 1/3; no later gap can cross the whole closed balanced interval. Thus P(T1<B0)>2/3. Deleting C0 and conditioning on the actual induced outside-extension law gives the upper bound

A=binom(b+t+v+u,u)/binom(a+b+t+v+u,u).

The order-dual event is T6<B5, with upper bound D=binom(c+t+u+v,v)/binom(d+c+t+u+v,v). The distinction B5 versus T5 is preserved. The source correctly avoids the false statement that every element before B0 belongs to C1.

Factorial cancellation gives A=product_{r=1}^a(s+r)/(s+u+r), s=b+t+v. Every factor increases strictly in s and the product tends to one. Therefore the necessary strict test 3A>2 has one exact integer threshold. Equality must be rejected and is. The dual filter works identically. The supplemental lower-bound binomial tests are also monotone in t, but remove no vector after the two rank filters and are not logically needed for the exclusion.

`reconstruct_domain.cpp` independently loops the capped rectangle u=2..V(a), v=2..V(d), b,c=1..90 and t=1..104. It applies product restrictions and the original four linear inequalities directly, without using author intervals, threshold tables or count code. The complete rectangular scope comprises 1,132,185,600 tuples; exact product restrictions leave 1,982,272 six-weight combinations before t is tested. The candidate counts are:

- (1,3): 87,160 candidates; 87,160 after the first rank filter; 0 after both.
- (2,3): 2,020,542; 1,715,016; 380.
- (3,1): 87,160; 0; 0.
- (3,2): 2,020,542; 3,537; 380.
- (3,3): 57,570,102; 3,524,719; 65,191.

Total: **61,785,506 candidates, 5,330,432 after the first rank filter, 65,951 after both.** Both additional lower bounds retain all 65,951. The survivor set agrees exactly with the author's full list, including its duals.

The certificate stores all 1,746,956 nonempty t intervals compactly in `interval_certificate.tsv.gz`. A second implementation, `verify_intervals.py`, locates every threshold by exponential bracketing and integer bisection, verifies the integer boundary and every retained interval, and checks that sums of interval lengths equal the independently obtained pointwise counts. Since direct counts cannot exceed the first-to-last span, equality of those sums additionally certifies that no filtered interval contains a missing interior integer. This checks the author's monotone pruning without trusting its implementation. No giant per-candidate prerequisite ledger is needed.

## 3. Independent exact recurrence for every survivor

The author uses a proved binomial double sum split immediately after T2. This audit independently implements integer word recurrences for each side of that split, with no closed binomial counting formula or author counting code.

Let L_a(i,k,j) count a poset consisting of i independent C0 elements and a C1 elements preceding a fork of k C2 and j C4 elements. With k=j=0, L counts shuffles of chains of lengths a,i and is obtained by a two-dimensional Pascal recurrence. Otherwise classify by the final letter:

L_a(i,k,j)=L_a(i-1,k,j)+L_a(i,k-1,j)+L_a(i,k,j-1),

omitting terms with negative coordinates. Let A_a obey the same recurrence with the additional boundary A_a(i,0,j)=0 for j>0. It counts the further restriction first C2 before first C4.

Let F_d(p,q,v) count two chains of lengths p,q, both preceding a terminal chain of length d, together with an independent chain of length v. At p=q=0 its boundary is the ordinary two-chain shuffle recurrence. Otherwise classify by the first letter:

F_d(p,q,v)=F_d(p-1,q,v)+F_d(p,q-1,v)+F_d(p,q,v-1).

For the T2 split, k=b-1, p=u-i+c, q=t-j. Multiplying L_a(i,b-1,j) by F_d(u-i+c,t-j,v) and summing over i,j counts every extension exactly once. The event T0<T2 is exactly i=u. Replacing a by a-1 counts B1<B0 because the only initial possibilities are B0,B1; replacing d by d-1 counts T6<T5 because the only final possibilities are T5,T6. All survivors have a,d>=2, so these replacements retain positive chain lengths. Replacing L by A counts B2<B4, including its correct b=1 boundary.

The full recurrence output agrees with all five author columns at all 65,951 survivors: **329,755 exact integer comparisons**. Full independent records are preserved in `recurrence_counts.txt.gz`; the seven weights are followed by Z,N(B1<B0),N(T6<T5),N(T0<T2),N(B2<B4). This output is sufficient to check each survivor individually. All arithmetic uses GMP integers; no floating-point probability enters any decision.

All 65,951 satisfy the stronger inequality 2N(T0<T2)>Z, and their duals do too. The exact minimum is

4465154496058864828291 / 8852345120096299414144,

uniquely at (9,2,13,19,19,3,7). This is above 1/2 and hence decisively contradicts the necessary P(T0<T2)<1/3. The exact six-arrow cumulative pass counts are 65,951; 65,951; 0; 0; 0; 0. There are no equality exceptions and no unresolved survivors.

## 4. Separate actual-labelled-ideal oracle

To check the combinatorial split rather than merely its arithmetic, `verify_and_ideal.py` constructs actual labelled elements and predecessor bitmasks. Every ideal is represented by its full labelled-element bitmask. A layer recurrence counts all complete extensions. For each requested x<y event, a parallel count forbids the transition inserting y before x; this is exactly the extension count of the augmented order.

The deterministic sample contains 30 vectors: both probability-minimizing orientations, all coordinate extremes, each nonempty outer-spine family, total-order extremes, and a spread across the survivor list, closed under duality. Its maximum order is 348. Across **8,695,806 distinct ideal states**, all **210 total/endpoint comparisons** agree, and all **60 actual-probability versus analytic rank-bound comparisons** pass. The largest case has 661,680 ideals; layer streaming keeps only up to 3,150 ideals at once. Full sample records, exact counts, event labels and state counts are in `verification.json`.

The finite sample validates the independent recurrence implementation. Exhaustive rejection rests on the all-survivor recurrence comparison and the proof of its bijection, not on extrapolation from these 30 checks.

## 5. What this establishes, and the genuine next obstacle

The route succeeds because the unrestricted structural/rank results first turn five unbounded weights into a complete finite necessary region when the two outer spine weights are at most three. The rank-chain filters then remove almost all of that region, and every remaining vector fails a single actual endpoint prerequisite with a substantial gap. The observed >1/2 inequality is only certified over the stated complete finite survivor set; this audit does not promote it to an unrestricted analytic lemma.

At d>=4 the present cap mechanism breaks. Its conditional law is a mixture of Beta(alpha,d+1) distributions, and the maximum last-interior beta-binomial atom tends to (beta/(beta+1))^(beta+1) for beta=d+1. For beta>=5 this exceeds 1/3, already 15625/46656 at beta=5. Thus no eventual terminal cutoff follows from the current uniform interior-atom bound. This is an obstruction to that particular lemma, not a counterexample poset and not evidence that the balanced-pair statement fails. Extending beyond a,d<=3 needs additional endpoint/mixture information or a genuinely different rank certificate; merely enlarging the current numerical box cannot restore completeness.

A failed forced orientation proves some balanced incomparable pair by the structural theorem. It does not identify the tested endpoint pair itself as balanced. No uniform balance constant stronger than 1/3 is established for the whole family.

## 6. Reproduction and source integrity

Run in this directory:

```
g++ -std=c++17 -O2 reconstruct_domain.cpp -lgmpxx -lgmp -o reconstruct_domain
./reconstruct_domain survivors.txt interval_certificate.tsv domain_summary.tsv
python verify_intervals.py
g++ -std=c++17 -O2 recur_endpoints.cpp -lgmpxx -lgmp -o recur_endpoints
./recur_endpoints survivors.txt recurrence_counts.txt
python verify_and_ideal.py --source ../outer-three-census
```

The Python readers also accept the frozen compressed files. Explicit exceptions perform checks; no Python assert or C++ assert controls acceptance. No duplicate normal/optimized author replay was needed. `SOURCE_INTEGRITY.json` pins the final theorem, counting sources and full author records and verifies all 11 declared dependency copies against their originals. The final terminal-rank and rank-chain PASS proofs were reviewed substantively above. No author source was changed, no external write was made, and no additional worker was used.
