# 确定链前缀截断：NBU 尾引理与任意补块定理

日期：2026-10-18。状态：已证明，独立审查 PASS；审稿见 `audit-nbu-prefix-20261018/REVIEW.md`（相邻目录）。审查者另从负超几何 PMF 独立回核旧最紧实例，与本文尾和计算一致。范围仅为本轮辅助槽目标 T 与强协方差界，不讨论原全局猜想，不运行新偏序、filter 或参数族搜索。

## 1. 主结论

设

\[
U=C_a\sqcup V,\qquad C_a=(c_0<\cdots<c_{a-1}),\qquad |V|=b\ge1,
\]

其中两块间没有任何可比关系，而 \(V\) 内部偏序任意。取确定整数

\[
0\le k\le l\le a,
\]

定义两个上理想

\[
A=\{c_k,\ldots,c_{a-1}\}\cup V,\qquad
B=\{c_l,\ldots,c_{a-1}\}\cup V.
\]

空链后缀按空集解释，故 \(B\subseteq A\)，两者因 \(b\ge1\) 均非空。对均匀随机线性扩张的一基秩函数 \(f_U\)，定义零基首次命中槽

\[
R=\min_{x\in A}f_U(x)-1,\qquad
T=\min_{x\in B}f_U(x)-1,
\qquad r=\mathbb ER,\quad s=\mathbb ET.
\]

则

\[
\boxed{\operatorname{Cov}(R,T)\le r(r+1-p_k)\le r(r+1),}
\tag{P1}
\]

其中

\[
p_k=\frac{(a)_{\underline k}}{(a+b)_{\underline k}},\qquad p_0=1.
\]

当 \(k>0\) 时 \(r>0,p_k>0\)，所以强协方差目标严格成立，且余量至少为 \(rp_k>0\)。当 \(k=0\) 时 \(R=0\)，是等号退化。

逐扩张有 \(R\le T\)，因此 \(r\le s\) 且 \(\min(R,T)=R\)。若沿用原目标记

\[
N=\mathbb E[RT+\min(R,T)]=\mathbb E(RT)+r,
\]

则本结构族的 T 目标与强协方差目标严格等价：

\[
\boxed{
rs+r^2+2r-N
=r(r+1)-\operatorname{Cov}(R,T)\ge rp_k.
}
\tag{P2}
\]

本定理无 principal-filter 假设；\(V\) 可为任意有限偏序。所需确定链 \(C_a\) 与确定阈值 \(k,l\) 的限制见第 7 节。

## 2. 抽象充分引理：只需尾的次乘性

令 \(J\) 为任意非负整数值随机变量，设

\[
p_j=\Pr(J\ge j),\qquad p_0=1.
\]

假设对全部非负整数 \(u,v\) 满足明确的尾条件

\[
\boxed{p_{u+v}\le p_u p_v.}\tag{NBU}
\]

本文称这一条件为 NBU；术语不代替上述精确不等式。对任意有限整数 \(0\le k\le l\)，令

\[
R=J\wedge k,\qquad T=J\wedge l,\qquad
r=\sum_{i=1}^{k}p_i,\quad s=\sum_{j=1}^{l}p_j.
\]

则 (P1) 成立。因为两个变量均有界，此引理不需要 \(J\) 有有限一阶或二阶矩。

### 2.1 控制截断间协方差

以下先取 \(k\ge1\)；\(k=0\) 直接成立。逐点有

\[
R=\sum_{i=1}^{k}\mathbf1_{\{J\ge i\}}.
\]

对 \(1\le i\le k\le l\)，

\[
\mathbb E\big[T\mathbf1_{\{J\ge i\}}\big]
=i p_i+\sum_{j=i+1}^{l}p_j.
\]

记

\[
H_k=\sum_{i=1}^{k}i p_i,
\qquad
D_1=\sum_{i=1}^{k}\left(s p_i-\sum_{j=i+1}^{l}p_j\right).
\]

则这是精确恒等式：

\[
\boxed{\operatorname{Cov}(R,T)=H_k-D_1.}\tag{N1}
\]

NBU 保证 \(D_1\ge0\)，因为对每个 \(i\le k\)，

\[
\sum_{j=i+1}^{l}p_j
=\sum_{h=1}^{l-i}p_{i+h}
\le p_i\sum_{h=1}^{l-i}p_h
\le p_i s.
\]

这一步也覆盖 \(p_i=0\)：不需除以它。其概率含义是每个截断剩余寿命的条件均值不大于 \(s\)，但上式已经给出无需条件概率的完整论证。

### 2.2 三角尾和控制

同一尾条件给

\[
\begin{aligned}
H_k
&=\sum_{\substack{0\le u\le k-1,\ 1\le v\le k\\u+v\le k}}p_{u+v}\\
&\le\sum_{\substack{0\le u\le k-1,\ 1\le v\le k\\u+v\le k}}p_u p_v\\
&\le\left(\sum_{u=0}^{k-1}p_u\right)
\left(\sum_{v=1}^{k}p_v\right)
=r(1+r-p_k).
\end{aligned}
\tag{N2}
\]

首行的每个 \(p_m\) 恰出现 \(m\) 次，对应 \((u,v)=(0,m),(1,m-1),\ldots,(m-1,1)\)，所以没有偏移或重复计数问题。

结合 (N1)、(N2) 即得

\[
\operatorname{Cov}(R,T)\le H_k\le r(1+r-p_k)\le r(r+1).
\]

令

\[
D_2=r(1+r-p_k)-H_k\ge0,
\]

还得到精确非负余量分解

\[
\boxed{
r(r+1)-\operatorname{Cov}(R,T)
=rp_k+D_1+D_2.
}
\tag{N3}
\]

这是本证明直接可核对的结构证书；\(D_1,D_2\) 的非负性各自只使用 NBU 与非负求和。

## 3. 生存尾比值递减足以保证 NBU

若在 \(p_j>0\) 的范围内

\[
q_j=\frac{p_{j+1}}{p_j}
\]

随 \(j\) 不增，则对 \(p_u>0\) 且 \(p_{u+v}>0\) 的情形，

\[
\frac{p_{u+v}}{p_u}
=\prod_{h=0}^{v-1}q_{u+h}
\le\prod_{h=0}^{v-1}q_h=p_v.
\]

若涉及零尾，则 \(p_{u+v}=0\)，NBU 仍成立。因此离散 IFR / 生存尾 log-concave 条件足够，而本证明实际只要求更弱的 NBU。

此处没有假定任意偏序中任意首次命中槽都具有上述性质。第 5 节会对本定理的特定 \(J\) 直接证明尾比值递减。

## 4. 独立核对实际槽与 shuffle 描述

任一 \(U=C_a\sqcup V\) 线性扩张唯一由以下两项构成：

1. 一条 \(V\) 的内部线性扩张；
2. 一个含 \(a\) 个 C 和 \(b\) 个 V 的 shuffle 字。

链内部顺序已固定，每条 \(V\) 扩张都对应同样多的 \(\binom{a+b}{a}\) 个 shuffle 字。因此均匀 \(U\) 扩张可由独立均匀的内部 \(V\) 扩张和 shuffle 生成；特别是 shuffle 均匀，与 \(V\) 的内部关系无关。

令 \(J\) 为 shuffle 开头在首个 V 元素之前连续出现的 C 元素数。则 \(0\le J\le a\)。

- 若 \(J<k\)，第 \(J+1\) 个扩张元素是 V，首次命中 A 的槽为 \(J\)。
- 若 \(J\ge k\)，前 \(k\) 个元素恰为 \(c_0,\ldots,c_{k-1}\)，均不在 A；第 \(k+1\) 个元素要么是 \(c_k\)，要么是 V，均在 A。因此槽为 \(k\)。
- 当 \(k=a\) 时 A=V，且 \(J\le a\)，同样得到槽 \(J\)。

所以在全部端点均精确有

\[
\boxed{R=\min(J,k),\qquad T=\min(J,l).}\tag{P3}
\]

这里用一基秩减一，因而没有额外的 \(+1\) 或 \(-1\)。

## 5. 固定负超几何尾的核验

对 \(0\le j\le a\)，shuffle 的前 \(j\) 个字符全为 C 的概率是

\[
\boxed{
p_j=\Pr(J\ge j)
=\frac{(a)_{\underline j}}{(a+b)_{\underline j}}
=\frac{\binom{a+b-j}{a-j}}{\binom{a+b}{a}}.
}\tag{P4}
\]

对 \(j>a\) 置 \(p_j=0\)。因为 \(b\ge1\)，对 \(0\le j\le a\)，有

\[
q_j=\frac{p_{j+1}}{p_j}=\frac{a-j}{a+b-j},
\]

其中 \(q_a=0\)。对 \(0\le j<a\)，

\[
q_j-q_{j+1}
=\frac{b}{(a+b-j)(a+b-j-1)}>0.
\]

故这些尾比值严格递减，第 3 节给出 NBU。再由第 2 节引理与 (P3)，主定理 (P1)、(P2) 完成。

当 \(a=0\) 时只有 \(k=l=0\)，直接由零槽退化覆盖；不需要使用上述比值差式。

若允许 \(b=0\) 的空补块，则 \(J=a\) 确定。非空后缀的首次槽为其阈值；空 filter 沿原模型约定槽为 \(n=a\)。因此全部 \(0\le k\le l\le a\) 仍有 \(R=k,T=l\) 确定，协方差为 0，原强界与 T 界均成立。可令 \(p_j=1\) 对 \(0\le j\le a\)、之后为 0，NBU 引理也直接适用。这一退化不使用 \(q_a\) 的比值式。若不为 empty filter 定义槽，则只保留 filters 非空的阈值即可。

## 6. 精确矩式与既有最紧例回核

本节只是代入既有对象，不产生新对象或扩大搜索。

一般尾和给

\[
r=\sum_{i=1}^{k}p_i,
\qquad s=\sum_{j=1}^{l}p_j,
\]

且

\[
\mathbb E(RT)
=\sum_{i=1}^{k}(2i-1)p_i
+k\sum_{j=k+1}^{l}p_j,
\qquad
N=2\sum_{i=1}^{k}i p_i
+k\sum_{j=k+1}^{l}p_j.
\tag{P5}
\]

固定负超几何尾的均值还可写成

\[
\boxed{
r=\frac{a-(a-k)p_k}{b+1},\qquad
s=\frac{a-(a-l)p_l}{b+1}.
}\tag{P6}
\]

其望远镜依据是

\[
(b+1)p_i=(a-i+1)p_{i-1}-(a-i)p_i,
\]

分别求和到 \(k,l\) 即可。

已有 `slot-coverage-union-20261018/RESULT.md` 第 4 节的对象为

\[
U=C_{10}\sqcup(C_{10}\sqcup C_{180}),
\quad a=10,\ b=190,\ k=7,\ l=9.
\]

因此该既有剩余最紧代表整族已落在本定理中。按 (P4)、(P5) 的单例精确回算已经逐项得到旧记录

\[
r=\frac{996464317}{19032468455},\qquad
s=\frac{6154163621889}{117544525178080},\qquad
N=\frac{234277819681}{2137173185056},
\]

以及相同的 T / Cov 绝对余量

\[
\frac{6550878543122831207}{11414094221988575803400}>0.
\]

精确回核脚本与结果见本目录 `verify_existing_case.py` 和 `existing_case.json`；它们只使用这个已经存在的四参数实例与上面的有限尾和，不枚举偏序或线性扩张。

## 7. 适用边界与停止结论

已证的无界结构族是

\[
\boxed{U=C_a\sqcup V,\quad
A=(C_a\text{ 从 }k\text{ 开始的后缀})\cup V,\quad
B=(C_a\text{ 从 }l\text{ 开始的后缀})\cup V,\quad 0\le k\le l\le a,}
\]

其中 \(V\) 内部偏序任意，\(b\ge1\)。抽象层面，所有满足 NBU 尾条件的非负整数随机变量的两个确定截断，也都满足强协方差界。

链假设的作用是让阈值 \(k,l\) 为确定常数。若将 \(C_a\) 换为任意 \(W\)，并用 \(W\) 中嵌套 ideals 的补集构造 filters，则首次越出两个 ideals 在 \(W\) 内部扩张中的位置一般成为随机阈值 \(K,L\)。即使条件于 \(K,L\) 可以应用本引理，全协方差公式仍包含

\[
\operatorname{Cov}(\mathbb E[R\mid K,L],\mathbb E[T\mid K,L]),
\]

而右侧条件界的平均也不自动等于 \((\mathbb ER)(1+\mathbb ER)\)。因此本证明不声称任意 \(W\) 与随机阈值版本，也不声称任意偏序首次槽的尾 NBU。

本任务已得到一般结构定理与可核查证明，没有遗留代数卡点；未研究原猜想全局，未运行新的大搜索。

## 附录 A. 随机阈值混合确实不保持结论：纯抽象控制

下面仅否定“把确定阈值直接换为独立随机阈值”的抽象推广，**没有声称它来自实际偏序或原 filters，更不是原猜想反例**。

令

\[
\Pr(J=0,1,2,3)=\left(\tfrac12,\tfrac14,\tfrac18,\tfrac18\right).
\]

其尾满足 \(p_j=2^{-j}\) 对 \(0\le j\le3\)，之后为 0，所以当 \(u+v\le3\) 时 NBU 取等号，之后左侧为 0，仍满足 NBU。令 \(K\) 与 \(J\) 独立，

\[
\Pr(K=0)=\frac9{10},\qquad \Pr(K=3)=\frac1{10},
\qquad R=J\wedge K,\quad T=J.
\]

条件于每个 K 都是本引理的确定截断情况，但

\[
\mathbb EJ=\frac78,\qquad
\operatorname{Var}J=\frac{71}{64},\qquad
r=\mathbb ER=\frac7{80},
\]

\[
\operatorname{Cov}(R,T)=\frac1{10}\operatorname{Var}J=\frac{71}{640}
>r(r+1)=\frac{609}{6400},
\]

超出量恰为 \(101/6400\)。这些数值已独立用精确有理数核对，见 `random_cap_control.json`；该控制不是对参数空间的搜索。

因此本定理的确定阈值条件有实际数学内容；条件应用后直接平均不足以证明随机阈值版本。
