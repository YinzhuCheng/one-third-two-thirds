# Q8 equal-maximum face: explicit analytic integer-gap proof

2026-11-10. Author proof; independent concrete algebra review PASS in Q8_ANALYTIC_BOUNDARIES_INDEPENDENT_REVIEW.md. This note concerns only the face r=0 of the source-bank reduced tail polynomials. It does not by itself close the full Q8 gate or upgrade the400 pure-analytic ledger.

## EM1. Polynomial definition and exact coverage

Use the original-P root compression and fixed source bank of Q8_SOURCE_BERNSTEIN_CERTIFICATE.md, but NOT its Bernstein signs. Let P_sigma(t,p,q,r) be its exact reduced count polynomial for sorted tail caps

    t, t+p, t+p+q, t+p+q+r,

assigned to physical tail labels(0,1,2,3)=(t1,t2,t3,z) in order sigma, with0 preceding3. Explicitly it is

    11F-24G+15W+9W_G + sum_(j=1..t)(9W_j-42F_j),

where F,W count the12 internal tail words satisfying0<3 with score2[1<0]+2[2<1]+[3<2], and G,W_G insert the independent cap-zero v. The flagged-chain recurrence/determinant in the source note defines these rational polynomials without using any positivity certificate. Only algebraic identities below are needed; they can be checked by expansion from that definition.

At r=0, swapping the last two equal-cap labels does not change the polynomial. The12 chambers reduce to seven representatives:

    i=0:0123, 2:0213, 4:0312, 6:1023,
      8:1203, 9:2013, 11:2103.

Write R_i(t,p,q)=P_sigma(t,p,q,0). The target is

    R_i>0 for integer t,p,q>=0, t+p+q<=6.             (EM)

The integer restriction is essential to the q-reduction below. No continuous-domain claim is made for that step.

Each R_i is quadratic in q. Its q=0 constant is C_0 for i0/2/4, C_6 for i6/8, and C_9 for i9/11. Its other endpoint is E_i(t,p)=R_i(t,p,6-t-p). Sections EM3 and EM4 prove these endpoints positive. Section EM2 verifies that the q minimum occurs at one of them for the integer domain. This is a directed reduction, not a circular appeal to the saturated-face proof.

## EM2. The q-axis is an endpoint problem

Write R_i=A_i q²+B_i q+C_i. A quadratic with A<=0 has its minimum at an endpoint; with A>=0,B>=0 it is increasing on q>=0. The following checks cover every integer t,p in the domain.

### i0

    4A_0=-p(75t²+79t+82)-(38t³+22t²-116t-16).

For t>=2 the second bracket is positive and increasing, so A_0<0. For t0 it is A=4-41p/2; for t1 it is A=18-59p. Thus p>=1 again gives A<0; p0 has B=106 or579, respectively, and A>0. This is the only step using p's integrality.

### i2,4,9

For t>=5,

    A_2=A_9=p(-12t²+23t+29)+(-8t³+11t²+77t+46)<0,
    A_4=p(-12t²+23t+29)+(-8t³+11t²+77t+46)/2<0.

Both brackets are negative at5 and strictly decreasing afterward. For0<=t<=4, B_2 and B_4 are positive. Here -8B_2 and -4B_4 are respectively

    [210t²-254t-332]p²
      +[236t³+130t²-2210t-1516]p
      +69t⁴+26t³-1861t²-4274t-2000,

    [105t²-127t-166]p²
      +[96t³+21t²-1143t-834]p
      +24t⁴+20t³-526t²-1190t-500.

For t<=2 both leading coefficients are nonpositive and both p coefficients are negative, so their maxima over p>=0 are at p0. For t>=2 the leading coefficients are nonnegative, so their maxima on0<=p<=6-t are at endpoints. The constant terms are negative for t<=4 by t⁴<=16t²,t³<=4t². At p=6-t, put u=4-t in[0,4]. The two values -B are

    43u⁴/8+387u³/4-2011u²/8-5447u/4-980
       <=-1901u/4-980<0,
    33u⁴/4+71u³-695u²/4-3363u/2-20
       <=-1425u/2-20<0,

using u⁴<=16u²,u³<=4u²,u²<=4u. Finally

    B_9-B_2=[(102t²+250t+280)p²
                  +(68t³+454t²+1094t+1104)p]/8>=0.

Thus B_9>0 too. Integer t is either<=4 or>=5, so this covers the three representatives.

### i6

For t<=2, -8B_6 has coefficients

    [126t²-390t-480]p²
      +[192t³-60t²-2536t-1948]p
      +75t⁴+138t³-1207t²-2790t-848,

all negative by t<=2. For t>=3, 4A_6 is the negative of

    D(t)+K(t)p,
    D=38t³+22t²-116t-16, K=39t²-149t-182.

D>0 on[3,6]. If K<0, its minimum on p<=6-t is

    D+K(6-t)=-t³+405t²-828t-1108.

This is26 at3 and has positive derivative on[3,6]. Hence A_6<0. Integer t leaves no gap between these two ranges.

### i8,11

For t<=5 the coefficients of -2B_8 as a polynomial in p are

    a=24t²-46t-58,
    b=32t³-8t²-377t-271,
    c=12t⁴+7t³-296t²-691t-334.

If a<0 then t<3 and b<0, so the maximum is at p0. Otherwise convexity puts it at p0 or6-t. One has c<=-496t-334<0. At p=6-t put u=5-t in[0,5]; then

    -B_8=(4u⁴+47u³+86u²-2743u-858)/2
           <=(-638u-858)/2<0.

For i11 the p² and p coefficients of -2B_11 are15t²-103t-124 and26t³-92t²-683t-571, both negative on[0,5]; its constant is the same c. Thus B_11>0. At integer t6, p=q=0 and there is no q interval.

These checks prove the endpoint reduction for all seven representatives.

## EM3. The q=0 endpoints: three cubic families

Set

    Z(t)=-(t+2)(t+3)(t+4)(24t²-151t-55)/10.

Z>0 on0<=t<=6, since the convex quadratic in parentheses has negative values at both endpoints. The three cubics are defined by

    20(C_0-Z)=p(-240t⁴-470t³+4690t²+13600t+6040)
       +p²(-430t³-635t²+3415t+2210)
       +p³(-285t²+175t+250),

    40(C_6-Z)=p(-375t⁴-790t³+6495t²+18710t+8440)
       +p²(-480t³+30t²+6570t+5160)
       +p³(-210t²+650t+800),

    40(C_9-Z)=p(-345t⁴-230t³+9825t²+26510t+14640)
       +p²(-420t³+780t²+9060t+7500)
       +p³(-180t²+840t+1020).

For C_0 the minimum in p is at0 or6-t. Here is a coefficient-sign proof rather than an enumeration of p values. For0<=t<=2 the p and p² coefficients are positive (bound them below by1120t²+13600t+6040 and425t+2210); the p³ coefficient may have either sign, so the derivative either stays positive or has exactly one positive zero, a maximum. For2<=t<=3 the p³ coefficient is negative and p coefficient positive, again giving one maximum at most. For3<=t<=6 both p² and p³ coefficients are negative, so the derivative is decreasing on p>=0. Thus no interior p minimum occurs.

The nonzero endpoint L(t)=C_0(t,6-t) is positive. Put u=6-t. Its explicit form is

    L=6984-1437u/5-43u²/2
          +u³(979/4-47u/2-47u²/20).

The bracket is>=383/20 on0<=u<=6, and the remaining first three terms are>=22428/5>0.

For C_6 and0<=t<=4 all three p coefficients are positive: their numerators are bounded below by40, 5160-990t, and8050t+8440. At integer t5,

    C_6=10584-1719p-531p²-30p³>=8304

since0<=p<=1. At t6, p0 and C_6=Z(6)>0. For C_9 and0<=t<=5 all three p coefficients are positive: the numerators are bounded below by720,2460t+7500, and50t²+26510t+14640. At t6 again p0. Thus all q=0 endpoints are positive.

## EM4. The q=6-t-p endpoints

Write E_i=R_i(t,p,6-t-p), with0<=p<=L0=6-t. Define J_i(t)=E_i(t,0) for i0,2,4,8. The following univariate bounds are useful:

1. With u=6-t,

       J_0=6984-3647u/5+u² R(u),
       R=3801/4-1445u/8-51u²/4+101u³/40.

   R'<=399u/20-1445/8<0 for0<=u<=6, so R>=R(6)=-471/10 and J_0>=912>0.

2. J_2=-(t+2)N_2/40, where

       N_2=71t⁴-2222t³+25089t²-80738t-65760.

   N_2'' is decreasing and at least858 on[0,6]. Thus N_2 is convex and bounded above by its negative endpoint maximum; J_2>0.

3. J_4=-(t+2)N_4/5, where

       N_4=2t⁴-84t³+1438t²-6051t-4275.

   N_4''=24t²-504t+2876 has negative discriminant and positive leading coefficient. N_4 is convex, with both endpoints negative, so J_4>0.

4. With u=6-t,

       J_8=6984+u B(u),
       B=32763/5-505u-701u²/2+46u³-11u⁴/10.

   B'<0: for u<=4, bound138u²<=552u; for4<=u<=6 use138u²<=828u and u³>=16u in B'=-(22/5)u³+138u²-701u-505. Thus B>=B(6)=-585 and J_8>=3474>0.

For i2,4 the p quadratic coefficients are respectively

    3(t-8)(3t²+19t+22)/4,
    3(t³-27t²-194t-232)/4,

strictly negative on[0,6]. Both p endpoints are J_2 or J_4 and the positive L(t) of EM3. Therefore E_2,E_4>0.

For i6 write A=3t²+19t+22. Its p³ and p² coefficients are A/4 and-(5t³-144t²+989t+1186)/4. The vertex of its quadratic p derivative lies at or beyond L0: the relevant numerator is

    14t³-141t²+713t+790>0,

whose derivative has negative discriminant and positive leading coefficient. Therefore E_6' decreases on[0,L0]. Its right-end value is

    (7t³-72t²+347t+384)/2>0,

again because its derivative quadratic has negative discriminant. Hence E_6 is increasing and E_6>=J_0>0.

For i9 its p derivative is concave. At p0 it equals

    -7t⁴+116t³-814t²+1927t+2573>0,

a concave function of t with positive endpoint values. At p=L0 it equals

    -t³-36t²+321t+401>0,

also concave with positive endpoints. Thus E_9 is increasing and E_9>=J_2>0.

For i11 the vertex of its quadratic p derivative is exactly7-t=L0+1. Its derivative is decreasing on the interval. The right-end derivative equals1258+tH(t)/8, with

    H=-5t³+322t²-3163t+9094
        >=292t²-3163t+9094>0.

The last quadratic has negative discriminant. Hence E_11 is increasing and E_11>=J_8>0.

For i8 its p³ and p² coefficients are positive. If its p coefficient b8 is nonnegative, E_8>=J_8>0. If b8<0, discard the positive high terms and use p<=L0 to get E_8>=J_8+b8L0. With u=6-t this last polynomial is

    6984-182u/5+u²Q(u),
    Q=615/4+1299u/8-137u²/4+21u³/40.

Q is concave on[0,6] and both endpoint values are positive (615/4 and42/5). Thus this lower bound is positive too.

Finally E_0=a p²+b p+J_0, where

    a=-3(t³-8t²-81t-102)>0,
    b=-(63t⁴-1358t³+5777t²-706t+4408)/8.

Its negative discriminant D=4aJ_0-b² is positive by the single explicit identity

    33592320 D = sum_(j=0..8) c_j t^j(6-t)^(8-j),

with the fully displayed positive integer coefficients

    (16253740,760378532,7144614835,30009930716,
     45103320694,37839020864,21922217299,
     7744836200,1102358320).

All nine constants and the identity are part of this proof, not a pointer to the1512-entry coefficient certificate. Thus D>0 and E_0>0. This completes EM4, then EM3/EM2 prove EM for the equal-maximum integer face.

## Status and next boundary

This note eliminates any need for Bernstein sign checks on the r=0 face, with independent review of the explicit identities and inequalities now PASS. It does NOT prove the separate saturated-face q=0 boundary. The main first-head proof still must combine its other boundary reductions, integer discriminant branches, and that boundary before any pure-analytic ledger promotion. The old1512 certificate remains valid throughout; no count is changed here.
