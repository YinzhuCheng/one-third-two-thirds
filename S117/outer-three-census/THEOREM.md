> S117 publication note: this proof/review text records the completed research run. This lean edition retains proof texts, replay sources and selected small results; large generated ledgers, duplicate source snapshots, historical manifests and checksums are not bundled. For the exact retained/generated distinction, portable commands and prior proof links, use [the S117 guide](../README.zh-CN.md), [reproduction instructions](../REPRODUCE.md) and [dependency map](../DEPENDENCIES.md). Historical statements about material being stored refer to that research run; the package contents are listed in the guide.

# Exact exclusion of the outer-three seven-core class

Date: 2026-10-10. Status: complete finite-computation-assisted author proof; a new independent audit of this census is separate. All unrestricted prerequisites used below have previously frozen independent PASS audits in `dependencies/`. The remaining all-weight seven-core problem is not claimed solved.

## 1. Statement and scope

Let Q have covers 0<3; 1<2,4; 2<3,6; 3<5; 4<5. Replace vertex i by a nonempty chain C_i, inheriting all quotient comparisons, and write

(u,a,b,c,t,d,v)=(|C0|,|C1|,|C2|,|C3|,|C4|,|C5|,|C6|).

**Theorem.** If a,d belong to {1,2,3} and at least one of a,d equals 3, then the inflated poset has a balanced incomparable pair under the uniform law on its actual complete linear extensions.

Here balanced means probability in the closed interval [1/3,2/3]. The five weights u,b,c,t,v are unrestricted positive integers in the theorem statement. This file does not repeat or rely on the separate finite census for a,d<=2. Joining that separately proved class to this theorem gives the full a,d<=3 result.

The method is a mathematically proved finite reduction followed by an exact integer rejection certificate. The finite experiment is not used to extrapolate any unrestricted inequality.

## 2. Audited unrestricted prerequisites

Write B_i,T_i for the first and last elements of C_i. Suppose, for contradiction, that there is no balanced pair. The audited good-pair consequence forces an incomparable ordered pair (x,y) to have Pr(x<y)>2/3 whenever either

- D(x) is contained in D(y), and U(y) minus U(x) is a chain; or
- U(y) is contained in U(x), and D(x) minus D(y) is a chain.

This is the established consequence of Zaguia's good-pair theorem, Definition 1 and Theorem 2, https://arxiv.org/html/1610.00809 . In particular, the actual inflated pair (T2,T0) satisfies the second condition: U(T0) is contained in U(T2), and D(T2) minus D(T0) consists of C1 followed by C2 without T2, a chain. Therefore

Pr(T0<T2)<1/3.                                                   (1)

The general terminal-rank theorem and its dual give, with

V(1)=3, V(2)=9, V(3)=29,

2<=u<=V(a), 2<=v<=V(d),
3 product_{i=0}^a(b+i) < product_{i=0}^a(b+u+i),
3 product_{i=0}^d(c+i) < product_{i=0}^d(c+v+i).                    (2)

The endpoint insertion and generalized middle-shuffle results give

2u<a+b+t+v,  2v<u+c+t+d,
2t<b+c+u,   2t<b+c+v.                                           (3)

Finally the rank-chain consequence requires

Pr(T1<B0)>2/3,  Pr(T6<B5)>2/3,

and bounds these probabilities above by

A=binom(b+t+v+u,u)/binom(a+b+t+v+u,u),
D=binom(c+t+u+v,v)/binom(d+c+t+u+v,v),                            (4)

respectively. Hence both A and D must be strictly above 2/3. The event in the second rank bound is T6<B5, not merely T6<T5.

For clarity, the first rank-chain prerequisite follows by considering q_i=Pr(C1_i<B0), q_0=1. Before T1 the only available blocks are C0,C1, so q_i is the probability of the forced initial C1 prefix. Deleting that prefix followed by B0 identifies q_i-q_(i+1) with a residual extension count divided by the original count. Prepending a new first C1 element shows these gaps are nonincreasing. The good-pair condition gives q_1>2/3 and first gap <1/3. No later rank may jump from above 2/3 to below 1/3 without a balanced pair, so q_a>2/3. Conditional insertion of C0 into an outside extension whose window has h<=a+b+t+v elements gives ratio binom(h-a+u,u)/binom(h+u,u), increasing with h, and proves the first bound (4). Complete-extension reversal proves its dual. This uses the induced outside law, not a uniform deletion law.

All these results are identified, copied, and hashed in `dependencies/MANIFEST.json`, including the rank-chain independent audit, general terminal-rank independent audit, weighted-count independent audit, and generalized-shuffle independent audit. The new theorem's logical computation only needs (1)--(4); the two additional binomial lower-bound filters recorded in the data remove no additional candidates.

## 3. Complete finite domain

For fixed positive d,v, the ratio product_{i=0}^d (c+i)/(c+v+i) increases strictly with c and decreases with v. At the largest allowed v, the first disallowed c values are

(d,v,c)=(1,3,4), (2,9,20), (3,29,91).

In all three cases 3 product(c..c+d) >= product(c+v..c+v+d), contradicting (2). Thus

M(1)=3, M(2)=19, M(3)=90,

and b<=M(a), c<=M(d). The duality used here is the actual complete-extension reversal

(u,a,b,c,t,d,v) -> (v,d,c,b,t,a,u).

By (3) and integrality,

1<=t<=floor((b+c+min(u,v)-1)/2)<=104.

It follows that every hypothetical counterexample in the theorem lies in the finite rectangle with u,v<=29, b,c<=90, t<=104 and total order at most 348. The maximum is attainable in the prerequisite relaxation, at (29,3,90,90,104,3,29).

For each a,d with max(a,d)=3, `explore.py` first enumerates every allowed (u,b),(v,c) satisfying the caps and exact strict product conditions (2). For each such pair combination, (3) is equivalent to the integer interval

L=max(1,2u-a-b-v+1,2v-u-c-d+1),
H=floor((b+c+min(u,v)-1)/2),
L<=t<=H.                                                        (5)

Empty intervals contribute nothing. This is exact, not an upper-envelope approximation. Every candidate is counted once, with no symmetry quotient.

To apply (4) efficiently, let S(a,u) be the least nonnegative integer s such that

3 product_{r=1}^a(s+r) > 2 product_{r=1}^a(s+u+r).

Each factor (s+r)/(s+u+r) strictly increases with s, and their product tends to one; the threshold exists. Cancelling factorials shows the first ratio A equals this product with s=b+t+v. Its strict test therefore just replaces L by max(L,S(a,u)-b-v); the dual similarly replaces L by max(L,S(d,v)-c-u). These are exact integer thresholds with equality rejected.

The alternative `verify_domain.cpp` imports no enumeration code and uses a rectangular loop u,v=2..29, b,c=1..90, t=1..104. It checks port caps, both original product inequalities, all four original linear inequalities, and both short-product versions of (4) directly. It does not use (5), the threshold table, or inner-cap specialization. Its complete candidate counts and residual sets agree with the Python interval enumeration.

The exhaustive counts are:

| (a,d) | Candidates after (2)--(3) | After first bound (4) | After both bounds (4) | Maximum order |
|---|---:|---:|---:|---:|
| (1,3) | 87,160 | 87,160 | 0 | 176 |
| (2,3) | 2,020,542 | 1,715,016 | 380 | 210 |
| (3,1) | 87,160 | 0 | 0 | 176 |
| (3,2) | 2,020,542 | 3,537 | 380 | 210 |
| (3,3) | 57,570,102 | 3,524,719 | 65,191 | 348 |
| Total | 61,785,506 | 5,330,432 | 65,951 | 348 |

The machine-readable domain summary and the full ordered residual vector list are included. The two safe lower-bound conditions from `WEIGHTED_COUNT_FORMULAS.md` hold for every one of the 65,951 residuals and are redundant here.

## 4. Exact count and rejection

For 0<=i<=u and 0<=j<=t, set

F(i,j)=binom(b+j-1,j) binom(a+b+i+j-1,i),
G(i,j)=binom(u-i+c+t-j,t-j) binom(u-i+c+t-j+d+v,v).

Then the exact complete-extension count and the event numerator are

Z=sum_{i=0}^u sum_{j=0}^t F(i,j)G(i,j),
N02=sum_{j=0}^t F(u,j)G(u,j),
Pr(T0<T2)=N02/Z.                                                (6)

Proof: split each extension immediately after T2; i,j count C0,C4 elements in its prefix. Removing C0 and the final T2 leaves all C1 followed by a shuffle of b-1 C2 elements and j C4 elements. Reinsert i C0 elements before T2, giving F. In the suffix, the remaining C0 followed by C3 is one chain, freely shuffled with the remaining C4; all C5 then follow, and C6 shuffles freely with this entire suffix, giving G. Every extension has a unique split. The event T0<T2 is precisely i=u. Thus (6) counts the actual uniform law exactly.

For all 65,951 residual vectors, the integer certificate verifies

3 N02 >= Z.                                                    (7)

Indeed every vector satisfies the stronger 2 N02>Z. The least probability is

4465154496058864828291 / 8852345120096299414144 > 1/2,

attained at (9,2,13,19,19,3,7). The dual minimum occurs at (7,3,19,13,19,2,9). No decimal approximation or floating-point comparison is used in the proof.

Equation (7) contradicts the necessary strict inequality (1), excluding every residual. All other candidates were already excluded by necessary bounds (4). Every vector outside the prerequisite rectangle was excluded by the proved unbounded implications (2)--(3). This proves the theorem.

A rejected forced orientation guarantees that some balanced pair exists by the structural theorem. The tested endpoint itself need not be balanced. In particular this proof does not label every T0,T2 pair a balanced witness.

## 5. Reproducibility and audit limits

`exact_counts.txt` has one row per residual, with seven weight fields followed by Z, N(B1<B0), N(T6<T5), N(T0<T2), N(B2<B4). Its SHA-256 is

0757a2a656f8f3b9dc5608ba4d7b380c8a4e172574bfd8de68cf1bfed64b7978.

The supplementary numerator formulas are the audited prefix-deletion, suffix-deletion, and middle-endpoint variants of (6). They are not needed for the main exclusion once N02 is known. `summarize.py` verifies exact dual denominators and swapped outer numerator identities across all 65,951 vectors; it reconstructs the six oriented tests and confirms zero survivors.

`count_endpoints.cpp` uses exact GMP integers (the preinstalled system library) with a Pascal binomial table. `verify_exact.py` uses only Python's standard library, independently constructs a factorial binomial table, swaps the summation loop order, recomputes every one of the five stored integer counts, and directly verifies all four binomial filter inequalities. It also checks exact equality of the residual sets obtained by the two different domain enumerators. This is full arithmetic cross-validation, not independent peer review and not a claim of a distinct combinatorial derivation.

All Python checks use explicit exceptions and remain active with python -O. The normal and optimized verification outputs record the same mathematical results; the existing dependency manifest identifies the proof sources. A separate independent audit may establish additional implementation and mathematical checks; this author note does not claim that separate audit has passed until it does.
