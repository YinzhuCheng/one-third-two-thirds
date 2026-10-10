# Independent audit of the two-dimensional logconcave square-transfer lemma

## Verdict

**The analytic inequality is valid for the entire stated class.** This is stronger than a statement restricted to order-polytope fibers. The Busemann–Ball radial-body reduction and supporting-triangle argument have no gap in normalization, reflection, zero support, or zero supporting coefficients. The audit below is independent of any combinatorial reduction to this lemma; that reduction needs its own verification.

Let f: [0,∞)^2 → [0,∞) be measurable, coordinatewise nonincreasing, logconcave, and integrable. Define

- H = ∫₀∞ t f(t,t) dt;
- U = ∫_{0≤s<t} f(s,t) ds dt and L = ∫_{0≤t<s} f(s,t) ds dt;
- Ru = U − H and Ry = L − H.

Then H² ≥ Ru Ry. All these quantities are finite and nonnegative. The second wing in the question equals L−H after swapping s and t.

## External theorem checked directly

Keith Ball, “Convex geometry and its connections to harmonic analysis, functional analysis and probability theory,” Proceedings of the ICM 2022, volume 4, pp. 3104–3139, Theorem 3 on p. 3108 (PDF page 5): for any even logconcave F with finite positive integral and p≥1, x ↦ (∫₀∞ F(rx)r^(p−1)dr)^(−1/p) is a norm. No continuity, smoothness, or full-support hypothesis is stated.

- Survey DOI: https://doi.org/10.4171/ICM2022/65
- Publisher PDF, directly read and visually checked: https://ems.press/content/book-chapter-files/33237
- Original paper: Keith Ball, “Logarithmically concave functions and sections of convex sets in R^n,” Studia Mathematica 88 (1988), 69–84, https://doi.org/10.4064/sm-88-1-69-84

The PDF’s text extractor drops the minus sign in the exponent; the rendered page visibly has −1/p. Local source and page image are `ball_2022_survey.pdf` and `ball_theorem_3.png`.

## Self-contained application and geometric proof

1. Coordinate monotonicity gives f(s,t)≥f(t,t) on 0≤s<t. Integrating proves U≥H. The corresponding lower-sector argument gives L≥H. In particular H is finite.

2. If ∫f=0, then f(t,t)=0 for every t>0: otherwise f is bounded below by f(t,t)>0 throughout [0,t]^2. Thus H=U=L=0 and the result is trivial. Henceforth ∫f>0. There is a positive value f(s₀,t₀) with s₀,t₀>0, which implies H>0 by the same rectangle argument.

3. Set F(x₁,x₂)=f(|x₁|,|x₂|). For 0<λ<1,

   |λx+(1−λ)y| ≤ λ|x|+(1−λ)|y| coordinatewise.

   Coordinate monotonicity followed by logconcavity therefore yields

   F(λx+(1−λ)y) ≥ f(λ|x|+(1−λ)|y|) ≥ F(x)^λ F(y)^(1−λ).

   Thus F is logconcave, even, and in fact unconditional. Its total integral is four times that of f, so Ball’s theorem applies.

4. Use the unnormalized radial construction

   q(x) = [2∫₀∞ r F(rx) dr]^(−1/2),   K={x:q(x)≤1}.

   Ball’s theorem with p=2 makes q a norm multiplied by a positive constant. Consequently K is a compact, convex, unconditional body with the origin in its interior. This construction deliberately avoids division by f(0).

5. For every unit direction θ,

   ρ_K(θ)^2 = 2∫₀∞ rF(rθ)dr.

   Polar-coordinate integration therefore gives, for every measurable cone C,

   area(K∩C)=∫_C F(x)dx.

   In particular the upper- and lower-quadrant sector areas of K are U and L. No Euclidean √2 factor is missing: on the diagonal q(a,a)=a/√(2H). Hence the unique positive diagonal boundary point is (a,a), where a²=2H.

6. Take a supporting line at (a,a):

   αs+βt ≤ a(α+β) for every (s,t)∈K,

   with (α,β)≠(0,0). Unconditionality puts (−a,a) and (a,−a) in K. Substitution gives α≥0 and β≥0. This does not require a smooth boundary or a unique supporting line.

7. If α,β>0, the positive-quadrant portion of K lies in the triangle

   T={s,t≥0 : αs+βt≤a(α+β)}.

   The upper sector of T has vertices (0,0), (a,a), (0,a(α+β)/β), and thus area a²(α+β)/(2β). The lower sector similarly has area a²(α+β)/(2α). Since H=a²/2,

   0≤Ru=U−H≤αa²/(2β),
   0≤Ry=L−H≤βa²/(2α).

   Multiplication gives RuRy≤a⁴/4=H².

8. Zero coefficients cause no division problem. If α=0, then β>0 and K lies in t≤a. Its upper-quadrant sector lies in 0≤s<t≤a, of area a²/2=H, so U≤H. Together with U≥H this gives Ru=0. If β=0, the analogous lower-sector argument gives Ry=0. Both cases satisfy the desired inequality.

This completes the proof for the whole analytic class, including uniform indicators of convex downward sets.

## Exact falsification/regression checks

The accompanying Python script uses `fractions.Fraction` throughout its polygon checks; there is no floating-point sign decision.

- 5,000 random convex downward rational polygons, with exact halfspace clipping and shoelace areas: no violation. There were 2,855 exact equalities and 302 zero-wing cases.
- 5,000 homogeneous potentials V(s,t)=max_i(a_i s+b_i t), all a_i,b_i positive integers, with f=e^(−V): no violation, including 2,099 exact equalities. Their three masses are twice those of the indicator of the unit sublevel polygon, by homogeneity.
- 961 product-survival examples f(s,t)=(1−s)^m(1−t)^n on [0,1]^2 and zero outside, 0≤m,n≤30: no violation, by the exact formulas

  H=1/[(m+n+1)(m+n+2)],
  Ru=[m/(n+1)]H,
  Ry=[n/(m+1)]H,
  H²−RuRy=H²(m+n+1)/[(m+1)(n+1)]>0.

These are bounded regression checks, not evidence needed to close the proof.

### Nonhomogeneous max-affine check with exact integrals

Take V(s,t)=max(2s+t,s+2t−1). Every affine form has strictly positive coefficients, and V is convex and coordinatewise increasing. On the diagonal V(t,t)=3t, hence H=1/9. On s>t, V(s,t)=2s+t, giving L=1/6 and Ry=1/18. On s<t, the switching line is s=t−1. Splitting at t=1 yields

U = ∫₀¹ e^(−t)[1−e^(−2t)]/2 dt
    + ∫₁∞ [e^(1−2t)−e^(2−3t)/2−e^(−3t)/2]dt
  = 1/3−1/(6e).

Therefore Ru=2/9−1/(6e), and H²−RuRy=1/(108e)>0 exactly.

### Sharpness

For f(s,t)=exp(−as−bt), a,b>0,

H=1/(a+b)²,  Ru=a/[b(a+b)²],  Ry=b/[a(a+b)²],

so equality holds. More generally, f(s,t)=φ(as+bt) has equality whenever it belongs to the stated class and has positive finite integral. Thus the constant 1 cannot be improved.

## Scope warning

The proof concerns decreasing logconcave f. It does not by itself verify the poset-to-fiber formula or identify H, Ru, and Ry with particular linear-extension counts. Those identifications remain separate, even though the analytic class is broader than the intended order-polytope application.

## Reproduction

Run `python check_logconcave_exact.py` from any directory. The script writes `exact_checks.json` next to itself, with deterministic seed 109002. There were 10,961 rational/formula checks, plus the explicit nonhomogeneous example.
