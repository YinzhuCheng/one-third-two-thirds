# Source Q8: nine internal tail words pay individually

2026-11-10. New analytic reduction, independent review pending. It does not yet pay the three remaining words or change any source-row ledger. This route is separate from the cap-order chamber argument and its finite Bernstein certificate.

Use the already analytically compressed source roots B=0,U=min h. Fix one of the twelve internal words w of H=(t1<z)+{t2,t3}. Let f be its flagged-gap placement count, s its constant physical score 2[t2<t1]+2[t3<t2]+[z<t3], k0 the number of its marks in gap zero, and L its minimum occupied gap. Caps may be suffix-minimized; let m be their minimum. All four caps are integers between zero and six. All expectations below are uniform over this ONE word's legal gap placements, an auxiliary counting device, not a replacement for original completion weights.

## Exact wordwise margin

Adding an independent deadline-zero v offers k0+1 positions in each placement, so its count is g=f E(k0+1). Similarly the sum of the translated counts is f E L. The fixed word's contribution to the source reduced signed count is exactly

    f E[ -13+24s + (-24+9s)k0 + (-42+9s)L ].       (W1)

Indeed this expands (11+15s)f+(-24+9s)g+(-42+9s)sum_j f_j. This keeps the real z-insertion law: z is one of the four stars, not part of a conditioned exterior word.

## Uniform initial-run bound

For n ordered stars whose individual caps are all at least the integer m, with arbitrary further upper flags,

    E k0 <= n/(m+1).                               (W2)

Condition on the suffix beginning with bar m+1, including which n' initial stars occur before that bar. If needed append a final bar after all allowed gaps; this has no effect on the placement count. Before that bar there are precisely m bars and n' ordered stars. Every interleaving of those colors is legal: their gaps are <=m, whereas each star's upper flag is >=m. The suffix and the internal orders stay fixed. Thus this conditional prefix is the unrestricted shuffle of n' stars and m bars. Its stars are uniformly distributed over the m+1 weak-composition gaps, so its expected first run is n'/(m+1)<=n/(m+1). Averaging gives (W2). This argument does not assume that distinct original exterior words have equal weights.

The previously audited FD translation bound, with n=4,M=6, also gives

    E L <= 6/5;
    m=1: E L <= 6/10=3/5;
    m=2: E L <= 6/10+(6*5)/(10*9)=14/15.           (W3)

For m=0, L=0 exactly. The truncated inequalities use f_j=0 for j>m.

## Positive words

If s=2, (W1)/f=35-6 E k0-24 E L. Apply (W2)-(W3):

    m=0: margin/f >=11;
    m=1: margin/f >=43/5;
    m=2: margin/f >=23/5;
    m>=3: margin/f >=35-6-24*(6/5)=1/5.

Thus EVERY score-two internal word pays strictly, with a uniform bound f/5. No cap-order cases or rational coefficient table are involved.

If s=3, its margin/f=59+3 E k0-15 E L>=41. If s=4, its margin/f=83+12 E k0-6 E L>=379/5. These also pay individually.

Of the twelve internal words, the only words not paid by this argument are

    (t1,t2,t3,z), score zero;
    (t1,t2,z,t3), score one;
    (t1,z,t2,t3), score one.

There are six score-two, two score-three, and one score-four words. The whole source-bank proof would follow from a suitable count-preserving charge of the three remaining word contributions to the positive nine. Such a charge is NOT supplied here. The 400 pure analytic + two finite-symbolic classification is unchanged.
