# Independent audit: finite additive representatives

Date: 2026-10-10. Verdict: **PASS**, subject only to the exact source-version binding below. No unresolved mathematical defect was found. This is an additive approximation theorem, not an exact threshold or uniform strict-counterexample theorem.

## 1. Version-bound result

Audited source: `../finite_epsilon_representative.md`.

Source SHA-256: `3cc5606209bad491a52c3591e2ed337f04748b4e4f267e7298aa3b84327ebfe5`.

An exact copy is saved as `proof_audited_snapshot.md`. The local-probability prerequisite has independently passed audit:

- `../local_decay/local_probability_decay.md`, SHA-256 `7eaf6b449270286010b98b2e0725b8fbaec21bbe641dcd0e270fcc4a4628c14b`.
- `../local_decay/independent_audit/independent_audit.md`, SHA-256 `9d1806231cfc43a8dfcd9d179c2d4145265864b24783703e648b390e1482d858`.

The finite-representative proof conservatively uses only the prerequisite's induced-window Theorem 2, twice at tolerance epsilon/2. Its validity does not depend on the separately proved direct two-environment boundary variant. The source, prerequisite, audits, independently implemented test script, exact results, and run log are bound by `audit_manifest.json` and `SHA256SUMS`.

For integer D>=2, rational epsilon>0, R=2D-1, and a radius B obtained from the displayed exact integer test, the conclusion passes:

    |P'| <= min(|P|, q+2*2^(R(q-1))-2),
    |delta(P')-delta(P)| <= epsilon,
    q=2B+3R+6.

Every nonchain has a nonchain representative. The one-sided unmarked variant and the finite-infimum approximation also pass within their stated scopes.

## 2. Probability prerequisite and effective quantifiers

The proof does not assume uniformity after deleting points from a random extension. It compares a complete-poset probability with the actual uniform-extension probability of its induced B-window, under the independently established error bound. For two isomorphic windows, the induced probabilities agree exactly. Two comparisons of error epsilon/2 give one final-versus-original pair comparison of error epsilon. There is no sum over intermediate deletions or graph cycles.

With C=(2D)!/D!, M=(2D)!, and tau=(M-1)/(M+1), the exact condition

    2(C-1)(M-1)^m <= epsilon*(M+1)^m

implies (C-1)tau^m<=epsilon/2, hence tanh((log C)tau^m)<=epsilon/2. Since 0<tau<1, some nonnegative integer m exists and may be found by exact rational arithmetic. The radius B=2D(m+1) matches the prerequisite precisely. No unsafe rounding or unproved computable modulus is needed.

For an arbitrary positive real epsilon the claim is existential: choose a positive rational epsilon_0<=epsilon. The effective finite calculation is stated for rational input (or a computably supplied sufficient rational tolerance). No algorithm that extracts a rational lower bound from an unspecified real number is asserted.

## 3. Encoding and local legality

An incomparable pair i<j has span at most 2D-1. Every intermediate label is incomparable with at least one endpoint; the endpoints together have at most 2(D-1) other incomparable neighbors. Thus all longer pairs are comparable in the reference direction.

The backward-bit encoding correctly determines both directions of every induced relation: for i<j, the bit is read in the later letter b_j at offset j-i. A comparison within a matched word interval never needs a bit whose other endpoint lies outside that interval. In particular a matching block need not identify external backward bits for the induced-order comparison.

The retained original prefix has q-1>=R letters. Therefore all out-of-range bits at the actual beginning remain correctly zero. No right-end padding is required: nonexistent later neighbors are omitted.

Any failure of transitivity is a triple i<j<k with i<j and j<k comparable but i and k incomparable, so it lies in at most R+1 consecutive labels. Any degree violation at v is visible inside its full actual radius-R neighborhood, of size at most 2R+1. A matching original q-gram lifts every such violation, since q>=2R+1. An original witness may have additional neighbors beyond the lifted interval; that only increases its degree and cannot invalidate the contradiction. Antisymmetry is automatic from the reference orientation.

This establishes legality of the compressed word. There is no assumption that compression preserves an induced subposet of the original poset.

## 4. Marked directed-graph compression and size

The graph consists of actually occurring (q-1)-grams as vertices and actually occurring q-grams as edges. There are at most S<=A^(q-1), A=2^R, vertices. The original word supplies paths from its initial state to the selected edge's tail and from that edge's head to its final state.

Each shortest path has at most S-1 edges, including a zero-edge path when the endpoints agree. Keeping the marked edge between them gives at most 2S-1 edges, so the output length is at most q+2S-2. The forced edge also gives output length at least q, even for a loop. The sum of the two shortest-path lengths is no greater than the corresponding two pieces of the original walk, proving n'<=n. Shared vertices or overlaps between the shortest paths do not cause an issue; a walk, rather than a simple complete path, is sufficient.

Every sliding q-gram of the reconstructed output is one of its traversed edge labels. This applies at newly joined portions as well. Its initial and final states are exactly the original prefix and suffix of length q-1.

The unmarked shortest path has at most S-1 edges, giving q+S-2. When initial and final states coincide, its length can be zero and the output length is q-1. The source treats this separately as an original induced prefix; it does not incorrectly assume that a q-gram still exists.

Short inputs, chains, and the marked loop case are all handled. No hidden nonempty-input assumption conflicts with the empty-poset convention.

## 5. Every new pair has one original witness

Write the new pair as i<j. Its span is at most R, and every relevant output has

    n'>=q-1=2B+3R+5>2B+R+1.

The left case i<=B+1 has j+B<=2B+R+1<q-1. Its entire B-window is in the common prefix; its left physical endpoint flag agrees, including exact contact i=B+1, and its right endpoint is strictly internal in both words.

The right case j>=n'-B is dual under translation by n-n'. Its whole B-window is in the retained suffix and its left endpoint is strictly internal. The left and right cases cannot overlap, since overlap would imply n'<=2B+R+1.

For the remaining interior pairs, the augmented interval [i-B-1,j+B+1] exists and has length at most 2B+R+3<q-1. It is contained in some output q-gram, whose original occurrence supplies a translated pair. The extra label on each side guarantees that both actual B-windows remain strictly interior, even if the q-grams themselves abut an endpoint. This resolves the exactly-touching endpoint ambiguity.

For an unmarked output of length q-1, the entire original prefix is the common block; the same extra margins give a valid interior witness without a q-gram. The original pair is truly incomparable because the relevant later-letter bit is inside the common interval.

Thus every final pair is compared directly with one lawful original pair, independently of how many cycles were deleted. Different final pairs need not share a common global embedding or original occurrence.

## 6. The reverse witness and the maximum

An exact maximum-balance original pair exists because a finite nonchain has a nonempty finite set of incomparable pairs. The selected q-gram contains its augmented clipped B+1 interval; its length is less than q, so such a containing q-gram always exists when n>=q.

If the maximizing pair is near an original endpoint, the retained prefix or suffix supplies the correctly aligned final copy. If it is interior, the forced marked edge supplies the full augmented interval and therefore both interior endpoint flags. The proof does not rely on a boundary-clipped pair being placed at an arbitrary new interior position.

The copied bit preserves an actual incomparable pair, so the representative is a nonchain. The function min(p,1-p) is 1-Lipschitz. The forward witnesses imply delta(P')<=delta(P)+epsilon, while this reverse witness implies delta(P')>=delta(P)-epsilon. Selecting an exact maximizer is effective by finite exact enumeration, although it need not be efficient.

For a nonchain-preserving one-sided conclusion, marking any incomparable pair suffices. A completely unmarked construction can remove every incomparable pair, so the source correctly does not use it for the infimum over nonchains.

## 7. Degenerate degrees and the finite infimum

For D=0 the class consists of chains; a one-point representative works except that the empty input remains empty. Its nonchain infimum is not claimed as an ordinary real number.

For D=1 the poset is an ordinal sum of singletons and two-point antichains. Every incomparable pair has exact probability 1/2; every nonchain has the two-point antichain as an exact representative. Thus N(1,epsilon)=2 is valid, while N(0,epsilon)=1 is consistent with the empty-input size bound.

The bounded-size nonchain class is finite up to labelled presentations, nonempty for N>=2, and has an exact rational minimum b_(D,N). The entire class has an infimum b_D, which need not be attained. Inclusion gives b_D<=b_(D,N). Applying the one-sided representative conclusion to a poset within any eta>0 of b_D, then letting eta tend to zero, gives b_(D,N)<=b_D+epsilon. The source's proof therefore does not assume an infinite-class minimizer.

Exact finite enumeration provides the interval [b_(D,N)-epsilon,b_(D,N)]. This is a valid computability statement with an explicit modulus, not a practical algorithm. An additive approximation does not decide exact equality to 1/3, provide a uniform positive margin, or give a degree-only bound for strict counterexamples.

## 8. Independent executable checks

Run:

    python check_compression.py

The script is independent of the author's test implementation and imports no project poset solver. It builds genuine natural-labelled posets, validates transitivity and degree, implements its own marked graph compression, and computes all actual incomparable-pair probabilities with integer ideal dynamic programming and exact rational arithmetic.

The reproducible seed is 948013. The checks cover:

- 37 families, including connected path-incomparability posets, repeated adjacent-incomparability patterns, interval-order families, and random bounded-inversion-degree permutation posets.
- 93 marked compressions, 54 of which strictly shorten the input; input sizes up to 561.
- True maximum-balance pair selections, endpoint pair selections, and interior pair selections. There are 34 left, 31 right, 22 interior, and 6 unchanged short selected-pair cases.
- Full legality, correct beginning padding, prefix/suffix equality, all output q-grams occurring originally, graph-size bound, n'<=n, and preservation of the selected incomparable pair.
- Exact matching induced B-windows and physical endpoint flags for every final incomparable pair, including both endpoints and new interior joins.
- Exact original and final delta values. For true maximizing selections, the observed absolute delta change is at most the maximum of the forward pair-witness errors and the selected reverse-witness error, as required by the proof.
- Nine further unmarked zero-edge cases with n'=q-1, explicitly checking left, right, and interior witnesses despite the absence of any output q-gram.

All 4,727 final-pair witness checks pass (4,572 marked/short plus 155 unmarked zero-edge). All selected reverse witnesses pass. Test tolerances B are deliberately small and varied; these are structural and exact finite-law checks, not claims that an arbitrary tested B satisfies a chosen epsilon-decay target. The universal epsilon bound comes from the proved and independently audited prerequisite.

The author’s separate supplementary script was also rerun successfully: 70 genuine-poset cases, all 597 valid R=1 degree-one words on lengths 5 through 12, 87 zero-edge outputs, and the explicit negative control in which unmarked compression erases the sole incomparable pair. Its original exact-output hash remained unchanged. The report’s primary independent tests above use a separate implementation.

Finite testing supplements the proof; it cannot establish the all-n assertion by itself. No publication, external upload, repository modification, or threshold-resolution claim was made in this audit.

## 9. Final disposition

**PASS** for the version-bound finite additive representative theorem, explicit effective constants, nonchain preservation, one-sided unmarked variant, degenerate cases, and additive finite-infimum approximation. The local-decay prerequisite has itself passed independent audit. No unresolved mathematical defect remains in the reviewed argument. Bounds are deliberately conservative and no novelty determination is claimed.
