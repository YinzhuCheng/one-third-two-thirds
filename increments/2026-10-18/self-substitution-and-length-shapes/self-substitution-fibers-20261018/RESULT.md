# 代换 $P[Q]$ 的线性扩张纤维与 cross-rank 障碍

## 0. 范围、记号与结论

本文只分析给定代换操作，不尝试证明原 $1/3$–$2/3$ 猜想。$P,Q$ 均为有限非空偏序，$n=|P|,m=|Q|$。元素写作 $(p,a)\in P\times Q$，代换关系为

\[
(p,a)<(r,b)\quad\Longleftrightarrow\quad
[p<_{P}r]\ \text{或}\ [p=r\ \text{且}\ a<_{Q}b].
\]

记 $e(S)=|\operatorname{LE}(S)|$，
\[
\pi_S(x,y)=\Pr_{L\sim\operatorname{UnifLE}(S)}[x\text{ 先于 }y],\qquad
\beta(t)=\min(t,1-t),
\]
\[
\delta(S)=\max_{x\parallel_S y}\beta(\pi_S(x,y)),
\]
无不可比对时令最大值为 $0$。

**精确主结果。** 设 $R=P[C_m]$，则
\[
\operatorname{LE}(P[Q])\simeq
\operatorname{LE}(R)\times\operatorname{LE}(Q)^n,
\qquad
 e(P[Q])=e(R)e(Q)^n.
\]
均匀线性扩张在此双射下为独立乘积的均匀分布。若
\[
\mu^Q_a(i)=\Pr[\operatorname{rank}_{L_Q}(a)=i],\quad
 K^{p,r}_{P,m}(i,j)=\Pr_{L_R}[(p,i)\text{ 先于 }(r,j)],
\]
则不可比块 $p\parallel_P r$ 间任一实际元素对满足
\[
\boxed{\ \pi_{P[Q]}((p,a),(r,b))
   =\sum_{i=1}^m\sum_{j=1}^m
      \mu^Q_a(i)\mu^Q_b(j)K^{p,r}_{P,m}(i,j).\ }
\tag{F}
\]
标签词的 law 和核 (K) 只依赖 $P,m$，不依赖 $Q$ 的内部结构；实际 cross 概率还依赖 $Q$ 的元素 rank 分布。

若 $\Delta(S)$ 是最大不可比度，则
\[
\boxed{|P[Q]|=nm,\qquad\Delta(P[Q])=m\Delta(P)+\Delta(Q).}\tag{D}
\]
自代换因此确实放大最大不可比度：
\[
|P[P]|=n^2,\qquad\Delta(P[P])=(n+1)\Delta(P).
\]
当 $n>1$ 时，归一化量 $\Delta/(n-1)$ 恰好不变。

## 1. 等长标签词的精确双射

定义 $W(P,m)$ 为长度 $nm$ 的词集合：

1. 字母表是 $P$，每个标签 $p$ 恰出现 $m$ 次；
2. 若 $p<_{P}r$，则每次 $p$ 都在每次 $r$ 之前。

给定 $w\in W(P,m)$，把第 $i$ 次出现的 $p$ 改写为 $(p,i)$。得到 $P[C_m]$ 的线性扩张：每块内部 $1<\cdots<m$，可比块间的全部约束也满足。反向去掉第二坐标便恢复原词。因此
\[
W(P,m)\simeq\operatorname{LE}(P[C_m]).
\tag{W}
\]

现在给每个 $p\in P$ 独立选择一个内部扩张
\[
L_p=(q_{p,1},\ldots,q_{p,m})\in\operatorname{LE}(Q).
\]
在词 $w$ 的第 $i$ 次 $p$ 处填入 $(p,q_{p,i})$。块内顺序来自 $L_p$，块间约束来自 $w$，因此得到 $P[Q]$ 的线性扩张。

反过来，任一 $P[Q]$ 线性扩张投影到第一坐标后给出唯一 $w\in W(P,m)$；限制到每个块后给出唯一 $L_p\in\operatorname{LE}(Q)$。两个构造互逆，证明纤维双射。

特别地，每个标签词的纤维大小都是 $e(Q)^n$。所以均匀 $P[Q]$ 扩张的标签词在 $W(P,m)$ 上均匀；给定标签词，$L_p$ 是相互独立、均匀的内部扩张；它们还与标签词独立。并不存在额外的、依赖 $w$ 或 $Q$ 的纤维权重。

## 2. 每一种元素对的实际概率

### 2.1 同块：原内部 pair 完整保留

对于 $a\ne b$，
\[
\pi_{P[Q]}((p,a),(p,b))=\pi_Q(a,b).
\tag{I}
\]
所以内部不可比 pair 的 balance 完整保留，且 $\delta(P[Q])\ge\delta(Q)$。

### 2.2 原本可比的两个外块

若 $p<_{P}r$，则对所有 $a,b$ 概率均为 $1$；若 $r<_{P}p$，则概率均为 $0$。这些 pair 不成为新增不可比 pair。

### 2.3 原本不可比的两个外块

若 $p\parallel_P r$，两个块之间每个 $(p,a),(r,b)$ 都不可比。设 $I,J$ 分别为 $a,b$ 在各自内部扩张中的 rank。由乘积 law，$I,J$ 独立，分布为 $\mu_a^Q,\mu_b^Q$，且均与均匀标签词独立。给定 $I=i,J=j$，目标事件就是第 $i$ 个 $p$ 先于第 $j$ 个 $r$。全概率公式即给出 (F)。

核也有纯计数形式。令 $R=P[C_m]$，则
\[
K^{p,r}_{P,m}(i,j)
 =\frac{e\!\left(R+\{(p,i)<(r,j)\}\right)}{e(R)}.
\tag{K}
\]
这里加关系后取传递闭包。因 $p\parallel r$，所加关系不会产生环；分子恰好计数满足该先后事件的原扩张。

核满足易核的单调性
\[
K(i+1,j)\le K(i,j),\qquad K(i,j+1)\ge K(i,j),
\]
以及 $K^{r,p}(j,i)=1-K^{p,r}(i,j)$。它们本身不推出 $1/3$ 阈值排除。

### 2.4 rank 计数与 DP 接口

内部 rank 分布可独立按理想计数：
\[
\mu_a^Q(i)=\frac{1}{e(Q)}
\sum_{\substack{I\text{ 是 }Q\text{ 的理想},\ |I|=i-1,\ a\notin I\\
                       I\cup\{a\}\text{ 是理想}}}
 e(Q[I])\,e\!\left(Q\setminus(I\cup\{a\})\right).
\tag{M}
\]
每项对应前 $i-1$ 个元素恰为 (I)，接着是 $a$，再接剩余元素。

标签词的合法状态是已输出次数向量 $c\in\{0,\ldots,m\}^{P}$。可输出标签 $p$ 当且仅当 $c_p<m$，且所有 $r<_{P}p$ 都有 $c_r=m$。令 $A(c)$ 计数到达 $c$ 的合法前缀，$F(c)$ 计数从 $c$ 出发的合法后缀，则
\[
F(c)=\sum_{p\text{ 可输出于 }c} F(c+e_p),\quad F(m,\ldots,m)=1,
\]
且 $F(0)=e(R)$。无需读取 $Q$ 的内部结构。

还可直接求
\[
K^{p,r}_{P,m}(i,j)=\frac{1}{F(0)}
 \sum_{\substack{c_p=i-1,\ c_r\le j-1\\p\text{ 可输出于 }c}}
 A(c)F(c+e_p).
\tag{DP}
\]
每个满足事件的标签词由“第 $i$ 个 $p$ 被输出前”的唯一状态计数一次。

## 3. 外部 $P$ 的均匀 law 并没有自动保留

从均匀标签词抽出“标签首次出现的次序”，得到的确是 $P$ 的扩张，但一般不均匀。

例如 $P=\{a<b\}\sqcup\{c\}$，$m=2$。标签词等价于长度四的固定链词 $aabb$ 与两个 $c$ 的交织，共 $\binom62=15$ 个。首次出现的三种外部次序 $abc,acb,cab$ 的词数分别为 $3,7,5$，而均匀 $\operatorname{LE}(P)$ 应为 $1:1:1$。这由固定链词与 $c$ 的插入位置直接计数，并非另一种乘积分布。

即使在每个块均匀随机选一个元素，跨块先后概率也只是
\[
\frac1{m^2}\sum_{i,j}K^{p,r}_{P,m}(i,j),
\]
不必等于 $\pi_P(p,r)$。仍取上例，则 $a,c$ 的此平均概率为 $7/10$，原概率为 $2/3$。不能把“旧 pair”不加说明地识别为某个 cross lift。

## 4. 保持严格反例究竟还缺什么

定义
\[
B(P,Q)=\max_{\substack{p\parallel_P r\\a,b\in Q}}
  \beta\!\left((\mu_a^Q)^T K^{p,r}_{P,m}\mu_b^Q\right),
\]
无外部不可比 pair 时令 $B=0$。由所有 pair 的分类，得到精确恒等式
\[
\boxed{\delta(P[Q])=\max\{\delta(Q),B(P,Q)\}.}\tag{B}
\]

因此，从 $\delta(P),\delta(Q)<1/3$ 推出 $\delta(P[Q])<1/3$，**唯一尚缺的非平凡内容是整个 cross-rank 项满足**
\[
\boxed{\quad B(P,Q)<\frac13.\quad}\tag{T}
\]
等价地，对每个 $p\parallel r,a,b$，实际混合值都须落在
\[
[0,1/3)\ \cup\ (2/3,1].
\]
它不能由均匀纤维、计数乘积、同块概率保留或核的坐标单调性直接推出。特别是 $\delta(Q)$ 不给出某个元素 rank 的位置：所有链的 $\delta=0$，但链内各元素的 rank 可以是任意确定位置。

在共同前提 $\delta(P),\delta(Q)<1/3$ 下，一种比 (T) 更强、足够但尚未证明的“外部偏向对齐”不等式是：若 $\pi_P(p,r)>2/3$，则
\[
\min_{a,b\in Q}(\mu_a^Q)^T K^{p,r}_{P,m}\mu_b^Q>2/3,
\]
原方向小于 $1/3$ 时则要求所有混合值小于 $1/3$。不得将这个更强结论当成现有引理；完整阈值保持也未必需要沿每个原 pair 的方向对齐。

自代换取 $Q=P,m=n$，有
\[
\boxed{\delta(P[P])=\max\{\delta(P),B(P,P)\}\ge\delta(P).}\tag{S}
\]
由 (S) 已有单向蕴含：若 $P[P]$ 是严格反例，则 $P$ 必是严格反例。未知的是反方向。

所以自代换的 balance 本来就不减。要保留严格反例，需要新增 balance 虽可能增加，却始终低于 $1/3$。这需要阈值特有的 cross-rank 不等式，不能用普适“不增”代替。

## 5. 可非空核验的强化被边界例明确否定

普适强化 $\delta(P[P])\le\delta(P)$ 可以在普通已知偏序上测试，无需假设存在严格反例。它已经失败。

取
\[
P=\{a<b\}\sqcup\{c\}.
\]
其三条扩张给出 $\delta(P)=1/3$，内部 rank 分布为
\[
\mu_a=(2/3,1/3,0),\quad
\mu_b=(0,1/3,2/3),\quad
\mu_c=(1/3,1/3,1/3).
\]
$R=P[C_3]$ 是长度六的链 $a_1<a_2<a_3<b_1<b_2<b_3$ 与长度三的 $c$-链的并，故
\[
e(R)=\binom93=84,\qquad e(P[P])=84\cdot3^3=2268.
\]

考察实际 cross pair
\[
x=(c,a),\qquad y=(a,c).
\]
令 $A_i$ 为六链第 $i$ 个元素，$C_j$ 为三链第 $j$ 个元素。均匀交织下的所需核值是
\[
\begin{array}{c|cc}
 & C_1&C_2\\\hline
 A_1&2/3&11/12\\
 A_2&5/12&65/84\\
 A_3&5/21&25/42
\end{array}
\]
表中每项可由超几何计数
\[
\Pr(A_i<C_j)=
\frac{\displaystyle\sum_{k=i}^{\min(6,i+j-1)}
 {6\choose k}{3\choose i+j-1-k}}
 {{9\choose i+j-1}}
\]
直接获得。于是
\[
\begin{aligned}
\Pr(y<x)
 &=\frac13\left[
  \frac23\left(\frac23+\frac5{12}+\frac5{21}\right)
 +\frac13\left(\frac{11}{12}+\frac{65}{84}+\frac{25}{42}\right)\right]\\
 &=\frac{23}{42},
\qquad \Pr(x<y)=\frac{19}{42}.
\end{aligned}
\]
所以仅此一个解析证书已经给出
\[
\delta(P[P])\ge19/42>1/3=\delta(P).
\]
该 pair 的有利扩张数为 $2268\cdot19/42=1026$。独立完整概率检查还确定此例的最大值恰为 $19/42$；否定强化本身只需上面的一个 pair，无需该最优性结论。

**边界声明：** 此输入 $\delta(P)=1/3$，不满足严格前提。因此它否定普适 balance 不增，**没有否定** $\delta(P)<1/3\Rightarrow\delta(P[P])<1/3$。反过来，缺少真实严格反例输入，也不能把条件命题的空测试当作支持证据。

## 6. 更局部的来源标签转移也存在准确障碍

另一种可非空检验的企图是：若某 cross pair balanced，则四个来源标签 $p,r,a,b$ 中已有一个原 balanced pair。这同样不成立。

取
\[
P=\{a<b<c\}\sqcup\{x\},
\]
自代换时考察 $(a,c)$ 先于 $(x,a)$。此时
\[
\mu_c=(0,0,1/4,3/4),\qquad
\mu_a=(3/4,1/4,0,0).
\]
外部核来自长度十二的链与长度四的链的均匀交织。所需四个值为
\[
K(3,1)=11/28,\quad K(3,2)=275/364,\quad
K(4,1)=99/364,\quad K(4,2)=33/52.
\]
代入 (F) 得
\[
\Pr((a,c)<(x,a))
 =\frac3{16}\frac{11}{28}+\frac1{16}\frac{275}{364}
  +\frac9{16}\frac{99}{364}+\frac3{16}\frac{33}{52}
 =\frac{11}{28}\in[1/3,2/3].
\]
但四个来源标签只涉及 $\{a,c,x\}$：$a<c$，而 $\pi_P(a,x)=3/4$、$\pi_P(c,x)=1/4$。其中没有原 balanced pair。此例全局仍有 $\pi_P(b,x)=1/2$，故 $\delta(P)=1/2$。

这个障碍严格表明：若希望把新增 balanced pair 转移回原偏序，不能只检查该 pair 的四个来源标签；可能需要 $P$ 的全局信息。它仍不冒充严格反例保留命题的反例。

## 7. 参数放大及证明

对顶点 $(p,a)$，其不可比邻居分为互不相交的两类：

- 外部 $r\parallel_P p$ 的每个块贡献 $m$ 个邻居；
- 同块内 $b\parallel_Q a$ 的邻居。

所以
\[
\deg_\parallel^{P[Q]}(p,a)=m\deg_\parallel^P(p)+\deg_\parallel^Q(a).
\]
最大化时两个坐标可分别选取各自最大度顶点，得到 (D)。自代换时 $n'=n^2,\Delta'=(n+1)\Delta$，且
\[
\frac{\Delta'}{n'-1}=\frac{(n+1)\Delta}{n^2-1}=\frac{\Delta}{n-1}.
\]
若不断自代换 $P_{k+1}=P_k[P_k]$，$n\ge2$，则
\[
n_k=n^{2^k},\qquad
\Delta_k=\Delta(P)\frac{n_k-1}{n-1}.
\]
原偏序非链时 $\Delta(P)>0$，故最大不可比度趋于无界；原偏序为链时始终为 $0$。这一放大结论独立于尚未解决的 (T)。

可选的另外两个精确参数是
\[
\operatorname{height}(P[Q])=\operatorname{height}(P)\operatorname{height}(Q),\qquad
\operatorname{width}(P[Q])=\operatorname{width}(P)\operatorname{width}(Q).
\]
证明：一条链所涉及的外部标签必须成链，每块最多取 $h(Q)$ 点；一条反链涉及的外部标签必须成反链，每块最多取 $w(Q)$ 点。反向分别沿最长外链/最大外反链取每块最长内链/最大内反链即达到上界。

## 8. 可以与不可以据此宣称的结论

可以严格宣称：代换的计数、均匀 law、每个 pair 概率、cross-rank 精确归约和最大不可比度放大均已给出；自代换确实突破“序和不放大最大不可比度”的限制。

已经确定的方向是：$P[P]$ 为严格反例蕴含 $P$ 为严格反例。

目前不能宣称反方向：自代换保留严格反例、所有 lexicographic product 保留严格反例、或由本操作与任何尚未独立复核的外部大参数结果推得矛盾。操作本身与均匀纤维并未提供欠缺的阈值特有不等式 (T)。
