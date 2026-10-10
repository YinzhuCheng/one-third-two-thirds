# Five eight-point cores require at least two nonsingleton chains

## Statement and scope

For each frozen class C08, C09, C11, C14 and C15, every positive-integer chain inflation with at most one nonsingleton block has a balanced pair. Consequently a counterexample on any of these five cores must have at least two nonsingleton blocks, hence order at least 10. This strengthens their previous lower bound of one block. It does not exclude any class for arbitrary support, and is separate from the C13 four-block theorem.

All probabilities refer to uniform actual labelled linear extensions, never uniform core extensions or uniform outside extensions. The strict relation masks and original labels are copied in certificate.json. The proof uses the previously independently audited necessary linear inequalities only for three families; the other 37 single-block families and all five zero-support cases have direct certificates.

## 1. Exact polynomial counts for one variable chain

Let block i have length t and all seven outside blocks be singletons. Delete block i. For a fixed linear extension sigma of the outside poset, let L be the last predecessor position (or start sentinel) and R the first successor position (or end sentinel). Every predecessor is below every successor, so L<R. Let h=R-L-1 be the number of elements strictly within this legal insertion window. These elements are all incomparable with block i; 0<=h<=7.

The number of insertions is f_h(t)=binomial(t+h,h). Conditional on this sigma, all its insertions are equiprobable. The unconditioned extension count Z(t) is the sum of f_h(t) over all outside extensions. Thus sigma's marginal weight is proportional to f_h(t), not uniform.

For a comparison between two outside singleton vertices a,b, the favorable count from a fiber is f_h(t) if a precedes b in sigma, and zero otherwise. For a comparison between the variable chain's bottom/top and an incomparable singleton x:

- If x is left of the window, both favorable counts are zero.
- If x is right of the window, both favorable counts are f_h(t).
- If x is the r-th outside element in the window, 1<=r<=h, the bottom numerator is f_h(t)-f_(h-r)(t), and the top numerator is f_(r-1)(t).

These are literal extension counts. Summing them makes Z and each endpoint-pair numerator polynomials of degree at most seven. The certificate stores their integer coefficients in the basis f_0,...,f_7. The discovery script enumerates every outside extension, not a uniform sample, and sums counts.

For a polynomial g of degree at most seven, the Newton identity at integer K is

    g(t) = sum_{k=0}^7 Delta^k g(K) * binomial(t-K,k).

For integer t>=K, all binomial factors are nonnegative. Thus nonnegative stored forward differences certify g(t)>=0 on the complete infinite integer tail. We apply this to 3N-Z and 2Z-3N, proving 1/3<=N/Z<=2/3. Z is a positive extension count for every positive t.

Exactly 36 of the 40 single-nonsingleton families have fixed-pair tail certificates. For 34, K=2 covers every nonsingleton length. The remaining two are C09 variable 2 and C09 variable 7, with K=3 and independently recounted t=2 witnesses. Every stored pair, polynomial, shift coefficient, and finite-prefix witness is in certificate.json.

## 2. Three inequality-bounded single-block families

For variable block 6 in C09, C14 and C15, the audited necessary inequality is 2w6 < sum of incomparable weights. Exactly five core vertices are incomparable with block 6. When all other weights equal one, any hypothetical counterexample therefore has 2t<5, giving t=2 because t>=2 is integral.

The sole remaining vector in each case has a directly counted balanced pair:

- C09: Pr(B0<B2)=137/400.
- C14: Pr(B0<B2)=131/374.
- C15: Pr(B2<T6)=239/374.

These three complete all-positive-integer families are excluded. The verifier independently reconstructs the appropriate structural witness for the necessary inequality from the relation sets.

## 3. A general adjacent-chain-rank lemma

Let C=(c_1<...<c_t) be any chain block in a chain inflation, and let M be the total number of outside elements in blocks incomparable with C. For any outside element x incomparable with C, put p_k=Pr(c_k<x). Then p_k is nonincreasing and

    0 <= p_k-p_(k+1) <= M/(t+M),       1<=k<t.

Proof. Remove C and condition on any outside linear extension sigma under the actual full-extension law. Use its legal window as above, now with arbitrary outside chain lengths. Its h elements are incomparable with C, so h<=M. If x is outside the window, it is either before every c_k or after every c_k, and the difference is zero.

If x is the r-th outside element inside the window, then p_k-p_(k+1) within this fiber is the probability that precisely k elements of C lie before x. In the uniform shuffle, this makes x occupy the fixed window position k+r. This event is contained in the event that position k+r is occupied by any outside element. Uniform shuffling selects the h outside positions uniformly among all h-subsets of t+h positions; the latter event has probability h/(t+h). Thus the conditional difference is at most h/(t+h)<=M/(t+M). Averaging these pointwise bounds under sigma's true induced probability preserves the inequality. No uniform outside law is assumed. QED.

Corollary. If t>=2M, p_1>=2/3, and p_t<=1/3, some pair (c_k,x) is balanced. Equality at an endpoint already suffices. Otherwise the decreasing sequence crosses from above 2/3 to at most 2/3, with each drop at most 1/3, so its first crossing value is strictly greater than 1/3.

## 4. The remaining C09/block-1 family

Let C09 have w1=t and all other weights one. Its incomparable blocks are {2,3,5,6,7}, so M=5. Use outside vertex 3. In the f_h basis, the complete counts are

    Z = [4, 7, 10, 9, 6, 3, 0, 0]
    N_bottom = [-7, -4, -1, 3, 6, 3, 0, 0]
    N_top = [11, 11, 3, 0, 0, 0, 0, 0].

The Newton coefficients of 3N_bottom-2Z at K=10 are

    [10608, 5275, 1771, 390, 51, 3, 0, 0],

and those of Z-3N_top are

    [17340, 6967, 2029, 408, 51, 3, 0, 0].

All are nonnegative. Thus for every integer t>=10, Pr(B1<B3)>=2/3 and Pr(T1<B3)<=1/3, while t>=2M. The corollary supplies a balanced pair using a possibly internal rank of C1. This is deliberately not a claim that one fixed endpoint pair remains balanced. The finite lengths t=2,...,9 have explicit exact witnesses in certificate.json.

## 5. Exhaustiveness and independent verification

A poset with at most one nonsingleton has either all weights one or exactly one of the eight choices of variable block. The certificate covers all 5*8=40 exact-support families once: 36 fixed-pair polynomial families, three inequality-bounded families, and the single rank-crossing family. All five all-singleton cases are independently recounted too.

Run `python verify.py`. It imports neither the author's occupancy recurrence nor the outside-fiber enumeration code. Its labelled-element predecessor-mask DP independently counts each denominator and both pair orientations at t=1,...,8. The polynomial degree-at-most-seven theorem above means eight distinct exact evaluations certify every stored count-polynomial identity, including moving top endpoints. It independently checks all Newton coefficients, their signs, the integer tail domains, all finite witnesses, and complete 40-family coverage. This is a finite proof-certificate verification of infinite families, not extrapolation from a bounded experiment.

The verifier reports PASS. A separate research auditor is still appropriate before treating this as part of the canonical frozen catalogue. The theorem does not rely on the stage-A search's empirical 2-through-8 cutoff.
