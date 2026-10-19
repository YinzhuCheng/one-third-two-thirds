# 有界不可比度、无界规模核：定向原始文献核查

核查日：2026-10-19。记 $I(P)$ 为有限偏序 $P$ 的不可比图，$D=\Delta(I(P))$；$\delta(P)=\max_{x\parallel y}\min\{\Pr_P(x<y),\Pr_P(y<x)\}$。本报告不重复 Aires–Kahn 固定 width 的大度数渐近结果。

## 先给结论

1. **已有真正的全规模排除：$D\le6$。** Peczarski 2008 的 GPC 定理直接覆盖任意 $n$，不是有限规模枚举的推测。
2. **任意固定 $D$ 给出有界带宽/路径宽度及精确计数接口，但没有自动给出 $1/3$ 平衡或有界最小反例规模。** 可用 $\operatorname{tw}(I(P))=\operatorname{pw}(I(P))\le\operatorname{bw}(I(P))\le2D-1$。这是长度无界、截面有界的结构。
3. **自治块内部的 pair law 严格传递。** 2026 年已正式发表的 lexicographic-sum 论文提供等纤维证明。可以剔除含有较小、已知平衡非链自治块的候选。
4. **不能把“已归约到 prime quotient”说成完成。** 一般商的平衡常数不向上单调；纯链 blowup 仍需处理。该论文 v2 已把这一遗漏补进最后的归约表述。
5. 在下列五条原始来源中，**没有找到**“有界 $D$ 强制有界阻塞长度/确定再生点”或“最小反例 $n\le f(D)$”的定理。此处是定向检索结果，不是对全部文献的不存在证明。

## 最相关的五条原始来源

### L1. Peczarski：$6$-thin 的真正平衡排除

Marcin Peczarski, *The Gold Partition Conjecture for 6-Thin Posets*, **Order 25(2), 91–103 (2008)**。已发表；出版社给出版日 2008-06-25。

- 精确假设：有限偏序中每个元素至多与六个元素不可比，即 $D\le6$；无 $n$ 上界。
- 结论：GPC 成立，因而 $1/3$–$2/3$ 猜想成立。证明大量使用计算机。
- 对本问题：可直接排除整个 $D\le6$ 区域；不能外推 $D=7$。
- 核验层级：出版社原始摘要、书目信息已核；全文在此访问为订阅内容，因此没有把其内部有限归约或程序细节冒称已审。
- 原始源：[出版社与 DOI](https://link.springer.com/article/10.1007/s11083-008-9081-9)。

### L2. Wood：不可比图有界带宽

David R. Wood, *Characterisations of intersection graphs by vertex orderings*, **Australasian Journal of Combinatorics 34, 261–268 (2006)**。已发表；2004 年预印本。

- Theorem 4 的 cocomparability ordering 满足：$i<j<k$ 且 $v_iv_k\in E$ 时，$v_iv_j\in E$ 或 $v_jv_k\in E$。
- Corollary 2：每个 cocomparability 图满足 $\operatorname{bw}(G)\le2\Delta(G)-1$。任何给定偏序的线性扩张也满足上述 ordering 条件；对不可比端点还直接有跨度 $\le d(v_i)+d(v_k)-1$。
- 对本问题：参考线性扩张的切口只需保留有限邻域；是 transfer/frontier 方案的可靠结构入口。没有平衡概率结论，也没有总长度上界。
- 原始源：[期刊 PDF](https://ajc.maths.uq.edu.au/pdf/34/ajc_v34_p261.pdf)、[可检索预印本 PDF](https://arxiv.org/pdf/cs/0404031)。

### L3. Habib–Möhring：树宽等于路径宽度

Michel Habib and Rolf H. Möhring, *Treewidth of cocomparability graphs and a new order-theoretic parameter*, **Order 11(1), 47–60 (1994)**。已发表。

- 精确图类：所有 cocomparability 图，故包括所有有限偏序的不可比图。
- 结论：$\operatorname{tw}(G)=\operatorname{pw}(G)$（Theorem 2.1；也由 L4 的 Fact 5 明确引述）。配合 L2 得二者均 $\le2D-1$。
- 其 interval-width 参数通过包含于原偏序的 interval order 刻画同一分解量；不同文献把 clique size 或 bag size 减一与否的归一化不同，应用时应固定约定。本报告不依赖该符号的 off-by-one。
- 对本问题：可以把树形分隔转成线性前沿；不能由此声称存在空前沿、再生切口或有限多全局核。
- 核验层级：出版社原始摘要已核；定理号/等式交叉核于 L4 原文。
- 原始源：[出版社与 DOI](https://link.springer.com/article/10.1007/BF01462229)。

### L4. Eiben–Ganian–Kangas–Ordyniak：分隔结构与精确计数

Eduard Eiben, Robert Ganian, Kustaa Kangas, Sebastian Ordyniak, *Counting Linear Extensions: Parameterizations by Treewidth*, **Algorithmica 81, 1657–1683 (2019)**，DOI 10.1007/s00453-018-0496-4；先发表于 **ESA 2016**, LIPIcs 57, 39:1–39:18。均已发表。

- Theorem 2：参数 $k=\operatorname{tw}(I(P))$ 下，精确计算 $e(P)$ 为 FPT，时间 $f(k)n^{O(1)}$。
- Lemma 3：任意删点集 $S$ 后，$I(P)-S$ 的不同连通分支在 $P$ 中整体全序排列。
- Corollary 2：不可比图树宽 $\le k$ 时，cover–incomparability combined graph 树宽 $\le3k+2$；再用 MSO 计数。本文并非给一个现成的实用前沿 DP。
- 应用：加入一个不可比关系 $x<y$ 再取传递闭包只会删不可比边，因此参数不增，可算 $e(P+(x<y))/e(P)$。这是个体实例认证能力，**不是**全体实例必有平衡对的定理。
- 原始源：[期刊 DOI](https://link.springer.com/article/10.1007/s00453-018-0496-4)、[作者存档全文](https://eprints.whiterose.ac.uk/id/eprint/168075/1/Counting%20Linear%20Extensions%20Parameterizations%20by%20Treewidth.pdf)、[ESA 2016 正式记录](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ESA.2016.39)。

### L5. Dolores-Cuenca–Guzmán-Sáenz–Kim：自治块严格传递，商不单调

Eric Dolores-Cuenca, Aldo Guzmán-Sáenz, Sangil Kim, *The Gold Partition Conjecture and the Lexicographic Sum of Posets*, **Order 43, article 34 (2026)**，DOI 10.1007/s11083-026-09747-y。**已于 2026-09-29 正式发表**；不能继续标作仅 2024 预印本或 to appear。

- v2 Lemma 1：限制映射 $L(P\circ_iQ)\to L(Q)$ 各纤维等势。因此自治块 $Q$ 内每一对的 law 都原样保留。
- Theorem 3：某个非链输入块满足 GPC，则整个 lexicographic sum 满足 GPC。Corollaries 2–3 给 $\delta(P(Q_i))\ge\max_i\delta(Q_i)$ 及平衡对传递。
- Remark 3：不能替换成 $\delta(P(Q_i))\ge\delta(P)$；文中讨论商的概率改变及下降例子。
- 关键版本差异：v1 最后说只需证 indecomposable；v2 最后明确还须证 indecomposable $P$ 的非平凡**链 blowup** $P(\langle s_1\rangle,\ldots,\langle s_n\rangle)$，$\prod s_i>1$。
- 原始源：[正式发表记录](https://link.springer.com/article/10.1007/s11083-026-09747-y)、[v2 全文](https://arxiv.org/html/2410.12494v2)、[v1 用于版本核对](https://arxiv.org/html/2410.12494v1)。

## 可以立即采用的自含推论（非冒称文献新定理）

### A. 更直接的精确理想格 DP

固定任意线性扩张 $v_1,\ldots,v_n$。对任意真理想 $J$，设 $i=\min\{j:v_j\notin J\}$。若 $j>i$ 且 $v_j\in J$，必有 $v_i\parallel v_j$：反向比较被参考线性扩张排除，$v_i<v_j$ 又会违反理想性质。因此

$$J=\{v_1,\ldots,v_{i-1}\}\cup S,\qquad S\subseteq N_{I(P)}(v_i)\cap\{v_{i+1},\ldots,v_n\}.$$

于是理想总数至多 $1+\sum_i2^{d^+(v_i)}\le1+n2^D$。枚举这些候选并筛理想，以 $F(J)=\sum_{x\in\max J}F(J\setminus\{x\})$、$F(\varnothing)=1$ 精确计数，得到 $2^D n^{O(1)}$ 算法。对 $P+(x<y)$ 重用同一参数界，能核全部 pair laws。状态值为无界整数；有限的“接口形状”不等于有限个概率或有限个可替换核。

### B. Ordinal sum 是严格安全的切断

取 $S=\varnothing$ 于 L4 Lemma 3，得到 $P$ 是 $I(P)$ 连通分支的 ordinal sum。线性扩张只能依序拼接，各块内部 law 原值；故 $\delta(P)=\max_C\delta(C)$。最小非链反例可以假设不可比图连通。删去非空 $S$ 后虽仍有全序分支，却可能经 $S$ 发生相关性，不能无条件把各分支的平衡对提升。

### C. 自治模块的参数约束与剩余核

这里“自治”要求外点对块内所有点具有**相同方向**的比较关系，不能只用无向图 module 代替。若不可比图连通，$C$ 是真自治链，则存在外点与整个 $C$ 不可比，故 $|C|\le D$。对链 blowup $R(\langle s_i\rangle)$，块 $i$ 内各点不可比度恰为 $\sum_{j\parallel_R i}s_j$，所以剩余对象是带正整数权且满足这些邻居权和约束的 prime quotient。每个块可有界，quotient 的点数仍未有界。

## 对下一步的建议与停止线

- 直接做：把 $D\le6$、ordinal-sum、含已证非链自治块作为严格排除器；把链 blowup 权重保留下来。
- 对无界长度剩余核：有界前沿允许精确 transfer、带标记 pair 计数和候选反例搜索。若想升级为全规模证明，需要另证一个在任意边界权重/可达边界分布下成立的平衡不等式，或一个保持 pair laws 的有限替换/阻塞长度定理。
- 目前五条来源都不给上述最后一步。不要以 FPT、带宽有界、反复出现接口形状或“所有已算实例通过”填补它。

