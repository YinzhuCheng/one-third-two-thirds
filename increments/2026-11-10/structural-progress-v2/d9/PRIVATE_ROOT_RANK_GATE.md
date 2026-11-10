# DH-R: a private root with at most two outside-tail points

2026-11-10. Unified extension of DOMINATED_TWO_HEAD_GATE.md. Internal independent theorem and mapping review PASS in PRIVATE_ROOT_RANK_INDEPENDENT_REVIEW.md. Forty-nine net source rows are included in the current483 ledger.

## Contract and conclusion

Keep the exact original-P ideal/exterior contract of FG1: Q={a,b,u,v} union H, a<u,v, b incomparable with a,u,v, every H point above u and incomparable with v, b below an arbitrary up-closed H subset, no other root relations; all exterior points above v.

Suppose H has a minimal point p which is private, meaning b is not below p. Put

    R=H minus ({p} union U_H(p)),       r=|R|.

Require

    r<=2,       r(|H|-2)<=6.                            (DH-R)

Then

    2 Pr_P(u before b)+Pr_P(v before u)>=1.

There is no assumption on the number or common/private status of other H minima. No tail word, deadline or exterior sample is used to select the physical events. The three parameter regimes are r=0 with arbitrary |H|, r=1 with |H|<=8, and r=2 with |H|<=5.

## Proof

Use the same actual first-exterior-prefix cells as FG1 and DH. Cells missing u or b pay immediately. All other cells have prefix ideal I={a,b,u,v} union K, where K is an ideal of H, k=|K|. For each internal K word sigma let J be its first common-label rank, with J=k+1 if it has no common label. The exact raw insertion margin is

    M_sigma=(k+4)J-2(k+1).                              (1)

If p is absent, every point of K belongs to R, since an ideal containing any successor of p must contain p. Thus k<=r<=2. Equation (1) is at least 2-k>=0, the previously proved small-tail bound.

Now let p belong to K, and put r_K=|K intersect R|. Every K letter preceding p belongs to R, so there are at most r_K such letters. Move p from its position to the front and keep every other letter in its original relative order. This produces a legal K extension: p is minimal and is moved earlier, while no other relative order changes. Every word beginning in p has at most r_K+1 preimages, including itself. Indeed an inverse is determined by the position of p, and p's rank in every possible original word is at most r_K+1. Therefore

    Pr_uniform LE(K)(first letter p)>=1/(r_K+1).

Because p is private, J>=2 whenever the first letter is p. Since J>=1 always,

    E J>=1+1/(r_K+1).

The average of the exact margins (1) is consequently at least

    (k+4)(1+1/(r_K+1))-2(k+1)
            =[6-r_K(k-2)]/(r_K+1)>=0.                 (2)

If k<=2 the last inequality is immediate. If k>2, use r_K<=r and k<=|H| together with (DH-R). Sum the raw margins over K words, then over the actual prefix/suffix cells. The internal uniform-K word is used only to express a sum divided by e(K); it is NOT an assumed induced law after deletion from an original extension. This preserves the original true weights exactly.

## Relation to the earlier gates

- r=0 means p lies below every other tail point, so this is already a delayed-common-tail case.
- The reviewed two-minimum DH condition has minima p(private),h(common), with every h-successor above p. Then R={h}, and DH-R gives exactly the |H|<=8 theorem.
- If there are two common minima, each with all successors above p, R consists of those two heads. DH-R gives the earlier m=2, |H|<=5 extension.
- If there are two minima p,h but at most one h-successor is not above p, then |R|<=2. Thus the newly proposed one-domination-defect |H|<=5 gate is the same theorem, not six separate source-row proofs.

The proof is a bounded-rank insertion multiplicity argument inside the existing exact first-cut bank. It does not rename an old unconditional swap theorem; its extra content is a sufficient condition for every prefix ideal's first-common-rank average.

## Independently audited source applicability

PRIVATE_ROOT_RANK_CENSUS.py/.json checks the source masks directly and records 102 applicable occurrences: 53 overlap the 404 baseline and none overlap the four-equal-downset 30-row gate. Thus the net contribution after 434 is 49: the 43 already audited DH rows and six further r=2 rows. These are one parameter-uniform class, not a profile certificate list. The independently audited union is483, leaving2986 original banks unchanged. No count is added separately for the r=0 or old m=2 special cases.

## Sharpness of the parameter thresholds for this bank

Let H consist of p(private), r common minima h_1,...,h_r and s common leaves, every leaf above p and all h_i. Take P=Q with no exterior. Put k=r+1+s. The first r+1 letters of every H word permute these minima freely, followed by a free permutation of the leaves. Hence e(H)=(r+1)!s!, p is first with probability 1/(r+1), and J=2 precisely when p is first, otherwise J=1. Thus E J=1+1/(r+1), and every inequality used for the rank average is an equality.

The per-word counts from the original insertion count are

    N_sigma=(k+3)J+2k+5,
    KA_sigma=(k+3)J,
    KB_sigma=J+3.

Consequently the actual original bank margin is exactly

    2KA+KB-N=e(H)[6-r(k-2)]/(r+1).

For r=1, k=8 gives equality and k=9 fails. The latter is an actual thirteen-point P with Delta11, e(H)=10080, N=413280, KA=181440, KB=45360 and margin -5040. It is not a D9 or D10 counterexample.

For r=2, k=5 gives equality and k=6 already fails inside D9. The latter is an actual ten-point P with predecessor masks

    (0,0,1,1,5,7,7,119,119,119),

Delta8, e(H)=36, N=1044, KA=432, KB=156 and margin -24. Therefore the r=2 size bound cannot simply be relaxed from five to six even under the original maximum-degree-nine assumption.

These are failures only of the fixed bank 2Pr(u<b)+Pr(v<u)>=1 outside its proved parameter range. They are not ordinary-balance/NB counterexamples: the common heads and the shared leaves have fair twin pairs. PRIVATE_ROOT_RANK_SHARPNESS.py/.json reconstruct the actual posets and independently verify their counts by full ideal-subset DP; the family formula itself proves the threshold sharpness.
