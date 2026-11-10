# Exact deletion-window rank gap: a parameter-uniform one-event bound

2026-11-10. Author derivation; independent review PASS in RANK_GAP_INDEPENDENT_REVIEW.md. This is an application of the original legal-insertion-window law, not a novelty claim or a whole-D9 proof. All probabilities refer to one fixed original P.

## RG1. Statement

Let x||y in a finite poset P, and suppose the full strict downsets satisfy D(x) subset D(y). Write d=d_inc,P(x). If D(x) is nonempty, put

    r=min_(a maximal in D(x)) |{z: a<z<y}|.

If D(x) is empty, put r=|D(y)|. Then

    Pr_P(x before y) >= (r+1)/(d+1).                  (RG1)

The inequality requires no degree, width, NB, memory, or exterior assumption. It gives a lower bound in one direction, not unconditional balance by itself.

## RG2. Exact original-word proof

Delete x from a full word and fix one actual extension sigma of P minus x. Number its positions1,...,N-1, where N=|P|. Let L be the position of the last predecessor of x (0 if absent); let R be the position of its first successor (N if absent); let j be the position of y. Its legal x insertion gaps are exactly

    L,L+1,...,R-1, with n_sigma=R-L.

Each insertion gives one original extension. The induced deletion-word mass is n_sigma/e(P), not uniform on sigma. The conditional event probability is exactly

    min(max(j-L,0),n_sigma)/n_sigma.

Every letter strictly between L and R is incomparable with x, so n_sigma<=d+1. If D(x) is nonempty, its last predecessor a is maximal in D(x). Every z with a<z<y appears strictly after a and before y. Such z is incomparable with x: z<x would contradict maximality of a, while x<z would imply x<y. The same is true of all predecessors of y when x is minimal. In either case at least r such incomparable letters precede y after the insertion-window start.

Since D(x) subset D(y), y is after L. If y is before R, it therefore has at least r+1 insertion slots before it, giving conditional probability >=(r+1)/(d+1). If y is after R, that probability is1. This also dominates the claimed bound, because the r interval letters together with y are distinct incomparable partners of x; thus r+1<=d. Multiply by n_sigma and sum over the same original deletion words. This proves RG1 with the true completion weights and no NB statement on a helper.

## RG3. Sharpness of the two-parameter statement

For every m>=1 and0<=r<=m-1, take a chain of m labels with y at rank r+1 and add an isolated x. Then D(x) is empty, d=m, and x has m+1 equally counted insertion slots, exactly r+1 before y. Equality in RG1 holds. To obtain a nonempty D(x), add one forced initial a below x and the entire chain. Then D(x)={a}, the interval count remains r, and the same equality holds.

Hence no universally larger lower bound can follow from (d,r) alone. Additional original-P incidence or completion information would be needed for a stronger statement.

## RG4. Source application and exact degree from memory

For an original ideal Q, both full downsets D(x),D(y) and the interval counts used in r are already inside Q. If x has no exterior incomparable, then d is its EXACT internal degree d_Q(x). Such exhaustion follows from genuine permanent pivot memory, terminality of the current pivot, or saturation of its degree budget, not a zero seen in only one word.

The source state

    pred=(0,0,1,1,7,23,23)

has labels a,b,u,v,t,s1,s2. The full marked relations include a<u,v; a,b,u<t; and t<s1,s2. On the two terminal-v references

    (0,1,2,4,3,5,6), (0,1,2,4,3,6,5),

take x=v, y=t. Full D(v)={a}, D(t)={a,b,u}. The only interval element above a and below t is u; b is incomparable with a. Thus r=1. Exhausted-v memory gives exactly d=5, namely the five physical partners b,u,t,s1,s2. RG1 yields

    Pr_P(v before t)>=2/6=1/3.

The source reference places t before v, so this one-event bank contradicts ORIGINAL NB. It does not need a degree cap on any other label, and it is not an NB assertion on a conditioned law. Both charged labels have at most three full predecessors.

## RG5. Mapping and de-duplication

RANK_GAP_CENSUS.py structurally scans the original packet. It checks reversed incomparable pairs, full-downset inclusion, r, and a justified degree upper bound. With no exhaustion it uses the original local degree9 bound; with actual exhausted memory it uses the exact internal degree. Endpoints are restricted to full predecessor count<=8 to preserve M8 locality.

The census finds11 existing source bank occurrences satisfying RG1 at threshold1/3. Nine are already in the402-row analytic union. Only the two terminal references in RG4 are new. RANK_GAP_INDEPENDENT_REVIEW.md and its separately written source reconstruction audit these counts and decode the old source singleton bank as the event v<t. The resulting pure analytic union is404, leaving3065 original source occurrences unchanged. The previous two Q8 finite-symbolic rows have been PROMOTED to analytic by Q8_COMPLETE_ANALYTIC_PROOF.md; they are not counted again here. No source phase route or other certificate is altered.
