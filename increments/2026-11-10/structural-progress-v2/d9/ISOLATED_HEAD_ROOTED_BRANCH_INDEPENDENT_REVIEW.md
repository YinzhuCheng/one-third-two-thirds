# Independent review: isolated head plus an arbitrary rooted branch

2026-11-10. PASS for ISOLATED_HEAD_ROOTED_BRANCH_GATE.md, with its exact original ideal/exterior and selected-label degree contract. This is a branch-uniform analytic theorem; its current packet mapping adds only one row.

## Root and weight audit

Since q is incomparable with all |B| branch labels and v, its internal incomparable degree is |H|>=3, giving q's exterior cap d<=6. Every branch label is incomparable with q,v, giving cap<=7. These bounds use full original degrees of the selected tail labels. The proof need not impose an extra degree condition on b,u or v. Full root relations imply h_a=h_v=0 and h_b,h_u<=min_H h.

In RC notation (lambda,mu,rho)=(21,6,10), n=|H|>=3, M=7, s=1. The two C1 quantities are 17 and 28, C2 has slack one, and C3 is 17j+24-4(7-j)/(n+1)>=18j+17>0 for 1<=j<=7. Therefore B=0,U=min_H h is indeed worst. The exact reduced signed count is 16F-9G+15W+9W_G+sum(9W_j-12F_j).

The remaining uniform branch-word/placement expectations are only notation for summing RAW margins. They are not asserted to be the induced law after deleting q,v,b,u from an original extension. This distinction is essential and is correctly retained in the proof.

## Independently reconstructed branch accounting

For a fixed branch word and legal branch gap vector, p is its first letter and has its minimum gap x. Put e=min(d,x), L=#branch gaps <=d, Z=#branch gaps zero. There are F=d+1+L placements of q and exactly T=F-W=e+1 with q before p. Adding the independent gap-zero v gives T_G=T+1+Z: the q-before-p placement at gap zero contributes Z+2 v slots, and the other e such q placements contribute one slot apiece.

For every j<=e, translated placements have F_j=F-j and T_j=e-j+1; for larger j the contribution vanishes. Hence sum F_j=eF-e(e+1)/2 and sum T_j=e(e+1)/2. Substitution gives exactly

    (31-3e)(d+1+L)-3e^2-27e-33-9Z.

This was independently derived before consulting the author's combined expression. Equivalently, for x=0 it is 31(d+L)-9Z-2; for 1<=x<=d it is (31-3x)(d+L)-3x^2-30x-2; and for x>d it is d-6d^2-2. These forms yield the displayed f_d using L>=Z>=1 or L>=1 in the applicable branches. The positivity of 31-3x used when discarding L-1 follows from x<=d<=6.

## Stochastic order and positivity

For each fixed internal branch word, FD1 controls the survival probabilities of its first gap. With n=|B|>=2 and max cap seven, those survival probabilities are at most the two-star cap-seven survival probabilities. Thus X is stochastically NO LATER than Y. The f_d sequence is nonincreasing, including the d=0 boundary and the constant plateau for x>d, so the expectation inequality has the correct direction: E f_d(X)>=E f_d(Y).

The two-star masses are exactly (8-x)/36 for x=0,...,7. Symbolic summation independently reproduces the numerator -5d^4+96d^3-387d^2+1512d+416 over 144. Its decomposition 5d^3(6-d)+d(66d^2-387d+1512)+416 is exact; the quadratic discriminant is -249399. Therefore the lower bound is strictly positive throughout the continuous d interval [0,6]. No deadline table or small-integer case enumeration is used for positivity.

Each branch word has a positive number of legal branch placements, so multiplication by their actual count and summation preserves strictness. Summation over actual original exterior words then yields the stated original-P bank. The fixed events are u<b,v<u,p<q throughout. The opposite p/q orientation is not covered.

## Corroboration and census

ISOLATED_HEAD_ROOTED_BRANCH_INDEPENDENT_CHECK.py/.json verifies the raw-margin identity, stochastic-bound expectation identity, and positive decomposition. Independently, twelve actual D9-class original posets (chain, fork, and diamond branches with varied q caps) are counted by full-poset event DP and by the separate branch-gap raw-margin formula; all exact margins agree and are positive. These are corroboration, not proof dependencies.

ISOLATED_HEAD_ROOTED_BRANCH_INDEPENDENT_CENSUS.py/.json reconstructs the full packet and the exact exhausted/saturated-v applicability contract. It finds one applicable row, no overlap with the prospective audited 606-row union, and one net addition, hence prospective 607. It is the source ideal (0,0,1,1,7,7,23), reference (0,1,2,3,5,4,6). Here p=4,q=5 and the charge p<q reverses that stored reference. The theorem remains uniform for arbitrary rooted branches even though this source tree contributes only its smallest nontrivial branch. No broad source-count claim follows from the theorem's parameter range.
