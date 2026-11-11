# Independent review of Sections 3–4

2026-11-11. PASS within the stated scope. I read READ_FIRST.md Sections 3–4 and independently enumerated every labelled permutation of each explicit example, without importing or executing the author's discovery or verification programs. The original manuscript was not modified. This review does not independently certify Virtanen's fixed-label inclusion-coupling theorem or any D9/D10 bank.

## 1. Five-point through-prefix counterexample

P has exactly a<d, a<e, b<c and their transitive consequences. J={a,b} is exactly the set of minima and is an ideal. The original uniform linear-extension law has 20 words: interleave the three-point fork (two extensions) and the two-chain (one extension), giving binom(5,3)*2=20.

For last(J)=2, the through-prefix set is {a,b}, with 12 words. For last(J)=3 the sets {a,b,c}, {a,b,d}, {a,b,e} each have two words. The words for {a,b,c} are bcade,bcaed; for {a,b,d}, adbce,adbec; for {a,b,e}, aebcd,aebdc. For last(J)=4 there are exactly adebc,aedbc, both with through-prefix set {a,b,d,e}. There are no other classes.

Thus the lower-layer atom {a,b,c} has mass 1/3 and has no containing upper-layer set. No coupling with C_3 subset C_4 can exist: its event c in C would require probability 1/3 at the lower layer to be at most 0 at the upper layer. This uses complete original-P counts, not uniform ideal sampling or a selected projection. Incomparable degrees are (2,3,3,3,3), so the example also satisfies global degree bounds 9 and 10. It refutes only a universal last-of-J inclusion bridge, not a specified project source contract or the balanced-pair conjecture.

The final label is a in 2/6 lower-layer words and 0/2 upper-layer words; the other words end J with b. This establishes the changing-mixture mechanism precisely. Conditioning separately on a fixed final label can be represented by adding the other J labels below it; that is a conditional application to a different augmented poset, not a proof about the changing untagged mixture.

## 2. Three-point before-prefix counterexample

For a<b and c independent, the complete extension list is abc,acb,cab. J={a,c} is an ideal (indeed all minima). At last(J)=2, the before-prefix sets are {a} and {c}, each with probability 1/2. At last(J)=3 the only set is {a,b}. The {c} atom has no inclusion neighbor. Incomparable degrees are (1,1,2). This counterexample and the five-point example are independent of any external coupling theorem.

## 3. Exact pivot-bank criterion and proof

Fix P and a label x. The legal before-x sets are precisely the ideals I of P not containing x such that D(x) is contained in I. No such ideal contains a strict successor of x. Every such set occurs with positive probability: concatenate an extension of I, x, and an extension of the remaining induced poset. The true conditional mass at size p is proportional to e(I)e(P minus (I union {x})).

For fixed coefficients, the stated identity is exact:

B(I)=sum_(y<x)c_y + sum_(x<y)d_y + sum_(y parallel x)d_y
     + sum_(y parallel x)(c_y-d_y)1[y in I].

Hence nonnegative differences for all incomparable y suffice for inclusion-increasing B, and nonpositive differences suffice for inclusion-decreasing B. Comparable y need no sign restriction: their contributions are constants. Nonnegativity of c_y,d_y is natural for the bank interpretation but is not needed for this algebraic monotonicity fact.

Necessity is also correct, and can be made explicit. For each y parallel x, take I=D(x) union D(y). This is an ideal, omits x and y, and contains D(x). I union {y} is also a legal before-x ideal. Both occur with positive mass by the concatenation argument. The change of B along this legal inclusion edge is exactly c_y-d_y. Thus an inclusion-increasing B on the whole legal-prefix lattice forces c_y-d_y>=0 for every incomparable y; decreasing gives the reverse inequalities. No degree, width, or maximality assumption is used. As a supplementary implementation check only, I tested this witness for all 407 naturally labelled posets of sizes 1 through 5 and all 4252 ordered incomparable pairs. The constructive argument, not that finite test, proves the unrestricted statement.

If the fixed-label inclusion-coupling theorem being invoked is accepted for the same P and x, applying B to that coupling gives the stated conditional expectation monotonicity for successive feasible ranks. This last implication is conditional on the external theorem. The same-sign criterion is an iff for set-function monotonicity, not an iff for expectation monotonicity: mixed coefficients can still yield monotone means in special posets. No claim in this review upgrades the external preprint's status.

## 4. Mixed and nonpivot examples

For b<v with u independent, the only extensions at ranks of u equal to 1,2,3 are ubv,buv,bvu. The bank 2*1[u<b]+1[v<u] has exact conditional means (2,0,1), so neither expectation direction holds. With pivot u, the incomparable differences are -2 for b and +1 for v. The prefix sets themselves are the nested chain empty,{b},{b,v}; it is the bank function, not an inability to couple those sets, that obstructs inference.

For the antichain {x,a,b}, conditioning on the before-x set yields E[1[a<b]|I] equal to 1/2,1,0,1/2 for I=empty,{a},{b},{a,b}, respectively. Since {a} subset {a,b} lowers the value and {b} subset {a,b} raises it, the function is neither inclusion-increasing nor inclusion-decreasing. The stated three values are correct.

For a nonpivot event entirely inside I, conditional extensions of I are uniform because every such extension has the same number of actual suffix completions; the ratio K_I/e(I) is therefore correct. The same reasoning applies inside the actual suffix. Cross-side events are deterministic. These conditional ratios do not acquire monotonicity merely by being conditional expectations.

## 5. Disposition

No correction to the mathematical assertions in Sections 3–4 is required. The explicit construction I=D(x) union D(y) supplies a short rigorous proof of the necessity sentence. Preserve these limitations:

- Universal multi-label last(J) inclusion coupling is false, even at degree 3.
- The counterexample does not refute fixed-label coupling.
- Same-sign refers only to differences for labels incomparable with the fixed pivot.
- Expectation transfer requires the same full P, fixed x, true prefix/suffix weights, and acceptance of the cited fixed-label theorem.
- Mixed/nonpivot failure examples establish limitations, not failure of the project's separately proved banks.

Source increment is zero; no ledger, original manuscript, repository, or external service was changed.
