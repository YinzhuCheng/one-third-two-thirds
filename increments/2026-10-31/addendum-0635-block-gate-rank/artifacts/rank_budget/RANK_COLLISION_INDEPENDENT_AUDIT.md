# Independent audit of first-target collision correction

Verdict: **valid**, under the original structural assumptions 1–3, replacing the original endpoint test by the corrected endpoint test. No new global/nonredundancy claim follows automatically.

1. Suppose α<β. If I<J, I cannot be the final sentinel, because no deadline exceeds that sentinel. Thus F is nonempty and position I contains its first actual letter. Since e<F, I≥H; since F∩R=∅, this is one non-R letter in [H,J−1]. If U(s) is nonempty, the first such target has β distinct R-predecessors in that same interval. If it is empty, J is the sentinel and all |R|≥β R-letters lie in that interval instead. In either case J−H≥β+1. The finite/sentinel distinction is fully covered; the extra position cannot be accidentally counted among R-predecessors.

2. Separate strict monotonicity of D in I,J on I,J>H gives
D≤D(H,H+α,H+β+1).
Because α<β, increasing J from H+β to H+β+1 does not change min(I,J)=I. The change is 4H−4I=−4α, exactly the claimed correction.

3. If I≥J, the β-budget implies both I,J≥H+β. Thus D≤f_{β,β}(H). With δ=β−α≥1, the difference from the proposed bound is
(f_{α,β}(H)−4α)−f_{β,β}(H)
=δ(2H+4β+4)−4α
=2δH+4α(δ−1)+4δ²+4δ
≥2H+8>0.
This case includes I=J and F empty, including the possibility that both deadlines are the final sentinel. No ordering case is omitted.

4. For α≥β the original bound is retained, not improved. The corrected polynomial has leading coefficient 2, so the same convex endpoint argument applies for k≥0, including the singleton interval k=0. The b-nonfirst branch is unchanged. Strictly negative endpoints make every b-first fiber negative; an actual nonempty such fiber exists, giving the stated strict unconditional bound. A zero endpoint is sufficient only for the weak conclusion under the stated argument. For (α,β,k)=(1,3,1), the endpoints are indeed −13 and −2.

5. **Sharpness of this fiber bound:** for any integers 1≤α<β and k≥0, take R={r1,…,rβ}, K={h1,…,hk}, F={f1,f2}. Generate a finite poset by
v<b,d; a<x,s; a<hi and d<hi for all i; d<e; e<rj and a<rj for all j; b<s; x<f1,f2; rj<f1 for j≤α; rj<f2 for all j; s<f2.
No other generating relations are imposed. It satisfies complete C2 with c1=a,c2=x, A={s}∪K∪R, and its maximal separate budgets are α and β. The actual external word
b,h1,…,hk,r1,…,rα,f1,r_{α+1},…,rβ,f2
has H=k+1,I=H+α,J=H+β+1. Consequently D=f_sharp(H) exactly. Failure of the corrected endpoint criterion can therefore obstruct uniform nonpositivity of all fibers; it does not disprove the global inequality. This construction makes no claim about passing other old filters.

Editorial recommendation: replace “Retain every hypothesis” with “Retain structural hypotheses 1–3 and replace the endpoint hypothesis 4 as follows,” so that the new theorem is not accidentally written as also requiring the old endpoint test.

Audit performed entirely in /tmp; no repository changes.
