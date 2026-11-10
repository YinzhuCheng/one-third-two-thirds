# Correlated missing-run boundary for private-predecessor lifts

Status: analytic manuscript, collaborative reconstruction complete, final uninvolved independent audit requested. No new object search or LE DP is needed. This advances the previous private-predecessor lift, not a new novelty claim about deadline counting. It is not full B1/D10 payment.

## 1. Exact inherited original-order contract

Let P be any finite original B1, with roots a,b, a below all other non-b labels, private ideal T={x,y,z} a three-antichain, R=P−{a,b}, C=R−T. C may have empty T-signatures. Let E be a C-ideal, every point of which has complete T-signature exactly {y,z}. Put

    m=|E|, Mx=C−U_P(x), k=|Mx|; hence m<=k.

Add u with a<u<x and u<C−E, otherwise only transitive closure. As established in the sealed preceding theorem, this retains P induced, changes the private ideal to u<x plus y,z, preserves three private a-children, and increases the physical intrinsic J by exactly u. New u is incomparable exactly with b,y,z,E. Old b,y,z and E labels gain one degree each; all other old degrees stay fixed. In an actual Delta10 lift, k<=7 since deg_P(x)=k+3, and m<=7 since deg_(P+)(u)=m+3.

For uniform original words, let A_i count LE(R) words with initial private prefix length i. Define I=#K2 words whose prefix contains x, X=#K1 words with prefix x, Y=A1−X. Let L be the total leading E-run after the initial y,z prefix over old K2,x-out words. Write N=e(P+), K=#LE(P+) with u<b. The preceding exact original-word/root-slot formulas are

    N=3A0+12A3+15A2−15I/2+4L+4X+8Y,
    K=A0+(20/3)A3+6A2−2I+2X+3Y,
    3K−N=8A3+3A2+(3/2)I−4L+2X+Y.          (1)

The old upper bound K/N<=5/9 remains valid. All counts here are original full-word counts, not equal weighting of interface sources. The seed's original moment condition is A3>=A2+2A1+2A0.

## 2. The correlated C-word identities

For beta in LE(C), let h_i(beta) be its initial run missing root i. Let q(beta) be its initial E-run. Then 0<=q<=h_x<=k. If q>0, the first C label has signature {y,z}, so h_y=h_z=0. Put s=h_x+h_y+h_z. Exact deletion/insertion gives

    A3=6e(C),
    A2=2 sum_beta s(beta),
    I=2 sum_beta (h_y+h_z),
    L=2 sum_beta [q h_x−q(q−1)/2].           (2)

For the last identity, after the first y,z in either of their two orders, insert x after j C letters, 1<=j<=h_x. That old word has initial E-run min(q,j), and sum_j min(q,j)=q h_x−q(q−1)/2. This is a literal unique recovery of the original words; it does not freely combine the largest L with the largest A2.

Substituting(2) into(1),

    3K−N=sum_beta F(beta)+2X+Y,
    F(beta)=48+(6−8q)h_x+9(h_y+h_z)+4q(q−1). (3)

If q=0, F>=48. If q>0, s=h_x and

    F=48+(6−8q)h_x+4q(q−1).                (4)

This same-word correlation is the missing ingredient in the earlier independent scalar caps.

## 3. Complete sharp scalar-contract guarantee

For m>=1,k>=m define

    Phi(k,m)=48+(6−8m)k+4m(m−1).

For q>0, (4) decreases as h_x grows, hence F>=Phi(k,q). Also

    Phi(k,q+1)−Phi(k,q)=8(q−k)<=0.

Thus every beta has F>=Phi(k,m); the q0 case also does because Phi(k,m)<=48 for k>=m>=1. Therefore Phi>=0 guarantees the original fixed pair (u,b) is balanced; Phi>0 guarantees its lower inequality strictly. m=0 is separately automatic: F>=48.

This is necessary as well as sufficient for a guarantee using ONLY actual (k,m), in the following precise sense. For every m>=1,k>=m take any m-point poset E and let

    C=E ordinal-sum a (k−m)-point chain,
    every C label above y,z and incomparable with x.

Add standard B1 roots, then perform the lift. In every C word, q=m,h_x=k,h_y=h_z=0, and A0=X=Y=I=0. If e=e(C)=e(E),

    A3=6e, A2=2ke,
    L=2e[mk−m(m−1)/2],
    K=(40+12k)e,
    N=[72+(30+8m)k−4m(m−1)]e,
    3K−N=e Phi(k,m).                       (5)

Hence Phi<0 has an actual original-poset counterexample to the marked pair's lower bound. It does NOT say every object beyond that cap fails, and is NOT a counterexample to B1 or to existence of another balanced pair.

Taking E an antichain gives complete Delta(P+)=max(k+3,5). Therefore all listed failures with 0<=m<=k<=7 are actual Delta10 objects. They retain fair twins y,z (and often other modules), so old guards already pay them; their sole purpose is sharpness of this marked-pair parameter contract.

Within Delta10, the COMPLETE universal scalar guarantee region is exactly:

- m=0 or1: every feasible k<=7;
- m=2: k<=5;
- m=3: k<=4;
- m>=4: no feasible k gives a guarantee solely from(k,m).

Concrete exact controls from(5):

    (m,k)=(2,5): p=50/147>1/3;
    (2,6): p=28/85<1/3;
    (3,4): p=1/3;
    (3,5): p=50/159<1/3;
    (4,4): p=11/34<1/3.

No finite search is used in these computations.

## 4. Consequences for the previous rho boundary

The previous rho was

    max_(i!=j)(|C_empty|+|C_i|+|C_ij|).

Since Mx=C_{y,z}, k<=rho. Thus two new unconditional original-structure classes are:

- rho<=5, m<=2 (in fact only k<=5 is needed);
- rho<=4, m<=3 (in fact only k<=4 is needed).

The first strictly improves the earlier rho4/m2 condition. The control m2,k5 has rho5 and fails both the old seed moment condition and the preceding coarse gate8A3>=5A2, but the correlated kernel pays it. It has old fair twins and carries no new-net-coverage claim.

At m3,k4, if p(u<b)=1/3, equations(3)–(4) force every C word to have q=3,h_x=4 and X=Y=0: all other kernels are positive. In particular every C-minimal point lies in E. Every C point is then above a C-minimal E point, hence above both y,z. The two original labels y,z have equal complete lower set {a} and equal complete upper set C, so they are fair twins in P+. Thus the new endpoint is genuinely realizable but already covered by old guards; non-twin objects in this endpoint contract have a strict lower inequality.

## 5. The old-moment three-hole closure survives all of Delta10

The sharp scalar table does not use seed moments. Stronger seed information permits genuinely larger safe parameter regions. Let m>=1 and k>=m, and set

    b=8m−6−4m(m−1)/k>0.

For q>0 rewrite F=48−a(q,h_x)h_x, where

    a(q,h)=8q−6−4q(q−1)/h.

For fixed q this increases with h; moreover

    a(q+1,k)−a(q,k)=8(1−q/k)>=0.

Hence a(q,h_x)<=a(m,k)=b. For q0, F>=48 and s>=0. In all cases

    F>=48−b s.                              (6)

The old moment condition is equivalent, by(2), to

    sum_beta s + A1+A0 <=3e(C).               (7)

Equations(3), (6), (7) give

    3K−N >=(48−3b)e(C)+b(A1+A0)+2X+Y.        (8)

For m=3, 48−3b=72/k−6, positive whenever k<12. Every legal Delta10 lift has k<=7. Thus **an old original moment-paid seed admits every legal three-hole Delta10 lift of this exact signature-ideal type, with the one fixed new pair (u,b) strictly balanced**. This strictly enlarges the preceding m<=2 closure. The m3,k5 scalar counterexample is not a contradiction: its old seed fails the moment condition.

## 6. Quantitative old-moment correlated interval

A stronger quantitative consequence, not claimed sharp, is

    Pr(u<b)>=76/(180+3b)
             =38k/[(81+12m)k−6m(m−1)],       (9)

with the same5/9 upper bound. Here m>=1,k>=m and the old seed moment condition is assumed; for larger m the lower bound need not exceed1/3.

For a proof write Hx=sum h_x, Ht=sum(h_y+h_z). The bound on a in section5 also gives

    L<=((b+6)/4)Hx.

Thus by(1)–(2),

    N<=72e(C)+(36+b)Hx+15Ht+4X+8Y+3A0,
    K=40e(C)+12Hx+8Ht+2X+3Y+A0.

Let Z=3e(C)−Hx−Ht−X−Y−A0>=0 from(7). Substitute e(C)=(Hx+Ht+X+Y+A0+Z)/3. The numerator K coefficients in (Hx,Ht,X,Y,A0,Z) are

    (76/3,64/3,46/3,49/3,43/3,40/3),

and the displayed upper denominator has coefficients

    (60+b,39,28,32,27,24).

Since b>=2, the minimum coefficient ratio is (76/3)/(60+b), giving(9). This is a nonnegative-coordinate inequality on exact counts, not a claim that every coordinate vector is poset-realizable.

For m=3 and Delta10 k<=7, r in(9) is minimized at k7, so the uniform genuine-original-P window is

    266/783 <=Pr(u<b)<=5/9,

with lower margin5/783 above1/3. No sharpness or attainment claim is made for this probability constant.

## 7. Dedup, actual scope, and unchanged open work

- The exact root-slot event formula, original-word deadline kernel and5/9 upper bound are inherited from the sealed private-predecessor-lift theorem. The new content is the SAME-C-word coupling of h_x,q, the sharp scalar table, and the old-moment chord extension.
- m0 lifts are already paid by the old two-sided factor2 theorem; they are not new net coverage.
- The actual sharpness/overlap controls in section3 all have fair twins/modules. They negate marked-pair parameter guarantees only, not global B1 payment or NB.
- The earlier V2 example E={h1,h2,h3} is a genuine k4,m3,Delta10,non-twin original structure. Its previously stored numeric counts are not needed here: the new original-structure theorem pays it directly. However the preceding generic weak count gate8A3>=9A2 already pays that specific object. Do NOT count it as newly paid ordinary population; it demonstrates nonvacuity beyond twins only.
- The new pure k cap does not subsume all old seed-moment m2 instances at k6/7; the union of conditions should be retained. Conversely pure-cap controls need not have moment-paid seeds. These are different input classes.
- No full B1/T4/varying-J theorem, all-history comparison, or counterexample to the1/3–2/3 conjecture is claimed.
- The lift still changes T and raises intrinsic J by exactly one; all hypotheses of the earlier same-T J-lock are deliberately not met.

 No new poset enumeration or LE program is required for the theorem or controls.
