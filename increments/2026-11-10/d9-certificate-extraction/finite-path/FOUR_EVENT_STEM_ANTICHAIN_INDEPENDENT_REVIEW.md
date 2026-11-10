# Independent audit: four-event private-stem antichain bank

2026-11-10 UTC. **PASS_WITH_EXACT_STEM2_FOUR_ANTICHAIN_SCOPE.**
Reviewer did not participate in construction. This binds the corrected
`FOUR_EVENT_STEM_ANTICHAIN.md`, SHA256
`5070b2494e0ce4c5dfc6e796205df410fd7d3624a681d62823b3d36149247326`.

The four-event inequality is valid for the stated original-object
contract, with arbitrary original exterior and no degree bound. It
replaces only the identified four-antichain-tail example, not the full
stem batch, the four-prescribed-minima calculation, or a D9 theorem.

## 1. Exact domain and conditional fibers

Q must be an induced original ideal on seven labels, with precisely
 a1<a2<t_i (i=1,...,4), the t_i an antichain and b incomparable with
all other Q labels. Every exterior label must lie above a1 and b.
These are actual order hypotheses, not a conditional law or a newly
completed order.

When exterior exists, fixing the exact Q set I before its first letter
and the entire literal suffix partitions the original extensions.
I is an ideal of P and necessarily contains a1,b. Any linear extension
of P[I] followed by that same suffix is legal: no suffix label can
precede an I label by ideality, and the fixed suffix already respects
its own comparisons. Thus each cell is uniform on the extensions of
I, with no omitted weight or new probability assumption. The empty-
exterior case I=Q is the same argument without a suffix.

If a2 is not in I, b precedes a2 deterministically and the bank is at
least8. If a2 belongs to I, then I={a1,a2,b} union K for an actual
subset K of the antichain. With s=|K|, deleting b leaves the forced
two-letter stem followed by a uniform permutation of K. There are
s+3 equally counted insertion slots for b, precisely two of which
precede a2. Hence the conditional root contribution is16/(s+3).

## 2. The fixed adjacent-path cut bound

The reference naming t1,...,t4 is fixed before any conditioning.
For its three adjacent reversal events:

- both endpoints in K give probability1/2;
- the later reference endpoint in K and the earlier endpoint outside K
  give probability1;
- the other cases are nonnegative, and are legitimately dropped.

Thus the sum is at least

    C(K)=sum_(i=1..3)[x_(i+1)(1-x_i)+(1/2)x_i x_(i+1)]
        =s-x1-(1/2)sum_(i=1..3)x_i x_(i+1).

For s>=1 the selected adjacent-edge count is at most s-1 and x1<=1,
giving C(K)>=(s-1)/2. For s=0 it is zero. This derivation applies to
every K, including noncontiguous K and either endpoint of the path.
It does not choose a new physical pair or reference order in a cell.

Combining it with the root term gives the exact listed lower bounds
for s=0,1,2,3,4:

    16/3, 4, 37/10, 11/3, 53/14.

The minimum11/3 is correct. Equality of this lower certificate is
possible at s=3 with K={t1,t2,t3}; no positive uniform margin should
be inferred or is claimed.

## 3. True-law averaging and strict reference contradiction

The same bank in every cell uses the fixed weights8,1,1,1 on the same
four original physical events. Multiplying each cell inequality by its
actual number of extensions and summing proves

    8Pr(b<a2)+Pr(t2<t1)+Pr(t3<t2)+Pr(t4<t3)>=11/3

in the original uniform extension law. There is no uniform averaging
over I, K, suffixes, or cap profiles.

The bank's weight sum is11. If a putative strict two-thirds reference
places a2 before b and the four t labels in the named order, each of
these fixed reverse events has probability<1/3, so their weighted sum
is strictly<11/3. The resulting contradiction needs only a non-strict
bank lower bound. It does not assert that one particular pair pays
every cell, nor that the bank alone handles other positions of b in a
putative reference order.

## 4. Archive comparison and the higher-h barrier

Directly inspected Fathi v22 §24.4, pp282–283, and the certificate
archive `singleton_stem/README.md` and `length4.json`. The displayed
old vector (14,0,0,0,0,3,1,0,1,1,1) has six positive coordinates,
not seven; their sum is21 and its threshold is7. The corrected author
version now counts them correctly. The new bank has four positive
coordinates and total11. This is a genuine reduction of that explicit
example's support, not evidence that every stored certificate has a
four-event replacement.

The general adjacent-path cut lemma is valid for arbitrary h. For a
root coefficient c and equal adjacent weights1, an exact cell with
K={t1,t2,t3} and the rest of the tail appearing in increasing reference
order has root probability1/3 and reversal sum1. The per-cell payment
would require c/3+1 >= (c+h-1)/3, hence h<=4.

That is a cellwise-template obstruction only. One low cell does not
refute a whole-P bank because other cells or positive suffix reversals
can compensate. The initial author wording was too broad on this
point; the corrected frozen version explicitly limits the claim to
cellwise payment/proof and claims no global counterexample.

## Scope and method

No blocking error remains in the corrected version. This report does
not prove a generalized large-tail bank, a new original balanced-pair
class, any finite-batch replacement beyond this example, or any D10
result. No degree bound is required for this exact original ideal
inequality.

Method: direct source/author reading, manual fiber and path-cut
verification, exact fraction arithmetic, and file hashes. No object
family enumeration, LE DP/LP, numerical certificate replay, external
write, or participation in a replacement construction occurred.
