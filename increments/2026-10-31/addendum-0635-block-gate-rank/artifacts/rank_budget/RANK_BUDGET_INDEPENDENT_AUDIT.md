# Independent audit: separate predecessor-rank budgets

**Verdict:** the stated sufficient theorem and its strictness claim are correct under the complete finite C2 hypotheses. No counterexample or missing probabilistic weighting was found. This audit first reconstructed the argument on paper; the independent finite ideal-DP checks below are supplemental, not the proof.

## Structural and quantifier checks

- Under C2, the vertices partition as `{v,c1,c2,b,d,e} ⊔ A ⊔ F`. On `v<c1`, v is first. Write a=c1,x=c2,y=e. The five core vertices have exactly a<x,s and d<y. Every other A point is above d; consequently none can precede s. Neither A nor F can precede a,d,x,y. Thus b<s is indeed the sole external-to-core restriction.
- The external successors of a,d are K∪R∪F; those of y are R∪F, those of x are F, and those of s are its full strict upper set U(s), contained in the external set. All additional external relations are retained by fixing an actual external linear extension.
- The rank conditions are universal over individual targets and existential over their predecessor sets: for each target f or u separately, its R-predecessor set has the required cardinality. Intersections between different targets' predecessor sets are not needed.
- If F or U(s) is empty, its deadline is the final gap, not zero or infinity. The explicit cap by |R| makes the rank argument valid in this vacuous case. A nonempty target automatically gives the same cap. If R is empty, no α,β≥1 satisfy the assumptions: the theorem does not inadvertently cover that case.

## New rank argument

In a b-first external word, delete b. Every letter before the first y-successor belongs to K, so 1≤H≤k+1. Every R-letter is a y-successor and therefore occurs at position at least H. For the first F-letter at position I, all its α distinct R-predecessors occur in the I−H available positions H,…,I−1. Therefore I≥H+α. No common anchors, ordering between those α vertices, or assumption about earlier F-targets is used. If F is empty, all |R| R-letters occur before the sentinel I; the same proof applies. Identical reasoning for the first U(s)-letter yields J≥H+β, including the empty case. A target belonging to R cannot count itself because D is strict; the argument remains valid.

## Exact fiber calculation reconstructed

For two remaining independent labels, assigning their gaps gives ij choices, with a second ordering exactly when both use the same gap: W(i,j)=ij+min(i,j). With s restricted to C, the analogous count is W(C,j)=j|C|+|C∩[1,j]|.

If b is not first, a,d precede the first external letter and s cannot do so. Swapping the first two projected core labels a,d cancels all such pairs. The only remaining projected prefixes are a,x,d and d,y,a; the remainder gives W(C,H)−W(C,I)≤0. Here e<F implies I≥H, including F empty. No upper bound on H is invoked in this branch.

If b is first, after deleting b the same cancellation leaves exactly five prefixes. For a,x,d there are three positions of b before d and, after d, B(J,H)=W(J,H)+J possibilities for b,s,y. For a,s,d there are two positions of b before s; for a,x,s,d there are three, and for a,s,x,d two. For d,y,a there are three positions of b before a and B(J,I) possibilities afterward. Thus the displayed weighted prefix formula is exact. In B(J,t), b is either first among the residual labels, or preceded only by z in the initial gap; these alternatives give W(J,t) and J. The J terms cancel. In particular these are counts in a fixed real fiber, not probabilities under a uniform external-word law.

## Algebra, sums, and edge cases

The difference is
D=4HJ+2HI+11H−4IJ−4min(I,J).
Its forward difference in I is 2H−4J minus either 0 or 4; its forward difference in J is 4H−4I minus either 0 or 4. Both are strictly negative since α,β≥1. Substituting I=H+α,J=H+β gives exactly
f(H)=2H²+(7−2α)H−4αβ−4min(α,β).
Convexity bounds f on the entire real interval [1,k+1] by its endpoint maximum, and hence bounds every integer H. The k=0 interval is a singleton and is covered. One vanishing endpoint is allowed for the weak conclusion; failure of the endpoint test does not disprove the global inequality.

All external fibers are summed by actual integer cardinality. Because b is minimal in the external induced poset, some external word begins with b; its insertion fiber is nonempty (for example prepend a,d,b and then place the other core labels before required external successors). Strictly negative endpoints therefore imply a strictly negative total difference. The conditioning event v<c1 is nonempty because v,c1 are incomparable. Finally p_d=q0+(1−q0)Pr(a<d|v<c1), giving precisely the claimed bound. No integrals or limit exchanges are involved.

## Comparison with the old theorem

If m common R-anchors lie below every point of F∪U(s), then both maximal budgets are at least m, including vacuous target sets. The new theorem may choose α=β=m. Under the old condition m≥2,k≤2m−3, f_m(1)=9−6m−4m²<0 and f_m(2m−2)=−2m−6<0; convexity supplies the new endpoint test. The separately recorded old m=1,k=0 case also has f(1)=−1. Thus the old sufficient theorem is genuinely contained in the new one; this is not just an informal comparison of individual hypotheses.

The supplied witness has target predecessor profiles {r,t} and {r,u}, so α=β=2 but the common intersection is only {r}. With k=1 it passes the new test (−19,−10) and cannot use the old m≥2 anchor hypothesis. This establishes strict enlargement of this structural sufficient domain, not separation from every previous numerical criterion and not historical novelty.

## Independent finite check

`audit_rank_budget_independent.py` builds the core/external-chain poset directly and computes signed extension counts by ideal DP, without calling the draft's insertion formula. It checks 196 b-first deadline configurations and 1,134 b-nonfirst configurations (external word lengths up to 7), including final-gap deadlines. Every count agrees with the independently reconstructed identity. This supplements, but does not replace, the unrestricted proof above. No repository files or remotes were changed.
