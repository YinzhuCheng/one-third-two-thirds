# Excluding an arbitrary single outer-spine chain

Date: 2026-10-10. Status: direct proof; independent audit of the newly generalized middle-shuffle bound is a stated dependency. Numerical verification is supplementary, not the proof.

## Statement and scope

Let Q have covers

0<3; 1<2,4; 2<3,6; 3<5; 4<5.

Replace its vertices by nonempty chains with weights

(u,a,1,1,t,1,v).

Assuming the established structural-good-pair prerequisites and the generalized middle-shuffle bound stated below, every such inflation, for all positive integers u,a,t,v, has a balanced pair. By the quotient duality (0 6)(1 5)(2 3), the same holds for every weight vector (u,1,1,1,t,d,v).

The a=1 subfamily is already excluded in the S113 four-ray result. The new part here is the full a>=2 range. This is not a theorem about simultaneous arbitrary a,d, about varying b,c, or about arbitrary seven weights.

Write A=C0, R=C1, C=C4, F=C6. Their lengths are u,a,t,v. The blocks C2,C3,C5 are singleton elements s,x,z, respectively. B_i and T_i mean the bottom and top of block i. All probabilities are under uniform complete linear extensions of the actual chain inflation.

## Prerequisites for a hypothetical counterexample

The established structural-good-pair argument and singleton-port filter imply:

1. u,v>=2.
2. P(B1<B0)>2/3.
3. P(T6<T5)>2/3, hence 2v<u+t+2 by the already proved window-insertion bound.
4. P(T4<T3)>2/3. The generalized middle-shuffle bound gives

   P(T4<T3) <= (u+2)/(u+t+2),

   and therefore 2t<u+2.

Items 1--3 and the forced orientation in item 4 are structural prerequisites, not assumptions about a particular pair being balanced when an orientation fails. The numerical upper bound in item 4 is the dual instance of the generalized middle-shuffle inequality; its independent audit is being handled separately.

The proof below uses no other linear cone and no finite search for a>=2.

## Lemma 1: all R ranks must precede B0 with probability greater than 2/3

Suppose P has no balanced pair. Set q0=1 and, for 1<=i<=a,

qi=P(R_i<B0).

The only minimal elements are B0 and B1. Before T1 appears, the only possible elements belong to C0 and R, because every other block has T1 as a predecessor. Therefore, for i<=a, the event R_i<B0 forces the first i elements of the extension to be R_1,...,R_i. Thus qi is exactly the probability of this forced initial prefix.

Let Z(u,r,1,1,t,1,v) count the remaining poset when R has length r, permitting r=0 in this deletion interpretation. Deleting the forced initial R-prefix gives

qi = Z(u,a-i,1,1,t,1,v)/Z(u,a,1,1,t,1,v).

For 0<=i<a, deleting the initial prefix R_1,...,R_i,B0 gives

qi-q(i+1) = Z(u-1,a-i,1,1,t,1,v)/Z(u,a,1,1,t,1,v).       (1)

For fixed other weights, Z(u-1,r,1,1,t,1,v) is nondecreasing in r>=1. Indeed, every extension with r-1 R-elements extends injectively to one with r R-elements by prepending a new first R-element and shifting the old R-labels. Hence the gaps in (1) are nonincreasing in i.

The first gap is q0-q1=1-P(B1<B0)<1/3. Therefore every gap is strictly less than 1/3. Since q1>2/3, induction shows qi>2/3 for every i: if qi>2/3, then q(i+1)>1/3, and R_(i+1),B0 are incomparable, so the absence of any probability in the closed balanced interval [1/3,2/3] forces q(i+1)>2/3. In particular,

qa=P(T1<B0)>2/3.                                         (2)

This argument is not a uniform-deletion-law assumption. The counts are exact prefix-deletion bijections under the original uniform complete-extension law.

## Lemma 2: a binomial upper bound for the last R rank

Remove the entire A-chain, and condition on one extension of the remaining poset. Its A-insertion window starts at the beginning and ends immediately before x=B3. Let h be the number of outside elements in this window.

The outside extension begins with all a R-elements; the window also contains s and some initial elements of C and F. Consequently

a+1 <= h <= a+1+t+v.

There are binom(h+u,u) equally likely A-insertions after conditioning. The event T1<B0 says that no A-element occurs before the ath outside element. Exactly binom(h-a+u,u) insertions satisfy it. Put H=1+t+v. The conditional probability is

binom(h-a+u,u)/binom(h+u,u)
 = product_(r=1)^a (h-a+r)/(h-a+u+r)
 <= product_(r=1)^a (H+r)/(H+u+r).

Each factor increases with h, so the inequality holds for every outside extension and survives averaging under the induced outside law. Thus

qa <= product_(r=1)^a (H+r)/(H+u+r).                      (3)

If a>=2, all remaining factors are less than one, giving

qa <= (H+1)(H+2)/[(H+u+1)(H+u+2)].                       (4)

## The contradiction for every a>=2

The two necessary strict integer inequalities in the prerequisites give

2t<u+2  =>  t <= (u+1)/2,
2v<u+t+2  =>  v <= (u+t+1)/2.

Therefore

H=1+t+v <= (u+3t+3)/2 <= (5u+9)/4.

Each factor in (4) increases with H. Substituting this upper bound yields

qa <= [(5u+13)(5u+17)]/[(9u+13)(9u+17)] < 2/3             (5)

for every integer u>=2. To check the last strict inequality, its positive denominators reduce it to

2(9u+13)(9u+17)-3(5u+13)(5u+17)
 = 87u^2+90u-221 > 0.

At u=2 the polynomial is 307, and it increases thereafter. Equation (5) contradicts (2). Hence no counterexample with a>=2 exists. Together with S113 for a=1, this excludes the entire four-parameter family.

## Optional stronger gap observation

The proof of Lemma 1 only uses the facts that two chains are the entire initial set of available elements, that one chain's remaining length can be increased by prepending its new first element, and that its first element has probability >2/3 of preceding the other chain's first element. It applies unchanged to the original seven-core inflation with arbitrary positive weights. The binomial bound there becomes

P(T1<B0) <= binom(b+t+v+u,u)/binom(a+b+t+v+u,u).

Thus every no-balanced-pair inflation must satisfy

3 binom(b+t+v+u,u) > 2 binom(a+b+t+v+u,u).

Its dual version is also necessary. No general all-weight theorem follows here.

## Verification and exact dependencies

The companion verify_single_outer_spine.py uses:

- the exact binomial double-sum count;
- an independent ideal DP on labelled elements, with added pair constraints;
- exhaustive bounded verification of the prefix identities, nonincreasing gaps, insertion bound, and the two middle probabilities;
- an exact integer check of the polynomial implication over a bounded grid as a coding check.

The finite computation is explicitly bounded in the script and JSON. It does not establish the infinite theorem; Lemmas 1--2 and the displayed algebra do.

Existing references:

- /workspace/shared/weighted-surviving-core/ANALYTIC_RESULT.md for the quotient, exact count, endpoint prerequisites, and terminal linear bound.
- /workspace/shared/four-ray-exclusion/FOUR_RAY_EXCLUSION.md for the whole a=1 family.
- The separately authored and audited generalized middle-shuffle result for P(T4<T3)<=(u+2)/(u+t+2).

The structural prerequisites use Zaguia's good-pair theorem (Definition 1 and Theorem 2), https://arxiv.org/html/1610.00809 . A failed forced orientation proves existence of some balanced pair; it does not automatically identify that tested pair as a balanced witness.
