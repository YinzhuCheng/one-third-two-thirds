# T13 rank-budget extension (proof draft; independent review requested)

## Scope and status
This is a structural extension of the existing T13 fiber proof, not a second independent mechanism and not a claim of historical novelty. It does not solve all C2. All work is in `/tmp`; the repository and remotes have not been changed.

Use the complete C2 definition from the authoritative 2026-10-31 entry: v is minimal, I(v)={c1<c2}, U(v)\U(c1)={b} disjoint union {d<e}, A=U(v) intersect U(c1) minus U(c2), F=U(c2). Write q0=Pr(c1<v), p_d=Pr(c1<d), under the uniform law on all linear extensions of P.

Assume:
1. A\U(d)={s}; b<s; e<F.
2. R=A intersect U(e), K=A\({s} union R), k=|K|.
3. Integers alpha,beta>=1 satisfy
   - every f in F has at least alpha distinct predecessors in R;
   - every u in U(s) has at least beta distinct predecessors in R.
   Empty target sets are allowed provided alpha<=|R|, respectively beta<=|R|. Thus define the maximal safe values
   alpha=min({|D(f) intersect R|:f in F} union {|R|}),
   beta=min({|D(u) intersect R|:u in U(s)} union {|R|}).
   Here D,U are full strict sets in P. Different targets can use different R predecessors; no common anchor is required.
4. Let
   f(H)=2H^2+(7-2alpha)H-4alpha beta-4min(alpha,beta).
   Suppose max(f(1),f(k+1))<=0.

Then p_d<=(1+q0)/2. If both endpoint values are negative, the inequality is strict. The inherited C2 universal bounds q0<=2/3 and p_d>=1/3 give the existing fixed-menu corollary {(c1,v),(c1,d)}. The inequality itself does not depend on those auxiliary bounds, on |A|=5, or on an incomparability-degree bound.

The old T13 common-m-anchor theorem implies alpha,beta>=m and is a corollary. The extension is genuinely weaker: targets may have sufficient R-rank without sharing their predecessor sets.

## Fiber proof, with actual weights preserved
On v<c1, v is necessarily first. Delete v, put a=c1,x=c2,y=e, and retain core {a,d,x,y,s}. The only core relations are a<x,s and d<y; the sole external predecessor of a core point is b<s. All A\{s} and all F are above a,d. The other external set is O={b} union K union R union F. Fix an actual linear extension w of P[O]. We sum its insertion fiber cardinality, never assigning equal probability to different w.

For a fixed external word, gap j is immediately before its j-th letter; the final gap is |O|+1. A point with first required external successor at position j can occupy initial gaps 1,...,j. Empty upper sets use the final gap.
For two independent labels with deadlines i,j, write W(i,j)=ij+min(i,j). For an interval C of allowed gaps, write W(C,j)=j|C|+|C intersect [1,j]|.

### b not first
Let b occupy external position B>=2 and let H,I,J be the y,x,s deadlines. Both a,d must precede the first external letter; s has allowed gaps C={B+1,...,J}. Because e<F, every x successor is a y successor and I>=H. Cancel words with initial a,d versus d,a by swapping those labels. The only remaining positive prefix is a,x,d; the only remaining negative prefix is d,y,a. Their exact difference is
  D=W(C,H)-W(C,I)<=0.
No bound H<=k+1 is used in this branch.

### b first
Delete b from w to get w'. Let H,I,J now denote the deadlines in w'. Only the k labels in K fail to be above y. Consequently 1<=H<=k+1.

Consider the first F letter, if any. Its alpha distinct R predecessors occupy distinct positions from H through I-1, since no R occurs before the first y successor. Thus I>=H+alpha. If F is empty, all |R| R labels occur before the final sentinel, giving the same bound. Likewise, the first letter of U(s) has beta distinct R predecessors in positions H through J-1, or all R precede the sentinel if U(s) is empty. Hence J>=H+beta. This is the sole new structural step: it uses predecessor counts, not a globally fixed set of anchors.

Retain the exact existing T13 insertion identity, whose complete prefix derivation is included here. After canceling adjacent starting a,d and d,a, the remaining core prefixes and their b-weighted counts are:
  a x d:   3W(J,H)+B(J,H)
  a s d:   2W(I,H)
  a x s d: 3H
  a s x d: 2H
  d y a:  -3W(I,J)-B(J,I).
Here B(J,t) counts insertion of b,s,z after the listed prefix with b before the first external letter, b<s, and s,z deadlines J,t. Its initial labels must be b or z,b, so B(J,t)=W(J,t)+J. The extra J terms cancel. Therefore
  D=4W(J,H)+2W(I,H)+5H-4W(I,J)
   =4HJ+2HI+11H-4IJ-4min(I,J),
because H<I,J. This expression is strictly decreasing separately in I,J when I>=H+alpha,J>=H+beta and alpha,beta>=1. Substitution gives
  D<=2H^2+(7-2alpha)H-4alpha beta-4min(alpha,beta)=f(H).
Since f is convex, its maximum over [1,k+1] is attained at an endpoint. The stated condition therefore gives D<=0 for every actual fiber.

If both endpoint values are negative, every nonempty b-first fiber has D<0; such a fiber exists because b is minimal in the external induced order. Summing actual fibers proves Pr(a<d | v<c1)<=1/2, strictly in that case. On c1<v, necessarily c1<d, hence the claimed unconditional inequality.

## Useful A5 case and nonredundancy boundary
For |A|=5, k=1, |R|=3, alpha=beta=2 gives f(1)=-19,f(2)=-10. The pair (alpha,beta)=(3,1) also suffices, giving -13,-6. The asymmetric choice (1,3) does not follow: f(2)=2. Failure of this fiber bound is not a theorem counterexample.

A 15-point witness is `candidate.json`: start from the recorded E16 generating relations, remove t<f0, and add u<f0. Its exact validation is `candidate.json.checked.json` and reproducible with `python check.py candidate.json`.
- C2, A={s,r,t,u,w}, R={r,t,u}, K={w}, e<F, b<s.
- Every F and every U(s) target has two R predecessors; their profiles are {r,t} or {r,u}. Only r is a common anchor, so old T13 m=1,k=1 is outside its stated bound and m=2 is unavailable.
- Delta=9; no primal/dual very-good pair; mixed forcing graph acyclic; no proper nontrivial autonomous module.
- N=117501, R0=33398, Kcount=#(c1<d)=69853, E=1750, G=12943, E-G=-11193.
These are finite applicability checks and a witness separating old and new hypotheses, not the general proof. The old unsigned error budget also holds in this instance (1750 < N/3-R0=5769), so do not claim every previous tool fails. Historical and literature overlap remain unverified.
