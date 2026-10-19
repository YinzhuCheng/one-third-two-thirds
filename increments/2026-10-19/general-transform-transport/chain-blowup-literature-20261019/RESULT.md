# 固定商链膨胀的文献定位：定性主结论由 Aires–Kahn 直接涵盖

核验日期：2026-10-19。范围：五个原始来源；只读公开文献与两份现有稿件，没有联系作者或对外发布。以下区分文献定理、直接推论和本轮未核验的新颖性。

## 1. 核心结论

**已找到直接涵盖定性主结论的原始文献，不能再把该定性范围称为新结果。**

Max Aires、Jeff Kahn 的 [Variance vs. range for linear extensions, and balancing extensions in posets of bounded width，arXiv:2510.26134v1](https://arxiv.org/abs/2510.26134v1)，Theorem 1.6（PDF 第3页；[精确原文位置](https://arxiv.org/html/2510.26134v1#S1.Thmthm6)）给出：

\[
\forall w\in\mathbb N\ \forall\varepsilon>0\ \exists T(w,\varepsilon)\quad
\forall\text{有限偏序 }Q:\quad
w(Q)\le w,\quad \pi(Q)\ge T(w,\varepsilon)
\ \Longrightarrow\ \delta(Q)>\tfrac12-\varepsilon,
\]

这里 \(\pi(Q)=\max_{x\in Q}|\{y:y\parallel_Qx\}|\)，\(\delta\) 使用真实均匀线性扩张，与两稿定义一致。这是固定**宽度上界**下对所有偏序的一致断言；并不是宽度趋于无穷定理，也不要求商固定或全部链块同时变长。其依赖链是 Theorem 1.3（最大不可比数发散迫使某元素的位置标准差发散）和 Theorem 1.5（有界宽度下大标准差迫近平衡）。[Aires–Kahn 原稿](https://arxiv.org/html/2510.26134v1)

### 1.1 直接应用：仅需两个精确恒等式

以下是本报告给出的初等适用性推导，不是对文献证明的改写。设
\[
R=P[(C_{n_p})_{p\in P}],\qquad n_p\ge1,\qquad
A(P)=\{p:\exists q,\ p\parallel_Pq\}.
\]

首先
\[
\boxed{w(R)=w(P).}
\tag{L1}
\]
因为反链与每个链块至多相交一次，其投影是 \(P\) 的反链；反之从 \(P\) 的最大反链各取一个真实元素即可。

其次，对块 \(p\) 中任意真实元素 \(x\)，有
\[
\pi_R(x)=\sum_{q\parallel_Pp}n_q,
\quad\text{因而}\quad
\boxed{\pi(R)=\max_{p\in P}\sum_{q\parallel_Pp}n_q.}
\tag{L2}
\]
同块内是链，可比外块之间完整比较，不可比外块之间完整不可比，故此式精确成立。若 \(P\) 非链，任选最长活跃块 \(p\) 及其不可比邻点 \(q\)，则块 \(q\) 中任意真实元素与块 \(p\) 的全部元素不可比，所以
\[
\max_{p\in A(P)}n_p\ \le\ \pi(R)
\ \le\ (|A(P)|-1)\max_{p\in A(P)}n_p.
\tag{L3}
\]

将 (L1)–(L3) 代入文献定理，立即得到：

- 固定有限非链 \(P\)，只要 \(\max_{p\in A(P)}n_p\to\infty\)，就有 \(\delta(R)\to1/2\)。这是 BB §8 的 AU。
- BB1 中只要一个发散块活跃，便满足上述条件；其他块可以保持有限长度，也可以任意变速。
- 没有 \(\min_p n_p\to\infty\) 假设，没有正权比例下界，没有最大/最小链长比限制；例如一个活跃块长度为 \(N\)，不可比邻块长度为1，仍被覆盖。
- 在固定 \(\varepsilon\in(0,1/6)\) 下，若 \(\delta(R)\le1/3\)，则全部活跃链长都严格小于 \(T(w(P),\varepsilon)\)。所以固定商的低平衡有限盒**存在性**也是该文献定理的直接推论。
- 更强的量词：即使 \(P=P_k\) 改变，只要 \(w(P_k)\le w\) 有共同常数上界，同一个 \(T(w,\varepsilon)\) 对这些外商及全部正整数链长向量均适用。不能移除这个共同宽度上界。

非活跃块属于精确序和骨架，删除它们保留 \(\delta\)；这由均匀线性扩张在序和分量上的笛卡尔积直接得到。BB2 的恒等式可保留为结构说明，不能用它重新包装上述已被涵盖的定性范围。

## 2. 版本与公开时间

同作者更早的 [Balancing Extensions in Posets of Large Width，arXiv:2509.11549v1](https://arxiv.org/abs/2509.11549v1)，2025-09-15，§2 Corollary 2.8 已公开陈述相同的固定宽度结论；该稿将困难的 \(\pi\leadsto\sigma\) 证明推迟到伴篇。2025-10-30 的 2510.26134v1 是本轮核验其证明和精确假设使用的来源。[2509 原文 §2](https://arxiv.org/html/2509.11549v1#S2)

不要因为前一篇标题含“large width”就只检查其主定理，或反过来把其大宽度条件套到本题。它的 Corollary 2.8 本身就是有界宽度结论。

截至本轮检索，[2510.26134 的官方记录](https://arxiv.org/abs/2510.26134)只列2025-10-30的 v1，11页，未列 journal-ref 或期刊 DOI。页面的 10.48550/arXiv.2510.26134 是 arXiv 自身 DOI。**本轮未核实正式发表，不能据此断言未发表。** 也没有把 arXiv 记录说成同行评审认证。

## 3. 其他三个原始来源：相关，但不是渐近结论的替代依据

### 3.1 Bergman：对象与计数先例

George M. Bergman，[Some results on counting linearizations of posets](https://math.berkeley.edu/~gbergman/papers/unpub/lnzn.pdf)，作者存稿2018-06-08；另有 [arXiv:1802.01712](https://arxiv.org/abs/1802.01712)。

- §4 Definition 8 正是固定有限外偏序上任意长度链的 lexicographic sum。
- Theorem 7 将一般内部偏序代换的扩张计数分解为内部扩张数乘以相应链膨胀扩张数。
- Proposition 12、Theorem 13 研究固定其他链长后，扩张数关于可变长度何时为多项式；Theorem 13 的条件是可变外点集合成链。

**适用性判断：** 这是对象、分解、有限标记插入及计数多项式的重要先例；该稿的 sign-imbalance 指扩张的奇偶差，不能当作本题的成对比较 balance constant。核验的这些结论没有给出 AU 的 \(1/2\) 极限。作者存稿首页明确说明保留在线但决定不正式发表；这里按作者存稿引用，不把它描述为已发表论文。[Bergman 原稿](https://math.berkeley.edu/~gbergman/papers/unpub/lnzn.pdf)

### 3.2 Dolores-Cuenca、Guzmán-Sáenz、Kim：内部块的平衡保持

Eric R. Dolores-Cuenca、Aldo Guzmán-Sáenz、Sangil Kim，[The gold partition conjecture and the Lexicographic sum of posets，arXiv:2410.12494v1](https://arxiv.org/abs/2410.12494v1)，2024。

Corollary 2.7 给出
\[
\delta(P(Q_1,\ldots,Q_m))\ge\max_i\delta(Q_i),
\]
来自内部块的均匀扩张概率保持；Lemma 2.5 是 Gold Partition Conjecture 的代换保持。[原稿 §2](https://arxiv.org/html/2410.12494v1#S2)

**适用性判断：** 当全部 \(Q_i\) 是链时，右端为0，不能由此得到 AU。尤其不能把“内部块的均匀限制”错误推成“任意删去有限外块后的核心仍均匀”；后者正是 BB §10 所警告的非均匀重加权问题。这一来源也不能授权一般内部偏序版本的 \(1/2\) 极限。

### 3.3 Stanley：order-polytope 基础，不是本题渐近定理

Richard P. Stanley，[Two poset polytopes](https://math.mit.edu/~rstan/pubs/pubfiles/66.pdf)，Discrete & Computational Geometry 1 (1986), 9–23。

§3、§5 按线性扩张分割 order polytope；Theorem 4.1 联系 order polynomial 与 Ehrhart polynomial，Corollary 4.2 给出 \(\operatorname{vol}\mathcal O(Q)=e(Q)/|Q|!\)。等体积单纯形直接解释“均匀 polytope 坐标排序产生均匀线性扩张”。[作者存档原论文](https://math.mit.edu/~rstan/pubs/pubfiles/66.pdf)

**适用性判断：** 这是两稿几何模型的标准基础；固定偏序的格点伸缩/Ehrhart 渐近与偏序本身随链长改变是不同过程。本轮核验的该论文结论不直接提供 AU、任意比例端点浓缩或最大活跃块有效阈值。

## 4. 有效化定位与两稿应怎样表述

1. **定性层已经定位。** BB1/AU、低平衡有限盒存在性，均应明确标为 Aires–Kahn 有界宽度定理的推论；现有长证明可保留为该特殊结构中的自含替代证明，不应称为新的适用范围。
2. **统一性比 fixed-P 更强。** 只有外商固定并非最优量词：原文容许外商变化、只保持宽度共同有界。没有共同宽度上界时，本报告不作保证。
3. **有效化不自动等于新颖性。** 2510.26134 的定理以定性收敛陈述，其证明有可追踪的常数选择，但本轮未重审全证明以抽取一个可计算模，也未找到直接给出两稿同样的“混合尾域证书 + 量词消去 + 有限截断树”的算法陈述。没有找到相同算法，不证明算法或有效性首次出现。
4. **有效算法与运行结果分开。** active-threshold 稿提供的是理论终止与证书构造主张；没有实际运行量词消去、没有输出具体数值 \(M_A\)。文献已给定性存在性，不能把这误报成现已计算出阈值。要论证进一步贡献，应比较“显式可计算模、证书形式、定量误差/复杂度或新的自含机制”，并另做这些层面的文献与证明核验。
5. **未作全量首创检索。** 本轮止于上述五个原始来源，已足够纠正定性定位。未找到 autonomous-chain 专门渐近定理的更早独立出处；这个未找到不支持原创性。

## 5. 建议导读文字

> 固定商链膨胀的定性 \(1/2\) 极限及活跃链长有限盒存在性，是 Aires–Kahn 有界宽度平衡定理的直接推论。本稿保留该特殊结构的自含几何证明，并进一步讨论理论有效阈值与有限证书构造；相关算法尚未实际运行，且本轮文献核验不认证其有效化层面的新颖性。文献定理还表明：若外商可变但宽度共同有界，定性阈值可只依赖这一宽度上界与误差。

该段是可审阅的研究定位建议，不是代作者或用户对外作出的声明。
