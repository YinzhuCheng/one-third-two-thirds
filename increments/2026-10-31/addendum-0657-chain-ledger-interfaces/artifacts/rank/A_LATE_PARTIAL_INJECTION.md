# A-single-defect late-c2 cancellation

## Scope
Any finite C2. Assume S=A\U(d)={s} and U(s) subset U(e), with full strict upper sets in P. No assumption e<F, b incomparable s, |A|=5, or bounded incomparability degree is needed. Put a=c1,x=c2,R=A intersect U(e).

Let E_A={v<a<s<d}, and define its late-c2 part
  E_L={v<a<s<d and some r in R satisfies r<x}.
For every source word simultaneously swap (a,d) and (s,e), fixing all other labels. This is an injection E_L -> G, where G={v<d<e<a and some r in R lies before x} is the existing reverse bad event.

## Legality
In a source word, a<s<d<e<r<x for the chosen r, and v is first. The new d takes old a's position, new e takes old s's position, new a takes old d's position, and new s takes old e's position.
- d moves earlier and its sole strict predecessor is v.
- e moves earlier and its strict predecessors are v,d, which remain earlier in their new positions.
- a moves later to old d. All A\{s} are above d by the singleton-defect assumption. New s is at old e, after old d. Also x is after r>e>d, and every F point is above x. Thus every successor of a remains after its new position.
- s moves later. It has no A predecessor: every other A point lies above d, and such a predecessor would force d<s. Its only possible predecessors besides v,a are b, which was already before old s and hence before new s. All successors of s remain later because U(s) subset U(e) and old e precedes all U(e).
The r<x witness is unchanged, so the image is in G. The fixed label permutation is an involution, hence injective.

## Exact image and exact residual ledger
The image is precisely the following subset G_A of G:
  a<s;
  s<u for every u in U(e);
  b<e if b<s is a relation of P.
All displayed comparisons defining events are word-order comparisons; U(e) and the conditional b<s are fixed poset data.

Necessity follows directly from the source order: old d<old e, old e<U(e), and b<old s when b<s in P. For sufficiency, apply the same permutation to a word in G_A. The existence of r<x with a<r ensures x>a, so delaying d to old a preserves all d successors in A and F. Delaying e to old s is legal by s<U(e). Moving s earlier to old e preserves its b predecessor by b<e and its a predecessor because new a is old d; its successors remain later since U(s) subset U(e) and old e<old a<old s<U(e). Thus the inverse is a valid E_L word.

Consequently E_L and G_A have exactly equal unconditioned mass. Put
  E_A^early={v<a<s<d and x<every r in R},
and retain the original F failure event
  E_F={v<a<x<d and some z in F\U(e) is before e}.
E_L is disjoint from E_F, since its r<x witness forces d<x. Therefore the signed ledger refines exactly to
  2p_d=1+q0+Pr(E_A^early union E_F)-Pr(G\G_A).
In particular
  p_d <= [1+q0+Pr(E_A^early union E_F)]/2.
This is a partial compensation, not a universal control of the remaining error. If R is empty, E_L=G_A=empty and no improvement is claimed.

## Nonredundancy check, limited to named static filters
The rank-budget witness `candidate.json` satisfies U(s) subset U(e), has A5 and Delta9, and has no primal/dual very-good pair, no S112 mixed cycle, and no proper nontrivial autonomous module. Its exact counts are E_A=1750, E_L=G_A=680, E_A^early=1070, G=12943, N=117501. Thus the partial cancellation has a nonempty application beyond those static filters. It does not itself prove a new complete domain: the original unsigned error budget also closes on this particular finite instance. It is a structural lemma, not a claim of full residual classification or novelty against all literature.
