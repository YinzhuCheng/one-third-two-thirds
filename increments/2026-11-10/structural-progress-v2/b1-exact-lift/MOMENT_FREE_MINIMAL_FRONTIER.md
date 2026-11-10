# MF1: moment-free minimal-frontier sufficient condition

Status: analytic author candidate, pending uninvolved review. No original-poset enumeration or CA proof dependency. Exact rational arithmetic below merely evaluates finite binomial identities.

## Contract and result
Use the exact original B1 lift contract and counts in PROOF_CANDIDATE.md, without OLD seed moment. Retain actual full Delta10, m<=k<=7. A full C-minimum means a C-minimal physical label with complete T-signature xyz.

MF1: The fixed original pair (u,b) has 1/3 < Pr(u<b) <= 5/9 whenever either:
1. C has at least three full C-minima; or
2. C has at least two full C-minima, and either k<=6 or m<=5.

There is no ordinary-population novelty claim: twins, chain-private guards or earlier weak count gates may already give some balanced pair. This result certifies the specified pair without requiring a seed moment; it is not the full B1 or NB theorem. Earlier SR2 full-min depth-two result assumes OLD moment; this hypothesis is deliberately absent here.

## General degree/frontier certificate
Select r distinct full C-minima. Suppose each selected label has original C-incomparability degree at most d. Put D=d-r+1 (necessarily nonnegative). For t>=0 define

 h=min(k,t), q=min(m,h),
 G_(m,k)(t)=48+(6-8q)h+4q(q-1).

For m>=1 this is nonincreasing in t. The general B certificate in this section is explicitly restricted to m>=1. If m=0, use instead the unconditional exact bound F>=48, hence 3K-N>=48e(C)+2X+Y>0; no value of B(r,d;0,k) is asserted as a lower bound. Define, for m>=1,

 B(r,d;m,k)=sum_(t=0)^D binom(D+r-t-1,r-1)/binom(D+r,r) G_(m,k)(t).

For m>=1 the ORIGINAL full event margin obeys

 3K-N >= B(r,d;m,k) e(C) +2X+Y.

Thus positive B suffices. Only selected original point degrees enter. No inherited degree or moment on a deleted object is claimed.

## Proof, with actual multiplicities
Delete the selected minima S and fix an actual linear extension gamma of C-S. Since S is an antichain of C-minima, each c in S has no retained predecessor. Its legal insertion deadline d_c is the number of gamma labels strictly before its first successor (or all of gamma if no successor). Every such preceding label is incomparable with c; the other r-1 deleted minima are also incomparable with c. Hence d_c<=d-(r-1)=D, by the ORIGINAL point degree.

If gamma is shorter than D, append formal ordered placeholders solely for this proof. Every actual d_c remains at most the original length, so all selected labels must occur before these placeholders. Deleting placeholders is a count-preserving bijection, not a modification of P or C.

Now condition also on the relative order pi of the r selected labels. Their placements are represented by strictly increasing positions 1<=s_1<...<s_r<=D+r, satisfying s_j-j<=d_(pi_j). Every such placement is exactly one original C word in this gamma/pi fiber. The suffix of gamma after its first D positions is untouched. There are no arbitrary tail weights: every word is represented once and only once.

The increasing r-tuples form a finite distributive lattice under componentwise minimum/maximum. Uniform measure is log-supermodular; the finite FKG inequality applies. The feasibility event s_j<=d_(pi_j)+j for every j is decreasing. Thus, conditioned on feasibility, s_1-1 is stochastically no larger than under the unconstrained uniform r-subset of {1,...,D+r}. (Apply FKG to the increasing event s_1-1>=t and to the negative of the decreasing feasibility indicator.) The feasible set is nonempty, since placing all selected minima first always works.

Let H be the number of gamma labels before the first selected full token. In every actual reconstructed word beta,

 h_x(beta)<=min(k,H), q(beta)<=min(m,h_x(beta)).

The exact kernel F=48+(6-8q)h_x+9(h_y+h_z)+4q(q-1) is at least G_(m,k)(H). Indeed increasing q up to min(m,h_x) only lowers F, deleting its nonnegative hy/hz term only lowers it, and the resulting function of h_x is nonincreasing for m>=1. Since G is nonincreasing, stochastic domination gives the conditional fiber-average lower bound B. The unrestricted first-hit law is

 Pr(H=t)=binom(D+r-t-1,r-1)/binom(D+r,r), 0<=t<=D.

The same B applies to every gamma/pi fiber. Multiply by EACH ACTUAL fiber size and sum, rather than giving distinct fibers equal weights. This proves sum_beta F(beta)>=B e(C). Finally use the inherited exact full-event identity 3K-N=sum F+2X+Y. No moment was used at any stage, including the final sum. The inherited universal upper bound is K/N<=5/9.

## Exact D10 specializations
Full-signature C labels have no incomparabilities outside C, so d=10 is available. Selecting only r=2 or r=3 is allowed even if more full minima exist.

For r=2,D=9: denominator binom(11,2)=55. At the hardest cells in the claimed domain,

 B(2,10;6,6)=42/11,
 B(2,10;5,7)=86/55.

Monotonicity in m and k yields all k<=6 or m<=5. For r=3,D=8:

 B(3,10;7,7)=3622/165>0,

which yields all feasible m,k<=7. These constants are margin-per-C-word bounds, not claimed sharp probability bounds.

The unclaimed r2 cells illustrate the limit of this certificate:
 B(2,10;6,7)=-42/55, B(2,10;7,7)=-18/11.
Negative B is NOT a realizable counterexample or a failure of the fixed pair.

## Scope/nonvacuity and deduction boundary
For any m<=k<=7, C consisting of Mx=E ordinal-sum a (k-m)-chain (all signature yz), in parallel with three full-signature isolated C labels, realizes the r3 hypothesis and actual Delta10 (full label degree k+2<=9; E degrees include their two private-root incomparabilities plus other E labels and three full labels, at most k+4 if E is antichain; choosing E a chain makes the degree safely <=6). It retains fair twins y,z and is only a realizability illustration, not new population credit.

The frontier proof extends to arbitrary d,r via the displayed binomial formula; no finite certificate table is used. Any claim of new ordinary balanced-pair coverage requires separate old-guard exclusion and is not made here. 

## An actual seed failing OLD moment (analytic check)
Take E a four-chain of yz-signature labels, three full-signature C labels c1,c2,c3, and an empty-signature two-chain v1<v2. These three components are pairwise parallel in C. Then m=4,k=6 and the actual lifted degrees are: a1, b5, x9, u7, y=z6, each E label7, each full c8, and each v10. Thus actual Delta10 holds. (The full c degree is 4+2+2=8, and each v has three missing T predecessors plus four E and three full labels.)

The old C count is e(C)=9!/(4!2!)=7560. Uniform component shuffling gives mean hx=6/(3+1)=3/2 and mean hy=mean hz=2/(7+1)=1/4. Therefore A3=45360 and A2=30240.

For A0,A1 remove the two v labels. The remaining ten-label R0 has e(C0)=7!/4!=210, A3(R0)=1260, A2(R0)=2*210*(4/4)=420, A1(R0)=A0(R0)=0, so e(R0)=1680. Every original R word is a unique shuffle of a fixed R0 word with the two-chain v. To have initial private run zero, v1 is first and there are 11 positions for v2, giving A0=18480. To have run exactly one, the first R0 root occurs first, then v1, with 10 positions for v2, giving A1=16800. Consequently

 A3-A2-2A1-2A0=-55440<0.

The pure scalar Phi(6,4)=-60 is also negative. MF1 nevertheless certifies the fixed (u,b). This is a genuine non-moment input, while y,z and the full labels remain old fair-twin guards; no new ordinary-population claim follows. A small 12-label ideal-DP calculation was used as a diagnostic for these four A counts; the displayed component-shuffle derivation is the proof and has no computational dependency.

## Review correction: m0 versus the general B formula

The original candidate's displayed general B lower bound did not explicitly exclude m0. Independent review found that stronger reading false: E empty, C a three-antichain containing one yz label and two full labels has k1,r2,d10, actual Delta<=5, but mean F=50 whereas the syntactic formula B(2,10;0,1)=582/11. No poset conclusion fails. The revised theorem explicitly uses F>=48 for m0 and reserves the stochastic-decreasing B certificate for m>=1. This is a real corrected quantifier, not a claimed harmless proof shortcut.
