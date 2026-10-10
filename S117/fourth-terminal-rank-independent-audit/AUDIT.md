> S117 publication note: this proof/review text records the completed research run. This lean edition retains proof texts, replay sources and selected small results; large generated ledgers, duplicate source snapshots, historical manifests and checksums are not bundled. For the exact retained/generated distinction, portable commands and prior proof links, use [the S117 guide](../README.zh-CN.md), [reproduction instructions](../REPRODUCE.md) and [dependency map](../DEPENDENCIES.md). Historical statements about material being stored refer to that research run; the package contents are listed in the guide.

# Independent audit: the fourth terminal-rank tradeoff

Date: 2026-10-10. **Verdict: PASS.**

Reviewed source: `../fourth-terminal-rank-barrier/FOURTH_RANK_TRADEOFF.md`, including its simplified monotonicity argument. No author files were edited. One standalone exact checker is supplied, without extra packaging or archive layers.

## Accepted scope

For the quotient with covers `0<3; 1<2,4; 2<3,6; 3<5; 4<5`, every positive chain inflation `(u,a,b,c,t,4,v)` with `v>=44` has a balanced incomparable pair in the uniform complete-labelled-extension law. The five remaining weights are arbitrary positive integers.

By order reversal, `a=4,u>=44` is also excluded. A hypothetical counterexample with `d=4` must have `v<=43,c<=172`; with `a=4`, it must have `u<=43,b<=172`.

This does not prove all seven-weight inflations balanced. The number 44 is the first integer certified by this particular envelope boundary, not a claimed optimal balance threshold.

The accepted prerequisites are the conditional beta-mixture law and good-pair endpoint consequences independently audited in `../../S116/general-terminal-rank-independent-audit/AUDIT.md`. The new theorem does not depend on the ancillary unconditional mixture formula or the d5 obstruction.

## 1. Component inequality

Set `n=v`, `x=top(C3)`, and let R count C6 vertices preceding x. The accepted actual-law reduction represents H as a positive mixture of `Beta(alpha,5)` for positive integer alpha, and `R|H` as `Binomial(n,H)`.

For one component,

`q=Pr(R=n)=product_{i=0}^4 (alpha+i)/(alpha+n+i)`

and

`p=Pr(R=n-1)=5n q/(alpha+n-1)`.

Independently, the function `log(z/(z+n))` has second derivative `-1/z^2+1/(z+n)^2<0`. Applying strict Jensen to the five arguments alpha through alpha+4 yields

`q^(1/5)<(alpha+2)/(alpha+n+2)`.

The author's explicit paired-factor identity is the same inequality and is algebraically correct. Rearrangement gives

`alpha+n-1 >= n/(1-q^(1/5))-3`.

For n>3 this lower bound is positive, so inversion has the stated direction and gives

`p <= f_n(q)=5q(1-q^(1/5))/[1-3(1-q^(1/5))/n]`.

No asymptotic approximation is used.

## 2. Concavity, mixing and monotonicity

Put `z=q^(1/5)`, `a=1-3/n`, `b=3/n`, and `D=a+bz`. Direct differentiation gives

`f_n'(q)=5(1-z)/D-z/D^2`,

`f_n''(q)=-(z/q)[(6/5)a+(4/5)bz]/D^3<0`.

All denominators are positive for n>3. The continuous extension at q=0,1 is concave. Thus, for arbitrary probability weights on the component laws,

`P=E[p] <= E[f_n(q)] <= f_n(E[q])=f_n(Q)`.

This also applies after averaging over the actual induced C1,C2 coordinate law. No uniformity or arbitrary choice of that induced law is assumed.

Let `G_n(q)=q+f_n(q)`. Since `G_n''<0` and `G_n'(1)=0`, G is strictly increasing throughout `(0,1)`, which is stronger than the needed interval `(0,1/3]`.

At q=1/3,

`G_n(1/3)<2/3` iff `(5+3/n)(1-3^(-1/5))<1`.

At n=44 this is exactly

`223^5-3*179^5=175086646>0`.

The left-hand side in the preceding fractional inequality decreases with n, proving it for all n>=44. Independently expanding the integer polynomial at n=44+w gives the positive coefficient list

`175086646, 226795165, 19429030, 642530, 9515, 53`.

At n=43 the corresponding integer difference is -32912557. That only limits this envelope certificate.

## 3. First atom, middle atoms and the full rank crossing

For a Beta(alpha,5) component, the ratio of its R=1 probability at consecutive integer alpha values is

`(alpha+1)(alpha+5)/[alpha(alpha+n+5)]`.

The numerator minus denominator is `5-(n-1)alpha`, negative for all alpha>=1 and n>=44. Hence the maximum is at alpha=1 and equals

`5n/[(n+4)(n+5)]<1/3`.

For `2<=j<=n-2`, any binomial mixture is bounded by its largest conditional binomial atom. The previously audited bound is `80/243<1/3` for n>=6. The independent checker also recomputes these peaks exactly. Both bounds are uniform over components and persist under mixing.

Suppose there is no balanced pair and define `q_i=Pr(x<F_i)=Pr(R<i)`. The established actual-vertex good-pair consequences give `q_1<1/3` and `q_n>2/3`. All x,F_i comparisons are incomparable. For i=2,...,n-1, the increment `q_i-q_(i-1)=Pr(R=i-1)` is less than 1/3. Since balanced values are forbidden, induction forces every q_i in this range to remain below 1/3. Consequently

`A=Pr(R>=n-1)=1-q_(n-1)>2/3`,

while

`Q=Pr(R=n)=1-q_n<1/3`.

But the proved joint tail bound gives

`A=P+Q <= G_n(Q) < G_n(1/3) <2/3`,

a contradiction. This checks the first atom and every intervening rank; it does not assume the false generic bound on the last-interior atom.

## 4. Product bound and the new cap

The accepted mixture has alpha>=c, and the terminal probability increases with alpha, so

`Q >= product_{i=0}^4(c+i)/(c+v+i)`.

A counterexample forces Q<1/3 and v<=43. The product increases with c and decreases with v. At v=43 its values at c=172,173 are respectively

`2207480/6660009<1/3`,

`1480015/4440006>1/3`.

Thus c<=172. The reversal `(u,a,b,c,t,d,v)->(v,d,c,b,t,a,u)` supplies the dual statement.

## 5. Ancillary joint law and d5 obstruction

The joint component density `h^k y^ell(w-y)^(d-2)` on `0<h<y<w<1` is correct for d>=2. Integrating w gives the stated h,y density up to a constant common to components. The normalizer for that marginal density is `B(k+ell+2,d)/(k+1)`.

Integrating h first gives

`E[h^j]=(k+1)/(k+j+1) * (k+ell+2)_j/(k+ell+d+2)_j`.

Scaling h,y by w gives the marginal density of w proportional to `w^(k+ell+d)`, hence the stated top-C5 moment. Using bottom C5 in its place would be wrong; the source does not do that.

The unconditional weights in source Eq9 are also correct. The actual r,s top-coordinate density contributes `r^(a-1)(s-r)^(b-1)`. Following the two polynomial expansions, the r integral is `B(a,b+t-ell)`, while the s integral is `B(a+b+t-ell+u-i,i+ell+c+d+v+1)`. Multiplication by the h,y normalizer gives exactly Eq9. All beta-function arguments are positive. The independent program matches the entire histogram reconstructed from these weights to direct actual-labelled-poset ideal counts in six examples.

For d5,n100,k491,ell0, the published monomial values Q,A,C are exact. More importantly, the actual conditional fiber with u=t=1,c492,d5,v100,r=1/2,s999/1000 has exactly the source's four component coefficients and exact probabilities:

`Q=5975039402610052100339/18040870122675452479134<1/3`,

`A=14627871733570465872739291/21916650387363562186734621>2/3`,

`C=368290882408147051/442393380631568301>2/3`.

All are independently reproduced. These are strict inequalities on an interior fiber, so continuity preserves them on a neighborhood. Therefore a certificate valid on every individual actual fiber cannot separate this entire three-probability region.

This is **not an unconditional poset counterexample**, nor a refutation of a global balance theorem. The induced fiber weights, additional comparisons, or other global restrictions can still matter. The general-beta concavity formula and its limiting distinction between beta5 and beta6 are correct.

## 6. One reproducible exact check

Run:

`python ../fourth-terminal-rank-independent-audit/check.py`

The script uses only the Python standard library and explicit exceptions; it imports no author code and uses no floating point. It writes `results.json` and prints its result. The completed run is in `run.log`.

Coverage:

- 848 component formula and strict geometric-mean checks;
- 120 exact positive-mixture nonlinear checks;
- 856 first-atom bounds;
- 10,058 conditional middle-binomial peak bounds;
- the exact n44 polynomial and c172/c173 boundaries;
- six direct actual-labelled-poset rank histograms, including n45 and c100, all with explicit balanced x,F_i witnesses;
- all 271 actual rank probabilities matched to the unconditional coefficient formula;
- both d5 examples and their exact inequality directions.

For the nonlinear check, roots are eliminated exactly: `p<=f_n(q)` is equivalent to

`q[5nq+3p]^5 <= [5nq-(n-3)p]^5`,

with the right bracket nonnegative, which the program checks separately. Finite tests validate formulas and implementations; the infinite theorem rests on the proof above and its stated audited prerequisites.
