# Independent review: four-mark analytic replacement

2026-11-10 UTC. **PASS_WITH_EXACT_FOUR_MARK_ANALYTIC_SCOPE.**
No blocking mathematical error or counterexample found. The reviewer did
not participate in construction or derivation. This review binds
`FOUR_MARK_ANALYTIC_REPLACEMENT.md`, SHA256
`434bcf5fe6976b78903f41b3d9ad6a1c6d7f4af1b8b3b714bf5cc0a7509e36a1`.

The proof establishes an analytic replacement for the four-prescribed-
minima part of Fathi Proposition24.4 and its four-common-predecessor-set
application. It does not remove the proposition's three-minimum branch
or the other D9 finite banks, and it does not prove a D10 theorem.

## 1. Common-downset conditional insertion law

The common strict full downset condition is sufficient. In each actual
base word omega obtained by deleting the four marks, every letter of
the prefix through the last common predecessor is necessarily before
every mark. Conversely no mark can be inserted in that prefix. No
successor of a mark can occur in that prefix, since that would produce
a cycle with the common predecessor. After the prefix, there are no
retained predecessors of any mark. This is a genuine forced-prefix
factorization, not conditioning on a favorable event or deleting
information about an unforced predecessor.

Before its first successor every remaining base letter is therefore
incomparable with the mark. The three other marks are also incomparable,
so each h_i<=9-3=6. An empty exterior or a mark without a successor is
covered by taking the full remaining length as its deadline.

After sorting the deadlines, insert marks in nondecreasing h. At stage
i every earlier mark is before the current first forbidden base letter,
so there are exactly h_i+i=L_i legal insertion slots. This number does
not depend on earlier slot choices. Reverse deletion uniquely recovers
the insertion choices. Independent uniform choices of the slots thus
produce exactly the uniform conditional extension law over that actual
omega, with product_i L_i completions.

For i<j, the rank of mark i immediately after insertion i is uniform on
1,...,L_i. At any intermediate insertion r, its conditional expected
rank becomes its previous rank times (1+1/L_r), since the chance of an
insertion before it is rank/L_r. At insertion j the probability of j
preceding i is rank/L_j. This yields exactly

    q_ij = (1/2) product_(r=i,...,j-1) (L_r+1)/L_(r+1).

No independence assertion about the actual mark-pair events is used.

## 2. Auxiliary interval blocks preserve exactly what is needed

The sorted L increments imply 0<a_i=(L_i+1)/L_(i+1)<=1. For independent
cuts with probability 1-a_i, two marks i<j share a block with probability
product_(r=i,...,j-1) a_r. Uniform order within a shared block gives
reversal probability one-half, while different blocks preserve sorted
order. Therefore this auxiliary law has the same six pair probabilities
as the true conditional law. Its full joint distribution need not agree,
and the argument never requires it to agree.

For a fixed interval partition into b blocks, let a reference T have r
block runs and d interblock descents. Its adjacent reversal sum is

    (4-r)/2+d.

For the sorted reference it is (4-b)/2. Thus the required comparison is
2d>=r-b. If r<=b it is automatic. For b=1 or4 no remaining case arises.
For b=2, r=3 or4 forces a descent and r-b<=2. For b=3 the only remaining
case r=4 also forces a descent and r-b=1. This is an exhaustive proof
for four marks, including unequal block sizes. It establishes the
inequality for every physical reference permutation, not merely the
sorted order in one sector.

Pairwise expectation then transfers the inequality to the actual law.
The six-mark 123123 example correctly shows that this step is not a
valid unrestricted-number-of-marks principle.

## 3. Strict analytic lower bound and discriminant

For sorted marks the adjacent sum is

    S=(1/2)[(L1+1)/L2+(L2+1)/L3+(L3+1)/L4].

With integer x=L2>=2 and y=L3>0, L1>=1 and L4<=10 give

    2S >= 2/x+(x+1)/y+(y+1)/10.

Subtracting2 and multiplying by positive10y gives

    y^2+(20/x-19)y+10(x+1).

Its discriminant is exactly

    -[40x^3-321x^2+760x-400]/x^2.

The cubic values P(2)=156 and P(3)=71 are correct. For x=4+t,

    P(x)=40t^3+159t^2+112t+64>0  (t>=0).

The use of integrality at x=2,3 is explicit and legitimate because
L2 is an integer slot count. Negative discriminant and positive leading
coefficient show strict positivity for every real y, in particular for
all admissible integer L3. Thus S>1 without enumerating a finite cap
list, and every reference has a conditional adjacent sum>1.

## 4. Fixed-bank quantifiers, strictness and the original conclusion

Sorting the four marks may depend on omega. This causes no selection
error: the proved comparison holds for every reference permutation in
every omega. The final reference T is one fixed physical order, chosen
from the hypothetical original strict two-thirds tournament, not
rechosen after observing omega. Its three physical adjacent reversal
events remain fixed while the proof uses sorted coordinates internally.

In a fixed finite P there are finitely many actual omega sectors, each
having a positive integer number of completions. Multiplying the strict
conditional inequalities by those counts and summing preserves strict
>1 in the original extension law. No uniform mixing of deadline vectors
or exterior words occurs.

If all six mark pairs avoided closed balance, their probability>2/3
directions would form a tournament with no directed triangle: every
word satisfies at most two of a cyclic triple's directions. A tournament
without a directed triangle is transitive, giving the fixed order T.
Every adjacent reversal in this T would then have probability<1/3,
contradicting the proved strict sum>1. The closed-balanced conclusion,
including its endpoint convention, is correct.

## 5. Fathi source compatibility and exact eliminated dependency

Directly read Fathi v22 source PDF, Proposition24.4, p279, and the
four-equal-strict-predecessor-set use in §24.4, pp283–284. The source says
that the four-minimum deadlines are at most6 and that its74-vector
check has minimum adjacent inversion sum141/140, attained at
(0,2,4,6). It then treats the three-minimum two-layer problem separately.

The candidate proves the needed inequality over the larger entire
four-mark cap domain 0<=h_i<=6, with arbitrary reference permutations.
Consequently it covers every original vector used by that check. This
review does not reconstruct why the source reduced its numerical
list to exactly74 representatives; that cardinality is immaterial to
the analytic coverage. The original (0,2,4,6) vector gives L=(1,4,7,10)
and sorted adjacent sum1/4+5/14+4/10=141/140, consistent with the source.
No claim to have analytically proved the exact global minimum141/140
is made or needed.

Four prescribed original minima have empty common downset and fall
under A1 even if other minima exist. Four marks with identical nonempty
full downsets fall under the forced-prefix argument above. Only the
four marks' original degrees are used; no width or other-label degree
assumption was silently added. These quantifiers are sufficient for
both identified uses in the original proof.

## 6. Degree-ten stopping control is an actual object

Take the stated7-chain and four incomparable minima with cutoffs
(0,2,4,7). Exactly the first h_i chain points are incomparable with
mark i, so its degree is3+h_i, namely3,5,7,10. Chain-point degrees are
at most4. Thus the object's actual maximum incomparability degree is10,
with no fictitious independent deadline assignment.

There is only one base word, and L=(1,4,7,11). The three adjacent
reversal probabilities are exactly

    1/4, 5/14, 4/11,

with sum(77+110+112)/308=299/308<1. This is a real failure of the same
unweighted adjacent bank at degree10, not merely a negative relaxed
bound. The latter two displayed pair probabilities are within the
balanced interval. It therefore refutes neither a degree-ten balanced-
pair theorem nor the unrestricted conjecture, and it supplies no NB
object. It establishes exactly the claimed obstruction to changing9
to10 in this particular bank proof.

## Scope and method

Analytic proof passes within the scope above. No new priority claim,
full-D9 analytic proof, D10 coverage, arbitrary-mark generalization,
new weighted bank, or new residual construction follows.

This independent review used direct manuscript/source reading, manual
slot/rank and run-count verification, polynomial expansion, and exact
fraction arithmetic. It performed no poset-family enumeration, LE
DP/LP, numerical certificate replay, or external state change.
