> S117 publication note: this proof/review text records the completed research run. This lean edition retains proof texts, replay sources and selected small results; large generated ledgers, duplicate source snapshots, historical manifests and checksums are not bundled. For the exact retained/generated distinction, portable commands and prior proof links, use [the S117 guide](../README.zh-CN.md), [reproduction instructions](../REPRODUCE.md) and [dependency map](../DEPENDENCIES.md). Historical statements about material being stored refer to that research run; the package contents are listed in the guide.

# The fourth terminal-rank barrier: a concave tail tradeoff

## Result

For the seven-core with covers 0<3; 1<2,4; 2<3,6; 3<5; 4<5, inflate vertices by positive chain lengths (u,a,b,c,t,d,v). Under the uniform law on actual complete labelled linear extensions:

**Theorem. If d=4 and v>=44, the inflated poset has a balanced incomparable pair.** All five other lengths are unrestricted. By order reversal, a=4 and u>=44 is also excluded.

Thus a counterexample with d=4 satisfies v<=43 and c<=172; dually a=4 implies u<=43 and b<=172.

The key improvement is to bound two adjacent tail probabilities jointly. The largest last-interior atom can exceed 1/3, but cannot do so in the part of the probability region required by a counterexample.

The proof depends on the previously established actual-law conditional mixture and good-pair endpoint consequences in `../../S116/general-terminal-rank-bounds/GENERAL_TERMINAL_RANK_BOUNDS.md`, Sections 2–4. Those facts are restated below. No finite box extrapolation is used.

## 1. Actual-law setup and the two forced tails

Write x=T3, and C6=(F1<...<Fn), n=v. Let R count the F vertices below x. Condition on all coordinates in C1,C2 in the order polytope, with respective tops r<s. Normalize x to H=(x-s)/(1-s). The actual uniform extension measure is uniform order-polytope volume, since each labelled extension simplex has volume 1/N!.

On each fiber, C6 is an independent ordered uniform n-sample in (s,1), so R|H is Binomial(n,H). The marginal law of H is a positive mixture of Beta(alpha,d+1), with integer alpha>=c. Mixing over the actual induced fiber measure preserves that representation.

If there is no balanced pair, the good-pair theorem forces

Pr(F1<x)>2/3 and Pr(x<Fn)>2/3.

The corresponding set conditions are D(F1) subset D(x), U(x) minus U(F1)=C5; and U(Fn) subset U(x), D(x) minus D(Fn)=C0 union (C3 minus {T3}). Both displayed differences are chains. All compared vertices are incomparable.

For d=4 and n>=44, all atoms Pr(R=j), 1<=j<=n-2, are strictly below 1/3. For j=1 the Beta(alpha,5) component maximum is 5n/((n+4)(n+5)), attained at alpha=1, since the consecutive-alpha ratio comparison has sign 5-(n-1)alpha. For 2<=j<=n-2 the maximum conditional binomial atom is at most 80/243<1/3 for n>=6. These bounds persist under mixtures.

Consequently absence of balance forces Pr(Fi<x)>2/3 successively for i=1,...,n-1: otherwise consecutive such probabilities would jump from above 2/3 to below 1/3, across an atom smaller than 1/3. Define

Q=Pr(R=n), P=Pr(R=n-1), A=P+Q=Pr(F_(n-1)<x).

A counterexample therefore requires

Q<1/3 and A>2/3.                                           (1)

## 2. Exact component tradeoff

For H~Beta(alpha,5), put q=Pr(R=n), p=Pr(R=n-1). Beta-binomial formulas give

q=product_(i=0)^4 (alpha+i)/(alpha+n+i),
p=5n q/(alpha+n-1).                                       (2)

Let m=alpha+2. For h=1,2,

[m/(m+n)]^2 - [(m-h)/(m+n-h)] [(m+h)/(m+n+h)]
 = h^2 n(2m+n) / [(m+n)^2 ((m+n)^2-h^2)] >0.

Pairing the five factors in q around their midpoint gives

q^(1/5) <= (alpha+2)/(alpha+n+2).

Write z=q^(1/5). Rearranging yields alpha+n-1 >= n/(1-z)-3. For n>3 this denominator is positive. Hence

p <= f_n(q) := 5q(1-q^(1/5)) / [1-3(1-q^(1/5))/n].          (3)

This couples the atom p to its neighboring terminal mass q; it is much stronger than maximizing p independently.

## 3. Concavity makes the tradeoff survive arbitrary mixtures

Put a=1-3/n, b=3/n, z=q^(1/5), D=a+bz. Then for 0<q<1,

f_n''(q) = -(z/q) [(6/5)a+(4/5)bz]/D^3 <0,               (4)

provided n>3. The continuous extension to q=0,1 is concave too. Jensen's inequality applied to the component masses in (2) gives

P <= f_n(Q).                                              (5)

This step is essential: a componentwise nonlinear inequality need not survive mixtures unless its direction and curvature are checked.

Let G_n(q)=q+f_n(q). Its derivative is

G_n'(q)=1+5(1-z)/D-z/D^2.

Since G_n''=f_n''<0 and G_n'(1)=0, G_n'(q)>0 throughout 0<q<1 for every n>3. Thus G_n is strictly increasing. This endpoint-derivative observation was also independently identified during review.

At q=1/3, direct rearrangement gives

G_n(1/3)<2/3 iff (5+3/n)(1-3^(-1/5))<1.

Equivalently,

(5n+3)^5 > 3(4n+3)^5.                                    (6)

At n=44 the difference is 223^5-3*179^5=175086646>0. More explicitly, at n=44+w the difference polynomial, in ascending powers of w, has coefficients

175086646, 226795165, 19429030, 642530, 9515, 53,

all positive. Thus (6) holds for every n>=44.

Combining (1),(5) and strict monotonicity,

A=P+Q <= G_n(Q) < G_n(1/3) <2/3,

a contradiction. This proves the theorem.

## 4. The product consequence

The actual Beta(alpha,5) mixture has alpha>=c, so

Pr(Fv<x)>= (c)_v/(c+5)_v
 = product_(i=0)^4 (c+i)/(c+v+i).

The right endpoint forces this quantity below 1/3. Since the product increases with c and decreases with v, and v<=43, it suffices to check v=43:

at c=172 the product is 2207480/6660009<1/3;
at c=173 the product is 1480015/4440006>1/3.

Therefore c<=172. Duality gives b<=172 when a=4.

## 5. Correct joint law with the top of C5

This section records the right joint law for future inequalities and an exact obstruction beyond d=4. It is not needed for the theorem.

On a fixed r,s fiber write L=1-s, h=(T3-s)/L, y=(B5-s)/L, w=(T5-s)/L. For d>=2, after integrating the interior C5 coordinates, a component with indices k,ell has joint density proportional to

h^k y^ell (w-y)^(d-2),  0<h<y<w<1.                        (7)

For d=1, w=y and the density is h^k y^ell on 0<h<y<1. Marginalizing w in (7) gives h^k y^ell(1-y)^(d-1), up to a common constant. Write B for the beta function. Its normalizing integral is

Z_(k,ell)=B(k+ell+2,d)/(k+1).

The exact moments are

M_j=E[h^j]=(k+1)/(k+j+1) * (k+ell+2)_j/(k+ell+d+2)_j,
E[w^j]=(k+ell+d+1)/(k+ell+d+j+1).                         (8)

The second formula follows by scaling h,y by w in (7): w has Beta(k+ell+d+1,1) law. In particular

C=Pr(Fv<T5)=E[w^v]=(k+ell+d+1)/(k+ell+d+v+1).

This is the top C5 coordinate. Substituting B5 for T5 when d>1 would give the wrong law and the wrong forced comparison.

### Actual unconditional mixture coefficients

The coefficients are not arbitrary. Integrating the actual r,s law gives a finite exact unconditional mixture with i=0,...,u, ell=0,...,t, k=c+i-1, and unnormalized weights

W_(i,ell)=binom(u,i) i!/(i+c-1)! * binom(t,ell)
 * B(a,b+t-ell)
 * B(a+b+t-ell+u-i, i+ell+c+d+v+1)
 * B(c+i+ell+1,d)/(c+i).                                  (9)

All arguments are positive integers. To derive this, use the C1,C2 top-density factor r^(a-1)(s-r)^(b-1), expand

A_c(h)=sum_i binom(u,i)s^(u-i)L^i i!/(i+c-1)! h^(c+i-1)

and (s-r+Ly)^t in powers of y. The remaining common fiber factor is L^(c+d+v). The r integral gives B(a,b+t-ell), and the s integral gives the second beta factor in (9); integrating h,y gives the third factor. Constants common to all i,ell cancel on normalization. The verifier checks (9) against an independent actual labelled-extension count, including all R atoms and C.

Formula (9) is a potential route past relaxations that allow all positive mixtures independently of the seven lengths.

## 6. A precise next obstruction at d=5

For general beta=d+1, centered log-concavity gives, whenever n>(beta+1)/2,

p <= f_(n,beta)(q)
 = beta*q*(1-q^(1/beta))
   / [1-(beta+1)(1-q^(1/beta))/(2n)].                      (10)

The function is concave by the same derivative calculation. But its large-n boundary at q=1/3 satisfies q+f<=2/3 exactly when

(beta/(beta-1))^beta >=3.

This holds at beta=5, since 5^5>3*4^5, and fails at beta=6, since 6^6<3*5^6. Thus the same two-tail relaxation cannot directly handle all d>=5.

The top C5 endpoint by itself does not repair this. A concrete normalized monomial in (7), with d=5, n=100, k=491, ell=0, has

Q=646396283/1951717773 <1/3,
A=256619324351/384488401281 >2/3,
C=497/597 >2/3.

More strongly, this obstruction occurs in a genuine actual conditional fiber, not merely in an arbitrary isolated monomial. Take u=t=1, c=492, d=5, v=100, r=1/2, s=999/1000. Its four component coefficients are products of

(k,coefficient)=(491,s), (492,(1-s)/492)
and (ell,coefficient)=(0,s-r), (1,1-s),

with each product multiplied by Z_(k,ell) before normalizing. Exact evaluation gives

Q=5975039402610052100339/18040870122675452479134 <1/3,
A=14627871733570465872739291/21916650387363562186734621 >2/3,
C=368290882408147051/442393380631568301 >2/3.

Therefore A, B=1-Q, C all exceed 2/3 on that genuine fiber. No inequality valid uniformly on all actual fibers can rule out that three-probability region. Strict inequalities persist on a neighborhood of this fiber.

This is not an actual unconditional poset counterexample, and it does not invalidate global structural inequalities. It identifies exactly what extra information is needed: the induced r,s law / coefficient restrictions such as (9), further forced comparisons, or a genuinely global argument.

## Reproduction

Run `python verify_fourth_rank_tradeoff.py` in this directory. The verifier uses only the Python standard library. It checks the unbounded proof's exact algebraic certificates, component and mixture identities, actual-law reconstruction against independent complete-extension dynamic programming, the product boundary, and the exact d=5 obstruction. Finite numerical checks validate implementation; the all-weight theorem is the analytic proof in Sections 1–3. No hashes or archive layers are required for this deliverable.
