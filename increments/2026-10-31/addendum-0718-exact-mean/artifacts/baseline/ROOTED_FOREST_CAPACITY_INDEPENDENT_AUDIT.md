# Independent audit: rooted-forest comparison capacity

**Verdict:** the stated reference-distribution induction and the resulting sufficient comparison theorem are mathematically valid under the exact rooted-forest, upper-ideal, cross-incomparability, and external-window hypotheses. This review does not claim historical novelty or applicability to the filtered C2 residual class. The conclusion is based on the proof audit, not promotion of an unchecked draft or inference from finite experiments.

Audited source: `ROOTED_FOREST_CAPACITY_DRAFT.md`.

## 1. Definition, zero cases, and induction domain

Every recursive tree has positive integer total size n. For an anchor root, the child forest has n−1 vertices. By induction its capacity s satisfies 0≤s≤the number of child burden points≤n−1. Thus a nonzero root step always has 0<s<n. Capacities need not be integers; every use of Beta(1,s) permits arbitrary positive real s.

The capacity is zero exactly when that recursive subtree contains no burden point. Its actual first-burden reference variable is then defined as 1, and the comparison variable Y_0 is also 1. A zero-capacity component does not affect a forest minimum. If the whole forest is empty, the same empty-minimum convention gives 1.

If a root is in the upper ideal L, every descendant belongs to L, so the entire tree is in the exact all-burden case. There is no missing recursion branch. The formula ns/(n+s+1) is nonnegative and at most s; component addition then verifies 0≤κ≤|L|. Nonempty L gives κ>0.

The main statement assumes L nonempty. If one extends it to L empty, the desired first-occurrence inequality is immediate from first(M∪C)≤first(C), with the specified empty-set sentinel; no beta law with a zero shape parameter should be introduced.

## 2. Exact reference decomposition at an anchor root

For a rooted tree, the root is below all n−1 remaining points. Its fixed-coordinate cross-section is an affine copy of the deleted-root forest's unit order polytope, scaled in n−1 dimensions by 1−t. Hence the root marginal has density n(1−t)^(n−1), and its normalized remaining coordinate vector has a law independent of t. This proves both R~Beta(1,n) and the required independence of R from the normalized child forest. It is not merely a statement about the root's marginal distribution.

For a child first-burden variable Z, X=R+(1−R)Z exactly. If Z has the asserted truncated-mean domination, then for every fixed R=t<1,
min(t+(1−t)Z,z)=t+(1−t)min(Z,(z−t)/(1−t)).
The test cutoff can be any real number, so this identity also covers z<t or z>1. The zero-probability endpoint t=1 causes no issue. Independence makes the conditional law of Z the same law to which the induction applies; replace it by an independent Beta(1,s) variable and integrate. No unjustified replacement of a correlated variable is made.

These beta decompositions belong only to the uniform-window reference tree. Actual externally constrained root coordinates need not have these distributions; the final theorem correctly uses window comparison first.

## 3. Single-root transform, arbitrary real s, and equal-index limit

For independent R~Beta(1,n), Y_s~Beta(1,s), write W=1−AB with A=1−R~Beta(n,1), B=1−Y_s~Beta(s,1). Integrating their product gives, for u=1−t and n>s>0,
S_W(t)=(n u^s−s u^n)/(n−s).
This holds for noninteger positive exponents. Direct expectation gives
E W=(n+s+1)/((n+1)(s+1))=1/(1+ν),
ν=ns/(n+s+1).

The draft's survival ratio and derivative are correct:
r(u)=[n u^(s−ν)−s u^(n−ν)]/(n−s),
r'(u)=u^(s−ν−1)[n(s−ν)−s(n−ν)u^(n−s)]/(n−s).
Here 0<ν<s<n. The bracket strictly decreases from positive to negative, so r has one interior maximum. Since r(0)=0, r(1)=1, and r'(1)<0, the maximum exceeds 1 and there is exactly one additional interior crossing of 1. In the t direction, S_W−S_Beta(1,ν) is first positive and then negative. Its integrated difference starts and ends at zero, by equality of means, and stays nonnegative throughout. For z outside [0,1] the comparison follows from constants or equal means. This proves the required all-truncation comparison, not first-order stochastic domination.

**Equal exponents:** n=s never occurs in a valid nonzero recursive step because s≤n−1. There is therefore no hidden singularity in the theorem. If the standalone transform lemma is extended to n=s=a>0, its continuous limit is
S_W(t)=u^a(1−a log u),
ν=a²/(2a+1).
The ratio derivative has sign −ν−a(a−ν)log u, again changing from positive to negative exactly once; alternatively bounded-continuous parameter limits preserve every truncated expectation inequality. Thus the equality limit is well behaved, but it is not needed by this induction.

## 4. Forest composition and conditional independence

After deleting a root, actual components of a rooted-tree ancestor order have no comparisons between them. Their reference order-polytope domain is a Cartesian product, and the uniform volume law is a product. The corresponding first-burden variables are therefore independent, including any constant-1 components.

For each replacement, condition on the other independent variables. Their minimum together with the requested cutoff is a fixed scalar, so the one-variable truncated-mean comparison applies. Repeating gives the comparison with independent Beta(1,κ_i) variables. Their minimum has survival product (1−t)^(sum κ_i), as stated. This gives the induction's forest step for real capacities.

Extra comparisons or shared vertices between nominal children destroy this factorization. One must use the actual induced ancestor poset, including transitive comparabilities. It is not legitimate to retain an old branch decomposition after adding cross-branch edges. If the resulting induced order is still a rooted forest, its capacity must be recomputed from that new forest; otherwise this theorem is unavailable. A general undirected-tree Hasse diagram with converging incomparable ancestors is not enough.

## 5. Return to external windows and C2

The general-poset endpoint-monotonicity lemma was independently audited in `BARRIER_AND_FOREST_INDEPENDENT_AUDIT.md`. Its hypotheses apply to the actual rooted forest K because full predecessor/successor sets give isotone endpoint vectors. The full union/intersection external assumptions align every M window below a common reference window and every K window above it. Full K–M incomparability is required. Conditioning on R retains the actual coordinate-volume density; integrating against its true marginal avoids uniform-fiber errors.

The scalar cutoff min(C coordinates) is fixed after conditioning and may lie outside the common reference interval. The all-real-cutoff comparison and affine identity cover that case; empty C gives cutoff 1. If κ≤m, Beta(1,m) is stochastically no larger than Beta(1,κ), with κ=0 interpreted only as the point mass at 1. Combining the comparisons and the order-polytope first-rank identity proves the displayed extension-sum inequality.

For C2, L and M must be the entire actual sets, and K\\L must consist of genuine additional anchors. A partial cover of L does not prove the full-L first-occurrence inequality. All relations are checked in the full inherited Q order, not only within a proposed drawing of the forest. The result is a sufficient condition and gives no automatic strict inequality or general residual classification.

## 6. Example and relationship to earlier tools

For the four-point tree h0<l1 and h0<h1<l2, L={l1,l2}, the child capacities are 1 and 1/2. Thus s=3/2, n=4, κ=12/13. Its three extensions give first-L ranks 2,3,3, so the mean reference coordinate is 8/15. With an independent singleton M, direct shuffling gives 15 extensions and B=45,Z=48. All numerical statements in the demonstration are correct. The actual reference distribution is not asserted to be Beta(1,12/13); it merely dominates that comparison law in truncated means.

A prefix of q anchor-chain points followed by l all-burden points yields κ=l/(q+1) by this recursion, recovering the earlier chain budget. The current theorem treats additional partially ancestral rooted-tree shapes. It does **not** subsume every arbitrary H⊕L barrier: multiple incomparable H ancestors that converge on the same L vertices need not form a rooted forest. No historical-priority claim or no-VG/no-mixed-cycle/no-module applicability witness has been audited here.

## 7. Independent finite search

`independent_forest_capacity_check.py` enumerates 873 topologically indexed rooted forests of sizes 1 through 6 and all 18,815 nonempty upper-ideal burden selections. It computes κ exactly as a rational number. For the smallest integer m=ceil(κ), it independently enumerates actual extension ranks, forms the exact polynomial for the integrated survival function of the first-L coordinate, and compares it to Beta(1,m) at the ten rational cutoffs 1/10,…,1.

All **188,150 exact rational comparisons** pass. This checks the reference implication at finite samples and checks the recursive implementation; it is not proof of all real cutoffs, arbitrary sizes, or the noninteger comparison parameter. Those claims rest on the analytic induction audited above.

No repository or remote was changed; all new audit artifacts are in /tmp.
