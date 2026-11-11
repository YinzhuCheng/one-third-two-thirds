# Private-shield selection with additional private labels retained

2026-11-11. Independently reviewed analytic result: PASS for PS1 and PS2 under the exact hypotheses below. The mathematical body is unchanged from the signed draft SHA256 7e76afc54cb0b85b21ecc9794a903c4eb4da2f3a55fb51eec990e4bdaeb42555; only this current-status paragraph differs. This strictly generalizes the reviewed whole-private-ideal shield construction and includes the published DH-R gate. Its one-private-point specialization must not be counted again. Source increment is ZERO. This extends the existing first-cut / ideal-first-color mechanism without a historical priority claim. See PRIVATE_SHIELD_SELECTION_INDEPENDENT_REVIEW.md.

## PS1. An internal first-common-rank theorem

Let H be a finite poset and C an ideal of H. Put B=H minus C and call its points common. Choose a fixed ideal S of H contained in C; write a=|S|. Allow S empty, with the ordinary vacuous convention. Define

    B0={y in B: some x in S has x not<y},  s=|B0|,
    B1=B minus B0.

Every B1 point is above every S point. No condition is imposed on the number, order, or incidence of additional private points C minus S, except that the full C remains an ideal. Let J be the first B rank in a uniform extension of H, with J=|H|+1 if B is empty. Then

    E J >= 1+a/(s+1).                              (PS1)

The physical sets C,S,B0,B1 are fixed before the extension is sampled. The proof does not delete C minus S or assert that the remaining word has a uniform induced distribution.

### A second actual cut, rather than an uncontrolled deletion

If B1 is empty, B=B0 has s points. The usual ideal-first-color estimate gives E J>=1+|C|/(s+1)>=1+a/(s+1).

If B1 is nonempty, partition all actual H extensions by their exact set I before the first B1 point and by the complete literal suffix beginning at that B1 point. The set I is an ideal, contains all S, and contains common labels only from B0. Put c_I=|I intersect C|, r_I=|I intersect B|, so c_I>=a and r_I<=s. Within a nonempty cell every extension of I concatenates legally with the fixed suffix, and the prefix law is exactly uniform on LE(I). Its original unit completion weights are not changed.

Use the first-common rank in I, with the sentinel |I|+1 if I has no common point. This is also the first-common rank in the full H word: when I contains no common point, the first suffix label is the first B1 point and hence the first common point. The usual ideal-first-color bound in I gives

    E(J | this cell)>=1+c_I/(r_I+1)>=1+a/(s+1).

Sum raw J counts over all actual cells, with their actual sizes e(I). This proves PS1. Empty I, empty C, S empty, and empty H respect the same conventions.

For completeness, the used ideal bound is obtained by fixing both full internal color words and exchanging the first nonideal color with a marked ideal occurrence, preserving both internal orders. All ideal labels move weakly earlier and other labels weakly later, so the cross-relations remain legal. With c ideal and r other labels this gives Pr(first ideal)>=c/(c+r). Apply after every specific initial private prefix: Pr(J>t)>=(c)_t/(c+r)_t. Summing tails gives E J>=(c+r+1)/(r+1)=1+c/(r+1). Thus no unproved correlation principle enters PS1.

Although PS1 is stated for an ideal S, the cut proof works for any fixed subset of C. Replacing such a subset by its full down-closure in H keeps B0 unchanged and can only enlarge a, because C is an ideal and every common point above the subset is above its down-closure. Therefore restricting a structural search to private ideals loses no strength in this particular bound.

## PS2. A generalized original-object bank gate

Let Q be an original induced ideal in a finite original poset P, with labels a0,b,u,v and H. The complete root/tail relations are

- a0<u and a0<v; b is incomparable with a0,u,v;
- every H point is above u and incomparable with v;
- b lies below an up-closed subset B of H;
- there are no other root-to-tail relations; the induced H order is arbitrary.

Every original exterior point lies above v. Put C=H minus B, the full private tail ideal, n=|H|. Choose one fixed private ideal S contained in C, let a=|S|, and define B0,B1,s exactly as in PS1. Assume

1. In the true predecessor graph from B0 to the full private C there is a matching leaving at most two B0 points unmatched.
2. F_S=n(a-s-1)+4a+2s+2>=0.

Then in the uniform extension law of this same original P,

    2 Pr_P(u<b)+Pr_P(v<u)>=1.                      (PS2)

The two events and coefficients are fixed before any exterior word, prefix ideal, or extension is sampled. This is a one-sided bank. Its usual NB exclusion additionally requires a reference b before u before v, so both charged physical events reverse that same original reference. No helper NB premise or degree cap is used to prove PS2.

### Every original first-exterior prefix is covered

Use the same actual first-exterior cut as the established FG proof. Fix I, the exact Q prefix set before the first exterior label, and the entire literal suffix starting there. If the exterior is empty take I=Q. The actual exterior-above-v hypothesis forces a0,v into I. If u is absent, v<u is certain; if u is present but b absent, u<b is certain. These cells pay pointwise.

Otherwise I contains all four roots, and K=I intersect H is an ideal of H, k=|K|. For each fixed internal K extension sigma, let j be its first common rank, or k+1 if no common point occurs. The established exact insertion counts are

    N_sigma=(k+3)j+2k+5,
    K_(u<b),sigma=(k+3)j,
    K_(v<u),sigma=j+3,

so the raw bank margin is

    M_sigma=(k+4)j-2(k+1).                         (PS3)

The internal uniform K notation below only divides this raw sum by e(K). It is not the induced law after deleting the four roots from a random original extension.

If S is not contained in K, K contains no B1 point. Hence all its common points belong to B0. Restrict the one global matching to K: every matched common point in the ideal K brings its distinct actual private predecessor into K. With c_K=|K intersect C| and r_K=|K intersect B| this gives r_K<=c_K+2. The ordinary ideal-first-color bound E J>=(k+1)/(r_K+1) inserted in PS3 gives

    average raw M >= (k+1)(c_K-r_K+2)/(r_K+1)>=0.

If S is contained in K, apply PS1 inside this same K, with private ideal C intersect K and the unchanged S. Its exceptional common set is K intersect B0, of size at most s. Thus E J>=1+a/(s+1), and PS3 gives

    average raw M >= f_S(k)/(s+1),
    f_S(k)=k(a-s-1)+4a+2s+2.                      (PS4)

When a>=s+1, f_S(k)>0 for all k>=0. Otherwise f_S decreases, so k<=n and F_S=f_S(n)>=0 imply f_S(k)>=0. Every actual prefix/suffix cell therefore pays. Sum its raw original full-extension margin to prove PS2. Both nested cuts keep fixed physical labels and their complete actual suffixes; neither introduces uniform profile, orbit, deletion, or internal-word mixture weights.

## PS3. Exact relation to prior gates and what is actually new

1. Taking S=C recovers the reviewed whole-private-ideal shield theorem exactly, with a=c. Its rank bound is therefore a specialization of PS1.
2. DH-R selects a private minimum p and counts all H points outside p's principal upper tail, including other private points. Taking S={p}, our s counts only the COMMON points outside that tail, so s<=r_DH. The DH-R conditions r_DH<=2 and r_DH(n-2)<=6 imply s<=2 and 6-s(n-2)>=0 (with n<=2 handled directly). Thus the exceptional matching is automatic and PS2 includes DH-R. The entire old whole-private c=1 specialization was already exactly DH-R, as recorded in DH_R_RELATION_CORRECTION.md.
3. PS2 includes the whole-private shield test, DH-R, and FG(M), and it covers some contracts failing all of these and FG(D). It does not include FG(D) in general; the two mechanisms are incomparable. Extra private labels need not enter the obstruction count s and need not be artificially deleted. A private two-point shield with at most one exceptional common point pays for arbitrary tail size, even with arbitrary further private points and relations consistent with the ideal contract.

The numerical F_S condition is sufficient, not an asserted pointwise characterization of the bank in each P. An unsuccessful choice of S does not show no other choice works. Searching over private ideals is structural metadata work, not a deadline-profile certificate. No claim of new balanced-poset class or new source-row count follows merely from these theorem inclusions.

The reverse separation from FG(D) already occurs with seven tail points: take two private minima p,d, two common leaves above p only, and three common leaves above d only. FG(D) applies because every common label has a private predecessor. The only private ideals S are empty, {p}, {d}, and {p,d}. Their respective (a,s,F_S) values are (0,0,-5), (1,3,-9), (1,2,-4), and (2,5,-8). No choice passes the new selector. Thus one must retain FG(D) as a distinct mechanism, even within the degree-nine scale.

## PS4. A genuine degree-nine strict contract difference

Take P=Q with predecessor masks

    (0,0,1,1,5,5,37,7,151,407,919).

The tail is: private minimum p (label4); a separate private chain q1<q2 (labels5,6); common minimum z (label7); and a common three-chain (labels8,9,10) above p and z, incomparable with the private q-chain. It has n=7 and maximum incomparability degree9. Take S={p}. There is exactly one exceptional common point, z, so a=1,s=1,F_S=1 and the exceptional matching has one unmatched point. PS2 applies.

The whole-private shield test fails: C={p,q1,q2}, all four common points fail to lie above every C point, and only p can support them, so the exceptional matching has deficiency3. The old full matching gate fails for the same reason. The old delayed-common gate fails because z is common and minimal in H. For DH-R, p has three outside-tail points q1,q2,z, while q1 has five outside-tail points, so no private minimum meets r<=2. Thus this is a strict contract extension, not merely a renaming of DH-R.

Full original-Q counts, degree, and comparisons are checked in PRIVATE_SHIELD_SELECTION_CHECK.json. This distinguishing example is NOT asserted to survive every other analytic source-tree rule. Even if it does, no occurrence is added without the actual source packet and deduplication against the accepted1307 ledger.

## PS5. Sources and next use

The original root count and first-exterior interface are the FG proof, ultimately Kevin Fathi, Gold Certificates and Balanced Pairs v22, https://zenodo.org/records/23933091, §24.4.1. The exact public DH-R comparison uses

https://github.com/YinzhuCheng/one-third-two-thirds/blob/c07dfaf9fe4a82abcf3fd5b67c571a18ba1f3fba/increments/2026-11-10/structural-progress-v2/d9/PRIVATE_ROOT_RANK_GATE.md

and its independently reviewed companion PRIVATE_ROOT_RANK_INDEPENDENT_REVIEW.md. The reviewed whole-private construction is retained in the preceding frozen increment, without editing its signed bytes.

The current public recovery contains the published400/607-era proofs and source summaries but not a verified complete ORIGINAL_V_FIRST_PACKET.json or the accepted1307 raw occurrence ledger. This worker therefore reports a theorem generalization with source increment ZERO. The next useful operation is to restore those exact inputs, run a private-ideal structural selector on the unchanged source masks and genuine exhausted-v evidence, verify reference orientation, and deduplicate. It would be incorrect to infer a new source row solely because a poset contract differs from four older gates.
