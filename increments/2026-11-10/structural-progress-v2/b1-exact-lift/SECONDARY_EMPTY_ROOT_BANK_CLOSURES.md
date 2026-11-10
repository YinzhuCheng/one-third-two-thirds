# EC3/EC4: true triple-gap credit closes m3k7 and m4k6, including secondary empty labels

2026-11-10 UTC. Analytic author candidate; independent review requested. Original exact-D10 lift only. No no poset-family search, and no computational positivity certificate. A small finite root-run diagnostic suggested the coefficients; the proof below is analytic and does not depend on that diagnostic.

## Statements and original contract

Assume the original exact lift has zero x-frontier and exactly one low C-minimum f, of empty old T-signature. Other C-minima therefore have signature yz. **Nonminimal empty labels are allowed throughout.** Use the full original counts N,K_u,K_y,K_z and the exact kernels F,G in WB5/WB6: sum F=3K_u-N, sum G=K_u+K_y+K_z-N.

- **EC3**, m3k7: 24K_u+3K_y+3K_z-10N >=8e(C)>0. The one fixed physical bank has weights (8,1,1)/10 on (ub,yb,zb).
- **EC4**, m4k6: 7K_u+K_y+K_z-3N >=12e(C)>0. Its fixed physical bank has weights (7,1,1)/9.

The candidate-wise upper bounds ub<=5/9,yb/zb<=1/2 give an ordinary strictly balanced pair in each case. Combined with the already accepted unique-low-minimum reductions, these close the whole formerly remaining m3k7 and m4k6 ordinary cells. No uniformly specified u/b payment or full D10/B1/NB theorem is claimed.

## 1. The missing true triple-gap formula and shared empty budget

For any actual C word beta with root-missing runs H,Y,Z, the exact A0 count is

    a_beta=HYZ+H min(Y,Z)+Y min(H,Z)+Z min(H,Y)
                    +2min(H,Y,Z).                          (1)

Choose positive insertion gaps for all three old private roots. The baseline product counts one order. Every coincident pair adds one, and at a triple coincidence the baseline plus three pair corrections is4 rather than6, requiring two further orders. This proves (1) by literal old-word recovery.

Recall x_beta=YZ+min(Y,Z), y_beta=H(Y+Z)+min(H,Y)+min(H,Z), with A1_beta=x_beta+y_beta. For Q=q(beta)=0 the complete original kernels are

    F=48+6H+9(Y+Z)+2x_beta+y_beta,
    G=28+6H-(Y+Z)-2(x_beta+y_beta)-2a_beta.       (2)

An empty label belongs to Mx-E. Thus the TOTAL number of empty C labels is at most k-m. In particular every actual beta satisfies the correlated bound

    min(H,Y,Z) <= k-m.                          (3)

The left side is exactly the initial all-three-roots-missing run, hence consists of distinct true empty labels. This is not an independent free deadline cap. Always H<=k, Y,Z<=6 by the full original root degrees.

Delete the actual minimum f and fix a genuine gamma in LE(C-f). Its f gaps form 0..d with d<=7. Put h=h_x(gamma)<=k-1, q=q(gamma)<=min(m,h). No moment or degree bound is transferred to the deleted object.

If gamma starts in E, q>=1. At gap0, (H,Y,Z)=(h+1,1,1), so F0=80+8h,G0=8-2h. At j>=1, beta starts in E: all original A0/A1 prefix terms vanish and

    H_j=h+1_(j<=h), Q_j=min(q,j),
    F_j=48+(6-8Q_j)H_j+4Q_j(Q_j-1),
    G_j=28+(6-2Q_j)H_j+Q_j(Q_j-1).              (4)

If gamma does not start in E, its first label is either an original C-minimum of signature yz, or an actual successor of f. In the latter case d=0, even if that successor is empty. In the former case, every j>=1 begins with yz and has Q=Y=Z=0, so any positive combination of F,G has positive kernel with its stated constant term. At gap0, beta always starts with f, Q0 and positive H,Y,Z; use (1)-(3), allowing all three runs to exceed1.

## 2. EC3: the q0 first-gap kernel is at least232

Write T=7F+3G. Equations (1)-(2) give

    T=420+60H+60(Y+Z)+8[YZ+min(Y,Z)]
             +H(Y+Z)+min(H,Y)+min(H,Z)-6a_beta.   (5)

Here 1<=H<=7,1<=Y,Z<=6,min(H,Y,Z)<=4. The expression is symmetric in Y,Z; assume Y<=Z. Then

    T=420+68Y+60Z+8YZ
        +H[60-5Y-(6Y-1)Z]
        -(11+6Z)min(H,Y)-(6Y-1)min(H,Z).          (6)

If Y<=2, the constant part is at least556; the H coefficient is at least -16, hence its term is at least -112; the two final penalties total at most47*2+11*6=160. Thus T>=284>232.

If Y>=3, the H coefficient is at most -6 and both minimum penalties are nonincreasing as H grows. Thus T decreases with H. For 3<=Y<=4, use H7. Since Z<=6, both minimum terms simplify and

    T>=840+22Y+68Z-46YZ
      >=1248-254Y >=232.

The second inequality uses 68-46Y<0 and Z<=6. For 5<=Y<=Z<=6, (3) forces H<=4. Use H4; both minimum terms are4, so

    T>=620+24Y+40Z-16YZ
      >=860-72Y >=428.

This proves the q0 bound analytically over the full necessary original run domain, not merely at sampled tuples.

## 3. EC3: E-start gamma fibers have total at least70

At gap0, T0=584+50h. At every j>=1,

    T_j=420+(60-62Q_j)H_j+31Q_j(Q_j-1).         (7)

Increasing Q by1 changes this by62(Q-H)<=0. For h<=3, lower to q=h. Every term is positive: the smallest noninitial value through the h-th gap is102 (h3,j3), while all later values are at least228. Hence every partial fiber has total much more than8 times its cardinality.

For 4<=h<=6, lower q to3. The first two increments are 418-2h and 418-64h, followed up to gap h by the constant 480-126h. The gap0 through gap h sum is

    B3(h)=460+716h-126h^2.

Each later increment is 606-126h, so the sum through gap7 is

    B3(h)+(7-h)(606-126h)=4702-772h >=70.

The initial increments decrease through their plateau, and then jump upwards to a constant; thus any prefix minimum occurs at gap0,h,or7. The gap0 value is at least784; B3 is concave on [4,6] with endpoint values1308,220, hence at least220. The gap7 expression is at least70. Therefore every actual E-start fiber has total at least70 and at most8 words, giving at least8 times its true cardinality.

For non-E-start fibers, Section1 and the q0 bound232 handle gap0, while every later gap (if present) has kernel420+60H>=420. These too give at least8 times their actual cardinality. Summing true fibers proves EC3.

## 4. EC4: the q0 first-gap kernel is at least160

Now T=2F+G. Equations (1)-(2) yield

    T=124+18H+17(Y+Z)+2YZ+2min(Y,Z)-2a_beta.     (8)

Here H,Y,Z<=6 and min(H,Y,Z)<=2. If H<=2, bound

    a_beta <=H[YZ+min(Y,Z)+Y+Z+2].

This gives

    T>=124+14H+(17-2H)(Y+Z)+(2-2H)[YZ+min(Y,Z)].

For H1 the lower bound is at least168. For H2, use YZ<=3(Y+Z) and min(Y,Z)<=(Y+Z)/2; it is at least152+6(Y+Z)>=164.

Otherwise H>=2, and by symmetry assume Y<=Z and Y<=2 (as (3) forces). With min(H,Y)=Y, (8) becomes

    T=124+18H+15Y+17Z-2HYZ-2HY-2Ymin(H,Z).

At Y1 it is 139+16H+17Z-2HZ-2min(H,Z). Replacing the minimum by6 gives the bilinear lower bound127+16H+17Z-2HZ, whose corner values on [2,6]x[1,6] are172,237,228,253. At Y2 the same argument gives130+14H+17Z-4HZ, with corner values176,212,200,172 on [2,6]x[2,6]. Thus in all cases T>=160.

## 5. EC4: E-start fibers have total at least98

At gap0 T0=168+14h. At j>=1,

    T_j=124+(18-18Q_j)H_j+9Q_j(Q_j-1).         (9)

Increasing Q by1 changes it by18(Q-H)<=0. For h<=4, lower q to h. The mandatory gap0 through gap h sum is

    B4(h)=168+144h-6h^3,

and every later increment is c4(h)=124+9h-9h^2>=16 on1<=h<=4. B4 is concave on [1,4], with endpoint values306,360, hence at least306. As in EC3 the prefix minimum lies at gap0,h,or7, so every such fiber has total at least182.

For h5, lower q to4. The successive kernels from gap0 through7 are

    238,124,34,-38,-92,-92,-38,-38.

Their sum is98; their prefix minimum is min(238,98)=98. Thus every actual E-start fiber has total at least98 and at most8 words, hence at least12 times its true cardinality. Every non-E-start fiber has first-gap contribution at least160 and any later contributions124+18H>=124. Summing the actual fibers proves EC4.

## 6. Exact ledger and dependencies

The two claims are pure analytic weighted-root-bank extensions, preserving all original E and tail multiplicities and consuming prefix credit once. They need no OC2/OC3/OC4 or ND1 computer-assisted core counts. Equation(1) extends, rather than incorrectly reusing, WB5's min-run-one identity.

After accepted independent review and the prior unique-low-C-min reductions, these claims would leave only m4k7 and m5k7 in the necessary zero+empty ordinary parameter list. Both permit more complex low-minimum patterns; neither has been paid by this manuscript. All previous ordinary/fullscreen/prime/NB scope limits remain unchanged.
