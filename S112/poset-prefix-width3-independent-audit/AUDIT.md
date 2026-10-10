# Independent audit: three guarded width-three prefix exclusions

Date: 2026-10-10. Verdict: **PASS for the three stated finite guarded-prefix exclusion theorems and their exported exact certificates.** The original assertion-based author verifier has a separately documented optimized-Python hardening issue. No remote action or publication was performed.

The auditor imported no author implementation into the independent mathematical checks. The checks reconstruct each poset from its Hasse edges, exhaustively enumerate permutations of every core and cut ideal, independently subdivide the two-row probability simplex using exact fractions, check primal/dual identities, and enumerate the actual extensions of all completion witnesses. All checks remain active under `python -O`.

## 1. Precise exclusion theorem and transfer to completions

Let P be a **finite** poset. Suppose C is an **initial order ideal**, its induced order is isomorphic to one of the three specified cores, n=|C|, and r=n−1. Require that no vertex outside C can appear in the first r positions of any linear extension of P. An easily checked sufficient condition is

> Every z in P\\C has at least r strict predecessors in the full poset P.

Indeed, the earliest possible position of z is |pred_P(z)|+1: first order its predecessor ideal, then z, and extend the resulting ideal. Thus this predecessor condition is also equivalent to the stated exclusion of outside points by the cut. It is a condition on the completion, not something inferred from the core alone.

Every actual rank-r ideal must then be contained in C. The rank-(n−1) ideals of C are exactly J_m=C\\{m}, where m runs through the maximal vertices of C. Conversely every J_m is an ideal of P, because C is initial, so each really occurs as a prefix set. This gives **exactly** the listed three cut states, without suppressing a possible state or inventing a continuation-ratio bound.

Set F_m=e(P[J_m])=e(C[J_m]) and B_m=e(P\\J_m). Every B_m is a positive integer. Any linear extension of J_m concatenated with any linear extension of P\\J_m is valid, because an ideal has no incoming order relation from its complement. Therefore the number of extensions with that prefix set is F_m B_m.

For each selected incomparable ordered pair (x_i,y_i), both endpoints belong to **every** J_m. Let A_im count extensions of J_m with x_i before y_i. Its full-poset probability is exactly

p_i = (sum_m A_im B_m)/(sum_m F_m B_m) = sum_m q_im mu_m,

where q_im=A_im/F_m and mu_m=F_m B_m/(sum_j F_j B_j). The vector mu has strictly positive coordinates and sum one. The supplied certificates cover the **entire closed simplex**, a stronger sufficient relaxation. They therefore prove that at least one selected genuine pair is balanced for every completion satisfying the support premise. The successful pair may depend on that completion.

The same conclusion applies directly to **any finite completion with the same verified actual cut states and induced cut orders**, irrespective of how those states were verified. Neither a bound on tail size nor a ratio bound nor a degree bound is needed. Arbitrarily large finite tails are permitted. No infinite-poset assertion is made.

### What is forbidden in a counterexample

A finite counterexample to the 1/3–2/3 assertion cannot contain a relabeled copy C of any listed core **as an initial order ideal with the verified no-outside-point-by-rank-(n−1) guard**, or otherwise realize its exact verified cut-state configuration. This is a **forbidden guarded prefix configuration** statement.

It is **not** a forbidden arbitrary induced-subposet theorem, and it is not a proof for every width-three poset. The completion itself need not have width three for the transfer theorem; the three cores do.

## 2. Independently reconstructed cores and count tables

All extrema, Hasse reductions, widths, connectedness, and tables below were checked directly rather than trusted from the predecessor bitmasks. Each core has connected comparability graph. The selected pairs are genuine incomparable pairs and fully observed in every cut state.

### Core 1: six-boundary

Hasse edges: a<c, a<d, b<d, c<e, b<f, c<f.

- Minimal vertices: a,b. Maximal vertices: d,e,f.
- Width exactly 3; chains (a,c,e), (b,d), (f) provide an upper bound, and {d,e,f} provides the lower bound.
- Total core extensions: 24.
- At r=5, columns omit d,e,f; common intersection is {a,b,c}.
- F=(7,8,9).
- A_(a,b)=(5,5,6).
- A_(b,c)=(4,6,6).
- These are all fully observed incomparable pairs, up to reversal.

The identity 2A_(a,b)+A_(b,c)=2F holds exactly. Both probabilities are at least 1/2; in fact their common statewise lower bound is 4/7. At least one is at most 2/3. The two-dimensional displayed probability vectors lie on a line, with affine determinant zero. The closed-simplex maximum of min(p_(a,b),p_(b,c)) is exactly 2/3. The zero HH optimum is valid coverage, so endpoint inclusion is essential.

### Core 2: six-triangle

Hasse edges: a<c, b<d, c<e, b<f, c<f.

- Minimal vertices: a,b. Maximal vertices: d,e,f.
- Width exactly 3; the same chain partition works.
- Total core extensions: 26.
- At r=5, columns omit d,e,f; common intersection is {a,b,c}.
- F=(7,9,10).
- A_(a,b)=(5,5,6).
- A_(b,c)=(4,7,7).
- These are all fully observed incomparable pairs, up to reversal.

Here 2F−2A_(a,b)−A_(b,c)=(0,1,1). The q columns are genuinely noncollinear: the determinant of the two column-difference vectors is 1/315. The common lower bound is 5/9. The exact relaxed-simplex envelope is

max_mu min(p_(a,b),p_(b,c)) = 15/23,

with mu=(14/23,9/23,0). The HH dual row weights are (13/23,10/23), and its slack is −1/69. Thus one selected pair always belongs to [5/9,15/23].

### Core 3: seven-three-minima

Hasse edges: a<d, b<e, a<f, c<f, b<g, d<g.

- Minimal vertices: a,b,c. Maximal vertices: e,f,g.
- Width exactly 3; chains (a,d,g), (b,e), (c,f) give the upper bound and either extreme antichain gives the lower bound.
- Total core extensions: 169.
- At r=6, columns omit e,f,g; common intersection is {a,b,c,d}.
- F=(40,54,75).
- A1 for a<b: (28,30,42).
- A2 for a<c: (26,40,45).
- A3 for b<c: (18,38,40).
- A4 for b<d: (26,42,61).
- A5 for c<d: (28,28,60).
- These five are all fully observed incomparable pairs, up to reversal.

Pairs A1 and A3 suffice. Their common lower bound is 9/20. Their simple average is at most 17/27 coordinatewise. The sharper exact envelope is

max_mu min(p1,p3) = 131/215,

with mu=(16/43,27/43,0). Its HH dual row weights are (137/215,78/215), slack −37/645, and state residual eta=(0,0,317/5375). The selected probability triangle is also nondegenerate, with determinant 317/13500.

The displayed sharp envelopes are **optima of the closed relaxed simplex**. Their maximizing points have a zero coordinate, whereas a finite lawful completion has all coordinates positive. No claim is made that those maximizing points are achieved by actual completions, or that all positive simplex points are realizable.

## 3. Exact dual identities and every orientation mask

For orientation L set h_i=1/3−q_i; for H set h_i=q_i−2/3. A bad cell requires h_i·mu>0 for every selected i. Its common-slack LP maximizes epsilon subject to mu>=0, sum(mu)=1 and epsilon<=h_i·mu. Epsilon is unrestricted below.

The checked dual convention is

lambda_i>=0, sum(lambda)=1, eta_j>=0,
sum_i lambda_i h_ij + eta_j = nu for every state j.

Then epsilon <= sum_i lambda_i(h_i·mu) = nu−eta·mu <= nu. Feasible primal mu with epsilon=nu proves exact optimality. The independent checker verifies every dimension, sign, normalization, primal inequality, dual equality, and matching optimum with rational arithmetic. It separately recomputes the optimum by intersecting the line h_1=h_2 with all simplex edges and checking those intersection points and all simplex vertices.

Exact selected-menu cell optima, in order LL,LH,HL,HH:

- Six-boundary: −1/3, −7/24, −5/21, 0.
- Six-triangle: −16/51, −2/9, −5/21, −1/69.
- Seven-three-minima: −40/177, −2/9, −7/60, −37/645.

All are nonpositive, which excludes all strict bad cells. Reversing a pair changes p to 1−p and leaves balancedness unchanged.

The seven-point menu has five fully observed pairs. For **each of all 32 full-menu masks**, the audit projects to its A1/A3 orientations and extends that selected certificate's lambda vector by zeros. Every resulting full-menu dual identity is independently checked and has nu<=0. These are upper-bound certificates, not claims that the selected primal also attains each five-row optimum. The 32 explicit extended duals are saved in `independent_checks.json`.

Equivalently, multiplying the statewise identities by F_j gives certificates on the full nonnegative B cone under F·B=1. The mu change of variables loses no positive B vector and adds only boundary points. There is no hidden restriction to finite continuation ratios.

## 4. Actual guarded completions disqualify every fixed candidate

For a maximal core vertex m, append a chain x1<...<xk whose bottom is above every core vertex except m, leaving m incomparable with the chain. Every added vertex has at least n−1 core predecessors. The core remains initial and the cut-state support is unchanged. If state m is omitted, its remaining vertex can occupy any of k+1 places among that chain; at every other state the missing core vertex precedes the entire chain. Thus B_m=k+1 and the other B coordinates equal one.

The audit verifies this formula by independently enumerating the induced suffix extensions, and also enumerates **all actual full-poset extensions** to check the cut support, total count F·B, every pair count A_i·B, and each claimed failure. These witnesses remain width three: an antichain containing a tail point can contain at most the omitted core vertex in addition, and a core antichain has size at most three.

Core 1:

- Pair a<b: k=1 above C\\{d}; B=(2,1,1), 31 extensions, probability 21/31>2/3.
- Pair b<c: k=1 above C\\{e}; B=(1,2,1), 32 extensions, probability 11/16>2/3.

Core 2:

- Pair a<b: k=5 above C\\{d}; B=(6,1,1), 61 extensions, probability 41/61>2/3.
- Pair b<c: k=1 above C\\{e}; B=(1,2,1), 35 extensions, probability 5/7>2/3.

Core 3, including **all five** fully observed candidates:

- Pair a<b: k=10 above C\\{e}; B=(11,1,1), 569 extensions, probability 380/569>2/3.
- Pair a<c: k=1 above C\\{f}; B=(1,2,1), 223 extensions, probability 151/223>2/3.
- Pair b<c: k=9 above C\\{f}; B=(1,10,1), 655 extensions, probability 438/655>2/3.
- Pair b<d: the same k=1 f-omitting completion gives 171/223>2/3.
- Pair c<d: k=1 above C\\{e}; B=(2,1,1), 209 extensions, probability 144/209>2/3.

Consequently the adaptive-pair assertion really is stronger than selecting one fixed fully observed pair for all lawful completions. The evidence is not confined to unattainable simplex vertices.

## 5. Negative controls and implementation checks

### The guard cannot be dropped

Append one independent vertex z to Core 1. C is still an initial ideal with its original induced order, but the rank-five support now additionally contains {a,b,c,d,z}, {a,b,c,e,z}, and {a,b,c,f,z}. Thus the three-column transfer table is no longer the actual support. With two independent outside vertices z,w, rank-five states such as {a,b,d,z,w} even fail to observe the pair b,c. These controls establish failure of the unguarded reduction, not a counterexample to the balanced-pair conjecture.

### Covering simplex vertices is insufficient, even for a genuine core table

The recorded six-point negative core has predecessor masks (0,0,1,1,2,5). Independent permutations confirm F=(10,15,20), A1=(6,12,12), A2=(7,7,16). Every simplex vertex is covered, but its exact HH optimum is 1/120. The strictly positive abstract continuation vector B=(1,4,5) gives probabilities 57/85 and 23/34, both greater than 2/3. This verifies a genuine-poset-table vertex-only trap. It does **not** assert that this particular vector is realized by a completion.

### Search implementation

Code review confirms that the recursive generator appends every predecessor ideal exactly once, hence enumerates naturally labeled posets, not unlabeled isomorphism types. An independent antichain-downset generator confirms counts 357, 4,824, 96,428 for n=5,6,7. The author's width test, maximal-element selection, induced cut count recursion, added-pair precedence recursion, and Hasse reduction are consistent with this natural labeling. The one-direction incomparability check is valid only because labels increase along all relations. Its degree-partitioned canonical code is compatible with poset isomorphism; the numerical LP is only a discovery filter.

A copied author rerun exactly reproduces `candidates.json` and `exact_templates.json`. All **28 recorded exploratory candidates**, not only the promoted three, have independently permutation-verified profiles. For each of the 28, exact rational two-row geometry independently reproduces every recorded minimum two-pair cover and verifies that no one-pair cover exists. This supplements the three promoted results; it is not a claimed exhaustive classification of all successful cores or all posets.

### Verifier hardening

In the frozen original `certify.py`, assertions are the only certificate checks. A probe changing a certificate's optimum to 999 is rejected under normal Python and accepted under `python -O`. Its helper also omits explicit schema and full-mask validation, although the exporter itself generates the expected four masks. This is an implementation caveat for using that prototype as a general verifier, not a defect in the three validated outputs.

The independent verifier uses explicit exceptions and checks complete, unique masks and aggregate conclusions. It rejects 20 malformed bundles, including absent/duplicate masks, invalid orientations, negative or wrong multipliers, wrong dimensions, floats, false optima, wrong totals/rows/states, false predecessor closure, wrong selected endpoints, and a false aggregate verdict. All rejection tests pass under both normal and optimized Python.

## 6. Reproduction, provenance, and freeze

From this directory run:

- `python independent_checks.py`
- `python -O independent_checks.py`
- `python search_checks.py`
- `sha256sum -c SHA256SUMS`

The audit's `author_snapshot/` binds the precise source, proof, discovery outputs, and exported certificates reviewed. `author_rerun/` contains copied reruns, never a mutation of the source project. `audit_manifest.json` records all frozen file hashes; `SHA256SUMS` binds those files and the manifest. The report and checks apply to those snapshots, so later author changes cannot silently inherit this verdict.
