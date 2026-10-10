# Guarded-prefix balance certificates on the surviving n7/n8 cores

Date: 2026-10-10. This is a new bounded result, separate from the earlier three redundant templates and from the existing frozen research package. Independent audit is requested; this author's report is not itself an independent verification.

## Main result and exact scope

For each of the 18 independently catalogued prime-core classes (one at n=7 and seventeen at n=8), and for each orientation obtained by also taking the dual, the actual-vertex prefix at cut r=n−1 has an exact full-simplex balance-cover certificate. These are 36 presented profiles, not 36 nonisomorphic orders. Thirty-four profiles have a single fixed fully observed balanced pair. The remaining two are isomorphic presentations of one width-three eight-vertex poset and need exactly two pairs in the full-simplex menu.

The useful strict separation is the latter adaptive core. Its certificate excludes every finite lawful guarded completion. An explicit 23-vertex completion has both its comparability and incomparability graphs connected, all proper autonomous modules chains, a rigid prime nine-vertex chain quotient, width three, height nineteen, maximum incomparability degree π=18, cyclic cover graph, no very-good pair on either side, and an acyclic full actual-vertex forced graph. Thus this witness survives the structural funnel tested here and is nevertheless excluded by the prefix certificate. It is not a counterexample: its exact balanced pair is exhibited below.

**Weight restriction:** the eight prefix vertices are actual singleton vertices. Arbitrary chain inflations of those eight vertices are not covered by the fixed F/A table. The explicit family varies only the length of a new tail chain; it is an arbitrary-positive-weight family for that one block of a nine-vertex prime quotient. Nothing here excludes every weight vector on any catalogue core, bounds core size, or proves the 1/3–2/3 conjecture.

## Guarded-prefix theorem used

Let C be an initial ideal of a finite poset P, with |C|=n, and assume no element outside C can appear among the first n−1 positions of a linear extension. Equivalently, each outside element has at least n−1 strict predecessors: every element can be scheduled immediately after its predecessor ideal, so its earliest possible position is one plus its predecessor count.

Every rank-(n−1) ideal is then J_m=C minus {m}, where m ranges over the maxima of C. Conversely all these J_m are ideals of P and occur. Put F_m=e(J_m), B_m=e(P minus J_m), and let A_(x,y),m count extensions of J_m with x before y, for a pair x,y present in every J_m. Exact extension factorization at the cut gives

p(x before y) = sum_m A_(x,y),m B_m / sum_m F_m B_m
               = sum_m mu_m (A_(x,y),m/F_m),
mu_m=F_m B_m / sum_j F_j B_j > 0, sum_m mu_m=1.

A closed-simplex cover by balance slabs is therefore sufficient uniformly over all finite guarded tails, with no assumed realization of every simplex point and no bound on tail size, shape, or continuation ratios. Both endpoints 1/3 and 2/3 count as balanced.

The guard also places every nonmaximal core vertex below every outside vertex. To see this, choose a minimal outside predecessor y below a given outside vertex. All predecessors of y lie in C and there are at least n−1; that predecessor ideal must contain every nonmaximal core vertex. This observation is used only in the redundancy checks, not in computing F/A.

## Adaptive core C

Use labels 0,...,7. Its strict predecessor masks are

(0,0,3,2,15,11,2,107).

Its Hasse edges are

0<2, 0<5; 1<2, 1<3, 1<6; 2<4; 3<4, 3<5; 5<7; 6<7.

The two maxima are 4 and 7. At cut seven the columns omit 4 and 7, respectively. The complete observed menu and exact counts are:

| pair | omit 4 | omit 7 |
|---|---:|---:|
| F | 48 | 73 |
| 0 before 1 | 15 | 25 |
| 0 before 3 | 34 | 55 |
| 0 before 6 | 38 | 62 |
| 2 before 3 | 9 | 22 |
| 2 before 5 | 23 | 56 |
| 2 before 6 | 15 | 40 |
| 3 before 6 | 31 | 51 |
| 5 before 6 | 14 | 24 |

No row is balanced in both columns, so no single fully observed pair covers the entire closed simplex. The two pairs (2,5) and (2,6) suffice; thus the minimum menu size for this relaxation is exactly two. This does not assert that a two-pair menu is necessary on every restricted family of realizable tails.

For a short direct proof, let t=mu_omit4. The two probabilities are

p1=(23/48)t+(56/73)(1−t),
p2=(15/48)t+(40/73)(1−t).

Always p1>1/3 and p2<2/3. The only potentially bad combined orientation p1>2/3, p2<1/3 would require both t<352/1009 and t>752/825, which is impossible.

In the catalogue audit order this is n8 class index 15, primal. The other adaptive profile is class index 13, dual. The isomorphism from the latter labels to the former is

0→4, 1→2, 2→7, 3→5, 4→0, 5→3, 6→6, 7→1.

## Complete exact bad-cell certificates

For each selected pair i, set h_i^L=1/3−q_i and h_i^H=q_i−2/3. A strict bad cell needs all h_i·mu>0. Maximize their common slack epsilon. The displayed dual has lambda>=0, sum lambda=1, eta>=0 and

sum_i lambda_i h_i + eta = nu (1,1).

The matching primal mu attains epsilon=nu. All four exact optima are negative:

| cell | optimum nu | primal mu | lambda | eta |
|---|---|---|---|---|
| LL | −7/48 | (1,0) | (1,0) | (0,1009/3504) |
| LH | −1433/5502 | (552/917,365/917) | (825/1834,1009/1834) | (0,0) |
| HL | −401/5502 | (552/917,365/917) | (825/1834,1009/1834) | (0,0) |
| HH | −26/219 | (0,1) | (0,1) | (275/1168,0) |

Every profile, every F/A row, and every selected-cell certificate is in `initial_profiles.json`. The repaired exact certificate verifier checks rational primal feasibility, nonnegative dual multipliers, normalization, the dual identities, equality of primal and dual objectives, and complete unique L/H-mask coverage. Profile counts are separately recounted by all permutations of each rank-cut ideal. No floating point is used.

## Exact nonempty 23-vertex structural-funnel witness

Add z1<...<z15 (labels 8,...,22). Every zj is above all core vertices except 4, and incomparable with 4. The first new vertex has seven core predecessors, so the guard holds. The rank-seven continuation vector is B=(16,1), since after omitting 4 the vertex 4 can be inserted in any of sixteen positions relative to the tail chain; after omitting 7 the tail follows 7 in one order.

Exactly:

- e(P)=48×16+73=841;
- mu=(768/841,73/841);
- p(2 before 5)=(23×16+56)/841=424/841, balanced;
- p(2 before 6)=(15×16+40)/841=280/841<1/3.

`exact_23_vertex_witness.json` contains its full predecessor/upset masks, complete exact probabilities for every incomparable pair, full forced graph and rule edges, degree pairs, all module-closure witnesses, and graph invariants. There are eight balanced unordered pairs. All 23 (strict predecessor count, strict successor count) pairs are distinct, proving rigidity without relying on an automorphism heuristic.

Every proper nontrivial autonomous module is an interval of the new chain, hence is a chain. The quotient obtained by contracting the tail is a prime nine-vertex poset with strict-up masks

(436,508,272,432,0,384,384,256,0).

It is rigid: all nine predecessor/successor count pairs are distinct. Its full actual-vertex forced graph has a topological order

1,0,3,6,2,5,4,7,8.

The bottom/top endpoint graph is also acyclic. Both graphs of the actual 23-vertex witness are connected. Its cover graph is not a forest, its height is nineteen, and its maximum incomparability degree is π=18 (attained at core vertex 4). Thus it also lies beyond the π<=6 exclusion. These checks avoid the ordinal-top example, which has a proper nonchain module and disconnected incomparability graph and therefore is not an entire-funnel separation.

## Optional short all-length family proof

Let P_L be the same completion with an L-vertex chain, L>=1. All P_L have width three, height L+4, and connected comparability/incomparability graphs: the core has both graphs connected; every new vertex is comparable with core 7 and incomparable with core 4. An antichain containing a tail vertex has size at most two, so the width remains three. The old five-cycle 0−2−4−3−5−0 in the cover graph remains.

For module structure, a module M intersects the prime eight-vertex core C in a module of C, so its intersection has size zero, one, or eight. If it contains all of C, every outside tail vertex distinguishes 4 from the rest of C, so a module must then contain the whole tail and be P_L. If M contains one core vertex c and any tail vertex, an outside core vertex distinguishes them: use 4 for c=0,1,2,3; use 5 for c=4 or 6; use 6 for c=5; use 2 for c=7. Such an M is impossible. Thus all proper nontrivial modules lie within the tail and are chains.

The nine-vertex quotient is fixed and rigid, and its full actual forced graph is acyclic. The endpoint-compression lemma for positive chain inflations applies: every actual structural arrow projects to a corresponding quotient rule, or stays within the ordered tail block. Expanding the tail block in the displayed quotient topological order is therefore an acyclic ordering for the full actual forced graph for every L. In particular no P_L has a VGP on either side.

Rigidity can also be proved directly for every L. The core (down-count,up-count) pairs are

(0,L+4), (0,L+6), (2,L+1), (1,L+3), (4,0), (3,L+1), (1,L+1), (5,L),

and tail vertex zj has (j+6,L−j). These are all distinct. These arguments establish the stated graph, module, rigidity, and forced-arrow facts for every length, not merely a finite extrapolation. The maximum incomparability degree is π(P_L)=max(5,L+3); consequently the known π<=6 exclusion still applies at L=1,2,3. The family passes that additional cutoff for L>=4. Finite known size cutoffs must likewise be retained; the 23-vertex witness is the explicit separation used here.

For every L,

e(P_L)=48L+121,
p(2 before 5)=(23L+79)/(48L+121),
p(2 before 6)=(15L+55)/(48L+121).

The first is balanced for every L>=1; the second drops below 1/3 exactly when L>=15. This fixed-pair fact for the simple chain family does not remove the need for the adaptive two-pair certificate over arbitrary guarded tails.

## Redundancy and limits of the wider scan

All 36 presented profiles have exact coverage. Ten have an acyclic full forced graph already on the core; the two adaptive presentations are included among those ten. Twenty-two have a persistent full-forced cycle entirely among nonmaximal prefix vertices, so their guarded completions are already rejected structurally. Four further profiles have a core cycle involving maxima and no acyclic completion among the bounded simple tails tested; no universal impossibility is inferred for those four.

The completeness claim here is only: all 18 independently catalogued classes, their dual presentations, and the exact r=n−1 profile calculation. It is not an exhaustive classification of tails, adaptive certificates, larger cores, or chain weights. The earlier three templates remain structurally redundant for every guarded completion and are not counted as a new exclusion here. No smaller-cut search or new-core search was needed.

The other selected pair (2,5) can fail on a lawful one-vertex tail above C minus {7}, with B=(1,2) and p=135/194>2/3. That completion has a top VGP (7,8), so it is only a lawful fixed-pair failure, not a structural-funnel separation. We do not conceal this distinction or require that both fixed-pair failures survive all structural filters.

## Reproduction and files

Run with Python 3 and the two referenced local source packages present:

```
python research.py
python completions.py
python funnel_check.py
python freeze_witness.py
```

Source inputs are the independently audited core catalogue and the repaired exact prefix verifier. Their relevant files are copied into `reference_snapshot/`, with hashes, for a stable audit record. To reproduce using only the frozen reference inputs, run `python reproduce.py`; it preloads the snapshotted source modules and redirects the one fixed catalogue-input path. All six JSON deliverables then reproduce byte-for-byte against `outputs.sha256`. The same check also passes under `python -O`. No literature-priority or novelty claim is made.
