# Three common tail labels: a four-event analytic bank at degree nine

2026-11-10. Author proof; internal independent review PASS in THREE_TAIL_INDEPENDENT_REVIEW.md. This analytically replaces a source-bank family in Fathi v22 §24.4.1; no new ordinary-balance class or historical novelty is claimed. It reuses the common-downset insertion/pair law and the at-most-four-label interval/run argument already recorded in FOUR_MARK_ANALYTIC_REPLACEMENT.md, together with exact root-gap decomposition.

## T1. Precise original-object theorem

Let Q be an ORIGINAL induced ideal on a,b,u,v,t1,t2,t3. Its complete relations are a<u,v, and a,b,u<ti for each i; the three tail labels form an antichain and v is incomparable with b,u and all ti. Assume every original exterior label lies above v. Assume each ti has at most nine incomparable partners in P. No degree bound on the other labels is required.

For EVERY fixed naming t1,t2,t3, the uniform extension law of this same P satisfies

    6 Pr(u<b) + Pr(v<u) + Pr(t2<t1) + Pr(t3<t2) > 3.       (T1)

Thus every fixed reference placing b before u before v and t1 before t2 before t3 is excluded under ORIGINAL NB. The bank is chosen before the exterior word, not after it. Total weight is9. This is not a claim that one fixed pair is balanced in every conditional fibre.

Condition on one actual literal exterior word. Write B=h_b,U=h_u and temporarily sort the tail deadlines as x<=y<=z. Ideality/order gives B,U<=x. Each tail already has three marked incomparable partners (v and its two fellow leaves), so

    0<=B,U<=x<=y<=z<=6,  h_a=h_v=0.

All conditional lifts are counted with their true multiplicity. No uniform profile law is introduced.

## T2. Three-label pair/run bound

For independent marked labels with sorted allowable-slot counts L1,L2,L3 satisfying L2>=L1+1,L3>=L2+1, sequential insertion gives total F=L1 L2 L3 and

    q12=(L1+1)/(2L2), q23=(L2+1)/(2L3),
    q13=(L1+1)(L2+1)/(2L2 L3).

These are the probabilities of the reversed comparisons in deadline-sorted order. Write alpha=(L1+1)/L2 and beta=(L2+1)/L3. The interval-block model independently cuts the two sorted gaps with probabilities1-alpha,1-beta; permuting uniformly within blocks gives exactly these pair probabilities. For ANY fixed physical reference order of the three labels, its two adjacent reversal probabilities sum to at least(alpha+beta)/2.

Indeed, for a fixed block partition with b blocks, a reference visiting them in r runs has3-r within-block edges of reversal probability1/2 and d descents of reversal probability1. Relative to the sorted reference the difference is d-(r-b)/2>=0: b1 gives r1, b3 gives r3, and b2 with r3 necessarily has a descent. Average the partitions. This is the previous common-downset/run lemma specialized to three labels, not a new correlation assumption.

Consequently a lower bound for the TWO-event leaf count is

    W=1/2 L1[(L1+1)L3 + L2(L2+1)].                     (T2)

It holds for the fixed physical t1,t2,t3 even when their deadline order changes with the exterior word.

## T3. Exact max(b,u)-gap decomposition

For0<=j<=x define

    L(j)=(x-j+1,y-j+2,z-j+3),
    F_j=product L(j),
    W_j=1/2 (x-j+1)[(x-j+2)(z-j+3)+(y-j+2)(y-j+3)].

Also define F_+,W_+ by using L+=(x+2,y+3,z+4) in the same formulas. The plus case means v is one additional cap-zero independent label inserted before the three leaves.

Let A={u<b}, D={v<u}. We lower-bound the exact integer margin

    6K_A+K_D+K_(t2<t1)+K_(t3<t2)-3N.

Classify lifts by the exterior gap j of the later of b,u. For j>=1 both a,v have already appeared in gap0. If u is the later root, its root-placement multiplicity is (3+min(B,j))1[j<=U]. The3 accounts for the three orders of b,a,v when b occupies gap0. If b is later, its multiplicity is (2+min(U,j))1[j<=B]; the2 comes from the two orders of a,u,v when u occupies gap0. Put

    c_j=(3+min(B,j))1[j<=U]+(2+min(U,j))1[j<=B],
    a_j=(2+min(U,j))1[j<=B],
    d_j=c_j-1[j<=B].

Here c_j is the total root coefficient, a_j the A coefficient, and d_j the D coefficient. In the b-later class exactly one gap-zero root order has u before v. Every leaf must follow the last root, giving F_j completions per root placement and at least W_j leaf inversion count. Thus the contribution is bounded below by

    (6a_j+d_j-3c_j)F_j+c_jW_j.

For j=0 there are five root orders in which v precedes max(b,u), contributing (N,A,D)=(5,2,4)F_0. The other three have v last among the roots; first choose the a,b,u order, then insert v with cap0 jointly with the leaves. Their coefficients are(N,A,D)=(3,1,0)F_+. Therefore the full lower bound is

    M(B,U;x,y,z)=F_0-3F_+ +5W_0+3W_+
      +sum_(j=1..max(B,U))[(6a_j+d_j-3c_j)F_j+c_jW_j].  (T3)

Equivalently the j>=1 summand is

    (2j+1)F_j+(2j+5)W_j,                 j<=min(B,U);
    (B+3)(W_j-2F_j),                     B<j<=U;
    (4U+7)F_j+(U+2)W_j,                  U<j<=B.

This is a counting identity plus the uniform leaf-run lower bound, not an enumeration of cap profiles.

## T4. Uniform minimization in the two root deadlines

For j>=1, 0<W_j<=F_j. Also W_j>F_j/2. To see the latter, L1>=1,L2>=2,L3<=8 give

    2W_j/F_j >= 2/L2+(L2+1)/8 >1,

since L2^2-7L2+16 has negative discriminant and positive leading coefficient. The F_j are positive and decrease with j.

Fix U and increase B from k-1 to k. If k>U the newly added term is positive. If1<=k<=U, the difference is

    (4k+5)F_k+(k+3)W_k
          +sum_(j=k+1..U)(W_j-2F_j)
    >= [(13k+13-4U)/2]F_k >= F_k>0,

using U<=6, k>=1, the half-F bound and F_j<=F_k. Therefore B=0 is the worst root deadline.

At B=0 the j>=1 terms are3(W_j-2F_j)<0. Increasing U only adds such terms, so U=x is worst. Hence

    M(B,U;x,y,z)>=M(0,x;x,y,z)=:m(x,y,z).

Explicitly

    m=F_0-3F_+ +5W_0+3W_+
                       +3sum_(j=1..x)(W_j-2F_j).       (T4)

## T5. One polynomial proves the entire remaining domain

The finite sum in(T4) is evaluated by the ordinary formulas for sums of powers. It is affine in z. Writing a=y-x>=0, its z coefficient is

    -[3x^3+5x^2+6ax^2+10ax+10a+4]/2 <0.

Thus z=6 is worst. Put

    A(x)=3x^2+19x+22,
    B(x)=2x^3-87x^2-81x-70,
    C(x)=-2x^4+48x^3+110x^2+324x+96.

Direct summation gives

    4m(x,y,6)=A(x)y^2+B(x)y+C(x).

Its leading coefficient is positive, and the negative of its discriminant is

    P(x)=-28x^6+772x^5-2453x^4+2658x^3
                              +16715x^2+24468x+3548.

For the integer x=0, P=3548>0. For1<=x<=6 put t=x-1 in[0,5]. Then

    P=t^5(604-28t)+987t^4+6t^3+17271t^2
                              +59752t+45680>0.

Thus the quadratic is strictly positive for every real y. This proves m>0 and hence the full fixed-physical-event bank(T1) for every admissible exterior word. Summing actual completion counts proves the original-P statement. No finite deadline certificate remains in this gate proof. The positive diagnostic minimum11 is not needed or asserted as a separately proved optimal margin.

## T6. Application and nonclaims

The argument applies to the actual original subideal P minus U_P(v) whenever it has this seven-label shape and the original exterior is above v. In a retained state, already marked strict successors of v may be treated as part of that analytical exterior; no remembered mark is removed from the phase state. The charged endpoints have at most three full predecessors.

It replaces source banks for every qualifying reference on this interface, not just the original19/5/2/1 coefficients. A metadata coverage census and its independent audit are separate. The other remaining D9 states, phase coverage and D10 are not concluded.

The prior supported-tail two-event bank cannot cover this common-three-tail interface uniformly: its real degree-nine two-law obstruction remains valid. The new theorem adds two fixed physical leaf comparisons. A separate three-event-menu obstruction does not invalidate this four-event bank.

## T7. A sharp actual D10 stopping line for THIS bank

Take the same Q and an actual seven-chain exterior. Put x<z_j exactly when h_x<j, with

    h=(0,0,0,0,0,2,7) on(a,b,u,v,t1,t2,t3),

and take transitive closure. This fourteen-point original poset has Delta10, two minima a,b, singleton private branch{b}, and all exterior above v. Exact original counts are

    N530, K_A190, K_D160, K_(t2<t1)149, K_(t3<t2)140,
    6K_A+K_D+K_(t2<t1)+K_(t3<t2)-3N=-1.

THREE_TAIL_D10_STOPLINE.py independently counts the full poset by ideal subsets. This refutes changing the same leaf cutoff6 to7 in the SAME bank. The pair u,b is already balanced (190/530), so it is not an NB or ordinary-balance counterexample and does not refute another degree-ten bank with a larger event library.

## T8. A real degree-nine neighboring-interface control

The same four physical events do not automatically pay on the neighboring eight-label exhausted-v ideal. Take Q7 plus an actual six-chain, with

    h=(0,0,0,1,0,2,6).

The full13-point poset has Delta9. Its exact original ideal P\U_P(v) contains the first chain label z1 as well as Q7 and has predecessor array

    (0,0,1,1,7,7,7,23).

THREE_TAIL_D9_EXPOSURE_CONTROL.py/.json reconstructs and counts this original poset:

    N630, K_A222, K_D144, K_(t2<t1)165, K_(t3<t2)185,
    6K_A+K_D+K_(t2<t1)+K_(t3<t2)-3N=-64.

This is NOT loss of a valid payment under a theorem-preserving enlargement: the seven-label marking in this P did not satisfy the exhausted-v hypothesis, since z1 was still incomparable with v. Once z1 is legally exposed the actual exhausted-v interface has eight labels, outside T1's exact seven-label contract. The control refutes silently reusing the same bank on that adjacent interface, not legal remembered exposure itself or any statement actually proved above. Its u,b pair is already balanced (222/630), so again there is no NB or ordinary-balance counterexample. The source tree's corresponding terminal row uses an additional event involving label7; it is not contradicted.
