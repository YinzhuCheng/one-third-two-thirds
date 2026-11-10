# 数学源稿副本｜POPULATION_REVIEW.md

原研究稿标签：q18-delta3-population-and-old-guards-independent-20261110 :: REVIEW.md。

原稿 SHA256：a55d9a87eb96526f5e8764e5513b32fe082219d4f456a8e3d571b9c4d96cd6b3。原数学正文与原审查状态保留；仅公开路径规范化。

原日期与原接受范围按历史保留；较早停止线不倒改，新精确通道结论以主证明为准。原稿来源标签若未在本增量提供，标为 upstream-source，不是本仓库已迁入的文件。

---

# Independent audit: delta3 population and inherited old guards

2026-11-10. PASS_WITH_EXACT_SCOPE for the population classification,
m4 inherited BANK3 applicability and m1/m2 nonchain-Dc k2/3 old guards.
NO blanket k4 nonchain-Dc payment is certified. This review does not
participate in or import any new m2 bank derivation. No mathematical
program, source/word enumeration, DP/LP, replay, external write or ledger
increment. Natural analytic applicability audit, not a formal verification.

## 1. Precise original domain and population equations

Use the full ORIGINAL degree-ten seed/private/actual-Q18/selected-fork
one-saturated contract with unique population zero at child u, q=r_v=0,
all C classes occupied and delta_v3. All original b/internal/cross/O
ports and finite actual O, including empty, remain. Write m=|Y|>=1,
d=|Dc|,a0=|A|,r=|V|,k=|Cv|. There are13 nonseed Q labels.

Population delta_u0 gives r+a0+k=9. Population delta_v3 gives
1+a0+m=7, hence a0=6-m. The Q count then gives d+m=4, and
r+k=m+3. Thus 1<=m<=4. Population delta_c=10-(1+d+k+m)=5-k.
The ORIGINAL full c-incomparables are a,u,v,A,V, giving
 deg_P(c)=3+a0+r=12-k.
Full degree<=10 implies k>=2; unique zero at u and delta_c>0 imply
k<=4. Therefore the parameter range is exactly m1..4,k2..4, with
 d=4-m, A=6-m, V=m+3-k, Cv=k, Y=m.
These population deficits must not be called full-degree slack.

These algebraically admissible combinations are not ruled out by hidden
nonnegativity: r>=0 and A>=2 throughout. A simple common construction
also realizes them within the stated contract: O empty; choose each
nonempty class as an actual chain; put all V below A,Cv, all Dc below
Cv,Y, and b below V,A; retain all seed/signature-forced relations and
no other cross-class relations. Its full degrees are a2,b3,c12-k,u7,
v10,Dc11-k,V6,A5+k,Cv7,Y10 (omit empty classes). Transitive closure
preserves the prescribed signatures, actual O is empty and only u,v
have full downset {a}. This is a symbolic family, not source enumeration
or new ledger credit. It verifies that 'admissible' is not concealing an
impossible parameter branch.

## 2. Structural full profiles common to these channels

Each Y is incomparable with u,V,A,Cv, exactly
1+r+A+k=10 physical labels. Saturation forces the original Y chain,
Dc<Y and Y<O; reverse directions would add a forbidden pivot to a
signature. Thus every Dc is below every Y and every original O.
Original Dc predecessors outside Dc are precisely a,b,c. Its only
optional successors outside Dc are Cv: reverse Cv->Dc is impossible
since Cv is above u; A,V are signature-incomparable, as are u,v.
Consequently each physical z in Dc has EXACT full-degree formula
 deg_P(z)=11-k+inc_Dc(z)+miss_Cv(z).
This is the same scalar formula as in delta2, despite changed A,V
populations. There is no missing-O term for Dc: all O are already above
it via the saturated Y structure. Optional b ports elsewhere do not
alter its full profile.

In contrast a physical C in Cv has forced base
1+A+m=7 incomparable labels v,A,Y, not delta2's8. Its full budget is
 deg_P(C)=7+inc_Cv(C)+miss_Dc(C)+miss_V(C)+miss_O(C)<=10.
No other variable class contributes. This changed base is precisely why
some delta2 k4 saturation arguments cannot be transferred.

## 3. m4 is entirely inherited old BANK3 coverage

I actually read M4_ACCEPTED25_REVIEW.md sections1--2
and its stated original-law lift. It accepts BANK3 on exactly25 population
profiles: all j=c profiles, and on each child axis s_c<=s_other_child+1.
The full theorem retains original degree, seed/private/actual-Q18/selected
fork, arbitrary original open-class/D orders and arbitrary finite O.
Its word/exterior reductions preserve the same original physical
numerators with actual multiplicities; cells do not inherit original NB.
This is an inherited certified result, not re-run computation here.

For current m4, Dc is empty, j=u, and
 s=(2,4,k), r_vector=(0,7-k,0), k2/3/4.
All meet 2<=k+1. Therefore every such original source has a closed-balanced
pair among the old three bank pairs cu,cv,uv. Neither excluded profile
ID21 (j=u,s=(4,4,2),r=(0,3,0)) nor its ID15 mirror is involved.
No BANK4 repair or new numerical kernel is required. This is old coverage,
not three new paid populations or an analytic reproof of the old certificate.

## 4. m3 status is already complete, separately proved

The accepted M3_COMPLETE_REVIEW.md, SHA256
b4fc21bdcab8e3ba5d648d7e581c5979873047db8874da0831d94199114c5b26,
covers all k2/3/4, every allowed hole mask, arbitrary ports and actual O.
It gives a fixed original eight-pair balanced-pair conclusion from the
separate complete unit banks, cap and original directional bridge.
Nothing about its Y3 kernel, scalar endpoint support, bank constants or
fixed eight-pair list is transferred to m1 or m2 here.

## 5. m2 incomparable Dc: old guards at k2/3

I reread upstream-source(q18-delta2-m2-k4-chainD-one-hole-early-independent-20261110 :: NONCHAIN_DC_OLD_GUARDS_REVIEW.md), especially its full-profile argument,
and checked its parameter-dependent premises rather than importing its
entire delta2 conclusion. For m2 nonchain Dc={x,D}, x||D, both full
downsets are {a,b,c}. Both have all Y and O above; only Cv can differ.
Let L=U(x)\U(D), R=U(D)\U(x). The exact Dc budget with inc_Dc1 gives
miss_Cv<=k-2, hence |L|,|R|<=k-2.

For k2 both are empty, so x,D are original fair twins. For k3 each
private upset has at most one label; equal full downsets and these two
bounds meet the old almost-twin theorem. The physical x,D pair is
closed-balanced, with the actual entire exterior retained. No original
NB, a class-chain assumption or a completed source is needed.

## 6. m1 nonchain Dc3: old guards at k2/3

I reread upstream-source(q18-delta2-m1-xv-triple-orbit-independent-20261110 :: DIRECTION_REVIEW.md) section1. Only its Dc guard is reused, not its
later delta2 no-hole/least-point or dangerous-xv conclusion.

For k2 each Dc endpoint has allowance1 for internal incomparabilities
plus missed Cv. Any incomparable pair uses that allowance at both
endpoints, so both see every Cv. The third Dc label must be comparable
with both, on the same side by transitivity. Their full downsets and
upsets agree, including every Y/O. They are original fair twins.

For k3 the allowance is2. The actual three-point nonchains are:
- Antichain: each endpoint uses both internal units and sees all Cv;
  identical full profiles give twins.
- V or inverted V: the incomparable endpoints have equal full downsets,
  identical other-Dc profiles, and each misses at most one Cv. Their
  two full private upsets each have size at most1, so almost-twins applies.
- One comparison l<t with isolated z: z uses both units internally and
  sees every Cv. Full downsets of l,z are {a,b,c}; U(l)\U(z)={t}, while
  U(z)\U(l) is at most the one Cv point missed by l. All Y/O are common
  successors. Again the old almost-twin guard applies.
These exhaust three-point nonchains, not source or extension enumeration.
Thus original closed-NB at m1,k2/3 would force Dc to be an original
chain. The conclusion is old balanced-pair coverage of the nonchain
case; it does not certify any bank or cap in the remaining chain case.

## 7. Why k4 cannot be copied wholesale; exact retained gaps

For m2,k4 with x||D, the Dc budget only gives |L|,|R|<=2.
Opposite private endpoints are incomparable, and an l in L misses D.
But the Cv budget now gives 7+1+|R|<=10, hence only |R|<=2, NOT<=1.
The analogous bound holds for |L|. Thus the old delta2 reduction of
both-nonempty private sets to1/1 is unavailable.

If L has two incomparable labels p,q and R is empty, each endpoint's
forced contribution is base7 plus missed D plus its private peer, total9.
One further incomparability remains possible. It can be used by a V
predecessor port, an O successor port or another allowed Cv relation.
Therefore the delta2 inference that both endpoints have identical complete
lower/upper profiles and are fair twins is not justified. No claimed
actual counterexample to balance is needed to identify this failed
saturation inference. In particular missing V/O relations cannot be
ignored when invoking full-original twins.

Some k4 sources remain individually covered by ordinary old guards:
when equal full downsets have both private upset sizes<=1, almost-twins
still applies; for m2, if BOTH actual private differences are chains,
the old general slot guard applied in both directions contradicts original
closed-NB and gives SOME balanced pair. These are conditional full-profile
applications, not an exhaustive k4 classification or a guarantee that
the anchor pair itself is balanced. No blanket m1,k4 nonchain guard has
been established in this audit either.

## 8. Coverage ledger without numerical ledger claims

Certified from the inputs audited here:
- m4, k2/3/4: inherited old25-profile BANK3, all original ports/O.
- m3, k2/3/4: separately accepted full-original eight-pair theorem.
- m1 or m2, k2/3, Dc nonchain: old full-profile twins/almost-twins.
- k4: only whichever explicit old full-profile guards a source actually
  satisfies; no automatic nonchain-Dc exhaustion.

Not resolved by THIS review: m1/m2 original chain-Dc branches for any
k2/3/4, and the remaining m1/m2 k4 nonchain-Dc branches after valid old
guards. This is an evidence boundary, not a statement that every such
source is truly unpaid historically or evades all other known guards.
No m3 bank migration, universal weighted W assertion, source census,
net coverage increment or general D10 conclusion is certified.
