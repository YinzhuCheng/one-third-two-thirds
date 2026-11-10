# WB6 independent mathematical review

2026-11-10 UTC. **PASS, with the exact scope below.** This reviewer did not participate in deriving WB6. This is a non-blind internal independent mathematical review, not external peer review, formal verification, or an originality certificate.

Reviewed source: `ZERO_FRONTIER_M6_WEIGHTED_ROOT_BANK.md`, SHA256 `ad2fd6a623406f29e7c75b1bb1c296ddf749b73a322eb091e8bc3fd6608bb67e`.

## Conclusion first

The claimed original-count inequality is correct under the displayed OC1/OC2 residual contract:

    9K_u+3K_y+3K_z-5N >= 2e(C)>0.

It yields a single fixed physical bank with weights (3,1,1) on (u,b),(y,b),(z,b), not a different pair chosen in each conditional fiber. The accepted candidate-wise upper bounds then give an ordinary strictly balanced pair. Together with the already accepted guards and OC1/OC2 reductions, this closes the entire formerly remaining m6k7 zero-frontier cell. All nonzero-frontier cases and zero/no-empty cases were previously paid, so m6k7 no longer belongs in the open ordinary residual.

This does not prove fixed-(u,b) balance in every instance, close any of the other five zero+empty cells, solve full B1/D10, or produce NB/prime/all-history-unguarded objects. It is a pure analytic payment proof; no finite computational certificate is a dependency.

## 1. Structural premise and the needed asymmetric cap

I checked the source against OC1 and OC2, rather than assuming a deleted object's degree bound. In the guard-excluded m6k7 empty-minimum branch, the original missing-x set is exactly E union {f}; the unique exception g has nonempty predecessor ideal inside E; every other C label contains x and is above f. OC2 reduces the original y/z asymmetric sides to one nonchain A and an empty B (or its symmetric counterpart).

Every non-E, non-f, non-g point is x-only, xy, xz, or full. B empty removes xz. Consequently C labels missing y are exactly f plus the x-only labels L0, whereas those missing z are exactly f plus L0 plus A. The original z has four additional incomparable labels b,x,y,u. Hence |L0|+|A|<=5; A nonchain gives |A|>=2 and |L0|<=3. This proves the full-original bounds h_y<=4 and h_z<=6. There is no autonomous-side assumption or induced-VG lifting here.

## 2. Independent recovery of the bank identity

From the accepted root-slot table, independently subtracting N from S gives

    S-N=(14/3)A3+3A2-(7/2)I-L-2A1-2A0.

For one genuine C word, A3 contributes 6, A2 contributes 2(H+Y+Z), I contributes 2(Y+Z), and L contributes 2QH-Q(Q-1). Thus the displayed G kernel is exactly

    28+(6-2Q)H-(Y+Z)+Q(Q-1)-2A1_beta-2A0_beta.

The displayed F kernel is the accepted same-word fixed-u/b margin with the full 2x_beta+y_beta prefix credit. Therefore

    sum(2F+3G)=2(3K_u-N)+3(K_u+K_y+K_z-N)
             =9K_u+3K_y+3K_z-5N.

This confirms the coefficients and avoids double consumption of prefix credit.

## 3. Exact positive-gap multiplicity

When one missing-root run is 1, place that root in positive gap 1 to count K0 words. For the other roots choose gaps i in [1,r] and j in [1,s]. A baseline one ordering per pair requires the following corrections:

- at (1,1), all three roots coincide, giving 6 rather than 1, hence +5;
- when precisely one other gap is 1, two roots coincide, hence +(r-1)+(s-1);
- on the diagonal beyond 1, the remaining two roots coincide, hence +(min(r,s)-1).

The resulting count is rs+r+s+min(r,s)+2. The sum of the three accepted K1 pair-gap counts gives the same expression. Thus A0_beta=A1_beta exactly in the uses made by WB6. The equality has not been assumed for arbitrary root-run triples.

## 4. All actual f fibers are covered

For each gamma in LE(C-f), f is still an actual C-minimum, so its legal gaps are a full initial interval 0..d. The labels before its first successor are all original f-incomparables, namely E union {g}, so d<=7. The only missing-x labels in C-f are E, giving q(gamma)=h_x(gamma)=h<=6, and the initial h labels are f-incomparables, giving d>=h.

If h=0, the first gamma label cannot be g, since g has an E predecessor. It must be above f; therefore d=0. The only beta has H=1, 1<=Y<=4, 1<=Z<=6. Substitution into the exact kernels gives

    2F+3G=190+5(Y+Z)-8YZ-8min(Y,Z).

Both one-sided slopes in each variable are strictly negative for the displayed range. The minimum is 16 at (4,6).

If h>=1, inserting f first gives runs (h+1,1,1); inserting it later leaves an initial yz-signature E label, forcing the K0/K1 counts to vanish. For gaps 1..h the runs are (H,Q)=(h+1,j); for all later gaps they are (h,h). This remains correct if some E labels lie after the full exception g. No bound d<=h+1 is used.

Independent summation of these kernels gives

    B(h)=184+(616h+24h^2-22h^3)/3,
    extra(h)=180+19h-11h^2.

For 1<=h<=5, extra(h)>=0 by concavity and endpoint values 188,0. Also B(h)>184 since 308+12h-11h^2 is concave with endpoint values 309,93. For h=6, B=120, extra=-102, and d-h<=1, leaving at least 18. These elementary inequalities cover all required integer values without a positivity table.

A small SymPy expansion independently checked the displayed sum and the two h=6 numbers; it was diagnostic confirmation of the written analytic identities, not a proof dependency. No original-poset enumeration was run.

## 5. Original weights, full scope, and ledger impact

The h=0 fiber contains one word with margin at least 16. Every h>=1 fiber has d+1<=8 words and total margin at least 18, hence at least twice its actual size. The fibers partition LE(C) without normalization or deduplication. Summing proves the claimed 2e(C) margin while preserving all gamma/tail multiplicities.

The normalized physical bank is (3K_u+K_y+K_z)/(5N)>1/3. Since each member separately has probability at most 5/9 (and y/b,z/b at most 1/2), some one original pair is strictly balanced. No averaging argument is being used to supply an individual upper bound.

The proof depends on OC1/OC2 and earlier original root-count identities, but not OC3/OC4, the later consecutive-N exit deductions, or ND1's finite-core computer-assisted counts. Those remain valid structural/control results but are superseded as open ordinary-payment residuals. The updated necessary zero+empty parameter list should therefore be

    m3k7; m4k6/7; m5k6/7.


