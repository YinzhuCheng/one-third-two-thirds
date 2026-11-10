CURRENT UPDATE: the explicit integer discriminant inequalities below, Q8_EQUAL_MAX_FACE_ANALYTIC.md and Q8_MIDDLE_TIE_BOUNDARY.md have all passed review and are assembled in Q8_COMPLETE_ANALYTIC_PROOF.md. This removes the old81/1512 coefficient-check dependencies for the original integer cap problem. Older status sentences below describe the stages when those boundaries were still open; this file is not an additional paid-row count.

# Further Q8 source-tail reduction: maximum-cap endpoints and two discriminants

2026-11-10. Research reduction, not a new pure analytic payment. Preserve the 400 pure + 2 finite-symbolic classification and the true-law contract of Q8_SOURCE_BERNSTEIN_CERTIFICATE.md.

Let M_i(t,p,q,r) denote that document's twelve source-margin chamber polynomials, ordered as in its JSON. Each is affine in r. This is structural: the largest deadline occurs on the last-cap label only, and after the other gap choices are fixed that label has an interval of possible gaps. Consequently it suffices to prove the two faces r=0 and r=6-t-p-q.

This note handles reductions on the SECOND face, with t,p,q>=0 and t+p+q<=6. Write its polynomial as A_i q²+B_i q+C_i. The accompanying JSON records these exact coefficients for all chambers.

## Nine concave or linear cases

Indices 1,5,7 have A<0; indices 2,3,9,10 have A=0. Indices 8 and 11 also have A<0 on the domain:

    2A8=p(12t²-23t-29)+5t³-44t²-173t-130,
    2A11=p(3t²-80t-95)+5t³-44t²-173t-130.

For A11 both displayed parts are negative on 0<=t<=6. For A8 maximize its affine p expression at p=0 or p=6-t. The former is negative because 5t-44<0. The latter is -7t³+51t²-282t-304, strictly decreasing: its derivative -21t²+102t-282 has negative discriminant and negative leading coefficient. Hence both endpoint values are negative.

These nine cases reduce to q=0 or q=6-t-p. The right endpoint belongs to r=0. The left endpoint is a DIFFERENT boundary with the middle two caps equal; it still needs a proof, and must not be silently identified with r=0.

## Convex case 4 is increasing

Case 4=(t1,z,t2,t3) has A>0 and B>0. In fact

    8B=54p²t²+342p²t+396p²
       +p[t(92t²-570t+1634)+1444]
       +t²(23t²-162t+357)+1590t+88.

Both quadratics in parentheses have negative discriminant and positive leading coefficient. Thus this case reduces to q=0 on the whole domain.

## The two remaining convex cases

Only indices 0=(t1,t2,t3,z) and 6=(t2,t1,t3,z) remain. Their common quadratic coefficient is

    A=3[3pt²+19pt+22p+2t³+22t²+64t+56]/4>0.

On 4<=t<=6 they are decreasing throughout the permitted q interval. To verify this, put t=4+x, 0<=x<=2, and let R_i=8 times the q derivative at q=6-t-p. Then

    R0=(88x³-62x²-5230x-14836)p
                         +37x⁴-10x³-3561x²-14490x-8856.

Its two terms are negative, using x³<=4x and x⁴<=4x². For case 6,

    R6=(30x²+34x-592)p²
          +(60x³-160x²-1680x+3268)p+C(x),
    C(x)=37x⁴-10x³-3561x²-14490x-8856<0.

The quadratic p coefficient is negative. After dropping it, the affine p expression has endpoint values C(x) and

    C(x)+(2-x)(60x³-160x²-1680x+3268)
              =-23x⁴+270x³-2201x²-21118x-2320<0,

using x³<=2x². Hence both cases reduce to the right endpoint q=6-t-p when t>=4.

## Residual on 0<=t<=4

It suffices to prove H_i=4A_i C_i-B_i²>0 for i=0,6. This would make the quadratics positive on the entire real q-axis. Exact H polynomials are in the attached JSON; their degrees in p are 3 and 4.

A smaller FINITE SYMBOLIC proof is now available. Expand H_i in degree-3 or degree-4 Bernstein basis in y=p/(6-t). Its four or five coefficient functions are polynomials of degree eight in t. Expand each in Bernstein basis in t/4. All 81 rational coefficients are positive, with minimum 74816. Thus H_i>=74816 on this rectangle-with-rescaled-p domain. The generator independently re-expands both Bernstein levels to verify their polynomial identities.

This reduces the internal saturated-face dependence from twelve chamber quintics to two discriminants with 81 positive coefficients, plus the explicit analytic sign arguments above. It does NOT eliminate the finite symbolic dependence. It also does NOT independently prove either the r=0 face or the seven distinct q=0 saturated-face boundary polynomials. Therefore it must not be counted as a new full gate or a pure analytic replacement.

## Update: eliminating the 81-coefficient dependency using actual integer t

The original caps are integers. Thus in the residual range 0<=t<=4 only t=0,1,2,3,4 occur. The following elementary inequalities replace the Bernstein positivity dependency entirely. This is a bounded integer-case analytic argument, not interpolation or a list of profile-bank verifications. The variable p may remain real throughout each stated interval 0<=p<=6-t. The earlier continuous certificate remains as a stronger optional check, not a dependency.

For case 0 the five exact discriminant polynomials are:

    H0(0,p)=20196p³+(41943/4)p²+5424p+74816,
    H0(1,p)=75240p³+43604p²+522828p+1385343,
    H0(2,p)=186624p³-135756p²+855036p+5404887,
    H0(3,p)=372060p³-(2541201/4)p²-1053129p+12007775,
    H0(4,p)=643860p³-(4873609/4)p²-7607763p+17207559.

The first two are positive termwise. At t=2, p<=4 gives

    H0(2,p)>=186624p³+312012p+5404887>0.

At t=3, p<=3 and discarding the positive cubic gives

    H0(3,p)>=12007775-(2541201/4)*9-1053129*3
             =12522743/4>0.

At t=4, the derivative in p is the convex quadratic

    1931580p²-(4873609/2)p-7607763.

Its endpoint values on [0,2] are -7607763 and -4755052. A convex function is bounded above by its endpoint chord, so this derivative is negative throughout the interval. Therefore

    H0(4,p)>=H0(4,2)=2269304>0.

For case 6 the five exact polynomials are:

    H6(0,p)=-598p⁴+9162p³-(101233/4)p²+339240p+74816,
    H6(1,p)=-1357p⁴+7100p³+33986p²+1615572p+1385343,
    H6(2,p)=-(2673/4)p⁴-(66825/2)p³+(435699/4)p²
                                                  +4551309p+5404887,
    H6(3,p)=(11507/4)p⁴-110055p³-78547p²+8630556p+12007775,
    H6(4,p)=10511p⁴-198619p³-(3125233/4)p²+12033927p+17207559.

For t=0, p<=6 yields

    H6(0,p)>=5574p³+(374781/2)p+74816>0.

For t=1, p<=5 yields

    H6(1,p)>=315p³+33986p²+1615572p+1385343>0.

For t=2, use p⁴<=64p and p³<=16p, discarding the positive p² term:

    H6(2,p)>=3973941p+5404887>0.

For t=3, discard the positive quartic and use p³<=9p, p²<=3p:

    H6(3,p)>=7404420p+12007775>0.

For t=4, discard the positive quartic and use p³<=4p, p²<=2p:

    H6(4,p)>=(19353669/2)p+17207559>0.

These expressions were independently checked against the exact original chamber polynomials. Together with the t>=4 derivative argument, they remove all INTERNAL saturated-face finite-symbolic positivity dependencies for the actual integer cap domain. The q=0 and r=0 boundary obligations remain separate. Hence no full-gate closure or coverage increment follows from this update alone.
