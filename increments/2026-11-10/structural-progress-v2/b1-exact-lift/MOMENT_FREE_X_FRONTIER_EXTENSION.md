# MF2: physical x-frontier, without seed moment

Date: 2026-11-10 UTC. Analytic author candidate; independent review requested. Exact original B1 lift contract throughout; actual full Delta10, 0<=m<=k<=7. No OLD moment, deleted-object moment or uniform interface law is assumed.

## Statement
A physical x-frontier point is a C-minimum c with x<c in the original order. Its complete old T-signature need not be full. The original fixed pair (u,b) satisfies

    1/3 < Pr(u<b) <= 5/9

if any of the following holds:

1. Some physical x-frontier point has original C-incomparability degree <=6.
2. There are two physical x-frontier points, each with original C-incomparability degree <=9.
3. There are three physical x-frontier points (no further degree hypothesis beyond actual full Delta10).

In particular two non-full-signature x-frontier points meet condition2 automatically. The statement pays the specified original physical pair, not an independently selected pair per fiber. It is neither full B1 nor a net-new ordinary-population claim.

## Proof and general certificate
Use the reviewed MF1 degree/frontier certificate in MOMENT_FREE_MINIMAL_FRONTIER.md, but select r C-minima lying above x instead of requiring full xyz signatures. Every proof step remains valid:

- The selected points are mutually incomparable C-minima. Fix a genuine gamma in LE(C-S) and their genuine relative order pi. Selected point c has no retained predecessor. Its insertion deadline is the number of gamma letters before its first successor. All those letters and the r-1 other selected points are incomparable with c. Hence the deadline is <=d-r+1 when each selected original C-degree is <=d.
- Legal insertion-position tuples form a nonempty decreasing event in the uniform distributive lattice of r-subsets. FKG gives a first-selected-gap H stochastically no larger than the unrestricted negative-hypergeometric law with D=d-r+1.
- A selected label lies above x, so its appearance stops the initial x-missing run: h_x<=min(k,H). Its other signature entries are irrelevant. The exact original kernel remains F=48+(6-8q)h_x+9(h_y+h_z)+4q(q-1). Delete the nonnegative 9-term and maximize q<=min(m,h_x). For m>=1 the resulting decreasing function is G_(m,k)(H) from MF1.
- Therefore the same exact B(r,d;m,k) bound holds in every actual gamma/pi fiber. Multiply by each actual fiber size before summing. This retains the original law; it never equally weights different gamma or pi fibers. The full margin is 3K-N=sum_beta F+2X+Y. The case m0 uses F>=48 separately, not the syntactic B formula at m0.

For m>=1, B is nonincreasing in m,k, so it suffices to evaluate the hardest m=k7. The exact finite binomial identities give

    B(1,6;7,7)=2,
    B(2,9;7,7)=298/45,
    B(3,10;7,7)=3622/165.

All are strictly positive. For example r1 is the uniform average of 48+2h-4h^2 for h0,...,6, equal2. The other identities follow from the displayed MF1 negative-hypergeometric binomial sum; these are exact arithmetic evaluations, not original-poset enumeration or a computer-assisted proof dependency. The accepted original u/b upper bound supplies5/9.

If c is x-frontier, then c is outside E, hence u<x<c; a,b are also below c. Its outside-C incomparable labels are exactly the old T roots missing from its complete signature. Thus actual full Delta10 gives

    deg_C(c)<=10-(3-|signature(c)|).

A non-full x-frontier has at least one missing root and hence deg_C<=9. This proves the stated automatic case.

## Scope and nonvacuity
For any m<=k<=7, take Mx to be a k-chain of yz signature with E its initial m-chain, in parallel with r selected C-minimal full-signature labels. For r1,k<=6 its selected degree is k<=6; for r2 any k<=7 each selected degree is k+1<=8; for r3 it is k+2<=9. All actual lifted degrees are <=10 (x k+3, u m+3, b5; yz-root degrees4; missing-chain point degrees <=r+2). These are actual nonempty contracts, though they have old twins and are not population-novelty witnesses. The r1 condition does not claim nonvacuity at k7: a C-minimum above x is incomparable with all k x-missing labels and thus has C-degree at least k.

To realize the automatic two nonfull case, take m=k0 and C two incomparable x-only signature labels. Then each selected point has C-degree1 and full degree3; x,u have degree3, b has degree5, and y,z each have degree6. The exact lift is legal with full Delta6. This is only realizability; y,z are old twins.

No ordinary-population novelty or full B1 conclusion follows from these illustrations. The remaining x-frontier patterns (for example one frontier point of high original C-degree) are not closed by MF2. 
