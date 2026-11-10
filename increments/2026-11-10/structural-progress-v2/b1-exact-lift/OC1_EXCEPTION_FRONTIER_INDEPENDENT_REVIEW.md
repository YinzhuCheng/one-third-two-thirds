# OC2 independent mathematical review

2026-11-10 UTC. PASS for corrected OC1_EXCEPTION_FRONTIER_AND_ASYMMETRIC_SIDE_REDUCTION.md SHA256 35d6799cec175a6e51f89abd11282fb4f17ea6e678648960ca87e0dd0331759e. Nonblind internal independent review; I did not derive the submitted exception-frontier/side reduction. Not external peer review, formal verification or novelty certification. No object scan or computation was needed.

## Actual finite frontier
OC1 gives g's complete C predecessor set D as a nonempty E ideal, and every W point above f,x. Thus no W point lies below g. An E point outside D cannot be above g because E is an ideal, so it is incomparable with g. Together with f and J this exhausts the full incomparability neighborhood of the full-signature g; all outside-C labels are comparable. Hence deg(g)=1+(6-|D|)+|J|, and J<=|D|+3<=9 is exact.

If a W predecessor of a J point lay above g, so would that J point. Thus J is a W ideal. E, f, g have no missing predecessors outside the stated union, and a predecessor of J can only be in E, f, or J. Therefore K=E union{f,g} union J is an actual C ideal of size<=17. Every remaining point lies above both f,g and inherits full xyz signature. No relation of this tail to E-D or J is silently strengthened.

## Actual sides and degree saturation
A,B lie in J because E,g are common-root successors, f has neither root, and all tail points are full. Each A label is above x,f and has signature xy. Its original incomparable neighbors include E6,g,z,B and its internal A neighbors, giving deg_A<=2-|B|. If A has a two-antichain and B is nonempty, E6,g,z plus one B point provide nine common incomparable blockers, and the opposite endpoint fills degree10. Remaining labels outside the pair AND those blockers compare in a common direction, so the pair are full exact twins. Extra B points would violate Delta10. This proves the one-empty-opposite conclusion outside twins/rootVG.

The three-antichain saturation gives width<=2. The actual z degree charges four outside-C labels plus f and all A, so |A|<=5, with any additional x-only points only tightening this bound. LG1 supplies an internal candidate, not automatic original payment, as the manuscript correctly emphasizes.

## Two local corrections and final scope
The initial saturation wording could include its common blockers among 'every other point'; I requested their explicit exclusion. The revised source states they remain incomparable. I also requested removal of E from the list of potential distinguishing ports: E is uniformly incomparable with every A/B label, exactly as used in the degree proof. The corrected source now says only other J or full-tail labels may distinguish and explicitly notes E cannot be active. Both corrections are present in the frozen hash.

The theorem is a genuine original-structure interface, not an unweighted finite-core probability law. It does not remove a long uniform/asymmetric tail, grant inherited moment or assert that the remaining port requirements can coexist while avoiding every guard. All nonempty-exception probability claims remain open. The submitted corrected result passes within this precise scope.
