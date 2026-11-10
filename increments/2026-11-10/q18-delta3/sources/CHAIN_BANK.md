# 数学源稿副本｜CHAIN_BANK.md

原研究稿标签：q18-delta3-m1-chain-bank-analysis-20261110 :: PROOF.md。

原稿 SHA256：b33f3b003f54e00c704aa06a24bf239fe6b6795f14728aa1659c6c4eb85ab8c3。原数学正文与原审查状态保留；仅公开路径规范化。

原日期与原接受范围按历史保留；较早停止线不倒改，新精确通道结论以主证明为准。原稿来源标签若未在本增量提供，标为 upstream-source，不是本仓库已迁入的文件。

---

# Original delta3 m1 chain-Dc unit bank: nested physical caps

2026-11-10. AUTHOR CANDIDATE, independent review required. No numerical
program, enumeration, DP/LP, external write or ledger increment. This
is an original raw-bank theorem, not by itself balance or a directed cap.

## 1. Exact original scope

Retain the complete original degree-ten seed/private/actual-Q18/selected-
fork one-saturated child-u-zero occupied-C channel: q=r_v0, delta_v3,
delta_c>0, all original b/internal/cross/O ports, finite actual O including
empty. Set m=|Y|1. Thus Dc3,A5,r+k4,k=2/3/4. Here require the ORIGINAL
Dc order to be a chain x<D1<D2, with its fixed physical bottom x and
full D_P(x)={a,b,c}. No chain in A,Cv,V or O is imposed. Y={y} is
saturated, so Dc<y<O. The actual x-hole set H in Cv is allowed, including
a hole at k2; no delta2 hole-impossibility conclusion is imported.

Claim: in THIS original P,

 Bx=Kba-K(c<v<x)=Kvc+Kxv+Kba-e(P)>0.                 (1)

The exact bank/root law is the already accepted joint-pivot kernel in
ROOT_INSERTION_KERNEL.md section4. Only its
algebra and physical bijection are inherited, not a delta2/m2/m3 bank.

## 2. The nested actual-port insertion weights

Fix a COMPLETE actual word sigma of
R=P minus{a,b,c,x,v,D1,D2,y}; its ten non-O labels are u,V,A,Cv.
It starts u, since u precedes every other retained label. Keep all O
labels and their literal order. Let L be the number before the first O,
or L=10 if O is empty; L<=10. Write P0,S,T for the first Cv, x-successor
Cv and A ranks in this prefix, infinity if absent.

Each Dj is incomparable with u,V,A; its only retained successors are
its physical Cv ports and all O, and it has no retained predecessor.
Define pj as the first Dj-port Cv rank, clipped also by the first-O
rank L+1; if no such prefix port exists, pj=L+1. The chain implies

 2<=p1<=p2<=L+1,  pj>=min(S,L+1).                  (2)

The lower bound2 is used only when such a sigma exists (then L>=1,
because u precedes O); no assertion pj>=infinity is made. A D2 Cv
port is a D1 port, and every D1 port is an x successor. These are
original transitive implications, not completed cross edges.

Delete D1,D2,y from an actual residual word. Reinsert D1 after i sigma
letters, D2 after j, and y after l. Legality is EXACTLY

 0<=i<p1,  i<=j<p2,  j<=l<=L.

Equal gaps preserve the prescribed D1<D2<y order. Thus the TRUE count
for each legal i is

 wi=sum_{j=i}^{p2-1}(L-j+1)
   =binom(L-i+2,2)-binom(L-p2+2,2).                (3)

Every physical D1/D2 upper cap, y-before-all-O condition and complete
outside suffix is retained. Deletion recovers unique sigma and gaps.
There is no assumption of uniform physical gap probability.

## 3. Safe auxiliary deadline and the exact low-support library

For each such original residual word, the root deadlines satisfy
q=min(P0,i+1),ell=min(S,i+1),h<=q. D2 is after D1 and therefore cannot
be an earlier b,c or x successor. Define t'=min(T,i+1). If A is before
D1, actual t=T=t'; if D1 is before A, actual t is later than i+1>=ell.
The joint bank kernel H increases with t once t>=ell. Raising h to q
only increases the debit. Consequently every actual D2/y placement has

 H(actual)>=Fi=H(q,q,ell,t').                       (4)

No D1-v comparison has been added. Actual b ports remain in h.

The ORIGINAL x budget is
deg(x)=2+r+5+|H|=11-k+|H|<=10,
so r+|H|<=3. It implies min(q,t')<=r+2<=4 and
min(ell,t')<=r+|H|+2<=5. These hold for clipped ranks; they do not
claim raw S or T finite. The same ten-label count gives ell<=10.

Use ONLY the scalar library independently derived in
upstream-source(q18-delta2-m2-k4-chainD-one-hole-early-independent-20261110 :: GENERAL_M2_CHAIN_DC_REVIEW.md) sections2--3, not that source's physical
theorem. The library takes precisely u first,L<=10 and these two clipped
support bounds. It says: either every Fi is nonnegative (F0=2), or its
negative entries are controlled by ONE of the following eight complete
lower sequences di, with a single positive-to-negative transition:

 (P0,T)=(2,3),(2,4),(3,4),(2,5),(3,5),(4,5),(5,4),(6,4).

After first Cv/A exposure the affine forms are respectively
22-4ell,42-7ell,54-10ell,68-10ell,95-16ell,114-20ell,
39-6ell,19-2ell. Earlier entries are the explicitly clipped positive
ones in that review. Its ell<=min(i+1,10) lower sequences have true
free-weight sums, at L10,

 796,1129,547,1678,721,173,1503,2003.

The review proves each free-weight sum is strictly positive for ALL
L<=10 by its last-positive normalized weight argument. In particular,
for wi^free=binom(L-i+2,2),

 sum_{i=0}^L wi^free di>0,

di<=Fi, d0=2, and di is nonnegative up to its last positive index and
nonpositive afterwards. Zeros at a transition are harmless. No new
source/word enumeration or delta2 population assumption is used here.

## 4. Decreasing port-ratio preserves a one-sign weighted payment

Extend actual coefficients by zero for i>=p1. Relative to free weights,
write

 beta_i=1[i<p1]*(1-C/wi^free), C=binom(L-p2+2,2).

For i<p1<=p2, beta_i is positive. Since wi^free decreases with i,
beta_i is nonincreasing, including the zero tail; beta0>0. If all Fi
are nonnegative, i0 alone is strictly positive and proves the group.

Otherwise choose its controlling sequence di from section3 and let m
be the last positive index. If beta_m>0, monotonicity gives beta_i>=
beta_m on the nonnegative side and beta_i<=beta_m on the nonpositive
side. Therefore

 sum_i beta_i wi^free Fi
 >=sum_i beta_i wi^free di
 >=beta_m sum_i wi^free di>0.

If beta_m=0, all i>=m have zero actual weight; the retained early
di are nonnegative and i0 contributes beta0*wi^free_0*2>0. Thus the
same strict conclusion holds. This is a direct weighted sign argument,
not an assertion that removing any positive tail improves a bank.

This simultaneously handles BOTH original D caps. In particular the
D2 cap subtracts a constant from each free coefficient before p2;
one must not pretend it is the free Y2 law. No cap is selected afresh
for different members of sigma, and no partner word/capacity is reused.

## 5. Original assembly and stopping line

For EACH complete actual sigma, its full D1/D2/y residual-word group
has strictly positive original bank score by(3)--(4). The exact root
lift and deletion partition all original P extensions; the physical
event x<v and the same N=e(P) are never changed. Summing proves(1)
for arbitrary actual finite O. Empty O is the same argument with L10.
No first-O row is endowed with original NB, and no outside tail mass is
equated between different completions. All counts are true integers;
positivity needs no claimed common optimized constant.

This candidate does not prove a cap for x<v, a balanced pair by itself,
a nonchain Dc bank, m1 completeness, or a universal weighted W sign.
The k2 minimal-hole branch remains allowed under delta3 and is included
only through its actual shared-budget low-support ranks.
