# Fixed defect-three gate: one extra event is insufficient; equal adjacent four-event bank works

CURRENT UPDATE: the positive four-event bank below now has an independently reviewed analytic proof in THREE_TAIL_FOUR_EVENT_ANALYTIC.md. The finite replay is corroboration, not a remaining proof dependency. The negative eight-event-menu obstruction below remains an exact real-law result.

2026-11-10. Local exact computation and explicit rational certificates; not an analytic replacement of the positive four-event bank. Source Q/state: Fathi v22 §24.4.1 and the retained source packet, https://zenodo.org/records/23933091.

## Fixed contract and result

Q has predecessor masks(0,0,1,1,7,7,7), with labels a,b,u,v,t1,t2,t3 and reference T=(0,1,2,3,4,5,6). Let A={u before b}, B={v before u}. The D9 terminal-v domain is h_a=h_v=0, h_b<=6, h_u<=7, all three leaf caps<=6, and h_leaf>=max(h_b,h_u). The last condition automatically forces h_u<=6. There are2408 such profiles. Every one is a genuine degree-at-most-nine completion using one fixed six-label exterior chain, with x<z_j iff h_x<j. Exterior labels are all above v, and no profile-realizability claim beyond these explicit completions is needed.

**Negative result.** For every one of the eight other Q reverse events C, no nonnegative fixed bank supported on {A,B,C} can pay the one-third threshold uniformly on this domain. Explicit mixtures of only four actual complete-poset laws prove this. This is an anchored-library result: A and B are retained. It does NOT rule out every possible three-event bank using a different event library.

**Positive finite result.** Writing C21={t2 before t1} and C32={t3 before t2}, the simple equal-adjacent bank

    6 Pr(A)+Pr(B)+Pr(C21)+Pr(C32) >= 3

holds on all2408 profiles. Total weight is9. Its exact minimum raw count slack6K_A+K_B+K_C21+K_C32-3N is11. Thus adding two extra events is sufficient within this anchored library. This remains a finite certificate, not an analytic proof; it is intended as a simpler equal-weight target for a run/interval argument.

## Four actual laws, no fictitious profiles

Use the same13 physical labels, Q plus z1<...<z6. The four profiles, extension totals and maximum degrees are:

- P0: h=(0,0,0,0,0,0,0), N102, Delta5.
- Pinf: h=(0,0,6,0,6,6,6), N6948, Delta9.
- R5: h=(0,0,0,0,0,6,0), N270, Delta9.
- R6: h=(0,0,0,0,0,0,6), N270, Delta9.

All exterior labels are truly above v. The exact (A,B) probabilities of P0,Pinf are(6/17,4/17),(48/193,119/193). For either R_i they are(16/45,4/15). For an ordered leaf reversal involving the delayed leaf i before an undelayed leaf, its probability in R_i is17/90. In both P0,Pinf any leaf reversal has probability1/2.

The full thirteen-point ideal-subset DP in DEFECT3_THIRD_EVENT_EXACT_REPLAY.py checks every Q reverse count in these four laws independently of the discovery algorithm. It also verifies the degree bounds and the h-gap count agreement. No optimization package is required for replay.

## Exhaustive eight-event obstruction

For C in the five-element family

    {b before a}, {v before b}, {t1 before v},
    {t2 before v}, {t3 before v},

mix P0 and Pinf with law weights1207/1593 and386/1593. Then

    Pr(A)=Pr(B)=58/177<1/3.

The corresponding C probabilities are respectively155/531,113/531,49/177,49/177,49/177, all below1/3.

For the three leaf reversals, use:

- C={t2 before t1}: R_i=R5;
- C={t3 before t1} or {t3 before t2}: R_i=R6.

Mix(P0,R_i,Pinf) with law weights

    (11509,24705,9650)/45864.

In all three cases,

    Pr(A)=Pr(B)=Pr(C)=121/364=1/3-1/1092.

The weights are nonnegative and sum to1. Any nonnegative bank supported on these three events would have its mixture expectation strictly below one third of its weight sum. Therefore no bank that pays each of these real generators can exist. This argument proves impossibility without trusting LP optimality or exhaustive profile coverage.

These mixtures are NOT asserted to be the law of one original P. A bank depending on the full original P or additional fixed exterior-incidence information is not ruled out. The obstruction concerns a bank fixed for the same Q,T and specified common profile domain. Each actual component has balanced comparisons; this is not NB or a counterexample to ordinary balance. It does not obstruct four-event payment or the source bank.

## Positive replay and exact stopping point

The independent marked-ideal/gap recursion counts N and each named event after adding its comparison. It regenerates the domain and checks6K_A+K_B+K_C21+K_C32>=3N on all2408 profiles. This is a different counting method from the discovery's102 internal-order enumeration with weakly increasing gap tuples.

The minimum11 occurs at

    h=(0,0,0,0,0,2,6),
    N480, K_A172, K_B144, K_C21=135, K_C32=140.

For comparison, the source bank19A+5B+2C21+C32>=9 also passes this domain, with minimum raw count slack39. No new state coverage or phase switch is introduced. The event weights6,1,1,1 remove the unequal leaf coefficients from the analytic target, but the finite replay does not supply the desired cap-independent proof.

Files: DEFECT3_THIRD_EVENT_DISCOVERY.py/.json records the small diagnostic LP, DEFECT3_THIRD_EVENT_EXACT_REPLAY.py/.json contains the standalone integer/rational proof replay, and DEFECT3_THIRD_EVENT_PROFILES.json records diagnostic counts. The negative proof needs only the four explicit laws and the displayed rational mixtures; the positive result still uses all2408 profiles.
