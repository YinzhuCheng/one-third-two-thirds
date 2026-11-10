# Analytic replacement for the D9 four-mark deadline batch

2026-11-10. AUTHOR analytic proof; independent review requested.
Attribution: the conclusion is already Fathi v22 Proposition24.4 and
its equal-predecessor application in §24.4. It replaces that proof's
74-vector finite check by an arbitrary-size analytic argument. It does
not claim original discovery or remove the other finite D9 banks.

## A1. Four common-downset marks

Let M={m1,m2,m3,m4} be four pairwise incomparable labels of a finite
poset P, all with the same strict full predecessor set. If each mark
has at most9 incomparable partners in P, SOME pair of marks is closed
balanced in the original uniform linear extensions of P. No degree cap
on other labels or ambient width bound is required.

Fix an actual word omega on P minus M. The prefix through the last
common predecessor is before every mark; remove this forced prefix
for the conditional insertion calculation (empty if the downset is
empty). Let h_i be the number of remaining base letters before mark i's
first successor, or the entire remaining length if there is none.
All those letters are incomparable with the mark. Thus 0<=h_i<=6,
since its three marked partners already use three of its nine degrees.
Order marks by nondecreasing h, temporarily writing them as 1,2,3,4,
and let L_i=h_i+i. Then L1>=1, L2>=2, L3>=3, L4<=10, and
L_(i+1)>=L_i+1.

Insert marks in that order. Mark i has exactly L_i permissible slots,
independently of earlier choices: every earlier mark lies before the
current mark's forbidden base letter. Each combination of slots gives
one conditional extension, with a unique inverse by reverse deletion.
For i<j the conditional reversal probability is

 q_ij=1/2 product_(r=i..j-1) (L_r+1)/L_(r+1).                 (1)

Indeed mark i has expected rank (L_i+1)/2 immediately after its
insertion. Every intermediate insertion r multiplies that rank by
1+1/L_r, and mark j passes it with probability current rank/L_j.

## A2. Pairwise interval model and the four-letter order inequality

Put a_i=(L_i+1)/L_(i+1) in[0,1]. Independently retain each gap between
consecutive sorted marks with probability1-a_i; the uncut intervals
are blocks. Order blocks naturally and choose a uniform permutation
within each block. Two sorted marks are in one block with probability
product a_i, so this auxiliary law has EXACTLY the pair probabilities
(1). Equality of joint laws is neither claimed nor needed.

For any fixed reference permutation T of the four physical marks,
let V(T) be its three adjacent reversal events. Under EVERY fixed
interval partition, the expected sum of V(T) is at least the sum for
the naturally sorted reference order.

Proof. If there are b blocks and T visits them in r runs, there are
4-r adjacent within-block edges, each reversed with probability1/2.
Every descent between block indices is reversed with probability1;
ascending interblock edges contribute0. The sorted reference has
4-b within-block edges and no descent. It is enough to show
2 descents>=r-b. For four letters: b1 forces r1; b2 has r<=4 and
r>=3 forces at least one descent; b3 has r<=4 and r4 forces a descent;
b4 has r=b=4. These cases prove the inequality without a list of
permutations. Averaging the interval partitions gives the same order
inequality for the ACTUAL conditional mark probabilities.

## A3. A strict analytic lower bound

The sorted reference reversal sum is

 S=1/2[(L1+1)/L2+(L2+1)/L3+(L3+1)/L4].

Set x=L2 (integer x>=2), y=L3>0. Using L1>=1 and L4<=10,

 2S>=2/x+(x+1)/y+(y+1)/10.

The right side exceeds2. After multiplication by10y this is equivalent
to strict positivity of

 y^2+(20/x-19)y+10(x+1).

Its discriminant is -P(x)/x^2, where

 P(x)=40x^3-321x^2+760x-400.

For integer x2 and3 its values are156 and71. For x>=4 put t=x-4>=0;
then P(x)=40t^3+159t^2+112t+64>0. The quadratic has positive leading
coefficient and negative discriminant, proving S>1.

By A2, the sum of the three adjacent reversal probabilities exceeds1
for EVERY fixed reference T, in EVERY actual omega. Summing the actual
conditional completion counts over omega preserves this strict
inequality; no uniform weighting of omega or cap profiles is used.

If all six original mark pairs missed the closed balanced interval,
their >2/3 directions would form a transitive total order T. A directed
triangle is impossible, since a word satisfies at most two of its three
directions. Each of T's three adjacent reversals would have probability
<1/3, so their sum would be<1, contradiction. This proves A1.

## A4. Exact elimination and remaining certificate dependencies

A1 replaces Proposition24.4's four prescribed minima batch (74 cap
vectors and arbitrary references) and the identical strict-downset
four-fork-label use in §24.4. It does not reproduce the exact tabular
margin141/140, which is unnecessary for their contradictions.

It does NOT remove the three-minimum two-layer bank, six/seven maximum
antichain banks, nonsingleton private-ideal banks, long-stem tails or
the final seven-phase remembered-pivot certificate tree. Those require
separate analytic mechanisms; no coverage is inferred from A1.

The four-letter run inequality is genuinely limited to four marks:
with six marks partitioned into three blocks of size2, reference block
word123123 has one descent and no within-block edges, so reversal sum1
is below the sorted value3/2. Thus blindly generalizing A2 to an
arbitrary number of marks is false.

## A5. A real D10 stopping line for THIS bank

Let the exterior be a7-chain c1<...<c7. Take four marked minima whose
cutoffs are(0,2,4,7): mark i is below exactly the chain letters after
its cutoff. The actual maximum degree is10 (the last mark has seven
chain partners and three marked partners; each chain point has degree
at most4). The sorted conditional L-vector is(1,4,7,11), and the same
three adjacent reversal probabilities are

 1/4, 5/14, 4/11,

whose sum is299/308<1. Thus the D9 UNWEIGHTED adjacent bank does not
extend even to this small actual D10 object. It still has balanced
pairs (the latter two displayed probabilities), so it is not a failure
of A1 with a changed threshold or a conjecture/NB counterexample.
It only shows why the OLD bank proof cannot change9 to10 mechanically.

No object enumeration, LE dynamic program or external state change is
used. This proof is analytic at every size, with an elementary integer
polynomial argument, not a regenerated numerical cap certificate.
