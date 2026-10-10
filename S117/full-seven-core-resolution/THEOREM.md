> S117 publication note: this proof/review text records the completed research run. This lean edition retains proof texts, replay sources and selected small results; large generated ledgers, duplicate source snapshots, historical manifests and checksums are not bundled. For the exact retained/generated distinction, portable commands and prior proof links, use [the S117 guide](../README.zh-CN.md), [reproduction instructions](../REPRODUCE.md) and [dependency map](../DEPENDENCIES.md). Historical statements about material being stored refer to that research run; the package contents are listed in the guide.

# Every positive chain inflation of the seven-core has a balanced pair

Date: 2026-10-10.

**Status: complete, independently audited PASS.** The fourth-terminal-rank theorem, global finite reduction, both previous small-outer censuses, and the full complementary-domain proof all have final independent PASS audits. This is a finite-computation-assisted theorem for all seven positive weights.

## 1. Statement

Let Q be the seven-vertex poset with covers

0<3; 1<2,4; 2<3,6; 3<5; 4<5.

Replace each vertex i by a nonempty chain C_i, inheriting all quotient comparisons. Write the positive chain lengths as

(u,a,b,c,t,d,v)=(|C0|,|C1|,|C2|,|C3|,|C4|,|C5|,|C6|).

**Theorem. Every such inflated poset has an incomparable pair x,y satisfying 1/3 <= Pr(x<y) <= 2/3, under the uniform law on its actual complete linear extensions.**

The weights are arbitrary positive integers. The proof uses no experimentally chosen cutoff. It first proves that every hypothetical counterexample lies in an explicit finite region, then exhausts that entire region exactly. No probability is taken under a uniform quotient-extension or uniform deletion law.

## 2. Structural and probability prerequisites

Let B_i,T_i be the bottom and top of C_i. The good-pair consequence says that in a poset with no balanced pair, an incomparable ordered pair (x,y) has Pr(x<y)>2/3 whenever either

- D(x) is contained in D(y), and U(y) minus U(x) is a chain; or
- U(y) is contained in U(x), and D(x) minus D(y) is a chain.

This is the previously audited application of Zaguia's good-pair theorem. In particular (x,y)=(T2,T0) satisfies the second condition: U(T0) is contained in U(T2), while D(T2) minus D(T0) is C1 followed by C2 without T2. Therefore every counterexample must have

Pr(T0<T2)<1/3.                                                     (1)

The prior insertion, terminal-rank, rank-chain and middle-shuffle proofs give the following necessary conditions. Set m=min(u,v).

u,v>=2,

3 product_(i=0)^a(b+i) < product_(i=0)^a(b+u+i),
3 product_(i=0)^d(c+i) < product_(i=0)^d(c+v+i),                     (2)

2u<a+b+t+v, 2v<u+c+t+d, 2t<b+c+m,                                (3)

3 product_(r=1)^a(b+t+v+r) > 2 product_(r=1)^a(b+t+v+u+r),
3 product_(r=1)^d(c+t+u+r) > 2 product_(r=1)^d(c+t+u+v+r).          (4)

The last two products express upper bounds on the forced probabilities Pr(T1<B0)>2/3 and Pr(T6<B5)>2/3. The second event uses B5, not T5. Conditioning on an outside extension induces a nonuniform outside law, but insertion is uniform within its fiber; that is the probability law used in deriving these bounds.

For k=1,2,3,4 define

V(k)=3,9,29,43 respectively.

The terminal-rank theorems give

a<=4 => u<=V(a), d<=4 => v<=V(d).                                 (5)

For k<=3 these were established previously. The new k=4 argument is a joint tail tradeoff: the actual conditional distribution is a positive mixture of Beta(alpha,5) laws. If Q is the last rank mass and P the preceding mass, then Jensen's inequality applied to the explicitly concave function

f_n(q)=5q(1-q^(1/5)) / [1-3(1-q^(1/5))/n]

gives P<=f_n(Q). At n>=44, q+f_n(q) is strictly increasing and its value at q=1/3 is below 2/3 because

(5n+3)^5 > 3(4n+3)^5.

At n=44+w the difference has positive coefficients

175086646,226795165,19429030,642530,9515,53.

The counterexample requirements Q<1/3 and P+Q>2/3 contradict this tradeoff. This is an unrestricted theorem about all remaining weights, not a sampled check. The full derivation and actual-law mixture justification are in the fourth-terminal-rank proof cited in Section 7.

Order reversal is the genuine full-extension bijection

(u,a,b,c,t,d,v) -> (v,d,c,b,t,a,u).                                (6)

It suffices to consider a<=d. When a=d, this proof retains both port orientations rather than making an additional symmetry identification.

## 3. Why the complete domain is finite

Let A=log(3/2), L=log3, and define

alpha_k=1/(exp(A/k)-1),
beta_k=1/(exp(L/(k+1))-1),
gamma_k=alpha_k-2 beta_k-1.

From (2), b<beta_a u and c<beta_d v. From (4), b+t+v+a>alpha_a u and c+t+u+d>alpha_d v. Adding and using (3) yields the strict necessary inequality

gamma_a u+gamma_d v < min(u,v)+a+d.                               (7)

The elementary estimates

1/x-1/2 < 1/(exp(x)-1) < 1/x-1/2+x/12

and rigorously bounded logarithms give, uniformly for all positive k,

gamma_k>16k/25-12/5;
gamma_k>11/50 for k>=4;
gamma_k>87/100 for k>=5.                                          (8)

These are analytic all-integer bounds. Their proofs and exact rational verification are in the global-bound note; finite sampling is not used to extend them to arbitrary k.

Write S=a+d and P=u+v. The deductions from (7)--(8), together with (5), are:

- If a,d>=5, then S<=41 and P<=110.
- If a<=3, then d<=50,92,181 for a=1,2,3 respectively.
- If a=4<=d, then d<=36.
- If a<=4 and d>=5, then the sharper integer inequality holds:

  (16d-60)v < 25d+25a+(85-16a)u.                                 (9)

Together these imply a,d<=181, S<=184 and P<=110. Moreover, writing W=au+dv and B=b+c, (7)--(8) give

16W <60P+25min(u,v)+25S,
B<W+P,
t<(B+min(u,v))/2,

hence every hypothetical counterexample has total order

N=u+a+b+c+t+d+v<=1665.                                            (10)

The proof below does not enumerate arbitrary posets or the 1665-sized Cartesian weight box. It retains the coupled inequalities.

The following complete port domain is enumerated, always with a<=d:

1. a=1,2,3; a<=d<=50,92,181 respectively; 2<=u<=V(a). For d<=4, 2<=v<=V(d). For d>=5, use (9).
2. a=4; 4<=d<=36; 2<=u<=43. For d=4, 2<=v<=43. For d>=5, use (9).
3. 5<=a<=d, a+d<=41; u,v>=2, u+v<=110.

Every tuple is filtered by the exact necessary rational-line consequence

16(au+dv)<60(u+v)+25min(u,v)+25(a+d).                              (11)

There are exactly 14,190 port tuples in this explicitly proved domain. A looser bounding rectangle can have more; no particular intermediate count is assumed as a mathematical premise.

## 4. Exact elimination of the new complementary domain

The already completed censuses cover a,d<=2 and max(a,d)=3 with a,d<=3. Of the 14,190 port tuples, 1,148 belong to these covered classes. The present certificate handles every remaining tuple, including the mixed cases a<=3<d.

For fixed a,u, let M(a,u) be the largest positive integer b satisfying (2), or zero if none does. The product ratio increases strictly with b, and b<(a+1)u supplies a rigorous binary-search bracket. Thus the exact allowed range is 1<=b<=M(a,u). Similarly 1<=c<=M(d,v).

Let R(a,u) be the least nonnegative integer s such that

3 product_(r=1)^a(s+r)>2 product_(r=1)^a(s+u+r).

The ratio increases strictly to one. Thus R exists, and every exact admissible t interval is

low=max(1,2u-a-b-v+1,2v-u-c-d+1,R(a,u)-b-v,R(d,v)-c-u),
high=floor((b+c+min(u,v)-1)/2),
low<=t<=high.                                                     (12)

Nothing inside a nonempty interval is omitted. Equality in a necessary strict probability condition is rejected, as required for the closed balanced interval.

The exact enumeration gives:

| Outer weights (a,d) | Nonempty port tuples | Compressed intervals | Weight vectors |
|---|---:|---:|---:|
| (2,4) | 10 | 29 | 47 |
| (2,5) | 4 | 6 | 6 |
| (2,6) | 1 | 1 | 1 |
| (3,4) | 87 | 1,449 | 4,494 |
| (3,5) | 18 | 67 | 106 |
| (4,4) | 66 | 617 | 1,434 |
| Total | 186 | 2,169 | 6,088 |

All other outer pairs in the complete domain have zero intervals. Of the 13,042 new port tuples, 12,856 have no allowed inner/shuffle interval. The largest surviving total order is 631, attained at (43,4,172,172,193,4,43); this is a derived residual maximum, not an input cutoff.

The entire ledger is the 2,169-row text file `domain_intervals.txt`. A row

u a b c d v low high

represents precisely the consecutive weights (u,a,b,c,t,d,v) with low<=t<=high. `domain_summary.json` also records every tested outer pair, including the zero rows, and its port/interval counts.

## 5. Counting the actual extensions and rejecting every residual

Split an actual complete extension immediately after T2. Let i and j be the numbers of C0 and C4 elements in its prefix. Put

F(i,j)=binom(b+j-1,j) binom(a+b+i+j-1,i),
G(i,j)=binom(u-i+c+t-j,t-j) binom(u-i+c+t-j+d+v,v).

The exact denominator and event numerator are

Z=sum_(i=0)^u sum_(j=0)^t F(i,j)G(i,j),
N02=sum_(j=0)^t F(u,j)G(u,j).                                    (13)

For the prefix: after deleting its i C0 elements and final T2, it is all of C1 followed by a shuffle of b-1 elements of C2 with j elements of C4. Reinserting C0 gives F. For the suffix: the remaining C0 followed by C3 is a chain, shuffled with the remaining C4; C5 follows, while C6 shuffles freely into this entire suffix. This gives G. The decomposition is bijective, and T0<T2 is exactly i=u. Hence Pr(T0<T2)=N02/Z under the original full-extension law.

For every one of the 6,088 residuals, exact integers satisfy the stronger rejection

2 N02 > Z.                                                       (14)

The minimum probability over this entire new domain is

21095146905395260272614 / 36016977281285366345651,

attained uniquely at (9,2,16,18,19,4,5). No floating-point comparison is used. Equation (14) contradicts (1), so every new residual is excluded.

The endpoint T0,T2 need not itself be balanced when its forced orientation fails. The good-pair consequence supplies the existence of a balanced pair. This argument does not assume that an arbitrary endpoint menu always contains a balanced pair.

## 6. Complete coverage and method

The classes partition the entire positive-weight family after (6):

- a,d<=2: the previous exact census eliminates all 62,109 prerequisites, leaving 2,285 rank-filter survivors and then zero after four exact forced-arrow tests. Its actual-label DP independently checks all 2,285 survivors.
- a,d<=3 with max(a,d)=3: the previous exact census eliminates all 61,785,506 prerequisites, leaving 65,951 rank-filter survivors and then zero using (1). Those reported counts include both dual orientations.
- max(a,d)>=4: the global bound and this complementary census leave 6,088 residuals with a<=d, every one excluded by (14).

There is no uncovered mixed class and no remaining candidate. Reversal restores the a>d half. The final independent audits of every prerequisite and this composition are PASS, so this proves the theorem for all seven positive lengths.

The reusable idea is a sequence of different reductions, each with a separate role:

1. Structural good-pair consequences turn absence of balance into strict orientations.
2. Rank propagation strengthens endpoint orientations into whole-chain inequalities.
3. A concave adjacent-tail tradeoff survives arbitrary actual-law mixtures and closes the formerly unbounded fourth-rank corner.
4. Product/rank/shuffle tension gives a global finite region with coupled bounds.
5. Monotone thresholds compress that complete region to a short exact interval ledger.
6. A bijective complete-extension count rejects every remaining vector.

The numerical work closes a proved finite domain; it is not the reason the domain is finite. This theorem is specific to this seven-core chain-inflation class and does not settle the unrestricted 1/3--2/3 conjecture.

## 7. Reproduction, prerequisites and audit status

The proof sources are:

- `../bounded-outer-spine-census/THEOREM.md` and its existing independent audit;
- `../outer-three-census/THEOREM.md` and its existing independent audit;
- `../fourth-terminal-rank-barrier/FOURTH_RANK_TRADEOFF.md`, independently PASS in `../fourth-terminal-rank-independent-audit/AUDIT.md`;
- `../global-seven-weight-reduction/GLOBAL_WEIGHT_BOUND.md`, independently PASS in `../global-seven-weight-independent-audit/AUDIT.md`;
- the frozen structural, rank-chain, terminal-rank, shuffle and weighted-count proofs listed in the earlier censuses' dependency manifests.

The proof dependency flow has no census circularity. Structural, terminal-mixture, rank-chain and shuffle lemmas imply the fourth-rank theorem and the gamma reduction; these analytic results prove global finiteness without using either earlier census. The old censuses separately use the same analytic prerequisites to settle their small-outer classes. The present census uses the already proved global finite domain. Only the final union uses all three disjoint census results.

One practical reproduction entry point is:

`python reproduce.py`

It needs Python 3, a C++ compiler named g++, and the installed GMP development libraries. It regenerates the new ledger, counts every residual, independently regenerates its domain, and cross-checks every exact integer. It uses no network, installs nothing, removes temporary binaries on exit, and does not rerun the already accepted old large searches. After `reproduce.py` has generated the count rows and the second ledger, `python verify_resolution.py` checks those files without recompiling. The lean S117 edition does not bundle `exact_counts.txt` or `independent_intervals.txt`.

The author generator uses exact product binary search, monotone rank thresholds and algebraic lower bounds on c. The independent domain replay instead uses a broad global rectangle, direct product checks, no c pruning, and a direct scan of t against the original rank products. Their full interval lists agree.

The C++ counter uses GMP integer binomial recursion. The Python verifier imports no author implementation, constructs binomial coefficients by factorial quotients, reverses the summation order, checks every stored denominator/numerator, rechecks the original prerequisites, and requires 2*N02>Z in all cases. Its explicit exceptions remain active under python -O.

The generated `exact_counts.txt` is a reproducible convenience, with rows u a b c t d v Z N02; it is not a trusted input because the verifier recomputes every count. No hash collection or archive layer is needed to understand or run this certificate. The final independent audit is PASS in `../full-seven-core-independent-audit/AUDIT.md`. It reconstructs the complete domain independently and recomputes all 12,176 integers using word recurrences with no closed binomial formulas. It separately checks 15 actual-labelled ideal DPs, including the maximum-order vector and all selected duals, across 3,774,024 reachable ideals. The N=631 maximum case has 3,312,320 ideals and maximum layer size 8,536, avoiding any blind 2^631 subset scan. All denominators, endpoint events and dual correspondences agree. These sample DPs validate implementation and interpretation; the exhaustive exclusion comes from the proved recurrence and all-vector replay.

The optional independently authored reproduction entry point is `python ../full-seven-core-independent-audit/check.py`. It is not necessary to run both replay implementations routinely.
