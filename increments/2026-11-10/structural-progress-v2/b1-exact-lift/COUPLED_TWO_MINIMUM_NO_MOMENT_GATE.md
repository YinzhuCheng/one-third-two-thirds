# CT1: coupled two-minimum payment without OLD moment

Date: 2026-11-10 UTC. Analytic author candidate for uninvolved review. No original-poset scan or LE DP. A small deadline-sum diagnostic suggested the proof below; no computational positivity table is a proof dependency.

## Theorem

Use the exact original B1 private-predecessor lift, actual full Delta10, and m<=k<=6 with m<=5. Suppose C has a C-minimum c above x and a distinct C-minimum f missing x whose T-signature has size at most1. Then the original physical pair(u,b) is strictly balanced, without OLD seed moment. More precisely for m>=1,

    3K-N >= (17/44)e(C)+2X+Y >0.

The separate m0 bound F>=48 is stronger. The original universal upper bound remains5/9. It is enough to assume the two original C-degree bounds deg_C(c)<=10 and deg_C(f)<=8, rather than reusing a degree bound on a deleted object.

## 1. Keep both selected orders in the same actual fiber

The two minima are incomparable. Delete c,f and fix a genuine gamma in LE(C-{c,f}), but DO NOT fix their relative order. Let R and S be their actual deadlines in gamma. Since the other selected minimum consumes one original incomparable neighbor, R<=9 and S<=7. There is no retained predecessor of either minimum. The low-support f is outside E, above u, and misses at least two T roots, so actual full Delta10 indeed gives its C-degree<=8. Formal padding to nine retained positions, if needed, leaves all actual deadlines unchanged and introduces no additional words.

When f occurs first, write a for its gap and b for c's gap. The exact constraints are0<=a<=S, a<=b<=R. When c occurs first, write a for its gap and b for f's gap; the exact constraints are0<=a<=R, a<=b<=S. Equality of gaps contributes both selected orders, as two different original words. These two sets partition the complete gamma fiber. Its size is exactly

    W(R,S)=(R+1)(S+1)+min(R,S)+1<=88.

There are no arbitrary relative order weights: the same actual R,S govern both pieces of this one original fiber.

## 2. Typed kernel lower bounds

It suffices to use the worst m5,k6 kernel, since increasing either cap can only lower the relaxed kernel. If c is first selected, hx<=min(6,a); put q*=min(5,hx_cap). The standard same-word comparison gives F>=G(a), where

    G(0..5)=(48,46,36,18,-8,-42),
    G(a)=-76 for a>=6.

If f is first selected, hx<=h*=min(6,b+1), and the initial E run is at most a because f is not in E. With q*=min(5,a), we have q*<=h*. Define

    Psi(a,b)=48 if a0;
    Psi(a,b)=48+(6-8q*)h*+4q*(q*-1) otherwise.

For actual q>=1, increasing hx to h* and q to q* lowers the original kernel after discarding9(hy+hz)>=0. If actual q0, F>=48>=Psi. Thus these are pointwise lower bounds; earlier retained x-successors only improve them. They do not require c to have full signature. The initial h/q are the original ones throughout.

Consequently the entire actual gamma fiber has total kernel at least

    T(R,S)=sum_(a=0)^S sum_(b=a)^R Psi(a,b)
           +sum_(a=0)^R (S-a+1)_+ G(a).

Empty inner sums are zero. The following analytic lemma pays every actual deadline pair simultaneously.

## 3. Deadline lemma: T(R,S)>=34

Assume integer0<=R<=9,0<=S<=7. Put

    P_s(h)=sum_(a=0)^s [48+(6-8min(5,a))h+4min(5,a)(min(5,a)-1)],

except that the a0 summand is48, not48+6h. For s0,1,2,3 and1<=h<=6, P_s(h) is positive; at h6 its values are48,84,80,44, and its slopes in h are nonpositive. For s4,...,7, its h6 values are-16,-92,-168,-244.

Writing n=R>=1, direct addition of the new c-gap column and new c-first row gives

    T(n,S)-T(n-1,S)
      =P_(min(S,n))(min(6,n+1))+(S-n+1)_+G(n).

If S<=3, this increment is positive for all n: when n>S only the positive P remains; when n<=S the formulas below are positive. Thus the minimum is at R0.

For S>=4, increments at n1,2,3,4 are respectively

    92+46S, 80+36S, 68+18S, 64-8S,

all strictly positive for S<=7. At n5, the increment is-16 if S4, and76-42S<0 if S>=5. At n6 or7, if n>S the increment is one of the negative P_S(6); otherwise it is212-76S<0. For n8,9 it is simply P_S(6)<0. Hence T increases through R4 and decreases thereafter. In every case the minimum over R is at R0 or R9.

The first endpoint is T(0,S)=48(S+2)>=96. For the second put U(S)=T(9,S). Its increment is

    U(s)-U(s-1)=sum_(b=s)^9 Psi(s,b)+sum_(a=0)^s G(a).

For1<=s<=5 the two elementary arithmetic-series sums simplify to

    D_s=798-(1208/3)s+44s^2-(4/3)s^3.

For5<=s<=7 the increment is-282 (the two expressions agree at5). For s1,...,4,

    D_(s+1)-D_s=-4(s-6)(s-15)<0.

Thus U is discretely concave on0,...,7, so its minimum is at an endpoint. Direct closed-form evaluation gives U(0)=528 and U(7)=34. The latter can also be recovered from the increment sum

    528+438+158-50-194-282-282-282=34.

Therefore T(R,S)>=34 throughout the entire necessary deadline rectangle. This proof uses formulas and monotonicity, not acceptance of a finite computed table.

## 4. Original-word summation

Since each actual gamma fiber has W<=88 words and kernel sum at least34, its average F is at least34/88=17/44. Sum over actual gamma with its true cardinality. The exact identity3K-N=sum F+2X+Y gives the theorem. No seed moment or FKG-conditioned moment is used. No equal weighting of the two orders or distinct retained words is used.

## Scope and present limitation

CT1 covers the notable non-diagonal m5,k6 cell under this actual typed two-minimum hypothesis without OLD moment. It does not prove the whole cell: the only low-support minimum might itself contain x, or there may be no x-containing C-minimum. It is a sufficient fixed-pair theorem, not a statement that failed typed lower bounds are realizable counterexamples.

This theorem does not imply novelty beyond all older guards. For instance RX1 satisfies its typed premise but was already paid by an internal q1,q2 VG configuration; the present theorem additionally certifies u/b there if accepted. Every claimed VG configuration must still be checked in the full original order, not only among the three root-child pairs. No new construction or claim of an object escaping all guards is made.
