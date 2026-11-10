# MF2: x-containing minimal frontiers

Date: 2026-11-10 UTC. Analytic extension proposed by the boundary coordinator and independently checked and written by the MF1 reviewer. This document is separate from the frozen, independently audited MF1 manuscript; it is not represented as having a second uninvolved audit of its own.

## Contract and extension

Use the exact original B1 lift and event identity of PROOF_CANDIDATE.md, actual Delta10, and m<=k<=7. No OLD seed moment is assumed. Select r distinct C-minimal physical labels each strictly above x; they need not have full xyz signature. Suppose each has original C-incomparability degree at most d.

For m>=1, the general frontier certificate B(r,d;m,k) of corrected MF1 holds unchanged:

    3K-N >= B(r,d;m,k)e(C)+2X+Y.

For m0 use the unconditional bound3K-N>=48e(C)+2X+Y instead, not the B formula. Here D=d-r+1 and

    B = sum_(t=0)^D [binom(D+r-t-1,r-1)/binom(D+r,r)]
        [48+(6-8q)h+4q(q-1)],
    h=min(k,t), q=min(m,h).

## Proof of the changed hypothesis

The selected labels remain an antichain of actual C-minima. Their legal gamma deadlines are at most d-(r-1), exactly as in MF1, and the selected order/position representation, padding convention, uniform distributive-lattice FKG comparison, and actual fiber cardinality summation are unchanged. The only use of a selected full signature in MF1's kernel step was to force the initial missing-x run to stop no later than the first selected token. A selected label strictly above x already does this, so hx<=min(k,H) still holds. The other missing-root runs need not have stopped, but9(hy+hz) is nonnegative and is discarded in the lower bound. The same monotone kernel G and same binomial first-hit law therefore apply. This proves the extension for the original physical event without changing the original object or its signatures.

If a selected label has signature sigma containing x, it is outside E and hence above u in the lift. It is also above a,b. Its outside-C incomparable neighbors are exactly the3-|sigma| missing T roots. Thus actual Delta10 gives

    deg_C(c)<=10-(3-|sigma(c)|).

Individual degree caps may be retained in the deadlines; a common d equal to their maximum is a valid weaker uniform certificate. This does not assign inherited degrees to a deleted or synthetically chained object.

## Three uniform sufficient gates

Monotonicity in m,k makes(7,7) the hardest positive-moment-free cell. Direct rational evaluation of the closed binomial identity gives

    B(1,6;7,7)=2,
    B(2,9;7,7)=298/45,
    B(3,10;7,7)=3622/165.

Consequently any of the following actual conditions guarantees1/3<Pr(u<b)<=5/9 over all m<=k<=7:

1. One x-containing C-minimum of C-degree at most6.
2. Two x-containing C-minima, both of C-degree at most9.
3. Three x-containing C-minima (their actual C-degrees are automatically at most10).

In particular, two nonfull x-containing C-minima each miss at least one T root and automatically satisfy gate2. The constants are per-C-word lower margins, not sharp probability estimates. Their evaluation is finite arithmetic of an analytic identity, not object enumeration or a computer-assisted proof table.

## Scope and provenance

The extension uses corrected MF1 source SHA256 `ee284d443736573468786cc11060d9eff3447938f9930ad6136d158e6fac5a48` and its audit SHA256 `9c1d095656a5e949888faa934471cfcd90920fffbe94c44f272417f14942b968`. MF1's proof of stochastic domination and exact event-kernel source are explicit dependencies.

These are sufficient fixed-pair gates. They do not pay the entire residual with one high-C-degree x-containing minimum, nor do they classify cases with fewer such minima. There is no claim of new ordinary balanced-pair population, no NB conclusion, and no full B1 theorem. No original-poset enumeration, LE DP, moment transfer, or new realizability claim is used.
