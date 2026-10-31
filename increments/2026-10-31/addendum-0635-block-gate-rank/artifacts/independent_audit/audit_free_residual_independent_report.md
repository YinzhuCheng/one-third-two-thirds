# Independent audit: 15-point free-interface fixed-menu obstruction

## Result and limitation

**All requested finite checks pass.** The unique candidate in `free_residual_hits.json` is a complete C2 poset with `|A|=5`, `Delta=9`, `A\\U(d)={s}`, `b || s`, `e<F`, exactly one d-only point `h=a1`, and no common anchor (hence no double anchor). Its two fixed-menu pairs `(c1,v)` and `(c1,d)` are both unbalanced. It has no primal or dual very-good pair, its full S112 mixed graph is acyclic, and it has no proper nontrivial autonomous module.

**This is not a counterexample to the 1/3–2/3 conjecture and is not a witness avoiding every actual good-pair criterion.** There are nine balanced unordered pairs in the entire poset. In particular `(a2,f1)` is balanced and satisfies the actual primal good-pair conditions, with probability `88349/201453 < 1/2`.

## Exact counts, independently checked twice

A two-sided ideal dynamic program and a separate direct enumeration of every linear extension both give

- `N = 201453`;
- `R0 = #{c1 before v} = 66867`;
- `K = #{c1 before d} = 137524`.

Thus

`q0 = 66867/201453 = 22289/67151 = 1/3 - 284/201453 < 1/3`,

`p(c1<d) = 137524/201453 = 2/3 + 3222/201453 > 2/3`.

Both pairs of the fixed menu therefore fail to be balanced. The stronger proposed upper bound also fails:

`2K-N-R0 = 6728 > 0`, equivalently

`p(c1<d) - (1+q0)/2 = 3364/201453 > 0`.

The algorithm has 113 reachable ideals; the separate recursion visits all 201453 extension leaves. All unordered pair counts satisfy `count(a<b)+count(b<a)=N`.

## Structural certificate

The supplied relations were read in full, directed reachability was recomputed independently, and absence of a directed cycle was checked before any poset property was used. The full strict downsets and upsets, source generating relations, transitive reduction, and all pair counts are in the JSON certificate.

- `D(v)=empty`, `I(v)={c1,c2}`, and `c1<c2`.
- `T=U(v)\\U(c1)={b,d,e}`, with the only induced relation `d<e`; hence `T=b disjoint-union (d<e)`.
- `A=(U(v) intersect U(c1))\\U(c2)={s,a1,a2,a3,a4}`.
- `F=U(c2)={f0,f1,f2,f3}`; all four are above `e`.
- These sets, together with `{v,c1,c2}`, partition all 15 vertices.
- `S=A\\U(d)={s}` and `b || s`.
- `(A intersect U(d))\\U(e)={a1}`, and `a1 || e`; hence the unique d-only point is `h=a1`.
- `R={a2,a3,a4}` and `U(s)={a2,f1,f2,f3}`.
- None of `a2,a3,a4` is below `f0`, so not even one of them is below every point of `F union U(s)`. This is a zero-anchor example, not merely an example with fewer than two anchors.

Incomparability degrees, in source vertex order `v,c1,c2,b,d,e,s,a1,a2,a3,a4,f0,f1,f2,f3`, are

`2,4,9,7,4,5,8,7,8,7,7,7,4,2,1`.

## Full-poset screening audit

For every incomparable unordered pair, checked:

- primal very-good: equal strict downsets and both upset differences chains;
- dual very-good: equal strict upsets and both downset differences chains.

Both result lists are empty.

For every incomparable ordered pair `(x,y)`, added S112 arcs from either rule

- `D(x) subset D(y)` and `U(y)\\U(x)` is a chain;
- `U(y) subset U(x)` and `D(x)\\D(y)` is a chain.

All strict poset arcs were also retained. There are 30 primal and 30 normalized-dual incomparable arcs, 37 distinct incomparable arcs in their union. The following order respects **every** arc:

`v,c1,d,b,e,c2,s,a1,a3,f0,a4,a2,f1,f2,f3`.

Therefore the full mixed graph has no directed cycle. This conclusion uses the whole 15-point P, not an induced core.

For autonomous modules, checked every one of the `2^15-15-2=32751` proper vertex subsets of size at least two. For each outside vertex, tested that its relation to all vertices of the subset is uniform (below all, above all, or incomparable to all). No subset passes.

## Global balanced pairs and actual good-pair caveat

The nine balanced unordered pairs (orientation as shown) and their numerator over `N=201453` are:

| Pair | Count |
|---|---:|
| `(c2,b)` | 70411 |
| `(c2,e)` | 89094 |
| `(c2,s)` | 111970 |
| `(b,e)` | 127776 |
| `(e,s)` | 123788 |
| `(a1,a3)` | 104963 |
| `(a2,a4)` | 98133 |
| `(a2,f1)` | 88349 |
| `(a4,f1)` | 86947 |

For the especially relevant good pair:

`D(a2)={b,c1,d,e,s,v} subset D(f1)={a3,b,c1,c2,d,e,s,v}`,

`U(f1)\\U(a2)={f2,f3}`, a chain since `f2<f3`, and

`p(a2<f1)=88349/201453`, which lies strictly between `1/3` and `1/2`.

Consequently it is valid to call this a residual relative to **the specified very-good / S112-cycle / autonomous-module screens**, but not a residual avoiding all good-pair tests. Acyclicity of a hypothetical no-balanced-pair forcing graph does not assert that every forcing direction actually has probability above `1/2` in a poset that has balanced pairs.

## Exact logical consequence

This one rigorously counted finite example refutes any universal claim that the displayed free-interface, one-d-only-point hypotheses (even after the three listed structural screens) guarantee balance of the fixed menu `{(c1,v),(c1,d)}`. It also refutes the corresponding stronger bound `p(c1<d) <= (1+q0)/2` in that domain.

It does not refute a theorem retaining the double-anchor hypothesis, does not show that the global poset lacks a balanced pair, and does not prove a classification or a general impossibility statement about other menus. No conclusion about an infinite family is inferred from this finite computation.

## Reproducibility

- Script: `audit_free_residual_independent.py`
- Detailed certificate: `audit_free_residual_independent_result.json`
- Source SHA-256: `8b915c872eacbac5eb95dd1ff751a1c0dc17eaa6a8511067fdce0742bb2cba60`
- All files for this audit are under `/tmp`; no repository was changed.
