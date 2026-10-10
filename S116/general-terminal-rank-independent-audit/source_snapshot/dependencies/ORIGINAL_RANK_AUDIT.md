# Independent audit: long-final-chain rank obstruction

Date: 2026-10-10. Verdict: **PASS** for the frozen theorem and its explicitly delimited consequences. This is a next-package result; this audit neither changes nor republishes frozen S114.

## 1. Accepted theorem and scope

Let Q have covers 0<3; 1<2,4; 2<3,6; 3<5; 4<5. Inflate its seven vertices by nonempty chains of lengths (u,a,b,1,t,1,v), where u,a,b,t are arbitrary positive integers and v>=5. Every such actual poset has a balanced pair under the uniform distribution on its complete labelled linear extensions.

More precisely, let x be the unique C3 element and let C6=(F1<...<Fv). If both Pr(F1<x)>2/3 and Pr(x<Fv)>2/3, then some pair (x,Fi), with 2<=i<=v-1, is balanced. If either endpoint requirement fails, the independently known good-pair theorem guarantees balancedness, possibly elsewhere.

No cone assumption, minimal-counterexample hypothesis, equality of weights, uniform quotient law, or uniform deletion law is used. The theorem is not an exclusion of all arbitrary seven-weight inflations, nor of every width-three poset. The generic rank lemma does not extend to v=4. The theorem does not assert a balanced x-to-C6 pair without its endpoint hypotheses.

## 2. Actual uniform law and the conditional polynomial

Give all N actual labelled elements coordinates in (0,1), restricted by all poset inequalities, with uniform Lebesgue density. Apart from zero-volume ties, each complete extension occupies a coordinate-order simplex of volume 1/N!. The resulting complete extension is therefore exactly uniform.

Condition on all C1 and C2 coordinates. Their top coordinates r,s satisfy 0<r<s<1 almost surely. With z the unique C5 coordinate, the remaining constraints are precisely:

- C0 is an ordered u-tuple in (0,x).
- s<x<z<1.
- C4 is an ordered t-tuple in (r,z).
- C6 is an ordered v-tuple in (s,1).

The fiber factors as a C6 factor and the remaining factor. In particular C6 is independent of x,z on this conditioned fiber. Integrating C0 and C4 contributes x^u/u! and (z-r)^t/t!, respectively. The C6 volume (1-s)^v/v! does not depend on x,z. Thus the conditional x,z density is proportional to x^u(z-r)^t on s<x<z<1, exactly as claimed. C4 may contain coordinates below s; its correct lower endpoint is r.

Set x=s+(1-s)h and z=s+(1-s)y. Constant Jacobian and scale factors disappear on normalization. Integrating y gives

f(h) proportional to [s+(1-s)h]^u integral_h^1 [s-r+(1-s)y]^t dy.

The binomial coefficients of both powers are nonnegative, since s>0, s-r>0 and 1-s>0. For every integer ell>=0,

integral_h^1 y^ell dy = (1-h)(1+h+...+h^ell)/(ell+1).

Consequently f(h)=(1-h)P(h)/Z, with P(h)=sum_(k=0)^(u+t) c_k h^k, c_k>=0 and P nonzero. In fact every coefficient in that range is positive on the almost-sure interior fibers. Since integral_0^1 h^k(1-h)dh=1/((k+1)(k+2)), the normalized weights are

w_k = [c_k/((k+1)(k+2))] / sum_l[c_l/((l+1)(l+2))].

These form a probability distribution, and H is its finite mixture of Beta(k+1,2) laws. The factor ((k+1)(k+2)) belongs in the denominator of the mixture weight; the author's formula has the correct normalization.

Conditional on H=h, the number R of C6 elements below x is Binomial(v,h). Sorting an iid uniform v-sample from (s,1) gives exactly the ordered C6 distribution, and sorting does not change that count. Thus the beta-binomial mixture is a distribution under the actual extension law, not an approximation or a quotient model.

The induced law of the conditioned C1,C2 coordinates generally is not uniform. The proof never needs it to be uniform: a bound valid on every almost-sure fiber can be averaged under that actual induced law.

## 3. Rank-atom lemma, all quantifiers, and a uniform gap

For integers n>=5, k>=0, and 1<=j<=n-1, direct beta integration gives

p(n,j,k) = binom(n,j)(k+1)(k+2) (j+k)! (n-j+1)! / (n+k+2)!
         = (n-j+1) binom(k+j,j) / binom(k+n+2,n).

The consecutive-k ratio is (k+j+1)(k+3)/((k+1)(k+n+3)). Its comparison with one is governed exactly by (j-n)k+3j-n. Since j<n, the ratio eventually lies below one; all maxima occur at the finite threshold specified by this linear sign calculation. No finite cutoff in k is needed for the proof.

For j=1 the maximum is at k=0 for n>=5, giving 2n/((n+1)(n+2))<1/3. For j=n-1 the two maximizing integers are 2n-3 and 2n-2, giving

L(n)=4n(2n-1)/(3(3n-2)(3n-1)).

The inequality L(n)<1/3 is equivalent to n^2-5n+2>0, which holds at n=5 and increases thereafter.

For n>=6 and 2<=j<=n-2, every binomial(n,h) atom is at most B(n,j)=binom(n,j)(j/n)^j(1-j/n)^(n-j). The stated consecutive-j ratio is correct in the range needed to reach the middle. The function m -> (1+1/m)^m is increasing for positive m; hence symmetry gives B(n,j)<=B(n,2). Finally

(d/dn) log B(n,2) = 1/(n(n-1))+log(1-2/n)+2/n
                  < 1/(n(n-1))-2/n^2 < 0

for real n>2. The logarithmic inequality follows from log(1-z)<-z-z^2/2 for 0<z<1. Thus B(n,j)<=B(6,2)=80/243<1/3. For n=5 the two middle maxima are 3/14 at j=2,k=1 and 5/21 at j=3,k=2,3. This covers every rank and every nonnegative integer k.

There is even one uniform bound for all n>=5, stronger than the note needs:

p(n,j,k) <= 30/91 < 1/3.

Indeed the j=1 bound decreases for n>=5 and starts at 5/21; L(n) decreases for n>=5 and starts at 30/91; and 80/243<30/91. The derivative sign of L follows from

L'(n)=-12(9n^2-8n+2)/(27n^2-27n+6)^2<0.

Therefore every probability mixture over k, and then every averaging over conditioned coordinates, retains the uniform gap at least 1/273 below 1/3. It is independent of all weights and fiber coordinates. The generic equality 30/91 is attained at n=5,j=4,k=7 or 8; equality need not be attainable by the particular poset mixture.

At n=4,j=3,k=5 the atom is 56/165>1/3. This invalidates only extension of this generic atom lemma to n=4, not the 1/3–2/3 conjecture or a poset statement.

## 4. Endpoint dependencies and the internal witness

The external dependency was checked directly in [Imed Zaguia, arXiv:1610.00809v3, Definition 1 and Theorem 2](https://arxiv.org/html/1610.00809). An incomparable ordered pair (y,w) satisfying D(y) subseteq D(w), with U(w) minus U(y) a chain, is good when Pr(y<w)<=1/2; the theorem then supplies a balanced pair somewhere. If 1/2<Pr(y<w)<=2/3, the tested pair is itself balanced. Thus absence of every balanced pair forces Pr(y<w)>2/3. Reversing the order gives the upper-set version. This derivation needs no minimality assumption.

For (F1,x):

- D(F1)=C1 union C2 is contained in D(x)=C0 union C1 union C2.
- U(x) minus U(F1)={z} is a chain.

For (x,Fv):

- U(Fv) is empty and contained in U(x)={z}.
- D(x) minus D(Fv)=C0 is a chain, even though D(Fv) also includes F1,...,F(v-1).

Both pairs are actually incomparable. The chain prefixes/tails do not invalidate either set identity. Accordingly no-balanced-pair assumptions force the two strict endpoint inequalities.

Let qi=Pr(x<Fi)=Pr(R<i). The hypotheses imply q1<1/3 and qv>2/3. At the least i with qi>=1/3, one has i>=2 and

qi=q(i-1)+Pr(R=i-1)<1/3+1/3=2/3.

Since qv>2/3, this crossing index cannot equal v. Thus 2<=i<=v-1, proving the advertised internal-vertex conclusion. The source leaves the last one-line inference implicit, but its conclusion is correct. Equality qi=1/3 is allowed because balancedness uses the closed interval.

## 5. Independent exact computation

The author source files were copied before execution; the originals were never edited. Replaying the identical verifier in separate normal and python -O directories reproduces frozen verification.json byte-for-byte in both modes:

- 1,024 vectors: u,a,b,t each in 1..4; v in {5,6,7,8}.
- All 1,024 satisfy the two endpoint hypotheses and have the required crossing.
- Largest interior atom is 141704/494527 at weights (4,1,1,1,4,1,5), rank 4.
- 433,524 exact beta-binomial checks, plus the last-rank maxima and n=4 countercheck.

The author's explicit require helper keeps checks active under -O. Its finite box only validates an implementation; it is not the unbounded proof.

Our independent_check.py imports none of the author's implementations. It computes each rank histogram in two distinct ways:

1. A chain-prefix ideal-state recurrence, counting each complete labelled extension once.
2. Positive exact simplex integration, independently recovering the integer counts.

For the second method, integrate the joint density of 0<r<s<x<z<1 after all other actual coordinates have been integrated. For rank j the density is

r^(a-1)(s-r)^(b-1) x^u (z-r)^t (x-s)^j (1-x)^(v-j)
 / [(a-1)!(b-1)!u!t!j!(v-j)!].

Introduce nonnegative gaps g0=r, g1=s-r, g2=x-s, g3=z-x, g4=1-z, summing to one. Expand only positive multinomials:

(g0+g1+g2)^u, (g1+g2+g3)^t, (g3+g4)^(v-j).

Each resulting monomial has exact simplex integral product_i(e_i!)/N!. Multiplication by N! converts volume into the number of labelled extensions with the given rank. The resulting histogram agrees entry-for-entry with the separate recurrence in all 1,034 tested vectors, including ten larger asymmetric cases. These computations do not invoke either the conditional-mixture representation or the author's code.

Additional checks include 2,068 actual-label endpoint arrows; 433,524 equalities between factorial beta integration and the claimed binomial formula, together with their bounds; exact all-k maximizing candidates for n=5..60; and 324 normalized positive-mixture checks at rational fibers. Both independent normal and -O runs produce identical JSON and logs. Every check uses an explicit exception, not an assert statement.

## 6. Scope guard and residual reduction

A concrete exact scope guard is weights (30,1,1,1,1,1,5). The actual complete-extension count is 519684868, and its rank histogram is

(75888,777480,5657872,31164672,129389040,352619916).

All five probabilities Pr(x<Fi) are below 1/3; the largest is Pr(x<F5)=1347298/4191007<1/3. Thus the note correctly refuses to infer an x-to-C6 balanced witness without the endpoint hypotheses. The structural theorem supplies balancedness elsewhere in this example.

The standalone rank theorem excludes v>=5. The separate frozen singleton-upper-spine theorem excludes v>=t+1; its proof and independent audit are copied under dependencies solely to identify that dependency. The v=1 case is also excluded directly: F1=Fv would have both F1<x and x<F1 forced above 2/3 by the two displayed structural rules. Therefore the requested residual family (u,1,b,1,t,1,v) can only have

2<=v<=min(4,t).

In particular v lies in {2,3,4}. This does not settle any of those unbounded slices. This audit does not reclassify the separate generalized-shuffle or other results as dependencies of the standalone v>=5 theorem.

## 7. Frozen evidence

The four original source files and their hashes are frozen under frozen/ and SOURCE_SHA256SUMS. Original source hashes were checked unchanged after all runs. Key source SHA256 values:

- RANK_OBSTRUCTION.md: 68d7c409010fa3552a8b9cfd5cb8b2cf7e88e9fc2abc6897b67dda539888a4fc
- verify_rank_obstruction.py: 41e6c65a9efabe9008c7bd78c09f28b32be4014eefd43aa2837a31ce50a59344
- verification.json: d3988f8cee72c7b548f099f1014cb5fb7bc923918a4fec5c0dcda97ae88f78a4

MANIFEST.json records replay checks and scope. SHA256SUMS covers every deliverable except itself. No publication was attempted and no frozen S114 file was changed.
