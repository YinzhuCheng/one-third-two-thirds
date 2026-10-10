# Independent audit of the exact common-downset recurrences

Date: 2026-10-10. Scope: Section 5 of the S111 report, only. No publication or
external-state change was performed. The source report and the earlier
independent audit are unchanged.

## Verdict and scope

**PASS.** Both displayed continuous recurrences, and the last-predecessor
recurrence for each original count E,F,G,H, are valid with the stated
nonempty-D hypothesis. The exact marked-ideal quantifiers, the prefix
factorial, and both endpoint exponents are correct. The suffix has u,y
minimal. Literal swap legality is inherited, including when upper sets have
common successors. The formulas preserve the original law; they do not give
arbitrary positive-mixture closure for a quadratic inequality.

This audit supplies the missing proof detail and an independent exhaustive
implementation. It does not audit or modify the counterexample, minimality,
or other statements in Sections 1–4 of the source report. In particular, it
does not claim a proof of either target inequality by recurrence.

Source REPORT.md SHA-256:

    18bdcf867d8a0b632dee083a1faeafc7c6f7b566e3fa9351b21b4f342a59f1bf

`SECTION5_SOURCE.txt` fixes the exact audited passage. `SOURCE_SHA256SUMS`
fixes the accompanying source files as well. No supplied program specifically
implemented Section 5; the recurrence tests below are new and import none of
the author's or earlier auditor's programs.

## 1. Objects and quantifiers

Let P be a finite n-element poset with incomparable u,y sharing exactly the
same strict downset D. Put Q=P−{u,y}, m=n−2, U={v:u<v}, V={v:y<v}.
All deletions mean induced subposets, retaining transitive comparabilities.
The upper sets U,V may be empty, equal, or overlapping. Put

    L(z)=max_{d∈D} z_d, with L=0 if D=∅;
    T_U(z)=min_{v∈U} z_v, with T_U=1 if U=∅;
    T_V(z)=min_{v∈V} z_v, with T_V=1 if V=∅;
    A=T_U−L, B=T_V−L;
    f_Q(s,t)=vol_m{z∈O(Q):A≥s,B≥t}.

We use 0≤s,t≤1 and set a fiber to zero when either nonnegative threshold is
above 1. This is the support convention needed by the integrals; no claim
about the original survival function at negative thresholds is needed.
Set e(∅)=1 and vol_0 O(∅)=1.

For D≠∅ the last-predecessor index set is exactly

    B(Q,D)={(I,d): I is an order ideal of Q,
                    D⊆I, d∈D∩Max_Q(I)}.

Here d is maximal *in I*, not necessarily in Q. Automatically d is maximal
in D. The sum includes all marked d, even if several choices have the same
I. It includes a=|I|=m when admissible. The object e(I−d) counts extensions
of the induced subposet I\{d}; it is neither e(I), a factorial, nor a count
of extensions of D alone.

For every d∈D and v∈U∪V, transitivity gives d<v. Thus d∈Max(I) forces
I∩(U∪V)=∅. It follows that I is also an ideal of P: the only possible new
predecessors of an element of I, beyond Q, would be u or y, which would
place that element in U or V. Moreover I\D consists of elements
incomparable to both u and y. Hence P−I has u,y minimal and their strict
upper sets are still exactly U,V.

## 2. First-coordinate recurrence

Assume D≠∅. Up to the null set of coordinate ties, every z∈O(Q) has a
unique smallest coordinate at v∈Min(Q). Such a v cannot belong to U∪V,
since every element of that union has all D below it. Set z_v=ℓ and

    z_w=ℓ+(1−ℓ)x_w for w≠v.

The suffix x runs over O(Q−v), and the absolute Jacobian is
(1−ℓ)^(m−1). If D\{v} is nonempty then

    L(z)=ℓ+(1−ℓ)L(x).

If v is the sole D element then L(z)=ℓ and the child convention L(x)=0
gives the same formula. If v is not in D, D remains nonempty, so there is
no further case. For empty upper sets the convention T_U=1 gives
1=ℓ+(1−ℓ)·1, just as for a nonempty upper set. Consequently

    A(z)=(1−ℓ)A(x), B(z)=(1−ℓ)B(x),

and, exactly,

    f_{Q,D,U,V}(s,t)
      = Σ_{v∈Min(Q)} ∫_0^1 (1−ℓ)^(m−1)
          f_{Q−v,D\{v},U,V}(s/(1−ℓ),t/(1−ℓ)) dℓ.

The integrand only needs to be defined for ℓ<1; its value at the single
endpoint ℓ=1 cannot affect the integral. For D empty the translation of L
would fail, so this nonempty-D formula must not be extended to that case.

For completeness the literal extension partition at its first element also
gives X(P)=Σ_{v∈Min(Q)}X(P−v), for X∈{E,F,G,H}, under D≠∅. The tests check
this useful consequence as well, without claiming it was an additional
displayed statement in the source.

## 3. Last-predecessor fiber recurrence and Jacobian

Fix z outside all coordinate-tie hyperplanes. Let d be the unique D element
with largest coordinate ℓ=L(z), and put I={v∈Q:z_v≤ℓ}. Then (I,d)∈B(Q,D),
and the pair is unique. Conversely, for each (I,d)∈B(Q,D), every point of
this piece, apart from its boundary, is parametrized by

    z_d=ℓ;
    z_i=ℓ w_i for i∈I\{d}, with w∈O(I\{d});
    z_j=ℓ+(1−ℓ)x_j for j∈R=Q−I, with x∈O(R).

There are no relations from R into I because I is an ideal. Every relation
from I to R is satisfied by the coordinate separation. Every relation into
d is satisfied, and no relation out of d goes to I\{d}, because d is
maximal in I. Thus these are precisely the required constraints.

Writing a=|I| and k=m−a, the full Jacobian, including the variable z_d=ℓ,
is

    ℓ^(a−1)(1−ℓ)^k.

This follows by expanding the Jacobian along the z_d row: the remaining
blocks are ℓ times an (a−1)-dimensional identity and (1−ℓ) times a
k-dimensional identity. There is no additional a, m, or factorial factor.
Integration over w gives vol O(I\{d})=e(I−d)/(a−1)!.

Since U,V are both contained in R, and the child downset is empty,

    A(z)=(1−ℓ)T_U(x), B(z)=(1−ℓ)T_V(x).

This includes empty U or V. Therefore the exact formula is

    f_Q(s,t)
      = Σ_{(I,d)∈B(Q,D)} e(I−d)/(a−1)! ·
          ∫_0^1 ℓ^(a−1)(1−ℓ)^(m−a)
          f_{R,∅,U,V}(s/(1−ℓ),t/(1−ℓ)) dℓ.

The pieces partition the actual order polytope up to a Lebesgue null set.
This is an identity of continuous volumes, not a finite-order-map model or
a substitution of arbitrary rank weights.

At s=t=0 the beta integral is

    B(a,m−a+1)=(a−1)!(m−a)!/m!,

so this formula gives

    e(Q)=Σ_{(I,d)∈B(Q,D)}e(I−d)e(Q−I).

For a=m, R is empty and necessarily U=V=∅. Its fiber is the constant 1 on
the closed square. The branch contribution is explicitly

    e(I−d)/m! · (1−max(s,t))^m.

Thus the exponent zero at (1−ℓ)^(m−a) is legitimate; no degenerate beta
distribution or undefined endpoint value is being integrated. For D≠∅,
f_Q(1,t)=f_Q(s,1)=0, as also follows directly from L>0 almost surely.

## 4. The original extension law and literal H recurrence

Let E=e(P), F count extensions with u before y, G count those with y before
u, and H count extensions with u before y whose permutation obtained by
exchanging the actual positions of u and y is also a linear extension.

Take a full extension of P and stop just after its last D element d.
Neither u nor y can yet have occurred, because each must follow every
element of D. The set I of elements in this prefix is therefore a subset
of Q, and (I,d) lies in B(Q,D). Conversely, every triple

    a branch (I,d), an extension α of I\{d},
    and an extension τ of P−I

gives exactly the extension α,d,τ of P. Since I is an ideal and d is
maximal in I, every such concatenation is valid. This is a bijection.

Both distinguished elements lie in τ, so their relative order is unchanged.
For literal swap legality, swapping u,y affects only τ. The prefix remains
fixed and before all suffix elements. Because I is an ideal, a valid suffix
cannot create a backward cross-boundary relation. Thus

    swap_{u,y}(α,d,τ) is an extension of P
      iff swap_{u,y}(τ) is an extension of P−I.

This proves inheritance for the actual swap, not merely for an abstract
count assigned to the suffix. In particular,

    X(P)=Σ_{(I,d)∈B(Q,D)}e(I−d)X(P−I),  X∈{E,F,G,H}.

Common successors cause no exception: U∩V remains in R and is above both
distinguished elements. It cannot lie between them in any legal extension.
No part of the proof assumes U∩V=∅ or U≠V.

### Independent continuous verification of the n! normalization

After fixing z∈O(Q), translate the u,y coordinates by L. Their insertion
rectangle is [0,A]×[0,B]. The respective two-dimensional areas are

    φ_E(A,B)=AB;
    φ_F(A,B)=area{0≤x≤A,0≤y≤B,x<y};
    φ_G(A,B)=area{0≤x≤A,0≤y≤B,y<x};
    φ_H(A,B)=min(A,B)^2/2.

The last formula follows because the original and swapped placements are
both feasible exactly when both coordinates are at most min(A,B), with
x<y for the counted orientation. All four functions are homogeneous of
degree two, and X(P)=n!∫_{O(Q)}φ_X(A,B)dz.

On a last-D branch the suffix scaling therefore supplies two additional
powers of (1−ℓ). Since n=m+2,

    ∫_0^1 ℓ^(a−1)(1−ℓ)^(m−a+2)dℓ
      = B(a,n−a+1)=(a−1)!(n−a)!/n!.

Also ∫_{O(R)}φ_X(T_U,T_V)dx=X(P−I)/(n−a)!. Multiplying this, the prefix
factor, and n! yields exactly e(I−d)X(P−I). Thus the fiber formula and the
original full-extension count recurrence have matching normalizations.

## 5. Structured beta mixtures, with their actual weights

Under the uniform probability law on O(Q), the branch weight is

    π_Q(I,d)=e(I−d)e(R)/e(Q).

Conditional on this branch, L has Beta(a,m−a+1) density, and the rescaled
suffix is an independent uniform point of O(R). Hence, if
S_Q=f_Q/(e(Q)/m!) and S_R=f_R/(e(R)/(m−a)!), the normalized version is

    S_Q(s,t)=Σ π_Q(I,d) ·
      E_{L~Beta(a,m−a+1)} S_R(s/(1−L),t/(1−L)).

Under the original uniform law on full extensions of P, instead, the
branch weights are

    π_P(I,d)=e(I−d)E(P−I)/E(P).

The suffix is uniform on the extensions of P−I. In the continuous uniform
law on O(P), its branch radial variable has Beta(a,n−a+1), consistent with
the additional insertion-area factor. The deletion law π_Q and original
law π_P are generally different and must not be interchanged. In fact the
deletion-coordinate marginal of uniform volume on O(P) has density
AB/(E(P)/n!) with respect to dz on O(Q); uniform volume on O(Q) is an
integration device, not that original-law marginal.

For an explicit distinction, let Q have labels d,w,r with d<r and w<r,
take D={d}, U={r}, V=∅, and adjoin u,y as specified. The two branches are

    I={d}, d:       e(I−d)=1, suffix (E,F,G,H)=(8,5,3,3);
    I={d,w}, d:     e(I−d)=1, suffix (E,F,G,H)=(3,2,1,1).

Thus the original counts are (11,7,4,4), and the two conditional F/E
values are 5/8 and 2/3. The deletion weights are 1/2,1/2; the original
extension weights are 8/11,3/11. The correct full-law forward probability
is 7/11. This example is reproduced by the exhaustive script.

The mixture is constrained simultaneously by a single poset, its marked
ideals, exact integer prefix counts, and dimension-dependent radial laws.
Nothing here asserts that arbitrary positive mixtures preserve MTP2, the
ordinary swap inequality, or the dimension-sharp inequality. Even a valid
branchwise quadratic inequality cannot simply be summed without controlling
the cross terms and changing dimensions.

### Empty D

When D=∅, u,y are already minimal. This is the terminal case of the
reduction; one keeps the original empty-downset fiber and original counts.
The displayed last-predecessor sum has no marked d and must not be read as
an empty sum equal to zero. If desired, the discrete identity can be given
one artificial base branch I=∅ of weight 1, with no d. This is only an
identity convention, not a Beta(0,·) formula. The fiber need not be constant
when D is empty. For m=0 it is constant 1 and (E,F,G,H)=(2,1,1,1).

## 6. Independent exhaustive exact checks

`audit_section5.py` uses only Python's standard library and imports no
source or prior-audit routines. It generates natural posets by recursively
appending the greatest label with any predecessor ideal. This produces each
naturally labelled transitive poset exactly once, and every poset admits
such a labeling. For each Q it checks every ideal D and every **ordered**
pair U,V of upper ideals contained in the strict common upper set of D.
These are precisely the configurations that can be extended by the required
u,y. Empty, equal, and overlapping upper sets are all included.

For each configuration the program:

1. Directly enumerates full extensions, tests literal swaps, and computes
   the original E,F,G,H, caching only identical induced posets.
2. Independently reconstructs both complete triangular fiber polynomials
   using exact fractions and order-statistic simplex volumes. It integrates
   them to obtain E,F,G,H and compares those values to literal enumeration.
3. Integrates each radial recurrence symbolically, coefficient by
   coefficient, and checks equality of the complete polynomials in both
   sectors. This is stronger than checking a threshold grid.
4. Checks every original count recurrence and every marked-ideal branch
   separately. It partitions both deletion extensions and full extensions
   by their actual last D element; for every full extension with D≠∅ it
   compares literal swap legality before and after deleting the prefix.
5. Checks the factorial beta cancellation, zero-dimensional suffixes,
   f(0,0), all upper-edge corners including isolated-element exceptions,
   and the complete diagonal polynomial matching between the two sectors.

For explicit details of the symbolic integration, write the child sector
polynomial as Σ c_ij s^i t^j, put k=|R|, r=1−ℓ, and assume s≤t. Support
forces r≥t, and each term contributes

    c_ij s^i t^j · Σ_{h=0}^{a−1} (−1)^h C(a−1,h)
      [1−t^(k−i−j+h+1)]/(k−i−j+h+1).

All k−i−j are nonnegative, so these are polynomial integrals with positive
integer denominators. The prefix coefficient e(I−d)/(a−1)! is then
applied. For the first-coordinate formula a=1 and k=m−1. Boundary values
follow from these exact polynomials together with the explicit support
convention, rather than an undefined evaluation at ℓ=1.

The complete finite check passes. Counts by deletion size m are:

    m   Q posets   all configurations   D≠∅       marked branches
    0       1              1                 0              0
    1       1              5                 1              1
    2       2             33                 8             11
    3       7            315                77            142
    4      40           4403              1026           2495
    5     357          89611             19469          61567

Thus all 94,368 configurations through n=7 pass, including 20,581 with
nonempty D and 73,787 empty-D base cases. All 64,216 marked branches are
checked separately. The original extension counts sum to 15,595,912 over
these configurations; all 2,277,476 full extensions in the nonempty-D cases
receive a literal, branch-specific swap-inheritance check. Both recurrences
pass complete exact polynomial comparisons in both sectors for every
nonempty-D configuration. The enumeration includes 65,131 configurations
with U∩V≠∅ and 12,994 with U=V.

The exact finite results are recorded in `section5_exact_checks.json`.
The genuine n=8 example from the source is also checked separately, with
its four marked-ideal branches and all 200 literal full extensions.

## 7. Reproduction and hashes

From this directory run:

    python audit_section5.py --max-m 5 --literal-partition-max-m 5

There are no third-party dependencies. The output includes deterministic
SHA-256 digests of every ordered configuration and its exact branch count
record, plus runtime metadata. `AUDIT_VERDICT.json` records the bounded
scope and totals. `SHA256SUMS` hashes the audit script, exact result, source
snapshot, source hashes, verdict, and this proof. No checksum file claims
to hash itself. A modified source requires a scoped recheck.

Publication note: relative-path and source-hash binding changes are documented in
`../PORTABILITY.md`; they do not expand this audit's mathematical scope.
