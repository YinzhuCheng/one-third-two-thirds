# Independent review: analytic private fork and diamond absorption

2026-11-10 UTC. **PASS_WITH_EXACT_FORK_BANK_AND_DIAMOND_EXCLUSION_SCOPE.**
Reviewer did not participate in derivation. This report binds
`PRIVATE_FORK_ANALYTIC_REPLACEMENT.md`, SHA256
`33f06f00e0c8b79ea5488ed7b0d6139e019beb5310ee73dfc1647b3d4463f708`.

No blocking mathematical error or counterexample found. The proof
analytically establishes both fixed physical fork inequalities for
all the stated actual deadlines and therefore replaces the285-profile
fork bank. Applying that same lemma to the original three-label
subideal of a private diamond makes the1110-profile diamond table
unnecessary for its ordinary-balance exclusion purpose. It does not
establish the diamond's stronger107/140 numerical bound, remove larger
private-chain trees, or prove a new D9/D10 theorem. The added F1E
corollary analytically discharges the entire nonchain minority-private
stage under its explicit original NB premise; F3 supplies only the
stated two-summary convex-mixture obstruction.

## 1. Exact conditional completion law

The hypothesis that {b,s,t} is an original ideal, with exactly b<s,t
and s||t, ensures there are no exterior predecessors of any marked
label. Each actual exterior word therefore constrains insertion only
by the first exterior successor deadlines. Actual b<s,t implies
h_b<=min(h_s,h_t). No synthetic independence or external relation is
added. A first exterior successor may be absent; then the deadline is
the full exterior length, and the same counts apply.

For h_s<=h_t put A=h_s+1, B0=h_t+2 and n=h_b+1. Their ranges
1<=A<=9, A+1<=B0<=10 and1<=n<=A are correct.

Fixing b in exterior gap j leaves A-j choices for s's base gap and
B0-j-1 choices for t's base gap. Each common gap requires two orders
rather than one, so the exact count is

    N_j=(A-j)(B0-j-1)+(A-j)=(A-j)(B0-j).

The corrected author explanation now calls the first product all
base-gap pairs counting a common gap once; it is not the number of
strictly distinct-gap pairs.

For t before s, summing over s's legal gaps gives exactly

    Q_j=(A-j)(A-j+1)/2.

Swapping the two leaves injects this earlier-longer-deadline orientation
into its reverse, because both positions in the former are at most
h_s<=h_t. Thus Q_j is the harder directional count. The total number
of conditional words is N=sum_j N_j; its b-start count is N_0=AB0.
Since both other marked labels lie above b, b starts the full original
word exactly when it is in exterior gap0. This includes empty exterior.

## 2. Margin polynomial and endpoint arithmetic

The integer margin for the harder fixed bank is

    F=2AB0+sum_(j=0,...,n-1)(Q_j-N_j).

With r=A-j its summands equal

    r(A-B0+1/2-r/2)<0.

Hence F is minimized, for fixed A,B0, by the largest legal n=A.
Direct summation gives exactly

    F >= A/12[6B0(3-A)+2(A+1)(2A+1)].

For A<=3 the bracket is strictly positive. For A>=4, using B0<=10
in the negative coefficient gives

    F >= A/6(A-7)(2A-13).

This is nonnegative for every admissible integer A=4,...,9: the only
negative real interval between the roots6.5 and7 contains no such
integer. The stated factorization and direction of the endpoint
inequality are correct. Thus the bank is analytic over the full cap
domain; it is not a regenerated finite cap table.

The equality example(h_b,h_s,h_t)=(6,6,8) gives
A=7,B0=10,n=7 and

    N=sum_(r=1..7)r(r+3)=224,
    N_start=70,
    Q=sum_(r=1..7)r(r+1)/2=84,

so2N_start+Q-N=0 exactly. No strict bank margin is available or claimed.

## 3. Fixed physical orientations and actual-weight transfer

Leaf relabeling is allowed internally to prove which orientation is
harder in one omega. It is not used to select an event after observing
omega. The result proves separately, for the same physical s,t,

    2N_start(omega)+N_st(omega)>=N(omega),
    2N_start(omega)+N_ts(omega)>=N(omega)

for every actual omega. Summing each integer inequality over omega
recovers the exact corresponding counts in the same original P.
Equivalently, both fixed banks hold in the unconditional law. This
justifies the statement with the unconditional minimum of the two
probabilities; it does not interchange a minimum and expectation.

If original start probability S<1/3, both leaf orientations have
probability>=1-2S>1/3, and hence each is also<2/3 by complementarity.
The resulting leaf balance is strict. At S=1/3, both orientations
are>=1/3 and closed balance follows. Thus a non-strict bank is fully
sufficient for the intended minority-root contradiction.

Only the original degrees of s and t are needed to derive the cap8:
each already has the other leaf as one incomparable partner, and
every exterior letter preceding its first successor is another
original incomparable. No degree assumption on b or the other
exterior labels is hidden in the conditional theorem.

## 4. Diamond absorption preserves the actual law

If the original private ideal is b<s,t<z, removing z from the MARKED
set leaves {b,s,t} as an original ideal. Nothing is removed from P:
z becomes an actual letter of each exterior word along with the
previous exterior labels. All original relations, including s,t<z,
remain. Each full extension has a unique restriction to this new
exterior and its marked insertion, so there is neither resampling nor
uniform weighting of z positions.

The original leaf degrees remain at most9, with s||t still using one
internal degree unit; both new exterior deadlines are therefore at
most8. Root b is still below the two marked leaves, so its gap0 event
is exactly the original full-word start event. Each fixed directional
bank from Section3 holds on every such actual new exterior word and
sums back to the original P unchanged.

Consequently the same root-minority condition S<1/3 already forces
leaf balance in the diamond. This discharges the exclusion for which
Fathi's1110-profile diamond bank was used. It does not imply that the
stronger archived S+Pr(s<t)>=107/140 bound has been analytically
reproved, and the source appropriately disclaims that claim.

## 4A. Full nonchain-minority-private elimination

The F1E corollary is correct under the original no-balanced-pair
hypothesis, equivalently with the conclusion: either P already has a
balanced pair or its minority private ideal J is a chain of at most4
labels. The no-balanced-pair qualification is essential to inferring
that J itself must be a chain; a bank supplying a balanced pair is not
an order-theoretic contradiction without it.

In the exact original two-minimum setup, J=P minus the inclusive
upset of a is an original ideal uniquely rooted at b. The first letter
lies in J exactly when it is b, and b precedes a exactly when b starts.
The existing rooted-ideal lemma with d=9 gives

    S>=|J|/(|J|+9).

Thus S<1/3 implies2|J|<9 and |J|<=4. If b has two distinct immediate
children s,t in J, each has the full original predecessor set{b}:
there are no other J predecessors because they cover the unique root,
and no predecessors outside J because J is ideal. The selected fork
is an original ideal, so F1 gives a balanced leaf pair.

If b has just one child z, every other J label is above z. A nonchain
J of at most4 labels must therefore have exactly the shape b<z<s,t.
Its two maximal leaves each already have one internal incomparable
partner, so each has at most8 incomparable partners outside J. The
same rooted-ideal lemma gives S>=4/(4+8)=1/3, contradicting minority.
This exhausts all rooted nonchain shapes of the allowed size without
a poset table. Under the original NB premise only the chain cases
remain. No private chain of sizes2,3,4 is eliminated by this corollary.

The initial author F1E wording omitted an explicit NB qualification.
A7-chain disjoint from a3-point fork has maximum degree8 and b-start
probability3/10, but its private ideal is a nonchain fork with fair
leaves. This was raised during review to require the scope correction;
it does not refute the corrected corollary or F1. The final frozen
author includes the required NB/either-pay-or-chain qualification.

## 5. Actual degree-ten negative bank control

The stated original12-point construction consists of the9-chain,
b<s,t, s<c7, and the redundant b<c7, with no other generated relations.
Its only minima are c1 and b. The labels not above c1 are precisely
{b,s,t}, giving the stated actual private ideal.

Each of b,s is incomparable with c1,...,c6; s is additionally
incomparable with t. The label t is incomparable with all9 chain
labels and with s, hence has degree10. Chain labels have degree at
most3. Thus maximum original degree is exactly10, not merely a cap
assignment.

There is exactly one exterior word. Its deadlines are(6,6,9), giving
A=7,B0=11,n=7. Direct exact sums yield

    N=sum_(r=1..7)r(r+4)=252,
    N_start=77,
    N_ts=84,
    2N_start+N_ts-N=-14.

This is an actual failure of the same fork bank after increasing the
leaf cap8 to9. The leaf probability84/252=1/3 is balanced at the closed
endpoint, so this object is neither NB nor a balanced-pair counterexample.
It does not prove failure of every D10 bank or of a degree-ten analogue
of ordinary balanced-pair existence.

## 6. Two-real-law convex-summary obstruction

Also checked the added F3 claim in the revised source. Its P_L is the
actual degree-ten control in Section5. For P_H, s<c2 gives h_b=h_s=1
and h_t=9, so A=2,B0=11,n=2. Its exact counts are

    N=2*11+1*10=32, N_start=22, Q=3+1=4.

The two minima are again c1,b, the actual private ideal is still
{b,s,t}, and t again has degree10. Both laws are therefore genuine
original degree-ten poset laws on the same physical label set, not
arbitrarily chosen cap laws.

For S=Pr(b starts) and R=Pr(t<s), their summaries are

    P_L: (11/36,1/3), P_H: (11/16,1/8).

Their99/100 and1/100 convex mixture has exactly

    S_mix=99/320<1/3, R_mix=53/160<1/3.

Thus no universally valid mixture-stable constraints on just(S,R)
can, together with S<1/3, force leaf balance: such constraints must
hold on both actual component summaries and on their mixture, whose
summary violates the proposed conclusion. This is not an assertion
that the mixture is itself an original poset law. It is also not an
assertion that all pairs in that mixture are unbalanced, and cannot
refute any original degree-ten balance theorem or enlarged-mark fork
proof. The corrected frozen author explicitly preserves these limitations.

P_H does not satisfy the minority-start premise, so the argument must
not say that the conditional guarantee itself applies to P_H. What
passes through mixtures are the proposed universal constraints; the
minority-start premise is then checked on the mixture. This is a
logical wording precision, not a change to the valid obstruction.
The final frozen author has made this distinction explicit.

## Sources, dependency scope and audit method

Directly read the frozen author manuscript and Fathi v22 source PDF,
§24.3, pp279–280. The source explicitly uses the285-profile fork bank
2S+R>=1 and the1110-profile diamond bank S+R>=107/140, including
leaf swapping. The reviewed analytic proof covers the first bank's
whole cap domain and absorbs the second bank's ordinary exclusion
purpose as above. No priority claim or new ordinary-balance class is
attributed to this replacement. The remaining private-chain and other original D9 finite banks
remain outside this report. F1E additionally makes the nonchain-private
stage analytic using the already analytic rooted-ideal lemma.

The independent audit used direct reading, manual actual-order and
gap-count reasoning, finite polynomial identities, and exact arithmetic
on the displayed examples. No poset-family enumeration, LE DP/LP,
numerical profile replay or new covering construction
was performed.
