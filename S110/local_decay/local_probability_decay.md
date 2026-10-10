# Uniform finite-window approximation of actual pair-direction probabilities

Date: 2026-10-10. Status: proof statement; independent audit status is recorded separately.

This is a quantitative locality result for the uniform law on genuine linear extensions of a finite poset. It is not an exact pumping theorem, a proof of the 1/3–2/3 conjecture, or a uniform finite bound on strict counterexamples.

## 1. Constants and principal conclusions

Let P be a finite poset, with a fixed reference linear extension labelled 1,...,n. Suppose every point is incomparable with at most D other points. For D>=1 set

    C_D = (2D)!/D!,
    M_D = (2D)!,
    tau_D = (M_D-1)/(M_D+1),
    epsilon_D(m) = tanh((log C_D) tau_D^m),       m=0,1,2,... .

Write p_P(x,y) for the probability that the actual point x precedes the actual point y in a uniformly random linear extension of P. All logarithms are natural.

### Theorem 1: comparison of two lawful environments, interior version

Let P and Q be two finite reference-labelled posets of maximum incomparability degree at most D. Let x<y be labels of P, and let x'=x+c, y'=y+c be labels of Q for an integer shift c. Suppose the two full intervals

    I_P = [x-2D(m+1), y+2D(m+1)],
    I_Q = I_P+c

lie inside the respective label sets. Suppose translation by c identifies the complete induced partial orders on these intervals, including all comparisons and incomparabilities. Then

    |p_P(x,y)-p_Q(x',y')| <= epsilon_D(m).

The environments to the left and right may otherwise differ arbitrarily, provided both complete posets satisfy the assumptions. The number of points outside the common window is unrestricted. The two posets may have different total sizes and different numbers of points before the window.

This theorem as stated uses untruncated windows. Merely clipping a comparison window to the end of one poset does not justify comparison with an unrelated environment in the other poset. A clipped side may be used only when the corresponding physical endpoints are aligned, as in the induced-window corollary below.

### Theorem 1B: sufficient endpoint-aware comparison

Write n_P,n_Q for the two total sizes, L=2D(m+1), and set

    A_P=max(1,x-L),       B_P=min(n_P,y+L),
    A_Q=max(1,x'-L),      B_Q=min(n_Q,y'+L).

Suppose translation by c identifies the two clipped intervals and their complete induced partial orders. In addition require matching physical-endpoint flags:

    A_P=1 if and only if A_Q=1,
    B_P=n_P if and only if B_Q=n_Q.

Then the same probability comparison holds. More precisely, with

    k=1_{A_P>1}+1_{B_P<n_P},

the error is at most tanh((k/2)(log C_D)tau_D^m). These endpoint flags are a sufficient convention for clipped comparisons; they are not additional requirements on the untruncated Theorem 1.

### Theorem 2: computable local approximation, including boundary pairs

For any pair x<y in P and any integer m>=0, define

    A = max(1, x-2D(m+1)),
    B = min(n, y+2D(m+1)),
    Q = P[[A,B]],

and retain the actual point identities when computing the uniform-extension probability p_Q(x,y). Then

    |p_P(x,y)-p_Q(x,y)| <= epsilon_D(m).

More precisely, let k be the number of sides on which points are removed: k=1_{A>1}+1_{B<n}. The upper bound can be replaced by

    tanh((k/2)(log C_D) tau_D^m).

Thus a side with no removed points contributes exactly zero error. If k=0, Q=P and the result is exact.

If x and y are incomparable, then y-x<=2D-1. Consequently Q has at most

    (4m+6)D

points. In particular, every actual pair-direction probability in this class has an approximation, with a rigorously bounded error tending exponentially to zero, that is computable from a bounded reference-label window. This statement concerns the uniform law of the smaller induced poset; it does not assert that deleting points from a uniform extension leaves a uniform extension.

For D=0 the poset is a chain, all pair directions are deterministic, and there are no incomparable pairs. For D=1 every incomparable pair has direction probability exactly 1/2, both globally and in every induced subposet containing the pair. The displayed general bounds are valid for D=1 but are unnecessary and non-sharp there.

## 2. Genuine ideal profiles and exact local transfers

At output rank r, let I_r(P) be the set of all size-r ideals of P. For J in this set, define the genuine unmarked counts

    F_r(J)=e(P[J]),      B_r(J)=e(P\J).

The extension count e(empty)=1. Both counts are positive on every legal state.

An elementary rank identity is

    rank_sigma(v) = |{u:u<_P v}|+1
                    + |{u:u parallel_P v and u precedes v in sigma}|.

Comparing two extensions shows that the position of v changes by at most its incomparability degree. In particular,

    |rank_sigma(v)-v|<=D.

Every ideal extends to a complete linear extension, so every J in I_r obeys

    [max(0,r-D)] subset J subset [min(n,r+D)].

For an interior rank D<=r<=n-D, encode J by S=J\[r-D], a D-element ideal in the induced window [r-D+1,r+D]. Conversely every such window ideal gives a genuine global ideal. The analogous clipped statement uses the selected cardinality min(r,D) and the clipped window. The complete legal support is therefore local; different global environments have the same support whenever these windows and their endpoint conventions agree.

The established, independently audited cut-profile bound gives

    max_J F_r(J)/min_J F_r(J) <= C_D,
    max_J B_r(J)/min_J B_r(J) <= C_D.                   (2.1)

This remains true at clipped ranks. It is a statement on the legal support only. For reference, it follows from the following insertion argument. Every ideal has a common core [max(0,r-D)] and at most D added points. In a fixed linear extension of the core, an added point can precede at most D core points, because all such points must be incomparable with it. Thus all insertions occur among the last D core points, giving a fiber size between 1 and (2D)!/D!. Sum over core extensions. Reverse the order to obtain the suffix bound. No equal-fiber or uniform-deletion assertion is used.

Let T_r(J,K)=1 if J subset K for J in I_r and K in I_{r+1}, and 0 otherwise. Then, with F a row vector and B a column vector,

    F_{r+1}=F_r T_r,         B_r=T_r B_{r+1}.          (2.2)

The local descriptions of the two supports and the inclusion test show that T_r depends only on the relations on [r-D+1,r+D+1], with actual endpoints clipped when necessary. After a translation of reference labels, ranks must be translated by the same integer. This is a transfer identity, not an identification of the entire global ideals: the forced prefix cores may have different sizes.

### Uniformly positive 2D-step blocks

If 0<=r<=n-2D, every J in I_r and K in I_{r+2D} satisfies

    J subset [r+D] subset K.

Therefore the entry (J,K) of T_r...T_{r+2D-1} is exactly e(P[K\J]). The difference has 2D points, so

    1 <= (T_r...T_{r+2D-1})(J,K) <= M_D.              (2.3)

The matrix is rectangular when the two legal supports have different cardinalities; positivity holds between every pair of legal states. Illegal masks are not inserted into the matrix. Each one-step transfer has no zero row or column because every ideal has a legal next step and every nonempty ideal has a legal preceding step.

## 3. Two elementary probability and projective lemmas

### Lemma 3.1: bounded reweighting

Let a probability law on a finite set be reweighted by positive factors t(omega) in [l,u]. The total variation distance between the original and normalized reweighted laws is at most

    (sqrt(u)-sqrt(l))/(sqrt(u)+sqrt(l))
      = tanh((log(u/l))/4).                           (3.1)

Here total variation is the supremum of the absolute probability differences over all events. To prove the inequality, fix an event of old probability p. Let alpha and beta be the conditional averages of t on the event and its complement. Its new probability is

    q = p alpha / (p alpha+(1-p) beta).

For an upward change, the largest possible q occurs at alpha=u, beta=l. Maximizing q-p over 0<=p<=1 gives (sqrt(u)-sqrt(l))/(sqrt(u)+sqrt(l)). The downward case interchanges the event and its complement. Empty and full events have zero change. This proves (3.1) without any positivity requirement for event-refined counts.

### Lemma 3.2: positive rectangular matrices contract projective distance

For positive vectors u,v on a common finite support, define

    h(u,v) = max_i log(u_i/v_i)-min_i log(u_i/v_i).

This is unchanged by separately scaling either vector, so it applies equally to their separate l1 normalizations. Let A be any rectangular matrix with entries in [1,M], where M>=1. For positive row vectors u,v,

    h(uA,vA) <= ((M-1)/(M+1)) h(u,v).                (3.2)

The same result applies to column vectors by transposition.

Here is a self-contained proof. Put f_i=log(u_i/v_i), z_i(t)=v_i exp(t f_i), and

    g_j(t)=log(sum_i z_i(t) A_ij),      0<=t<=1.

Then g'_j(t) is the expectation of f under weights

    w_i^j(t) = z_i(t) A_ij / (sum_l z_l(t) A_lj).

For columns j,k, the j-weights are obtained by reweighting the k-weights by A_ij/A_ik, which lies in [1/M,M]. Lemma 3.1 gives

    TV(w^j(t),w^k(t)) <= (M-1)/(M+1).

The difference of expectations of a function is bounded by its oscillation times total variation. Hence

    |g'_j(t)-g'_k(t)| <= ((M-1)/(M+1)) osc(f).

Integrate from 0 to 1 and maximize over j,k. This proves (3.2). One-coordinate supports cause no problem: their projective distance is zero. More generally, multiplication by a nonnegative matrix with no zero output coordinate is projectively nonexpansive, since each output ratio is a weighted average of input ratios.

Thus no external version of the Birkhoff contraction theorem is being assumed.

### Consequence for lawful boundary profiles

If two true profiles live on an identified legal support, (2.1) implies

    h(F,F')<=2 log C_D,       h(B,B')<=2 log C_D.     (3.3)

Indeed each profile has its own within-vector coordinate ratio at most C_D; their cross-ratio can therefore be at most C_D^2. After m common 2D-step blocks, (2.3) and (3.2) give

    h(F_out,F'_out)<=2(log C_D) tau_D^m,             (3.4)

and analogously for suffix profiles propagated backwards. Arbitrary lawful environments are allowed at the starting cuts. Their individual normalized vectors need not be identical, rational with bounded denominator, or drawn from a finite set.

For genuinely arbitrary nonzero nonnegative vectors, rather than lawful profiles, one positive block first makes both images positive with coordinate ratios at most M_D. Thus m>=1 common blocks give the weaker universal bound 2(log M_D) tau_D^(m-1). The main theorems use the stronger lawful-profile estimate (3.4).

## 4. Proof of Theorem 1: output-rank and actual-identity bookkeeping

In P choose the four output-rank cuts

    a = x-D-1,            b = y+D,
    s = a-2Dm,           t = b+2Dm.

In Q use a+c,b+c,s+c,t+c. The assumed full common interval is exactly

    [s-D+1,t+D] = [x-2D(m+1),y+2D(m+1)].

Because this interval lies inside both posets, all four cuts and all intermediate cuts have matching untruncated legal supports. The transfers from s through t-1 are identified by translation. There are exactly m positive blocks from s to a and exactly m from b to t. Apply (3.4) to obtain

    h(F_a^P,F_{a+c}^Q) <= delta,
    h(B_b^P,B_{b+c}^Q) <= delta,
    delta=2(log C_D) tau_D^m.                        (4.1)

The common central sample space consists of every legal sequence of output points between cuts a and b, including its starting and ending local states J,K. Translation identifies these sequences with those between cuts a+c and b+c in Q. If a sequence is not legal, it is absent from both sample spaces. On a legal sequence gamma, the weight induced by a uniformly random full extension of P, before normalization, is exactly

    w_P(gamma) = F_a^P(J) B_b^P(K).                 (4.2)

Every extension of the initial ideal, the specified middle sequence, and every extension of the final complement concatenate to a legal full extension, and every full extension is obtained once. In particular the sum of (4.2) is e(P). The corresponding Q weight is F_{a+c}^Q(J') B_{b+c}^Q(K'). These are the actual prefix and completion weights, not independently reset laws.

Across the common central atoms, the oscillation of log(w_Q/w_P) is at most the sum of the two distances in (4.1), namely 2 delta. Lemma 3.1 gives

    TV(central path laws) <= tanh((2 delta)/4)
                          = epsilon_D(m).           (4.3)

Finally, neither actual point has appeared by cut a: the rank of x is at least x-D=a+1, and the rank of y is at least y-D>a. Both have appeared by cut b: their ranks are at most x+D<=y+D=b and y+D=b, respectively. The same assertions hold for the translated actual points of Q. Their direction is therefore an event of this common central path space, and (4.3) proves the theorem. Nothing in the argument treats a moving mask position as if it were a fixed actual point.

## 5. Proof of Theorem 2: exact treatment of clipped endpoints

Set z=A-1 and relabel Q by 1,...,N, where N=B-A+1. Its designated pair is x'=x-z, y'=y-z. Use its central cuts

    a_Q=max(0,x'-D-1),      b_Q=min(N,y'+D),

and P's corresponding cuts a_P=a_Q+z, b_P=b_Q+z. The local state supports and the central transfers match. If a window is clipped at a physical endpoint, that same endpoint is present and aligned in P and Q; an endpoint introduced by deleting points is separated from the central segment by the full prescribed guard. Here are the explicit profile checks.

Left side:

- If A=1, then z=0. The genuine prefix ideals at a_P=a_Q are identical. If a_Q=0 the unique ideal is empty. Otherwise every such ideal has largest label at most a_Q+D=x-1<B, so it is entirely inside Q. The supports agree and F_{a_P}^P=F_{a_Q}^Q exactly. The left projective error is zero.
- If A>1, then x'=2D(m+1)+1 and a_Q=(2m+1)D. Start at s_Q=D and s_P=s_Q+z. The entire transfer segment from s_Q to a_Q consists of m common 2D-step positive blocks, and the necessary relation window starts exactly at Q's first label. Both starting ranks have complete legal D-windows. Estimate (3.4) bounds the left projective error by delta=2(log C_D)tau_D^m.

Right side:

- If B=n, the true complements at b_P and b_Q correspond identically. If b_Q=N they are empty. Otherwise every point in these complements has original label at least b_P-D+1=y+1>A. Thus the actual suffix counts agree exactly and the right projective error is zero.
- If B<n, then t_Q=N-D and t_P=t_Q+z. There are exactly m common positive blocks from b_Q to t_Q. Backward propagation from t_Q gives right projective error at most delta.

These assertions also cover m=0. A zero-length propagation just uses (3.3). The existence of an unremoved buffer on the other side ensures that a starting window is not incorrectly truncated; if neither side is removed then Q=P and no estimate is needed.

The designated points are absent at the two a-cuts and present at the two b-cuts, by the same rank guard as above or by the actual rank-0/rank-N endpoint. Apply the central-path argument (4.2) with total projective distortion at most k delta. Lemma 3.1 yields tanh(k delta/4), the stated sharper bound.

Theorem 1B follows by exactly the same argument for its two lawful environments. When the left physical endpoint is aligned, translation has c=0, and the entire prefix ideals relevant to the central cut are contained in the common interval; their induced orders and prefix counts are identical. When the right physical endpoint is aligned, n_Q=n_P+c, and the entire relevant suffix complements correspond under translation with identical suffix counts. On each non-endpoint side there are m common positive blocks as above, and (3.4) applies. Matching the endpoint flags ensures that no truncated ideal window is silently identified with an untruncated one.

For the size assertion, suppose x parallel_P y and x<y. Every label v strictly between them must be incomparable with at least one of x,y: otherwise natural labelling gives x<_P v<_P y, a contradiction. Each endpoint has at most D-1 incomparable neighbors other than the other endpoint. Hence

    y-x-1<=2(D-1),       y-x<=2D-1.

The unclipped window length is y-x+4D(m+1)+1, at most (4m+6)D; clipping only reduces it.

## 6. Finite calculation, certified intervals, and the 1/3 barrier

Theorem 2 gives an entirely finite computation for each designated actual pair. Enumerate the linear extensions of Q, or use exact ideal dynamic programming, to obtain the exact rational

    q = p_Q(x,y).

Let E=epsilon_D(m), or use the sharper k-dependent error. Then

    p_P(x,y) is in [max(0,q-E), min(1,q+E)].        (6.1)

A safe numerical implementation uses a rigorous upper bound on E, so rounding never narrows this interval. The elementary bound E<=(log C_D)tau_D^m is sufficient and avoids evaluating tanh.

An entirely rational alternative is

    E_bar = min(1, (C_D-1) ((M_D-1)/(M_D+1))^m),

which is an upper bound because log C_D<=C_D-1. For a positive rational target eta, choose the first m for which

    (C_D-1)(M_D-1)^m <= eta (M_D+1)^m.

This is a terminating integer-arithmetic prescription, so the local approximation and its certificate do not rely on unverified floating-point transcendental evaluations.

For any 0<eta<1, a sufficient integer choice is

    m >= max(0, ceil(log((log C_D)/eta)/(-log tau_D))),

with exact or upward-certified evaluation. Thus the needed window has O_D(log(1/eta)) points. D=0,1 may instead use their exact descriptions below.

Conditional certificates are valid:

- If q-E>=1/3 and q+E<=2/3, then the designated actual pair is balanced in P.
- If min(q,1-q)-E>=1/3, the same conclusion follows.
- If min(q,1-q)+E<1/3, the designated actual pair is strictly unbalanced in P.
- If the interval (6.1) genuinely straddles a threshold, the interval alone does not decide on which side of that threshold the true value lies; increase m or use a different exact argument. Equality at an interval endpoint is handled by the closed-threshold certificates above.

For example, q in [1/3+gamma,2/3-gamma] and E<=gamma certifies a balanced actual pair. Equality is allowed here because balancedness is the closed condition [1/3,2/3]. In contrast, preserving a strict unbalancedness claim requires strict separation of its interval from both thresholds.

The non-strict 1/3 barrier remains. Exponential approximation alone does not turn a value arbitrarily close to 1/3 from below into a uniform sign certificate. A family of strict counterexamples could, as far as this theorem is concerned, have its maximum balance approach 1/3 with no uniform gap. The theorem neither supplies a uniform positive margin nor proves that a finite local collection decides the exact closed threshold. It therefore does not, by itself, prove the 1/3–2/3 conjecture or a degree-only finite bound for strict counterexamples.

If a fixed P is a strict counterexample, its finite set of actual incomparable pairs has an instance-dependent positive gap. An m chosen using that gap makes all the corresponding local intervals strictly unbalanced. This does not make m uniform in D. Conversely, locally proving a pair balanced with an explicit error margin is sound without any conjectural assertion.

## 7. Degenerate degree bounds and zeros

For D=0 all pairs are comparable and P is a chain. There is no 2D-step block to discuss, so the positive-block argument is not invoked.

For D=1 any incomparable pair has consecutive reference labels: an intervening label would be comparable with both endpoints and create a comparison by transitivity. Different incomparable pairs share no vertex. P is therefore an ordinal sum of singletons and two-point antichains. Flipping either order of a two-point antichain gives a bijection on full extensions, so p_P=1/2 for every incomparable pair. This remains true in every induced subposet containing it.

For arbitrary D, every unmarked F and B coordinate on a genuine legal support is positive. Illegal masks are omitted, not assigned artificial positive mass. The direction-refined transfer or event count may be zero, and no positive lower bound or projective contraction is asserted for that refinement. The proof first compares the unmarked boundary profiles, then compares the full central path laws and their events. That order is essential.

## 8. Input provenance and scope

The cut-profile estimate used above is established in the following source artifacts (paths relative to this file in the combined S110 research bundle):

- ../bounded_cut_profiles.md.
- Its independently passing audit is ../independent_audit/independent_audit.md.
- The positive-block observation also appears in Section 7 of ../single_splice_stability.md; it is proved again in Section 2 here.

All additional probability, matrix, support-alignment, output-rank, and endpoint arguments needed for the stated local approximation have been proved in this document. No external publication or repository change is made by preparing it.
