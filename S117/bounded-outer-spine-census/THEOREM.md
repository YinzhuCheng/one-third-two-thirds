> S117 publication note: this proof/review text records the completed research run. This lean edition retains proof texts, replay sources and selected small results; large generated ledgers, duplicate source snapshots, historical manifests and checksums are not bundled. For the exact retained/generated distinction, portable commands and prior proof links, use [the S117 guide](../README.zh-CN.md), [reproduction instructions](../REPRODUCE.md) and [dependency map](../DEPENDENCIES.md). Historical statements about material being stored refer to that research run; the package contents are listed in the guide.

# Every seven-core inflation with both outer spine weights at most two is balanced

Date: 2026-10-10. Status: complete exact finite-computation-assisted proof, with independently audited universal prerequisites. A new independent peer audit of this census is separate. No statement about unbounded outer spine weights is claimed.

## 1. Statement and actual extension law

Let Q have covers

0<3; 1<2,4; 2<3,6; 3<5; 4<5.

Replace each vertex i by a nonempty chain C_i, with every interblock comparison inherited from Q. Write its weights as

(u,a,b,c,t,d,v)=(w0,w1,w2,w3,w4,w5,w6).

**Theorem.** If a,d belong to {1,2}, then this poset has an incomparable pair (x,y) for which

1/3 <= Pr(x<y) <= 2/3.

The remaining five positive integer weights are unrestricted. Consequently, any remaining counterexample in this seven-core chain-inflation family must have a>=3 or d>=3. The probability is uniform over complete linear extensions of the actual inflated poset, equivalently its valid multiset words. It is never uniform over extensions of the seven-vertex quotient. All closed balance endpoints are retained in the computation.

The theorem is proved by audited unrestricted inequalities reducing the hypothetical counterexamples to a finite set, followed by exact integer certificates excluding every member of that finite set. Computations alone are not claimed to establish any unrestricted inequality.

## 2. Precise universal prerequisites

Use B_i and T_i for the bottom and top of C_i. The previously independently audited good-pair consequence says that an incomparable ordered pair (x,y) satisfying

D(x) subseteq D(y), and U(y) minus U(x) a chain,

must satisfy Pr(x<y)>2/3 in a poset having no balanced pair. The dual set condition gives the corresponding upper-good-pair orientations. This is an application of Zaguia's good-pair theorem, Definition 1 and Theorem 2, https://arxiv.org/html/1610.00809 . All uses below are on the actual inflated poset.

In a hypothetical counterexample, the audited general-terminal theorem gives

- 2<=u<=3 if a=1, and 2<=u<=9 if a=2;
- 2<=v<=3 if d=1, and 2<=v<=9 if d=2;
- 3 product_(i=0)^a(b+i) < product_(i=0)^a(b+u+i);
- 3 product_(i=0)^d(c+i) < product_(i=0)^d(c+v+i).

The lower port bounds are the structural prerequisite. The upper bounds use the general terminal-rank exclusions and their duals. The duality is complete-extension reversal under

(u,a,b,c,t,d,v) -> (v,d,c,b,t,a,u).

The general-terminal proof is frozen at SHA-256
f5f62c0bf2e1224926c80f895b954e274bda134dfc025202a77935262f2cdefa,
and its final independent PASS audit is frozen at
95bf3d1c020ce4d566837f4ff3d4ef7cead3c317830bf1ed7db3804b742ee92b.

The independently audited endpoint insertion and generalized middle-shuffle bounds also require

2u<a+b+t+v,  2v<u+c+t+d,
2t<b+c+u,   2t<b+c+v.                                  (1)

Finally the independently audited rank-chain argument gives

Pr(T1<B0)>2/3,   Pr(T6<B5)>2/3,

and the upper bounds

Pr(T1<B0) <= binom(b+t+v+u,u)/binom(a+b+t+v+u,u),
Pr(T6<B5) <= binom(c+t+u+v,v)/binom(d+c+t+u+v,v).          (2)

Thus both ratios in (2) must be strictly larger than 2/3. The rank-chain proof and exact event correspondence, including B5 rather than T5 in the second event, have frozen independent PASS in dependencies/RANK_CHAIN_AUDIT.md.

For clarity, the reason the first forced rank orientation is stronger than a single endpoint arrow is as follows. Put q_i=Pr(C1_i<B0) and q_0=1. For i<=a this event is precisely the initial prefix C1_1,...,C1_i. The consecutive gaps q_i-q_(i+1), for i<a, equal the counts with that prefix then B0, divided by the original extension total. Prepending one C1 element injects shorter residual extensions into longer ones, so the gaps are nonincreasing. The good-pair condition gives q_1>2/3, hence every gap is below 1/3. If no pair were balanced, the rank chain could never jump from above 2/3 to below 1/3. Therefore q_a>2/3. Conditional insertion of C0 into an outside extension, whose window length satisfies h<=a+b+t+v and whose first a elements are C1, gives the first upper bound (2). This uses the induced outside law, with uniform insertions within each fiber, and makes no uniform-deletion assumption. Reversal gives the second bound.

The two additional safe lower-bound tests

3 binom(a+b+u-1,u) < binom(a+b+t+v+u,u),
3 binom(d+c+v-1,v) < binom(d+c+t+u+v,v)                    (3)

are also recorded and verified. They are **redundant for this proof after (2)**: neither removes any additional candidate. The theorem can omit (3).

## 3. Completeness of the finite reduction

For fixed d,v, the product ratio

R(c)=product_(i=0)^d (c+i)/(c+v+i)

strictly increases with c, since every positive factor does; for fixed c,d it decreases with v. Thus the largest allowed v gives a valid common cap on c.

- If d=1, v<=3. At c=4, 3*4*5=60 >= 7*8=56, so c<=3.
- If d=2, v<=9. At c=20, 3*20*21*22=27720 >= 29*30*31=26970, so c<=19.

Apply the same argument to the dual product to obtain b<=3 when a=1 and b<=19 when a=2. These bounds do not assume that arbitrary weights are self-dual.

By integrality, (1) also gives

t <= floor((b+c+min(u,v)-1)/2) <= 23.

Consequently every hypothetical counterexample with a,d<=2 has total order at most

9+2+19+19+23+2+9=83.

The optimized enumerator in census.py loops over the port and inner caps, checks both strict product inequalities, loops over the exact displayed t interval, and checks the two remaining outer linear inequalities. This is precisely the set satisfying all prerequisites in Section 2 through (1), before the extra binomial filters.

The alternate enumerator in verify_census.py uses the independent rectangular over-envelope a,d in {1,2}, u,v in {2,...,9}, b,c in {1,...,19}, t in {1,...,23}. It checks the d=1/a=1 port caps, both products, and all four original inequalities directly. The resulting sets agree without duplicates. No symmetry quotient is used; dual vectors occur separately.

The complete prerequisite set contains exactly 62,109 weights:

- (a,d)=(1,1): 41;
- (a,d)=(1,2): 1,609;
- (a,d)=(2,1): 1,609;
- (a,d)=(2,2): 58,850.

The maximum order 83 occurs uniquely at (9,2,19,19,23,2,9). These are candidates in a necessary relaxation, not counterexamples.

## 4. Exact full-extension counts and rejection certificate

For 0<=i<=u and 0<=j<=t, define

L(i,j)=binom(b+j-1,j) binom(a+b+i+j-1,i),
G(i,j)=binom(u-i+c+t-j,t-j) binom(u-i+c+t-j+d+v,v).

The exact total is

Z=sum_(i=0)^u sum_(j=0)^t L(i,j)G(i,j).                   (4)

Split each complete word immediately after T2, and let i,j count the C0,C4 elements before it. In the prefix, C1 precedes a shuffle of b-1 C2 elements and j C4 elements, and i C0 elements can be inserted before the final T2. In the suffix, the remaining C0 followed by C3 is one chain, freely shuffled with remaining C4, followed by C5; C6 can be shuffled into that entire suffix. These choices are bijective and give (4).

The following numerators follow directly:

- N(B1<B0) is the same total with a replaced by a-1, from deleting the compulsory first B1;
- N(T6<T5) is the same total with d replaced by d-1, from deleting the compulsory final T5;
- N(T0<T2)=sum_j L(u,j)G(u,j), hence N(T2<T0)=Z-N(T0<T2).

For the fourth endpoint, set H_b(0)=1, and for j>0 set H_1(j)=0 and H_b(j)=binom(b+j-2,j) when b>=2. Then

N(B2<B4)=sum_i sum_j H_b(j) binom(a+b+i+j-1,i)G(i,j).     (5)

After removing the prefix's C0 elements and final T2, the C2/C4 shuffle must begin in C2 when j>0, giving H_b(j). This is the independently audited middle-endpoint count formula.

All four orientations

B1<B0, T6<T5, T2<T0, B2<B4

are structurally forced above 2/3 under the counterexample hypothesis. Rejecting an exact numerator N when 3N<=2Z is therefore valid, including equality. A rejected endpoint need not itself be balanced; the good-pair theorem then supplies a balanced pair somewhere in the poset.

The two rank upper bounds (2), in displayed order, leave exactly

62,109 -> 13,028 -> 2,285.

The two lower bounds (3) leave the same 2,285. By outer-spine pair, these 2,285 are 41,12,12,2,220 in the order above.

Apply the four exact arrows in the displayed order. The remaining counts are

2,285 -> 2,254 -> 2,232 -> 1 -> 0.

Thus every finite candidate is excluded, proving the theorem. The certificate census.json includes every candidate, all four analytic numerator/denominator pairs, exact flags, and one explicit first rejection reason. For every analytic survivor it also records Z and six exact arrow numerators, including the dual old and middle tests. It uses integer cross-multiplication throughout, with no floating-point probability decisions.

The first-rejection partition is

- first rank upper filter: 49,081;
- second rank upper filter: 10,743;
- B1<B0 exact test: 31;
- T6<T5 exact test: 22;
- T2<T0 exact test: 2,231;
- B2<B4 exact test: 1.

These sum to 62,109. No unresolved vector remains.

## 5. The one short-menu residual

The unique vector after both rank upper filters and the first three exact tests is

w=(3,1,2,2,3,1,3),  Z=142680.

The three exact numerators are 95536,95536,105335, all strictly larger than 2Z/3. The middle numerator is

N(B2<B4)=90360,   Pr(B2<B4)=753/1189,

which is genuinely balanced. The dual middle arrow T4<T3 has the same numerator. This is the first rejection in the chosen four-test sequence, not an exclusive rejection by B2<B4 among all eighteen arrows. The vector also survives the old fourth arrow B6<B3, with numerator 105335.

A separate actual-label all-pair calculation for this diagnostic vector gives delta(P)=1700/3567 and retains every incomparable-pair count and every maximizing pair in verification.json. The unique short-menu residual is not a counterexample or an unresolved balance case.

## 6. Independent state-representation validation and scope

The alternate verifier imports no census implementation. It reconstructs the finite candidate region as described above and recomputes all analytic bounds via factorial quotients rather than the primary binomial routine.

For each of the 2,285 analytic survivors it builds the actual labelled poset, with chain edges and quotient cover edges. Its states are actual labelled-element ideal bitmasks. Each transition inserts one eligible actual element. Backward and forward path counts give the denominator and numerator for each query x<y by summing

forward(I) * backward(I union {x})

over transitions inserting x when y is absent. Every desired full extension is counted once, at its unique x transition.

The verifier independently reconstructs all eighteen structurally forced bottom/top arrows from quotient lower/upper sets. For every analytic survivor it counts all eighteen, checks the six double-sum numerators and denominator, and checks each of the four actual analytic event probabilities against its claimed bound. This is a check on the uniform actual full-extension law, not on a quotient law. All eighteen leave zero survivors, so there are no remaining vectors requiring an all-pair search. Only the short-menu diagnostic above receives an additional full all-pair calculation.

The normal replay passes all 248,436 analytic arithmetic checks, 41,130 endpoint counts, 13,710 double-sum numerator cross-checks, and 9,140 actual probability-bound comparisons. Its 2,285 actual-label DPs contain 11,511,843 ideals in total and at most 11,560 for one vector. The two lower-bound filters each have five equality cases in the full 62,109-vector region; strict comparisons correctly exclude equality. Normal and python -O replays agree byte-for-byte for both the complete census and the alternate verification output. Every validation uses explicit exceptions; optimization cannot disable the checks. Reproducible counts and source bindings are in verification.json, MANIFEST.json and SHA256SUMS. A separate independent mathematical/computational peer audit is not replaced by these author cross-checks.

The finite certificate supports only a,d in {1,2}. It does not prove the seven-core conjecture for arbitrary outer weights, or for all seven weights. Nor does it establish a universal lower bound on delta(P) beyond 1/3. The unbounded range in the theorem is the five other positive weights, covered by the proved finite reduction.
