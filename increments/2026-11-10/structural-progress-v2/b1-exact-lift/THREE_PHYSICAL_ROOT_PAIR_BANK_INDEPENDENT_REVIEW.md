# Independent analytic audit of the three physical root-pair bank

2026-11-10. **PASS: TB1, TB2, additional closed gate, and the stated scope.**

Target: `THREE_PHYSICAL_ROOT_PAIR_BANK.md`, SHA256
`e67b715b55a3985c6b024743711558bf60bd9f9231380d42eeb9d896b98f38cc`.

This is a nonblind internal independent mathematical review. I did not participate in this bank's derivation. I independently reconstructed the complete-word table, upper bounds, inequalities and realizations after reading the frozen manuscript. This review uses analytic counting, not original-poset enumeration, numerical certificates, formal verification or an originality claim. No hard gap was found. No external repository was modified.

## 1. Literal old-word reconstruction

Delete u, obtaining a unique old R-word. Its legal u slots precede the first x or C−E label. For a lifted private prefix of length K, restoration of a,b has K+2 possibilities; a private label at rank r precedes b in K−r+1 of them. This counts complete original P+ words, not a uniform conditional-interface law.

The following independently reconstructed totals are `(S,N,K_ub)` per old word (averages only within freely permutable legal initial-root cells):

- K0: `(1,3,1)`. The first C label cannot be E, so only the initial u slot exists.
- K1 beginning x: `(2,4,2)`.
- K1 beginning y or z: two slots, each with S=3,N=4; the u contributions are 2 and 1. Total `(6,8,3)`. Again the first C label cannot be E.
- K2 containing x, x rank 1: `(4,5,3)`. Rank 2: `(10,10,5)`. The other private label and x may be exchanged without changing the legal suffix, giving the true average `(7,15/2,4)`.
- K2 beginning y,z: the three u slots before C contribute `(18,15,6)`. Each of the ell additional slots within the initial E run keeps u after the first C, hence adds `(3,4,0)`. Total `(18+3ell,15+4ell,6)`.
- K3, x rank r=1,2,3: r legal u slots, each has new private prefix length 4. S total is r(6+r), namely 7,16,27; N total is 6r, namely 6,12,18; K_ub totals are 4,7,9. Their averages are `(50/3,12,20/3)`.

The prefix permutations are bijections with the same entire suffix; no equal weights between different suffixes or different objects are asserted. These totals prove both displayed S,N formulas. They additionally give

    K_ub=(20/3)A3+6A2−2I+2X+3Y+A0.

For x itself, each of r insertion slots leaves i−r+1 favorable b slots, hence r(i−r+1); averaging within old prefix size i gives 1,2,10/3. Thus the independent subtraction check is exactly

    K_xb=(10/3)A3+2I+X.

All four private events sum to K(K+1)/2 in each lifted prefix, agreeing with S after subtracting this x event.

## 2. Candidate-wise caps and selection quantifier

The reconstructed K_ub table gives ratios respectively 1/3,1/2,3/8,8/15,6/(15+4ell),5/9. Thus K_ub/N≤5/9 without degrees or moments; the K2-containing-x bound is correctly applied to its symmetric rank cell, not incorrectly to its individual rank-1 word (whose ratio is 3/5).

For y,b, swap their positions in a complete word having y before b. The only predecessor of y is a, which remains earlier; all y successors lie in C and were after b. Moving b earlier and y later is legal. The involutive swap is an injection into b-before-y words. This proves K_yb/N≤1/2, and identically for z. The lift adds no successor of y outside C.

The three pairs are fixed physical pairs of the original P+. A lower bound on their mean guarantees some one of their whole-object probabilities is at least that mean. Each candidate separately has the necessary upper cap. No wordwise choice of different pairs is used.

## 3. TB1: all m from 0 to 7, no k/degree cap

Subtracting the reconstructed tables gives

    S−N=(14/3)A3+3A2−(7/2)I−L−2A1−2A0.

Set J=A2−I and s0=A3−A2−2A1−2A0. Both are nonnegative under the stated OLD moment. Every ell is between 0 and m, so L≤mJ, with its negative sign in S−N treated in the correct direction. Substitution yields precisely

    S−N ≥ (14/3)s0+(25/6)I+(23/3−m)J+(22/3)(A1+A0).

All coefficients are strictly positive for every integer m≤7. Since T is an ideal, a legal R-word can list all three T labels first; hence A3>0. Vanishing of all right-side coordinates would force A3=0. Strictness S>N is therefore genuine, including degenerate C/E cases, and not an unproved equality exclusion.

For the quantitative ratio, independently substituting A3=I+J+2X+2Y+2A0+s0 and L=mJ gives the stated coefficient arrays

    S: 71/3, (104+9m)/3, 106/3, 118/3, 103/3, 50/3;
    N: 39/2, 27+4m, 28, 32, 27, 12.

The J ratio is (104+9m)/(81+12m), derivative −519/(81+12m)^2, and its m=7 value is 167/165. Each of the other five ratios is larger. For rho=167/165, the coefficient of L in S−rho N is 3−4rho=−173/165<0. Thus evaluation at its upper envelope mJ is a valid lower bound, not an optimization with the wrong sign. It proves S/(3N)≥167/495>1/3. This argument imposes no k cap and does not require realizability of arbitrary abstract coordinate rays. The lower constant is not asserted sharp.

## 4. TB2 and the extra gate

A C-minimum of old T support 0 or 1 can be preceded by precisely its required T labels, giving an old K0 or K1 word. Conversely the first C label in either such word is a C-minimum with that support bound. Thus the stated equivalence with A0=A1=0 is exact, including empty C.

Independently using the literal deletion-of-T fibers gives

    A3=6e(C), A2=2 sum(h+t), I=2 sum t,
    L=sum l, l=2qh−q(q−1), t=h_y+h_z.

Here 0≤q≤h, and q>0 forces t=0. Hence in the no-K0/K1 branch the same-C-word kernels are exactly

    n=72+30h+15t+4l, s=100+36h+14t+3l.

The actual degree bounds are h≤k≤7 (x has three outside-C incomparable labels) and h_y,h_z≤6 (each has four, including u). Thus t≤12. The denominator kernel is positive. If q=0,

    253s−260n=6580+1308h−358t≥2284>0.

If q>0, l≤h(h+1), giving 6580+1027h−281h², a concave polynomial on [0,7] with values 6580 and 0 at its endpoints. This proves the claimed kernel ratio and its sum without OLD moment. Equality at h=q=7 is allowed, so TB2's bank-mean lower bound is closed, while still strictly above 1/3.

For general K0/K1 counts the exact difference is

    S−N=sum_beta[28+(6−2q)h−t+q(q−1)]−2(A1+A0).

For q=0 the summand is at least 16. For q>0 its difference upon increasing q is 2(q−h)≤0, so its minimum at fixed h occurs at q=h and equals 28+5h−h². On 0≤h≤7 this concave expression has minimum 14. Therefore the additional gate S−N≥14e(C)−2(A1+A0) is valid throughout actual D10. It is closed at A1+A0=7e(C), strict below, and is not claimed automatic.

## 5. Realizability and separation checks

For each m=0,...,7, let C be E (an m-chain of yz signature) disjoint from a two-chain of full signature. E is a genuine C ideal; k=m. Shuffling the two chains gives e(C)=binom(m+2,2), sum h=binom(m+2,3), and no K0/K1 words. Thus A2/A3=m/9 and the OLD moment holds. Actual degrees: x and u each m+3; y,z each 4; b has 5 (including a); E labels have 4 when present; full-chain labels have m; a has 1. Consequently Delta(P+)=max(m+3,5)≤10. The m=0 case is included and is nonempty, not inferred by a nonexistent E label.

For C=E a seven-chain, the unique C word has h=q=7,t=0,l=56. Thus A3=6,A2=14,I=A1=A0=0,L=56, and the independent formulas give N=506,S=520,K_ub=124. Symmetry gives K_yb=K_zb=198, so the probabilities are 62/253 and 99/253, respectively. Delta is 10. OLD moment fails; the mean is exactly 260/759. The new two-moment expression quoted in the manuscript is 144−168−784=−808. These are separation of tests and sharpness of this bank mean, not a best-pair optimum or a newly unguarded population.

The four previously independently checked MC1 marked-pair countercontrols all have only yz/full signatures, hence A0=A1=0, and satisfy OLD moment. Both bank theorems apply to them without altering their fixed u/b failure. The y,z twins already supply historical guards. MC1's specified-pair theorem remains distinct and stronger for that specified pair in its safe region.

## Verdict

All stated bank conclusions follow analytically under their exact contracts. TB1 indeed covers every OLD-moment actual-D10 exact lift because its actual u degree is m+3, forcing m≤7. TB2 covers the indicated signature class without OLD moment. This does not solve unrestricted B1/T4, transport a conditional witness, identify the OLD moment with a new-lift moment, or certify net-new coverage beyond prior root-prefix/twin/very-good mechanisms. The manuscript's analytic proof status is accurate; the unrelated computer-assisted MC1 classification is not a dependency of the two bank inequalities.
