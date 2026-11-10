# Four-event analytic compression of the four-tail example

Status: author analytic proof; pending independent audit. This replaces only the explicit four-antichain-tail example in Kevin Fathi, Gold certificates and balanced pairs, v22 §24.4, https://zenodo.org/records/23933091. It does not replace the full D9 certificate tree.

## Exact original-object contract
Let P be a finite poset. Its induced ideal Q consists of a1,a2,b,t1,t2,t3,t4. The only relations in Q are a1<a2<ti for i=1,...,4. In particular the ti form an antichain and b is incomparable with all six other Q labels. Every label of P\Q lies above a1 and b. No further restriction is placed on the exterior, and no degree bound is needed. All probabilities below refer to uniform linear extensions of this same original P.

For every fixed naming t1,...,t4, the following holds:

8 Pr(b precedes a2) + Pr(t2 precedes t1) + Pr(t3 precedes t2) + Pr(t4 precedes t3) >= 11/3.

Thus if a putative strict two-thirds reference order places a2 before b and t1 before t2 before t3 before t4, not all four displayed reverse events can have probability strictly below 1/3. This is a weighted contradiction, not a claim that the same one of these events is >=1/3 in each conditional cell.

## Proof with actual prefix and suffix weights
If P\Q is nonempty, condition on I, the exact Q label set before the first exterior letter, and on the complete literal suffix starting at that exterior letter. If exterior is empty take I=Q and suffix empty. Any legal such cell has I containing a1,b. The full count factors as legal permutations of the ideal I followed by the one fixed suffix, with no omitted or independently assigned weight.

If a2 is not in I, b precedes a2 in every full word in this cell, so the left side is at least 8 > 11/3.

Otherwise let K=I intersect {t1,t2,t3,t4}, s=|K|. After deleting b, the I-word is a1,a2 followed by a uniform permutation of K; b has s+3 equally counted legal insertion slots. Exactly two slots place b before a2, so its probability is 2/(s+3).

Put xi=1 if ti belongs to K. For the adjacent reverse event ti+1 before ti, both labels in K contribute 1/2, a later label in K with the earlier label outside contributes 1, and every other case contributes at least 0. Therefore the sum of the three adjacent reverse-event probabilities is bounded below by

C(K)=sum(i=1..3) [xi+1(1-xi)+(1/2)xi xi+1]
    =s-x1-(1/2)sum(i=1..3)xi xi+1.

For s=0 this is 0. For s>=1, the number of selected adjacent edges is at most s-1, and x1<=1. Hence C(K)>=(s-1)/2. The conditional bank is at least

16/(s+3)+max(0,(s-1)/2).

For s=0,1,2,3,4 this bound is respectively 16/3, 4, 37/10, 11/3, 53/14. The minimum is 11/3. Average using the actual numbers of full words in all cells. This proves the original-object inequality.

## Relation to the archived example
The paper's displayed 11-coordinate vector is (14,0,0,0,0,3,1,0,1,1,1), i.e. six positive event weights, with total weight21 and threshold7. The present bank uses four positive events, total weight11, with an analytic path-cut lower bound. Neither this one example nor the sparse-support census below proves that all D9 certificates can be similarly compressed.

## General reusable cut lemma
For an arbitrary antichain of h fixed ordered labels and a selected subset K of size s, the directed adjacent-path cut functional satisfies C(K)>=max(0,(s-1)/2). This is a parameter-uniform combinatorial inequality, independent of degree or exterior size. The root insertion term then determines which h admits a bank. For h=4 it gives the inequality above; for h>=5 this particular cellwise 1-root-plus-equal-adjacent-weights proof cannot hold on every prefix/suffix cell: on the exact cell K={t1,t2,t3}, a suffix with the remaining tail in increasing order attains the cut lower bound, and the s=3 cell inequality is independent of the root coefficient and forces h<=4. This only blocks a per-cell proof with that bank template. It does not prove failure of a whole-P bank: other cells or tail comparisons may compensate, and no global counterexample is claimed.
