# WB5 independent mathematical review

2026-11-10 UTC. **PASS, exact stated scope.** This reviewer did not participate in deriving WB5. This is a non-blind internal independent mathematical review, not external peer review, formal verification, or originality certification.

Reviewed source: Section 6 of `ZERO_FRONTIER_M6_WEIGHTED_ROOT_BANK.md`, current complete-source SHA256 `45e091fa365060ae800e1e48f5f9c15917b7296da5bc8d1bf38a9f1c7dac3071`.

The first 118 lines still have SHA256 `ad2fd6a623406f29e7c75b1bb1c296ddf749b73a322eb091e8bc3fd6608bb67e`, exactly the previous WB6 source. The separate WB6 review therefore remains applicable without modification.

## Result

Under the stated actual Delta10, zero-x-frontier, m5k6, empty C-minimum f residual contract, the claimed original-count inequality is correct:

    4K_u+K_y+K_z-2N >= 16e(C)>0.

Thus the fixed physical bank (u,b),(y,b),(z,b), with weights (4,1,1)/6, has mean strictly greater than 1/3. The accepted candidate-wise upper bounds give one strictly balanced original physical pair. Combined with the preceding accepted frontier/no-empty reductions, this closes the formerly remaining m5k6 ordinary-payment cell. It does not assert universal fixed-(u,b) payment, full D10/B1, or an unguarded/NB realization.

## Independent verification

1. **Structure.** Cardinality gives Mx=E union {f}, so C-f has exactly E as its missing-x labels. The actual f-degree cap gives at most seven C labels incomparable with f. Consequently every true gamma deletion fiber has legal slots 0..d, with h=q(gamma)=h_x(gamma)<=5 and h<=d<=7. The author's argument that every exception in Z0 has an E ancestor follows from the genuine ideal E union Z0 and zero x-frontier.

   There is also a shorter independent check of the only needed h0 consequence. If the first gamma label c contains x, it is C-f-minimal. Unless f<c, it is then C-minimal in C as well, contradicting zero x-frontier. Thus it is an f-successor and d=0. Here gamma is never empty because m=5, so no empty-word boundary is omitted.

2. **h0 kernel.** The original beta has H=1 and 1<=Y,Z<=6 by the two original root degree caps. The exact A0=A1 positive-gap identity, independently verified in the WB6 review, gives

       F+G=82+5(Y+Z)-2YZ-2min(Y,Z).

   Since YZ<=6Y and YZ<=6Z, we obtain YZ<=3(Y+Z). Therefore the displayed expression is at least 82-(Y+Z)-2min(Y,Z)>=58. Its fiber has one word. No OC2 side-shape restriction is used.

3. **h>=1 kernels and analytic sum.** The first-slot value is 88+6h. The values on mandatory later slots 1..h are

       76+(12-10j)(h+1)+5j(j-1),

   and each extra legal slot has value 76+7h-5h^2. Summing independently gives

       B5(h)=88+(262h+6h^2-10h^3)/3.

   For 1<=h<=4 the extra coefficient is concave with endpoint values 78,24, hence positive. B5''=4-20h<0, and its endpoint values 174,256 give B5>=174. At h=5 its value is 158, each extra slot contributes -14, and d<=7 permits at most two such slots. Thus every h>=1 fiber has total at least 130. A small symbolic expansion checked the written sum and endpoint values only; the analytic proof does not depend on software or a finite positivity table.

4. **True-law assembly.** A fiber has at most eight C words, so its total is at least 16 times its actual size (130>=128); the h0 fiber also satisfies that bound. The fibers partition LE(C), with every actual retained gamma and completion counted at its genuine multiplicity. Summing gives the claimed 16e(C) margin.

5. **One physical bank throughout.** From the independently verified original kernels,

       sum(F+G)=(3K_u-N)+(K_u+K_y+K_z-N)
               =4K_u+K_y+K_z-2N.

   The coefficient sum is six, hence this is exactly the lower 1/3 inequality for the stated bank. No pair is changed between gamma fibers, no conditional moment is imposed, and no old-prefix credit is used twice. The upper bounds remain individual rather than only averaged.

## Consequences and limits

The proof does not require OC2, OC3, OC4, or ND1's computer-assisted core counts. It is pure analytic original-weight payment. It also correctly warns against transferring the argument to k-m>=2: a nonminimal empty label above f can invalidate H=1 and the one-run-equals-one gap identity.

Combining this result with the separately reviewed WB6 leaves exactly the following necessary zero-frontier+empty parameter cells open in the current entry:

    m3k7; m4k6; m4k7; m5k7.

No assertion of simultaneous realizability or of a point escaping all historical guards is made. No external repository/document or CURRENT_ADVANCE entry was changed by this reviewer.
