# An isolated common head beside an arbitrary rooted branch

2026-11-10. Internal independent theorem and source-mapping review PASS in ISOLATED_HEAD_ROOTED_BRANCH_INDEPENDENT_REVIEW.md. The structural theorem is uniform in the branch, but its current source census has ONLY ONE new row. Its one net row is included in the live607 ledger.

## Original-P contract

Let an actual original ideal be Q={a,b,u,v} union H. Its root relations are a<u,v, b incomparable with a,u,v. Every H point is above b,u and incomparable with v. Inside H, one point q is isolated, and the other points form an arbitrary poset B with unique minimum p. Assume |B|>=2. Every original exterior point is above v. Assume the full original incomparability degree of q and of every B point is at most nine. The q degree hypothesis itself implies |B|<=8; arbitrary means no further restriction on branch shape, not an unbounded-size claim.

Then the same original uniform extension law satisfies

    7 Pr(u<b)+2 Pr(v<u)+Pr(p<q)>10/3.                 (IB)

Thus the bank excludes a strict two-thirds reference with b<u<v and q<p. The direction p<q is fixed physically and is important; the opposite direction is not covered.

Fix one literal ORIGINAL exterior word. The marked ideal condition leaves only upper gap caps. Write d for q's cap. Each branch point is incomparable with both q and v, hence has cap<=7. The old marked incomparable degree of q is |H|>=3, hence d<=6. These are the only degree consequences used below. The root caps satisfy h_a=h_v=0 and h_b,h_u<=min_H h.

## Root reduction

Apply FD/RC from FLAG_TRANSLATION_ROOT_COMPRESSION.md with tail size k=|H|>=3, max cap 7, score X=1[p<q], and

    (lambda,mu,rho)=(21,6,10),   0<=W_j<=F_j.

Its root-increment coefficient is

    17j+24-4(7-j)/(k+1)>0,   1<=j<=7,

and rho-mu-3=1>0. Thus the worst root caps are h_b=0 and h_u=min_H h. The exact three-times-bank margin there is

    M=16F_0-9G+15W_0+9W_G
                          +sum_j(9W_j-12F_j).         (1)

F_j counts tail placements with all gaps at least j; W_j counts those with p<q. G,W_G include an extra independent deadline-zero v. The sum ends at min_H h. This step is analytic and does not enumerate root profiles.

## Exact branch-gap accounting

Fix an internal branch word sigma and one legal weak gap vector for that word. Write

    x=gap(p), e=min(d,x),
    L=number of branch letters with gap<=d,
    Z=number of branch letters with gap=0.

Since p is the unique branch minimum, x is the least branch gap. Summing all placements of q beside this fixed branch vector gives

    F=d+1+L,           T=F-W=e+1.

Indeed q has one base slot in each exterior gap 0,...,d and one extra slot per branch letter in those gaps. It precedes p in precisely one slot in each gap 0,...,e.

The analogous q<p count after adding deadline-zero v is

    T_G=G-W_G=T+1+Z.

For the q-gap-zero placement before p there are Z+2 possible v positions. Each of the other e placements of q before p gives exactly one v position. This counts the actual v insertion multiplicities.

For a translation j<=e, the same branch vector contributes F_j=d-j+1+L and T_j=e-j+1. It contributes zero at larger j. Therefore

    sum F_j=eF-e(e+1)/2,
    sum T_j=e(e+1)/2.

Substitute W=F-T and W_G=G-T_G into (1). Its exact contribution from the fixed branch vector becomes

    m=(31-3e)(d+1+L)-3e²-27e-33-9Z.                  (2)

This summation is over genuine placements in the ORIGINAL exterior word; no projected word with a branch point moved into the exterior is substituted.

## A one-variable lower envelope and stochastic domination

Equation (2) is bounded below by f_d(x), where

    f_d(0)=31d+20;
    f_d(x)=31d+29-3xd-33x-3x²,   1<=x<=d;
    f_d(x)=d-6d²-2,              x>d.

For x=0, L>=Z>=1, so 31L-9Z>=22. For 1<=x<=d, Z=0 and L>=1. For x>d, L=Z=0 and the displayed value is exact.

For integer 0<=d<=6 this function decreases with x on {0,...,7}. The first drop is -3d-27, subsequent drops within 1,...,d are -3d-36-6x, and the final drop at d to d+1 is 3d-31; all are negative. The d=0 case is simply 20 followed by -2.

For the fixed branch word sigma, let X be its first gap under the uniform legal branch-gap placements. FD1 with all caps<=7 and branch size n=|B|>=2 gives

    Pr(X>=j)<=product_(i=0..j-1) (7-i)/(7-i+n)
              <=product_(i=0..j-1) (7-i)/(9-i).

The final expression is the survival function of the first gap Y of two ordered letters with unrestricted caps seven. Its masses are

    Pr(Y=x)=(8-x)/36,  x=0,...,7.

Thus X is stochastically no later than Y. Since f_d decreases,

    E m >= E f_d(X) >= E f_d(Y)
      =[-5d⁴+96d³-387d²+1512d+416]/144 >0.             (3)

The final strict sign is explicit, not a table:

    -5d⁴+96d³-387d²+1512d+416
       =5d³(6-d)+d(66d²-387d+1512)+416.

The quadratic has discriminant -249399 and positive leading coefficient. Therefore (3) is positive throughout 0<=d<=6.

Multiply by the actual number of branch-gap placements for sigma, sum over all internal branch words, then sum the original exterior-word counts. This proves (IB) with the original true weights. Neither uniform weighting of exterior words nor NB on a conditional law is assumed.

## Source scope and stopping lines

The existing source packet has one currently unproved row with this structure AND q<p reference: Q=(0,0,1,1,7,7,23), reference (0,1,2,3,5,4,6), events u<b,v<u,p<q with weights 7,2,1. Other larger branch structures surviving in that packet take the opposite head reference, so this theorem must not be marketed as a large source-row count.

The earlier three-chamber calculation TWO_HEAD_CHAIN_THIRD_REFERENCE_IDENTITIES.py/.json is now optional corroboration for the smallest branch, not a proof dependency. Likewise the natural-ref third-event mixture obstruction is compatible with (IB): it uses q<p as the reverse event, whereas this theorem charges p<q.

The projected Q6 fibre with p cap7, q cap3, root caps h_b0,h_u3 has margin -27 for this same weighted bank. Thus the proof must retain the branch's actual insertion correlations, as (2) does; it cannot claim payment separately after arbitrarily moving z or other branch points into the exterior.
