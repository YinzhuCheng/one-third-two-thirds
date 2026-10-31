# Independent audit: collision-corrected A5 witness

**Verdict: all stated structural and exact-count claims verified independently.**

Input: `sharp_rank_witness.json`.
Independent implementation: `audit_sharp_witness_independent.py` in this directory.
Machine-readable output: `sharp_witness_independent_result.json`.

## Method

The implementation does not import or invoke `check.py`. It computes transitive closure using a Boolean Floyd–Warshall matrix, checks C2 explicitly including minimality of v and incomparability of b with d,e, checks all unordered pairs for primal/dual very-good status, builds the S112 graph directly from its defining inclusions and chain tests, checks every vertex subset of cardinality 2 through 14 for autonomous-module status, and directly enumerates every full linear extension to count the specified events. Direct extension enumeration is independent of the original memoized constrained-event counting method.

## Structural results

- Complete C2 holds.
- A={s,r,t,u,w}, F={f0,f1,f2,f3}.
- A\\U(d)={s}, b<s, and e<F.
- R={r,t,u}, K={w}, hence |A|=5 and k=1.
- Maximum incomparability degree is exactly 9.
- R-predecessor sets of F targets are:
  - f0: {r,u};
  - f1: {r,t,u};
  - f2: {r,t,u};
  - f3: {t}.
- U(s)={f1,f2}; each has R-predecessor set {r,t,u}.
- Thus the maximal separate budgets are α=1, β=3.
- The common-anchor intersection is empty (already {r,u}∩{t}=∅).
- No primal or dual very-good pair exists.
- The S112 graph, including all ordinary poset edges and both primal/dual forcing edges, is acyclic. One independently computed topological order is:
  `v,c1,d,b,e,w,c2,r,s,t,u,f3,f0,f1,f2`.
- No proper nontrivial autonomous module exists.

## Direct enumeration results

N=168366,
R0=#(c1<v)=49873,
K=#(c1<d)=104621,
E=#(v<c1 and s<d)=2690,
G=#(e<c1 and some r∈R precedes c2)=11687.

Since v<d<e, the displayed G event is identical to the longer ordered-prefix condition used in the signed-defect definition. Independently, 2K−N−R0=−8997=E−G.

## Interpretation and limits

For α=1,β=3,k=1, the uncorrected rank bound has endpoint f(2)=2 and is inconclusive. The collision-corrected endpoints are f_sharp(1)=−13 and f_sharp(2)=−2, so the corrected structural theorem applies strictly. There is no common-anchor alternative at all. Together with the verified absence of the listed old structural filters, this is a valid nonredundancy witness relative to those specific hypotheses.

It is **not** a witness against every prior numerical tool: the old unsigned error budget also holds, since E=2690<N/3−R0=6249. No claim of historical novelty, exhaustive old-filter separation, or full C2 closure is justified by this finite example.

All audit artifacts were written under /tmp only; no repository or remote was changed.
