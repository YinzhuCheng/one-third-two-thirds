# Excluding every inflation with both inner spine blocks singleton

Date: 2026-10-10. Direct proof, extending the separately frozen one-outer-spine result. Its dependencies are the previously audited structural-good-pair prerequisites, S113, and the generalized middle-shuffle bound. The new argument below is independent of finite experimentation.

## Theorem

For the seven-block quotient with covers

0<3; 1<2,4; 2<3,6; 3<5; 4<5,

every chain inflation with positive weights

(u,a,1,1,t,d,v)

has a balanced incomparable pair under its uniform complete-extension law.

Equivalently, any counterexample built by chain inflation of this quotient must have at least one nonsingleton inner spine block: b>1 or c>1. This theorem does not address arbitrary b,c and is not an all-seven-weight result.

## Prerequisites and rank filters

Use the notation B_i,T_i for the endpoints of C_i. A hypothetical counterexample satisfies u,v>=2. The generalized middle-shuffle bound supplies

2t<2+u and 2t<2+v.                                      (1)

The monotone-prefix-gap argument in SINGLE_OUTER_SPINE_EXCLUSION.md applies unchanged with arbitrary d: before T1 appears, only C0 and C1 can appear, so R_i<B0 for i<=a forces the initial R-prefix; adding one initial C1 element gives the same counting injection. Thus absence of a balanced pair, together with the structural prerequisite P(B1<B0)>2/3, forces

P(T1<B0)>2/3.                                           (2)

Inserting C0 into an outside extension gives

P(T1<B0) <= product_(r=1)^a (K+r)/(K+u+r),
K=1+t+v.                                               (3)

Neither the prefix argument nor its insertion window depends on d. Reversing full extensions under the quotient involution (0 6)(1 5)(2 3), which fixes 4, sends the weight vector to

(v,d,1,1,t,a,u).

Applying (2)--(3) in the dual gives exactly

P(T6<B5)>2/3,
P(T6<B5) <= product_(r=1)^d (K'+r)/(K'+v+r),
K'=1+t+u.                                              (4)

The event correspondence matters: the top of dual block 1 is original B5, and the bottom of dual block 0 is original T6; reversing their order yields T6<B5 in the original poset.

## The case a,d>=2

Because the conclusion and the hypotheses a,d>=2 are duality-invariant, assume v>=u.

By (1) and integrality,

t <= (u+1)/2.

Consequently

K'=1+t+u <= (3u+3)/2 <= (3v+3)/2.

Since d>=2, truncate the product in (4) to its first two factors. Each factor increases with K', so

P(T6<B5)
 <= (K'+1)(K'+2)/[(K'+v+1)(K'+v+2)]
 <= (3v+5)(3v+7)/[(5v+5)(5v+7)]
 < 2/3.                                                (5)

For the final strict inequality,

2(5v+5)(5v+7)-3(3v+5)(3v+7)
 = 23v^2+12v-35 > 0

for every integer v>=2. It is 81 at v=2 and increases thereafter. This contradicts the first inequality in (4), excluding every a,d>=2 instance.

## The remaining cases

- If d=1, the entire (u,a,1,1,t,1,v) family is excluded by SINGLE_OUTER_SPINE_EXCLUSION.md. Its a>=2 proof combines (1), the old terminal cone, and (2)--(3). Its a=1 case is S113.
- If a=1, reverse the poset to obtain a d=1 instance and apply the same result.

These cases exhaust all positive integers a,d, proving the theorem.

## Dependency discipline and validation

The following are distinct facts:

1. The structural prerequisites force certain orientations only under the no-balanced-pair hypothesis.
2. The shuffle and prefix-insertion bounds apply to every inflation under its actual uniform extension law.
3. The algebra combines these facts into a contradiction for the whole five-parameter family.

No uniform law on the quotient or on deleted extensions is used. Failure of a forced orientation proves that some balanced pair exists; this proof does not identify a single universal balanced-pair witness.

The file verify_two_singleton_inner_blocks.py performs independent labelled ideal-DP checks over the explicitly bounded five-dimensional box u,a,t,d,v in {1,2,3,4}. It verifies both complete endpoint-rank chains, their prefix/suffix deletion formulas, their monotone gaps, the product bounds, and the relevant middle probabilities. Its additional algebra loop is only an implementation check. The universal proof is above and in the one-outer-spine result.

Dependencies:

- SINGLE_OUTER_SPINE_EXCLUSION.md, SHA256 b39b63f4e7b457359fe541f7224435e8e44f24e4b9a08b1c8e2348c61da5ce81.
- /workspace/shared/generalized-seven-core-shuffle/GENERALIZED_SHUFFLE_BOUND.md, for the full-weight shuffle bounds.
- /workspace/shared/four-ray-exclusion/FOUR_RAY_EXCLUSION.md, for S113.
- /workspace/shared/weighted-surviving-core/ANALYTIC_RESULT.md, for the quotient and prior necessary inequalities.

The separate independent audit is authoritative for the audit status of these dependencies and of this supplement.
