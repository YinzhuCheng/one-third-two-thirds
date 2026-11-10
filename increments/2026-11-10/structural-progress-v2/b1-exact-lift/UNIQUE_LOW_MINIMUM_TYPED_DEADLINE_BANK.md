# UL1: unique-low-minimum typed deadlines in the two remaining k7 cells

2026-11-10 UTC. Analytic author candidate, independent review requested. Exact original D10 lift only; research manuscript. This proof does not claim payment for the two-low-minimum patterns.

## Statement

Consider the original exact lift with zero x-frontier and exactly one actual low C-minimum f, of empty signature. In either (m,k)=(4,7) or (5,7), this manuscript claims an ordinary strictly balanced pair. The proof chooses one physical bank for the WHOLE original poset using the actual typed set Mx-E-{f}; it never changes pairs or bank weights between words.

Use F,G of WB5/WB6, and the exact triple-gap A0 formula of EC3/EC4. A bank margin alpha F+beta G means the complete original sum, with individual upper bounds ub<=5/9,yb/zb<=1/2.

## 1. The real typed deadline and its shared budget

Put R=Mx-E-{f}, and partition it into R_hi (signature yz) and R_lo (empty,y,z). Every v in R_lo lies above f. Indeed any C-minimum below v has signature of size at most one, and the unique such C-minimum is f. Write r=|R_hi|.

All C labels missing x are exactly E,{f},R_hi,R_lo. For any actual beta with runs H,Y,Z, the initial min(H,max(Y,Z)) labels miss x and at least one of y,z. They cannot be in E or R_hi. Thus

    min(H,max(Y,Z)) <=1+|R_lo| = k-m-r.         (1)

This strengthens the common-empty budget, and comes from the literal SAME initial words.

Delete f and fix an actual gamma, with legal f gaps0..d, d<=7. Let h=h_x(gamma)<=6 and q=q(gamma)<=min(m,h). Every R_lo label is an f-successor, so if q<h and the first non-E label in that initial missing-x run is low, then d=q. More generally, if h>m+r, the initial h labels contain a low label, hence d<=h-1. All these deadlines refer to real original f-successors; none is a freely chosen profile condition.

At q>=1, use the exact E-start kernels of EC3/EC4, including F0=80+8h,G0=8-2h. At q0 the first actual gamma label is either yz (an original C-minimum or a member of R_hi) or an f-successor. In the latter case d0. At gap0 all root runs are positive; at later gaps starting yz, A0=A1=0 and Q=Y=Z=0. These later kernels are positive for all combinations used below.

## 2. A common 3F+2G lemma with budget2

Let T=3F+2G. At a q0 f-first word its exact triple-gap expression is

    T=200+30H+25(Y+Z)+2[YZ+min(Y,Z)]
           -H(Y+Z)-min(H,Y)-min(H,Z)-4a_beta.

Assume 1<=H<=7,1<=Y,Z<=6 and min(H,max(Y,Z))<=2. Then T>=168.

If H<=2, bound a_beta<=H[YZ+min(Y,Z)+Y+Z+2] and min(H,Y)+min(H,Z)<=2H. This gives

    T>=200+20H+(25-5H)(Y+Z)+(2-4H)[YZ+min(Y,Z)].

Use YZ+min(Y,Z)<=7(Y+Z)/2. At H1 the lower bound is at least220+13(Y+Z)>=246; at H2 it is at least240-6(Y+Z)>=168.

If H>=3, condition(1) forces Y,Z<=2. Thus a_beta<=6H+12 and y_beta<=4H+4. Dropping only the positive 2x_beta gives

    T>=148+2H+25(Y+Z)>=204>168.

(The weaker number204 suffices.)

For an E-start gamma the exact kernels are

    T0=256+20h,
    Tj=200+(30-28Q_j)H_j+14Q_j(Q_j-1), j>=1,
    H_j=h+1_(j<=h), Q_j=min(q,j).

Increasing Q changes Tj by28(Q-H)<=0. For h<=4 lower q to h: the sum through h is

    B(h)=256+(694h+6h^2-28h^3)/3,

and every later increment is c(h)=200+16h-14h^2>=40. B is concave on[1,4] with endpoint values480,616, so every partial prefix is at least min(T0,B)>=276.

For h5 lower q to5. The exact successive kernels through gap7 are

    356,212,72,-40,-124,-180,-70,-70,

with minimum prefix total156. For h6,q<=5,d<=5, lower q to5: the kernels through gap5 are

    376,214,46,-94,-206,-290,

with minimum prefix total46. If h6,q<=4,d<=5, lowering q to4 instead gives minimum130 (the last two increments are both -206). The prefix endpoint arguments follow from the same decreasing initial increments and constant tail already independently reviewed in EC3/EC4. Thus this lemma handles both configurations below, with true positive margin in every actual fiber.

## 3. m4k7: all three high-count cases

Here |R|=2.

### r=0

Every R point is low and above f. If q<h, the first non-E missing-x label is low, forcing d=q<=4. If q=h, then h<=4.

Use F alone, so the result in this subcase is fixed-u/b payment. For q=h<=4, the sum through h is

    B_F(h)=80+(170h-6h^2-8h^3)/3,

and the later increment is48+2h-4h^2. The full prefixes have minimum at gap0,h,or7. For h1,2,3 the noninitial kernels through h are nonnegative and all later kernels positive. At h4, B_F=104 and every later increment is -8, leaving at least80. Thus these fibers are positive.

For q<h, d=q. At q1 the fiber total is126+6h>=132. For 2<=q<=4, its total is nonincreasing in h (the coefficient of h is8+2q-4q^2<0), so lower it using h6. The resulting total is

    128+(182q-84q^2+4q^3)/3.

This polynomial decreases on[2,4] and equals8 at q4. Thus the fiber is at least8. A non-E-start gamma must be an f-child (there is no non-E original yz minimum), so its only f-slot has q0 and F>=48. All fibers are positive.

### r=1

There is one low label; (1) has budget2. Use the one fixed bank margin3F+2G. For h<=5 all E-start fibers are positive by Section2. If h6, then h>m+r=5, so d<=5; q<=4, and Section2 gives total at least130. Non-E-start first-gap words satisfy the budget2 lower bound168; every later word starts yz and has T=200+30H>0. Thus the whole fixed bank is strictly paid.

### r=2

There are no R_lo labels. Hence f is the only empty label in C. The already independently reviewed WB4 theorem applies directly: its unique-low-minimum and zero-frontier premises remain exactly those here. It gives the physical (4,1,1)/6 bank, with no use of a new degree bound.

## 4. m5k7: both high-count cases

Here |R|=1.

### r=0

There is one low label above f. Condition(1) has budget2. Use the fixed bank margin3F+2G. All h<=5 E-start fibers are positive by Section2. If h6, then q<=5<h and the first non-E missing-x label is the low label, forcing d=q<=5. Section2 gives total at least46. The q0 first-gap words are at least168 and all later yz-start words positive. Thus this subcase is paid.

### r=1

There are no low labels outside f, so all missing-x labels outside E are f and one yz label. Use the one fixed bank margin T=2F+3G.

First remove the already paid original root VG guard. Let A=U_C(y)-U_C(z), B=U_C(z)-U_C(y), and L=C-(U_C(y) union U_C(z)). If both A,B are chains the original y,z positive VG applies, since D(y)=D(z)={a}. Otherwise one side has at least2 labels. The full original y/z degrees give |L|+|A|<=6 and |L|+|B|<=6; hence |L|<=4. Thus every true beta satisfies

    min(Y,Z)<=4.                               (2)

For a non-E-start gamma, its first label is either yz or an x-containing f-child. A yz first label gives at gap0 Y=Z=1 and T=174+10H>0; every later legal gap starts yz and gives T=180+30H>0. An x-containing child forces d0 and H1; there are no other possibilities. In this case

    T=190+5(Y+Z)-8YZ-8min(Y,Z)>=16,

by (2), Y,Z<=6, symmetry, and the separate monotonicity of this expression on Y,Z>=1. The minimum is at the allowed corner(4,6).

For E-start gamma, use q<=min(5,h), h<=6. If h<=5, lower q to h. The exact sum through h is

    B(h)=184+(616h+24h^2-22h^3)/3>184,

and the later increment180+19h-11h^2 is nonnegative for1<=h<=5. Prefix minima at0,h,7 are therefore positive. At h6, lower q to5. The successive kernels through gap7 are

    244,236,104,-6,-94,-160,-160,-80,

whose minimum prefix total is84. Thus every true fiber has positive total, completing this subcase.

## 5. Ledger effect and limits

All routing above uses actual signature counts r fixed by the original poset, so one physical bank is fixed before summing its genuine words. Every bank member separately has its original upper bound. No conditional mixing, pair selection per fiber, or OLD moment is used.

If accepted, UL1 removes all unique-low-C-minimum branches from m4k7 and m5k7. Their parameter cells remain open only in the existing two-low-minimum patterns (at least one actual empty C-minimum). In m5k7, the accepted RG1 classification leaves exactly empty+one singleton-y/z. In m4k7, this manuscript makes no new restriction among the two-low-minimum patterns. No joint realizability, outside-all-history novelty, full B1/D10, fixed-u/b guarantee outside the stated r0 subcase, or NB claim is made.
