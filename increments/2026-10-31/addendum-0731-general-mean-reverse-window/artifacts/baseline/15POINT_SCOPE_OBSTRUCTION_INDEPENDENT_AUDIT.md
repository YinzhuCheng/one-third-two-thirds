# Independent audit: scope obstruction and necessary prefilter

Verdict: the reasoning in `15POINT_SCOPE_OBSTRUCTION.md` is valid.

For any full K containing L and cross-incomparable with M, a point in D_Q(M)\\M cannot lie in K, so it must lie in the external set R. The assumed external lower inclusion forces it below every point of K, hence below every L point. This proves the first necessary prefilter.

For the upper prefilter, a successor of L outside L cannot lie in K\\L because L is an upper ideal in K, and cannot lie in M because K and M are cross-incomparable. It lies in R and the external upper inclusion forces it above every M point. This second prefilter explicitly depends on the upper-ideal assumption; it must not be copied unchanged into a later theorem that permits arbitrary L without checking that condition.

I independently recomputed the 15-point example's transitive closure from `free_residual_obstruction_verified_local.json`: e<f0, while e and a1 are incomparable. Since M={f0} and a1 is in the full L, cross-incomparability forces e outside K and hence into R, immediately violating the lower inclusion. No choice of additional anchors, internal K shape, or comparison capacity can repair this within the stated uniform-window interface. The lower obstruction does not require L to be an upper ideal and therefore also remains applicable to any broader arbitrary-L theorem retaining the same lower and cross-incomparability hypotheses.

This proves non-applicability of this family of sufficient conditions, not failure of the balanced-pair conjecture. The previously independently verified B=12891,Z=9101 and net/menu budgets remain consistent, but are not needed for this structural exclusion.

Only this /tmp receipt was created; no repository or remote was changed.
