# EC3/EC4 independent mathematical review

2026-11-10 UTC. **PASS for both stated ordinary-payment closures.** This reviewer did not participate in their derivation. This is a non-blind internal independent mathematical review, not external peer review, formal verification, or originality certification.

Reviewed source: `SECONDARY_EMPTY_ROOT_BANK_CLOSURES.md`; SHA256 `63d015e9687c1afca5d5152ee1f7e50b86c8aee9eea1a107240a6bd647994858`.

## Findings first

Both original-count inequalities are correct under the complete displayed contracts:

- EC3, m3k7: `24K_u+3K_y+3K_z-10N >= 8e(C)>0`.
- EC4, m4k6: `7K_u+K_y+K_z-3N >= 12e(C)>0`.

Nonminimal empty labels are genuinely allowed: the proof uses the true triple-gap A0 count rather than incorrectly extending the min-run-one identity. All kernels retain original word multiplicities. The selected banks are fixed on the complete original object, not chosen anew in each fiber. With the accepted candidate-wise upper bounds and earlier unique-low-C-minimum reductions, the two formerly remaining cells are ordinarily paid.

The remaining necessary zero-frontier+empty parameter list becomes m4k7 and m5k7. This is not universal fixed-(u,b) payment, full D10/B1, a new unguarded realization, or NB.

## 1. Triple-gap counting and correlated empty budget

I independently reconstructed A0_beta by placing the three old roots in positive C-word gaps. The baseline has HYZ gap choices. A collision of roots Y,Z contributes one extra ordering for each of H*min(Y,Z) choices, and similarly for the other two pairs. At a triple collision, baseline plus three pair corrections totals four orderings, whereas six are legal; this requires two extra for each common positive gap. Hence

    a_beta=HYZ+H min(Y,Z)+Y min(H,Z)+Z min(H,Y)+2min(H,Y,Z).

The formula remains correct when some runs are zero. No root permutations or old-word multiplicities are missing.

Every empty-signature C label lies in Mx-E, so their total number is at most k-m. The initial min(H,Y,Z) labels of an actual beta are precisely an initial all-three-roots-missing run and thus all empty. This proves the necessary correlated bound min(H,Y,Z)<=k-m. It is valid even when those labels are nonminimal or related. The original root degree bounds give H<=k and Y,Z<=6.

## 2. Non-E-start gamma fibers are exhausted correctly

Deleting the actual C-minimum f gives each true gamma all legal f gaps 0..d, d<=7. If gamma's first label c was C-minimal, the unique-low-C-minimum and zero-x-frontier hypotheses force c to have yz signature. If not, its only possible predecessor is f, hence f<c and d=0. This argument does not require c to be nonempty.

At gap0 the original beta begins with f, so Q=0 and H,Y,Z are all positive. Its complete triple-gap formula and empty budget apply. For any later legal gap in the yz branch, Q=Y=Z=0 and A0=A1=0, giving the stated positive kernels. No nonminimal empty branch has been omitted. C-f is nonempty because m is three or four.

## 3. EC3 q0 bound independently checked

Adding 7F+3G gives the source's equation (5). Under Y<=Z, collecting the two minimum terms using the exact A0 formula yields exactly equation (6). I verified each coefficient.

- For Y<=2, the constant part is at least556, the H-coefficient term at least-112, and the two minimum penalties together at least-160, yielding284.
- For Y>=3, the H coefficient is at most-6, while both negative minimum terms are nonincreasing with H. Thus increasing H gives a valid lower bound.
- For 3<=Y<=4, setting H=7 gives `840+22Y+68Z-46YZ`, then Z<=6 yields `1248-254Y>=232`.
- For 5<=Y<=Z<=6, the actual shared-empty budget forces H<=4. Setting H=4 gives `620+24Y+40Z-16YZ`, and Z<=6 gives `860-72Y>=428`.

These cases exhaust the necessary original run domain. The weakest bound232 is therefore analytic and does not depend on sampled run tuples.

## 4. EC3 arbitrary-deadline prefix bound

For E-start fibers the exact first value is584+50h, and the later kernel is

    420+(60-62Q)H+31Q(Q-1).

Raising Q changes it by62(Q-H)<=0, so the stated q relaxations are in the correct direction.

For h<=3 and q relaxed to h, the smallest mandatory noninitial value can be written `480-33h-31h^2>=102`; each extra-slot value is `420+29h-31h^2>=228`. Thus every term exceeds the required per-word margin8.

For 4<=h<=6 and q relaxed to3, I independently summed the first two increments and the plateau to obtain

    B3(h)=460+716h-126h^2.

Later increments are606-126h, producing the stated full-prefix total4702-772h. The mandatory increments decrease to the plateau, so the partial sums are concave through gap h; thereafter they are linear. Consequently the prefix minimum over every actual d in0..7 lies among0,h,7. These three bounds are respectively at least784,220,70. No unproved d>=h assumption is needed. At most eight C words occur in a fiber, and70>=8*8.

The non-E-start first value is at least232 and each later value is420+60H>=420. These also exceed8 per actual word. The true-fiber sum proves EC3.

## 5. EC4 q0 bound independently checked

Direct addition 2F+G gives equation (8), including cancellation of the exact y_beta term. For H<=2, the source's upper bound on a_beta follows termwise from min(H,Y),min(H,Z),min(H,Y,Z)<=H. It gives at least168 for H=1 and at least164 for H=2, using YZ<=3(Y+Z) and min(Y,Z)<=(Y+Z)/2.

Otherwise the shared-empty cap min(H,Y,Z)<=2 forces one of Y,Z to be at most2. Taking Y<=Z and relaxing H to the domain[2,6], I recovered the two expressions for Y=1 and2. Replacing min(H,Z) by6 is valid because its coefficient is negative. The resulting bilinear lower bounds have exactly the four stated corner values:

- Y1:172,237,228,253;
- Y2:176,212,200,172.

A bilinear function on a rectangle takes its minimum at a corner, so the conservative uniform lower bound160 follows. The overlap at H=2 is harmless; the H<=2 branch already covers all cases with that H.

## 6. EC4 arbitrary-deadline prefix bound

For E-start fibers the later kernel is124+(18-18Q)H+9Q(Q-1), with change18(Q-H)<=0 on raising Q. Independently summing the q=h mandatory slots gives

    B4(h)=168+144h-6h^3.

For1<=h<=4 the extra coefficient124+9h-9h^2 is at least16; B4 is concave with endpoint values306,360. The same concave-then-linear prefix argument shows a minimum at0,h,7, all at least182.

For h=5,q=4 the eight values are exactly

    238,124,34,-38,-92,-92,-38,-38.

Their sum is98. The first increments are positive and all subsequent increments are negative, so the prefix minimum is98. Every actual fiber contains at most eight words, and98>=12*8. The non-E-start first value160 and later values124+18H also exceed12 per actual word. Summing proves EC4.

## 7. Fixed-bank quantifiers, dependencies, and ledger

The full-original sums are exactly

    sum(7F+3G)=24K_u+3K_y+3K_z-10N,
    sum(2F+G)=7K_u+K_y+K_z-3N.

These correspond to the fixed normalized banks (8,1,1)/10 and (7,1,1)/9. Each candidate separately has an upper bound below2/3, so a strict lower bank mean supplies an individual strictly balanced member. No averaging shortcut is used for upper bounds.

The proof partitions actual LE(C) by deletion of f and sums each genuine gamma fiber with its actual size. No profile deduplication, uniformization of tails, conditional OLD moment, or double consumption of prefix credit occurs. The manuscript's two parameter closures follow from the accepted unique-low-C-minimum residual reduction; neither claims to handle the other two cells.

The existing WB4 unique-empty-label result remains correct, but its m3k7 and m4k6 portions are now subsumed for ordinary payment by EC3/EC4. Its applicable m4k7 portion remains useful. No OC2/OC3/OC4 or ND1 computer-assisted core count is a dependency of these new proofs. No original-object search was performed in this review; CURRENT_ADVANCE was not edited.
