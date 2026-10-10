# Four-ray exclusion for singleton spine blocks

Date: 2026-10-10. This proves the four-ray family exclusion, using the already audited structural-good-pair prerequisite. It does not prove the result for arbitrary seven-block weights.

## Setup and statement

The quotient has covers 0<3; 1<2,4; 2<3,6; 3<5; 4<5.
Inflate its blocks by chains of lengths (u,1,1,1,t,1,v), with u,t,v positive integers.
Write A=C0, C=C4, F=C6, and r=B1=T1, s=B2=T2, x=B3=T3, z=B5=T5.
All probabilities are uniform over complete linear extensions of the inflated poset.

**Uniform bound.** For every u,t,v≥1,

Pr(s<B4) ≤ (v+2)/(v+t+2).                                      (1)

In fact the inequality is strict for v≥1, but the weak inequality suffices.

Together with the established four-ray necessary condition, (1) excludes all possible counterexamples having the four spine blocks 1,2,3,5 singleton. Therefore every chain inflation with weights (u,1,1,1,t,1,v), for arbitrary positive u,t,v, has a balanced pair somewhere.

The proof below uses the existing forced-arrow theorem only for the implication that a poset without a balanced pair must have Pr(B2<B4)>2/3. A failed forced orientation does not by itself identify the balanced pair.

## A weighted binary-shuffle lemma

Fix k,t≥1, a≥0, and 1≤q≤k. Consider three labelled chains A of length a, S=(S1,...,Sk), and C=(C1,...,Ct), with the additional relations Ai<Sq for all i. If a=0 these extra relations are empty. There are no other cross-relations. Under uniform complete linear extensions of this poset,

Pr(S1<C1) ≤ k/(k+t).                                          (2)

Proof. First fix a binary shuffle w of S and C, and let R(w) be the rank of Sq in that word, starting at 1. The A-chain can be inserted in exactly

W(R)=binom(a+R−1,a)

ways, because its a elements must be distributed over the R gaps before Sq. Thus the induced law on binary shuffles is the initially uniform law weighted by W(R), an increasing function of R.

Under the initially uniform binary-shuffle law, E={S1<C1} means the first symbol is S, so Pr(E)=k/(k+t). The conditional rank R given E is stochastically no larger than the conditional rank R given its complement:

Put n=k+t. Choose a uniform k-element subset U of {2,...,n}, and remove one of its elements uniformly, producing V. Then V is a uniform (k−1)-element subset of {2,...,n}. The S-position set {1} union V has precisely the law conditional on E, while U has precisely the law conditional on the complement of E. If q=1, the two ranks are 1 and min(U). If q≥2, the two ranks are V_(q−1) and U_q, and V_(q−1)≤U_q for every such pair of subsets. (An order statistic with index j means the jth smallest member.)

It follows that E[W(R)|E]≤E[W(R)|not E]. Weighting a two-event partition by such conditional mean weights can only decrease the probability of E. This proves (2). Every weight is positive; the statement covers a=0 because then W is identically 1. QED.

## Proof of the uniform bound

Condition a complete extension on the following data:

- i, the number of A-elements before r, where 0≤i≤u;
- f, the number of F-elements before z, where 0≤f≤v;
- the relative order of the elements s, x, and the first f elements of F before z.

Before r, the extension consists exactly of the first i elements of A; no other block is allowed there. After z, it consists exactly of the remaining v−f elements of F; all other blocks are below z. Both the prefix before r and suffix after z are therefore unique after this conditioning.

In the conditioned relative order, s is first, since s<x and s<F. The remaining symbols are x and the first f elements of F, with F internally ordered. Regard this fixed word as a chain S of length k=f+2. Let q be the rank of x in S, so 2≤q≤k.

The segment strictly between r and z consists of precisely:

- the remaining a=u−i elements of the A-chain;
- all t elements of C;
- the k elements of S.

Its only cross-relation, after these three internal orders are fixed, is that every remaining A-element precedes x=Sq. There are no A-to-C, C-to-S, or A-to-F cross-relations. All three chains lie after r and before z in this conditioned segment.

Every admissible shuffle of these three chains gives one complete extension with the fixed data, and conversely. Consequently the conditional law on these shuffles is exactly uniform, not a uniform quotient law or an assumed uniform deletion law.

Apply the lemma:

Pr(s<B4 | i,f,the fixed relative order) ≤ (f+2)/(f+t+2)
                                      ≤ (v+2)/(v+t+2).

Averaging proves (1). There are valid extensions with f=0<v, giving strictness for positive v if desired. QED.

## Excluding all four rays

The established linear cone and singleton-port filter show that any counterexample in this family must have u,v≥2 and

(u,v) ∈ {(t+1,t+1), (t,t), (t,t−1), (t−1,t)}.

In particular v≤t+1. If t≥3, (1) gives

Pr(B2<B4) ≤ (t+3)/(2t+3) ≤ 2/3.

This contradicts the required strict forced orientation Pr(B2<B4)>2/3. Thus all t≥3 ray points are excluded, without using sampled values or asymptotics.

For t=2, the condition u,v≥2 leaves exactly (u,v)=(2,2),(3,3). Exact integer counts, independently checked by labelled ideal DP, give:

- (2,1,1,1,2,1,2): e(P)=1,121 and e(P with B2<B4)=667.
  Thus Pr(B2<B4)=667/1121 is a concrete balanced-pair witness.
- (3,1,1,1,2,1,3): e(P)=7,626 and e(P with B2<B4)=4,908.
  Thus Pr(B2<B4)=4908/7626=818/1271 is a concrete balanced-pair witness.

For t=1, only (u,v)=(2,2) remains. Its exact counts give e(P)=315 and e(P with B1<B0)=202, so B1,B0 are a concrete balanced pair with probability 202/315.

There are no further positive t cases. QED.

## Dependencies and scope

The seven-block quotient, correct chain-inflation extension law, forced-arrow prerequisite, and four-ray necessary condition are recorded in /workspace/shared/weighted-surviving-core/ANALYTIC_RESULT.md. The forced-arrow prerequisite uses Zaguia's good-pair theorem (Definition 1 and Theorem 2): https://arxiv.org/html/1610.00809 .

This document supplies a direct, independent proof of the new shuffle bound. Its conclusion is the whole three-parameter family (u,1,1,1,t,1,v), because the previous structural filters reduce any hypothetical counterexample in that family to the four rays. The conclusion remains conditional on those previously established filters exactly as stated. No all-seven-weight theorem is claimed. For t≥3, only existence of some balanced pair is concluded; no particular pair is claimed balanced without a separate lower bound.
