# One-private-successor reverse-inclusion injection

Status: direct structural proof; an asymmetric instance of the existing T11 two-branch exchange mechanism, not a claim of new global coverage or literary priority.

## General statement
Let p,q be incomparable elements of a finite poset P. Suppose there are distinct x,y such that the **complete strict upper sets** satisfy

- U(q)\\U(p)={x};
- U(p)\\U(q)={y};
- D(p)⊆D(q);
- D(y)\\{p}⊆D(x)\\{q};
- U(x)⊆U(y).

Then, under the uniform law on all linear extensions of P,

    Pr(p<q) >= 1/2.

No degree bound or autonomous-module hypothesis is used. The upper-set differences imply q<x and p<y, while p∥x and q∥y; also x∥y. In particular, all four labels are distinct.

## Injection from q<p to p<q
Take a linear extension L with q<p. There are two disjoint cases.

### Case 1: p<x
Swap p and q only.

Moving p to the former position of q is legal because D(p)⊆D(q). Moving q to the former position of p does not cross a successor: its only successor not already a successor of p is x, which by the case condition is later than p. Its predecessors remain before its new position. Moving p earlier cannot cross one of its successors. Thus the image is a legal extension with p<q.

The image satisfies q<y: y is unchanged and originally follows p.

### Case 2: x<p
Simultaneously swap p with q, and x with y.

The original order includes q<x<p<y. The new positions have p<y<q<x.

- p moves earlier to the former q-position. Its predecessors are available by D(p)⊆D(q).
- q moves later to the former p-position. Every unchanged successor of q is also a successor of p and was after the original p-position; its exceptional successor x moves to the original y-position, also later.
- y moves earlier to the former x-position. Its predecessor p is now at the former q-position. Every other predecessor of y belongs to D(x)\\{q}, hence precedes the original x-position and is unchanged. Moving y earlier cannot violate a successor constraint.
- x moves later to the former y-position. Its unchanged predecessors already preceded the original x-position; its predecessor q is now at the original p-position, still earlier. Every successor of x is a successor of y by U(x)⊆U(y), hence lies after the original y-position and is unchanged.

No hidden cross-relation involving the four labels is omitted: p∥x, q∥y, and x∥y follow from the exact upper-set differences. Thus the image is legal and satisfies p<q.

The image satisfies y<q, since y occupies the old x-position and q the old p-position.

## Injectivity
Within each case the map is a fixed label permutation, hence injective. The two image classes are disjoint: Case 1 has q<y, Case 2 has y<q. Therefore the union map is an injection, proving the probability bound.

## Instantiation in the 15-point free-gate obstruction
Use p=c2, q=s, x=a2, y=f0. The exact sets are

    D(c2)={c1} ⊆ {v,c1}=D(s),
    U(s)\\U(c2)={a2},
    U(c2)\\U(s)={f0},
    D(f0)\\{c2}={v,c1,d,e}
        ⊆ {v,c1,b,d,e}=D(a2)\\{s},
    U(a2)=∅ ⊆ {f2,f3}=U(f0).

Hence Pr(c2<s)>=1/2 without linear-extension enumeration. The independently checked finite value is 111970/201453, but is not used in the proof.

## Exact scope
This proves only the displayed lower bound. It does not prove Pr(c2<s)<=2/3, does not establish Pr(a2<f1)<=1/2, and supplies no new global 1/3–2/3 coverage by itself. The earlier birth-conditioned nine-point calculation 486/900>1/2 remains an obstruction to silently replacing the original measure by a uniformly sampled post-birth remainder.
