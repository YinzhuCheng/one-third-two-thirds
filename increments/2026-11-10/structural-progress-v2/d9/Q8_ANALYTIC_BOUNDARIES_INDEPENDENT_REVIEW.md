# Independent audit: explicit Q8 analytic boundary closure

2026-11-10. PASS for the source 15/3/2/2/1 bank on original integer deadline caps. This audit covers the concrete polynomial identities and inequalities in Q8_EQUAL_MAX_FACE_ANALYTIC.md, Q8_MIDDLE_TIE_BOUNDARY.md, and Q8_SATURATED_FACE_REDUCTION.md, together with the already audited integer discriminant branches. It does not rely on the signs of the historical 1,512 or 81 Bernstein coefficients.

## Reconstructed identities

The independent scripts take the exact reduced chamber polynomials from the source JSON. Those polynomials were previously reconstructed independently by flagged-chain determinants and direct sixty-word insertion counts in Q8_SYMBOLIC_INDEPENDENT_REVIEW.py; neither route needs the Bernstein coefficients to define them.

- Q8_EQUAL_MAX_INDEPENDENT_IDENTITIES.py verifies 52 exact identities: the seven equal-maximum representatives; A/B/C formulas; endpoint formulas J,L,E; derivative identities; and the displayed nine-term positive identity for E0's negative discriminant.
- Q8_MIDDLE_TIE_INDEPENDENT_IDENTITIES.py verifies 47 identities, the seven cubic coefficient rows, duplicate chambers, left/right endpoints, complete integer-t case coverage, and the eleven explicit coarse bounds.
- Q8_SATURATED_INDEPENDENT_IDENTITIES.py verifies all twelve r-affinities and fifteen identities for the quadratic classification, case-four linear coefficient, and the two right-derivative reductions.

The companion JSON files record PASS. These scripts check displayed algebra; they do not provide an additional sampled-profile positivity assumption.

## Equal-maximum face: inequality audit

EM2's integer coverage is complete. For representative zero, t>=2 gives negative A; the two remaining integer t values split into p=0 (positive A,B) and integer p>=1 (negative A). Representatives 2,4,9 split at integer t<=4 or t>=5. Their continuous endpoint bounds on -B are valid: after u^4<=16u^2 and u^3<=4u^2, the final bounds are exactly -1901u/4-980 and -1425u/2-20. The B9-B2 correction is nonnegative. Representative six splits at t<=2 or t>=3; the lower bound -t^3+405t^2-828t-1108 is 26 at t=3 and increases thereafter. Representatives eight and eleven have B>0 through t=5; t=6 has no remaining interval. Thus no integer (t,p) is omitted. No continuous extension across those integer thresholds is required.

EM3's cubic derivative argument is correct. A derivative quadratic with positive constant and negative leading coefficient has exactly one positive root, hence gives a maximum rather than an interior minimum; with negative quadratic and cubic coefficients the derivative decreases. The displayed C0 coefficient signs cover their ranges. The C6 and C9 coefficient lower bounds are positive on the stated intervals, and their remaining integer slices are explicitly handled. L's cubic bracket is at least 383/20, and its first three terms are at least 22428/5. Z is positive by the convex quadratic's two negative endpoint values.

EM4's univariate bounds hold as stated. In particular J0's R derivative is negative, R(6)=-471/10, and its final lower bound is 912. J8's B derivative is negative on each of [0,4] and [4,6], B(6)=-585, and the final lower bound is 3474. N2 is convex (its decreasing second derivative remains >=858) and N4 is convex; their endpoint values are respectively (-65760,-34920) and (-4275,-4365).

For E6, the derivative's vertex comparison reduces to 14t^3-141t^2+713t+790>0, and its right derivative to (7t^3-72t^2+347t+384)/2>0; both claimed derivative-discriminant arguments are valid. E9's p derivative is concave because its p-cubic coefficient is -3t^2-19t-22; both derivative endpoint functions are concave in t and positive at their endpoints. E11's derivative vertex is 7-t, with positive quadratic leading coefficient; hence it decreases through the relevant interval, and its right value has the stated positive lower bound. E8's high coefficients are positive; its auxiliary Q is concave and positive at both endpoints. Finally, the nine fully displayed positive integers in 33592320D=sum c_j t^j(6-t)^(8-j) reproduce D exactly and make it strictly positive even at t=0 and t=6. This is an explicit nine-term identity, not an appeal to the former coefficient tables.

Consequently the r=0 face is proved on its stated integer domain without either historical Bernstein sign certificate.

## Saturated q=0 face and full saturated classification

All seven cubic rows in Q8_MIDDLE_TIE_BOUNDARY are correct. The derivative endpoint mechanism a<0,c>0 is valid on the nonnegative axis. Its integer slices, the decreasing t=5 slices, the nonnegative-coefficient slices, and the eleven explicitly bounded slices together cover all seven representatives for t=0,...,5. At t=6,p=0 every value is 6984. The eleven coarse bounds reproduce their stated constants exactly. The G1/G3 concavity argument is valid; G0's upward quadratic derivative starts positive and ends negative, so on [0,6] it cannot create an interior minimum of G0. The right endpoint depends only on the already independently closed r=0 face. There is no circular use of the saturated-face theorem.

On the general saturated face, the four linear cases and five concave cases have the stated signs. For A8 the two p endpoint bounds are negative, and for A11 both parts are negative. Case four has positive A and positive B; the two displayed quadratic factors proving B>0 have negative discriminants. Cases zero and six have A>0. At t>=4, putting x=t-4 in [0,2] gives the stated negative right derivatives; the bounds x^3<=4x, x^4<=4x^2, and x^3<=2x^2 justify the reductions. For integer t=0,...,4, the positive H0/H6 proofs in Q8_INTEGER_DISCRIMINANT_REVIEW.md apply. The overlap at t=4 is harmless. The residual endpoints are precisely r=0 and saturated q=0, now both closed.

## Composition and scope

Original caps are integers. Taking the r endpoints preserves integrality of t,p,q; taking the saturated q right endpoint gives q=6-t-p, also an integer. Thus the integer-only r=0 lemma is sufficient at every place it is used. The cubic q=0 argument allows real p, so it is stronger than needed there. No step infers continuous-t positivity from the finite set of integer-t inequalities.

The resulting dependency order is: exact original-word counts and analytic root compression; r=0 face; saturated q=0 face using r=0; saturated interior classification plus integer discriminants; affine-r endpoint reduction. Combined with the already audited original-P contract, this proves the source bank without the 1,512- or 81-coefficient positivity dependencies. Those historical certificates remain valid independent corroboration. This review does not itself remap source rows; the final coverage audit must retain the exact Q8 ideal, exhausted-v memory, fixed physical events, and the two designated first-head references.
