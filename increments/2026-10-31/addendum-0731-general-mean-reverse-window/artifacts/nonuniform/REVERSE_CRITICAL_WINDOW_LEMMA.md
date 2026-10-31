# Reverse critical-window obstruction, with a quantitative cutoff gap

Status: complete derivation submitted for independent review. This is a sufficient **reverse** comparison, not a positive forest-capacity theorem or a claim of novelty.

## 1. General statement and exact scope
Let Q be a finite n-point poset. Let L,C be disjoint subsets with a in L, and let M={m} be a singleton disjoint from L union C. Assume a and m are incomparable and
  D_Q(a) subset D_Q(m),  U_Q(m) subset U_Q(a).
Use complete strict sets. Define
  B=sum_{sigma in LE(Q)} first_sigma({m} union C),
  Z=sum_{sigma in LE(Q)} first_sigma(L union C),
with first(empty)=n+1.

Then **B>=Z**. There is no assertion of strictness without an additional cutoff condition: for example, a C element always preceding both targets makes the two first values equal.

## 2. Conditional proof preserving the real external measure
Set R=Q\{a,m}; C and L\{a} are contained in R. Fix a point t of the interior of the actual order polytope O(Q[R]). The removed incomparable coordinates are independent uniforms in their feasible intervals
  a in [l_a,u_a], m in [l_m,u_m].
The poset inclusions give l_a<=l_m and u_a<=u_m. All relevant intervals have positive length almost everywhere; transitive relations among retained R points ensure their lower endpoints precede their upper endpoints.

Let c=min_{x in C} t_x, with c=1 for C empty. Couple the two uniform *marginals* by a common U~Unif[0,1]:
  A(U)=l_a+(u_a-l_a)U,
  M(U)=l_m+(u_m-l_m)U.
Then A(U)<=M(U) for every U. This coupling is used only to compare their expectations; it does not claim the two actual coordinates are coupled this way in Q. Hence
  E[min(m,c)|t]>=E[min(a,c)|t]>=E[min(L union C)|t].

The actual marginal density of t is proportional to (u_a-l_a)(u_m-l_m), not the uniform measure on O(Q[R]). Integrating the displayed pointwise inequality against this actual density is legitimate. The standard simplex/order-statistic identity
  sum first(S)=(n+1)e(Q) E[min_{x in S} t_x]
then gives B>=Z. For nonempty S this follows by conditioning on a linear extension and using the mean of the rank-th uniform order statistic; the empty-set conventions agree.

## 3. Quantitative strictness when the cutoff survives the later lower gate
Suppose additionally, on a set of positive actual R-marginal measure,
  delta=l_m-l_a>0,  c>=l_m.
Write w_a=u_a-l_a>0. On the common-quantile coupling, where A(U)<l_m,
  min(M(U),c)-min(A(U),c)>=l_m-A(U).
Elsewhere the difference is nonnegative. Therefore the conditional difference is at least
  Psi(delta,w_a)=integral_0^1 (delta-w_a*u)_+ du
  = delta^2/(2w_a)                 if delta<=w_a,
  = delta-w_a/2                   if delta>=w_a.
This proves strict B>Z under the stated positive-measure condition. The quadratic branch cannot be used when u_a<l_m; the piecewise formula handles that boundary correctly.

## 4. Apply to the exact 15-point C2 residual
Take the already verified base `free_residual_obstruction_verified_local.json`, and form
  Q=P\{v,b,c1,c2}, n=11;
  L={a1,a2,a4}, M={f0}, C={f1,f2,f3}.
The relevant complete sets in Q are exactly
  D(a1)={d},       D(f0)={d,e},
  U(a1)={a4,f2,f3}, U(f0)={f2,f3}.
Thus take a=a1,m=f0. Fix the other nine coordinates and write D=t_d,E=t_e,Q2=t_f2,W=t_a4,Y=t_f1. Then
  l_a=D, u_a=min(W,Q2), l_m=E, u_m=Q2, c=Y.

Every interior retained-coordinate point satisfies
  D<E<W, E<Y<Q2.
The first inequality uses the actual relations d<e<a4, all retained in Q[R]. The second uses e<f1<f2. Consequently
  u_a=min(W,Q2)>E>D,
so all interval widths are positive, delta=E-D is strictly less than w_a=u_a-D, and c=Y>E. These are not assumed from a schematic picture: they follow from the complete inherited strict relations just listed.

Hence at every interior external fiber,
  E[min(f0,f1)]-E[min(L,f1)]
    >= (E-D)^2/[2(min(W,Q2)-D)] >0.
This proves B>Z without counting Q's extensions. The nonuniform lower-gate mismatch has a definite positive contribution; the a1<a4 upper pressure only makes the a1 burden earlier.

## 5. Exact integer lower certificate
Multiply the previous conditional lower bound by the real fiber volume
  w_a*w_m=(min(W,Q2)-D)(Q2-E).
The denominator cancels, giving an unnormalized lower integrand
  (Q2-E)(E-D)^2/2.

Let Q_gap consist of the retained nine-point poset R, two new chain points
  d<g1<g2<e,
and a new independent interval point
  e<h<f2,
with no other new generating relations. Its order-polytope fiber over R has volume exactly (E-D)^2(Q2-E)/2. Since |Q_gap|=12=n+1,
  B-Z >= (n+1)n! vol O(Q_gap) = e(Q_gap).
The base R relations are inherited by taking closure before deleting a1,f0; no transitive relation is lost.

For this instance e(Q_gap)=699, so B-Z>=699. This is an integer lower certificate, not the exact value 3790. The already known menu allowance is 2N/3-2R0=568, so even this isolated lower-gap contribution exceeds that allowance. This explains the known failure structurally; it does not provide a global balance obstruction or forbid changing target pairs.

A direct 12-point DP certificate is `LOWER_GAP_WITNESS.json`; an enumeration-free small count is included in the following section.

## 6. Paper count e(Q_gap)=699
The four-element chain d<g1<g2<e precedes every other vertex except s. If s occurs before e, it has four possible slots in that chain. The seven points after e are a2,a3,a4,f1,f2,f3,h, with
  a3<f1<f2<f3, h<f2, a4<f3,
and a2 free. The six-point poset without a2 has 15 extensions: among a3,f1,h the a3<f1 relation gives three orders before f2, and a4 has five slots before f3. Inserting the independent a2 gives 7*15=105, hence 4*105=420 words with s before e.

If s is after e, the eight-point suffix adds s<a2,f1. Delete s,a2 and retain the same six-point poset. The rank of f1 among its 15 words is 2,3,4 with respective multiplicities 3,6,6: begin from the three words of a3<f1 together with h, followed by f2,f3, and place a4 in one of the five pre-f3 slots.
For fixed rank j of f1, insertion of the chain s<a2 with s before f1 has
  binom(8,2)-binom(8-j,2)
possibilities. These are 13,18,22 for j=2,3,4. The suffix count is therefore
  3*13+6*18+6*22=279.
Total: 420+279=699.

## 7. Smallest warning against dropping the lower-window condition
Take Q={e,m,l} with sole edge e<m, L={l}, M={m}, C=empty, K={l}. The common-reference forest mean is 1/2 and the m=1 reference mean is also 1/2, so the reference mean/capacity test is exactly satisfied. All upper-window restrictions are empty. But the missing lower inclusion e<l reverses the comparison: the three extensions give B=8,Z=6. Thus the lower-interface condition cannot simply be omitted, even with one missing predecessor and one-point blocks.
This three-point example is only a method boundary, not a C2 residual example.
