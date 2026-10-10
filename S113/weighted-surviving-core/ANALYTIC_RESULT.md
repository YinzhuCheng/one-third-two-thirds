# Exact count and necessary weight cone for the seven-block survivor

Date: 2026-10-10. Status: proved identities and necessary conditions; no all-weight balance theorem is claimed.

## 1. Poset, notation, and law

The quotient has covers

0<3; 1<2,4; 2<3,6; 3<5; 4<5.

Replace vertex i by a nonempty chain C_i of length w_i. Write B_i,T_i for its bottom and top. Throughout, probabilities mean the uniform law on the complete linear extensions of this inflated poset. Equivalently, they mean the uniform law on valid multiset words. They never mean a uniform extension of the seven-point quotient.

Use the abbreviations

(u,a,b,c,t,d,v)=(w0,w1,w2,w3,w4,w5,w6).

The order-reversing quotient involution is (0 6)(1 5)(2 3), with 4 fixed. Thus duality sends the weight vector to

(v,d,c,b,t,a,u).

This is a bijection on complete extensions after reversal, not an assumption that arbitrary weights are self-dual.

## 2. An exact double sum

Define

F(i,j) = binom(b+j−1,j) binom(a+b+i+j−1,i),

G(i,j) = binom(u−i+c+t−j,t−j) binom(u−i+c+t−j+d+v,v).

Then the exact number of complete extensions is

Z(u,a,b,c,t,d,v) = sum_(i=0)^u sum_(j=0)^t F(i,j)G(i,j).   (1)

Proof. Split a complete extension immediately after T_2. Let i and j be the numbers of elements of C_0 and C_4 appearing before T_2. Every element of C_1 and C_2 has then appeared, and no element of C_3,C_5,C_6 has appeared. The prefix ends with T_2. After removing its i elements of C_0 and the final T_2, the prefix consists of C_1 followed by a shuffle of b−1 elements of C_2 and j elements of C_4, yielding binom(b+j−1,j) choices. Insert the i C_0 elements into that prefix before its final T_2 in binom(a+b+i+j−1,i) ways.

After T_2, ignore C_6 for the moment. The remaining u−i elements of C_0 followed by all c elements of C_3 form one chain. The remaining t−j elements of C_4 form a second chain. These chains shuffle in binom(u−i+c+t−j,t−j) ways, and all d elements of C_5 follow. All v elements of C_6 may shuffle freely with this whole suffix, giving the other factor in G. Every extension has one unique split and is counted once. QED.

The formula continues to count the appropriate deletion posets when a=0 or d=0: deleting all of C_1 retains its imposed order between the remaining blocks, so C_2 and C_4 can start immediately; deleting C_5 removes its common final chain. In this use b,c,t remain positive.

## 3. Exact endpoint probabilities

Because the only minima are B_0,B_1, deleting a first B_1 gives

Pr(B_1<B_0) = Z(u,a−1,b,c,t,d,v)/Z(u,a,b,c,t,d,v).   (2)

Because the only maxima are T_5,T_6, deleting a last T_5 gives

Pr(T_6<T_5) = Z(u,a,b,c,t,d−1,v)/Z(u,a,b,c,t,d,v).   (3)

The split variable i gives

Pr(T_0<T_2) = [sum_(j=0)^t F(u,j)G(u,j)]/Z.   (4)

Applying (4) to the dual vector gives Pr(B_3<B_6) in the original poset.

The structural-good-pair forced graph requires, in any counterexample,

Pr(B_1<B_0)>2/3, Pr(T_6<T_5)>2/3,
Pr(T_0<T_2)<1/3, Pr(B_3<B_6)<1/3.

Thus (2)–(4) provide four exact integer rejection tests using only the double sum. Failure of a forced orientation proves the existence of some balanced pair by the already established good-pair theorem; that balanced pair need not be the endpoint pair tested.

## 4. Three simple linear necessary inequalities

Every counterexample in this family must satisfy

2u < a+b+t+v,                                            (5)
2v < u+c+t+d,                                            (6)
2t < u+b+c+v.                                            (7)

These conditions hold for every positive weight vector, independently of cardinality minimality. Combining them with the existing port-cycle filter gives u,v≥2.

### Window-insertion fact

Remove one chain module C of length k. Fix an extension sigma of the outside poset. Let its insertion window contain h outside elements, between the last predecessor of C and the first successor of C. There are binom(h+k,k) valid insertions. Conditional on sigma under the original inflated uniform law, they are equally likely, even though sigma itself has the induced reweighted law. If h≥1, the probability that C supplies the first element of the window is k/(k+h), by counting binary shuffles. This fact uses the correct conditional law and makes no uniform-outside assumption.

For (5), remove C_0. Every outside extension begins with B_1, and the window ends immediately before B_3. It contains all a+b elements of C_1,C_2, some elements of C_4,C_6, and no elements of C_3,C_5. Thus h≤a+b+t+v and

Pr(B_0<B_1) = E[u/(u+h)] ≥ u/(u+a+b+t+v).

The lower good-pair arrow B_1→B_0 requires Pr(B_0<B_1)<1/3 in a counterexample. Rearranging yields (5). Applying duality gives (6).

For (7), remove C_4. Its window starts immediately after T_1 and ends immediately before B_5. It contains all elements of C_2,C_3 and at most all elements of C_0,C_6. In particular it contains B_2. Hence h≤u+b+c+v, and the event that B_4 is the first element of this window implies B_4<B_2. Therefore

Pr(B_4<B_2) ≥ E[t/(t+h)] ≥ t/(t+u+b+c+v).

The lower good-pair arrow B_2→B_4 requires Pr(B_4<B_2)<1/3. This gives (7).

The displayed forced arrows can be checked directly: D_Q(1)=D_Q(0)=empty and U_Q(0)\U_Q(1)=empty; D_Q(2)=D_Q(4)={1} and U_Q(4)\U_Q(2)=empty. Their bottom lifts apply for all positive weights. The top arrow for (6) is the dual of the first.

### Finite tail range after fixing the five central weights

Set A=a+b+t and B=c+d+t. Because the weights are integers, (5)–(6) imply

u+v ≤ A+B−2,
u ≤ floor((2A+B−3)/3),
v ≤ floor((A+2B−3)/3).

Thus, once (a,b,c,t,d) are fixed, only finitely many pendant-chain lengths u,v survive these simple necessary conditions. This does not bound the five central weights or the total order globally.

## 5. An additional binomial necessary inequality

The same C_0 insertion window gives a useful nonlinear condition. For a fixed outside extension, let h be its window length and let k be the rank of T_2 in that window, counted starting at 1. Then k≥a+b and h≤a+b+t+v. The exact conditional probability that all u C_0 elements precede T_2 is

binom(k+u−1,u)/binom(h+u,u).

Consequently

Pr(T_0<T_2) ≥ binom(a+b+u−1,u)/binom(a+b+t+v+u,u).

The forced top arrow T_2→T_0 therefore makes the following necessary:

3 binom(a+b+u−1,u) < binom(a+b+t+v+u,u).             (8)

The inequality obtained by applying the displayed dual weight transformation is necessary as well. These are safe bounds, not claimed sharp.

## 6. Exact checks and smallest surviving singleton pattern

The accompanying standard-library script weighted_core_formula.py compares (1)–(4) with an independent ideal DP on the actual labelled inflated poset. The DP adds the tested pair as an extra precedence constraint and counts the resulting ideals; it does not reuse the double-sum decomposition. Validation output is in formula_validation.json.

For (u,a,b,c,t,d,v)=(2,1,1,1,1,1,2),

Z=315,
N(B_1<B_0)=N(T_6<T_5)=202,
N(T_0<T_2)=N(B_3<B_6)=96.

Thus B_1,B_0 are a concrete balanced pair, with probability 202/315. This is an example, not an all-weight inference.

## 7. Boundary of this result

The double sum, endpoint formulas, duality, linear cone, and binomial inequalities above have direct proofs. Finite tests check their implementation only. There is no claim that all positive chain inflations are now excluded, that the quotient law is uniform, or that acyclic structural constraints suffice for a counterexample. The relevant good-pair theorem is Zaguia, Definition 1 and Theorem 2, https://arxiv.org/html/1610.00809 ; its precise use was audited in the main reductions document.

## 8. Two proved corollaries

### Arbitrarily long pendant chains, five singleton central blocks

If w1=w2=w3=w4=w5=1, every positive choice of w0,w6 gives a balanced pair somewhere in the inflation.

Proof. A counterexample would require u,v≥2 by the previously proved endpoint-cycle filter. Here A=B=3, so the finite tail bounds force u,v≤2. The only remaining vector is (2,1,1,1,1,1,2), whose displayed endpoint probability 202/315 is balanced. QED.

This is an infinite two-parameter subfamily exclusion, not a proof for arbitrary weights on the other five blocks.

### Four-ray restriction when the four spine blocks are singletons

Suppose only w1=w2=w3=w5=1, and put t=w4. Every counterexample must have

(u,v) in {(t+1,t+1),(t,t),(t,t−1),(t−1,t)},

subject also to u,v≥2.

Proof. Now A=B=t+2, so u,v≤t+1. Put x=t+1−u and y=t+1−v; these are nonnegative integers. The three linear inequalities become

y≤2x, x≤2y, x+y≤3.

The only nonnegative integer solutions are (x,y)=(0,0),(1,1),(1,2),(2,1), yielding the displayed rays. QED.

No claim that every point of these four rays has been excluded is made here.

## 9. Exact rejection counts in the already validated box

The separate script screen_tested_box.py exhausts precisely the same 2,187 vectors with every weight in {1,2,3}. All comparisons are integer comparisons, with closed balance thresholds handled exactly. The full output, including all survivors, is screen_tested_box.json.

Tests are applied in the following order; each line gives the number passing that test alone among all 2,187 vectors, followed by the number remaining cumulatively:

- Singleton ports u,v≥2: 972 alone; 972 cumulative.
- Linear (5), for u: 2,043 alone; 927 cumulative.
- Linear (6), for v: 2,043 alone; 883 cumulative.
- Linear (7), for t: 2,043 alone; 874 cumulative.
- Binomial (8): 1,413 alone; 847 cumulative.
- Dual binomial inequality: 1,413 alone; 829 cumulative.
- Exact Pr(B1<B0)>2/3: 1,732 alone; 616 cumulative.
- Exact Pr(T6<T5)>2/3: 1,732 alone; 441 cumulative.
- Exact Pr(T0<T2)<1/3: 247 alone; 42 cumulative.
- Exact Pr(B3<B6)<1/3: 247 alone; 25 cumulative.

Thus this short rejection menu does not exclude every tested vector. Its 25 survivors are menu survivors only; they are not asserted to be counterexamples.

The smallest surviving vector, ordered by total cardinality and then lexicographically, is

w=(2,1,1,1,2,1,2), of order 10, with e(P)=1,121.

Its four tested endpoint numerators are respectively 766,766,315,315. These all satisfy their forced strict thresholds. However, checking every actual incomparable pair by an independent ideal DP gives

delta(P)=454/1121.

For example, Pr((2,1)<(4,1))=667/1121, so that pair is balanced; equivalently, its smaller orientation probability is 454/1121. The dual maximizing pair is (3,1),(4,2), with Pr((3,1)<(4,2))=454/1121. There are seven balanced unordered pairs in this example, all recorded in the JSON. Here (i,r) denotes the rth element of block i.

This concrete residual identifies a limitation of the chosen four-probability menu, rather than any failure of the 1/3–2/3 conjecture or the structural-good-pair filter. In particular the balanced pair (2,1),(4,1) concerns another known forced arrow not included in this four-probability menu.

## 10. Frozen artifact status

This file, weighted_core_formula.py, formula_validation.json, screen_tested_box.py, and screen_tested_box.json form the bounded result. The implementation validation passed all 2,187 vectors, 13,122 independent oracle counts, 2,187 duality checks, and 6,561 bound checks. The counts are arithmetic verification; the general claims have the proofs above. Independent mathematical audit is pending at the time of this freeze. No larger weight range or extra ray-family theorem is part of the result.
