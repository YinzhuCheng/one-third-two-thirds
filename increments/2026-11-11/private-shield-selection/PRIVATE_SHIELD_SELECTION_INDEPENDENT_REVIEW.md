# Independent review: selecting a private shield

2026-11-11. **PS1 and PS2 PASS under their exact stated original-object hypotheses. One erroneous old-gate inclusion claim was found and corrected: PS2 and FG(D) are incomparable. No source-row increment is established.** This is an internal independent mathematical review, not external peer review or a complete D9 proof.

Final reviewed manuscript binding is recorded at the end. I read the preceding whole-private shield proof and review, the complete new manuscript, the DH-R comparison correction, and the recovered fixed public DH-R theorem. I did not import or run either author checker. The separate `PRIVATE_SHIELD_SELECTION_INDEPENDENT_CHECK.py` reconstructs counts from full predecessor arrays.

## 1. The strongest objection found: FG(D) is not included

The initial manuscript said the selected-shield gate was strictly more general than the whole-private shield, DH-R, FG(D), and FG(M). Inclusion is valid for all named gates except FG(D). This is a scope error, not a gap in the PS1 or PS2 proofs. The author corrected the inclusion statement after the following counterexample was reported.

Let H have private minima p,d, two common leaves above p, and three common leaves above d, with no other tail relations. Its complete tail predecessor array is

    (0,0,1,1,2,2,2).

Every common label has a private predecessor, so FG(D) holds. The only private ideals S are empty, {p}, {d}, and {p,d}. Their parameters (a,s,F_S), with n=7, are respectively

    (0,0,-5), (1,3,-9), (1,2,-4), (2,5,-8).

No choice passes PS2. The complete original Q is

    (0,0,1,1,5,5,23,23,39,39,39),

and has maximum incomparability degree9. Independent full-Q recursion gives (N,K_(u<b),K_(v<u))=(18780,10800,2340), with bank margin5160. Thus this is a failure of the new sufficient structural test, not a failure of the bank. Together with the manuscript's opposite separation example, it proves actual incomparability of the two contracts, even within degree9.

With this correction, no load-bearing mathematical gap remains.

## 2. PS1: arbitrary extra private labels are retained with true weights

Fix C and S before sampling a word. When B1 is nonempty, a cell consists of the actual ideal I preceding the first B1 label, together with the entire literal suffix starting at that label. Every selected point lies below this first B1 label, so S is contained in I. Every common point in I belongs to B0. Hence c_I=|C intersect I|>=a and r_I=|B intersect I|<=s.

The cell is in exact bijection with LE(I): concatenate any I extension with its fixed suffix. The set I is an ideal, so no predecessor obligation crosses from the suffix back into I. Reordering the prefix cannot invalidate the fixed suffix. Each prefix has exactly one completion in this cell, and the uniform conditional law is therefore the uniform law on LE(I), with no discarded multiplicity.

The first-common rank in I equals the full-word first-common rank. If a common label is already in I this is immediate. If none is, its sentinel |I|+1 is exactly the position of the first suffix label, which is itself common. This boundary is essential; replacing the sentinel with a different convention would break the argument.

The full private intersection C intersect I remains an ideal of I. The standard ideal-first-color inequality gives

    E[J | cell]>=1+c_I/(r_I+1)>=1+a/(s+1).

The inequality holds separately in every cell, so averaging with their actual sizes e(I) proves PS1. If B1 is empty, all common points are the s exceptional ones, and the same established ideal inequality on H gives 1+|C|/(s+1)>=1+a/(s+1). Empty H, C, S, I, and B obey the stated conventions. In particular, B empty has s=0 and J=|H|+1>=a+1.

The ideal-first-color inequality itself is applicable: fix the full internal words of the ideal and its complement. From a legal shuffle beginning outside the ideal, mark an ideal occurrence and exchange its color with the initial color, restoring both internal orders. Ideal labels move weakly earlier and other labels weakly later, preserving every cross-relation. Marking the exchanged nonideal occurrence in the output gives c*N_other-first<=r*N_ideal-first. Apply after each specified initial private prefix and sum the resulting lower bounds on Pr(J>t) to obtain 1+c/(r+1).

Nothing in the cut argument actually requires S to be an ideal: any fixed S subset of C works. Its down-closure remains in C, has the same B0, and can only increase a. The manuscript's restriction to ideal choices therefore loses no strength. In PS2 the matching graph is unchanged under this closure and F_S increases by (n+4) per added private point, so the same conclusion applies to the full structural gate, not only to the rank bound.

## 3. PS2: both parts of the original-prefix split are valid

The outer first-exterior cut is made in the same original P. Because every exterior label lies above v and a0<v, every nonempty cut cell contains a0 and v. Fixing the complete exterior-starting suffix makes its prefix uniformly range over LE(I), with original unit word weights. If u is absent, v<u is certain; if u is present but b absent, u<b is certain. These cases pay the same fixed bank pointwise.

In the remaining case all four roots are present and K=I intersect H is an ideal. The full-root insertion identity was independently rederived and checked. For one K word with first-common rank j, inserting v after a0 gives one v-before-u position, j positions after u but before the first common, and k+1-j later positions. The numbers of legal b positions in these classes are respectively j+3, j+3, and j+2; the corresponding numbers realizing u<b are j, j+1, and j. Only the first class realizes v<u. Thus

    N=(k+3)j+2k+5,
    K_(u<b)=(k+3)j,
    K_(v<u)=j+3,
    2K_(u<b)+K_(v<u)-N=(k+4)j-2(k+1).

The convention j=k+1 when K has no common points is valid, including k=0. A uniform K word is used only to divide a sum of these raw counts by e(K); it is not claimed to be the deletion marginal of a full original extension.

If S is not contained in K, no B1 label can occur in K. The single matching from B0 to the **full** private C restricts correctly: every matched common label in K pulls its distinct private predecessor into the ideal K. At most two common points remain unmatched, giving r_K<=c_K+2. The standard rank bound then yields raw average margin

    (k+1)(c_K-r_K+2)/(r_K+1)>=0.

If S is contained in K, PS1 applies to the induced K with private ideal C intersect K and the unchanged physical S. Its exceptional set is precisely K intersect B0. Bounding its size by s gives the stated raw margin f_S(k)/(s+1), where

    f_S(k)=k(a-s-1)+4a+2s+2.

If a>=s+1, this is positive for all k>=0. Otherwise a<=s because the parameters are integers, so f_S decreases with k; k<=n and F_S=f_S(n)>=0 then give nonnegativity. The two cases exhaust every actual prefix ideal. Neither the matching nor the event choice is allowed to depend on an extension, and the proof does not make either depend on one.

Summing the actual raw cell margins proves PS2 for arbitrary exterior size and order under the specified exterior-above-v contract. No degree, NB, helper-law, or uniform-profile premise entered this proof. The strict reverse-reference/NB conclusion remains a separate application requiring the original reference b before u before v.

## 4. Prior-gate relation and the c=1 attribution correction

The new theorem contains the whole-private shield by S=C. That shield already contains FG(M), as follows directly from its matching and the inequality verified in the preceding review. The whole-private and DH-R inclusions are strict at the contract level, as the manuscript's example shows. They are not newly measured source occurrences.

I directly read the recovered public `PRIVATE_ROOT_RANK_GATE.md` fixed at c07dfaf9fe4a82abcf3fd5b67c571a18ba1f3fba. It permits any number/status of additional private tail labels, selects a private minimum p, and counts all labels in R=H minus ({p} union U_H(p)). Taking S={p} gives s<=r=|R|. DH-R requires r<=2 and r(n-2)<=6. Thus the exceptional matching condition is automatic, and for n>=2,

    F_S=6-s(n-2)>=6-r(n-2)>=0.

The remaining tiny cases are direct. Hence the new gate indeed contains the full published DH-R contract, not just its one-private-point case.

When the **entire** private ideal is C={p}, p is minimal and every other tail point is common. Then B0 equals R exactly. No exceptional point has a private predecessor, so the exceptional matching condition is exactly s<=2, and the numerical condition is exactly 6-s(n-2)>=0. Therefore the whole-private c=1 specialization is precisely the already published DH-R theorem, including its finite thresholds. The comparison correction is mathematically correct. The prior threshold controls, source mappings, and historical contributions cannot be counted again.

The actual relation is: PS2 contains whole-private shielding, DH-R, and FG(M); PS2 and FG(D) are incomparable. It can apply to contracts failing all four named older tests. This does not establish exclusion from every other prior mechanism.

## 5. Independent exact diagnostics and separating controls

The separate checker uses full transitive predecessor arrays. Naturally labelled posets are generated recursively by adding a last label with each possible ideal as its predecessor set. The rank routine is a direct subset recurrence, and the full-Q event routine counts each event when its first endpoint is appended before its second endpoint. It neither inserts event edges nor uses the root identity to produce event counts.

Executed checks:

- All 408 naturally labelled H posets of sizes zero through five, with all 5,231 private ideals.
- 43,722 rank tests over **all** S subsets of C, including 27,871 ideal selections; 1,856 rank equalities.
- 5,231 full-Q root identities by independent full-poset event counts.
- 4,189 distinct full-Q instances admitting a qualifying ideal selection, arising from 21,512 qualifying ideal choices; every bank margin is nonnegative.
- 719 first-shield partition instances through tail size four, comprising 3,044 literal cells. Each cell's extension count and total first-common rank equal a separately induced-prefix DP, checking the exact completion-weight claim.
- 445 one-exterior-point completions for qualifying tails through size three, ranging over every actual predecessor ideal containing v; every bank margin is nonnegative.

These finite checks corroborate the proof and implementation only. They do not prove the unbounded theorem or establish a source-tree census.

The manuscript's private-three-point distinguishing example has

    pred=(0,0,1,1,5,5,37,7,151,407,919),
    Delta=9, (N,K_(u<b),K_(v<u))=(1638,840,210), margin252.

Its selected p has a=1,s=1,F_S=1. The whole-private matching and FG(M) fail with deficiency3; FG(D) fails at the common minimum; neither private minimum satisfies DH-R. The exact arrays support every stated separation claim.

An independent second distinguishing control has two private minima p,d, one common minimum q, and a common four-chain above p and q but incomparable with d:

    pred=(0,0,1,1,5,5,7,87,215,471,983),
    Delta=9, (N,K_(u<b),K_(v<u))=(506,240,66), margin40.

Choosing S={p} gives a=1,s=1,F_S=1; choosing all C has F=-8 and matching deficiency4. FG(D) fails at q; DH-R fails for p with r=2,n=7 and for d with r=6. The tail has 14 extensions and first-common-rank sum24, checked independently. This control must not be confused with the older whole-private example whose common chain lies above both private minima.

For necessity of retaining a numerical hypothesis, the old a=1,s=2,n=6 control has F=-2, degree8, and full counts (174,72,26), giving margin -4. It refutes dropping F merely because the exceptional matching has deficiency at most two. It does not show that F>=0 is necessary for each individual P, and it is not an ordinary-balance counterexample.

## 6. Status and limits

PS1 and PS2 are analytically proved under the stated exact contracts and independently reviewed here. The corrected comparison to FG(D) is supported by explicit controls in both directions. The DH-R attribution correction is confirmed against its public source. Frozen preceding files were not edited.

No complete current source packet or accepted1307 occurrence ledger was audited in this review. No source row is added or removed, no certificate is retired, and no claimed historical population is verified merely by reproducing a small poset. Structural selection on the true original masks, exhausted-v evidence, reference orientation, and deduplication remain separate work.

## Final reviewed file bindings

The author confirmed this correction-only final freeze, and I reread the amended comparison section and verified these file hashes. The core PS1/PS2 proof is unchanged by the comparison correction.

- `PRIVATE_SHIELD_SELECTION_DRAFT.md`: SHA256 `7e76afc54cb0b85b21ecc9794a903c4eb4da2f3a55fb51eec990e4bdaeb42555`.
- `DH_R_RELATION_CORRECTION.md`: SHA256 `0b17c2f3e4cb103da22468999a1868fd755dacbc5d73d5f98db098207884bc15`.
- Independent checker `.py`: SHA256 `bd8f31f9d7b9b9b586172aee7cdf1c46d3cb91bac1c99bad3ba9bdb2858c9740`.
- Independent checker output `.json`: SHA256 `e0d37a479613c9c816842d7bb9fdbe180a31b0f98efda5d2052aba6ff56e7c2a`.

The review does not depend on the author's selector or checker. It does not approve source census arithmetic or any external publication action.

### Current reader edition: status-only promotion

The author subsequently supplied `PRIVATE_SHIELD_SELECTION_PROOF.md` as the current reader edition. I independently compared its raw bytes and line diff with the signed draft. The files have the same line count, and only line3 differs: the former author-draft/pending paragraph is replaced by a reviewed-PASS status paragraph naming the signed draft hash. All lines before and after that status paragraph, including the complete mathematical body, are byte-identical. No mathematical review scope, hypothesis, conclusion, control, or source-row count changes.

- Current reader edition `PRIVATE_SHIELD_SELECTION_PROOF.md`: SHA256 `41a076ec2ba3ff5e92f37952e7a4101e4a0428fb6e9359e8dbdec01b6e5de350`.
- Signed historical `PRIVATE_SHIELD_SELECTION_DRAFT.md` remains unchanged at SHA256 `7e76afc54cb0b85b21ecc9794a903c4eb4da2f3a55fb51eec990e4bdaeb42555`.

The PASS in this review therefore also applies to the mathematically identical current reader edition. This binding is not an external publication action or an authorization for one.
