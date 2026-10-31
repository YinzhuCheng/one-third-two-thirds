# Nonuniform-window boundary and an exact local rescue criterion

These statements concern reference or conditioned windows. They do not automatically assert a theorem about an arbitrary realized C2 after mixing its true external weights.

## 1. Smallest actual-poset warning
Q={e,m,l}, e<m, L={l}, M={m}, C=empty gives B=8>Z=6. The common-window one-point reference means are equal, yet a single unmatched lower predecessor e invalidates the desired comparison. This is the three-point method counterexample, not a C2 example.

## 2. Mean advantage does not repair shifted lower endpoints
Let X~Beta(2,1) on [0,1], representing the top of a two-point chain in its uniform order polytope. Let Y~Uniform[1/4,1]. Their means are
  EX=2/3 > 5/8=EY.
But at cutoff z=1/4,
  E min(X,z)=z-z^3/3=47/192 < 1/4=E min(Y,z).
Thus even one anchored chain, a common upper endpoint, and a strict mean advantage do not give all truncated-mean comparisons once the lower endpoints differ. The original forest mean criterion cannot be transferred unchanged to such windows.

## 3. Exact cutoff-aware sufficient condition in the simplest shifted case
Let X~Beta(2,1) on [0,1], Y~Uniform[delta,1], 0<=delta<1. For a specified cutoff delta<=z<=1,
  E min(X,z)=z-z^3/3,
  E min(Y,z)=z-(z-delta)^2/[2(1-delta)].
Consequently the desired comparison is **equivalent** to
  3(z-delta)^2 >= 2(1-delta) z^3.
This supplies a genuine, exact nonuniform-window condition with a retained cutoff. It is not the old mean-only condition. For z>=1, the condition becomes delta<=1/3 by comparing full means. For 0<z<=delta, the desired inequality fails whenever delta>0.

For physical windows [a,b] for X and [c,b] for Y, use delta=(c-a)/(b-a) and z=(cutoff-a)/(b-a), assuming a<=c<b. This formula is usable only if the actual conditional reference distributions and all interfaces have really been established. It is not applicable to the 15-point residual merely because a two-point chain occurs somewhere in its diagram.

## 4. Safe meaning of 'reselect M'
In the C2 deletion interface, B is the fixed count sum first(M union C)=sum first(F), while Z is sum first(L union C), **not** first(L union F). Moving a point from C to M is harmless only if BOTH first-hit targets are preserved; preserving M union C alone is insufficient. Replacing M by an ancestor outside F changes B and introduces an additional waiting term; it is not a proof of the original inequality.

For the 15-point residual, the exact minimal target frontiers are B:{f0,f1} and Z:{a1,a2,f1}, because a1<a4 and both f0,f1 lie below f2<f3. Their common frontier point f1 must remain the shared cutoff in a disjoint exact frontier representation: C_front={f1}, M_front={f0}, L_front={a1,a2}. In particular moving f1 from C into M drops it from the Z target and is NOT harmless. The frontier reduction removes redundant a4,f2,f3 from the targets, but those vertices remain in Q and still impose their real window restrictions. These identities do not change the proved reverse sign B>Z.

## 5. Do not lift a deleted-poset comparison without restoring the measure
The reverse critical-pair proof applies to a1,f0 inside Q=P\{v,b,c1,c2}. They are not a critical pair in the original P: the deleted b is a predecessor of a1 but not f0, while c2 is a predecessor of f0 but not a1. In fact the original finite example has
  p_P(a1<f0)=144124/201453>2/3.
Thus this pair is not an alternative balanced pair in P. The deletion-level obstruction cannot be silently promoted to such a claim. Finding a different balanced-pair mechanism remains open in this branch; the known pair a2,f1 is handled by the separate strict-four-gate result.
