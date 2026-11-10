# Q8 first-head source bank: complete explicit integer-analytic proof

2026-11-10. Author assembly; full independent composition review PASS in Q8_COMPLETE_ANALYTIC_INDEPENDENT_REVIEW.md, with separate concrete algebra audit in Q8_ANALYTIC_BOUNDARIES_INDEPENDENT_REVIEW.md. This note assembles the explicit analytic boundary arguments. The old1512-coefficient Bernstein proof remains valid historical corroboration, but is NOT an input to the positivity argument below. This proof has finite structural chamber and integer-threshold splits; it is not case-free and makes no novelty or whole-D9 closure claim.

## AC1. Fixed original-P statement

Let Q be an ORIGINAL ideal on a,b,u,v,t1,t2,t3,z with predecessor masks(0,0,1,1,7,7,7,23). Thus a<u,v, each ti is above a,b,u, t1<z, and there are no other marked relations. Every original exterior label lies above v. Each of the four tail labels has full incomparable degree<=9. For the fixed PHYSICAL events

    A={u<b}, B={v<u}, C={t2<t1}, D={t3<t2}, E={z<t3},

one has in the uniform extensions of the SAME original P

    15 Pr(A)+3 Pr(B)+2 Pr(C)+2 Pr(D)+Pr(E)>23/3.      (AC)

This pays the original source bank for the two first-head references01234567 and01234657 (fix the names of the two unsupported leaves according to the reference before conditioning). Only these two source occurrences are covered by this assembly. They were already counted as two finite-symbolic replacements; promotion to an analytic proof, if independently confirmed, is not two further rows on top of them.

## AC2. Original exterior-word law and analytic root compression

Fix one actual literal word on P minus Q. Keep z MARKED throughout this calculation; do not condition on an exterior word that already contains z. Ideality gives pure upper-gap constraints. Exhausted-v memory gives h_a=h_v=0. The tail gaps h=(h_t1,h_t2,h_t3,h_z) are integers with h_t1<=h_z and upper bounds(6,5,5,6). We prove the larger domain all four<=6. Root deadlines B0=h_b,U=h_u are at most every tail gap.

Use FLAG_TRANSLATION_ROOT_COMPRESSION.md with n4,M6,alpha15,beta3,tau5 and tail score

    s(w)=2[ t2 before t1 ]+2[ t3 before t2 ]+[ z before t3 ].

All three reversed edges cannot hold simultaneously because t1<z, so s<=4. The cone parameters are(lambda,mu,rho)=(45,9,23); its positive B increment lower bound is C(k)=(169k+111)/5, while rho-mu-3s=2>0. Consequently the exact full count margin is minimized at B0=0,U=m=min h. This is an analytic translated-tail count argument, not a root-cap table.

Let F_j,W_j count the tail H=(t1<z) disjoint from t2,t3 with all upper gaps shifted down by j, and with the fixed score s. Let G,W_G insert the independent deadline-zero v beside H in the gap-zero root model. The original margin at these worst roots is exactly

    M=3(15K_A+3K_B+2K_C+2K_D+K_E)-23N
      =11F_0-24G+15W_0+9W_G
                    +sum_(j=1..m)(9W_j-42F_j).       (AC2)

It remains to prove M>0 for integer tail flags<=6. All events remain physical and fixed. Different formulas below count the same events; they do not choose a bank after a profile is seen.

## AC3. Structural order chambers and the largest-gap reduction

Temporarily sort the four tail caps, retaining their physical names. Write their sorted values as

    t, t+p, t+p+q, t+p+q+r,
    t,p,q,r integers>=0, t+p+q+r<=6.

There are twelve possible orders sigma with t1 preceding z. Weak ties can always be broken that way. Let P_sigma(t,p,q,r) denote AC2 computed in that chamber.

These polynomials can be reconstructed exactly from the flagged-chain determinant (or the equivalent flagged-chain recurrence) for the12 internal words of H; G inserts the independent v in five positions per word. This is a counting identity, not the old positivity certificate. The complete polynomials and their verification scripts are retained, but their Bernstein coefficients are not used below.

Every P_sigma is affine in the largest gap r. One way to see this is that, for any fixed internal word, the largest tail cap is either removed by a suffix-minimum constraint or is the cap of only the last free coordinate; its count is affine in that largest cap. The extra cap-zero v and the j-sum preserve affinity because their summation endpoint is the MINIMUM t, independent of r. This also follows by direct symbolic expansion of AC2.

Thus, setting L=6-t-p-q, its minimum over0<=r<=L is at r=0 or r=L. If L0, these coincide. Both substitutions keep t,p,q integral and stay in the same closed chamber. It suffices to prove the equal-maximum face and the budget-saturated face.

## AC4. Equal-maximum face, independently closed

Q8_EQUAL_MAX_FACE_ANALYTIC.md proves

    P_sigma(t,p,q,0)>0

for every admissible integer t,p,q. On this face the twelve orders reduce to seven because the two largest caps tie. Each polynomial is quadratic in q. Its q minimum is reduced to q0 or q=6-t-p by explicit coefficient signs, using integer t and, in one low-t case, integer p.

The q0 endpoints are three cubic families in p. Their positivity follows from derivative shape, positive coefficients, and the explicitly bounded t5/t6 branches. The opposite endpoints are handled by concavity, positive endpoint derivatives, or elementary univariate bounds. The sole convex p case uses one fully displayed nine-term positive identity for a univariate negative discriminant. No list of unseen sign checks is invoked. In particular, this proof does NOT refer back to the budget-saturated face and creates no circular dependency.

## AC5. Budget-saturated face

Set

    S_sigma(t,p,q)=P_sigma(t,p,q,6-t-p-q),
    0<=q<=6-t-p.

The explicit coefficient identities and inequalities in Q8_SATURATED_FACE_REDUCTION.md give the following classification. Indices refer to its fixed twelve-order list, not to sampled profiles.

- Nine chambers have nonpositive q quadratic coefficient, including the linear cases. Their minimum is at q0 or q=6-t-p.
- Chamber4 has positive q linear coefficient and nonnegative quadratic coefficient, so it is increasing and its minimum is at q0.
- Chambers0 and6 are convex in q. If t>=4, their right-end q derivative is nonpositive, hence they decrease throughout the allowed q interval and the minimum is at q=6-t-p.
- In the remaining integer t range0,...,4, the negative discriminants H0,H6=4AC-B² are strictly positive by the explicit low-degree inequalities of Q8_INTEGER_DISCRIMINANT_REVIEW.md and the integer appendix of Q8_SATURATED_FACE_REDUCTION.md. All ten fixed-t polynomial arguments are displayed. This replaces the earlier81-coefficient test and is asserted only for integral t. Since the leading q coefficients are positive, the whole q quadratic is then positive.

The right endpoint q=6-t-p has r0 and was proved in AC4. The left endpoint q0 is a DIFFERENT face and is proved by Q8_MIDDLE_TIE_BOUNDARY.md: seven exact cubics in p have endpoints controlled by explicit univariate factors or the already proved r0 face; derivative shape and eleven fully displayed integer-threshold bounds prove positivity between them. There is no invocation of the saturated-face interior or of Bernstein signs in that boundary lemma.

This proves every S_sigma>0. Together with AC4 and affine r interpolation, it proves every P_sigma>0 on the ORIGINAL integer tail domain.

## AC6. Actual completion weights and proof status

For each actual original exterior word, root compression followed by AC3-AC5 proves strictly positive original count margin. Sum those inequalities over the same original exterior words, retaining their true interleaving counts N_omega. This proves AC. No uniform cap/profile/exterior-word mixture is introduced, and NB is never assumed on a helper or conditioned law.

The real finer-fibre margin-88 in Q8_PROJECTED_WORD_CONTROL.md is compatible: it fixes z's exterior position and breaks precisely the marked-tail count model used here. The original-P source bank there still pays at margin+674. Likewise the actual uniform-cap7 Delta11 control remains a valid stopping line; its root compression works but its tail margin is negative. Neither is NB or a counterexample to the proved cap-six gate.

Dependency DAG:

    original ideal + fixed O word
       -> FD/RC analytic root compression -> AC2
       -> twelve structural deadline orders -> affine r endpoints
            -> r0 lemma (self-contained)
            -> saturated q shape
                 -> r0 right endpoint
                 -> middle-tie q0 lemma -> r0 right endpoint only
                 -> explicit integer H0/H6 inequalities.

There is no remaining1512- or81-coefficient positivity dependency in this assembled argument. Those files and the1372 diagnostic actual-P checks are corroboration/history, not proof inputs. Independent full composition review has now passed, including boundary coverage, acyclicity and integer/continuous distinctions. These two historical symbolic rows are reclassified as analytic, not counted twice. The live total, including any later separately reviewed additions, is maintained in PROOF_STYLE_LEDGER.json.
