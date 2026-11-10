# One remembered incomparable above the middle common head

2026-11-10. Author analytic proof; internal independent review PASS in MIDDLE_HEAD_INDEPENDENT_REVIEW.md. Continuation of THREE_TAIL_FOUR_EVENT_ANALYTIC.md. This extends an actual marked interface, not payment under arbitrary exposure.

## MH1. Original-object contract and fixed bank

Let the ORIGINAL ideal Q8 have labels a,b,u,v,t1,t2,t3,z. On the first seven labels it has exactly a<u,v and a,b,u<ti, with v incomparable with b,u and all three pairwise incomparable ti. The extra z is incomparable with v and has full strict downset `{a,b,u} union S`, where S is a subset of the three leaves containing t2. It has no other relation inside Q8. Every original exterior label lies above v. Each ti has full incomparable degree<=9; no other degree cap is needed.

For the fixed PHYSICAL leaf reference t1,t2,t3, one has in this same original P

    6 Pr(u<b)+Pr(v<u)+Pr(t2<t1)+Pr(t3<t2)>3.       (MH1)

Thus a candidate strict-two-thirds reference with b before u before v and this leaf order is excluded under ORIGINAL NB. The bank does not contain z, and it is not selected after conditioning. Its total weight is9.

## MH2. Legitimate fixed-word reduction

Put Q7=Q8 minus z. It remains an original ideal. Fix one actual complete word omega of P minus Q7, including the physical z. All these exterior labels except z are above v. Since z||v,

    V=h_v is0 or1.

If V=1, z is the first exterior letter, and z>t2 implies

    h_a=h_b=h_u=h_t2=0.

Every tail deadline is<=6 by its three Q7 incomparable partners and its full degree<=9. If V=0, apply the already audited Q7 count inequality for h_v=0 DIRECTLY to this fibre. This does not assert that v is exhausted at Q7 in the original P; it reuses the per-word count proof, without NB on a helper or any relabelled event.

It remains to prove the bank on the whole V=1 fibre. Here b,u occupy gap0 and v is allowed in gaps0 and1. Their positions must be summed with their actual counts, not conditioned or mixed uniformly.

## MH3. A middle head gives a stronger leaf-order lower bound

Temporarily sort the two other leaf deadlines, writing0<=a0<=b0<=6; t2 has deadline0. This sorting does not change the fixed physical bank. In any of the flag models below, put the deadline-zero middle head first in sorted order. The pair law in THREE_TAIL T2 gives nearest reversal q and endpoint reversal r with q>=r. If the physical t1 has the smaller of the other deadlines, the physical sum is1-q+r; if t3 has the smaller deadline it is1+q-r>=1-q+r. Thus1-q+r is a uniform lower bound for the SAME two physical events.

For L=(L1,L2,L3), write F=L1 L2 L3. The lower count is

    W_mid=F-K_nearest+K_endpoint.

All three models preserve this argument even when deadlines tie.

## MH4. Exact v-gap decomposition at V=1

Abbreviate a=a0,b=b0.

For the gap0 placements of v, the audited zero-gap root count has baseline flags(1,a+2,b+3) and plus flags(2,a+3,b+4). In these models,

    F0=(a+2)(b+3),       W0=F0+a-b,
    Fplus=2(a+3)(b+4),   Wplus=Fplus+3(a-b).

The count margin6K_(u<b)+K_(v<u)+K_(t2<t1)+K_(t3<t2)-3N contributed by these placements is therefore at least

    F0-3Fplus+5W0+3Wplus =6F0+14(a-b).          (MH2)

Now put v in gap1. Delete v and the leaves. There are exactly three orders of a,b,u, of which one realizes u<b; v<u is false. Treat v as one additional base letter at gap1, then insert the three leaves. If Fextra is the leaf completion count and Wextra the physical-leaf lower count in this model, the additional margin is exactly bounded below by3(Wextra-Fextra). This sums all such lifts, not a selected v position law.

- If1<=a<=b, flags are(1,a+3,b+4), and Wextra-Fextra=a-b. Adding this to MH2 gives

      6(a+2)(b+3)+17(a-b)
        =(6a-5)b+35a+36>0.

- If a=0<b, flags are(1,2,b+4). Thus Wextra-Fextra=-(b+1), and the total margin is at least

      33-5b>=3>0.

- If a=b=0, flags are(1,2,3), Wextra=Fextra, and the total lower margin is36>0.

These cases prove strict positivity throughout every V=1 fibre. Together with the already proved V=0 fibres, sum the ORIGINAL full-completion counts over omega. This proves MH1 without a finite deadline certificate.

## MH5. Remembered-pivot use and limitations

At a retained source state, require the true original ideal K_v=P minus U_P(v) to have precisely this eight-label structure. A permanently exhausted v, a terminal v, or saturation of its internal incomparable degree can establish that the marked K_v is complete. Already marked successors of v may be included in the analytical exterior, without deleting them from actual phase memory.

The extra physical z is not forgotten. It is included in the actual conditioning word, and its exact incidence z>the middle head is the reason V=1 forces the three zero deadlines. This is a lawful original-P reduction, not a pivot switch inferred from one zero deadline. The proof does not claim that a previously exhausted seven-label interface could gain a new v-incomparable: that is impossible by exhaustion.

The neighboring Q8 control with z above the FIRST physical head does not contradict this theorem. It deliberately fails the middle-head incidence. Nor does this prove payment for two or more extra v-incomparables; V<=1 is an exact structural hypothesis. The charged endpoints still have at most three full predecessors.

## MH6. More than one incomparable, when only the middle branch supports them

There is a complementary extension not requiring exactly one extra label. Replace z by an induced poset E in the original ideal K_v. Require every member of E to be above t2 and incomparable with v,t1,t3; the order within E is arbitrary. Keep the complete Q7 root/head relations and require every original exterior label of K_v to be above v. Then the SAME fixed bank MH1 holds, with the same three leaf degree caps9.

This sets no additional explicit bound on |E|, but it is NOT an unbounded-memory theorem: t1 and t3 each have their three original incomparable partners plus all E, so the leaf degree condition itself implies |E|<=6. The positive-gap formula below does not separately use that cardinal bound.

Project E into the actual exterior word of Q7. If V=h_v=0, use the previously proved conditional count bank. If V>0, all of the first V exterior letters must be members of E. They force B=U=h_t2=0, while t1,t3 are incomparable with every one of them. Hence, after sorting only their two deadlines,

    1<=V<=a<=b<=6.

v may occupy any exterior gap0,...,V. Gap0 contributes the same MH2 lower bound. For each j=1,...,V, both non-head deadlines are at least j, so treating v as one extra base letter gives exactly the flags(1,a+3,b+4). Each such gap contributes the additional lower margin3(a-b). Summing ALL v placements with their actual multiplicity gives

    M>=6(a+2)(b+3)+(14+3V)(a-b)
      =(6a-2-3V)b+(32+3V)a+36>0,

because a>=V>=1 implies6a-2-3V>=3V-2>0. Thus the one-extra/multiple-supported-head gate MH1 and the multiple-extra/only-middle-supported gate MH6 are two complementary structural sufficient conditions. The latter must not be applied when some E is also above t1 or t3: then a>=V need not hold.

## MH7. Source coverage and next bridge

MIDDLE_HEAD_MEMORY_CENSUS.py scans the unchanged source packet using the complete analytical subideal K_v, retaining every mark in actual memory. The union of MH1 and MH6 matches10 existing source rows: six are the old no-extra Q7 rows already covered by THREE_TAIL, and four are genuinely new terminal rows. The new rows are two references on each of

    (0,0,1,1,7,7,7,23),
    (0,0,1,1,7,7,7,55).

They have the supported head in the middle of their three-head reference. The deduplicated analytic union is therefore400/3469 bank occurrences, leaving3069, not396+10. All charged endpoints have at most three full predecessors. The original phase-coverage proof and every other certificate remain in place. The broader MH6 formula does not increase the source-row count: larger branches of that particular form were already stopped earlier by the source's different unconditional certificates. It remains a valid original-P sufficient class, not a reason to invent additional replaced rows.

The two first-head references on the23 shape are still unpaid analytically here. Q8_PROJECTED_WORD_CONTROL.md records why the source bank cannot simply be asserted on each finer projection word, even though its full original-P weighted sum pays. An extension of MH6 allowing extra labels above another head also requires new information; the current positivity proof uses that other head's original incomparable prefix, not merely the number of marks.

## MH8. Real degree-nine boundary: two supports and two extra labels

The alternative hypotheses MH1/MH6 matter. Keep Q7 and a six-chain, with

    h=(0,0,0,2,0,0,6).

The original13-point poset has Delta9 and complete K_v with predecessor array

    (0,0,1,1,7,7,7,55,183).

There are two extra v-incomparables, both above t1 AND the physical middle t2. They are not only-middle-supported. Exact full original counts are

    N390, (K_A,K_B,K_C21,K_C32)=(136,72,195,69),
    6K_A+K_B+K_C21+K_C32-3N=-18.

MIDDLE_HEAD_TWO_SUPPORT_CONTROL.py/.json and the independent ideal DP/direct390-word enumeration in MIDDLE_HEAD_TWO_SUPPORT_INDEPENDENT.py/.json check the actual relations and counts. Thus one cannot combine the one-extra/multiple-support condition with the multiple-extra/only-middle condition into a multiple-extra/multiple-support assertion using this same bank. A is already balanced and C21 is fair; there is no NB, ordinary-balance, or theorem-preserving-enlargement counterexample.
