# Analytic replacement for all 285 D9 private-fork profiles

2026-11-10. AUTHOR proof, independent review requested.
This is an analytic proof of the already-used inequality in Fathi v22
§24.3, not a new ordinary-balance class or historical novelty claim.
It removes the need for that285-vector fork check AND makes the
separate1110-vector diamond check unnecessary for its balance target.
It does not remove the larger private-branch trees.

## F1. Actual-word theorem

Let B={b,s,t} be an original ideal with b<s,b<t and s||t. Fix an
actual word omega on P minus B. Let the exterior deadlines satisfy
0<=h_b<=min(h_s,h_t) and max(h_s,h_t)<=8. Because b is below
both other marked labels, b starts a complete extension exactly when
it occupies exterior gap0 (also when the exterior is empty). Then,
CONDITIONALLY on this same actual omega,

 2Pr(b starts)+min{Pr(s<t),Pr(t<s)}>=1.                (F1)

The same inequality therefore holds in the full original P after
summing true completion counts, not uniform cap vectors. If the
unconditional start probability is<1/3, the leaf pair s,t is closed
balanced. Degree<=9 on s,t gives their exterior caps<=8 because
the other leaf is already an internal incomparable partner. The
two-minimum/private-B setting is one application, but not required
for the arbitrary original ideal inequality itself.

## Proof

Relabel leaves, for this conditional calculation only, so h_s<=h_t.
Write A=h_s+1, B0=h_t+2, n=h_b+1. Thus

 1<=A<=9, A+1<=B0<=10, 1<=n<=A.

If b is put in gap j, 0<=j<n, there are exactly

 N_j=(A-j)(B0-j)

lifts of s,t. Explanation: all pairs of base gaps, counting each
common gap once, contribute(A-j)(B0-j-1). A common gap actually
has two orders, so add one extra choice at each of its A-j positions.
The number with t before s is

 Q_j=(A-j)(A-j+1)/2.

Indeed if t precedes s both gaps lie at most h_s; this is the sum of
1,...,A-j, including the appropriate same-gap order. Its reverse is
at least as numerous by swapping s,t (the earlier cap belongs to s).
The full conditional N is sum_j N_j, Q is sum_j Q_j, and the number
with b first is N_0=A B0. Hence the desired integer margin is

 F=2A B0+sum_(j=0..n-1)[Q_j-N_j].

Each added summand is strictly negative: on writing r=A-j,
Q_j-N_j=r(A-B0+1/2-r/2)<0 because B0>=A+1.
Therefore F is minimized over allowed n at n=A. Using sums of r
and r² for r1..A gives

 F>= A/12 [6B0(3-A)+2(A+1)(2A+1)].                  (F2)

If A<=3, the displayed bracket is positive. If A>=4 its B0
coefficient is negative, so B0<=10 gives

 F>=A/6 (A-7)(2A-13)>=0.                            (F3)

The last inequality holds for each integer A4..9: A4/5/6 have both
factors negative, A7 gives0, and A8/9 both positive. This is a single
factored polynomial argument, not a table of cap probabilities.

Thus 2start+Pr(t<s)>=1 in the harder direction; the other direction
is larger. The leaf relabelling was only used to prove BOTH event
inequalities. In particular the fixed physical inequalities
2N_start+N_st>=N and 2N_start+N_ts>=N each hold for EVERY omega,
so each transfers to the original unconditional law with its actual
completion multiplicities. If start<1/3, both leaf orientations exceed
1/3, giving strict leaf balance. At start=1/3 the conclusion is closed
balance. This does not choose the leaf orientation after averaging.

Equality in the conditional harder bank is possible, e.g.
(h_b,h_s,h_t)=(6,6,8): N224,N_start70,Q84. No uniform positive
margin is claimed for F1, and the input start<1/3 supplies strictness.

## F1D. The diamond batch is absorbed by the SAME lemma

If the original private ideal is b<s,t<z, its subideal{b,s,t}
is still an ORIGINAL ideal. Put z back into the actual exterior word
and apply F1 to that three-label ideal. The full leaf degrees remain
<=9, their exterior caps remain<=8, and the root gap0 event remains
that b starts the complete original extension. The possible location
of z before the other exterior labels changes the actual conditioning
word but violates none of F1's assumptions. Both fixed-direction
integer inequalities hold on every such word, and sum back to P.
Thus b minority implies leaf balance without a diamond-specific table.
This does NOT reprove the stronger107/140 numerical inequality; it
replaces the1110-profile table only for the exclusion it was used for.

## F1E. Entire D9 nonchain-minority-private stage becomes analytic

In the original two-minimum D9 setting, ASSUME P HAS NO CLOSED
BALANCED PAIR. Name b withPr(b<a)<1/3 and letJ=P minus up(a),
the rooted private ideal. The existing
analytic rooted-ideal start bound |J|/(|J|+9) implies |J|<=4.
If J is nonchain and its root b has at least two immediate children,
choose two s,t. The induced{b,s,t} is an ORIGINAL ideal (their full
predecessor sets insideJ are{b}, andJ is ideal), so F1 already pays.
If the root has just one child but J is nonchain with at most4 labels,
the only possibility is b<z<s,t. Each maximal leaf has one internal
incomparable, hence at most8 exterior partners; the same rooted-ideal
start bound givesPr(b starts)>=4/(4+8)=1/3, contradiction.
Therefore under that original no-balanced-pair hypothesis J must be
a chain, with at most4 labels. Equivalently, without that hypothesis,
either P has a balanced pair or J is a chain of at most4 labels. This derives the
nonchain-private elimination in §24.3 using only the pre-existing
analytic rooted-start lemma plus F1, not the285/1110 finite batches.
No claim is made about eliminating the remaining private chain sizes.

## F2. The actual D10 stopping line for this bank

Take a9-chain c1<...<c9 as exterior, a=c1. Let b<s,b<t; impose
b<c7 and s<c7 (h_b=h_s6), and leave t incomparable with all c_i
(h_t9). Take no other comparisons beyond transitive closure.
Then the original minima are a,b, B={b,s,t} is exactly the private
ideal P minus up(a), and Delta(P)=10 (t sees the9 chain labels and s).

A7,B0=11,n7 gives

 N252, N_start77, N_ts84,
 2N_start+N_ts-N=-14.

Thus the old D9 fork bank does not extend to this actual degree10
object. The leaf probability84/252 is1/3, so it HAS a balanced pair;
this is not a conjecture/NB counterexample. It only refutes mechanically
changing the exterior cap8 to9 in the same bank.

No object enumeration, LE DP or LP was used. The
arbitrary-size proof is the actual-word gap count and its factored sum.

## F3. A two-real-law obstruction to a D10 (start,leaf) closure

This is stronger than failure of one coefficient choice, but only
concerns that two-event summary. On the SAME twelve physical labels
{b,s,t,c1,...,c9}, use the exterior9-chain and h_t9. Two actual
private-fork posets are:

 P_L: h_b=h_s6, with b<s, b<t and s<c7;
 P_H: h_b=h_s1, with b<s, b<t and s<c2.

For both, transitive closure gives exactly two minima a=c1,b,
private ideal{b,s,t}, and Delta10. P_L has
(S,Q/N)=(11/36,1/3). P_H has N32,start22,Q4, hence
(S,Q/N)=(11/16,1/8). Mix their extension LAWS with weights99/100
and1/100 (this is not asserted to be an individual poset law). Then

 S_mix=99/320<1/3, R_mix=53/160<1/3.

Thus minority start plus any universally mixture-stable constraint
using only(S,R) cannot guarantee the leaf pair's balance at D10.
Any proposed universal mixture-stable constraints on the two summaries
must hold for both actual component summaries and therefore their
mixture. Combined with S_mix<1/3 they thus cannot implyR_mix>=1/3.
The minority premise itself is NOT asserted forP_H. This is NOT a
mixture without ANY balanced pair and NOT an ordinary poset/NB
counterexample. It only forces a valid D10 proof either to retain
more original structural information that forbids arbitrary mixing,
or to use other comparison events/candidates. In particular it does
not refute Fathi's D10 fork elimination using enlarged marked ideals.
