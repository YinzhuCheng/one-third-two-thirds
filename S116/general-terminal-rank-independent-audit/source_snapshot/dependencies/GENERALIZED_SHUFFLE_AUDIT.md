# Independent audit: generalized seven-core shuffle bounds

Date: 2026-10-10. **Final verdict: PASS, bound to the author source hashes below.**

This audit independently reconstructs the complete-extension fibers, implements actual-label ideal DP, and tests the proposed exact numerator against that DP. It does not import or call the author's implementation. The results apply to chain inflations of the quotient with covers 0<3; 1<2,4; 2<3,6; 3<5; 4<5 and positive weights (u,a,b,c,t,d,v).

## 1. Findings and scope

The following claims are correct:

1. Pr(B2<B4) < (b+c+v)/(b+c+v+t) for every positive weight vector.
2. Pr(T4<T3) < (b+c+u)/(b+c+u+t), by genuine order-reversal duality.
3. Using the prior structural forced-orientation theorem, a hypothetical counterexample must satisfy 2t<b+c+min(u,v).
4. Together with 2u<a+b+t+v and 2v<u+c+t+d, this implies 2t≤a+d+3b+3c−4.
5. The author's sharper integer cap and full finite-cone intervals are exact for this inequality relaxation, including the claimed extremal construction.
6. The proposed double-sum numerator for Pr(B2<B4) is correct, including b=1 and j=0 boundaries.

The universal probability bounds and counting identity are directly proved. The consequences for counterexamples additionally depend on the already audited structural-good-pair prerequisites and singleton-port exclusion. This audit does not convert a necessary-condition cone into a set of counterexamples and does not assert an all-seven-weight balanced-pair theorem.

## 2. Independent full-extension fiber reconstruction

Let L be a complete labelled extension. Record its entire ordered prefix through T1, its entire ordered suffix starting at B5, and the relative order S of all C2 and C3 elements together with the C6 elements before B5.

The prefix contains exactly C1 and a prefix of C0. The suffix contains exactly C5 and a suffix of C6. These statements hold for arbitrary a,d≥1. Fixing merely the two lengths would not make these external segments unique; fixing their full ordered words does.

Write i for the number of C0 elements in the prefix and f for the number of C6 elements before B5. The middle then contains exactly:

- the remaining r=u−i elements of C0;
- all t elements of C4;
- the fixed word S of length k=b+c+f.

Because T2 precedes every C3 and C6 element, S begins with all b C2 elements and S1=B2. If q is the rank of B3 in S, its exact possible range is

b+1 ≤ q ≤ b+f+1 ≤ k.

Thus neither q=0 nor an out-of-range q can occur. The original cross-relations among these three chains reduce precisely to C0 remainder < S_q. In particular, there is no hidden C4-to-S relation, and no C0-to-C6 relation. Original C1 predecessor relations have already been satisfied by the fixed prefix, while every C5 successor relation is satisfied by the fixed suffix.

Adjoining the fixed prefix and suffix to any legal middle shuffle gives one full extension in the fiber, and deletion of those fixed words reverses the construction. This proves a bijection, and hence the exact conditional uniform law. No uniform quotient-extension or uniform deletion assumption occurs.

## 3. Weighted lemma, endpoint checks, and strictness

For chains of lengths r,k,t with C0 remainder < S_q, deleting the r-chain produces a binary S/C4 word. If R is the position of S_q in this binary word, its multiplicity is binom(r+R−1,r). There are R possible gaps before S_q, and distributing an ordered r-chain among them gives exactly that stars-and-bars count.

Under uniform binary shuffles, E={S1<C4_1} has probability k/(k+t). The standard coupling is valid even at q=1 and q=k: take a uniform k-subset U of {2,...,k+t}, remove one uniformly chosen member to produce the uniform (k−1)-subset V, and compare the S-position sets U and {1}∪V. For q=1 the ranks are min(U)>1 and 1; for q≥2 the ranks are U_q and V_(q−1)≤U_q. Therefore the increasing insertion weight cannot increase Pr(E).

There is a useful stronger equality statement: equality in this lemma occurs exactly when r=0. If r>0, the insertion weight is strictly increasing. For q=1 the coupled rank inequality is always strict. For q≥2, deleting any member of U at rank q or later gives V_(q−1)=U_(q−1)<U_q with positive probability; q≤k ensures such a member exists. Hence the conditional mean insertion weights are strictly ordered and the lemma probability is strictly smaller.

The global strict bound needs no argument about which fibers have r>0. Every positive weight vector has a legal complete extension with f=0, for example the full block order C0,C1,C2,C3,C4,C5,C6. Such a fiber has positive probability, and

(b+c)/(b+c+t) < (b+c+v)/(b+c+v+t)

because v,t>0. Averaging the fiber bounds is therefore strictly below the final envelope. Equality is impossible in either global bound for the stated positive domain.

Duality is the complete-extension reversal with relabeling (0 6)(1 5)(2 3). It sends weights to (v,d,c,b,t,a,u), and the transformed B2<B4 event corresponds to original T4<T3. This checks both the endpoint choice and orientation.

## 4. Arithmetic cone and sharpness

Put s=b+c, α=a+b−1, β=c+d−1. The integer form of the four necessary inequalities is

2u−v≤t+α, 2v−u≤t+β, u,v≥2t−s+1.

Therefore

u≤t+U, v≤t+V,
U=floor((2α+β)/3), V=floor((α+2β)/3),
t≤T=s−1+min(U,V).

For a fixed t, let L=max(2,2t−s+1). Solving the two upper inequalities for v gives precisely

L≤u≤t+U,
max(L,2u−t−α)≤v≤floor((u+t+β)/2).

These intervals are equivalent to the four inequalities and u,v≥2; an empty interval contributes no vector. No omitted inequality is needed in the converse.

For sharpness, the possible remainders of (2α+β,α+2β) modulo 3 are (0,0),(1,2),(2,1). Consequently 2U−V≤α and 2V−U≤β. The vector (u,v)=(t+U,t+V) satisfies the full relaxation for every 1≤t≤T; U,V≥1 enforce both port constraints. At t=T it attains the cap and both global coordinate upper bounds. This proves sharpness only of the inequality relaxation.

Equivalently,

3t≤2a+d+5b+4c−6,
3t≤a+2d+4b+5c−6.

Adding the original two upper inequalities gives u+v≤a+d+s+2t−2, whereas the two lower inequalities give u+v≥4t−2s+2. Combining them proves the requested simpler 2t≤a+d+3b+3c−4. All constants and strict-to-integer conversions check out.

For a=b=c=d=1, T=2 and the new cone contains exactly (u,t,v)=(2,1,2),(3,2,3). The vector (2,2,2) fails the new condition, so it must not be listed as a new-cone survivor.

## 5. Independent numerator check

At the T2 split, remove the C0 elements from the prefix and its final T2. The remaining C2/C4 subword has b−1 C2 symbols and j C4 symbols after C1. To enforce B2<B4:

- If j=0, there is one admissible C2/C4 word.
- If b=1 and j>0, there are none, because all those C4 elements precede B2=T2.
- Otherwise the first symbol must be C2, leaving b−2 C2 and j C4 symbols. The number is binom(b+j−2,j).

The C0 insertion and suffix factors are independent of this restriction and remain exactly the author's K(i,j). This proves the H_b(j) coefficient and the new numerator, including all boundaries. Duality provides the second numerator.

## 6. Independent computational evidence

The self-contained standard-library script audit.py uses a predecessor bitmask on every actual labelled element. It counts order ideals recursively. Each probability numerator is obtained by adding the corresponding actual-label comparison edge and counting again. No block-word recurrence or double-sum formula is used as the oracle.

Verified results in results.json:

- 756 weighted-lemma cases, lengths r=0,...,5 and k,t=1,...,6 with every q=1,...,k; 126 equality cases exactly at r=0 and 630 strict cases. Both q endpoints have 216 checks.
- All 2,187 vectors in {1,2,3}^7, with 10,935 independent actual-label DP calls and 4,374 comparisons with the transcribed closed formulas. Both strict inequalities and dual equality pass.
- Nine larger asymmetric weight vectors, including substantial a,d values and up to 50 actual elements, pass the same checks.
- Complete enumeration of 10,110 labelled extensions across five selected vectors, grouped into 240 fibers. Every fiber's cardinality and event numerator agree with a separately counted three-chain lemma poset. This tests the full-prefix/full-suffix bijection, including non-singleton a,d.
- All 6,912,000 integer candidates with spine weights in [1,4] and u,t,v in [1,30], checking the 23,774 survivors of the four-inequality cone against every claimed derived bound.
- All 160,000 spine choices in [1,20]^4, checking the sharp cap identity, residue inequalities, and extremal cone witness.

These finite checks support implementation accuracy. They are not substitutes for the universal proofs above.

## 7. Reproduction and separation of supplements

Run `python audit.py` in this directory. The run rewrites results.json and prints its output. The separate files rank_chain_supplement.py, rank_chain_results.json, and rank_chain_run.log concern an additional rank-chain candidate and are not part of the primary author's shuffle-source claim set.

## 8. Frozen source binding and replay

The author declared the following source snapshot frozen; this audit independently read it, recomputed all three hashes, and replayed the exact verifier in a separate directory:

- GENERALIZED_SHUFFLE_BOUND.md: e522a13a63f73a58c1af862e603c3b90c46084a1f83b3b79da7e6bd3d6b0a8d3
- verify_generalized_shuffle.py: 0a69a8efaac4a95d645c65705f7b25ba2c721d4eadcf7eee941fbe27e041369a
- verification.json: 9f89f96bd7b5ac9ad938860200894b0d2f8789aac7185aaf8ab8813a368cde4d

Both the author replay and this independent audit were run under normal Python and python -O; their checks remain active in optimized mode. The author replay reproduced its frozen verification.json byte-for-byte in both modes. The independent results.json likewise agrees byte-for-byte between normal and optimized runs.

The author replay covers 2,255 full-weight vectors, 6,765 block-DP counts, 4,510 strict probability checks, 121,327 complete words in 3,192 fibers, and 350,020 cone comparisons. These are additional to, and differently implemented from, the actual-label oracle evidence above.

No substantive correction to the frozen primary source was required. Its full-prefix/full-suffix conditioning correctly handles arbitrary a,d, and its strictness, dual event, integer floors, and H_b boundaries are valid.
