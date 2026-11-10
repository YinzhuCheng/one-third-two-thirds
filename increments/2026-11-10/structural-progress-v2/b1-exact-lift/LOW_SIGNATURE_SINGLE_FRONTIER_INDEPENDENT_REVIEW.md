# SG1 independent mathematical review

Date: 2026-11-10 UTC. Reviewer: audit_alpha2_four, not involved in SG1 derivation. Earlier authorship of the underlying CT1 fiber method is background, not participation in the new m6,k7 deadline inequalities.

**PASS.** Reviewed source `LOW_SIGNATURE_SINGLE_FRONTIER_CLOSURE.md`, SHA256 `0c49b5788c39ba89f3ab1562ae00029a1ae738cc07316a3a5bcd0fecca51bcb9`, independently verified. Both degree gates are analytic fixed-pair sufficient conditions, and the stated ordinary consequences correctly distinguish the separately reviewed RC1 alternative.

## Actual typed fibers and kernel

The missing-x low-support minimum f is outside E, belongs to Mx-E, and hence forces m<=k-1<=6. It is above u and has at least two missing T-root neighbors outside C, giving C-degree<=8; empty signature strengthens this to7. The other selected minimum is incomparable with it. Thus actual degrees give(R<=7,S<=7) in A and(R<=8,S<=6) in B. All further insertion constraints are true successor deadlines in the same fixed retained gamma. Neither selected minimum has a retained predecessor. No artificial degree bound is used.

Both orders share those same R,S. Distinct assigned gaps have one order; equal gaps have two original words. Thus W=(R+1)(S+1)+min(R,S)+1 is exact, and the displayed two sums cover every actual word exactly once. Gamma padding and its untouched suffix have the same count-preserving interpretation as CT1. There is no distributional assumption on the relative selected orders or on different gamma words.

If c is first, the initial missing-x run is at most its gamma gap. If f is first, the first selected x-containing point has at most b gamma labels plus f before it, so hx<=min(7,b+1). The initial E run stops at f and is at most a. Relaxing q to min(6,a) is legal because a<=b and this q cap is at most the h cap. For actual q>=1, first raising h and then q weakens the kernel in the required direction. For q0 the actual F>=48 and each displayed relaxed value is at most48. Removing9(hy+hz) is safe. Thus the worst-cell G and Psi are valid throughout both rectangles and every m<=k allowed by the typed premise, including m0 via its separate stronger bound.

## Independent deadline algebra

Direct summation of Psi_a at h7 gives48,82,68,14,-72,-182,-308,-434 for s0,...,7. Each P_s has nonpositive slope in h; in particular the first four remain positive for1<=h<=7. Differencing in R adds exactly one f-first column and one c-first row, giving the displayed increment identity. For n1,...,4 when S>=4, substitution yields92+46S,80+36S,68+18S,64-8S. All are positive. At n5, S4 gives-16 and S>=5 gives76-42S<0. At n6 the only additional row, when present, yields-308-84(S-5)=112-84S<0. At n7 the only row-present case is S7, yielding-434-126=-560. Row-absent cases use negative P_S(7). For S<=3 the early formulas and then positive P_S prove all increments positive. This verifies the endpoint reduction over the complete actual deadline rectangles, including zero deadlines and caps smaller than the displayed maximum.

Independently adding the new f-gap row at fixed R gives

    D_s=sum_(b=s)^R Psi(s,b)+sum_(a=0)^s G(a).

At R7 this evaluates to362,146,-14,-126,-198,-238,-238; at R8 through s6 it gives396,132,-68,-212,-308,-364. These are elementary finite arithmetic-series evaluations, independently checked rather than adopted from a positivity table. Their nonincreasing order proves discrete concavity in S. The R7 endpoint values are432 and126; the R8 endpoint values are480 and56. The other R endpoint is48(S+2)>=96. Therefore T>=96 throughout A and T>=56 throughout B. The word-count maxima are(8*8+8)=72 and(9*7+7)=70. Dividing gives the claimed conservative mean margins4/3 and4/5. Multiplication by every actual fiber cardinality and the original full-event identity complete both fixed-pair proofs without OLD moment.

## Ordinary consequences and realizability

A signature{x} C-minimum has original C-degree<=8, so A applies if a distinct missing-x low-support minimum exists. Otherwise, every minimum of Mx has signature yz: Mx is an ideal, so its minima are C-minima; absence of support<=1 there forces the only missing-x support-two signature yz. Every point of Mx lies above such a minimum and therefore also has signature yz. This is precisely the root-cover hypothesis needed by RC1. The unique-x-frontier branch with signature{x} is thus ordinary-paid using the separately reviewed RC1 theorem, without asserting that RC1 pays fixed u/b. For signature xy or xz, C-degree<=9 and an empty-signature minimum permits B as claimed.

The six-chain E plus singleton c,f example is legal: each selected point has C-degree7; f has full degree10; c has full degree9 for signature{x}, or8 for signature xy. The point x has degree10 and u degree9; other roots and E labels satisfy the bound. In the first example y,z are twins; in the second their exclusive upper differences are{c} and empty, an original VG configuration. These are feasibility examples, not unguarded population witnesses.

No gap found. No object scan, LE DP, moment transfer, union-FKG assertion, freely chosen tail weights, or external modification is used. This is an internal independent audit, not external peer review or formal verification.
