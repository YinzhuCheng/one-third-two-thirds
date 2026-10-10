# Independent audit: general terminal-rank bounds

Date: 2026-10-10. **Final verdict: PASS for the frozen source hashes and precise scope below.**

## 1. Accepted mathematical scope

The quotient covers are `0<3; 1<2,4; 2<3,6; 3<5; 4<5`; its seven positive chain lengths are `(u,a,b,c,t,d,v)`. Probabilities always refer to uniformly chosen complete linear extensions of the actual inflated poset.

The proof establishes balancedness for each of:

- `d=1,v>=4`, with all other weights arbitrary;
- `d=2,v>=10`, with all other weights arbitrary;
- `d=3,v>=30`, with all other weights arbitrary.

Their order-dual versions hold under `(u,a,b,c,t,d,v) -> (v,d,c,b,t,a,u)`.

In every hypothetical no-balanced-pair poset, the necessary product restriction is

`3(c)_v < (c+d+1)_v`, equivalently `3 product_{i=0}^d(c+i) < product_{i=0}^d(c+v+i)`.

Together with the previously independently audited all-spines-at-most-three census theorem, these results prove **every `(u,1,b,c,t,1,v)` is balanced for arbitrary positive `u,b,c,t,v`**. This includes and settles the earlier single-inner-spine residual slices. The finite-computation dependency is substantive and explicitly retained.

When a,d lie in {1,2,3}, the proof further gives a finite necessary region: u,v<=29, b,c<=90, t<=104 and N<=348. It does not exclude that entire region.

No theorem for all seven unbounded weights is proved. The numbers 5,10,30 are sharp for the unrestricted beta-binomial interior-atom lemma, not for the poset balance problem. The first threshold is bypassed at v=4 by the triangle certificate. No fixed pair is asserted balanced for all weights.

## 2. Independent conditional-law derivation

Fix all C1 and C2 coordinates under the actual uniform order-polytope volume law, and let their maxima be r<s. Put L=1-s, let x=top(C3), z=bottom(C5), h=(x-s)/L and y=(z-s)/L.

All C6 coordinates form an independent sorted sample of v uniform points on (s,1): the only external inequalities involving C6 are that its elements follow C2. Thus, conditional on h, the count R of C6 elements below x is Binomial(v,h).

For c=1, integrating C0 gives `(s+Lh)^u`, up to a common positive constant. For c>=2, integrate the bottom C3 coordinate q and the c-2 intervening coordinates:

`integral_0^h (s+Lq)^u (h-q)^(c-2)/(c-2)! dq`.

The coefficient of `h^(i+c-1)` is `binom(u,i)s^(u-i)L^i i!/(i+c-1)!`, giving the author's A_c(h) for all c>=1. Integrating C4 and the d-1 C5 coordinates above z supplies `(s-r+Ly)^t(1-y)^(d-1)`. There are no omitted h- or y-dependent factors.

A second independent positive expansion for each monomial in y is

`integral_h^1 y^ell(1-y)^(d-1) dy = B(ell+1,d)(1-h)^d sum_{j=0}^ell binom(d+j-1,j) h^j`.

This identity, multiplied by A_c, yields `h^(c-1)(1-h)^d P(h)` with nonnegative coefficients in P, hence a probability mixture of Beta(c+k,d+1), 0<=k<=u+t. Normalization multiplies coefficient p_k by B(c+k,d+1), as the source correctly states. This argument is uniform on every interior fiber; averaging uses the actual induced r,s law, with no claim of quotient-uniformity or uniform outside extensions.

The independent program verifies this positive expansion against direct alternating-polynomial antiderivatives at exact rational r,s,h values in 162 parameter configurations. Those checks validate implementation; the displayed identities prove the unbounded statement.

## 3. Actual-vertex structural endpoints

Let F1<...<Fv be C6 and x=top(C3). Reconstructing the full actual-vertex order gives:

- `D(F1)=C1 union C2 subset D(x)`;
- `U(x) minus U(F1)=C5`, a chain;
- `U(Fv)=empty subset U(x)`;
- `D(x) minus D(Fv)=C0 union (C3 minus {x})`, a chain because C0 precedes all C3.

All compared endpoints are incomparable. The established good-pair consequence therefore forces `Pr(F1<x)>2/3` and `Pr(x<Fv)>2/3` in the absence of any balanced pair. At v=1 these are complementary and impossible; duality similarly excludes u=1.

For d=1, z=bottom(C5)=top(C5), both U(Fv) and U(z) are empty, and `D(Fv) minus D(z)=C6 minus {Fv}` is a chain. Hence `Pr(Fv<z)>2/3` is forced. For d>1, this third argument applies to top(C5), not bottom(C5). The author's source explicitly respects this distinction.

The audit checks the full set equalities and incomparability on all 202 independently counted vectors. It also reconstructs the quotient involution `(0,1,2,3,4,5,6)->(6,5,3,2,4,1,0)` and verifies relation reversal directly.

## 4. Exact unbounded rank bounds

For Beta(alpha,beta) mixed Binomial(n,h), the atom is

`p_j(alpha)=binom(n,j)(alpha)_j(beta)_(n-j)/(alpha+beta)_n`.

The adjacent-alpha ratio is `(alpha+j)(alpha+beta)/(alpha(alpha+beta+n))`; its numerator minus denominator is `j beta-(n-j)alpha`. Thus the sequence is unimodal and its all-integer-alpha maximum is located exactly at the crossing, with an adjacent two-point plateau when the crossing is integral. No finite alpha cutoff is used.

For j=1 and the claimed n thresholds, the maximum is at alpha=1, with value `n beta/[(n+beta-1)(n+beta)]`. Its derivative has sign `beta(beta-1)-n^2`; this is negative throughout each stated range and the starting value is below 1/3.

For j=n-1 the maximizing alpha values are `beta(n-1)` and one more. Direct factorial cancellation gives the author's product maximum. Multiplying its 1/3 inequality by the positive denominator gives exactly the source P_beta. Independent polynomial multiplication gives, after n=N+z:

- beta=2, N=5: `6+15z+3z^2`;
- beta=3, N=10: `96+1202z+249z^2+13z^3`;
- beta=4, N=30: `603960+1425418z+140683z^2+4718z^3+53z^4`.

All coefficients are strictly positive; this proves the last-rank bound for unbounded n. Middle ranks for n>=6 are uniformly bounded by the conditional binomial peak, at most `B(6,2)=80/243<1/3`. Its symmetry, monotonicity toward the middle, and monotonicity in n follow from the exact consecutive ratio and logarithmic derivative given in the source. The sole n=5 middle cases at beta=2 have exact maxima 3/14 and 5/21. No small n is omitted.

The numerical audit locates all-alpha maxima exactly for every rank from the stated threshold through n=100: 14,402 maxima, together with 7,500 exact ratio identities. These are implementation checks, not the proof of unboundedness.

Averaging the component bounds retains a strict uniform gap for each n. The first crossing of `q_i=Pr(x<F_i)` from below 1/3 has increment `Pr(R=i-1)<1/3`, so q_i lies below 2/3 and gives a balanced pair. If either required endpoint orientation fails, the good-pair consequence supplies balancedness elsewhere.

At the immediately preceding n values, the exact last-rank probabilities are 56/165, 1755/5236 and 1432049/4294719, all above 1/3. These certify generic-lemma sharpness only; they are not actual poset counterexamples. For beta>=5 the limiting maximum `(beta/(beta+1))^(beta+1)` exceeds 1/3, since it is increasing in beta and already equals 15625/46656 at beta=5. Thus no eventual uniform interior-atom threshold exists for d>=4 via this method. This limitation says nothing adverse about the main balance conjecture.

## 5. The arbitrary-c four-tail lift

At d=1 the joint density is a positive mixture of triangle monomials `h^k y^ell`, now restricted to k>=c-1. The frozen triangle certificate holds for every integer k,ell>=0, so restriction to that subset requires no additional inequality.

For v=4 let A=Pr(F3<x), B=Pr(x<F4), C=Pr(F4<z). The exact bound `12A+15B+C<56/3` and small atom bounds `Pr(R=1)<=4/15`, `Pr(R=2)<=9/35` apply. Together with the three forced endpoint orientations, they contradict absence of a balanced pair exactly as in the singleton-C3 proof.

The independent audit reconstructs the triangle certificate polynomial directly from its moment denominators, checks positivity for k=0,...,4 by the five quadratic discriminants, and checks all coefficients after k=5+q are positive. It additionally counts the inequality directly in 52 actual arbitrary-c v4 posets. This validates the lift without pretending the rank-3 atom has a false uniform 1/3 bound.

## 6. Product obstruction and complete five-parameter corollary

The moment `(alpha)_v/(alpha+beta)_v` strictly increases in alpha because each factor does. Every conditional component has alpha>=c and beta=d+1, so `Pr(Fv<x)>= (c)_v/(c+d+1)_v`. The forced opposite comparison makes this moment strictly less than 1/3, proving the necessary product inequality. Cancelling the factorials proves its alternate form for all positive integer c,d,v.

For a=d=1, the terminal theorem and its dual force u,v<=3, while the port contradictions force u,v>=2. At v=2 the moment bound becomes `c(c+1)/[(c+2)(c+3)]<1/3`; at c=3 it is 2/5, so c<=2. At v=3 it becomes `c(c+1)/[(c+3)(c+4)]<1/3`; at c=4 it is 5/14, so c<=3. Monotonicity excludes every larger c. Duality gives b<=u<=3. Thus all four spine weights lie in {1,2,3}.

The independently PASS weighted-seven-core census expressly proves balancedness for *every positive* u,t,v whenever a,b,c,d lie in {1,2,3}. Its scope is an infinite family justified by universal necessary bounds and exhaustive exact rejection of the finite cone, not an extrapolation from a tested cube. It therefore applies to every remaining vector here. This completely settles `(u,1,b,c,t,1,v)` under the stated dependencies.

A separate fresh exact computation gives an especially transparent cross-check. Using the earlier four strict universal inequalities, the new caps force t<=4. Exhaustive enumeration gives 41 vectors, grouped as 7,7,7,20 for ports (2,2),(2,3),(3,2),(3,3), with maximum order 18. The new `audit_reduced_corollary.py` builds all labelled elements, their predecessor masks and all reachable ideals. To count x<y, it forbids ideals containing y but not x. The resulting augmented-order recurrence counts precisely the desired complete extensions.

This fresh oracle computes all 1,760 actual incomparable-pair numerators and finds 429 balanced pairs in aggregate. Every one of the 41 vectors has a concrete balanced pair and a failed structural forced orientation. Complete rational witnesses are in reduced_normal.json. Its finite scope is complete after the proved bounds; the author's declared census dependency remains accurately stated.

### The further finite-region corollary

For fixed d, the product ratio increases with c and decreases with v. At the maximal permitted v=3,9,29 for d=1,2,3, respectively, the exact ratios at candidate adjacent-spine caps c=3,19,90 are 2/7,19/58,83421/250954, each below 1/3. At the next integers they are 5/14,308/899,3049501/9078630, each above 1/3. This proves the universal caps 3,19,90 by monotonicity. Duality gives the same bounds from a on u,b. Thus a,d<=3 implies u,v<=29 and b,c<=90. The established strict shuffle bound yields 2t<b+c+min(u,v)<=209, hence t<=104. Summing gives N<=348. These are safe necessary bounds, not an assertion that all vectors up to order348 have been enumerated or excluded.

## 7. Independent computational design and reproducibility

`audit.py` uses no author imports and compares two distinct exact constructions on 202 weight vectors:

1. Chain-prefix ideal DP, recording the number of C6 elements already present when top(C3) is inserted.
2. Uniform simplex-gap integration. For c=1, integrate over `0<r<s<x<z<1`. For c>=2, also retain p=bottom(C3), with `0<r<s<p<x<z<1`. Expand all positive linear forms in simplex gaps and integrate each monomial using its factorial formula. The total event count is exactly N! times its volume.

Every histogram agrees term by term; every simplex count is checked integral. The grid varies all four of u,a,b,t in {1,2}, c in {1,2,3}, and the boundary terminal cases. Ten additional asymmetric vectors include c=12,d=3,v=30 and a d=4 case to check the conditional law outside the theorem's rank-bound scope.

The audit checks 2,058 actual interior atoms in the claimed threshold region, 146 actual rank-crossing instances, the product lower bound at every vector, and the structural differences above. These checks do not replace the unbounded arguments.

Both independent scripts run using only the Python standard library and explicit exception checks, with no assert statements. Normal and `python -O` result files agree byte for byte; all result fields are deterministic, so no keys are ignored.

No author source is edited. Author replay, once frozen, runs only from local execution copies. No remote publication, upload, or external mutation is performed.

Reproduction commands, run in this audit directory:

```sh
python audit.py --output reproduced.json > reproduced.log
python -O audit.py --output reproduced_optimized.json > reproduced_optimized.log
cmp normal.json reproduced.json
cmp normal.json reproduced_optimized.json
python audit_reduced_corollary.py --output reduced_reproduced.json > reduced_reproduced.log
python -O audit_reduced_corollary.py --output reduced_reproduced_optimized.json > reduced_reproduced_optimized.log
cmp reduced_normal.json reduced_reproduced.json
cmp reduced_normal.json reduced_reproduced_optimized.json
sha256sum -c SHA256SUMS
```


## 8. Final frozen-source integrity and author replay

The source proof SHA-256 is `f5f62c0bf2e1224926c80f895b954e274bda134dfc025202a77935262f2cdefa`; the verifier SHA-256 is `0b3d5c20256d3b29b770ff6206a8cf4e5f031cb6c5b98969b8934f844c4e4143`. The complete source `SHA256SUMS` validated all 17 listed files. Every file, including that checksum list, has an identical copy in `source_snapshot/`; all seven declared proof dependencies match their separately frozen original files.

The author's final verifier was reviewed and rerun under normal Python and `python -O` from `author_normal/` and `author_optimized/`. Both reproduce the original verification report and reduced-case certificate byte for byte. The report covers 464 actual-extension vectors, 3,024 conditional moments, 9,032 all-alpha maxima, 144 arbitrary-c four-tail cases, and the complete 41-vector reduction. Its new closed extension-count cross-check also passes.

`compare_author_certificate.py` independently matches every one of the 41 author denominators and all 82 published balanced-pair and failed-forced-arrow witnesses against the fresh labelled-ideal all-pair oracle, after explicit conversion from author one-based labels to audit zero-based labels. No author counting code is imported for this comparison.

The source verifier uses only direct explicit checks, so optimization does not bypass validation. Source integrity, replay equality and dependency identity are recorded in SOURCE_INTEGRITY.json. MANIFEST.json records the accepted scope and audit artifacts; SHA256SUMS freezes every audit file except itself. No source correction was required.
