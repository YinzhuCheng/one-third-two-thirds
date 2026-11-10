# 数学源稿副本｜ROOT_INSERTION_KERNEL.md

原研究稿标签：q18-joint-pivot-orbit-independent-20261109 :: PROOF.md。

原稿 SHA256：112a23a2872920aaa47d43ad9836691535086cd1d1860139dae0801dc1e693be。原数学正文与原审查状态保留；仅公开路径规范化。

原日期与原接受范围按历史保留；较早停止线不倒改，新精确通道结论以主证明为准。原稿来源标签若未在本增量提供，标为 upstream-source，不是本仓库已迁入的文件。

---

# Independent audit: complete physical v/x insertion orbit

2026-11-09 UTC. PASS_WITH_EXACT_SCOPE. NO NEW DELTA-2/3 PAYMENT.

No hard mathematical gap was found in the frozen candidate's new
joint-orbit formulas, original shared-budget bounds, actual P19 local
obstruction, or stated non-results. This is an independent natural
analytic reconstruction, not a blind review or machine-formal proof.
The candidate, proposed witness, and expected arithmetic were supplied
before checking; the derivations below, not agreement, support the verdict.

## 1. Exact frozen input and inherited interfaces

All paths here are relative to
research-review/b2-terminal18-global-mechanism-20261108.

The newly reviewed main candidate is
upstream-source(q18-joint-pivot-orbit-analysis-20261109 :: PROOF.md), 17609 bytes, SHA256
97765d8f5825f738fc2a205f0901b805ec5772a8ae33c51b4fc0ba0d68b7e629.
It was read completely and its actual byte count and hash checked.
The separately frozen candidate DU_JOINT_MASK_ADDENDUM.md in that
same directory, 2836 bytes, SHA256
3ad3b4db38b79ee337f64458179dbf18a09c6c6d8c525d2eec526e1b976c0740,
was also fully read and checked. The two frozen inputs total 20445 bytes.

The accepted baseline is
q18-root-joint-kernel-independent-20261109:
- PROOF.md, 19681 bytes, SHA256
  feb2468ee212accbcd2b0073b8fed8a4e22c7d4c8d8b8aff23d1e676fb53b5ff;
- REVIEW.md, 2312 bytes, SHA256
  7a4792d2046186bcb1ffae44b06baa1e6b739134b3dc99dcc0752350f5dfd998;
- MANIFEST.tsv, 1792 bytes, SHA256
  79a96f38257c12d025cd98ce92f3f956fd00da47b04b6e0643d674cf567d0ea3.

Those fingerprints were checked and the relevant accepted interfaces
consulted. No ancestral proof, earlier population, or payment was rerun.
In particular this audit inherits, rather than re-proves, the structural
Q18 class contract, the three-root F/G lift law, and the already accepted
same-fixed-x T/J orbit law.

The physical witness tables are from the existing
upstream-source(q18-real19-outside-bank-control-independent-20261109 :: PROOF.md),
18302 bytes, SHA256
42b4476f41b5db06c0cf1d845ec1b7b7ddf83245c73f59eafddc5798b725f5d2.
This fingerprint was checked. Its full D/U tables, not an invented
profile or completed relation template, determine the witness used here.
Its old whole-poset count is not a dependency of this local conclusion.

For inherited scope only, the existing exact-audit REVIEW.md (2828 bytes,
SHA256 253ccc058115eb414b9185fb1d185eecbc3560ccc0f12fc9bddb3a5ef1a34e80)
and RESULTS.json (7949 bytes, SHA256
1a280cc7c85138519ed43d49e719c7c8a9f08f80a4b3f0f55b1913e2d1c418c0)
under that P19 directory were read and fingerprinted. Their reviewed
whole-P counts are inherited evidence, not a counting execution here.

The author's historical PENDING INDEPENDENT REVIEW label stays frozen.
It neither overrides this fresh verdict for these exact bytes nor
extends this verdict to any later revision or ancestral claim.

## 2. Original hypotheses and the accepted lift laws

Fix one complete ORIGINAL finite P in the supplied Q18 one-saturated
scope: maximum full incomparability degree at most ten; induced ideal
(a,b,c,u,v) with exactly a<u, a<v, b<c; complement of the inclusive
a-upset {b,c}; D(c)={b}, D(u)=D(v)={a}; complete actual common upset O
of c,u,v; |P minus O|=18; unique zero deficit at u; structural q=r_v=0;
m=|Y|=|C_u| in {1,2,3}; delta=delta_v in {2,3}. No NB hypothesis is
imposed on any local word or on this full base domain.

Use A=C_c, V=D_u, k=|C_v|. The inherited structure gives

  |D_c|=4-m, |A|=9-m-delta, |V|+k=m+delta, 2<=k<=4,
  D_c<Y<O, with nonempty Y an original chain.

Original signatures are D_c above c only, V above u only, A above u,v,
C_v above c,u, Y above c,v, and O above c,u,v. Missing pivot relations
are incomparabilities. Every actual internal order, lower/b port, and
exterior relation is retained. Fix one physical minimal x in P[D_c]
ONCE. The accepted signature argument gives D(x)={a,b,c}; it does not
make x a least point of D_c.

With counts taken over full original extensions, set

  I_x={c before v before x},
  B_x=K_vc+K_xv+K_ba-N=K_ba-K_Ix.

This last identity is pointwise because c<x: vc, xv and I_x form an
actual disjoint partition. It is not the old global two-map identity.

For r>=0 and h>=1 the inherited root kernel is

  F(r,h)=sum_(i=0)^(min(r,h)-1) (r-i),
  G(0,h)=0; G(r,h)=F(r,h)+r+1 for r>=1.

On an actual word after deleting a,b,c, first original b/c-successor
deadlines h<=q give root mass G(q,h), ba mass q+1, and c-before-rank-s
mass G(min(s,q),h). Initial root orders and shared-root-gap
multiplicities are already included. G(0,h) is no allowed c slot, not
the lift count of an empty residual word.

For an actual rho after deleting a,b,c,x, let H<=Q<=L be its first
original b,c,x-successor ranks and let s be the rank of v. Inserting x
in gaps g=0,...,L-1 gives root deadlines min(H,g+1), min(Q,g+1). The
accepted all-x-slot laws are

  T(L,Q)=L(Q+1)-Q(Q-1)/2,
  J(L,Q,H,s)=(L-s)_+ G(min(s,Q),H).

They give ba and I_x mass, respectively, not normalized probabilities.
All later uses satisfy their physical-x and original-word hypotheses.

## 3. Independent joint insertion bijection and all boundaries

Let R_5=P minus {a,b,c,x,v}; fix an actual complete pi in LE(R_5),
of length n. Define h,q,ell,t to be the one-based first ORIGINAL
b,c,x,v-successor ranks in this physical word. The local q here is
not the structural parameter q=0. Successor inclusion gives h<=q<=ell.
In the application Y supplies a successor of each of these four labels.

For an empty successor set in the wider insertion setting, its deadline
is n+1, not n. This retains the final gap. The same proof below applies
with that sentinel. In particular the possible v ranks are
r=1,...,t, corresponding to pi gaps j=r-1.

Neither x nor v has a predecessor left in R_5: their full downsets are
{a,b,c} and {a}. They are originally incomparable. Thus inserting v
before its first original successor is necessary and sufficient. The
first old b,c,x successor shifts by one exactly when v is inserted
before that label. Since v itself is not a b,c,x successor,

  H_r=h+1[r<=h], Q_r=q+1[r<=q], L_r=ell+1[r<=ell].    (1)

Equality belongs in each indicator: inserting at rank h places v
immediately before the old rank-h label. For a missing successor,
h=n+1 gives H_r=n+2 for every possible r, the correct new sentinel.
The same check applies to q and ell.

Next insert x in every rho gap g=0,...,L_r-1, then lift the roots by
the accepted kernel. This checks all original edges: pi retains edges
among its labels, the v deadline checks all v-upset edges, the x
deadline checks all x-upset edges, and root deadlines check all root
edges. There is no additional hidden predecessor of v or x.

Both v/x orders in one original pi gap are included. If j precedes both
their first successors, r=j+1 is fixed after inserting v. The gap
g=j=r-1 inserts x just before v; g=j+1=r inserts x just after v.
Both are legal since j<ell gives L_r=ell+1>r. They are distinct words.
Conversely deletion of roots and x recovers a unique rho, and deletion
of v recovers pi and j. Each final word has a unique x gap in that rho.
Thus the two same-gap orders are counted once each, and no other gap
or order is duplicated or omitted, including the final gap when allowed.

The full O word remains in pi. No outside tail or port is removed or
given a substitute multiplicity. Every constructed lift is of the SAME P.

## 4. Target and debit derivation

Put C=T(ell,q), a0=min(t,q), b0=min(t,ell). In (1) there are only three
symbolic regions, with no parameter enumeration:

- If r<=q, then Q_r=q+1 and L_r=ell+1, so
  T(L_r,Q_r)=(ell+1)(q+2)-q(q+1)/2=C+ell+2.
- If q<r<=ell, then Q_r=q and L_r=ell+1, giving C+q+1.
- If r>ell, both deadlines are unchanged, giving C.

Therefore the ba mass above pi is

  a0(C+ell+2)+(b0-a0)(C+q+1)+(t-b0)C
    =tC+(q+1)b0+(ell-q+1)a0.                       (2)

For I_x, substitute s=r into J. If r<=ell then L_r-r=ell+1-r.
If r>ell, L_r-r=ell-r<0 and the positive part vanishes. For r<=q,
min(r,Q_r)=r. If r<=h also, H_r=h+1 but both h,h+1 reach the cutoff r,
so F(r,h+1)=F(r,h). If r>h, H_r=h. For r>q, h<=q<r implies H_r=h
and Q_r=q. Thus in all contributing cases the root factor is exactly

  G(min(r,q),h).

Consequently

  K_Ix,pi=sum_(r=1)^b0 (ell+1-r)G(min(r,q),h),        (3)
  H(pi)=tC+(q+1)b0+(ell-q+1)a0-K_Ix,pi,
  B_x=sum_(pi in LE(R_5)) H(pi).                     (4)

This last sum follows from the bijection, not from choosing a law on
deadline tuples. The actual full-P probability of a pi is N_pi/N.

For completeness split (3) at a0. In the remainder r=a0+1,...,b0
the cutoff is q. Summing its consecutive factors ell-a0 through
ell+1-b0 gives

  K_Ix,pi=sum_(r=1)^a0 (ell+1-r)G(r,h)
    +G(q,h)(b0-a0)(2ell+1-a0-b0)/2.                 (5)

If a0=b0 the second part is the empty sum, exactly zero. This also
covers t<=q without making the incorrect assertion that the cutoff
is already q at earlier ranks.

For the other original event counts, write

  W_rg=G(min(Q_r,g+1),min(H_r,g+1)).
  N_pi=sum_(r=1)^t sum_(g=0)^(L_r-1) W_rg,
  K_xv,pi=sum_(r=1)^t sum_(g=0)^(min(r,L_r)-1) W_rg.  (6)

The second summation uses g<r, precisely the slots before v. It includes
the x-before-v order in a shared original gap. The pointwise partition
gives K_vc,pi=N_pi-K_xv,pi-K_Ix,pi. Root weights W_rg are not all equal.
All coefficients of any bank must be fixed at original-P level before
taking these sums.

## 5. Shared original degree budget and support restrictions

Write deg_P for full-original incomparability degree. A label before
the first successor of b,c,x,or v in pi cannot be its predecessor:
the full predecessors of each were deleted. It is therefore incomparable.
Charge also deleted incomparable labels, rather than using independent
residual budgets:

- For b the prefix contributes h-1, and deleted a,v contribute two:
  h+1<=deg_P(b)<=10, hence h<=9.
- For c the prefix contributes q-1, and deleted a,v contribute two:
  q+1<=deg_P(c)=3+|A|+|V|=12-k, hence q<=11-k<=9.
- For x the prefix contributes ell-1, and deleted v contributes one:
  ell<=deg_P(x)<=10.
- For v the prefix contributes t-1, and deleted b,c,x contribute three:
  t+2<=deg_P(v)=3+|D_c|+|V|+k=7+delta,
  hence t<=5+delta<=8.

Here c's original incomparable seed labels are a,u,v; v's are b,c,u.
The equalities use the original signatures and sizes, not a residual
degree bound. The prefix counting remains valid at an end sentinel.

Define the SINGLE physical missing set

  M_x={z in (D_c minus {x}) union C_v: z incomparable with x},
  d_x=|M_x|.

A remaining D_c label cannot precede x by x's original minimality.
A C_v label cannot precede x because it lies above u whereas x does not.
Each such label is consequently either an x successor or in M_x.
The forced other incomparabilities are u,v,V,A; Y and O are successors.
Thus the exact set and budget are

  I_P(x)={u,v} union V union A union M_x,
  deg_P(x)=2+|V|+|A|+d_x=11-k+d_x<=10,
  d_x<=k-1<=3.                                     (7)

The two prefix estimates must use this SAME set, not a fresh allowance
for D_c and another for C_v. Before both the first c successor and the
first v successor, only u and V are possible: D_c and C_v follow c,
A follows v, and Y,O follow both. Hence

  min(q,t)-1<=1+|V|, so min(q,t)<=|V|+2
    =m+delta-k+2<=6.                               (8)

Before both the first x successor and the first v successor, only
u,V,M_x are possible. All other D_c/C_v labels follow x and A,Y,O
follow v. Hence

  min(ell,t)-1<=1+|V|+d_x,
  min(ell,t)<=|V|+d_x+2<=m+delta+1<=7.               (9)

The bounds count actual labels in actual prefixes. They are necessary
conditions on one original word, not realizability criteria for arbitrary
tuples or permission to choose unrelated endpoint budgets.

Also |A|=9-m-delta>=3>=d_x. This is only a cardinality inequality:
it provides no matching respecting lower/b ports and O, no injection,
and no weighted compensation between early A and C_v placements.

If q=t, the common first label belongs to U(c) intersect U(v), namely
Y union O in this domain. It is an x successor. Thus ell<=q, and
q<=ell gives ell=q=t. This verifies the exact tie restriction.

Finally, if all original b->V ports are present, a label before the first
b successor can only be u or a b-incomparable A label. The other retained
classes are b successors. Hence h<=2+|{z in A:b incomparable z}|<=|A|+2.
This improvement is conditional; it must not be used when a b->V port
is missing. No direction of an original bank pair follows from it.

## 6. Verify the existing P19 word directly from its full tables

This diagnostic uses exactly the previously reviewed original P19:

  D_c={x}, V={d1,d2}, A={A1,A2,A3},
  C_v={B1,B2,B3,B4}, Y={Y1,Y2,Y3}, O={o}.

The relevant STRICT ORIGINAL downsets in its table are:
u,v have {a}; x has {a,b,c}; d1 has {a,b,u}; d2 has {a,b,u,d1};
A_j has {a,b,u,v,d1,d2} plus earlier A labels;
B_j for j<=3 has {a,b,c,u} plus earlier B labels;
B4 has {a,b,c,u,x,B1,B2,B3};
Y_j has {a,b,c,v,x} plus earlier Y labels;
o has Q minus {A3,B4}.

After deleting a,b,c,x,v, consider the complete word

  pi=u,d1,d2,B1,B2,B3,A1,A2,A3,B4,Y1,Y2,Y3,o.

Check every remaining type directly. The d1,d2 requirements are u and
then d1, all earlier. Each B1,B2,B3 requires u and its earlier B prefix;
B4 additionally required deleted x. Each A label requires u,d1,d2 and
its earlier A prefix; its v predecessor was deleted. Each Y label only
requires its earlier Y prefix among remaining labels. The final o is
after every required remaining label. The complete word is therefore
legal in the actual deletion of this P19, not merely in a relaxed class
template. Placing A3,B4 before o is legal although they are not required
predecessors of o.

From the ORIGINAL upset tables, the first b successor is d1 at rank 2;
the first c successor B1 at rank 4; the first x successor B4 at rank 10;
and the first v successor A1 at rank 7. Thus

  (h,q,ell,t)=(2,4,10,7).

Here m=3, delta=3, k=4, |V|=2. The missing set is exactly
M_x={B1,B2,B3}; all three share the one budget d_x=3=k-1.
The forced x incomparables number 2+2+3=7, so deg_P(x)=7+3=10.
Both shared prefix bounds are sharp: min(q,t)=4=|V|+2 and
min(ell,t)=7=m+delta+1. Full b->V ports are also present.

No source was generated or searched for. This is one supplied actual
word of the existing source, with all original labels and exterior o.

## 7. Independent natural arithmetic for all seven v ranks

For h=2, G(1,2)=1+2=3, and for r>=2,

  G(r,2)=[r+(r-1)]+r+1=3r.

First compute C=10*5-4*3/2=50-6=44. Formula (2) then gives ba mass
44+10+2=56 for each of r=1,2,3,4, and 44+4+1=49 for r=5,6,7.
Therefore

  K_ba,pi=4*56+3*49=224+147=371.

The debit uses the seven direct products

  10*3, 9*6, 8*9, 7*12, 6*12, 5*12, 4*12
    =30,54,72,84,72,60,48.

The first four sum to 240 and the last three to 180, so K_Ix,pi=420.
Equivalently the first part is
3*[11*(1+2+3+4)-(1+4+9+16)]=3*(110-30)=240,
and the last part 12*(6+5+4)=180. Thus H(pi)=371-420=-49.

Independently inspect the root masses in (6). For r=1,2 the deadlines
are H_r=3,Q_r=5,L_r=11. As g runs through the first five legal x gaps,
the root counts are

  G(1,1)=3; G(2,2)=6; G(3,3)=10;
  G(4,3)=(4+3+2)+5=14;
  G(5,3)=(5+4+3)+6=18.

The remaining six gaps each have 18. Their total is
3+6+10+14+18+6*18=51+108=159.

For r=3,4 the deadlines are H_r=2,Q_r=5,L_r=11. The first five
counts are 3,6,9,12,15 and the other six each 15. Their total is
45+90=135.

For r=5,6,7 the deadlines are H_r=2,Q_r=4,L_r=11. The first four
counts are 3,6,9,12 and the other seven each 12. Their total is
30+84=114. Therefore

  N_pi=2*159+2*135+3*114=318+270+342=930.

The x-before-v sector keeps precisely the first r of those gap masses.
This yields 3,9,18,30,42,54,66, whose sum is 222. Subtracting the
already checked I_x and xv masses from each rank's N gives the full
event check below. These are evaluations of seven prescribed rank
groups, not enumeration of original sources or full extensions.

  r   N    ba   I_x  xv   vc   ba-I_x
  1   159  56   30   3    126   26
  2   159  56   54   9     96    2
  3   135  56   72   18    45  -16
  4   135  56   84   30    21  -28
  5   114  49   72   42     0  -23
  6   114  49   60   54     0  -11
  7   114  49   48   66     0    1

The vc sum is 126+96+45+21=288. Thus independently

  288+222+371-930=-49.

All legal positions of both physical labels and every root-lift
multiplicity are included. No selected v ranks, x gaps, root orders,
or exterior positions within this fixed-pi orbit have been omitted.

## 8. Exact obstruction scope and remaining correlation

This actual orbit falsifies the universal sufficient condition

  H(pi)>=0 for every actual pi in this base domain,

for the unit bank (vc,xv,ba) with threshold N. The falsification persists
after imposing the proved shared budgets and full b->V ports, since the
witness satisfies them. Strengthening only necessary tuple conditions
cannot legitimately remove an actual original word.

It does NOT falsify B_x>=0 after summing all actual pi of P19 or any
other original, any other fixed bank, the balanced-pair conjecture, or
a reference domain additionally restricted by original NB/other guards.
It proves no original bank direction, no new payment, and no authority
to remove paid sources. The already reviewed exact-audit records give
N=10269963 and K_ba=4511797. They establish balanced ba and nonNB,
with 10269963<3*4511797=13535391<20539926. The same inherited records
give K_vc=3248466 and K_xv=3221064, whose unit-bank arithmetic is
3248466+3221064+4511797-10269963=711364>0. Thus this particular
negative local orbit actually coexists with a positive full-P margin.
These whole-P counts are inherited, not re-counted or newly audited;
neither is required by the local obstruction.

Each orbit fixes the relative order of every label in pi, including the
complete O word and the D_c word with x removed. Moving x past another
incomparable D_c label can change the full D_c restriction word. Moving
v can cross older lower/class-prefix boundaries. Therefore only outer
conditions invariant under BOTH moves may be imposed. The physical x
and bank vector cannot be selected anew in those crossed cells.

The old H_A,R,E_x,Z_x two-map identity is a global original identity.
It cannot replace the per-pi formula without a separate invariance
proof. This review neither supplies such a proof nor assumes one.

The candidate's coarser actual-shuffle representation is valid as a
partition, with no positivity assertion. A and C_v are mutually
incomparable: A<C_v would force v<C_v, and C_v<A would force c<A,
both contradicting original signatures. Fix restriction words eta on
the complement of {a,b,c,x,v} union A union C_v, alpha on A, and beta
on C_v. Every actual pi has a unique such triple; conversely retain
only interleavings respecting ALL original ports. They partition the
same actual pi sum, each pi once. Eta retains V, other D_c, Y, and O.

Absent A/C_v cross edges do not make these shuffles freely weighted.
V->A, possible V->C_v and D_c->C_v ports, b deadlines, and actual
A/C_v-to-O edges still matter. Reordering changes h,q,ell,t jointly.
Neither |A|>=d_x nor the pointwise partition proves favorable association
or a legal weighted matching across these shuffles.

The precise open step remains a nonnegative coarser-shuffle sum, another
valid cross-pi compensation, or a different fixed original bank with
its thresholds and required directions proved. None is established
by this packet. Coverage 413809 and all payment ledgers are unchanged.

## 9. Full physical D_u/c mask joint: independent gap proof

This section reviews the separately frozen DU_JOINT_MASK_ADDENDUM.md
in the candidate directory, bound by its exact fingerprint in Section 1.
It does not change the already frozen main candidate or introduce
a new source, original pair direction, or payment.

Keep one physical V=D_u throughout P. Fix pi, one of the legal v ranks r,
and one of the legal x gaps g. For a physical d in V let p_d be its rank
in pi. The two successive rank changes are

  p_d^rho=p_d+1[r<=p_d],
  p_d^tau=p_d^rho+1[g<p_d^rho].                     (10)

The first uses insertion before the old rank-p_d label, including
equality r=p_d. The second uses exactly g old rho letters before x;
x precedes d precisely when g<p_d^rho. These shifts preserve all
physical V labels and their relative order.

Set q*=min(Q_r,g+1), h*=min(H_r,g+1). The remaining root insertion
has c-gap j with 0<=j<q*. Here j counts tau letters before c, not the
final full-word rank of c. For ANY fixed physical S subset V, the exact
event {d in V:d before c}=S is equivalent to

  j>=p_d^tau for every d in S,
  j<p_d^tau for every d in V minus S.

Define, with explicit empty-set conventions,

  lcut=max({0} union {p_d^tau:d in S}),
  ucut=min({q*} union {p_d^tau:d in V minus S}).

The legal c gaps are exactly lcut<=j<ucut. If ucut<=lcut the event is
empty and its mass is zero; do NOT subtract cumulative expressions in
that case. Otherwise 0<=lcut<ucut<=q*. The accepted cumulative root
count for c-gap j<K is G(K,h*) at each permitted cutoff K, with the
special G(0,h*)=0. Consequently the exact mask mass is

  M_S(pi,r,g)=G(ucut,h*)-G(lcut,h*) if ucut>lcut,
             0 otherwise.                         (11)

All b/c deadline restrictions are retained in this difference.
If S is not an initial segment of the actual V restriction word, an
excluded label precedes an included label. Its rank is at most lcut,
so ucut<=lcut and (11) is automatically zero. A prefix can also be
infeasible because q* is too early, which the same formula handles.
This is not a law assigning independent masks to the V labels.

If S is empty, lcut=0 and (11) includes the full allowed initial-gap
multiplicity, rather than subtracting G(0,h*) as though it were one
root order. If V minus S is empty, ucut=q*. If V is empty, the only
S is empty and (11) reduces to G(q*,h*)=W_rg. These conventions also
handle an empty c-gap interval without inventing an initial root lift.

In the ba sector, cumulative c-gap mass is

  Hcut(0)=0; Hcut(K)=K+1 for K>=1.

Indeed c-gap 0 allows two ba root orders, bac and bca; each later
c gap allows exactly one. Thus the joint ba-and-mask mass is
Hcut(ucut)-Hcut(lcut) for ucut>lcut, and zero otherwise.
This explicitly preserves the exceptional zero cutoff.

The exact second physical mask is

  {d in V:d before v}={d in V:p_d<r}.               (12)

Inserting x or roots cannot change the relative order of d and v.
The equality case p_d=r puts v before d, as the strict inequality
in (12) requires. Hence this mask is deterministic once pi,r are fixed.
A requested joint pair of V-before-c and V-before-v masks has the
mass in (11) when its second mask equals (12), and zero otherwise.

Other events of the main bank can be retained jointly, not just as
separate marginals. At fixed r,g, xv is the indicator g<r. The rank of
v in tau is s_v=r+1[g<r]. Thus c<v means j<s_v and v<c means j>=s_v.
Intersect [lcut,ucut) with the relevant half interval and use the same
cumulative difference. For I_x also require g>=r; for ba additionally
use Hcut rather than G. This supplies literal event intersections
without replacing the actual joint distribution by a product law.

Summing these exact masses over all legal r,g and then actual pi gives
the full original joint counts. Each lift determines unique masks, so
summing all mask classes recovers the unmasked mass, by a partition
argument rather than a mask scan. No scan, all-mask table, or additional
control is needed or performed.

The bank coefficients and every physical subset/event remain fixed in
the original P. Nothing here licenses choosing a bank after pi,r,g or
a mask is known, varying mask weights arbitrarily, discarding a class,
or inferring compensation between distinct pi. This addendum completes
the event-joint interface only. It leaves the same global sign,
cross-pi shuffle association, and payment obligations open.
