# Independent audit: actual shared-downset fiber MTP2

Date: 2026-10-10. No publication or external-state change was performed.

## Verdicts and boundaries

1. **PASS, exact counterexample and simplex kernel.** For predecessor masks
   `[0,0,3,3,1,2,23,43]` and distinguished labels `u=2,y=3`, the genuine
   continuous fiber violates MTP2. Both a boundary rectangle and a strictly
   interior rectangle have exact negative determinants. The Dirichlet-spacing
   reduction, empty-set conventions, coincident ranks and deterministic endpoint
   ranks are valid.
2. **PASS, exact finite computational minimum n=8.** All shared-downset fibers
   with n≤7 satisfy MTP2. Coverage was independently reconstructed using a
   different poset generator. Every nontrivial configuration is covered by
   full nonnegative polynomial-coefficient certificates, not sampling. The
   analytic empty-downset and unique-maximum branches also pass review; an
   additional exhaustive coefficient run covers those branches through n=7,
   so the finite minimum does not need those two analytic results as a shortcut.
3. **PASS, scope separation.** The counterexample does not refute either the
   ordinary swap square or the dimension-sharp conjecture. Its corresponding
   slacks are respectively 4800 and 23600, strictly positive.
4. The new common-downset recurrence statements in Section 5 of the author's
   report are **outside this audit's scope**. No verdict here certifies them,
   any general dimension-sharp proof, or any other global poset conjecture.

## 1. Definition and independent reconstruction

Let Q=P−{u,y}, m=n−2, and Ω=O(Q), using increasing coordinates along the order.
Write D for the common strict downset, U,V for the strict upper sets of u,y,
L=max z_D with empty maximum 0, and T_U=min z_U, T_V=min z_V with empty
minimum 1. Set A=T_U−L, B=T_V−L. The audited function is the actual volume

    f(s,t)=vol_m{z∈Ω:A(z)≥s, B(z)≥t}.

There is no replacement by finite order maps, uniform insertion choices, or
unweighted extension projections.

The candidate has D={0,1}, U={6}, V={7}. Deletion labels are (0,1,4,5,6,7)
and deletion predecessor masks are (0,0,1,2,7,11). A fresh recursion lists its
18 linear extensions. Their (p,q) histogram is

    (1,3):1, (2,3):2, (2,4):2, (3,1):1,
    (3,2):2, (3,4):4, (4,2):2, (4,3):4.

The independent program `audit_actual_fiber_independent.py` imports none of
the proposal's programs. It constructs this array directly from the original
8-element predecessor masks, builds the exact polynomial, enumerates all full
extensions, and compares a separate continuous integration.

## 2. Dirichlet-spacing reduction and degeneracies

On a deletion extension simplex let 0=z_(0)≤z_(1)≤...≤z_(m)≤z_(m+1)=1.
Its volume is 1/m!. Under its uniform probability law the m+1 consecutive
spacings G_i=z_(i)−z_(i−1) are Dirichlet(1,...,1).

Let a be the last D rank, with a=0 for D empty. Let b,c be the first U,V
ranks, with m+1 for an empty upper set. Transitivity gives a<b,c. Then

    A=G_(a+1)+...+G_b,  B=G_(a+1)+...+G_c.

These are nested sums of respectively p=b−a and q=c−a exchangeable spacings.
One common permutation of the spacing indices sends the smaller block into
the first min(p,q) positions and the larger block into the first max(p,q).
Thus (A,B) has the law of (X_(p),X_(q)), where X_(r) is the r-th order
statistic of m independent uniform variables and X_(m+1)=1. Hence exactly

    f(s,t)=Σ C[p,q] K[p,q](s,t)/m!,
    K[p,q](s,t)=Pr{X_(p)≥s,X_(q)≥t}.

This argument needs no Dirichlet distribution with a zero shape parameter:

- If p=q, A=B is one spacing sum; if p=q=m+1 it is identically 1.
- If p<q<m+1, the three masses have Dirichlet(p,q−p,m+1−q).
- If p<q=m+1, B=1 identically and A has Beta(p,m+1−p) law.
- The case p>q is the label swap; a=0 requires no change.
- For m=0, there is one zero-dimensional simplex with volume 1 and the sole
  rank pair is (1,1), giving f=1 on the closed unit square.

For 0≤s≤t≤1, counting independent uniform samples in the three intervals
below s, between s and t, and above t gives the single formula

    K[p,q]=Σ_{i+j+k=m, i<p, i+j<q} m!/(i!j!k!) s^i(t−s)^j(1−t)^k.

It is valid for either order of p,q and at 0 and 1. The other triangle is
obtained by transposition. `check_kernel_boundaries.py` separately compares
the proposal's integer kernel against direct enumeration of 4^m categorical
sample tuples for every m=0,...,6, every rank pair and every threshold on the
1/4 grid: all 3500 comparisons pass, including deterministic endpoints.
This finite check supplements the general derivation above.

## 3. Exact negative determinant, including a strict interior rectangle

On s≤t the reconstructed polynomial is

    f(s,t)=(t−1)^3 [25s²t+15s²−8st²+6st+2s−3t³−15t²−16t−6]/240.

On s≥t use f(t,s), by the candidate's label symmetry.

For an independent continuous derivation, rename the common predecessors
a,b and their private intermediates v,w. In the region a=L≥b, integrating
the terminal upper coordinates gives

    k_s=((1−L)^2−s²)/2, k_t=((1−L)^2−t²)/2,
    L k_s k_t + (L²/2)k_s(1−L−t).

The region b=L≥a gives its label-symmetric expression. Thus integrate

    2L k_s k_t + (L²/2)[k_s(1−L−t)+k_t(1−L−s)]

from L=0 to 1−t. This agrees identically with the simplex polynomial.

At ε=1/100 the exact values are

    f(0,0)=1/40,
    f(0,ε)=f(ε,0)=1992833399799/80000000000000,
    f(ε,ε)=992840016069/40000000000000.

Their MTP2 determinant is

    −24895078440973240401/6400000000000000000000000000 < 0.

No reliance on a boundary convention is necessary. For δ=1/10000 and
ε=1/100, the determinant of the strictly interior square [δ,ε]^2 is

    −6052032350938988314995726498339/
     1600000000000000000000000000000000000000 < 0.

All four exact interior values are stored in
`actual_fiber_independent_results.json`. The origin one-sided derivatives
are f=1/40, f_s=f_t=−1/120, f_st=0, giving the expected negative mixed
log-derivative numerator −1/14400.

**Caution:** the supplied S110 derivation also evaluates [1/100,2/100]^2.
That particular minor is positive, equal to
618047353260127/312500000000000000000000. It must not be presented as an
interior negative example. The [1/10000,1/100]^2 certificate above fixes this.

## 4. Original complete-extension law and target checks

Fresh enumeration of all 200 full extensions gives

    forward/legal=74, reverse/legal=74,
    forward/illegal=26, reverse/illegal=26.

Direct integration gives raw values

    ∫∫f=5/1008,
    ∫_{s<t}f=∫_{t<s}f=5/2016,
    ∫t f(t,t)dt=37/20160.

Multiplication by 8! gives E=200, F=G=100, H=74, hence Ru=Ry=26.
The source JSON field named `integrals` contains these scaled counts, not
the raw Lebesgue integrals. This is a labeling issue, not a numerical error.

    H²−RuRy=EH−FG=4800>0,
    (n−1)EH−nFG=23600>0.

Thus the actual MTP2 route is blocked, while both original target inequalities
remain valid on this candidate. This audit makes no inference from failure of
an auxiliary hypothesis to failure of the target conjecture.

## 5. Analytic cases and global positivity certificate

### Empty D and a unique maximum of D

For D empty, the joint feasible set in (z,s,t) uses the order inequalities,
0≤z_i≤1, 0≤s,t≤1, s≤z_U and t≤z_V. It is closed under coordinatewise min
and max. Its indicator is MTP2, and integration in z preserves MTP2.

If D has a unique maximal element d, then d is its maximum and L=z_d. Put
r=−z_d, w_i=z_i−z_d for i≠d, and w_d=0. The absolute Jacobian is 1. The
complete constraints include

    −1≤r≤0; r≤w_i≤r+1;
    w_i≤w_j for each order relation, with w_d fixed to 0;
    s,t≥0; s≤r+1; t≤r+1;
    s≤w_i (i∈U); t≤w_i (i∈V).

The endpoint bounds s,t≤r+1 handle empty upper sets and are redundant
otherwise. Every constraint is a coordinate difference inequality or a
one-coordinate interval bound, so the feasible set is a sublattice. The
indicator is MTP2, and integrating (r,w) gives f. The explicit −1≤r≤0 bound
avoids any ambiguity about applying the box inequalities to the fixed w_d.

The standard marginal-preservation theorem is externally sourced rather than
reproved here. Its statement was verified in the publisher abstract of
[Karlin and Rinott (1980)](https://www.sciencedirect.com/science/article/pii/0047259X80900652),
*Journal of Multivariate Analysis* 10(4), 467–498,
DOI 10.1016/0047-259X(80)90065-2. The full external proof was not re-audited.
The finite minimum below has also been independently checked without invoking
these analytic branches.

If U=V, A=B and f(s,t)=h(max(s,t)) for a nonincreasing h. In a rectangle one
of the two off-diagonal maxima equals the upper-right maximum, and the other
is at least the lower-left maximum. This directly proves the required minor
is nonnegative, even when h is zero. Such cases are safely omitted by the
nontrivial-pair enumeration.

### Polynomial and diagonal certificate

For x=s, y=t−s, z=1−t, put P=m!f. It is homogeneous of degree m and the
correct ambient derivative operators along the affine triangle are

    D_s=∂_x−∂_y, D_t=∂_y−∂_z.

The exact numerator

    Δ=P D_sD_t P−(D_sP)(D_tP)

is homogeneous of degree 2m−2 (or identically zero). Nonnegative monomial
coefficients in x,y,z certify Δ≥0 on the triangle; this is equivalent to
nonnegative Bernstein coefficients after dividing by positive multinomial
normalizations. Both triangles must be tested and were tested.

The fiber is positive throughout the open unit square: choose all D
coordinates close to 0 and all remaining coordinates close to 1 while
respecting a strict extension order. Therefore log f is well-defined there.
Unequal-rank kernels have continuous first derivatives across s=t. Only
p=q can create a jump: K[p,p]=h_p(max(s,t)). For fixed s, as t increases
through s, ∂_sK jumps from h'_p(s)≤0 to 0. Consequently the jump of ∂_s log f
is Σ C[p,p](−h'_p(s))/(m! f(s,s))≥0. The p=q=m+1 term has zero jump.
Together with Δ≥0 off the diagonal, ∂_s log f is nondecreasing in t. Integrating
this statement over s proves every MTP2 rectangle inequality inside the
square, including rectangles crossing the diagonal.

All kernels are continuous relative to the closed square, including the
constant endpoint kernels; boundary inequalities follow by limits. The true
fiber is zero outside the unit square. Extending the inequalities there
causes no problem: a positive right-hand product requires all four relevant
coordinates to be inside the square. No unjustified claim that every upper
edge vanishes is used.

## 6. Exhaustive coverage and independently reproduced finite minimum

The independent generator recursively appends the greatest natural label and
chooses its predecessor set to be any ideal of the old poset. This yields
every naturally labeled transitive poset exactly once. Counts for m=0,...,5
are 1,1,2,7,40,357. Every finite deletion poset admits such a labeling.

For each Q, the algorithm takes every ideal D and every upper ideal U,V
contained in the strict common upper set of D. These conditions are both
necessary and sufficient for adjoining incomparable u,y with exactly that D
and those upper sets. Sufficiency follows because all paths D<u<U and
D<y<V already impose relations in Q; no cycle or u−y relation is introduced.
Thus the procedure covers every actual shared-downset pair up to relabeling.
Empty upper sets are included. Checking unordered distinct U,V is sufficient
because transposition exchanges the two triangle certificates. Equal U,V
was proved directly above.

For the ≥2-maxima branch, exact independent totals are:

    m=0,1,2: zero nontrivial configurations;
    m=3: 1 configuration, 1 histogram;
    m=4: 29 configurations, 13 histograms;
    m=5: 828 configurations, 151 histograms.

Every histogram has nonnegative exact coefficients in both sectors. This
matches all proposal counts. The 165 stored oriented histogram records
collapse to 159 under histogram transposition. Canonicalizing in that way,
EVERY coefficient in the author's saved 165 certificate records agrees with
the independent records, not merely their signs or counts.

Additional direct finite verification of the analytic branches gives:

    m=1: empty D 1; unique-max D 0; 1 histogram.
    m=2: empty D 9; unique-max D 1; 7 histograms.
    m=3: empty D 99; unique-max D 15; 48 histograms.
    m=4: empty D 1510; unique-max D 246; 368 histograms.
    m=5: empty D 32659; unique-max D 5289; 3389 histograms.

All 39,829 additional configurations pass, with no inconclusive negative
coefficient cases. All 3813 additional representative coefficient records
are saved. With the 858 multiple-maxima configurations and the direct U=V
argument, this certifies the entire n≤7 scope. The m=0 case is the constant
fiber. Together with the exact n=8 counterexample, the smallest n is exactly 8.

This is an exhaustive exact computational theorem in the stated finite range,
not a conceptual classification of all realizable rank arrays. A no-failure
coarse-grid run at m=6 is not used: it misses the actual negative rectangle.

## 7. Artifacts and reproducibility

Run, in this directory:

    python audit_actual_fiber_independent.py
    python audit_small_minimality_independent.py
    python certify_all_branches.py
    python check_kernel_boundaries.py
    python compare_proposal_coefficients.py

Only the first script needs SymPy; the others use Python's standard library.
The core counterexample and exhaustive scripts do not import the author's
programs. The boundary comparison deliberately imports the exact engine under
test and compares it to an independently enumerated categorical sample space.
The coefficient comparison reads the author's saved artifacts without calling
its arithmetic routines.

`SOURCE_SHA256SUMS` fixes the source files reviewed, and `SHA256SUMS` hashes the
independent scripts, results, full certificates and this report. Neither file
claims to hash itself. The machine-readable verdict records the two audit
scopes separately. Changes to source files after these hashes require a
scoped recheck rather than silently inheriting this verdict.

Publication note: relative-path and source-hash binding changes are documented in
`../PORTABILITY.md`; they do not expand this audit's mathematical scope.
