# Exact guarded-prefix exclusions: width-three cores

## Scope and theorem

Let P be a finite poset and C an initial order ideal of P, with |C|=n. Set r=n−1. Assume no element of P\C can occur within the first r positions of a linear extension. A sufficient, easy-to-check condition is that every outside element has at least r strict predecessors in P.

Then the actual rank-r ideals of P are exactly J_m=C\{m}, one for each maximal element m of C. For every such state, let F_m=e(J_m)>0 and B_m=e(P\J_m)>0, where the latter is the number of continuations. For an incomparable ordered pair x,y contained in every J_m, let A_(x,y),m count linear extensions of J_m with x before y. The exact probability in a uniformly random linear extension of P is

p_(x,y) = (Σ_m A_(x,y),m B_m)/(Σ_m F_m B_m) = Σ_m μ_m q_(x,y),m,

where μ_m=F_m B_m/(Σ_j F_j B_j), μ_m>0, Σμ_m=1, and q=A/F coordinatewise.

The three tables below cover the entire *closed* μ-simplex by genuine pair-balance slabs [1/3,2/3]. Therefore every lawful completion satisfying the guard has a balanced pair, regardless of its size or tail shape. No pairwise continuation-ratio bound, tail-size bound, or incomparability-degree bound is used. 'Arbitrarily large tails' means arbitrarily large finite completions; it is not a claim about infinite posets.

Consequently a finite 1/3–2/3 counterexample cannot realize any of these guarded initial-ideal configurations, up to relabeling. This is not a forbidden-induced-subposet theorem without the guard, nor a proof for all width-three posets.

## Template 1: six vertices, exact boundary identity

Vertices a,b,c,d,e,f. Hasse relations:

- a<c, a<d, b<d, c<e, b<f, c<f.

The three maximal vertices are d,e,f, forming a size-three antichain. The chain decomposition (a,c,e), (b,d), (f) shows width exactly three. The comparability graph is connected.

At r=5, columns omit d,e,f respectively:

| count | omit d | omit e | omit f |
|---|---:|---:|---:|
| F | 7 | 8 | 9 |
| A1: a before b | 5 | 5 | 6 |
| A2: b before c | 4 | 6 | 6 |

The only incomparable pairs in the common intersection {a,b,c} are the two displayed. Each A_i≥F/2, and 2A1+A2=2F. Hence p1,p2≥1/2 and 2p1+p2=2; at least one lies in [1/2,2/3]. Neither fixed pair covers the simplex: q1=5/7>2/3 in column d, and q2=3/4>2/3 in column e. The HH common-slack optimum is exactly zero, so strict inequalities and the inclusion of balance endpoints matter.

Actual guarded completions realize the fixed-pair failures. Add one new vertex above C\{d}, obtaining B=(2,1,1), and p1=21/31>2/3. Instead add one vertex above C\{e}, obtaining B=(1,2,1), and p2=22/32=11/16>2/3. In both cases the new vertex has five core predecessors and cannot occur by rank five.

## Template 2: six vertices, nondegenerate triangle and strict margin

Remove only the relation a<d from Template 1. Hasse relations:

- a<c, b<d, c<e, b<f, c<f.

Again width exactly three and connected. At r=5, columns omit d,e,f:

| count | omit d | omit e | omit f |
|---|---:|---:|---:|
| F | 7 | 9 | 10 |
| A1: a before b | 5 | 5 | 6 |
| A2: b before c | 4 | 7 | 7 |

Here 2F−2A1−A2=(0,1,1), while A_i≥F/2. Thus 2p1+p2≤2 and an adaptive balanced pair exists. The q-columns (5/7,4/7), (5/9,7/9), (3/5,7/10) are noncollinear, so this is a genuinely two-dimensional completion-state profile, not a duplicated two-state profile.

A sharper exact statement is max_μ min(p1,p2)=15/23<2/3, achieved in the closed simplex at μ=(14/23,9/23,0). Both rows are at least 5/9, so one displayed pair always has probability in [5/9,15/23]. Neither fixed pair covers: q1=5/7>2/3 in column d and q2=7/9>2/3 in column e.

These failures also occur for lawful positive completions, not only at formal simplex vertices. Attach a five-vertex chain above C\{d}. Its continuation vector is B=(6,1,1), and p1=41/61>2/3. A single vertex above C\{e} gives B=(1,2,1), and p2=5/7>2/3.

## Template 3: seven vertices, three minimal and three maximal vertices

Vertices a,b,c,d,e,f,g. Hasse relations:

- a<d, b<e, a<f, c<f, b<g, d<g.

Minimal vertices a,b,c and maximal vertices e,f,g are three-element antichains. The chain decomposition (a,d,g), (b,e), (c,f) shows width exactly three. The comparability graph is connected.

At r=6, columns omit e,f,g:

| count | omit e | omit f | omit g |
|---|---:|---:|---:|
| F | 40 | 54 | 75 |
| A1: a before b | 28 | 30 | 42 |
| A2: a before c | 26 | 40 | 45 |
| A3: b before c | 18 | 38 | 40 |
| A4: b before d | 26 | 42 | 61 |
| A5: c before d | 28 | 28 | 60 |

These are all incomparable pairs in the common intersection {a,b,c,d}, using the displayed orientation. Every row has an entry outside [1/3,2/3], so no fixed fully observed pair covers the simplex.

The two genuine pairs A1 and A3 suffice. Their normalized rows are q1=(7/10,5/9,14/25), q3=(9/20,19/27,8/15). Both are at least 9/20. The simple average satisfies (q1+q3)/2≤17/27 coordinatewise, so one displayed pair always lies in [9/20,17/27]. The sharp bound is max_μ min(p1,p3)=131/215, attained at μ=(16/43,27/43,0); the exact HH dual weights are (137/215,78/215).

For actual fixed-pair failures, attach a ten-vertex chain above C\{e} for B=(11,1,1): p1=380/569>2/3. Attach a nine-vertex chain above C\{f} for B=(1,10,1): p3=438/655>2/3. All added vertices have at least six core predecessors.

## Exact common-slack certificates

For each selected pair i, define h_i^L=1/3−q_i and h_i^H=q_i−2/3. A bad orientation cell requires h_i·μ>0 for every selected pair. Its common-slack LP maximizes ε under μ≥0, Σμ=1 and ε≤h_i·μ.

A rational dual consists of λ_i≥0, Σλ_i=1, η_j≥0 and ν with Σ_i λ_i h_i+η=ν·1. Then ε≤ν. A matching rational primal μ gives the exact optimum. Every cell has ν≤0 below, certifying absence of every strict bad cell.

| template | LL | LH | HL | HH |
|---|---:|---:|---:|---:|
| six-boundary | −1/3 | −7/24 | −5/21 | 0 |
| six-triangle | −16/51 | −2/9 | −5/21 | −1/69 |
| seven-three-minima | −40/177 | −2/9 | −7/60 | −37/645 |

Full rational primal vectors and dual λ,η,ν values are in `exact_templates.json`. `certify.py` computes exact LP vertices by rational Gauss–Jordan elimination, finds exact duals, checks every dual identity and primal constraint without floating point, and separately recounts every F and A entry by exhaustive permutations.

## Search scope and caveats

`search.py` generated naturally labeled posets at n=5,6,7 (357, 4,824, 96,428 respectively), restricted attention to width exactly three and exactly three maximal vertices, discarded cores with a fixed fully observed balanced pair, and used floating-point LP only for candidate discovery. `candidates.json` and `analyzed.json` are exploratory outputs. These counts are not counts of all unlabeled posets and are not a claimed exhaustive mathematical classification of the successful profiles. Only the specifically displayed exact-certified templates are promoted to results here.

Covering each simplex vertex with some pair is not sufficient to cover the interior by their union. The all-orientation certificates, or the explicit weighted inequalities above, are essential. Also, actual continuation vectors need not fill the simplex: covering its entirety is a sufficient relaxation, and an uncovered artificial vector would not itself construct a poset counterexample.

## Genuine vertex-only negative control

This is an actual six-vertex width-three core, with Hasse relations a<c, a<d, b<e, c<f. At cut five, omit d,e,f respectively. The only fully observed incomparable pairs are a,b and b,c:

| count | omit d | omit e | omit f |
|---|---:|---:|---:|
| F | 10 | 15 | 20 |
| A1: a before b | 6 | 12 | 12 |
| A2: b before c | 7 | 7 | 16 |

Each simplex vertex is covered: the first and third by q1=3/5; the second by q2=7/15. But μ=(0,3/8,5/8) gives p1=p2=27/40>2/3. The exact HH optimum is 1/120, certified in `genuine_vertex_negative.json`. Strictly positive examples exist too: μ=(1,4,6)/11 corresponds to the artificial positive weight vector B=(3,8,9), and both probabilities exceed 2/3.

More strongly, a lawful guarded completion also fails this complete menu of fully observed pairs. Add two mutually unordered chains: five new vertices above C\{e}, and six above C\{f}. Every new vertex has at least five core predecessors. Their continuation counts for omissions d,e,f are exactly (462,792,924), proportional to (7,12,14). Therefore p1=177/265>2/3 and p2=357/530>2/3. These counts were independently computed by exact continuation dynamic programming in `audit_completions.py`. This completion is not asserted to violate the 1/3–2/3 conjecture: pairs outside the fully observed menu can still be balanced. It disproves only the attempted vertex-only union-cover inference.

## Ordinal-prefix closure

Each certified exclusion also permits an arbitrary finite common lower block H. If C=H⊕T is an initial ideal, where T is one displayed core and every element of H is below every element of T, cut at r=|H|+|T|−1. Assume no outside element can occur by rank r (again, ≥r strict predecessors each is sufficient). Each state count and selected-pair direction count is multiplied by the same factor e(H), so all normalized q rows and certificates remain unchanged. Thus these are infinite families of guarded configurations, with arbitrary common ordinal prefixes and arbitrary lawful finite tails, not merely three fixed finite posets.
