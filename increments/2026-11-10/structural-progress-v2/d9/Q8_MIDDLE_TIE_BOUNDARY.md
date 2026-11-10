# Q8 saturated q=0 boundary: explicit cubic inequalities

2026-11-10. Author analytic reduction; independent audit PASS in Q8_ANALYTIC_BOUNDARIES_INDEPENDENT_REVIEW.md. This concerns the source 15/3/2/2/1 bank, on the original integer cap domain, not a new bank or a coverage increment by itself.

The sorted caps are (t,t+p,t+p,6), with integer t in {0,...,6} and 0<=p<=6-t. We allow p real, so the argument does not enumerate its profiles. Of the twelve chambers, only seven distinct polynomials C_i(t,p) remain; representative indices are 0,1,3,6,7,9,10. Their duplicates are (0,2),(1,4),(3,5),(6,8),(9,11). These are the chamber indices in Q8_SOURCE_BERNSTEIN_CERTIFICATE.json.

Write C_i=a_i p³+b_i p²+c_i p+d_i. Define

    G0=36t³-595t²+2229t+1240,
    G1=39t³-995t²+5066t+880,
    G3=9t³-1165t²+6486t+4960,
    D0=(t+2)(t+3)G0/10,
    D1=(t+2)(t+3)G1/40,
    D3=(t+2)(t+3)G3/40,
    J=3t²+19t+22.

The exact coefficients derived from the source polynomial are:

| i | a_i | b_i | c_i | d_i |
|---|---|---|---|---|
|0|3J/4|(56t³−391t²+357t+330)/4|13t⁴−109t³−109t²+732t+224|D0|
|1|3J/4|(34t³−435t²+319t+254)/4|(39t⁴−650t³+345t²+7746t+3520)/8|D1|
|3|−3J/2|−(5t³+603t²−592t−908)/4|(9t⁴−924t³+621t²+12238t+9112)/8|D3|
|6|9(3t²−3t−4)/4|(64t³−417t²+385t+728)/4|(101t⁴−998t³−645t²+9198t+6680)/8|D0|
|7|−J/2|−(t³+219t²−740t−952)/4|(8t⁴−273t³+291t²+3786t+2692)/4|D1|
|9|(6t²−61t−73)/2|(20t³−249t²+344t+643)/2|(83t⁴−1042t³+825t²+15798t+13536)/8|D0|
|10|J/2|(7t³−66t²+385t+428)/2|(4t⁴−129t³+183t²+1870t+1254)/2|D3|

## Endpoint obligations

The right endpoint p=6-t has caps (t,6,6,6), hence is already part of the r=0 face. The conclusion below assumes that face's positive-payment lemma; this note must not be used circularly to establish it.

The left endpoint p=0 is positive independently. G1 and G3 are concave on [0,6] and have positive endpoint values (880,3880) and (4960,3880). For G0, its derivative is a convex quadratic, G0'(0)=2229>0 and G0'(6)=−1023<0. Thus G0 can only increase then decrease on this interval, not have an interior minimum; its endpoint values are 1240 and 970. Therefore D0,D1,D3>0 throughout [0,6]. At t=6, necessarily p=0, and all three D values equal 6984.

## A common cubic endpoint mechanism

If a<0 and c=C'(0)>0, then C' is a concave quadratic starting positive. On the nonnegative p-axis it crosses zero at most once, from positive to negative. Thus C increases and then decreases, and its minimum on any [0,L] is at an endpoint. This elementary lemma handles:

- i=3, t=0,...,4;
- i=6, t=0,1;
- i=7, t=0,...,4;
- i=9, t=0,...,5.

The required signs follow directly from the displayed coefficient formulas. For i=3 and i=7 at t=5, all nonconstant coefficients are negative, so C decreases and its minimum is the right endpoint. This also needs no interior calculation.

## Positive coefficients and eleven coarse inequalities

For i=0,1 at t=0,1, and i=6 at t=2, all nonconstant coefficients are nonnegative. For i=10 at t=0,...,5 they are positive. These cases are bounded below by the positive left endpoint.

Only eleven explicit integer-t slices remain. They are handled by dropping positive terms and replacing each negative term e p^j by e L^j, where L=6-t. The resulting exact positive constants are:

    i=0, t=2: 7212−18·4²=6924;
    i=0, t=3: 10632−(303/2)·3²−451·3=15831/2;
    i=0, t=4: 12348−(457/2)·2²−2240·2=6954;
    i=0, t=5: 11256−165−4341=6750;

    i=1, t=2: 3672−144·4²=1368;
    i=1, t=3: 6132−(893/2)·3²=4227/2;
    i=1, t=4: 8106−(1627/2)·2²=4852;
    i=1, t=5: 8694−1194−750=6750;

    i=6, t=3: 10632−(71/2)·3²=20625/2;
    i=6, t=4: 12348−77·2²−608·2=10824;
    i=6, t=5: 11256−3135=8121.

These eleven displayed inequalities exhaust all integer t cases not already covered by endpoint shape or coefficient positivity. No p profile is sampled, and no Bernstein coefficient table is used.

Consequently the entire saturated q=0 boundary follows analytically from the r=0 face lemma and the explicit elementary inequalities above. It does not require the original 1512-coefficient certificate. The original-P model, exterior-word weights and fine-fibre −88 stopping line remain unchanged.
