# Exact structure and failure of MTP2 for shared-downset fibers

Status, 2026-10-10: the genuine order-polytope fiber need not be MTP2. The
8-element counterexample below has two independent exact integrations, one
by direct continuous integration in the companion source and one by the
simplex kernel computation here. This does NOT refute either the proved
ordinary swap square or the still-open dimension-sharp inequality.

An exact finite computational certificate supports minimality at n=8. An
independent audit reproduced all small-size counts and nonnegative coefficient
certificates with a different poset generator, and audited coverage, the
derivative operators, diagonal jumps, and endpoint cases.

## 1. Original objects and exact rank-kernel theorem

Let P have n=m+2 elements and incomparable u,y with the same strict downset D.
Write Q=P−{u,y}, U={v:v>u}, V={v:v>y}, and Ω=O(Q). For z∈Ω set
L=max_{d∈D}z_d (0 if D is empty), Tu=min_{v∈U}z_v (1 if U is empty),
Ty=min_{v∈V}z_v (1 if V is empty), A=Tu−L, B=Ty−L. The actual fiber is
f(s,t)=vol_m{z∈Ω:A≥s,B≥t}.

Partition Ω into its e(Q) linear-extension simplices, each of volume 1/m!.
For a deletion extension σ let a be the position of its last D element,
or a=0 when D=∅. Let b,c be the positions of its first U,V elements,
using m+1 for an empty upper set. Then a<b,c. Put p=b−a and q=c−a,
and let C[p,q] count the deletion extensions giving those two ranks.

THEOREM (direct). Let X_(1)≤...≤X_(m) be the order statistics of m independent
uniform[0,1] variables and define X_(m+1)=1. Then

    f(s,t) = (1/m!) Σ_{p,q=1}^{m+1} C[p,q] K[p,q](s,t),
    K[p,q](s,t) = Pr(X_(p)≥s, X_(q)≥t).

Proof. The m+1 gaps of a point uniform in an extension simplex have the
Dirichlet(1,...,1) law. A and B sum respectively the first p and q gaps after
position a. These gap sets are nested. Exchangeability of all m+1 gaps
therefore identifies their joint law with the sums of the first p and q
gaps, which are exactly X_(p),X_(q). This includes p=q, a=0, b=m+1,
c=m+1, and p=q=m+1 (the constant A=B=1 case). For m=0 the same convention
reduces the formula to the single constant kernel 1. QED.

For 0≤s≤t≤1 the exact kernel formula is

    K[p,q](s,t) = Σ_{i+j+k=m; i<p, i+j<q}
                    m!/(i!j!k!) s^i (t−s)^j (1−t)^k.

Indeed i counts samples below s, j those between s and t. This formula is
valid for ALL relative orders of p,q, including endpoints. The other sector
is obtained by exchanging p with q and s with t.

Consequences specific to the actual fiber:

* On each triangle, f is a polynomial of degree at most m, represented
  homogeneously at degree m in nonnegative triangle coordinates.
* Its Bernstein coefficients before the overall 1/m! factor are nonnegative
  integers

      c[i,j,k] = Σ_{p>i, q>i+j} C[p,q], i+j+k=m.

  Thus they are cumulative tails of ONE shared integer rank array. They are
  more constrained than arbitrary nonnegative Bernstein coefficients.
* Σ C[p,q]=e(Q), so f(0,0)=e(Q)/m!.
* If D is nonempty, p,q≤m+1−|D|. If U is nonempty then p≤m. These imply
  the corresponding endpoint vanishing. In fact f(1,t)>0 for some t<1 is
  possible only when D=U=∅, in which case A≡1 and f is independent of s.
  Similarly for the other side. Endpoint vanishing has this isolated-element
  exception and should not be asserted indiscriminately.
* Arbitrary positive mixtures of these kernels have NOT been proved to obey
  either target inequality. The exact realizability of C by a poset remains
  essential; nonnegative mixture closure is not a valid shortcut.

## 2. Exact original counts from the rank array

Let E=e(P), F count u before y, G count y before u, and H count swappable
extensions with u before y. Then E=F+G. For each rank pair write r=min(p,q).
Its contribution, multiplied by C[p,q], is

    h[p,q] = r(r+1)/2,
    f[p,q] = h[p,q] + p(q−p) if p≤q, otherwise h[p,q],
    g[p,q] = h[p,q] + q(p−q) if q≤p, otherwise h[p,q].

Hence H=ΣC h, F=ΣC f, G=ΣC g, E=F+G. These are the ORIGINAL extension counts.
For example E[AB]=r(max(p,q)+1)/((m+1)(m+2)),
E[min(A,B)^2]/2=r(r+1)/(2(m+1)(m+2)). Multiplying each simplex integral by
n!/m!=(m+1)(m+2) gives the displayed integer contributions.

## 3. A genuine 8-element MTP2 counterexample

Use labels a,b,u,y,v,w,r,s, with the transitive closure of

    a,b < u,y;   a < v;   b < w;   u,v < r;   y,w < s.

Thus D(u)=D(y)={a,b}, with two incomparable maxima. Q has labels a,b,v,w,r,s,
predecessor bitmasks [0,0,1,2,7,11], and 18 linear extensions. Its rank array is

    C[1,3]=1, C[2,3]=2, C[2,4]=2, C[3,1]=1,
    C[3,2]=2, C[3,4]=4, C[4,2]=2, C[4,3]=4.

At ε=1/100, exact simplex integration gives

    f(0,0) = 1/40,
    f(ε,0) = f(0,ε) = 1992833399799/80000000000000,
    f(ε,ε) = 992840016069/40000000000000.

Consequently

    f(0,0)f(ε,ε) − f(ε,0)f(0,ε)
      = −24895078440973240401 / 6400000000000000000000000000 < 0.

This is a rational-grid evaluation of the EXACT continuous volume, not a
finite-order-map approximation and not numerical quadrature. The independent
auditor also supplied a strictly interior rectangle [1/10000,1/100]^2 with
determinant

    −6052032350938988314995726498339 /
      1600000000000000000000000000000000000000 < 0.

That interior value is reported from the independent audit; the reproduction
script here directly certifies the displayed boundary rectangle.

The original count check gives E=200,F=G=100,H=74, so Ru=Ry=26.
The ordinary square slack EH−FG=4800>0, and the dimension-sharp slack
7EH−8FG=23600>0. Both inequalities survive this example.

There is also a simple rank-array diagnostic for the failure. Let Z=ΣC,
R'=Σ_{q≥2}C[1,q], and S=Σ_p C[p,1]. On the s<t side at the origin,
with P=m!f,

    P=Z, P_s=−m R', P_t=−m S, P_st=m(m−1)C[1,2].

Thus MTP2 requires (m−1)Z C[1,2]≥m R'S. The candidate has Z=18,
R'=S=1 and C[1,2]=0, so the homogeneous cross numerator has coefficient −36
at z^(2m−2). The transposed necessary inequality uses C[2,1] analogously.

## 4. Exhaustive small-size certificate and its scope

The generator takes every subset of the natural edges i<j on m labels,
transitively closes it, and deduplicates the resulting posets. Every finite
poset has a natural labeling, so this covers every isomorphism type, allowing
redundancies. For each Q it enumerates every ideal D with at least two maximal
elements, and every upper ideal U,V contained in the strict common upper set
of D. These are exactly the choices compatible with adjoining incomparable
u,y having strict downset D and strict upper sets U,V:

* Necessity: D is an ideal, U,V are upper ideals, and every d∈D is below every
  element of U∪V by transitivity through u or y.
* Sufficiency: adding D<u,y and u<U,y<V creates no cycles or u–y relation,
  and imposes no new Q relation because all D<U∪V already hold in Q. The
  strict lower and upper sets of the two new elements are exactly those given.

Empty U or V are included as upper ideals. Distinct unordered pairs are
sufficient because both sector polynomials, equivalently C and its transpose,
are checked. U=V is omitted from enumeration because f depends only on
max(s,t), which is automatically MTP2. D=∅ and D with a unique maximum are
covered by the separate analytic sublattice argument in S110; the enumeration
is specifically the remaining multiple-maxima case.

For x=s,y=t−s,z=1−t, P=m!f is homogeneous of degree m. On this triangle use
D_s=∂x−∂y and D_t=∂y−∂z. The program forms exactly, with integers,

    Δ = P D_sD_t P − (D_s P)(D_t P).

It checks that EVERY coefficient of this degree-(2m−2) homogeneous polynomial
is nonnegative, on both triangles. This suffices for the nonnegative mixed
log derivative in the triangle interiors. Across s=t, only equal-rank kernels
produce a first-derivative jump. They are survival functions of max(s,t),
whose contribution to the jump of ∂s log f, as t increases, is nonnegative.
Thus the distributional cross derivative is nonnegative everywhere in the
positive open square, implying all MTP2 rectangle inequalities; boundary
inequalities follow by continuity (or by endpoint zeros).

Certified counts:

    m=2: 0 nontrivial pairs (the U=V case is trivial)
    m=3: 1 pair, 1 distinct rank array, all certified
    m=4: 29 pairs, 13 distinct rank arrays, all certified
    m=5: 828 pairs, 151 distinct rank arrays, all certified

Files bernstein_mtp2_m*.json contain summary results.
all_small_mtp2_certificates.json stores a representative Q,D,U,V, the rank
array, and both complete nonzero cross-polynomial coefficient lists for every
one of the 165 distinct arrays across m=2,...,5.

An independent audit regenerated the posets by recursively appended ideals,
without importing these scripts, and exactly matched all listed configuration
and histogram counts and both-sector coefficient certificates. Combined with
the analytic cases, the exact computational conclusion is: n=8 is the smallest
possible size of an actual shared-downset fiber violating MTP2.

CAUTION: a coarse grid is insufficient. Exhausting the m=6 cases on the
1/16 grid found no negative minor, even though the above true n=8 example
fails at ε=1/100. This is why the small-n claim uses full coefficient
certificates rather than grid sampling.

## 5. Exact common-downset recurrences

The following recurrences retain the actual fiber and weights. They are
structural tools, not a claim that quadratic inequalities survive mixing.

### First coordinate, while D is nonempty

If D≠∅, every minimal element v of Q is outside U∪V. Put
Q_v=Q−v and D_v=D−{v}. Partition by the first coordinate z_v=ℓ, then shift
and scale the remaining coordinates. Exactly,

    f_{Q,D,U,V}(s,t)
      = Σ_{v∈Min(Q)} ∫_0^1 (1−ℓ)^(m−1)
          f_{Q_v,D_v,U,V}(s/(1−ℓ),t/(1−ℓ)) dℓ.

The convention is f=0 outside its square support. This follows because both
A and B scale by 1−ℓ, including the case where v is the sole element of D.
The Jacobian is (1−ℓ)^(m−1).

### Last common predecessor: reduction to empty-downset fibers

For D≠∅, sum over ideals I of Q with D⊆I and over d∈D∩Max(I). Put a=|I|,
R=Q−I. Since d is maximal in I, I contains no element of U∪V. Let
f_R be the empty-common-downset fiber on R with upper sets U,V. Then

    f_Q(s,t) = Σ_{I,d} e(I−d)/(a−1)! ∫_0^1
        ℓ^(a−1)(1−ℓ)^(m−a)
        f_R(s/(1−ℓ),t/(1−ℓ)) dℓ.

Proof: d is the last D element, at coordinate L=ℓ; I is the ideal of all
coordinates at most ℓ. The prefix I−d has volume e(I−d)ℓ^(a−1)/(a−1)!;
the suffix is the scaled order polytope of R. These pieces partition Ω up to
a null set. At s=t=0 the beta integral recovers the ordinary extension count.

For each X∈{E,F,G,H}, after multiplying by n!, the same decomposition reads

    X(P) = Σ_{I,d} e(I−d) X(P−I).

The smaller P−I has u,y minimal. This reduces the original counts to a
structured mixture of minimal-pair counts. It does NOT imply the target
sharp inequality by summing: the ratios F/E can vary between branches.

## 6. Reproduction

No third-party Python packages are needed for these scripts.

    cd S111/actual_fiber
    python reproduce_candidate.py
    python certify_small_mtp2.py 3
    python certify_small_mtp2.py 4
    python certify_small_mtp2.py 5

Optional exact-grid evidence (not a global positivity certificate):

    python test_exact_fiber_mtp2.py --m 5 --grid 16 --exhaustive --out exhaustive_m5.json

Primary reusable files: test_exact_fiber_mtp2.py (integer exact volume engine),
certify_small_mtp2.py (homogeneous coefficient certificates),
reproduce_candidate.py (independent exact counterexample audit).
