# Independent audit: lower gate b<s, two upper anchors, one e-exception h

## Conclusion
The revised analytic argument has no identified gap. Removing the earlier condition b<h is valid. The proof uses neither a maximum-incomparability bound nor |A|=5. The supplied 15-point witness was independently reconstructed from its raw vertices and generating relations, and passes all stated structural and exact-count checks.

## Exact domain
Finite C2; A={s,h} disjoint-union R; A\U(d)={s}; e<R union F; d<h and e incomparable h; b<s. There are distinct r,t in R strictly below every member of F union U(s). As usual strict predecessor/successor sets use the whole poset, not cover sets. The assumptions imply s incomparable h and no R element is below s. Thus after deleting the first label v, the five retained labels a=c1,d,x=c2,y=e,s have only a<x,a<s,d<y internally, with the additional outside predecessor b<s. There is no hidden A-predecessor of s.

## Fixed outside word and cancellation
The outside word consists of b,h,R,F and obeys their induced order. Both a,d precede the first non-b outside label. The deadline of y is the first R-or-F label; x has deadline first F; s has deadline first U(s). Empty successor sets use the final virtual deadline.

In each outside-word fiber, swap the adjacent initial roots a,d in the reduced five-label word to cancel the a,d and d,a prefixes. This remains valid with b interspersed: b is independent of a,d and its sole retained-core constraint is b<s. The remaining positive prefixes are a x d, a s d, a x s d, a s x d where permitted; the only negative prefix is d y a.

### b is not the first outside label
The first outside label is non-b, so a,d must precede it and s cannot precede it. Hence only positive prefix a x d and negative prefix d y a survive. Let H,I be the y,x deadlines in the **original outside word containing b**, and let C be the allowed gap interval for s after b and before its deadline. Then

  D = W(C,H) - W(C,I),
  W(C,k) = k|C| + |C intersect {1,...,k}|.

Indeed these count insertion of the remaining independent pairs (y,s) and (x,s). Every F point follows the two R anchors, so the first F deadline I is no earlier than the first R-or-F deadline H; the empty-F virtual deadline also satisfies this. Therefore D<=0. H need not be at most 2 in this branch; imposing that bound here would be an error.

### b is the first outside label
Delete b from the word and count its insertions before the first remaining outside label and before s. Put W(i,j)=ij+min(i,j). The y deadline H is 1 or 2 because h is the sole outside exception to e; the two distinct anchors ensure I,J>=H+2 for the x,s deadlines. The prefix contributions give exactly

  D = 4 W(J,H) + 2 W(I,H) + 5H - 4 W(I,J).

The extra J terms in B(J,H)=W(J,H)+J and B(J,I)=W(J,I)+J cancel. Expanding under H<=I,J gives

  D = 4HJ + 2HI + 11H - 4IJ - 4min(I,J).

Each coordinate is strictly decreasing on I,J>=H+2. Thus D is at most 2H^2+3H-24, namely -19 for H=1 and -10 for H=2. An independent exact six-core ideal-DP agrees with this identity for H=1,2 and I,J=H+2,...,H+6. Those checks are diagnostic; the prefix argument and algebra provide the general proof.

Since b is minimal in the outside induced poset, there exists a legal outside word beginning with b. Its fiber is nonempty. Summing over the disjoint outside-word fibers therefore gives a **strict** negative signed difference. Consequently

  p(c1<d) < (1+q0)/2.

Combined with the already established universal C2 lower/upper menu bounds, the specified fixed menu is balanced. The strict conclusion is optional; the proposed non-strict bound is valid.

## Independent witness verification
Original independent-audit input, script and full receipt were temporary research files and are not included here. Their local paths are intentionally omitted. The corresponding E16 generating relations and separately reconstructed checks are included in `examples.json`, `verify_e16_structure.py`, `E16_STRUCTURE_VALIDATION.json`, `verify_e16_good_pairs.py` and `E16_GOOD_PAIR_VALIDATION.json`; these do not purport to restore the original full receipt.

Verified: 15 vertices; global maximum incomparability degree 9; no primal very-good; no dual very-good; no mixed forcing cycle; no proper nontrivial autonomous module. A topological order of the full mixed graph is

  v,c1,d,b,e,r,c2,w,t,s,u,f0,f3,f1,f2.

Exact independently recomputed counts:

  N=136953, #(c1<v)=38912, #(c1<d)=81688,
  E=2110, G=14599, E-G=-12489,
  R0=38912, R1=34629, B=8147, Z=4283.

G was counted directly by the reverse union event, not inferred solely from the signed identity. This witness establishes nonredundancy relative to the specified certificates. It is not a classification or a general originality claim.

## Prior three-anchor branch
The older b||s, b<h, R-size-3 branch is analytically redundant. If b is below every minimal R point, then b<R and (b,d) is primal very-good. Otherwise pick r minimal in R with b incomparable r. Its downset difference from c2 is the chain {v<d<e}. If U_R(r) is a chain, c2,r form a mixed two-cycle. Otherwise R must be r<t,u with t incomparable u; then U(t)=U(u)=F and both lower-set differences are subsets of the chain {b<h}, giving a dual very-good pair. No degree or F-buffer assumption is required for this coverage proof.
