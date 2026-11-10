# Flag translation/depletion and a common-tail root-compression cone

2026-11-10. Author analytic extraction; independent review PASS in Q8_SYMBOLIC_INDEPENDENT_REVIEW.md. This reuses the ideal-color marked exchange already used for rooted-ideal starts and supported-tail rank bounds. No originality claim, new phase coverage, or automatic payment is asserted.

## FD1. A uniform translated-tail count inequality

Fix a poset H on n>=1 marked labels and a literal exterior chain word. Let its order-monotone nonnegative integer upper gaps be h_x<=M. Let F_j count placements of H in which every marked gap is at least j, with its given full induced order and upper gaps. Take F_j=0 once no such placement is possible. Then, for0<=j<=M,

    F_(j+1) <= (M-j)/(M-j+n) F_j,                     (FD1)

and

    sum_(r=j+1..M) F_r <= (M-j)/(n+1) F_j.           (FD2)

These are exact count inequalities, not a probability law imposed on deadline vectors.

Proof. Fix one internal H word and subtract j from all its gaps. Encode placements by n stars and M-j bars, preserving the fixed star order. Individual upper flags restrict the allowed strings; surplus final bars beyond every flag are harmless. A string starting with a bar is exactly a placement counted by the next translation F_(j+1). Mark any of its n stars, exchange its color with the first bar, and restore the fixed star and bar names. Every named star moves weakly earlier, so all upper caps remain legal. The result starts with a star. Given the output and the bar position now marked, the inverse is unique. There are at most M-j marked-bar choices per star-first word. Thus

    n*N_bar-first <= (M-j)*N_star-first.

Sum over internal H words and rearrange, proving FD1. Iteration gives

    F_(j+t)/F_j <= (M-j)_t/(M-j+n)_t,

with falling factorials. The hockey-stick identity

    sum_(t=0..M-j) (M-j)_t/(M-j+n)_t
      =(M-j+n+1)/(n+1)

proves FD2 after removing t=0. If F_j=0 the statement is immediate. The cap constraints are preserved by moving marks earlier; no NB inheritance or independence assumption is present.

## RC1. Exact common-tail root model

Let an original marked ideal consist of a,b,u,v and H. The four special labels have exactly a<u,v; b is incomparable with a,u,v. Every H label lies above b,u and is incomparable with v. H otherwise has arbitrary induced order. Fix one actual original exterior word, entirely above v. Thus h_a=h_v=0 and root upper gaps B=h_b,U=h_u satisfy B,U<=m=min_(x in H)h_x<=M.

Let A={u before b}, D={v before u}. Let X be a fixed nonnegative weighted sum of comparison indicators with endpoints in H, total coefficient tau. Let its coefficient-sum-normalized bank be

    alpha Pr(A)+beta Pr(D)+E X >= (alpha+beta+tau)/3.

Weights and events are fixed before sampling the exterior word. Put

    lambda=3alpha, mu=3beta, rho=alpha+beta+tau.

For each translation j, let W_j be the exact weighted X count, or a justified nonnegative lower bound independent of B,U. Write F_j for its tail count. Similarly G,W_G denote the tail model with one extra independent deadline-zero base letter v. Suppose0<=W_j<=s F_j for j>=1. This can follow from a deterministic score cap or from an audited lower-envelope construction.

The lower bound for the signed full count is

    M(B,U)=(2lambda+4mu-5rho)F_0+(lambda-3rho)G
                 +15W_0+9W_G
       +sum_(j=1..max(B,U))[(lambda*a_j+mu*d_j-rho*c_j)F_j
                                                       +3c_j W_j],

where

    c_j=(3+min(B,j))*1[j<=U]+(2+min(U,j))*1[j<=B],
    a_j=(2+min(U,j))*1[j<=B],
    d_j=c_j-1[j<=B].

This is the same exact root-gap decomposition already audited for THREE_TAIL. Its gap-zero multiplicities are(N,A,D)=(5,2,4)F_0+(3,1,0)G. The tail payoff multiplicities are5W_0+3W_G. No tail shape enumeration is used.

## RC2. A numerical cone forcing B=0,U=m as worst roots

Suppose

    lambda+mu-rho>=0,  2lambda+mu-2rho>=0,            (C1)
    rho>=mu+3s,                                      (C2)

and, for every integer1<=k<=M,

    C(k)=(lambda+mu-rho)k+2lambda+2mu-3rho
          -(rho-mu)_+*(M-k)/(n+1) >=0.              (C3)

Since C(k) is affine, checking its two endpoint values suffices; a nonnegative slope and C(1)>=0 are another sufficient form. Then

    M(B,U)>=M(0,m).                                  (RC)

This is root-deadline reduction only. It is NOT a payment theorem until M(0,m) is proved nonnegative on the remaining tail flags.

Proof. Increase B from k-1 to k. For k<=U, direct cancellation in RC1 gives the increment

    [(lambda+mu-rho)k+2lambda+2mu-3rho] F_k
      +3(k+3)W_k
      +sum_(j=k+1..U)[(mu-rho)F_j+3W_j].

Using W>=0 and FD2 bounds it below by C(k)F_k. For k>U the newly added term is

    [(lambda+mu-rho)U+2lambda+mu-2rho]F_k
                                             +3(U+2)W_k>=0

by C1. Thus B=0 is worst. At B=0 every increase of U adds

    3[(mu-rho)F_j+3W_j] <=3(mu-rho+3s)F_j<=0.

Thus U=m is worst. Strict numerical inequalities give the corresponding strict monotonicity when F_j>0; nonstrict RC is sufficient for proof reduction.

## RC3. Two applications and de-duplication

### New simpler Q8 five-event template

For H=(t1<z) disjoint from t2,t3 and tail score

    X=1[t2<t1]+1[t3<t2]+1[z<t3],

one has n4, M6, tau3 and deterministic score cap s2: all three reverse edges would contradict t1<z. With(alpha,beta)=(6,1),

    (lambda,mu,rho)=(18,3,10),
    C(k)=(62k+18)/5>0,
    rho-mu-3s=1>0.

Hence both root axes are FULLY analytically compressed, without the previously proposed but unproved half-count bound W>=F/2. The remaining statement is

    -2F_0-12G+15W_0+9W_G
                      +3sum_(j=1..m)(3W_j-7F_j)>=0.

It is still unproved here. This updates Q8_SIX_BANK_ROOT_REDUCTION_CANDIDATE.md: root reduction is no longer conditional, but payment remains open. No ledger count is added.

### Original source Q8 weights

For the source tail score2[t2<t1]+2[t3<t2]+[z<t3], tau5 and score cap s4, since all three reverse edges cannot occur simultaneously. With(alpha,beta)=(15,3),

    (lambda,mu,rho)=(45,9,23),
    C(k)=(169k+111)/5>0,
    rho-mu-3s=2>0.

Thus root reduction holds even in the enlarged all-tail-caps<=6 domain, without the source's tighter individual caps5 on t2,t3. The remaining count polynomial is the original source one in Q8_PROJECTED_WORD_CONTROL.md. It is now covered by the separately audited finite symbolic certificate Q8_SOURCE_BERNSTEIN_CERTIFICATE.md; FD/RC alone does not close it.

For comparison the previously proved three-leaf6/1/1/1 gate can use n3,M6,tau2,s1 for its sorted-leaf lower envelope, giving C(k)=(27k+12)/2>0. This is an alternative proof of its root monotonicity, not another bank family or a new count.
