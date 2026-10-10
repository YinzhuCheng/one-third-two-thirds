# C13 requires at least four nonsingleton chains

Scope: the frozen eight-point prime core C13, with original labels and strict relation masks copied in certificate.json. A chain inflation means nonempty chains of positive integer lengths, with every relation between distinct chains inherited from C13. Probabilities are uniform over actual labelled linear extensions.

Theorem. Any C13 chain inflation having no balanced pair has at least four nonsingleton chains, hence has order at least 12. This is an all-positive-integer-weight necessary bound, not a claim that four nonsingletons suffice, not an exclusion of all C13 inflations, and not a theorem about other classes.

Proof. The independently audited port constraints require blocks 0 and 3 to be nonsingleton. The independently audited strict linear constraints additionally require the nonsingleton support to intersect each of {1,2,4,6} and {4,5,6,7}. With at most three nonsingletons, the support is therefore exactly {0,3,4} or {0,3,6}: the only possible third block belongs to the intersection {4,6}.

For either support write a=w0, b=w3, and c=w4 or w6, respectively. All other weights equal one. Three of the audited strict inequalities become

    2a - c <= 2,
    2b - c <= 2,
    2c - a - b <= 1.

The integer constants include the strictness correction; a,b,c >= 2. Let A be their coefficient matrix. Its inverse is

    A^(-1) = (1/4) [[3,1,2],[1,3,2],[2,2,4]].

All entries are nonnegative, so Ax <= (2,2,1) implies x <= (5/2,5/2,3), hence x <= (2,2,3) for integer weights. The first two coordinates are consequently 2. The third inequality then gives 2c <= 5, so c=2. No weight cutoff was presumed.

For support {0,3,4}, the sole remaining weight vector is (2,1,1,2,2,1,1,1). It has 2,060 labelled linear extensions; exactly 698 place B0 before B1. Thus 2,060 <= 3*698=2,094 <= 4,120.

For support {0,3,6}, the sole remaining vector is (2,1,1,2,1,1,2,1). It also has 2,060 labelled linear extensions; exactly 742 place B0 before B1. Thus 2,060 <= 3*742=2,226 <= 4,120.

The two blocks are incomparable. These are actual balanced pairs in both possibilities, a contradiction. QED.

## Verification and dependencies

The new scalar labelled-element predecessor-mask DP in verify.py imports no occupancy implementation. It recounts denominator and both pair orientations, checks they sum, verifies the inverse certificate in integers, and independently enumerates every support of size at most three satisfying the audited clauses. Run `python verify.py`.

The original occupancy forward/backward count is in the parent search.py ledger and gives the same two totals and numerators. The support and inequality facts are the previously independently audited results in /workspace/shared/eight-core-weight-independent-audit-frozen/AUDIT.md, themselves based on the frozen catalogue and Zaguia's structural good-pair theorem. This package is a narrow derived theorem, not a rerun of the original core classification or a reproof of that external theorem.
