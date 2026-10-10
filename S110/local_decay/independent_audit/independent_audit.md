# Independent audit: uniform finite-window pair-probability approximation

Date: 2026-10-10. Verdict: **PASS** for the fixed proof version below.

The audit establishes no exact pumping statement, uniform strict-counterexample size bound, or resolution of the 1/3–2/3 conjecture. The finite checks are supplementary validation, not a substitute for the proof for arbitrary finite posets.

## 1. Fixed version and outcome

Audited proof: `../local_probability_decay.md`.

SHA-256: `7eaf6b449270286010b98b2e0725b8fbaec21bbe641dcd0e270fcc4a4628c14b`.

Theorems 1, 1B, and 2, their constants, the clipped-endpoint treatment, the local-size estimate, the degree-zero/one cases, and the Section 6 conditional certificates all pass independent mathematical review. No unresolved mathematical defect was found. One overbroad diagnostic sentence about threshold ambiguity and one rank-guard sentence were clarified before this final version was hashed; neither correction changed a theorem or a certificate inequality.

The audit's exact script, output, log, and this report are version-bound by `audit_manifest.json`. The independently established cut-profile input has SHA-256 `06cb5f863b4055a5779160a7a07bf18908f089f7a54de872d6cd4f1e067acd31`; its passing audit has SHA-256 `93b662051614fae0c42d4567783544f9c111038cfcfe6db01639bb643864abbb`. The positive-block source observation in Section 7 of `single_splice_stability.md` has SHA-256 `d537434e9bfc71e6c94cad9148e78e37b8075d40239face596fef96308737a22`; the audited proof establishes that observation again directly.

## 2. Exact hypotheses and constants

Every poset is finite, and its labels come from a genuine reference linear extension. The integer D bounds each vertex's total incomparability degree in the entire poset. It may exceed the actual maximum. For D>=1, the constants are

    C=(2D)!/D!,  M=(2D)!,  tau=(M-1)/(M+1).

For m>=0, two full matching induced relation windows

    [x-2D(m+1), y+2D(m+1)]

around translated designated actual pairs have probability difference at most

    tanh((log C) tau^m).

All relations, including incomparabilities, must match, not merely an encoding fragment or an abstract unlabelled poset. Ranks must shift by the same translation as labels.

Theorem 1B is a sufficient endpoint convention: the translated clipped domains match, their relations match, and physical-left/physical-right endpoint flags agree. This convention is conservative; it is not an extra restriction on Theorem 1's full untruncated intervals. An actually clipped endpoint cannot silently be compared with unrelated missing context.

For the induced-window theorem, Q is the actual induced subposet on the displayed interval after clipping to P's endpoints. It retains the designated actual vertices. It automatically still has incomparability degree at most D. Its uniform extension law need not be the deletion law of a uniform extension of P.

## 3. Independent proof verification

### 3.1 Legal supports, varying cardinalities, and initial distance

For any extension, rank(v) is its number of predecessors plus one plus the number of earlier incomparable vertices. Thus its rank differs from its reference label by at most D. A rank-r ideal contains every label <=r-D and no label >r+D, with physical clipping. Removing its forced prefix core gives exactly the legal fixed-cardinality ideals of the induced guard window. Conversely, a window ideal together with that prefix core is a global ideal, because any predecessor outside the window must have a smaller reference label and lies in the core.

This identifies the complete legal support under matching windows. It does not identify every potential mask, and does not require a fixed number of states as the rank varies. Unmarked genuine prefix and suffix counts are strictly positive on these supports. The input ratio theorem bounds each one's within-vector coordinate ratio by C.

Consequently, for any two genuine profiles on an identified support, the maximum coordinatewise quotient divided by its minimum is at most C^2. Their Hilbert log-oscillation is therefore at most 2 log C. Normalizing each profile separately does not change that distance. No claim of a finite exact set of possible profiles is needed.

### 3.2 Positive rectangular blocks

Let J be any genuine rank-r ideal and K any rank-(r+2D) ideal. The guards imply

    J subset [r+D] subset K.

Thus J is contained in K. The legal middle paths are in bijection with the extensions of the 2D-point induced poset K\J. Concatenation with an extension of J is legal because J is an ideal, and no predecessor of a point in K lies outside K because K is an ideal. Hence every block entry is an integer between 1 and (2D)!=M.

This works when the matrix is rectangular and when its legal supports have different cardinalities. The full block is positive on its two actual supports, even though the one-step matrices can have zeros. Illegal masks are not inserted as zero coordinates in the positive cones.

### 3.3 Self-contained contraction and its constant

For a positive matrix A with entries in [1,M], interpolate u and v by z_i(t)=v_i exp(t log(u_i/v_i)). The derivative of log(sum_i z_i(t)A_ij) is the expectation of log(u_i/v_i) under the normalized j-column weights. The j-column distribution is a reweighting of the k-column distribution by A_ij/A_ik in [1/M,M].

For any probability law reweighted by factors in [l,u], maximizing an event's probability change over its old mass and the conditional factors gives total variation at most

    (sqrt(u)-sqrt(l))/(sqrt(u)+sqrt(l)).

With l=1/M and u=M this equals (M-1)/(M+1)=tau. The difference of expectations of a function is at most its oscillation times total variation. Integrating the column-derivative difference therefore gives

    h(uA,vA) <= tau h(u,v).

Transposition gives the backward version. This proves the required rectangular-matrix contraction without an external Birkhoff theorem. Applying it over m common positive blocks to lawful initial profiles gives 2(log C)tau^m at each central boundary. One-coordinate supports are harmless: their Hilbert distance is zero.

### 3.4 Correct rank guards and actual events

For the interior theorem choose

    a=x-D-1, b=y+D, s=a-2Dm, t=b+2Dm.

The union of all relation guards for transfers from s through t-1 is exactly

    [s-D+1,t+D]=[x-2D(m+1),y+2D(m+1)].

There are exactly m blocks from s to a and m from b to t. Neither designated actual point can have appeared by a, since rank(x)>=x-D=a+1 and rank(y)>=y-D>a. Both have appeared by b, since their upper rank bounds are <=b.

A central atom is a legal middle output sequence together with its starting and ending states J,K. Its unnormalized weight under the genuine full-extension law is exactly F_a(J)B_b(K). Summing these weights gives the full extension count; no conditional completion weight is discarded. The corresponding atom in the other poset has the same middle sequence under translation and its own genuine boundary weights.

The log-ratio oscillation of the two atom weights is at most the sum of the two boundary Hilbert distances, at most 4(log C)tau^m. The sharp reweighting inequality converts this to

    tanh((4(log C)tau^m)/4)=tanh((log C)tau^m).

Pair direction is an event of this common atom space, so the same bound applies. Marked event counts may vanish; no positivity or contraction is asserted for marked counts themselves.

### 3.5 Clipped endpoints and the sharper one-sided result

For Q=P[[A,B]], set z=A-1 and N=B-A+1. If A>1, Q's pair label is x'=2D(m+1)+1. Its central left cut is (2m+1)D; its starting cut D has a full guard [1,2D]. They differ by exactly 2Dm. The corresponding P cuts are shifted by z, and the transfers agree. Thus even an endpoint introduced by deletion has m complete positive blocks before the central segment. The right-side calculation is dual: t_Q=N-D and t_Q-b_Q=2Dm when B<n.

If A=1, the relevant genuine prefix ideals are the same in P and Q: they lie below x, inside the retained interval, and have identical induced orders. If the central cut is zero, both prefix profiles are the singleton value 1. Thus this side contributes exactly zero. If B=n, the relevant genuine suffix complements agree, including the empty-complement case, and this side also contributes zero.

Only the k actually removed sides contribute. The combined bound is therefore tanh((k/2)(log C)tau^m). Theorem 1B uses the same proof: matching left endpoints forces translation zero there; matching right endpoints forces the total sizes to differ by the label translation. Genuine prefix or suffix counts then agree on the aligned endpoint side. The m=0 case uses the initial lawful-profile bound without requiring a positive-length propagation. If no points are removed, equality is exact.

### 3.6 Local size, degenerate D, and threshold certificates

For incomparable x<y, each label strictly between them is incomparable with at least one endpoint. Each endpoint has at most D-1 other incomparable neighbors. Hence y-x<=2D-1, so the retained interval contains at most (4m+6)D points.

D=0 is a chain and does not use a zero-length positive-block argument. For D=1, incomparable pairs are disjoint consecutive-label pairs, and the poset is an ordinal sum of singletons and two-point antichains. Swapping either order gives exact probability 1/2, preserved in any induced subposet containing the pair.

Section 6's interval and closed balancedness certificates are correct. In particular q-E>=1/3 and q+E<=2/3 allow equality. Strict unbalancedness requires min(q,1-q)+E<1/3. The corrected diagnostic sentence concerns an interval genuinely straddling a threshold; it no longer incorrectly labels endpoint equality as always inconclusive.

The optional rational upper bound min(1,(C-1)tau^m) is sound because tanh z<=z and log C<=C-1. It permits exact rational target tests without unsafe floating-point narrowing. Exponential approximation still provides no uniform sign gap at 1/3 and no degree-only finite counterexample bound.

## 4. Independent exact computations

Run from this directory:

    python check_local_decay.py

The script imports no existing project solver or transfer implementation. It enumerates full ideals and genuine extension paths directly, using arbitrary-precision integers and exact rational arithmetic.

### Exhaustive positive-block checks

- All 5,232 naturally labelled posets on n=0,...,6 are independently generated by adjoining each new maximum reference label with each legal predecessor ideal.
- For every applicable minimal positive degree bound, 1,357 full 2D-step blocks are checked.
- All 1,933 entries are positive and at most (2D)!; containment of every initial ideal in every terminal ideal is checked directly.
- 234 entries on n<=5 are independently recounted by literal permutations of the difference set.
- All 38 incomparable pairs in the enumerated degree-one posets have exact probability 1/2.

### Actual pair-law checks

There are 73 actual-poset comparisons. They cover genuine D=1,2,4,6 families, a loose D=10 bound exceeding the example size, m=0,1,2,4,8,10,50, translated interiors, left/right/both aligned endpoints, changing legal support sizes, and 45 induced-window comparisons. All four combinations of exact/nonexact endpoint sides occur. A chain also checks the D=0 description.

The script checks common one-step matrices directly 1,824 times. It checks central unmarked and direction-marked path matrices in both environments, exact extension-count factorization, and exact agreement of central marked counting with a separate global count that records the first designated endpoint's emission and weights it by its genuine suffix completion count.

If e is the exact observed probability difference and R is the exact product of the forward and backward coordinate-ratio ranges, the sharp reweighting bound is tested without square roots through

    (1+e)^2 <= R(1-e)^2.

The displayed theorem bound is also certified without floating-point transcendental comparisons. For k nonexact sides let

    z = k(C-1)/(C+1) * tau^m.

Since log C>=2(C-1)/(C+1) and tanh z>=z/(1+z) for z>=0, z/(1+z) is a rigorous rational lower bound on the theorem's k-sided error allowance. The exact observed error is checked to be at most that lower bound. This is a sufficient test of the stated bound; it does not claim that this lower bound is sharp.

Every test passes. The largest observed error is approximately 0.0141569656882, in the D=4, m=0 induced-window test. The two-sided D=2, m=50 test has a nonzero exact error approximately 1.14267e-86. The varying-support example uses support cardinalities 1 and 2. Full exact fractions and case parameters are in `exact_checks.json`.

## 5. Limitations and final assessment

The universal proof is the reason the theorem holds for unbounded n and D; the finite tests do not establish that by themselves. The tests are genuine-poset tests, not arbitrary positive-matrix examples or a reset deletion experiment. The result controls actual designated pair probabilities through common central path laws and true completion weights. It does not permit inversion of transfers, assume positive marked coordinates, produce finitely many exact profiles, or preserve a strict threshold without a margin.

Final assessment: **PASS for the version-hashed local approximation theorems and stated conditional certificates, within their explicit scope.**
