# A three-physical-pair bank for the exact private-predecessor lift

Date: 2026-11-10 UTC. **Analytic candidate; independent audit requested.** This is a transport application of the accepted original root-slot mechanism. No literature-originality or net-new-population claim is made.

## Contract and two conclusions

Retain the exact original seed/lift contract of MC1: original B1 minima a,b, a below every non-b label; old private ideal T={x,y,z} a three-antichain; C=R-T; E a C-ideal of complete T-signature {y,z}; and the lift a<u<x,u<C-E. Let m=|E|,k=|C-U(x)|. Uniform probabilities always mean the complete original lifted poset P+, not a uniform interface law.

The physical candidate library, fixed before any word or completion is counted, is

    (u,b), (y,b), (z,b),

with constant bank weights1/3 each. Put S=K_ub+K_yb+K_zb and N=e(P+).

**TB1 (OLD-moment transport, no degree bound needed).** If m<=7 and the old seed has A3>=A2+2A1+2A0, then

    S/(3N)>=167/495>1/3.

At least one of these three physical pairs has probability in[167/495,5/9]. In particular every legal D10 lift of an OLD-moment seed is ordinary-balanced, including the four parameter points where the fixed pair (u,b) is not universally balanced. There is no restriction on k or overall size in TB1 beyond the exact seed/lift contract; D10 is not used once m<=7 is given.

**TB2 (structural, no OLD moment).** Assume the actual lift has full Delta10 and every C-minimum has at least two old T predecessors. Equivalently A0=A1=0. Then

    S/(3N)>=260/759>1/3,

so one of the same three physical pairs has probability in[260/759,5/9]. No seed-moment hypothesis is used. The lower constant is a bound on the fixed bank's mean, not a claimed optimal balanced-pair constant.

Neither conclusion says the same one member of the library works for every poset, nor that each library member is balanced. They choose one physical pair only after computing whole-object probabilities, not one pair per word or conditional fiber.

## 1. Candidate-wise original upper bounds

The accepted lift count gives Pr(u<b)<=5/9 for every seed, without moments or degree assumptions.

For y (and identically z), D(y)={a},D(b)=empty and U(y) is contained in U(b)=C. In a complete P+ extension with y before b, swapping these two labels is legal: b moves earlier with no predecessors and more successor obligations; y moves later, all its successors were after old b because they are b-successors. Every predecessor of y remains before it. This is an injection into the reverse-event words, so

    Pr(y<b)<=1/2, Pr(z<b)<=1/2.

Thus every candidate has its own upper bound below2/3. This is not an average upper bound used as if it were candidate-wise.

## 2. Independent table for S and N

Use inherited actual old R-word counts A_i,I,X,Y and L. Here I counts K2 prefixes containing x; X counts K1 prefixes x; Y=A1-X; for a K2 prefix y,z, ell is its leading E run after that prefix, and L is the sum of ell over those full old R-words.

Restoring a,b from any lifted R+ word with private prefix length K gives K+2 root slots. A private label at prefix rank r contributes K-r+1 slots with that label before b. This is the true original root multiplicity.

Deleting u gives a unique old R-word and legal insertion slot before its first label in {x} union(C-E). The contributions are:

| Old class | S contribution per old word | N contribution per old word |
|---|---:|---:|
| K0 |1|3|
| K1 prefix x |2|4|
| K1 prefix y or z |6|8|
| K2 contains x |7 averaged over x ranks|15/2 averaged over x ranks|
| K2 prefix y,z |18+3ell|15+4ell|
| K3 |50/3 averaged over x ranks|12 averaged over x ranks|

The rank averages are literal symmetric legal-prefix cells, not equal weighting of different posets or suffix laws. For K2 containing x, its two ranks give S values4 and10, respectively. For K3 with x at old rank r=1,2,3, there are r u-slots; each new prefix has K4, and the three children u,y,z contribute6+r root slots. Thus r(6+r) has values7,16,27 and average50/3. The rank divisibilities are automatic from the legal prefix permutations.

Summing this original-word table gives exactly

    S=(50/3)A3+18A2-11I+3L+2X+6Y+A0,
    N=12A3+15A2-(15/2)I+4L+4X+8Y+3A0.

As a cross-check, summing over all four private labels gives sum K(K+1)/2 over lifted R+ words; subtracting the non-child x event yields the same S. Its exact count is

    K_xb=(10/3)A3+2I+X.

For old x rank r in a private prefix of size i, the r u-slots each leave i-r+1 favorable root slots for x, giving r(i-r+1); its rank averages are1,2,10/3 for i1,2,3.

## 3. TB1: seed moment and strictness

Let J=A2-I and let s0=A3-A2-2A1-2A0>=0. The exact difference is

    S-N=(14/3)A3+3A2-(7/2)I-L-2A1-2A0.

Use only the literal bound0<=L<=mJ. Then

    S-N >=(14/3)s0+(25/6)I+(23/3-m)J
                  +(22/3)(A1+A0).

For m<=7 every coefficient is positive. A3>0 because T is an ideal and can be listed first, so the right side cannot vanish: otherwise all I,J,A1,A0,s0 would vanish, forcing A3=0. Hence S>N strictly for every actual seed under TB1, including all boundary m values.

A useful uniform quantitative bound follows in the nonnegative coordinates(I,J,X,Y,A0,s0). At L=mJ the S coefficients are

    (71/3,(104+9m)/3,106/3,118/3,103/3,50/3),

and the N coefficients are

    (39/2,27+4m,28,32,27,12).

Every coordinate ratio is at least167/165 for m<=7; the J ratio decreases with m and equals167/165 at m7, while all other ratios are larger. Since3-4(167/165)<0, replacing actual L by its upper bound mJ can only decrease S-(167/165)N. Thus S/N>=167/165 and TB1 follows. This uses a nonnegative-coordinate inequality on exact counts; no abstract coordinate vector is assumed realizable and no sharpness claim is made for167/495.

## 4. TB2: a same-C-word no-moment bank

If a C-minimum has support at most one, it can be placed after exactly those required old private roots and before the other old roots, producing A0>0 or A1>0. Conversely any K0/K1 word begins at such a C-minimum. Thus the structural hypothesis is equivalent to A0=A1=0 (vacuously if C is empty), and X=Y=0.

For beta in LE(C), set h=h_x,t=h_y+h_z,q its initial E run, and

    l=2qh-q(q-1).

The inherited correlated identities turn N and S into sums of the same-word positive kernels

    n_beta=72+30h+15t+4l,
    s_beta=100+36h+14t+3l.

Full D10 gives h<=k<=7 and h_y,h_z<=6, because each of y,z has the four outside-C incomparable labels b,x,the other root,u. Also q<=h; if q>0 then t0.

If q0, l0 and

    253s_beta-260n_beta=6580+1308h-358t
                              >=6580-358*12>0.

If q>0, t0 and l<=h(h+1), so

    253s_beta-260n_beta
      =6580+1308h-281l
      >=6580+1027h-281h^2>=0.

The last polynomial is concave on0<=h<=7 and has endpoint values6580 and0. Thus every actual beta has s_beta/n_beta>=260/253. Summation over the same physical C-word fibers proves S/N>=260/253. No old moment, deleted-object probability, or freely assigned completion weight was used.

The same identities also yield the weaker count-only gate

    S-N>=14e(C)-2(A1+A0).

Indeed the per-C-word margin is28+(6-2q)h-t+q(q-1), at least14 throughout the true D10 run domain. Hence A1+A0<=7e(C) suffices for a closed balanced member of the bank, and strict inequality gives strict lower payment. This is an additional original-count sufficient condition, not an assertion that it follows for every D10 object.

## 5. Actual contracts, separation and old guards

TB1 is nonvacuous for every integer m0,...,7 in actual D10. Take C the disjoint union of an m-chain E of signature {y,z} and a two-chain of full signature. Then k=m, E is an actual ideal, e(C)=C(m+2,2), A1=A0=0 and A2=2C(m+2,3),A3=6C(m+2,2). The old moment holds since m<=7<9. The full lifted degree is max(m+3,5)<=10. This certifies every hole-size contract, but y,z are twins and the example also has old chain/very-good guards; no new population credit is assigned.

For TB2 take C=E a seven-chain of signature {y,z}, with no other C labels. The actual lift has m=k7, Delta10,

    A3=6,A2=14,A1=A0=I=0,L=56,
    N=506,S=520,K_ub=124.

The old seed moment fails6<14 and Pr(u<b)=62/253<1/3, whereas Pr(y<b)=Pr(z<b)=99/253. The bank mean equals260/759, showing the TB2 bank-mean lower constant is attained. This is not an optimal-best-pair claim, and y,z are again old fair twins.

All four actual u/b countercontrols from MC1 satisfy TB1 and in fact A1=A0=0, so they also satisfy TB2. Their marked failure is preserved; the conclusion is that another member of the three-pair library pays them. They already have y,z twins, so this absorption is not new net coverage.

The general mechanism is a derived use of the already accepted root-prefix sum law, with a non-child event x/b subtracted and seed-moment transport retained. It is different from assuming the new T4 two-moment condition. For the seven-chain TB2 control, the new criterion has margin24A3-12A2-14L=-808<0, so that new criterion fails too. This separates input tests only, not all historical ordinary-payment mechanisms.

For ordinary balanced-pair existence TB1 subsumes the positive m/k region of MC1 and pays its four unsafe marked-pair parameter classes. MC1 remains stronger where a guarantee for the specified u/b pair is needed. TB2 removes OLD moment under a real signature condition. Neither statement solves arbitrary B1/T4, nor certifies an object outside every previously paid guard.

No external repository or document was modified. All bank identities and controls are analytic; there is no object enumeration or finite certificate dependency in this manuscript.
