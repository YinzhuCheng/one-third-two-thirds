# Chan–Pak minimal-clone/subset route for the actual slot bound

Date: 2026-10-18. Scope: only the common- `t2` antichain endpoint gap and its auxiliary slot inequality. No conclusion about the original conjecture or a global classification is made.

## Result first

The all- `U` third-clone controls supplied by the parent are correct. They give

\[
N\le 2(r+1)(s+1),\qquad 2N\le(r+s+2)^2,
\]

and do not close the desired unequal-mean bound

\[
\boxed{N\le rs+\min(r^2+2r,s^2+2s).}\tag{T}
\]

There is a more informative, exact subset translation. Add only the two minimal clones, and retain the original minimal elements which they do not block as a third subset. Put

\[
d=\mathbb E[T\mathbf1_{R=0}],\qquad
 e=\mathbb E[R\mathbf1_{T=0}],\qquad
L=N-r-s+d+e.
\]

Chan–Pak Theorem 1.10 then proves

\[
\boxed{N\le r+s-d-e+2(r-e)(s-d).}\tag{B}
\]

Theorem 1.9 also gives

\[
\boxed{(r+s-d-e)^2\ge(d+e+2)L.}\tag{C}
\]

These are genuine actual-poset inequalities, with the complete upper closures in the events. They strengthen the uncorrected two-factor bound in some regimes, but no argument from them to (T) was obtained. In particular the boundary corrections can both vanish for actual slots, leaving (B) equal to the known two-factor bound.

The limited mechanism audit is therefore **a useful exact translation, but not a proof of (T)**. It does not prove that all uses or iterates of Chan–Pak are incapable of proving (T).

## 1. Definitions, source, and normalization

Let `U` be any finite poset, `n=|U|`, and let `S_y,S_z` be upper ideals, possibly empty. For a uniform linear extension `f` of `U`, set

\[
R=f_{\min}(S_y)-1,\quad T=f_{\min}(S_z)-1,
\]

with an empty filter assigned the value `n`. Define

\[
r=\mathbb ER,\quad s=\mathbb ET,\quad
N=\mathbb E[RT+\min(R,T)].
\]

All expectations in this report are with respect to the original uniform extension of `U`, never the distribution obtained by forgetting clones from a uniform extension of an augmented poset.

Source: Swee Hong Chan and Igor Pak, *Correlation inequalities for linear extensions*, [arXiv:2211.16637v2](https://arxiv.org/html/2211.16637v2), §1.3, Theorems 1.9–1.10, equations (1.17)–(1.19); their event identification is checked in §6.5, Lemma 6.6, equation (6.13). The optional stronger determinant statement below is explicitly in Remark 5.4, equation (5.4), together with the hyperbolic-matrix application in §6.5.

The precise hypotheses used are: a finite poset `P`, and disjoint, nonempty subsets `A,B` (or `A,B,C`) of `min(P)`. With

\[
K_{AB}:=\#\{h\in\mathcal E(P):1\in h(A),\ 2\in h(B)\},
\]
\[
D_A:=\#\{h\in\mathcal E(P):1\in h(A),\ 2\in h(A\uparrow)\},
\]

the theorems, after canceling their common probability denominators, state

\[
K_{AB}^2\ge D_AD_B,\tag{CP9}
\]
\[
D_CK_{AB}\le2K_{AC}K_{BC}.\tag{CP10}
\]

Theorem 1.10 also asserts the existence of a permutation for which the factor `2` can be replaced by `1`. It does **not** allow us to prescribe the subset occupying the `C` position. We do not use Conjecture 1.5.

Below each displayed event count has been divided by `e(U)`, rather than `e(P)`. This is harmless in these homogeneous degree-two inequalities, and avoids incorrectly assuming that restrictions of augmented random extensions are uniform on `U`.

For disjoint minimal subsets one has the exact union identity

\[
D_{A\cup B}=D_A+D_B+2K_{AB}.\tag{U}
\]

Indeed, after a first element in `A`, a second element in `B↑` can only be an element of `B`: every strict successor of a still-present minimal `B` element is blocked. This is why the upper closure in (CP9) must not be discarded.

## 2. Insertion counts and the label factor

Add incomparable minimal elements `a,b`, with successors `S_y,S_z`, respectively. Because the sets are upper ideals, these are exactly their successor sets in `U`; no accidental extra relations need to be imposed.

For a fixed extension of `U`, `a` has `R+1` legal insertion gaps, and `b` has `T+1`. The two labeled clones can be inserted in

\[
(R+1)(T+1)+\min(R+1,T+1)
=RT+\min(R,T)+R+T+2
\]

ways. The additional `min` counts the second label order when the two clones occupy the same original gap. Thus

\[
\frac{e(U+a+b)}{e(U)}=H:=N+r+s+2.\tag{I}
\]

Theorem 1.8, or its underlying two-minimum count inequality, gives `H≤2(r+1)(s+1)`, namely

\[
N\le2rs+r+s.
\]

This is recorded solely as the already-known comparison bound.

## 3. Third clone below all of U: the parent's two controls are exact

Let `P=U+a+b+c`, where `c<u` for every `u∈U`. Then `min(P)={a,b,c}` (also when some original filters are empty). In units of `e(U)`, the complete three-clone event matrix is

\[
\begin{array}{c|ccc}
 &a&b&c\\\hline
a&0&1&s+1\\
b&1&0&r+1\\
c&s+1&r+1&N
\end{array}.
\tag{A}
\]

Here diagonal entries are `D` events, not ordinary two-distinct-label events.

To see `D_c=N`, force `c` first and an original `U` element second. The clones `a,b` must now be inserted after that first original element. For each original extension with `R,T≥1`, the permitted original gaps are `1,…,R` and `1,…,T`, giving exactly `RT+min(R,T)` labeled insertions. If either variable is zero there are none, agreeing with this formula. Equivalently `D_c/e(U)=H-(s+1)-(r+1)=N`.

The zeros on the other diagonal positions are essential: an original successor of `a` or `b` cannot be second while `c` is still present.

- (CP10) with `C={c}` gives `N≤2(r+1)(s+1)`.
- For (CP9), take `A={c}`, `B={a,b}`. Identity (U) gives `D_B/e(U)=2`, not `0` or `1`, while `K_AB/e(U)=r+s+2`. Hence `2N≤(r+s+2)^2`.
- The factor-one existence statement can select `a` or `b`, whose diagonal counts vanish, so it provides no factor-one bound with `c` prescribed.

Thus the two controls are correct, but neither supplies (T) in the strongly unequal-mean regime.

## 4. An isolated third clone: the n-dependent factor cancels correctly

Now let `c` have no successors. Write `k=n+1`. The clone-only event matrix, again in units of `e(U)`, is

\[
\begin{array}{c|ccc}
 &a&b&c\\\hline
a&kd&k&s+1\\
b&k&ke&r+1\\
c&s+1&r+1&0
\end{array}.
\tag{E}
\]

For example, an event with `a` first and an original successor of `a` second requires `R=0`; the `b` clone has `T` allowed positions after that original element. Once these are fixed, the isolated `c` has `n+1` positions among the `n` remaining labeled elements. This gives `(n+1)E[T 1_{R=0}]`, not `(n+2)d`, `nd`, or `d`. Likewise, forcing `a,b` first leaves an arbitrary extension of `U+c`, giving `(n+1)e(U)`.

The resulting nontrivial clone-only (CP10) bounds are

\[
d(r+1)\le2(s+1),\qquad e(s+1)\le2(r+1),
\]

and (CP9) for the two individual clones gives `de≤1`. Other clone-only subset choices are read exactly from (E) using (U); no entry in (E) contains `N`. This construction by itself therefore does not directly control the desired mixed slot count. The factor-one existence statement can use the isolated clone's zero diagonal.

## 5. Third clone with the same successors as b

Take `c→S_z`, a distinct labeled minimal clone of `b`, and put

\[
\alpha=\mathbb E[\mathbf1_{R=0}T(T+1)].
\]

The clone event matrix is

\[
\begin{array}{c|ccc}
 &a&b&c\\\hline
a&\alpha&s+1&s+1\\
b&s+1&0&r+1\\
c&s+1&r+1&0
\end{array}.
\tag{Z}
\]

For the first diagonal event, force `a` first and an original `S_y` element second. This requires `R=0`. Both `z`-clones must be inserted after that original element and before the first `S_z` element. They have `T` original gaps each, giving `T²+T`, because a coincident gap supports both label orders. The other two diagonals vanish because one still-present `z`-clone blocks every original `S_z` element.

Consequently (CP10) yields the actual boundary factorial-moment inequality

\[
\boxed{\alpha(r+1)\le2(s+1)^2.}\tag{ZB}
\]

Taking `{b,c}` as one subset in (CP9) gives exactly the same result: `D_{b,c}/e(U)=2(r+1)` and `K_{a,{b,c}}/e(U)=2(s+1)`. Interchanging `y,z` gives the dual inequality. These are genuine new translations relative to the bare second-moment calculation, but they do not contain `N`. Again, the factor-one existential conclusion can use a zero diagonal.

## 6. The informative original-minimum subset

Return to `P=U+a+b` and define

\[
G=\min(P)\cap U
=\{u\in\min(U):u\notin S_y\cup S_z\}.
\]

If `G` is empty, every original extension starts in `S_y∪S_z`, so `RT+min(R,T)=0`; hence `N=0` and (T) is trivial. Conversely, if `N>0` then some original extension starts outside the union, so `G` is nonempty. Thus the following application of the three-subset theorem is legitimate whenever a nontrivial `N` needs control.

For the three subsets `{a},{b},G`, their exact event matrix in units of `e(U)` is

\[
\boxed{
\begin{pmatrix}
d&1&s-d\\
1&e&r-e\\
s-d&r-e&L
\end{pmatrix},\qquad L=N-r-s+d+e.
}\tag{G}
\]

Here is a direct count, including the `G↑` event.

- `K_ab/e(U)=1` after removing the first two clones.
- `D_a/e(U)=d`, by first forcing an original `S_y` element and inserting `b` after it; similarly `D_b/e(U)=e`.
- Forcing `a` first leaves `(s+1)e(U)` extensions. Their second elements partition into `b`, `S_y` successors, and the unblocked original minima `G`. Thus `K_aG/e(U)=(s+1)-1-d=s-d`. The dual count is `r-e`.
- With both first elements original, the first is necessarily in `G`. Any available second original element is either another original minimum in `G`, or lies above the first one. It therefore belongs to `G↑`, exactly the event in the source theorem. For a fixed extension with `R,T≥1`, forcing the two clones after these two original elements leaves `R-1,T-1` insertion gaps. Its contribution is
  `(R-1)(T-1)+min(R-1,T-1)=RT+min(R,T)-R-T`.
  Correcting the cases `R=0` or `T=0` gives the stated expectation `L=N-r-s+d+e`.

This also establishes `L≥0` without importing a correlation assertion.

### 6.1 Exact consequences of Theorems 1.9 and 1.10

The `G`-pivot in (CP10) is

\[
L\le2(r-e)(s-d),
\]

which is precisely (B). The other two pivots give

\[
d(r-e)\le2(s-d),\qquad e(s-d)\le2(r-e).
\]

Theorem 1.10's additional conclusion says that at least one of

\[
d(r-e)\le s-d,\quad e(s-d)\le r-e,\quad
L\le(r-e)(s-d)
\]

holds. One may not choose the last inequality without further evidence.

All (CP9) applications formed from unions of these three groups are explicit:

\[
de\le1,\quad (s-d)^2\ge dL,\quad (r-e)^2\ge eL,
\]
\[
(r+s-d-e)^2\ge(d+e+2)L,
\]
\[
(s+1-d)^2\ge d(N+r-s+d),
\]
\[
(r+1-e)^2\ge e(N-r+s+e).
\]

The fourth is the promised two-clone-subset bound (C). The final two also show explicitly why replacing a subset's full upper closure by just its labels loses terms.

### 6.2 Optional stronger consequence from the published underlying matrix statement

This is not silently attributed to the wording of Theorems 1.9–1.10. The same source explicitly supplies, in Remark 5.4 and Lemma 6.6, the stronger fact that the determinant of the three-group matrix (G) is nonnegative. Its exact slot form is

\[
\boxed{
(1-de)N\le2rs+r+s-d(r+1)^2-e(s+1)^2+de(r+s+2).
}\tag{D}
\]

Equivalently,

\[
(1-de)L\le2(r-e)(s-d)-d(r-e)^2-e(s-d)^2.
\]

Keep (D) undivided when `de=1`. When `de<1`, it gives a valid refined upper bound after division. This is an actual theorem-based improvement, not a guessed FKG inequality.

Even this fixed three-group determinant does not by itself prove (T). For example, actual `U=C_n`, `S_y={last element}`, `S_z={second,...,last}` gives, for `n≥3`, deterministic `R=n-1,T=1`, hence `d=e=0`. Both (B) and (D) reduce to `N≤3n-2`, while the desired right-hand side is `n+2` and the actual value is `N=n`. The target is true in this example, but these bounds are strictly too weak. Further information about the extension process is needed; the example is not a counterexample to (T).

For `r≥s` and `de<1`, a sufficient extra boundary inequality that would let (D) close (T) is exactly

\[
d(r+1)^2+e(s+1)^2-de(s+1)(r+s+2)
\ge(s+1)(r-s).
\]

It is not proved here and is not universally necessary for (T). Indeed the deterministic-chain example with `d=e=0,r>s` shows this sufficient condition itself fails. Hence it cannot simply be asserted as a missing universal lemma.

## 7. What the supplied free-moment example does and does not show

For the parent's abstract joint law

\[
(R,T)=(29,0)\text{ with probability }2/3,
\quad (242,3)\text{ with probability }1/3,
\]

one obtains `r=100,s=1,N=243,d=0,e=58/3,L=484/3`. The desired bound would be `103`. This law satisfies (B) at equality and satisfies all the explicit (CP9)/(CP10) expressions in §6.1. Thus those few displayed scalar inequalities alone do not close the target.

This is emphatically **not an actual-poset counterexample**, nor a witness against all known Chan–Pak constraints. Its `T` marginal already violates Theorem 1.6: `P(T≥1)=P(T≥2)=1/3`, whereas the first-tail inequality requires the square of the first quantity to dominate the second. It also violates the stronger determinant (D): the right side of the corresponding `L` bound is `142`, below `484/3`. We therefore do not use this abstract example as a general obstruction to the entire source mechanism.

## 8. Independent exact verification of the translations

The local script `verify_translations.py` constructs finite augmented posets, counts their linear extensions by subset dynamic programming, and counts the precise first-two events from their definitions. It checks every event identity in matrices (A), (E), (Z), (G), and the total two-clone insertion count (I), for every naturally labeled poset with `0≤n≤4` and every pair of its upper ideals (empty ideals included).

Observed output:

`All exact event identities verified. {'pairs': 3645, 'posets': 51}`

This finite check is a safeguard for the formulas and label factors; the identities and inequalities above are proved by the direct counts, rather than inferred from enumeration. No external writes or hashes were performed.

## 9. Conditional endpoint algebra requested by the parent

Use the parent's separate endpoint notation `p,r` for lower-context left-slot means and `q,s` for upper-context right-slot means. Here the upper-context mixed count is `N`, so the generic target (T) reads

\[
N\le qs+\min(q^2+2q,s^2+2s).
\]

The supplied endpoint expression is

\[
F=(M+ps+r+s+1)(p+q+r+s+6)
 +(p+1)(6-M-N-ps-qr).
\]

Its coefficient of `M` is `q+r+s+5>0`. Consequently the supplied lower estimate `M≥pr-1` gives, by direct expansion,

\[
F\ge(p+1)\big[(r+s)^2+qs+6(r+s)+7-N\big].
\]

**Conditionally on** the as-yet-unproved upper-slot estimate `N≤qs+s²+2s`, this yields

\[
F\ge(p+1)[r^2+2rs+6r+4s+7]>0.
\]

The algebra is correct. This report has not proved the estimate on which the last step depends, so the endpoint gap is not declared closed. The dual argument must retain its analogous unproved target estimate as well.
