# Independent review: nonchain minimal-anchor true-law obstruction

2026-11-11. **PASS_WITH_EXACT_SCOPE.** No hard mathematical gap found in the supplied obstruction family, its actual orientation-fibre calculation, the surviving one-sided transfer statements, or the ordinal-sum closure. This is an internal independent analytic and exact-count review, not a blind review, formal proof, external peer review, or literature-priority certification.

## Frozen input and independence

Reviewed full author file:

`research-review/nonchain-D10-true-bank-20261111/PROOF.md`

- Bytes: 11131.
- SHA256: `42c020575bc74d0536f2405c2db15e866bb2d97270e61e43432e6f174ac40580`.

The candidate and its expected formulas were supplied before review. I independently reconstructed the six-point insertion argument from its stated cover relations. For n=5,6,7,8 I separately built the complete transitive closure, directly listed every full original linear extension, and counted all named events. I did not import or execute the author's counting/search code or use its JSON counts as inputs.

For each orientation, I also rebuilt a fresh poset with the extra cover x<d or d<x and compared its **entire linear-extension word set** to the corresponding filter of the original word set. Thus the real-fibre identity was checked as a set equality, not merely a count equality.

The separate reviewer code and actual output are `review_direct_words.py` and `INDEPENDENT_DIRECT_WORDS.json`. The output retains every original word for each checked n and both orientation statistics. Full-word recursion shares the elementary linear-extension legality condition with any ideal-DP method, but it does not use memoized subset counting, the author's implementation, or the insertion formulas to produce the counts.

## 1. Precise theorem accepted

For the original family P_n defined by the author's explicit cover relations, for every integer n≥1:

    N=38n+86,
    K(b<a)=18n+46,
    K(v<c)=14n+20,
    K(x<v)=45,
    K(d<v)=12n+33,
    B_x=25−6n.

The pointwise identity B_x=K(b<a)−K(c<v<x) is valid because c<x, and its three comparison cells partition all original words. The maximum original incomparability degree is max(5,n+2). Therefore n=5,6,7,8 are genuine degree-at-most-ten negative fixed-original-minimum-anchor examples, with negative margins −5,−11,−17,−23.

Both orientations of the actual nonchain Dc={x,d} have positive **completed-bottom** banks, while their true original count sum need not pay the original fixed physical x. This is an auxiliary-bank/transport counterexample. It does not refute existence of a balanced pair, existence of some good original anchor, or the narrower accepted Q18 channel.

## 2. Analytic rederivation, including the infinite parameter

After deleting x and the z-chain, the six-label H has a<u,v,d and b<c<d. In every original word all H labels precede z1: u,v,d do by covers, and a,b,c do by transitivity. Thus every deletion word is exactly a word of H followed by the one fixed z-chain. This verifies the crucial terminal-chain assertion without a uniform-deletion assumption.

For a word w of H, write j=max(pos(a),pos(c)). There are n+6−j legal gaps for x, after both a,c and before z_n, including the gap immediately before z_n. The j values 3,4,5 exhaust all cases: d follows a,c, and a cannot occur as late as fourth because u,v,d would all still have to follow it. Their word counts are 18,12,8. Their b<a counts are 12,4,2; their v<c counts are 0,6,8. Weighting by n+6−j proves N, Kba and Kvc above.

The x<v slot sum is independent of n because v is in H, before the whole z-chain. In the j=3 class, the relative v positions 1,2,3 in the remaining three-label suffix each occur twice, for sum 12 per root prefix and 36 total. At j=4 only the u-before-c case contributes, giving 9. At j=5 there is no legal x-before-v gap. Hence Kxv=45. The d<v H-word counts per j are 9,3,0, yielding Kdv=9(n+3)+3(n+2)=12n+33.

All steps are finite structural classifications independent of n, and establish the stated infinite formulas analytically. The checks at n5..8 corroborate, rather than prove, the general parameter claim.

## 3. Full n5..8 counts, degrees, and actual fibres

Original counts (N,Kba,Kvc,Kxv,Kdv):

- n=5: (276,136,90,45,93), Δ=7, Bx=−5.
- n=6: (314,154,104,45,105), Δ=8, Bx=−11.
- n=7: (352,172,118,45,117), Δ=9, Bx=−17.
- n=8: (390,190,132,45,129), Δ=10, Bx=−23.

The full degree list independently matches:

    deg(a)=2; deg(b)=deg(c)=deg(d)=3;
    deg(u)=deg(v)=5; deg(x)=n+2;
    deg(z_i)=1 for i<n; deg(z_n)=0.

The x<d fibre always has

    (N+,Kba+,Kvc+,Kxv+,Kdv+)=(62,32,17,30,15),
    bottom=x, bottom bank +17.

The d<x fibre has

    (N−,Kba−,Kvc−,Kxv−,Kdv−)
      =(38n+24,18n+14,14n+3,15,12n+18),
    bottom=d, bottom bank 6n+11.

Thus for n5..8 the minus-fibre sizes are 214,252,290,328 and the minus bottom-bank margins are +41,+47,+53,+59. The same minus fibres' **fixed-x** margins are −22,−28,−34,−40. The original fixed score adds as +17 plus this negative fixed-x score, not as the sum of the two positive changing-bottom scores.

The actual normalized fibre weights are 62/(38n+86) and (38n+24)/(38n+86). No free mixture parameter enters.

Fresh orientation-poset degrees were checked too: Δ(P_n plus x<d)=5 and Δ(P_n plus d<x)=max(5,n+1), in particular 6,7,8,9 for the minus n5..8 cases. Adding the relations does not exceed the original degree budget.

## 4. Exact transfer boundary accepted

Let the physical original set D be fixed, and let each restriction cell fix its complete relative D word, or at least its first physical D label b_t. Then b_t<v is exactly the fixed original union event “some D label precedes v” inside that cell. Thus changing-bottom banks sum to a bank for that union event, not automatically a prescribed original z<v.

For this family:

    B_union=6n+28,
    K(union)=12n+48,
    B_union−B_x=12n+3.

All three formulas were checked independently. At n8, the positive bottom-bank sum is 17+59=76, whereas the fixed-x sum is 17−40=−23; the discrepancy is 99.

There is no contradiction: {x<v} is contained in the union event, and a lower payment inequality need not survive shrinking an event. Conversely a uniform **upper cap** on b_t<v does transfer to any fixed z∈D, by this same containment. A common original least element is also sufficient to keep b_t the same physical label in all completion cells. These statements correctly isolate the surviving direction already present in the public M1/M2 reviews.

Minor precision only, not a blocking gap: §5's arbitrary partition notation should be understood to require a well-defined fixed first-D label in each cell. The stated orientation restriction cells satisfy this. No extra hypothesis is needed for the main family.

## 5. Original hypotheses and separation from Q18

From the reconstructed full relations:

- The seed S={a,b,c,u,v} is an induced ideal with exactly a<u,a<v,b<c.
- P minus the inclusive a-upset is exactly {b,c}.
- D(u)=D(v)={a}; full downsets of both x,d are {a,b,c}; x,d are incomparable original minima of Dc, so x is a legitimate original minimal anchor rather than an upper or word-selected anchor.
- The actual common upset O=U(c)∩U(u)∩U(v) is exactly the z-chain.
- Consequently |P minus O|=7. A,Cv,Y,V are empty here. In particular the occupied A,Cv,Y and actual-Q18 hypotheses of the accepted child-u-zero delta3 channel fail.
- For n≥5, x is incomparable with z1,...,z_(n−1). The accepted Dc<Y<O saturation/first-O mandatory-anchor protection is therefore unavailable. This is an essential structural difference, not merely a difference in the number of labels.

I read the local public-source copies of ROOT_INSERTION_KERNEL, M1_PREVIOUS_UNION_REVIEW and M2_COMPLETE_REVIEW, and re-fetched CHANNEL_SCOPE at the fixed public commit `295ddcda63de8bb3c0f32112302f40dd1610165c`. Their accepted claims explicitly preserve the actual-Q18 occupied signatures and common physical anchor, or invoke a separate direct original dominant-anchor bank. Nothing reviewed there licenses the broad failed transport tested by P_n. This review does not recursively reprove those accepted ancestor results.

u,v are full twins, so their comparison is fair. Independently, b,a is strictly balanced for every n≥1:

    3Kba−N=16n+52>0,
    2N−3Kba=22n+34>0.

The candidate's explicit statement that these are not NB or guard-free residual sources is therefore necessary and correct. The other minimal anchor d has positive original bank Bd=6n+13, so the family does not refute existence of some good anchor.

Verified public scope source:

https://github.com/YinzhuCheng/one-third-two-thirds/blob/295ddcda63de8bb3c0f32112302f40dd1610165c/increments/2026-11-10/q18-delta3/CHANNEL_SCOPE.md

## 6. Ordinal-sum closure

For P_n ordinal-sum R, every original P_n word precedes every R word. Hence the complete extension set is the Cartesian product LE(P_n)×LE(R), and every old physical event count is multiplied by e(R). No incomparable cross-summand pair is introduced; the maximum degree is max(Δ(P_n),Δ(R)). The old seed/private/minimal-anchor relations remain unchanged, and all R labels lie in the enlarged actual common upset O, so the actual complement Q remains the old seven-label ideal.

Thus n8 and arbitrary finite R of maximum incomparability degree≤10 give unbounded cardinality at maximum degree10 and fixed-anchor bank −23e(R)<0. This preserves the broad obstruction without approaching the occupied-Q18 channel. The general extension-product rule is standard; no originality claim follows from applying it here.

## Verdict and remaining limits

**Accept the stated auxiliary-bank obstruction and exact transport boundary.** No original file was edited and nothing was published. The finite replay covered n5..8 as requested, every full original word, both real orientations, their degrees, and all named event counts; the all-n proof is analytic. No universal D10/Q18 payment, NB counterexample, or literature-priority statement is certified.
