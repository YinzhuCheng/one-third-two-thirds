# Independent supplement audit: rank-chain filters and singleton inner blocks

Date: 2026-10-10. **Final verdict: PASS for the corrected, frozen sources listed below.**

The source package is /workspace/shared/single-outer-spine-exclusion. This supplement is separate from the primary generalized-shuffle audit. Its infinite statements use the prior structural-good-pair prerequisites, the already proved S113 singleton-spine result, and the generalized middle-shuffle bounds independently audited in AUDIT.md.

## 1. Results accepted

For every no-balanced-pair inflation of the seven-core quotient, with positive weights (u,a,b,c,t,d,v), the following additional necessary conditions hold:

Pr(T1<B0)>2/3,
Pr(T6<B5)>2/3,

3 binom(b+t+v+u,u) > 2 binom(a+b+t+v+u,u),
3 binom(c+t+u+v,v) > 2 binom(d+c+t+u+v,v).

The companion infinite-family conclusions are valid:

- Every positive (u,a,1,1,t,1,v) inflation has a balanced pair, as does its dual family (u,1,1,1,t,d,v).
- More strongly, every positive (u,a,1,1,t,d,v) inflation has a balanced pair, allowing both outer spine weights a,d to vary simultaneously.

Hence any remaining chain-inflation counterexample on this quotient must have b≥2 or c≥2. These claims do not establish the arbitrary-seven-weight conjecture, and they do not identify one fixed endpoint pair that is balanced in every member of the excluded families.

## 2. Important correction made before the source freeze

An earlier draft said that every element before B0 must belong to C1. That assertion is false: after T1 has appeared, elements of C2 and C4 may appear before B0. The author corrected this before the audited freeze.

The exact valid statement is: before T1 appears, only C0 and C1 can occur; therefore, for every 1≤i≤a, the event C1_i<B0 is equivalent to the first i extension elements being precisely C1_1,...,C1_i. The gap formula below is used only for 0≤i<a. The correction changes no counting identity or conclusion but is essential to the proof's wording.

## 3. Independent rank-chain proof

Set q0=1 and qi=Pr(C1_i<B0), 1≤i≤a. The valid initial-prefix bijection gives

qi=Z(u,a−i,b,c,t,d,v)/Z(u,a,b,c,t,d,v),

where the zero-length C1 count means deletion of that initial chain. For 0≤i<a, the event qi minus q(i+1) has the unique initial word C1_1,...,C1_i,B0. Consequently

gi=qi−q(i+1)=Z(u−1,a−i,b,c,t,d,v)/Z(u,a,b,c,t,d,v).

As the remaining C1 length r increases, prepending a new C1 bottom and shifting the old C1 labels injects every old extension into an extension with r+1 C1 elements. Thus the displayed gaps are nonincreasing in i. The structural requirement q1>2/3 implies g0<1/3 and hence every gi<1/3.

Every pair C1_i,B0 is incomparable. Under the no-balanced-pair hypothesis, none of its probabilities may belong to the closed interval [1/3,2/3]. Starting with q1>2/3, a step of size less than 1/3 cannot move directly below 1/3; the intervening interval is forbidden. Induction forces qa=Pr(T1<B0)>2/3. This uses exact counts under the original uniform full-extension law, not a uniform-deletion law.

For the upper bound, remove C0 and fix an outside extension. Its insertion window ends immediately before B3 and contains h elements, where a+b≤h≤a+b+t+v. Its first a elements are exactly C1. The C0 insertion is uniformly distributed over the binom(h+u,u) possible shuffles. The probability that all a C1 elements precede B0 is

binom(h−a+u,u)/binom(h+u,u)
 = product_(r=1)^a (h−a+r)/(h−a+u+r).

Each factor increases with h, so the upper endpoint h=a+b+t+v bounds each conditioned probability. Averaging under the induced outside-extension law gives

Pr(T1<B0)≤binom(b+t+v+u,u)/binom(a+b+t+v+u,u).

The strict necessary binomial inequality follows. Reversal with (0 6)(1 5)(2 3) sends the weight vector to (v,d,c,b,t,a,u). The dual event is precisely original T6<B5, yielding the second orientation and binomial condition. The use of B5 rather than T5 in the stronger rank condition is correct.

## 4. Independent check of the one-outer-spine exclusion

For b=c=d=1 and a≥2, put K=1+t+v. The upper bound is a product of a numbers strictly below one, so it is at most its first two factors:

Pr(T1<B0)≤(K+1)(K+2)/[(K+u+1)(K+u+2)].

The middle-shuffle condition 2t<u+2 gives t≤(u+1)/2, and the old terminal cone 2v<u+t+2 gives v≤(u+t+1)/2. Therefore K≤(5u+9)/4. Since both factors increase with K,

Pr(T1<B0)≤(5u+13)(5u+17)/[(9u+13)(9u+17)]<2/3

for u≥2. Cross multiplication gives exactly

2(9u+13)(9u+17)−3(5u+13)(5u+17)=87u²+90u−221.

Its value at u=2 is 307, and its derivative is positive thereafter. This contradicts the stronger rank orientation. The prior port filter supplies u≥2 under the counterexample hypothesis. The a=1 case is S113, and duality covers the other outer spine.

## 5. Independent check of simultaneous arbitrary outer spines

Suppose b=c=1 and a,d≥2. By reversal, assume v≥u. Apply the dual rank bound, writing K'=1+t+u:

Pr(T6<B5)≤(K'+1)(K'+2)/[(K'+v+1)(K'+v+2)].

The middle inequality 2t<u+2 implies

K'≤(3u+3)/2≤(3v+3)/2.

Monotonicity in K' gives

Pr(T6<B5)≤(3v+5)(3v+7)/[(5v+5)(5v+7)]<2/3,

because

2(5v+5)(5v+7)−3(3v+5)(3v+7)
 =23v²+12v−35=(v−1)(23v+35)>0

for v≥2. This contradicts Pr(T6<B5)>2/3. The source's value 81 at v=2 is correct. The a=1 or d=1 cases reduce to the preceding theorem and its dual. These cases exhaust all positive a,d.

The proof uses the actual complete-extension reversal, so its assumption v≥u is legitimate while simultaneously swapping a and d. Since a,d≥2 is reversal-invariant, no case is lost. For completeness, at v=1 the rational bound is exactly 2/3, which would still contradict the strict forced orientation; the source's use of the prior port prerequisite is harmless.

## 6. Independent tests and replays

rank_chain_supplement.py reuses only this auditor's actual-label predecessor-mask DP in audit.py. It does not import the author source. It checks:

- all 2,187 weight vectors in {1,2,3}^7 and four larger asymmetric vectors;
- an additional 3,125 vectors with u,a,t,d,v independently in {1,2,3,4,5} and b=c=1;
- every rank gap through actual-label constrained counts against the independently reconstructed residual actual-label poset;
- gap monotonicity, the binomial upper bound, and the claimed forced crossing into [1/3,2/3] whenever q1>2/3 but qa≤2/3;
- both polynomial positivity calculations for every integer input from 2 through 10,000.

Duality sends each of the two complete boxes to itself, so these tests cover both rank-filter orientations. Normal and python -O runs produce identical rank_chain_results.json, with checks active in both modes.

The exact corrected author scripts were copied to a separate replay directory and run in both modes. Both reproduce their frozen JSON byte-for-byte:

- Baseline: 625 vectors, 3,750 labelled-DP counts.
- Simultaneous outer spines: 1,024 vectors, 8,192 labelled-DP counts.

The author changed assertion statements to an explicit require helper before the final code freeze, so optimized mode cannot silently skip validation. Finite tests validate the implementations; the infinite theorems rest on the proofs above.

## 7. Frozen source hashes

- SINGLE_OUTER_SPINE_EXCLUSION.md: b39b63f4e7b457359fe541f7224435e8e44f24e4b9a08b1c8e2348c61da5ce81
- TWO_SINGLETON_INNER_BLOCKS_EXCLUSION.md: 5599ae57a9e90a6dde17a77cd2b01c6009f026970b2df10275dc7a6f6afc056f
- verify_single_outer_spine.py: 142bdb92b5333d00af65ef48bd5411f6635130d9db9a936e2bc4ad83f6a06af8
- verify_two_singleton_inner_blocks.py: 65327bcae06e337616d585a7848f45151a10c5b35af20146ecace9c404347ae8
- verification.json: 4f8a1799eac7b5ebb18e1eb266ff0326d9dfe617a055529674a5a2b9dab4ef2a
- two_singleton_inner_blocks_verification.json: 6fe8f44724ddb9827841216aef85f1da4d75cb72f5354c32afe6ef7ca104abd6

The generalized-shuffle proof dependency is the separately accepted source e522a13a63f73a58c1af862e603c3b90c46084a1f83b3b79da7e6bd3d6b0a8d3. The earlier S113 and structural prerequisites remain explicit dependencies.
