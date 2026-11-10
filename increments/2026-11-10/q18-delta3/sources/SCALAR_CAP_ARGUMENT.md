# 数学源稿副本｜SCALAR_CAP_ARGUMENT.md

原研究稿标签：q18-delta3-m2-k2-chain-dc-cap-analysis-20261110 :: PROOF.md。

原稿 SHA256：559f249223bc0029e2638765c9cc94b8cef6bf6cc5154abc6c3e497f23d0d7bc。仅摘录原稿第2节纯参数根核推导；不迁移 m2 几何或付款结论。

原日期与原接受范围按历史保留；较早停止线不倒改，新精确通道结论以主证明为准。原稿来源标签若未在本增量提供，标为 upstream-source，不是本仓库已迁入的文件。

---

## 2. Exact original root cap law and two purely algebraic bounds

For each ACTUAL pi in LE(P-{a,b,c,x,v}), the accepted original joint
root/x/v insertion bijection gives complete counts N_pi,K_pi and
M_pi=2N_pi-3K_pi. First original b,c,x,v-successor ranks are
h<=q<=ell and t. Insert v at r=1,...,t, with

 H_r=h+1[r<=h],Q_r=q+1[r<=q],L_r=ell+1[r<=ell],
 w_r(s)=G(min(Q_r,s),H_r),1<=s<=L_r,
 G(s,h)=sum_{j=0}^{min(s,h)-1}(s-j)+s+1,
 N_r=sum_s w_r(s),K_r=sum_{s<=min(r,L_r)}w_r(s).

Then M_pi=sum_r(2N_r-3K_r). All original b ports and both marker
orders in shared old gaps are included. No normalized rank law is used.
Full deg_P(v)=3+|Dc|+|V|+|Cv|=10; the three DELETED incomparable
labels b,c,x plus the first t-1 retained incomparable labels imply
actual t<=8. This is not a helper degree assumption.

The following exact-kernel consequences will be used:

 h=q=ell1: M=g(t)=12-3t;
 2<=h<=q<=ell,2<=t<=8: M>=f(t)=58-9t;
 2<=h<=q<=ell,q>=3,1<=t<=8: M>=12.                    (2)

Here the first line is exact. The other two are algebraic bounds,
not the m3 Y3 payment theorem. For completeness their derivation is:

* The already checked cap-kernel difference increasing e=ell by1 is
  2sum_{r<=min(t,e)}G(Q_r,H_r)+1[t>=e+1]G(q,h)
  -(t-e-1)_+G(q,h), at least(3e+2-t)G(q,h)>=0 when e>=q>=2,t<=8.
  Thus ell=q is a lower endpoint, with no original completion.
* For t>q, the exact diagonal formula is
  M(h,q,q,t)=sum_{s=1}^q(3s-t-3)G(s,h)+2qG(q+1,h)
  +h(q+1-h)(q+2-h). Its h->h+1 increment is
  sum_{j=1}^{q-h}(3h+3j-t+3)j>=0. At h2 it equals
  3q(q+1)(2q+2-t)/2+2q(q-1). For q2 this is58-9t; for q>=3 it is
  at least156-18t>=12, and exceeds58-9t for t<=8.
* If t<=q, the nondecreasing x-slot weights and nonincreasing actual
  N_r give K<=N/2 using weighted mean r<=(t+1)/2. At t2 the direct
  first-two-row bound is M>=40. For3<=t<=q, each row N_r>=30, so
  M>=N/2>=15t>=45. These imply the f bound, and >=12 for q>=3.
  At t1,q>=3 the first-row weights include3,6,10,14, while K1=3;
  hence M>=2*33-9=57>=12. These cover every case in(2).

The root bijection is inherited from
ROOT_INSERTION_KERNEL.md §4 eq(6); the
ell/h and weighted-row facts were previously checked at their pure
parameter interfaces in the delta3m3 cap audit. No m3 chain geometry
or source bank is borrowed.

