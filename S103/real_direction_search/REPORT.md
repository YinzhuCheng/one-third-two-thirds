# Snapshot status update

Subsequent complete scalar proofs and independent audits close the shared-downset/neutral-chain target; see [S103 report](../REPORT.md). The general-width normalized candidate remains open. Historical OPEN wording below records the search stage and does not supersede the later proofs. The finite witnesses still refute only the OLD energy sufficient closure.

# S103: genuine-direction search and failure of the old sufficient lower bound

Status: the target H² ≥ Ru Ry remains OPEN. No target counterexample was found. The S102 energy-minus-variance lower bound can be strictly negative for the ACTUAL q_j sequence of a width-three poset with a common strict downset. This is a counterexample to that sufficient closure, not to the target.

## Most useful exact witness

Take 13 labels d1<d2<d3, u,s,y,t, n1<…<n6. Add d3<u<s, d3<y<t, and n2<t; there are no other generating relations. Three displayed chains certify width ≤3. Both entries have strict downset D={d1,d2,d3}.

- a=(1,4,10,20,35,56,84), c=(1,3,6,10,15,21,28), f=(1,5,15,35,70,126,210).
- E_j=(1125,720,420,210,90,30,6).
- C_j=((225,180),(160,140),(105,105),(60,60),(30,30),(12,12),(3,3)).
- q_j=(119/225,37/72,1/2,1/2,1/2,1/2,1/2).
- E=10053, Ru=1708, H=3381, Ry=1583, p=5089/10053.
- H²−RuRy=8727397; target normalized gap =8727397/101062809 >0.
- Unnormalized old energy =2729/2880; variance =194423/201060.
- (energy−variance)/E =−4165/2156006592 <0.
- The proposed scalar-block Schur curvature term repairs this particular lower bound: its strengthened normalized value is 1565365/3436135506 >0.

The chain-ideal computation was independently checked with a bitmask-ideal recurrence for E, Ru, Ry and every q_j. A separate depth-first enumeration visited all 10053 COMPLETE linear extensions and directly counted the release events. See minimal_single_gate_negative_energy.json, refine.py, independent_checks.json and complete_extension_enumeration.json.

All 1792 induced subsets of this example retaining u,y and nonempty common D were also checked. Exactly two have negative old energy: this 13-point example and the 12-point example deleting s. Thus that 12-point example is induced-minimal for the negative-old-energy property among these subsets, not globally minimum among all posets. It has old lower bound −69205/22744599552. Its Ru=0 makes the determinant target trivial, so the 13-point two-arm witness is more informative. See induced_audit.json, induced_minimal_twelve.json and twelve_enumeration.json.

## A singleton common predecessor also fails the old closure

Take d<u<s, d<y<t, n1<…<n16, and n3<t. Here D={d}, all 16 neutral elements are incomparable with d, and the complete-extension count is 120288.

Ru=20328, H=40446, Ry=19068. The target gap is 707633/8202496 >0, but the old energy lower bound is −362411441/1317011877778176. All 120288 extensions were individually enumerated. The neutral prefix length is 16, NOT 3: 3 is only the successor gate location. This does not contradict a result restricted to singleton D with at most three neutral elements incomparable with d.

Within the explicitly searched one-sided single-gate family, the singleton sweep checked 2052 models in increasing total size, with arm lengths 1…6 and neutral length 2…22, and first found this n=21 witness. This is not a global minimality claim.

## Genuine backend constraints and a failed monotonicity shortcut

The sequence q_j need not be monotone. Nine-point example:
 d<u<s, d<y<t, n1<n2<n3<n4, n1<s, n4<t.
Its q_j=(79/133,25/42,26/45,11/20,1/2), with q_1>q_0 and q_2<q_1. Direct enumeration of all 288 extensions gives Ru=65,H=104,Ry=15. See first_nonmonotone.json.

Every saved certificate supplies the actual C_j,E_j,V_j, not a fitted scalar g. Exact identities checked in the code include E=2H+Ru+Ry=Σ c_jE_j. Actual q_j is computed as Σ_{k≥j}(C_k)_u/E_j and independently verified on selected examples. The strengthened search checks Δ_j=E_{j+1}²−E_jE_{j+2}≥0 and, at Δ_j=0, E_j(q_j−q_{j+1})−E_{j+1}(q_{j+1}−q_{j+2})=0. These are finite diagnostics of genuine backend compatibility, not new universal proofs.

## Explicit budgets, model classes and outcomes

1. Fixed-seed main search: seed 10320261010, 8222 parameter instances total, not deduplicated isomorphism classes.
   - 7272 exhaustive parameter-grid instances: d∈{1,2,4}, arm-length pair in {(1,1),(2,2),(4,4),(8,8),(3,8),(8,3)}, neutral length r∈{2,4,8,16}, each first arm successor gated by n_gu/n_gy with gu,gy∈{0,…,r}; 0 means no gate.
   - 800 random selective-backend instances: d∈{1,2,3,5}, each arm length 1…12, r=2…17. Random acyclic cross-arm dependencies, neutral-to-arm gates, opposite-entry requirements and D-to-neutral relations.
   - 150 larger instances of the same class: each arm length 1…26, r=2…31.
   - No target violation. 557 instances have negative old energy and 4316 have nonmonotone q_j. Neither statistic is a population-frequency claim.
2. Additional fixed-seed search: seed 103731, 2000 instances, observed n=11…79. The third chain now continues after its neutral prefix into a true successor backend; this allows more than two successor chains. d∈{1,2,3,5,8}, first two arm lengths 1…19, neutral prefix 2…24, third-chain successor tail 1…11, with acyclic cross-chain dependencies and D-to-neutral relations.
   - No target violation. No negative strengthened Schur lower bound; the minimum observed strengthened value was zero (including zero-direction cases).
3. Targeted reductions and independent verifications above are separate from these counts. All phases have terminated. No unbounded monitor or search is running.

The three-chain recurrence has at most (|A|+1)(|B|+1)(|C|+1) states and uses exact integers. States are chain-prefix triples; a next element is legal iff its predecessor requirements in all three chains are already consumed. It does not allocate a 2^n table. The independent verifier does use bitmask labels but memoizes only accessible ideals. The large 83-point selected certificate used 9052 ideal states.

## Closest observed target structures

The lowest normalized target gap in the main search was about 0.002544697 (51 points; best_gap.json). Its exact gap is 615777765863813973096821/241984634714416066547243532. This metric favors highly asymmetric entry probabilities.

The smallest H²/(RuRy) was about 1.14683 (83 points; best_ratio.json), with two long arms (lengths 26 and 24), a 5-point common chain, 26 neutrals and sparse selective gates. E=240590650517401571533201791829019318. Exact independent ideal/event recurrence reproduces its counts. This is the less asymmetry-sensitive closeness statistic, but long independent arms provide a still closer and elementary baseline, as described next.

## Essential independent-arm baseline

For D a chain, an independent neutral chain, and two independent equal arms u<s1<…<sm and y<t1<…<tm above D, symmetry and elementary two-chain shuffle counts give p=1/2, U=m/[2(2m+1)], target gap=1/[4(2m+1)] and H²/(RuRy)=((m+1)/m)². These tend to zero and one, respectively, without any suspicious backend interaction. Appending the independent neutral chain multiplies all four event counts by the same interleaving factor.

The recurrence checked m=1,8,40 exactly. At m=40 (91 total points with d=1,r=8), the gap is 1/324 and determinant ratio is 1681/1600, closer to 1 than the main random search. See independent_arms_baseline.json. Thus small normalized gaps or ratios near 1 alone should not be sold as evidence of imminent failure; a useful next search objective should compare selective-gate instances to the matching independent-arm baseline.

## Reproduction

Run python search.py; python refine.py; python singleton_and_enumerate.py; python induced_audit.py; python export_twelve.py; python strong_search.py from this directory (or by absolute path). Python standard library only. All rational outputs are exact Fraction strings. Scripts write only within their own directory. Published S102 files were read only and not changed.

No claim of theorem proof, target disproof, global minimum, exhaustive width-three enumeration, or uniform random-poset sampling is made.
