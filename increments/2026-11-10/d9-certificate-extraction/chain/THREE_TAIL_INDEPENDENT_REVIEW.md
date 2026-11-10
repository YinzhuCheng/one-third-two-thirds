# Independent review: analytic three-common-leaf bank

2026-11-10. Internal independent mathematical review, not external peer review, formal verification, or originality certification. **PASS** for THREE_TAIL_FOUR_EVENT_ANALYTIC.md T1–T7, with the exact scope below. The source/state is Fathi v22 §24.4.1, https://zenodo.org/records/23933091. The proof reuses the established original-ideal insertion and fixed-event counting logic; its new analytic application is not attributed historical novelty.

## Verified result

For the original seven-label ideal with a<u,v and a,b,u<t1,t2,t3, three incomparable leaves, exterior entirely above v, and local incomparable degree at most9 at each leaf, the FIXED physical-event bank

    6 Pr(u<b)+Pr(v<u)+Pr(t2<t1)+Pr(t3<t2)>3

holds for every fixed leaf naming. No degree bound on a,b,u,v is needed. The proof is analytic throughout this gate: the prior2408-profile positive replay is now corroborating evidence, not a remaining dependency. The negative third-event-menu certificates and their restricted quantifiers remain valid.

## Original law and cap audit

The retained Q is a full original ideal, so no exterior letter precedes a marked label in the poset. Exterior-above-v implies h_a=h_v=0 in every actual exterior word. Each leaf has exactly three internal incomparable partners, v and its other two leaves; degree<=9 gives its exterior deadline<=6. The relations b,u<all leaves force B=h_b and U=h_u below the least leaf deadline. Thus the entire conditional count domain is exactly covered by0<=B,U<=x<=y<=z<=6 after temporarily sorting leaf deadlines. This does not assume NB on a conditional helper, and it does not use uniform mixing of deadline profiles.

The same fixed event bank is used for every exterior word. Sorting the leaf caps only supplies a lower bound for that bank's leaf contribution; it does not select different events before averaging. Strictly positive count margins in every actual fibre sum using the actual full-completion counts, yielding strict>3 in the original finite P, including the empty-exterior case.

## Independent leaf-order check

Sequential insertion into the fixed exterior chain gives F=L1 L2 L3 for ordered slot bounds L2>=L1+1,L3>=L2+1. If a,b denote the sorted adjacent reversal probabilities, then

    a=(L1+1)/(2L2), b=(L2+1)/(2L3),
    q31=(L1+1)(L2+1)/(2L2 L3)=2ab,
    0<a,b<=1/2.

The third formula follows by taking the expected position of the first leaf after inserting the second, then inserting the third uniformly. It also applies to the plus model containing the extra cap-zero v before the exterior chain.

For the six physical reference orders the two-adjacent-reversal sum, minus a+b, is respectively

    0, (1-a)(1-2b), (1-b)(1-2a),
    1-a-2ab, 1-b-2ab, 2(1-a-b).

All are nonnegative on0<a,b<=1/2. This independently verifies the author's three-label interval/run lower bound without introducing a correlation assumption about P. Both F and F_plus models have the same deadline-sorted leaf order, and their coefficients in the full margin are positive, so their lower bounds can be combined.

## Independent root-gap reconstruction

For j>=1 the root gap is max(g_b,g_u)=j; a,v are already in gap0. If u is later, b's possible positions contribute3+min(B,j), with three orders in gap0; if b is later, u contributes2+min(U,j), with two gap0 orders. The same-gap roots contribute the appropriate distinct orders to those two classes. Therefore the author's c_j,a_j,d_j coefficients are correct. In particular, among the b-later placements exactly one has u before v, explaining d_j=c_j-1[j<=B].

I independently obtained the three regimes:

    (2j+1)F_j+(2j+5)W_j                 j<=min(B,U),
    (B+3)(W_j-2F_j)                    B<j<=U,
    (4U+7)F_j+(U+2)W_j                 U<j<=B.

At j=0, the five orders with v before the last b/u root contribute(N,K_A,K_B)=(5,2,4)F_0. The other three fix the a,b,u order and interleave a cap-zero v with the leaves after that last root, contributing(3,1,0)F_plus. Thus the margin's zero-gap part is exactlyF_0-3F_plus+5W_0+3W_plus. This root partition covers every extension once; it is not a sampling identity.

## Monotonicity and strictness audit

For j>=1 the sorted probabilities give0<W_j<=F_j. Since L1>=1 and L3<=8,

    2W_j/F_j >= 2/L2+(L2+1)/8>1.

The last inequality is equivalent to L2²-7L2+16>0, whose discriminant is-15. Also F_j strictly decreases while positive.

Increasing B from k-1 to k<=U changes the lower margin by exactly

    (4k+5)F_k+(k+3)W_k+sum_(j=k+1)^U(W_j-2F_j).

Using W_k>F_k/2, W_j>=0 and F_j<=F_k gives at least[(13k+13-4U)/2]F_k. With k>=1,U<=6 this is at least F_k>0. For k>U only a new positive b-later term appears. Thus B=0 is the minimum. With B=0, increasing U adds3(W_j-2F_j)<0, so U=x is the minimum. Neither argument silently varies the allowable leaf domain.

The resulting polynomial m(x,y,z) was independently reconstructed from the finite symbolic sum, not fitted to profile values. Its z slope is exactly the negative expression in T5 and is strictly negative for y>=x>=0, so z=6 is the minimum. The coefficients of4m(x,y,6), the expression4AC-B², and its x=t+1 expansion match the author's formulas identically. For x=0 the latter is3548. For1<=x<=6, 0<=t<=5 makes604-28t>=464>0; every other displayed coefficient is nonnegative and the constant45680 is positive. Hence4AC-B²>0 and A>0, so the quadratic is strictly positive for every real y.

This proves the desired strict margin on the entire integer cap domain. The argument does not prove the diagnostic minimum11 is optimal, and it does not need that minimum. THREE_TAIL_INDEPENDENT_ALGEBRA.py checks the symbolic identities only; there is no deadline-profile enumeration in this analytic verification.

## Independent original-packet coverage and deduplication

THREE_TAIL_INDEPENDENT_REVIEW.py independently searched the original packet by structural boundary labels and actual subideal Q_source minus U_Q_source(v), checking the complete seven-label shape and the reference restriction b before u before v. It found exactly six terminal rows, the six physical permutations of the leaf order on(0,0,1,1,7,7,7). None belongs to the prior390-row union. All charged endpoints have at most three full predecessors. For each such row, v is the only structurally exhausted usable reverse anchor; choosing y=u gives exactly the three leaf blockers, so their minimum frontier size is3.

Therefore the deduplicated analytic payment union grows from390 to396 of the3469 existing source bank occurrences, leaving3073. This does not replace the structural canonical-prefix/phase coverage proof, other D9 batches, or any D10 theorem. Marked successors of v may be put in the analytical exterior without deleting remembered marks from the actual phase state.

## Independent actual D10 stopping line

The full14-point forward ideal DP independently verified h=(0,0,0,0,0,2,7) on the same Q and a seven-chain exterior:

    N530, K_A190, K_B160, K_C21=149, K_C32=140,
    Delta10, bank margin-1.

There is also a direct second count from the root-gap model: B=U=x=0 givesF=40,F_plus=110, W=20,W_plus=63. Thus N=5F+3F_plus=530, K_A=2F+F_plus=190, K_B=4F=160; the two physical sorted leaf events have counts149 and140 by the insertion ratios. The same symbolic margin is40-330+100+189=-1. Thus the D10 control is verified by a full original-poset DP and by closed root-gap counts, not just by an altered cap-vector formula.

The pair u,b is already balanced,190/530=19/53. The construction has two minima, singleton private branch{b}, and all exterior above v. It refutes only raising the same leaf cutoff6 to7 in this same bank. It is not NB, not an ordinary-balance counterexample, and not an obstruction to another D10 bank.

## Additional independently checked D9 exposure stopping line

THREE_TAIL_EXPOSURE_INDEPENDENT.py constructs the original13-point poset from the same Q7 and six-chain, now with

    h=(0,0,0,1,0,2,6).

A forward ideal-subset DP and a separate direct enumeration of complete linear-extension words both give

    N630, K_A222, K_B144, K_C21=165, K_C32=185,
    6K_A+K_B+K_C21+K_C32-3N=-64, Delta9.

The full principal-upper-complement K_v=P minus U_P(v) is exactly the first eight physical labels and has predecessor array(0,0,1,1,7,7,7,23). Its additional eighth mark is the actual v-incomparable z1. All remaining original exterior labels are above v, so this is a legal remembered-pivot exposure, not a zero inferred from a single conditional word.

The original seven-label Q in this P is NOT at v exhaustion: z1 remains incomparable with v, reflected by h_v=1. After legally exposing it, the ideal no longer has the seven-label three-common-antichain shape required by T1. This is NOT a preservation counterexample starting from an already-applicable seven-label theorem: once v is genuinely exhausted there is no remaining v-incomparable to expose. Thus this degree-nine control does not refute the proved gate; it precisely prevents blindly transporting the same four physical events and coefficients to the adjacent larger Q8 memory state. The event A is already balanced,222/630=37/105, so this is not NB or an ordinary-balance counterexample. It identifies a next structural payment bridge, rather than a failure of legal exposure.
