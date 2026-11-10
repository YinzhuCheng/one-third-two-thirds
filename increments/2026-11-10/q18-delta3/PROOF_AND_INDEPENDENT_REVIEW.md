# 原首 O 前缀 cap 与精确通道：解析证明及研究内独审

2026-11-10。**PASS WITH EXACT SCOPE**。这是最终审校稿的公开数学副本；完整通道条件见 [CHANNEL_SCOPE.md](CHANNEL_SCOPE.md)。本文先按原 nohole 版本证明，随后在第8节逐项核准去掉该假设。因此最终新结论覆盖 m1k2 的整个原 Dc 链域、全部真实 O。

e(R) 表示偏序 R 的线性扩张数，K_R(x<v) 表示其中同一物理事件 x 在 v 前的扩张数。所有概率均属于所指定的原完整扩张律；条件对象只用于严格的整数分区。

本审查未参与该前缀证明的推导；独立从 gap 和消去 l，核对多项式、边界、原度、真实 suffix 因子及旧 bank/bridge 接口。最终论证不依赖1946组探索表，也不要求重跑 source census 或 LE DP/LP。这里是研究内独审，不是外部同行评审或形式化认证。

公开整理仅移除保存/执行过程说明、规范引用路径及加入导航；数学内容与接受范围未变。原审校稿 SHA256 为 76345d78f97181884239cb6c40d5044ed01a1147a58402602576b34d5ab8505b。来源公开边界见 [PUBLICATION_SCOPE.md](PUBLICATION_SCOPE.md)。

## 1. Exact theorem and original contract

Retain the complete finite ORIGINAL degree-ten seed/private/actual-Q18/
selected-fork occupied-C one-saturated child-u-zero contract, q=r_v=0,
delta_v=3,m=1,k=2. S={a,b,c,u,v} is the induced ideal with a<u,a<v,b<c;
P minus the inclusive a-upset is {b,c}. O is the actual common strict
upset of c,u,v. Dc is the original chain x<d<e, with D(x)={a,b,c}.
The main frozen author scope has x<Cv ALL. A has five labels, V two,
Cv two, and Y={y}. All original internal, b, cross and outside ports
and arbitrary finite actual O remain. Saturation gives Dc<y<O.

For each actual first-O prefix I, put M_I=2e(I)-3K_I(x<v). Then
 M_I >=16 e(I[V union A]) e(I[Cv]) >0.
Consequently M_P=2e(P)-3K_P(x<v)>0 for the entire original P, including
arbitrary interleaved O. Same-P bank and bridge imply some original pair
among ab,bu,cv,uv,uy,xv is closed-balanced. This is not merely a separated
Q-before-O reserve. B,C below rename only the actual Cv word, never x,v.

## 2. True words, complete ports and root kernel

I is the original ideal before the first actual O label; it contains
S5+Dc3+y. Also permit I=Q as an end-sentinel when O is empty. Put
a=|I intersect A|, r=|I intersect V|, c0=|I intersect Cv|, with a<=5,
r<=2,c0<=2. Fix an actual gamma on retained V union A and an actual
restriction word tau on retained Cv. Remove five markers Z={a,b,c,x,v}
and d,e,y. The remaining word is sigma=u+shuffle(gamma,tau), of length
n=1+a+r+c0, preserving all original V->Cv ports. A and Cv are incomparable.
A retained Cv cannot have a missing original V predecessor because I is
an ideal. Thus the canonical word u gamma tau is always legal.

Let p1,p2 be the first retained Cv successors of d,e in sigma, or n+1
if absent. Real insertion words are uniquely parametrized by
 0<=i<p1, i<=j<p2, j<=l<=n.
Equal gaps use the forced d<e<y order. If R is the first A rank in sigma
(or n+1 if A absent), the exact v deadline is
 t=min(l+3,R+1[i<R]+1[j<R]).
The first two insertion layers have h=q=ell=1 and 2, respectively, with
root scores g(t)=12-3t and f(t)=58-9t. The original b ports are not erased.
For i>=2, u is first and d has rank>=3. A c-successor at rank2 would be
Cv; the two original V labels and d,e must then all be incomparable to
it, on top of forced v,A5,y=7, contradicting degree ten. Missing V labels
are still original degree witnesses; ideality prevents their being hidden
predecessors. Hence q>=3,h>=2,ell>=q, and original v degree bounds t<=8.
The old pure scalar bound permits ell>=q and gives
 p0(t)=min(40,156-18t): 40 for t<=6,30 for t=7,12 for t=8.
Actual late t>=2; no t=1 application is made. No induced prefix, helper
completion or suffix is assumed NB or a new full-Q18 source.

Kernel dependency: sources/ROOT_INSERTION_KERNEL.md,
SHA256 112a23a2872920aaa47d43ad9836691535086cd1d1860139dae0801dc1e693be.
Pure scalar dependency only (not m2 geometry):
sources/SCALAR_CAP_REVIEW.md,
SHA256 c20652368e49a268bdd8f00654f93f6bad5cbf8d70c2bcf74628927c7057c60e.

## 3. No retained Cv: bound 16

Here n<=8 and caps p1=p2=n+1. If A is present R<=4; if absent n<=3.
Thus t<=6. Layers i=0,i=1,i>=2 have lower bounds -6,4,40 and counts
C(n+2,2),C(n+1,2),C(n+1,3). For n>=2 their total is at least
 (n+1)[(20/3)n(n-1)-n-6],
which equals16 at n=2 and increases thereafter. For n=1 the four actual
scores are3,0,0,22, giving25. Each gamma therefore contributes at least16.

## 4. One retained Cv: bound 32

Write B rank p,n=2+a+r<=9. The cap types are BB(p,p),BE(p,n+1),
EE(n+1,n+1). For EE take the ORIGINAL word subfamily d<B and rerun BE;
the complement B<d is positive late. This is not a helper-source transfer.
For A absent and n=2,3,4, BB rows (p increasing) are
 [32]; [24,112]; [1,85,189],
and BE rows are [42]; [30,150]; [-35,145,235]. Canonical p=n is always
legal, so each gamma group is at least32.

For A present let s=first-A gamma index, 1<=s<=3. If B is before A,
R=s+2,p<=s+1; otherwise R=s+1,p>=s+2. Use late b=40 for R<=4 and
b=30 for R=5. Independently eliminating l gives
 C0=(3/2)(R-1)(4-R)+(n-R+2)(6-3R),
 Cj=34(R-j)-6[R(R-1)-j(j-1)]+(n-R+1)(46-12R), 1<=j<R,
 Cj=(n+1-j)(58-12R), j>=R.
The lower sum is
 L=C0+sum(j=1..p2-1)Cj
   +b sum(j=2..p2-1)(n+1-j)max(0,min(j,p1-1)-1).
Increasing p1 only adds positive late terms. BB diagonal difference for
p>=R is (n+1-p)[58-12R+b(p-1)]>0. The after-A minima for s=1,2,3 are
96n-71,159n-236,238n-524. The before-A rows are respectively
 (7n+18); (48-8n,30n+22); (93-23n,113-7n,39n+33).
Credit canonical once and charge every possible negative once: for s2
net>=151n-236; for s3 net>=215n-524. Both exceed32 in their ranges.

For BE the late sum is b[C(n+1,3)-C(n-p+3,3)]. The after-A minima are
37n^2-15n+3,51n^2-96n+70,65n^2-217n+256. Before-A rows are
11n^2-16n+30;
5n^2-37n+96,25n^2-57n+96;
-n^2-58n+213,14n^2-73n+213,29n^2-118n+243.
Only the first s3 entry may be negative. Canonical pays it with net
>=64n^2-275n+469>=694 for n>=5. Hence c0=1 gives32 per gamma/tau.

## 5. Two retained Cv: cap exhaustion and positive-A cases

Now n=3+a+r<=10. Every original Dc endpoint has nine forced incomparable
neighbors u,v,A5,V2; therefore e has at least one original Cv successor.
d inherits it. Relative to the ACTUAL Cv word B then C, the first-port
types are exactly BB,BC,CC, whether Cv was a chain or antichain.
CC restricts to actual d<B words for the BC argument; remaining B<d
words are positive late. All bounds below use p0(t) pointwise, NOT the
c1 constant30 at R5. For R<=4 late p0=40. The BC p2>=R difference is
(n+1-p2)[58-12R+40(p1-2)]; BB diagonal difference is
(n+1-p)[58-12R+40(p-1)].

For A present let s=first-A gamma index and k0=number of Cv before A,
so R=s+1+k0. Canonical u gamma BC is always legal.
s1,n4..10: the sole potential negative k0=2 word has BB48-8n>=-32
or BC62-10n>=-38. Canonical values are
 BB=(20n^3+51n^2-365n+303)/3>=313,
 BC=(20n^3+51n^2-125n-213)/3>=461.
All other cells are nonnegative; nets>=281/423.

s2,n5..10: k0=2 has BB first two93-23n>=-137, third133-7n>=63;
BC first two143-37n>=-227,183-51n>=-327, third9n+123>=168.
k0=1,R4 BB pB2 has at most6 cells each>=-32, while pB3 is positive;
BC minimum Lambda(4,2,5)=36-2n>=16. k0=0 is positive. Canonical:
 BB=(20n^3+33n^2-428n+492)/3>=559,
 BC=(20n^3+33n^2-188n-96)/3>=763.
Thus nets>=559-274-192=93 and763-227-327=209.

s3 forces r=2,n=a+5. For a1,n6 the unique k0=0 cell is BB904,BC1164.
The k0=2 BB rows have pB2 three entries -75,pB3 two entries+1,pB4 one
entry+121; BC six entries are -133,-201,-267,+27,+15,+163.
The k0=1 rows are BB(-45,+91,+307),BC(-169,+301,+601).
Nets are at least634 and394. For a>=2,n7..10 preserve three positive
k0=0 cells (pB,pC)=(5,6),(5,7),(6,7). Both V precede first A, hence
all three satisfy every original V port. BB each>=1142 gives3426,
against debts<=1190+685, net>=1551. BC values are368n-1044,
498n-1694,578n-2054, total>=5316; debts<=2284+2325 yield net>=707.

For reproducible analytic boundaries, the directly expanded affine rows are:
R6 BB p2/3/4:153-38n,313-52n,445-54n.
R6 BC (2,3),(2,4),(2,5),(3,4),(3,5),(4,5):
251-64n,339-90n,429-116n,423-66n,495-80n,499-56n.
R5 BB p2/3/4:93-23n,133-7n,39n+73.
R5 BC(3,6)=63n-77,(4,6)=163n-377,(2,6)=233-67n,
(2,n)=-n^2-58n+215. R4 BB(5,5)=238n-524.
R5 p2>=R increment=(n+1-p2)[-2+40(p1-2)].
These formulas result from the displayed finite sums, with p0 split at
6/7/8; the endpoint and monotonicity comparisons are not interpolation
or a numerical table standing in for proof.

## 6. Two Cv with no A: ports cannot delete arbitrary positive rows

r0: unique uBC has BB24,BC32.
r1 words BCV,BVC,VBC have BB(1,1,105),BC(-5,-21,159).
Canonical is legal, yielding>=105/133.
r2 words BCVV,BVCV,BVVC,VBCV,VBVC,VVBC have
 BB(-37,-37,-37,53,53,175),
 BC(-69,-111,-151,93,95,219).
BB canonical175 alone pays all three negative rows, leaving64.
For BC the fixed actual V word induces effective prefix requirements
reqB<=reqC. If reqB>=1 all B-first negative words are removed and
canonical219 remains. If reqB=0,reqC=0/1/2, the ACTUAL allowed sums
are respectively76,145,163: in the latter cases use93+95+219-111-151
or95+219-151. These are genuine allowed subsets determined by original
V ports, not arbitrary deletions or chosen mixing weights. Antichain Cv
causes no issue because B,C denote its actual restriction order.
Therefore c0=2 gives at least24 per gamma/tau.

## 7. No double debt, true first-O factor and original bridge

Different gamma,tau,sigma,i,j,l index disjoint actual words. Each possible
negative cell is charged once; only guaranteed actual canonical or named
positive cells are credited. Optional V ports can delete other cells but
cannot delete the guaranteed credits, and deleting charged negative cells
only improves the estimate. Weights are actual integer root counts.
The uniform result is M_I>=16e(I[V union A])e(I[Cv])>0.

For the first actual O label o, its preceding set I is an ideal and
contains all five markers; D(o) is contained in I. With
 T(I,o)=e(P-(I union {o})),
all ideal extensions concatenate with o and every real suffix extension.
Thus N_(I,o)=e(I)T and K_(I,o)=K_I(x<v)T, with the SAME physical event.
The disjoint first-O partition gives M_P=sum_(I,o)T(I,o)M_I>0.
For O empty apply the same prefix lemma at I=Q. The old1999 separated
reserve is not used to pay arbitrary outside interleavings.

The same-original chain bank binds to
sources/CHAIN_BANK_REVIEW.md,
SHA256 8fc9ee758a4eb0f91500b3c0310ed861b95ca10c564d02c5ee5f8759721cfd89.
It gives Bx=Kvc+Kxv+Kba-N>0. The bridge binds to
sources/LOWER_BRIDGE_REVIEW.md,
SHA256 cc776ee3f733ee597592bbb9c21e50481b7ead5066490725c0b027518ca61797.
Its accepted conclusion1 gives Kxv>N/3 if ab,bu,cv,uv,uy all avoid
the CLOSED interval. New Kxv<2N/3 then proves the six-pair result.
The old frozen k4 application is not retroactively claimed to have paid k2.

## 8. Separately accepted optional weakening: drop nohole

PASS as a separate scope extension. In early layers d rank1/2 already
forces h=q=ell1/2 regardless of x/Cv holes. Late uses only ell>=q,
which the pure scalar bound permits. Original degree exclusion, e's Cv
successor, first-port exhaustion, y protection, ideality and first-O
factor do not require x<Cv ALL. Thus the new prefix/full-cap/six-pair
proof covers original m1k2 Dc-chain sources with any x-hole mask.
For O empty in this widened scope use the NEW lemma at I=Q, not the
old nohole1999 theorem. This optional extension is not necessary to
close the old m1 union; old hole-slot coverage remains old coverage.

## 9. Scope-only union: whole precise child-u-zero delta3 channel

The following final independent reports were actually read and their
SHA256 bindings checked. This is an interface/quantifier union audit,
not a recursive reproof of every ancestor or replay of finite certificates.

m1: sources/M1_PREVIOUS_UNION_REVIEW.md,
ec13f366af57f2ff333749528decff1512cffab42acb400c428b170c9c3cdb5f.
It covers all k3/k4 and k2 except original Dc chain/nohole. Section5
proves Cv cannot precede chain bottom x, so hole/nohole omits no third
relation. The new MAIN nohole result fills exactly its only remaining
branch, without needing the optional extension above.

m2: sources/M2_COMPLETE_REVIEW.md,
279397a7cebaa5cbd06f59a6bf07871dd22678c236e3174803c65016f3ff3ecc.
m3: sources/M3_COMPLETE_REVIEW.md,
b4fc21bdcab8e3ba5d648d7e581c5979873047db8874da0831d94199114c5b26.
Both are final accepted original all-k2/3/4 results, with all permitted
Dc orders, ports and finite actual O including empty. Neither retains
an unresolved dominant-existence or input-verdict condition.

Population: sources/POPULATION_REVIEW.md,
a55d9a87eb96526f5e8764e5513b32fe082219d4f456a8e3d571b9c4d96cd6b3.
It gives d=4-m,A=6-m,V=m+3-k,Cv=k,Y=m, with the exhaustive ranges
m1..4,k2..4. Population deficits are not full-degree slack.

m4: sources/M4_ACCEPTED25_REVIEW.md,
8d6f680c6515ff063570b940fd41dd82a9006c7a789c99caba009e3286efce68,
section1 accepts old25 BANK3 on child-axis s_c<=s_other_child+1.
Here j=u,s=(2,4,k),r=(0,7-k,0), and2<=k+1 for every k2/3/4.
Thus all current m4 sources are included, not excluded ID15 or ID21.
Its inherited original-law/exterior lift includes arbitrary actual O.

Conclusion: SOME original closed-balanced pair exists on the WHOLE
PRECISE original degree-ten seed/private/actual-Q18/selected-fork,
one-saturated occupied-C, unique population zero at child u, q=r_v=0,
delta_v3 channel. This is not all delta3, c-zero, general Q18, B1/B2 or
D10. No unified six-pair list is asserted across old-guard alternatives.
No net-new population or source count is claimed. m1/m2/m3 retain their
analytic accepted proof chains; m4 remains inherited finite-certificate
proof grade with original exterior lift, so the union is NOT all purely
analytic. Old coverage is not credited again.

