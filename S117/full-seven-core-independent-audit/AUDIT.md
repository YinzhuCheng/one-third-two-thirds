> S117 publication note: this proof/review text records the completed research run. This lean edition retains proof texts, replay sources and selected small results; large generated ledgers, duplicate source snapshots, historical manifests and checksums are not bundled. For the exact retained/generated distinction, portable commands and prior proof links, use [the S117 guide](../README.zh-CN.md), [reproduction instructions](../REPRODUCE.md) and [dependency map](../DEPENDENCIES.md). Historical statements about material being stored refer to that research run; the package contents are listed in the guide.

# Independent audit: complete positive-weight seven-core theorem

Date: 2026-10-10. **Final verdict: PASS. No mathematical correction was required.**

Reviewed source: `../full-seven-core-resolution/THEOREM.md`, its complete interval and integer-count records, and the proof dependencies identified below. This audit supplies one independently implemented replay, not another archive or repeated hash collection.

## 1. Accepted theorem and scope

Let Q have covers

`0<3; 1<2,4; 2<3,6; 3<5; 4<5`.

Replace each quotient vertex i by a nonempty chain C_i of length

`(u,a,b,c,t,d,v)=(|C0|,|C1|,|C2|,|C3|,|C4|,|C5|,|C6|)`.

**Every such inflation, with all seven positive integer lengths unrestricted, has a balanced incomparable pair under the uniform law on its actual complete labelled linear extensions.** Balanced means probability in the closed interval [1/3,2/3].

The proof is finite-computation-assisted: unrestricted probability inequalities imply a complete finite necessary domain, and exact enumeration excludes it. It does not extrapolate from an arbitrary weight box. The result concerns this fixed quotient and all its chain inflations; it does not prove the unrestricted 1/3–2/3 conjecture or make a statement about every seven-vertex quotient.

## 2. Prerequisites, strict orientation, and genuine duality

The dependency chain is complete and noncircular:

- `general-terminal-rank-independent-audit/AUDIT.md`: unrestricted actual-law beta-mixture/product bounds, u,v>=2, and V(1)=3,V(2)=9,V(3)=29.
- `generalized-seven-core-shuffle-independent-audit/AUDIT.md`: strict middle-shuffle and port inequalities.
- Its `RANK_AND_INNER_SINGLETON_AUDIT.md`: the forced whole-chain comparisons T1<B0 and T6<B5 and their insertion upper bounds. B5 is essential in the second event.
- `fourth-terminal-rank-independent-audit/AUDIT.md`: V(4)=43, with all remaining weights arbitrary. Its adjacent-tail concavity proof depends on the prior mixture law, not the global bound or final census.
- `global-seven-weight-independent-audit/AUDIT.md`: all-k gamma estimates and a complete global finite reduction, final PASS.
- `bounded-outer-spine-independent-audit/AUDIT.md` and `outer-three-independent-audit/AUDIT.md`: the complete a,d<=2 and a,d<=3,max(a,d)=3 classes, respectively, both final PASS.

Paths for earlier research inputs are resolved in the S117 dependency map. The earlier audits' scopes and substantive arguments were read; no ancillary d5 fiber calculation or unproved general atom cutoff is imported.

The structural implication agrees with [Zaguia, Definition 1 and Theorem 2](https://arxiv.org/html/1610.00809), checked against the primary source: a qualifying incomparable comparison must exceed 2/3 if there is no balanced pair. Its dual version applies to (T2,T0), because U(T0) is contained in U(T2), and D(T2) minus D(T0) is the chain C1 followed by C2 with T2 deleted. Thus a hypothetical counterexample necessarily satisfies

`Pr(T0<T2)<1/3`.                                                    (A)

The strict sign is correct: equality at either balanced endpoint is already disallowed by the counterexample hypothesis.

The permutation `(0 6)(1 5)(2 3)`, fixing 4, reverses the quotient covers and within-chain order. Reversing a complete extension therefore bijects the actual extension sets at

`(u,a,b,c,t,d,v)` and `(v,d,c,b,t,a,u)`.

Consequently it is legitimate to choose a<=d. This is a bijection between possibly different weighted posets, not an assumed automorphism of one vector. All port and inner orientations are retained when a=d. Under this reversal, the transformed T0<T2 event becomes original B3<B6, a distinction also checked by the actual-label oracle.

## 3. Why every remaining case is actually enumerated

Write `m=min(u,v)`, `S=a+d`, `P=u+v`. The audited necessary conditions are

`3 product_{i=0}^a(b+i) < product_{i=0}^a(b+u+i)`,

its (d,c,v) dual, the two strict rank products

`3 product_{r=1}^a(b+t+v+r) > 2 product_{r=1}^a(b+t+v+u+r)`,

its (d,c,u,v) dual, and

`2u<a+b+t+v; 2v<u+c+t+d; 2t<b+c+m`.

The product/rank comparison gives the genuine unbounded inequality

`gamma_a u+gamma_d v<m+S`,

where `gamma_k=1/((3/2)^(1/k)-1)-2/(3^(1/(k+1))-1)-1`.

The globally proved estimates are `gamma_k>16k/25-12/5` for every k>=1, `gamma_k>11/50` for k>=4, and `gamma_k>87/100` for k>=5. Their proof uses rational logarithm enclosures and strict elementary exponential inequalities, not a finite sample of k values.

For completeness, the case partition is:

1. If a=1,2,3, its port u is at most 3,9,29. The gamma inequality with m<=u gives `(16d-60)v<25d+25a+(85-16a)u` for d>=5. Using v>=2 bounds d by 50,92,181 respectively. For d<=4 its port v is capped by V(d).
2. If a=4<=d, the positive gamma coefficients give d<=36. The fourth-rank cap gives u<=43; v<=43 at d=4, and the same strict rational mixed bound applies at d>=5.
3. If 5<=a<=d, the positive coefficients after subtracting P/2 give `7S<290`, hence S<=41. Also `(37/100)P<S`, hence P<=110.

These branches exhaust all positive a<=d. In every branch,

`16(au+dv)<60(u+v)+25min(u,v)+25(a+d)`                      (B)

is necessary. The branchwise port bounds imply P<=110. The already audited global derivation gives N<=1665, although the final enumeration retains the stronger coupled inequalities instead of testing the enormous Cartesian box.

For fixed a,u, each factor `(b+i)/(b+u+i)` increases strictly with b. Thus the allowed b values are an initial positive integer interval; `b<(a+1)u` supplies an excluded finite upper bracket. The same applies to c. Each rank-product factor increases strictly with its argument s, so the exact passing s values likewise form a terminal integer interval. Translating the original strict linear inequalities gives precisely

`low=max(1,2u-a-b-v+1,2v-u-c-d+1,R(a,u)-b-v,R(d,v)-c-u)`,

`high=floor((b+c+min(u,v)-1)/2)`.

Every integer t between these endpoints passes the indicated conditions; no equality boundary or interior hole is suppressed. The +1 and -1 terms are necessary and correct.

My independent checker starts from the broad global a,d<=181,S<=184,P<=110 region, explicitly checks each branch cap and (B), and finds inner maxima by a forward scan. It then tests the original strict rank products directly. It uses neither the author's rank-threshold table nor its algebraic c-min formula: it locates the first possible c and t by monotonicity of the original conditions within the shuffle upper endpoint, and verifies the last failing/first passing t boundary. The full resulting interval set matches the author's, and its expansion matches the exact-count vectors with no duplicate.

The independently reproduced partition is:

- 14,190 total canonical port tuples;
- 1,148 already covered by a,d<=3;
- 12,856 new port tuples with no possible b,c,t interval;
- 186 new port tuples with 2,169 nonempty intervals;
- 6,088 new seven-weight vectors, maximum order 631.

The six surviving outer pairs and numbers of vectors are `(2,4):47`, `(2,5):6`, `(2,6):1`, `(3,4):4494`, `(3,5):106`, `(4,4):1434`. Every other permitted outer pair has zero intervals. In particular, the mixed class a<=3<d is present, not accidentally covered by an inapplicable previous theorem.

## 4. Independent recurrence for all 6,088 counts

The author uses a binomial double sum. This audit recomputes every denominator and numerator with integer word recurrences that use no closed binomial formula.

Let `L_a(i,k,j)` count extensions of an independent i-chain together with an a-chain preceding both a k-chain and a j-chain. At k=j=0 its values count two-chain shuffles, computed by a two-dimensional Pascal recurrence. Otherwise the last element belongs to one of the three terminal chains, giving

`L_a(i,k,j)=L_a(i-1,k,j)+L_a(i,k-1,j)+L_a(i,k,j-1)`,

with nonexistent terms omitted. This recurrence is valid when k=0 or j=0; only the k=j=0 base requires the independent a-chain boundary.

Let `F_d(p,q,r)` count a p-chain and a q-chain that both precede a d-chain, together with an independent r-chain. At p=q=0 its values are two-chain shuffle counts, again by Pascal recurrence. Otherwise the first element is from a still nonempty p-, q-, or r-chain, so

`F_d(p,q,r)=F_d(p-1,q,r)+F_d(p,q-1,r)+F_d(p,q,r-1)`.

Split an actual extension immediately after T2. If i C0 elements and j C4 elements precede that split, deleting final T2 leaves the prefix counted by `L_a(i,b-1,j)`. The suffix has the remaining C0 followed by all C3 as a single chain, the remaining C4 as another, C5 above both, and the independent C6. Its count is `F_d(u-i+c,t-j,v)`. The split is unique and reversible. Therefore

`Z=sum_{i=0}^u sum_{j=0}^t L_a(i,b-1,j) F_d(u-i+c,t-j,v)`,

while `N02` is the same sum restricted to i=u. This proves the actual-law interpretation independently of the author's binomial arithmetic.

All **12,176 exact integer comparisons** agree across the **6,088 vectors**. Every vector satisfies `2*N02>Z`, so in particular `3*N02>Z`, contradicting (A). No rounding or floating-point probability is used.

The exact minimum is

`21095146905395260272614 / 36016977281285366345651`,

at `(9,2,16,18,19,4,5)`. It exceeds 1/2. The comparison is only claimed over the complete finite residual domain; it is not promoted to an unrestricted endpoint inequality.

## 5. Separate actual-label and dual checks

A second oracle builds the actual labelled poset's transitive predecessor bitmask for every element. It visits only reachable ideal masks, layer by layer. Every legal transition inserts the next actual chain label whose predecessors are already present. Thus each complete path is exactly one actual labelled linear extension.

Alongside total counts, two constrained counts suppress transitions inserting T2 before T0 or B6 before B3, respectively. These are exactly the numerators for T0<T2 and B3<B6, without any split formula. The deterministic sample contains the minimum-probability vector, a shortest vector from every nonempty outer pair, the maximum-order vector, and all their duals: **15 vectors**.

All checks agree, across **3,774,024 reachable ideal states**. The maximum-order vector `(43,4,172,172,193,4,43)` has **3,312,320 reachable ideals** and a maximum layer of **8,536**, rather than a blind scan of 2^631 subsets. Its denominator and both endpoint counts agree exactly with the recurrence; the two numerators are equal as required by its self-duality. Every a=d=4 census vector also has its reversed vector present with equal denominator.

These selected actual-label checks validate the recurrence implementation and event/duality interpretation. Exhaustive exclusion rests on the proved recurrence plus all-vector replay, not on extrapolation from the sample.

## 6. Composition and reproduction

Every positive-weight vector is accounted for: genuine reversal reduces to a<=d; the two independently PASS previous censuses settle all a,d<=3; the global bound and complementary census cover every remaining case; each of its 6,088 residuals violates the necessary endpoint orientation. All prerequisites are now final PASS, so no conditional audit gate remains.

The tested endpoint need not itself be balanced. The contradiction to a forced orientation proves that some balanced incomparable pair exists by the structural theorem. No stronger universal balance constant or global conjecture is claimed.

Run the single independent check:

`python ../full-seven-core-independent-audit/check.py`

It compiles `recurrence.cpp` with the available system C++ compiler and GMP library, reconstructs the full domain, recomputes all counts, and performs the 15 actual-label checks. It imports no author implementation. Checks use explicit exceptions, not assertions removed by optimization. The completed run is in `run.log`; `results.json`, `independent_intervals.txt`, and `recurrence_counts.txt` contain the reproducible results. No remote writes or additional subagents were used.
