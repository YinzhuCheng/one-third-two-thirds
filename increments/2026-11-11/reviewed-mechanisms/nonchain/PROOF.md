# Nonchain minimal-anchor bank: a true-law D10 obstruction family

2026-11-11. Author proof, pending independent review. This is an auxiliary-bank counterexample and an exact transfer-boundary result. It is not a counterexample to the 1/3–2/3 conjecture, the accepted exact Q18 delta3 channel, or any theorem assuming Dc<Y<O saturation.

## 1. What is inherited, and what is new here

Public baseline checked at commit 295ddcda63de8bb3c0f32112302f40dd1610165c:

- `increments/2026-11-10/q18-delta3/CHANNEL_SCOPE.md`.
- `sources/ROOT_INSERTION_KERNEL.md`, especially fixed original minimal anchor, same-event bank, shared original degree budgets, and the prohibition on changing the physical anchor after a word is known.
- `sources/M1_PREVIOUS_UNION_REVIEW.md` and `M2_COMPLETE_REVIEW.md`: fixed-anchor cap transfers through actual Dc restriction fibers; a positive variable-bottom bank does not automatically transfer. Their positive nonchain results use a common physical minimum or a separately proved direct dominant-anchor bank.

Those sources already identify the direction-of-transfer obstacle. The new item below is a self-contained, explicit real-poset family in which BOTH actual chain-orientation bottom banks are strictly positive, yet the fixed original minimal-anchor bank is strictly negative. The mixing weights are the actual extension counts. No claim of literature priority is made. The narrower Q18 result is left unchanged.

## 2. Definition and exact hypotheses retained

For integer n>=1 define P_n on

    {a,b,c,u,v,x,d,z_1,...,z_n}

by the transitive closure of

    a<u, a<v; b<c;
    a<x, c<x; a<d, c<d;
    u<z_1, v<z_1, d<z_1;
    z_1<...<z_n; x<z_n.

For n=1 the same definition applies, so x<z_1 as well. No other relation is added.

The five-point S={a,b,c,u,v} is an induced ideal with exactly a<u,a<v,b<c. The complement of the inclusive a-upset is exactly {b,c}. D(u)=D(v)={a}, and the only a-only children are u,v. Both x and d have full strict downset {a,b,c}; they are incomparable and form a nonchain class above c but not u or v. Thus Dc={x,d}, and x is a physical ORIGINAL minimum of Dc, not a word-selected point.

The actual common strict upset of c,u,v is O={z_1,...,z_n}. All z_i are above d, while x is incomparable with z_1,...,z_(n-1) and below z_n.

The complete original incomparability degrees are:

    deg(a)=2;
    deg(b)=deg(c)=deg(d)=3;
    deg(u)=deg(v)=5;
    deg(x)=n+2;
    deg(z_i)=1 (i<n), deg(z_n)=0.

Hence Delta(P_n)=max(5,n+2). In particular n=5,6,7,8 gives Delta=7,8,9,10.

The fixed-anchor bank, in the uniform law of THIS same original P_n, is

    B_x=K(v<c)+K(x<v)+K(b<a)-N
       =K(b<a)-K(c<v<x),       N=e(P_n).

The identity is pointwise because c<x. All counts below are original full extension counts.

## 3. A six-point calculation without source or word enumeration

Remove x and the z-chain. The remaining six-point H has relations

    a<u,v,d; b<c<d.

Every extension w of H is followed by the z-chain. Write

    j=max(position_w(a),position_w(c)).

Inserting x into w z_1...z_n is legal precisely in the gaps after j and before z_n. There are n+6-j such gaps. This is a deletion/insertion bijection with all full original words, including the true x-versus-z timing. In particular it is not uniform deletion of x.

The value j can only be 3,4,5, and the counts in these classes are as follows:

- j=3: the first three letters are abc,bac,bca, followed by an arbitrary permutation of u,v,d. There are 18 words, 12 with b<a and none with v<c.
- j=4: c is the fourth letter, exactly one w in {u,v} appears before c, and the first three letters are an ordering of a,b,w with a<w. There are 3 choices for that order, 2 choices for w, and 2 orders of the remaining pair, hence 12 words. Exactly 4 have b<a. Exactly 6 have v<c, obtained by w=v.
- j=5: the first four labels are a,b,u,v with a before u,v. There are 8 orders; then c,d. Exactly 2 have b<a, and all 8 have v<c.

Therefore

    N=18(n+3)+12(n+2)+8(n+1)=38n+86,
    K(b<a)=12(n+3)+4(n+2)+2(n+1)=18n+46,
    K(v<c)=6(n+2)+8(n+1)=14n+20.

For a given H word, x<v contributes max(0,position(v)-j) insertion gaps. At j=3, each of the three root prefixes has two suffix orders for each v-position 4,5,6, contributing 2(1+2+3)=12, hence 36 in all. At j=4, only the case w=u contributes; for each of the three prefixes the two suffixes put v at 5 or 6 and contribute 1+2=3, hence 9. The j=5 case contributes zero. Consequently

    K(x<v)=45.

It follows identically for every n>=1 that

    B_x=(18n+46)+(14n+20)+45-(38n+86)=25-6n.

For n=5..8 the original B_x is respectively -5,-11,-17,-23. This disproves the assertion that an original seed/private/D10 poset automatically has positive unit bank at every original minimal Dc anchor. The precise stronger hypotheses of the accepted Q18 theorem are not satisfied.

For later fiber checks one also has

    K(d<v)=12n+33.

Indeed the j=3 class has 9 words with d<v, each weighted n+3; the j=4 class has 3 such words, each weighted n+2; the j=5 class has none.

## 4. Both true orientation-bottom banks are positive

Partition the ORIGINAL LE(P_n) by the actual relative order of x,d. Let P_n^+ add x<d and let P_n^- add d<x, in both cases taking transitive closure. Their linear-extension sets are exactly the two disjoint original fibers. The added relations can reduce degrees, and no abstract/free mixture is introduced.

In P_n^+, x<d<z_1 makes the z-chain a terminal ordinal summand. In the H insertion description, x is inserted after j and before d. The genuine insertion multiplicity is position(d)-j.

These same j-classes give

    N^+=36+18+8=62,
    K^+(b<a)=24+6+2=32,
    K^+(v<c)=0+9+8=17,
    K^+(x<v)=24+6=30,
    K^+(d<v)=12+3=15.

For clarity, in the j=3 suffix permutations the sum of the smaller of the relative positions of d,v is 8, hence 3*8=24 for x<v. At j=4 only the w=u case contributes, with three prefixes and both suffix orders contributing one each, hence 6. No arithmetic relies on a listed search output.

The physical bottom of completed Dc in this fiber is x, and

    B_bottom^+=32+17+30-62=17>0.

Subtract the + counts from the exact whole-P counts to obtain the other ORIGINAL fiber:

    N^-=38n+24,
    K^-(b<a)=18n+14,
    K^-(v<c)=14n+3,
    K^-(x<v)=15,
    K^-(d<v)=12n+18.

Here the completed Dc bottom is d. Its unit bank is

    B_bottom^-=(18n+14)+(14n+3)+(12n+18)-(38n+24)
              =6n+11>0.

Thus each actual completed-source bottom has a strictly positive bank. Nonetheless the bank for the ORIGINAL fixed physical x is

    B_x=B_x^++B_x^-=17+(8-6n)=25-6n<0 (n>=5).

This is a genuine true-weight failure of variable-bottom-to-fixed-anchor bank transfer. The actual fiber masses are 62 and 38n+24, not freely chosen weights. It does not show failure when the physical anchor is bottom in every completion, or when a separate direct original bank has been proved.

## 5. What does survive: exact union-event transfer and fixed-event cap transfer

There is a valid general statement behind the failed route. Let E_t be a disjoint partition of LE(P), possibly induced by completing a subposet D. Fix original events F_1,...,F_s and a number c, and suppose for each cell

    sum_j alpha_j K_t(F_j)+K_t(b_t<v)-c N_t>=0,

where b_t is the first D label in that cell, and alpha_j,c do not depend on t. Summing yields exactly

    sum_j alpha_j K_P(F_j)+K_P(any D label before v)-cN>=0.

Reason: b_t<v is equivalent in the t-cell to the earliest D label preceding v, namely the fixed original UNION event. It is generally not equivalent to z<v for a prescribed z in D.

If there is one original least x in D then b_t=x in every cell, and the same sum is a valid original fixed-x bank. More generally, a separate identity/inequality controlling the discrepancy

    K(any D before v)-K(z<v)

is required; positivity of the union bank alone does not control it. In the family above the union-bank margin equals

    B_union=B_bottom^++B_bottom^-=6n+28>0,

while

    B_union-B_x=12n+3.

By contrast, an upper cap for every completed bottom DOES transfer to a fixed z: since b_t<=z in the completion,

    {z<v} subseteq {b_t<v}.

Thus K_t(z<v)<=K_t(b_t<v)<=beta N_t sums to K_P(z<v)<=beta N, strictly if the cell bounds are strict. This is the existing one-sided containment mechanism in the public m1/m2 review, recorded here to state the exact surviving direction. It is not asserted as a new project theorem.

## 6. A whole-class closure of the obstruction

Let R be any finite poset and form P_n ordinal-sum R, placing every P_n label below every R label. Then

    e(P_n ordinal-sum R)=e(P_n)e(R),
    K(F)=K_Pn(F)e(R)

for every event F involving only original P_n labels. In particular the bank becomes (25-6n)e(R), so its sign remains negative for n=5..8. Degrees inside each summand are unchanged. If Delta(R)<=10 then the whole poset still has Delta<=10. The induced seed ideal, its private-a complement {b,c}, both original minimal Dc downsets, and the same physical x all persist. Thus already n=8 gives an unbounded-cardinality D10 family of genuine negative fixed-anchor banks, by appending arbitrary D10 ordinal tails.

This uses the standard ordinal-sum extension product (the project's broader neutral-environment preservation was already recorded at S101); the new point is application to the explicit true-law obstruction, not a claim that the product rule is new.

## 7. Exact stopping line: what this family deliberately does NOT satisfy

- Q=P_n minus actual O has 7 points, not actual Q18.
- The occupied A,Cv,Y population contract of the accepted child-u-zero delta3 result is absent; here those classes are empty.
- Most decisively x is incomparable with the initial actual O labels. Hence no Dc<Y<O shield and no mandatory first-O ideal containing the same bank anchor can be imported. The public Q18 proof uses precisely that saturation protection.
- u and v are full twins. Also b,a is closed-balanced, since
  3K(b<a)-N=16n+52>0 and 2N-3K(b<a)=22n+34>0. Therefore these examples are explicitly NOT no-balanced-pair objects and not guard-free residual sources.
- The new family refutes a broad automatic-bank claim and the true variable-bottom transfer. It does not reopen or refute the narrow Q18 channel, nor disprove existence of some good anchor (d itself has B_d=6n+13>0).

## 8. Computation and status

The proof above is the basis for the infinite formulas. `verify_countercontrol.py` independently computes full original ideal-DP counts at n=1..8 and both actual orientation fibers, checks all degrees and the original seed/private/signature conditions, and compares to these formulas. It is a small exact arithmetic cross-check, not a prerequisite for the analytic result or an enumeration-based general theorem.

Earlier exploratory search scripts and outputs are retained as diagnostics. They found no negative MINIMAL anchor in a finite sampled exact delta3 Q18 channel, but that observation is not used in any theorem. The negative upper-anchor sample in `TRUE_BANK_SEARCH.json` is not a minimal-anchor counterexample. No GitHub or Notion write was made.
