# Independent review: supported middle leaf survives one extra v-incomparable

2026-11-10. Internal independent mathematical and metadata review, not external peer review or formal verification. **PASS** under the explicit original-ideal contract below. No new historical originality claim.

## Precise contract and conclusion: one added label

The original seven-label Q7 is an induced ideal with a<u,v and a,b,u<t1,t2,t3, the leaves incomparable, and b incomparable with a,u,v. There is exactly one additional original exterior label z incomparable with v. Its full strict predecessor set inside the resulting eight-label ideal is {a,b,u} together with a nonempty subset of the three leaves, and this subset contains the physical middle leaf t2. Thus z is above t2, possibly above another leaf, but cannot be a predecessor of any original leaf. All remaining original exterior labels are above v. Each original leaf has incomparable degree<=9.

For the same fixed physical leaf naming, the original law satisfies

    6 Pr(u<b)+Pr(v<u)+Pr(t2<t1)+Pr(t3<t2)>3.

This extends the previously proved Q7 four-event bank to this particular Q8 structural interface. It does not claim arbitrary exposure preserves payment. The old Q7 theorem was not applicable before z was exposed, since z was still an exterior v-incomparable.

## Original-word projection and event bookkeeping

Project the actual full extensions onto the original ideal Q7 and condition on one literal word of its complement, which includes the fixed physical z. All other complement labels are above v, so the deadline h_v is either0 or1. If h_v=1, z is the first exterior label. As z is above a,b,u,t2, it forces h_a=h_b=h_u=h_t2=0. The other two leaf deadlines are bounded by6 from their original local degree9 and their three original internal incomparable partners. Additional relations from z to another leaf only force another zero and are included in the cases below.

For h_v=0, the previous THREE_TAIL_FOUR_EVENT_ANALYTIC theorem applies to exactly this conditional insertion law. There is NO extra event E and no added coefficient cost. For h_v=1, separate the words with v in gap0 from those with v in gap1. Both parts count the same physical four events; neither part receives an NB assumption. Summing the actual counts therefore preserves the required fixed-bank quantifiers.

## Independently verified h_v=1 calculation

Temporarily sort the two nonmiddle leaf deadlines as0<=r<=s<=6. If the physical leaf with cap r is t1, the fixed leaf reference is near,head,far, corresponding to sorted-cap reference213. If cap r belongs to t3 it is312. Writing q_near and q_end for the reverse probabilities head versus near and head versus far, q_end<=q_near by the sequential-insertion pair formula. Thus the213 leaf reversal sum1-q_near+q_end is a uniform lower bound for BOTH physical orientations. This is a bound on the fixed bank, not a new event choice.

### v in gap0

The tail slot flags are(1,r+2,s+3), with

    F=(r+2)(s+3), W=F+r-s.

The plus model including the cap-zero v has flags(2,r+3,s+4), with

    Fplus=2(r+3)(s+4), Wplus=Fplus+3(r-s).

The independently checked zero-root-gap decomposition gives

    M0=F-3Fplus+5W+3Wplus=6F+14(r-s).

### v in gap1

With b,u already in gap0, the three a,b,u root orders give coefficients(N,K_A,K_B)=(3,1,0). Insert v in gap1 by treating it as one added fixed chain position immediately after the first exterior label. A leaf whose deadline is at least1 receives one extra allowable slot; cap-zero leaves do not. This gives three cases.

- If r>=1, the flags are(1,r+3,s+4), and Wnew-Fnew=r-s. The added margin is3(Wnew-Fnew), so total M is at least(6r-5)s+35r+36>0.
- If r=0<s, the flags are(1,2,s+4), and Wnew-Fnew=-s-1. The total is at least33-5s>=3.
- If r=s=0, the flags are(1,2,3), Wnew=Fnew, the added margin is zero, and M0=36.

Every formula follows directly from q_near=(L1+1)/(2L2), q_end=(L1+1)(L2+1)/(2L2 L3). Thus no cap-profile certificate is required. MIDDLE_HEAD_INDEPENDENT_COUNTS.py independently checked the exact counts at the28 sorted integer(r,s) pairs, solely as a diagnostic corroboration; these checks are not a proof dependency. The expressions themselves establish the entire parameter domain.

The lower count margin is strictly positive in both h_v cases. Summing over the actual exterior words with their actual completion multiplicities gives the original-P strict bank. The empty remainder after z and equal/zero deadlines are included.

## Independently verified arbitrary single-supported middle branch

There is a second, complementary structural case. Let K_v=P minus U_P(v)=Q7 union E, where E is any nonempty poset, every e in E is above the physical middle leaf t2, and every e in E is incomparable with v,t1,t3. Q7 remains an original ideal and all labels outside K_v are above v. The same original leaf degree<=9 bounds are retained. No separate size bound on E or degree bound on v is needed. Under the current leaf-degree hypotheses |E|<=6 is already implicit because both nonmiddle leaves are incomparable with all of E; the positive-V algebra itself needs no numerical upper bound on E.

In a fixed original exterior word of Q7 put V=h_v. If V=0, use the old per-profile cap-count theorem, NOT a global assertion that Q7 has exhausted v. If V>0, its first V exterior letters all belong to E. They are all above t2 and incomparable with t1,t3. Therefore h_b=h_u=h_t2=0, and the two other leaf deadlines satisfy V<=r<=s<=6. This lower bound r>=V is the decisive new structural information.

Each allowed positive placement gap j=1,...,V of v lies no later than either nonmiddle leaf's deadline. Inserting the fixed v into the exterior chain at gap j therefore adds exactly one allowable slot to EACH of these two leaves and none to the cap-zero middle leaf. The slot flags are(1,r+3,s+4) for every such j, independently of where j lies. The fixed physical leaf path has Wnew-Fnew>=r-s as above. Each j contributes at least3(r-s) to the same bank count margin. Adding all positive gaps to the zero-gap part yields

    M >= 6(r+2)(s+3)+(14+3V)(r-s)
       = (6r-2-3V)s+(32+3V)r+36 > 0,

because r>=V>=1 implies6r-2-3V>=3V-2>=1. This is a single algebraic argument for every allowed V and E; it does not choose a different bank per gap or condition on NB.

The arbitrary-E case requires every E label to be incomparable with BOTH nonmiddle leaves. It must not be conflated with the unique-z case, which allows z above another leaf and uses the additional zero-cap cases. Their union, together with E empty as the old Q7 base theorem, is the verified unified middle-support gate. Arbitrary many multiply-supported E labels have not been proved here.

## Independent source-packet census and deduplication

MIDDLE_HEAD_INDEPENDENT_MAPPING.py independently searched the unique-z case; MIDDLE_BRANCH_INDEPENDENT_MAPPING.py independently searched the full union of the unique-z case, arbitrary single-supported branch, and the old empty-E Q7 base case. Both scripts use the original packet by genuinely exhausted or degree-saturated boundary labels, formed the full non-upper-set ideal, checked the complete Q7-plus-z predecessor structure, and required that the T-middle physical leaf belong to z's supporting leaf set. It verified all charged events reverse the same fixed reference and retained the original row types.

The unified gate covers10 source bank occurrences: six are the already-paid empty-E Q7 rows, and four terminal rows are new relative to the existing396-row union:

- pred(0,0,1,1,7,7,7,23), T=abuv5467 and abuv6457;
- pred(0,0,1,1,7,7,7,55), T=abuv4567 and abuv5467.

The arbitrary nonempty E branch contributes no further existing bank occurrence beyond those four in this packet. The pred119 support-all-three shape contributes no terminal bank occurrence in the supplied source packet. It may satisfy the theorem abstractly, but is not added to the source-row count. All charged endpoints have full downset size<=3.

The deduplicated analytic payment union therefore becomes400/3469, leaving3069. This does not prove the rest of the source states, structural phase coverage, or all D9, and it does not erase the earlier D9 adjacent-Q8 counterexample: that control puts the singly supported head at the LEFT end of the reference, not in the middle.

## Independently checked stopping line for multiple supported heads

The final author draft MIDDLE_HEAD_MEMORY_GATE.md MH1–MH7 was read and agrees with the audited contracts and formulas above. Its multiple-E branch must retain the incomparability with BOTH nonmiddle leaves. This restriction is substantive, not merely needed by the displayed proof.

MIDDLE_HEAD_TWO_SUPPORT_INDEPENDENT.py constructs the original13-point poset from Q7 and a six-chain with h=(0,0,0,2,0,0,6). Independent forward ideal-subset DP and direct enumeration of all390 complete words agree:

    N390, K_A136, K_B72, K_C21=195, K_C32=69,
    bank margin6K_A+K_B+K_C21+K_C32-3N=-18,
    Delta9.

The true K_v is Q9 with predecessor masks(0,0,1,1,7,7,7,55,183). Both extra labels are above t1 AND the physical middle t2, form a chain, and are incomparable with v,t3. Thus the unique-extra condition fails, and the multiple-extra/only-middle condition also fails. The projection has V=2 but one nonmiddle deadline is0, precisely violating the audited lower bound r>=V.

This is an actual degree-nine countercontrol to applying the SAME bank after dropping the only-middle-support requirement. It is not a counterexample to the proved gates, not a preservation failure starting from an already applicable gate, and not NB. A is already balanced,136/390=68/195; t1,t2 are fair,195/390=1/2. A different event library may pay this original P.
