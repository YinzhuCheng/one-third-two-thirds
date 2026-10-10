# Generalized shuffle bounds and a finite pendant cone

Date: 2026-10-10. Status: direct proofs below; author exact checks are in `verification.json`; independent audit is recorded separately. No all-weight balance theorem is claimed.

## 1. Poset and main results

Let Q have covers

0<3; 1<2,4; 2<3,6; 3<5; 4<5.

Replace vertex i by a nonempty chain C_i. Put

(w0,w1,w2,w3,w4,w5,w6)=(u,a,b,c,t,d,v),

and write B_i,T_i for the first and last elements of C_i. The law is uniform on the complete linear extensions of the inflated poset, equivalently uniform on valid block words. It is not uniform on the seven-point quotient.

**Theorem 1.** For every positive integer weight vector,

Pr(B2<B4) < (b+c+v)/(b+c+v+t),                         (1)
Pr(T4<T3) < (b+c+u)/(b+c+u+t).                         (2)

The strict inequalities can be weakened to non-strict inequalities without affecting any consequence below.

The previously established structural-good-pair theorem says that a counterexample to the 1/3–2/3 conjecture in this family must satisfy both Pr(B2<B4)>2/3 and Pr(T4<T3)>2/3. Therefore every such counterexample satisfies

2t < b+c+v,   2t < b+c+u.                             (3)

Together with the already established necessary inequalities

2u < a+b+t+v,   2v < u+c+t+d,                         (4)

and the singleton-port prerequisite u,v≥2, these leave only finitely many (u,t,v) once the four spine weights (a,b,c,d) are fixed. The exact finite envelope is given in Section 5.

Here and throughout, a failed necessary forced orientation proves that some balanced incomparable pair exists by the structural theorem; it need not prove that the particular tested endpoint pair is balanced.

## 2. Weighted binary-shuffle lemma

Let A,S,C be chains of lengths m,k,t, with m≥0, k,t≥1. Write S=(S1,...,Sk), and impose exactly the additional cross-relations A_i<S_q for every A_i, where 1≤q≤k. Under the uniform complete-extension law,

Pr(S1<C1) ≤ k/(k+t).                                  (5)

Proof. Fix a binary S/C shuffle, and let R be the position of S_q in that binary word. The A elements may be inserted in the R gaps before S_q in

W(R)=binom(m+R−1,m)

ways. Consequently the binary-shuffle law is uniform initially, then weighted by the positive, nondecreasing function W(R).

For the uniform binary law, E={S1<C1} is the event that the first symbol is S, and Pr(E)=k/(k+t). Conditional on E, the S positions are {1} together with a uniform (k−1)-subset of {2,...,k+t}. Conditional on the complement, they form a uniform k-subset of the same set.

Couple these two laws by choosing a uniform k-subset U of {2,...,k+t} and deleting one uniformly chosen member to get V. The deletion law on V is uniform. If q=1, the ranks of S_q in the two coupled words are 1 and min(U). If q≥2, they are V_(q−1) and U_q, and V_(q−1)≤U_q. Thus R conditional on E is stochastically no larger than R conditional on its complement. Hence

E[W(R)|E]≤E[W(R)|not E].

Reweighting a two-event partition by these conditional means cannot increase Pr(E). This proves (5), including m=0, when W is constant. QED.

## 3. Full-weight conditioning proof

Fix a complete extension, and condition on all three of the following data:

1. The entire prefix P through and including T1.
2. The entire suffix R from and including B5.
3. The relative word S of all elements of C2, all elements of C3, and the C6 elements that precede B5.

These data are taken from an actual extension, so they are feasible. They also determine i, the number of C0 elements in P, and f, the number of C6 elements before B5.

Before T1, only C0 and C1 can occur. Therefore P is a fixed shuffle of the first i C0 elements and all a C1 elements, ending in T1. In particular, no C2,C3,C4,C5,C6 element occurs in P. This fixes every C0/C1 interleaving even when a>1.

At B5, all of C0,C1,C2,C3,C4 have already occurred. Consequently R is a fixed shuffle of all d C5 elements and the last v−f C6 elements, beginning with B5. This fixes every C5/C6 interleaving even when d>1. Fixing the full suffix, rather than only f, is important.

The open segment between T1 and B5 consists exactly of:

- the remaining m=u−i elements of C0, called A;
- all t elements of C4, called C;
- the fixed word S, of length k=b+c+f.

Since every C2 element precedes every C3 and C6 element, the first element S1 is B2. Regard the fixed relative word S as one chain. Let q be the position of B3 in S; in particular b+1≤q≤k. Among A,S,C, the only extra cross-relation is that all elements of A must precede S_q=B3. There is no C0/C4, C0/C6, or C4/S relation. All predecessor relations from C1 have been completed in P, and all successor relations into C5 are satisfied by ending the middle segment before R.

Every legal shuffle of these three chains with A<S_q gives exactly one full extension after adjoining P and R. Conversely, every full extension with the conditioned data gives exactly such a shuffle. This is a bijection. The conditional middle law is therefore uniform, even though different fibers have different cardinalities.

The event B2<B4 is exactly S1<C1 within this middle segment. The lemma gives

Pr(B2<B4 | P,R,S) ≤ (b+c+f)/(b+c+f+t)
                  ≤ (b+c+v)/(b+c+v+t).

Average over the fibers to obtain the non-strict version of (1). For strictness, there is a valid full extension with f=0: the block order C0,C1,C2,C3,C4,C5,C6 is one such extension. Its fiber has positive probability, and since v,t>0 its first upper bound is strictly smaller than the final bound. Thus the average is strictly smaller as well.

The order-reversing quotient involution is (0 6)(1 5)(2 3), fixing 4. Reversal of full extensions sends the weights to

(v,d,c,b,t,a,u).

It sends the event B2<B4 in the dual poset to T4<T3 in the original poset. Applying (1) to this transformed vector proves (2). No equality of an arbitrary vector with its dual is assumed. QED.

## 4. Structural dependencies and necessary inequalities

The application to hypothetical counterexamples uses the same previously audited good-pair prerequisite as the earlier singleton-spine proof. In the quotient, D(2)=D(4)={1} and U(4) is contained in U(2), so the bottom lift requires Pr(B2<B4)>2/3 in a poset with no balanced pair. Its dual requires Pr(T4<T3)>2/3. These prerequisites concern the actual inflated law.

Combining either strict forced probability with the corresponding upper bound gives b+c+v>2t and b+c+u>2t, proving (3). The earlier endpoint insertion arguments give (4). The singleton-port prerequisite u,v≥2 is separate and is used only in the finite enumeration.

For completeness, the established linear insertion arguments for (4) can be summarized as follows. Delete C0 and fix an outside extension. Its insertion window begins at the first outside element B1 and ends immediately before B3; it has h≤a+b+t+v elements. Conditional on this outside extension, the C0 insertions are uniform binary shuffles, so Pr(B0<B1)≥u/(u+a+b+t+v). The required opposite orientation Pr(B1<B0)>2/3 implies the first inequality in (4). Duality gives the second. This conditioning does not assume a uniform deletion law.

The external structural theorem used by these prerequisites is Zaguia's good-pair theorem, Definition 1 and Theorem 2, https://arxiv.org/html/1610.00809 . Its precise use and the singleton-port cycle prerequisite were independently audited in the preceding research packages; they are dependencies, not consequences of this new shuffle lemma.

## 5. Exact finite integer envelope for pendant weights

Fix positive integers (a,b,c,d). Define

s=b+c,   α=a+b−1,   β=c+d−1,
U=floor((2α+β)/3),   V=floor((α+2β)/3),
T=s−1+min(U,V).                                      (6)

Since α,β≥1 and s≥2, we have U,V≥1 and T≥2.

**Theorem 2.** Every hypothetical counterexample with these four spine weights belongs to the following finite set:

1≤t≤T;
ℓ_t=max(2,2t−s+1)≤u≤t+U;
max(ℓ_t,2u−t−α)≤v≤floor((u+t+β)/2).                 (7)

Empty integer intervals contribute no triples. Conversely, (7) is exactly the set of positive integer triples satisfying u,v≥2 and all four linear inequalities (3)–(4). This converse is only about the inequality relaxation, not about counterexamples.

Proof. By integrality, the four inequalities are equivalent to

2u−v≤t+α,   2v−u≤t+β,
u≥2t−s+1,   v≥2t−s+1.                              (8)

Combining twice the first upper inequality with the second gives 3u≤3t+2α+β, so u≤t+U. Similarly v≤t+V. Combining these upper bounds with the lower bounds in (8) gives

t≤s−1+U,   t≤s−1+V,

hence t≤T. Solving (8) for v at fixed (t,u), and adjoining u,v≥2, gives exactly (7). Every triple in (7) satisfies (8), proving both directions. QED.

The cap T is sharp for this relaxation, and each fixed t with 1≤t≤T admits a triple in it. Indeed, choose

u=t+U,   v=t+V.                                     (9)

We have 2U−V≤α and 2V−U≤β. To see this, let r=(2α+β) mod 3 and q=(α+2β) mod 3. The only possible pairs (r,q) are (0,0),(1,2),(2,1), so 2r−q and 2q−r are nonnegative. Substitution into the definitions of U,V proves the claims. Also min(u,v)=t+min(U,V)≥2t−s+1 exactly when t≤T, and u,v≥2. Thus (9) satisfies all four inequalities and both port constraints. At t=T it attains the cap, and also attains the individual universal upper bounds u≤T+U, v≤T+V.

The sharper cap is equivalently the pair of inequalities

3t≤2a+d+5b+4c−6,
3t≤a+2d+4b+5c−6.                                  (10)

A simpler, sometimes weaker bound follows directly by adding the two upper inequalities in (8) and the two lower ones:

2t≤a+d+3b+3c−4.                                    (11)

Thus the proposed symmetric arithmetic bound is valid; (6) gives the exact cap for this four-inequality integer relaxation.

Example: a=b=c=d=1 gives U=V=1 and T=2. The exact envelope contains only (u,t,v)=(2,1,2),(3,2,3). These are two of the small cases already explicitly excluded in the earlier singleton-spine proof; the new inequality itself rejects (2,2,2). Thus the general bound gives another finite reduction of that entire three-parameter family.

The range is finite only after all four spine weights are fixed. This does not bound a,b,c,d or the total order globally, and does not exclude every point of the finite cone without further tests.

## 6. Exact new endpoint numerator

An efficient exact formula checks the new bottom endpoint without enumerating complete extensions. Set

K(i,j)=binom(a+b+i+j−1,i)
       binom(u−i+c+t−j,t−j)
       binom(u−i+c+t−j+d+v,v).

Define H_b(0)=1. For j>0, define H_1(j)=0 and, when b≥2, H_b(j)=binom(b+j−2,j). Then

N24= e(P with B2<B4) = sum_(i=0)^u sum_(j=0)^t H_b(j)K(i,j),       (12)
Z  = e(P)           = sum_(i=0)^u sum_(j=0)^t binom(b+j−1,j)K(i,j). (13)

Proof. Split after T2, letting i,j count C0,C4 elements before T2. Delete the i C0 elements and the final T2 from this prefix. After all a C1 elements, the remaining word is a shuffle of b−1 C2 elements and j C4 elements. If j=0, B2<B4 is automatic. If b=1 and j>0, it is impossible. If b≥2 and j>0, the shuffled word must start in C2; this gives binom(b+j−2,j) words. Reinsertion of C0 gives the first factor of K. After T2, the residual C0 followed by C3 is a chain, freely shuffled with residual C4, all followed by C5; the free C6 chain is then inserted. This gives the other two factors of K. This decomposition is bijective. QED.

Apply (12) to the dual vector to count T4<T3. Formula (13) is the previously established total count; it is included here to make the implementation self-contained.

## 7. Verification and limitations

`verify_generalized_shuffle.py` uses exact Python integers and no external packages. It checks (12)–(13), their dual counterparts, and the strict probability bounds against a separate block-state recurrence. It also exhaustively checks the finite-envelope arithmetic and its claimed extremal witnesses over a bounded spine box. All checks remain active under Python optimization. The author run passed 2,255 weight vectors, 6,765 independent block-state DP counts, 4,510 strict probability inequalities, all 121,327 complete extensions in the {1,2}^7 box across 3,192 conditioning fibers, and 350,020 finite-cone membership comparisons for all 256 spine vectors in {1,2,3,4}^4. The 1,892 claimed componentwise extremal witnesses also passed. Finite computations validate the implementations, not the universal proof.

The newly proved results are the two uniform full-weight probability bounds, the resulting necessary inequalities, the exact finite pendant cone for fixed four spine weights, its sharp linear-relaxation cap, and the endpoint numerator formula. No seven-weight all-balanced theorem and no new global finite reduction are claimed.
