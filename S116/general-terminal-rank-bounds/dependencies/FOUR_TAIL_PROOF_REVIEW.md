# Independent audit: four-element terminal-chain certificate

Audit date: 2026-10-10 (UTC). **Verdict: PASS, with no mathematical correction required.**

## Frozen target and claim

- Certificate: `FOUR_TAIL_CERTIFICATE.md`, SHA-256 `227708fc40a94df919101bcd6815e2191a8e45fd7c9676b222aafa74baa0ab3c`.
- Companion verifier: `verify_four_tail.py`, SHA-256 `96ef9375351cda862f832e102baa577c92778fdc487dbba4ed4e9f45efb407d5`.
- Source-result JSON: SHA-256 `a02196ea9e99e2e547f9ad7be81af20c80c80424699ded4bc985540b3db1ba7c`.
- All six original files are preserved unchanged under `source_snapshot/`. Their source manifest is preserved there, and the audit manifest binds every preserved file.

The verified theorem concerns exactly the chain inflations of the quotient with covers

`0<3; 1<2,4; 2<3,6; 3<5; 4<5`,

with weights `(u,a,b,1,t,1,4)` for all positive integers `u,a,b,t`. Every such actual labelled poset has a balanced incomparable pair under uniform counting of its complete linear extensions.

This is an unbounded mathematical theorem. The audit does not infer it from a finite box.

## 1. Actual conditional law

Uniform volume in the actual order polytope gives each complete labelled linear extension a simplex of volume `1/N!`. It therefore produces precisely the uniform extension law, without a quotient-uniformity assumption.

Condition on every coordinate in C1 and C2, and let their respective maxima be r,s. Almost surely `0<r<s<1`. With x=C3 and z=C5, integrating C0 and C4 contributes `x^u/u!` and `(z-r)^t/t!`. The remaining support is `s<x<z<1`. C6 is a separate ordered four-coordinate simplex in `(s,1)`, of constant volume `(1-s)^4/4!`. Thus its sorted sample is conditionally independent of `(x,z)`; its four ordered coordinates are not being asserted mutually independent.

After `x=s+(1-s)h`, `z=s+(1-s)y`, the joint law on `0<h<y<1` has density proportional to

`[s+(1-s)h]^u [s-r+(1-s)y]^t`.

All binomial coefficients and all associated powers of `s, s-r, 1-s` are positive on the conditioning support. This is a finite positive combination of `h^k y^ell`, with the mixture weights obtained by multiplying each coefficient by its monomial integral and normalizing. No assumption is made about the induced law of r,s. Null boundary values need no separate conditioning formula.

## 2. Triangle identities and strict certificate

Direct integration gives

`Z(k,ell)=1/((k+1)(k+ell+2))`,

`E[h^j]=(k+1)/(k+j+1) * (k+ell+2)/(k+ell+j+2)`,

`E[y^j]=(k+ell+2)/(k+ell+j+2)`.

Given h, the rank R of x among C6 has the binomial law Binomial(4,h), because the unordered sample behind the sorted chain is independent uniform sampling. Therefore the stated formulas for A=Pr(F3<x), B=Pr(x<F4), and C=Pr(F4<z) are exact.

The audit derives the cleared-denominator polynomial directly, without importing the source polynomial function. Its formal sparse-polynomial coefficients exactly equal equation (4). Substitution `n=k+ell` gives exactly the five stated small-k quadratics. For k=1,2,3,4, the reduced discriminants are respectively `-16271, -14087, -32903, -215`, with positive leading coefficients; k=0 has positive coefficients. Formal substitution `k=d+5` gives exactly the stated 12-term positive polynomial, including the positive constant 3060.

These are polynomial identities for symbolic variables, not evaluations on a grid. They prove strict positivity for every integer k,ell>=0. The denominator `3(k+4)(k+5)(n+5)(n+6)` is positive throughout. Hence

`12 A + 15 B + C < 56/3`.

For any fixed conditioned r,s, the mixture is finite, so its gap is strictly positive. Averaging its strictly positive, bounded measurable gap over the actual conditioning law remains strictly positive. A uniform lower bound independent of r,s is unnecessary.

## 3. Two rank-atom bounds

The marginal identity in the certificate is correct. Explicit normalized Beta(m+1,2) weights for a triangle monomial are

`w_m = 1 / ((ell+1)(m+1)(m+2) Z(k,ell))`, for `k<=m<=k+ell`.

They are positive and sum to one. Independent factorial-beta integration yields the claimed beta-binomial formula and the ratio of consecutive atoms. The ratio numerator minus denominator is exactly `(j-4)m+3j-4`.

For j=1 this is negative for every m>=0, so the maximum is `4/15` at m=0. For j=2 it is positive at m=0, zero at m=1, and negative afterward; the maximum `9/35` occurs at m=1,2. Both maxima are strictly less than 1/3. The two successive mixture operations preserve these bounds.

The certificate correctly avoids a false rank-3 extension: the Beta(6,2) component gives `Pr(R=3)=56/165>1/3`. This generic mixture example is not being called a counterexample poset.

## 4. Good-pair dependency and endpoint orientations

The primary source was checked directly: Imed Zaguia, *The 1/3-2/3 Conjecture for ordered sets whose cover graph is a forest*, arXiv:1610.00809, Definition 1 and Theorem 2, https://arxiv.org/html/1610.00809 . These state a sufficient good-pair condition, allowed in the order or its dual, and that a good pair guarantees a balanced pair somewhere in the poset.

The required consequence is legitimate: if the structural condition holds but the corresponding orientation probability is <=1/2, the good-pair theorem already supplies balancedness. In a poset with no balanced pair that probability must therefore exceed 1/2, and exclusion of the closed interval `[1/3,2/3]` strengthens it to `>2/3`.

The three uses are:

1. In P, choose `(a,b)=(F1,x)`. Then `D(F1)=C1 union C2` is contained in `D(x)=C0 union C1 union C2`, and `U(x) minus U(F1)={z}`. Thus `Pr_P(F1<x)>2/3`.
2. In the dual P*, choose `(a,b)=(F4,x)`. The structural condition reads `U(F4) subset U(x)` and `D(x) minus D(F4)=C0`, a chain. Its probability in the dual is `Pr_P(x<F4)`, hence `>2/3`.
3. In the dual P*, choose `(a,b)=(z,F4)`. Their original upsets are empty, and `D(F4) minus D(z)={F1,F2,F3}`, a chain. Its probability in the dual is `Pr_P(F4<z)`, hence `>2/3`.

All pairs used are incomparable in the actual inflated poset. The audit explicitly constructs their strict downsets and upsets independently, checking the displayed set equalities on all tested vectors. The equalities also follow immediately for arbitrary positive block lengths. A missing orientation is not itself asserted to be a balanced displayed pair; the structural theorem may locate balancedness elsewhere.

## 5. Rank crossing and contradiction

Put `a_i=Pr(F_i<x)`. Chain order gives `a_i-a_(i+1)=Pr(R=i)`. In a poset without a balanced pair, every `a_i` lies below 1/3 or above 2/3. Starting from `a_1>2/3`, a jump to `a_2<1/3` would require an atom greater than 1/3, contradicting `Pr(R=1)<=4/15`. Thus `a_2>2/3`. The identical argument using `Pr(R=2)<=9/35` yields `a_3>2/3`.

The three probabilities A,B,C then all exceed 2/3, giving

`12A+15B+C > 28*(2/3)=56/3`.

This contradicts the strict certificate. Endpoint equalities at 1/3 or 2/3 already give a balanced pair and introduce no gap in the argument.

## 6. Independent exact computations

The independently written verifier uses reversed vertex labels and a forward dynamic program on actual labelled order ideals. It propagates event-count vectors to full extensions; it does not use the source's suffix/prefix event algorithm, source transitive-closure routine, or source polynomial routines.

It compares exact extension totals, five rank-event counts, and the F4<z count against both the source verifier and an unconditional exact rational integration. For the latter, set

`q0=r, q1=s-r, q2=x-s, q3=z-x, q4=1-z`.

The base polynomial is `q0^(a-1) q1^(b-1) (q0+q1+q2)^u (q1+q2+q3)^t`. The total C6 volume contributes `(q2+q3+q4)^4/4!`; rank j contributes `q2^j(q3+q4)^(4-j)/(j!(4-j)!)`; the F4<z event contributes `(q2+q3)^4/4!`. The other fixed denominator is `(a-1)!(b-1)!u!t!`.

Each positive polynomial term is integrated on the standard four-dimensional simplex using `integral q^e = product(e_i!)/(sum(e_i)+4)!`. Here the latter factorial is exactly N!. Multiplication by N! yields integer event counts, all matching both DPs. This cross-check integrates out the full actual law of r,s as well, including the C1/C2 multiplicities.

Both ordinary Python and `python -O` pass with byte-identical JSON results and per-vector records:

- 640 actual labelled posets: all 625 vectors with u,a,b,t in 1..5, plus 15 specified larger/asymmetric vectors, up to `(8,8,8,1,8,1,4)`.
- 108,447 labelled ideals processed by the independent DP.
- 4,480 exact unconditional volume/count comparisons.
- 8,649 triangle moment checks; 4,805 explicitly normalized Beta-mixture atom equalities.
- 5,005 factorial-beta and atom-ratio checks; 64 exact positive conditional-mixture examples.
- The source-box largest rank-3 atom is exactly `1432380/4451621`.
- The source-box minimum certificate gap is exactly `291260/1483581`.
- Exactly 7 source-box vectors satisfy all three forced endpoint inequalities, reproducing the source report.

The original verifier was also replayed independently from byte-identical copies in ordinary and optimized mode. Its two complete reports match the frozen source report exactly. No correctness check in the independent script uses a Python `assert`, so optimization cannot disable it.

## 7. Scope and exclusions

The four-tail theorem requires only the cited good-pair theorem externally. It does not require the prior long-tail theorem, the prior `v>=t+1` integral theorem, a minimal-counterexample weight cone, or any finite exhaustive classification.

The certificate's contextual reduction to remaining terminal lengths `{2,3}` additionally relies on previously established exclusions, including the handling of v=1 and any cited residual inequalities. Those prior statements are not newly proved by this audit. They must retain their own provenance if included in a combined release.

This audit does not establish the unbounded v=2 or v=3 slices, the general seven-weight family, the full 1/3-2/3 conjecture, or balancedness of one fixed named pair for every weight vector. It does not validate a rank-3 atom bound below 1/3, assert the previously failed two-probability inequality outside its proved scope, or authorize publication or modification of any repository or earlier release.

Only local audit files were created; the original source directory was not modified.
