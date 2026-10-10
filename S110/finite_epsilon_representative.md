# A finite additive representative theorem for bounded incomparability degree

Date: 2026-10-10. Status: **Proved using the independently audited local probability-decay theorem.** The finite-word argument below is self-contained; independent version-bound audits are recorded separately. No exact 1/3-threshold reduction, uniform strict-counterexample bound, or novelty claim is made.

## 1. Definitions and the exact prerequisite

A reference labelling of a finite poset P is a linear extension labelled 1,...,n. Its maximum incomparability degree is the maximum number of points incomparable with any one point. Put

    p_P(x,y) = Pr[x precedes y in a uniformly random linear extension of P],
    beta_P(x,y) = min(p_P(x,y), 1-p_P(x,y)),
    delta(P) = max_{x parallel_P y} beta_P(x,y).

Set delta(P)=0 for a chain, including the empty poset. The finite-infimum result below explicitly restricts to nonchains.

We use this prerequisite, denoted LD(D,B,epsilon). If two lawful degree-at-most-D reference-labelled posets have designated incomparable pairs whose clipped radius-B intervals are translation-isomorphic as induced posets, with the designated points identified, and with corresponding physical endpoint flags equal, then their actual directional probabilities differ by at most epsilon. The interval for x<y in a poset of size n is

    I=[max(1,x-B), min(n,y+B)].

The endpoint flags say whether the left end of I is the physical label 1 and whether the right end is the physical label n. An exactly touching untruncated interval has its corresponding endpoint flag set. Agreement of encoded bits pointing outside I is NOT required. The comparison is between the actual uniform-extension laws on the two complete posets.

For complete conservatism, LD follows from Theorem 2 of `local_decay/local_probability_decay.md` with error epsilon/2: compare each full-poset probability with the probability in its induced radius-B interval. The two induced laws are exactly isomorphic, so the triangle inequality gives epsilon. This is one comparison between one final pair and one original pair; there is no chain of intermediate splices and no length-dependent accumulation. The endpoint flags are a stronger condition than this two-projection derivation needs. A separately audited direct boundary-environment comparison with error epsilon can improve the radius but is not needed for the constants below.

Here is an entirely explicit, conservative choice, valid for D>=2 and positive rational epsilon. Set

    C=(2D)!/D!,    M=(2D)!,    tau=(M-1)/(M+1).

Let m be the least nonnegative integer satisfying

    2(C-1)(M-1)^m <= epsilon (M+1)^m,                 (1.1)

and put

    B=2D(m+1),
    R=2D-1,
    q=2B+3R+6,
    A=2^R,
    N(D,epsilon)=q+2 A^(q-1)-2.                      (1.2)

The integer m exists since 0<tau<1. Formula (1.1) is checked by exact rational arithmetic. It guarantees the local theorem's bound tanh((log C)tau^m)<=epsilon/2 because tanh(t)<=t and log C<=C-1. For arbitrary real epsilon>0, choose any positive rational epsilon_0<=epsilon and use N(D,epsilon_0). Alternatively, a certified-upward logarithmic choice of m can be used.

The extra one-label guard in the compression proof is intentional: a radius-B interval that exactly touches an endpoint must not be matched to one that does not. The conservative q in (1.2) accommodates this guard and every legality test. It is not optimized.

## 2. Main theorem

Assume LD(D,B,epsilon), with integer D>=2 and B>=0. Set R,q,A,N as in (1.2), using this B. For every finite reference-labelled poset P of maximum incomparability degree at most D, there is such a poset P' with

    |P'| <= min(|P|,N),
    |delta(P')-delta(P)| <= epsilon.                 (2.1)

If P is a nonchain, P' is a nonchain. Every incomparable pair of P' has an original incomparable pair in P with the same directional probability to error at most epsilon, by a single application of LD. An original maximum-balance pair also has a retained local copy in P', or an aligned endpoint copy, so that LD gives the other direction in (2.1).

Without preserving a maximum-balance pair, an unmarked construction gives the weaker one-sided conclusion delta(P')<=delta(P)+epsilon with

    |P'| <= q+A^(q-1)-2.

An unmarked construction can produce a chain and is consequently insufficient, by itself, for infima over nonchains.

For D=0 every poset is a chain; take the one-point chain when P is nonempty and the empty poset otherwise. There are no nonchains in this class. For D=1, every nonchain has delta(P)=1/2 and has the two-point antichain as an exact representative. Chains again have a representative of size at most one. Thus N(0,epsilon)=1 and N(1,epsilon)=2 work under the empty-poset convention, with exact error zero.

## 3. Finite-range encoding, including both directions and padding

For D>=1, an incomparable pair i<j in any reference labelling has

    j-i <= R=2D-1.                                  (3.1)

Indeed each intermediate label v must be incomparable with i or with j, or else i<v<j in the poset. Each endpoint has at most D-1 incomparable neighbors other than the other endpoint. Hence j-i-1<=2(D-1).

Encode position j by the R-bit letter b_j whose coordinate t, 1<=t<=R, is 1 precisely when j-t>=1 and j-t is incomparable with j. Coordinates with j-t<=0 are padded with zero. Thus the alphabet has A=2^R letters.

Decode any word of length n by putting, for 1<=i<j<=n,

- i parallel j if j-i<=R and coordinate j-i of b_j is 1;
- i<j otherwise.

No backward order relation is inserted. At positive offset t from i, its relation to i is read from coordinate t of the LATER letter b_(i+t). At negative offset -t it is read from coordinate t of b_i. Therefore matching a consecutive word block determines every induced pair relation inside the block, in both offset directions; it does not merely determine one-sided neighborhoods. Distances exceeding R are comparable in both decoded objects. Bits with an endpoint outside a matched block are not used to compare its induced poset.

The original word decodes exactly to P by (3.1). The compressed word retains the initial q-1 letters, so all actual beginning-padding coordinates remain zero; q-1>=R. There is no right-padding convention: symbols simply end at n, and nonexistent right-hand neighbors are omitted.

Legality has a finite witness:

- A transitivity violation i<j<k with i<j, j<k but i parallel k necessarily has k-i<=R, and is witnessed in R+1 consecutive labels.
- A degree violation at v is witnessed among the actual labels [max(1,v-R),min(n,v+R)], of length at most 2R+1.

Thus any decoded word whose consecutive windows of length at most 2R+1 lift to induced windows of genuine degree-at-most-D posets is itself such a poset. Antisymmetry is automatic from the reference orientation. For the degree argument, the lifted neighborhood need not include ALL possible neighbors of the original witness: the original degree is at least the number of lifted incomparable neighbors, which suffices.

## 4. Word compression with a marked original q-gram

The following is an elementary finite directed-graph argument. It is a standard de Bruijn-word construction, not a claimed new graph mechanism.

If n<q, retain P unchanged. Suppose n>=q. Form a directed graph whose vertices are the distinct (q-1)-letter consecutive words actually occurring in w=b_1...b_n. Each distinct occurring q-letter word is an edge from its first q-1 letters to its last q-1 letters. Keep an occurrence index for each edge when a witness is needed. Let s be the initial vertex, t the final vertex, and S the number of vertices. Then

    S<=A^(q-1).

The original word gives a walk from s to t.

For a chain there is no maximizer to preserve, and a one-point representative already suffices. Otherwise choose an original incomparable pair x<y attaining delta(P). Choose one original q-gram containing the augmented clipped interval

    J=[max(1,x-B-1),min(n,y+B+1)].                   (4.1)

Such a q-gram exists: |J|<=2B+R+3<q and n>=q; every interval of length at most q in a word of length at least q is contained in some q-gram. Mark that q-gram edge e:u->v, retaining the offsets of x and y in this chosen occurrence.

Take a shortest directed path from s to u, then e, then a shortest directed path from v to t. Both paths exist from the portions of the original walk before and after the chosen occurrence. Each shortest path has at most S-1 edges, including the zero-edge path when its endpoints agree. The combined walk has at most 2S-1 edges. Read its initial state followed by the final letter of each traversed edge to obtain w'. Its length n' satisfies

    q <= n' <= q-1+(2S-1)=q+2S-2<=N.               (4.2)

Moreover n'<=n: each of the two shortest paths is no longer than the corresponding part of the original walk. The marked edge is retained even if u=v; it is not removed as a cycle. This is exactly what prevents the possible loss of the selected incomparable pair.

The initial and final (q-1)-grams of w' are exactly those of w. Every q-gram of w' labels an edge in the combined walk and therefore occurs in w. This includes q-grams crossing every newly created join. The marked edge has a definite occurrence in w', and its full q-letter block agrees with the selected original occurrence.

For the unmarked variant simply take a shortest s-to-t path, of at most S-1 edges. Then q-1<=n'<=q+S-2. If s=t the zero-edge path is allowed, and n'=q-1. This zero-edge case must not be silently assumed to have a q-gram.

## 5. The decoded compressed word is lawful

Let P' be the decoding of w'. For the marked construction, n'>=q, so every interval of at most 2R+1 labels is contained in a q-gram of w', since q>=2R+1. That q-gram occurs in w. Its induced order is a translated copy of a genuine induced order of P, by Section 3.

A transitivity violation or a degree violation would therefore lift to P, contrary to its assumptions. This proves that P' is a genuine poset of maximum incomparability degree at most D. The numerical order is a reference extension.

For the unmarked zero-edge case, w' has length q-1 and equals the original prefix of that length. Its decoding is exactly the corresponding induced subposet of P, so it is lawful without a q-gram argument. If the input was short and left unchanged, legality is automatic.

Every new incomparable pair, including a pair spanning a newly created join, has new-label span at most R by the definition of the decoding. No longer-span cross-pair can be incomparable. There is no claim that a new incomparable pair's old retained endpoint identities were incomparable: the required witness is the translated local original pair, not an ancestry of physical retained points.

## 6. Every final pair has one original local witness

It remains to prove all boundary and neighborhood assertions used in LD. Consider n>=q and an arbitrary incomparable pair i<j of P'. Then j-i<=R. The marked construction has n'>=q; the argument also works for the unmarked zero-edge case n'=q-1. In all cases

    n'>=q-1=2B+3R+5>2B+R+1.                       (6.1)

Classify the pair as follows.

### Left boundary: i<=B+1

Use the retained initial q-1 letters, and use the same numerical pair i,j as the witness in P. Its radius-B interval ends at j+B<=2B+R+1<q-1. Hence it is fully covered by the common prefix. Its left endpoint is the physical label 1 in both posets, including the case i=B+1, while its right endpoint is strictly before both physical right endpoints. The clipped intervals, designated pair, induced relations, and endpoint flags therefore match exactly.

### Right boundary: j>=n'-B

Use the retained final q-1 letters and translate by n-n'. The radius-B interval lies inside that common suffix: its length is at most 2B+R+1, and its right endpoint is the physical right endpoint in both posets, including the exactly touching case j=n'-B. Its left endpoint is strictly beyond the physical left endpoints by (6.1). The two conditions above cannot both hold: otherwise

    n'<=i+(j-i)+B<=2B+R+1,

contradicting (6.1).

### Interior: i>=B+2 and j<=n'-B-1

The augmented interval

    J'=[i-B-1,j+B+1]

lies in the final word and has length at most 2B+R+3<q-1. If n'>=q, choose a final q-gram containing J' and any original occurrence of that q-gram. Translate i,j into that occurrence. Because J' has one extra label beyond each end of the radius-B interval, both the final and original radius-B intervals are strictly interior, even if their containing q-grams abut a physical endpoint. The induced orders and designated pairs match, and both endpoint flags are false.

If n'=q-1 in the unmarked variant, use the common entire prefix instead. The same augmented-margin argument makes both radius-B intervals strictly interior. This separately handles the final word that has no q-gram.

These cases exhaust all final incomparable pairs. The witness pair is genuinely incomparable because its positive-span encoded relation occurs entirely within the common block. LD now gives, directly between P' and P,

    |p_(P')(i,j)-p_P(i*,j*)|<=epsilon.             (6.2)

There is precisely one selected original witness per comparison. Its original occurrence need not be the same for different final pairs. No common global embedding of P' into P is claimed or needed.

Since f(p)=min(p,1-p) is 1-Lipschitz, (6.2) implies

    beta_(P')(i,j)<=beta_P(i*,j*)+epsilon
                    <=delta(P)+epsilon.

Taking the maximum over final incomparable pairs proves the upper half of (2.1).

## 7. The original maximizing pair also survives locally

Use the selected original maximizing pair x<y.

If x<=B+1, the retained prefix supplies the same pair x,y in P'; its complete radius-B interval and flags match just as in the left-boundary case above. If y>=n-B, use the suffix copy shifted by n'-n; the right-boundary argument applies. These two original cases cannot overlap since n>=q>2B+R+1.

Otherwise the original pair has the extra interior guard on both sides. Its augmented interval J from (4.1) lies in the chosen marked q-gram. The marked occurrence in w' supplies an incomparable pair x',y' whose augmented radius-(B+1) interval lies inside that occurrence. In particular both radius-B intervals are strictly interior and match by translation. This is why it is not enough merely to mark a q-gram containing the two endpoints with no buffer.

In every case an actual incomparable pair of P' has

    |p_(P')(x',y')-p_P(x,y)|<=epsilon,

so P' is a nonchain and

    delta(P')>=beta_(P')(x',y')>=delta(P)-epsilon.

Together with Section 6 this proves the theorem. Selecting the exact original maximizer is a theoretical construction; it can be done by a finite exact enumeration of P's linear extensions, with no efficiency claim. For only the one-sided theorem plus preservation of nonchains, any chosen original incomparable pair can be marked instead.

## 8. Finite approximation of the infimum

For D>=1 let

    b_D=inf{delta(P): P finite, nonchain, maximum incomparability degree<=D},
    b_(D,N)=min{delta(P): P nonchain, |P|<=N,
                           maximum incomparability degree<=D}.

The second set is nonempty for N>=2, and is finite up to labelled presentations, so its minimum exists and is an exact rational number. The representative theorem gives

    b_D <= b_(D,N(D,epsilon)) <= b_D+epsilon.       (8.1)

The first inequality is inclusion of classes. For the second, for every eta>0 select P with delta(P)<b_D+eta and use its nonchain representative. Then b_(D,N)<b_D+eta+epsilon; let eta decrease to zero. No assumption that the infinite-class infimum is attained is used.

Therefore, using the audited decay proof and its effective constants, b_D is uniformly computably approximable for each fixed D: enumerate all labelled posets of at most N points, retain the nonchains satisfying the degree bound, and compute all extension counts and pair probabilities exactly. The rational interval

    [b_(D,N)-epsilon,b_(D,N)]

contains b_D (it may be intersected with [0,1/2]). This is an existence/computability statement, not a practically efficient algorithm. For D=1, b_1=1/2 exactly. For D=0 the nonchain class is empty; b_0 is left undefined, or may be +infinity under the extended-real infimum convention. Formula (8.1) is not asserted for D=0.

## 9. Limits and provenance

- This is an additive finite approximation, not an exact threshold reduction. A hypothetical P with delta(P)=1/3-gamma is only guaranteed to have delta(P')<1/3 when epsilon<gamma. The required radius and size can depend on that instance-dependent gap.
- No positive uniform gap below or above 1/3 is proved. A sequence of strict counterexamples approaching 1/3 is not excluded.
- Neither (2.1) nor (8.1) settles whether b_D equals 1/3 or lies strictly below it. Finite approximations alone cannot decide exact equality.
- The compressed P' need not be an induced subposet of P. New local incomparable pairs require their own original local witnesses, supplied in Section 6.
- The finite graph method is classical de Bruijn/finite-language path shortening; the probability prerequisite uses standard positive-matrix/projective-contraction ideas with a supplied proof. No literature-level novelty determination has been made.
- The local-decay dependency is `local_decay/local_probability_decay.md`, specifically its induced-window Theorem 2 at error epsilon/2 for the conservative constants here. Its frozen SHA-256 is `7eaf6b449270286010b98b2e0725b8fbaec21bbe641dcd0e270fcc4a4628c14b`; its independent PASS report is `local_decay/independent_audit/independent_audit.md`. This proof deliberately keeps the conservative epsilon/2 constants even though the audited direct boundary comparison would allow an improvement.


## 10. Supplementary exact checks

The self-contained script `finite_representative_tests/check_encoding_compression.py` uses no project solver. Its exact output is `finite_representative_tests/exact_checks.json`. It checks genuine decoded posets, canonical beginning padding, all q-gram joins, transitivity, degree, endpoint flags, every final local pair witness, and the original designated-pair reverse witness. It uses arbitrary-precision extension counting and exact rational pair probabilities for diagnostic comparisons; the finite tests do not establish the probability-decay theorem.

There are 70 genuine-poset cases, including incomparability gap sets {1}, {1,3}, and {1,2,5}, plus seeded random ordinal sums. The degree bounds include D=1,2,3,4,6, and test radii include B=0,1,3,7. The original sizes are 100 or 110. Both maximum-balance marked pairs and explicitly interior or left-boundary marked pairs are exercised; the retained reverse-witness cases include left, right, and marked interior.

Additionally, all 597 valid R=1, D=1 words of lengths 5 through 12 are tested with q=5 for the graph/legality/witness argument; 87 produce a zero-edge path. This deliberately smaller diagnostic q is not substituted into the theorem's conservative formula.

A negative control starts with a 41-point degree-one poset having just one incomparable pair in the middle. The unmarked shortest path gives an 8-point chain, while a marked path gives a 17-point nonchain retaining the pair. This confirms that nonchain preservation cannot be omitted from the infimum argument, and that the unmarked shortest-path construction alone is insufficient.
