# 自治链延长交错：定向文献核验及 Shepp 机制的直接推论

日期：2026-10-19。只读文献；未联系作者，未改任何外部材料。

## 结论先行

- 未在下述有限检索中找到把目标交错原样命名、陈述的一般定理；这不构成新颖性判断。
- **但弱交错已有直接的经典证明机制覆盖：Shepp 的 XYZ 证明所用“锚定差坐标”FKG 格，比 XYZ 两事件陈述更强。** 把新自治链点插在指定 `c_i` 之后，order-polytope 积分纤维长本身就是该格上的增函数。因此无须单独证明每个截断合取 `c_m<y<所有U` 与 `c_i<x` 正相关。
- 一般弱交错 `Q_i(m+1) ≥ Q_i(m) ≥ Q_{i+1}(m+1)` 的下面推导不依赖 `t=2`。是否可以统一写严格号，由主任务的证明作者和独立审稿继续核验；本报告不冒领严格性证明。
- Shepp 1980 的“monotonicity”定理自身是固定底集上添加关系的结果，不可直接替代上述积分桥梁。Bergman 的一般替换链计数、块内均匀性和固定偏序上的秩对数凹，也均不能单独省去该桥梁。

## 1. 精确目标和测度

有限外偏序固定，加入自治链 `C_m=(c_1<⋯<c_m)`。对每个外点，它与所有链点的关系相同。记共同前驱集合为 `D`、共同后继集合为 `U`、其余外点集合为 `I`；传递性给 `D<U`。指定 `x∈I`。

`Q_i(m)=Pr_{LE(P_m)}(c_i<x)`，所有 LE **实际均匀**，`i` 是链中的固定整数下标，既不是全偏序固定秩，也不是归一化秩。`P_m→P_{m+1}` 是加入一个新点；通过重命名，允许将新点置于任意相邻链点之间。

## 2. 为什么 Shepp 证明机制确实能用

### 2.1 已知锚定格的准确适用范围

Brightwell–Trotter 的完整重建见来源 [S2] §7.3.5，PDF pp.9–10。对**任意**有限偏序 `P` 和指定锚点 `a`，其构造为

`Φ(t) = (s, (r_y)_{y≠a}) = (−t_a, (t_y−t_a)_{y≠a})`。

先在全部保序映射 `P→[k]` 上使用此格及 FKG，再取极限得到均匀 LE 的相关结论。构造不要求宽度二、不要求锚点极小或极大、不要求任何自治块。

同一构造可直接在均匀 order polytope 上使用。其像由以下约束给出：

- `−1≤s≤0`；
- `s≤r_y≤s+1`；
- `r_y≤r_z`，若 `y<z` 且两者都不是锚点；
- `r_y≥0`，若 `a<y`；`r_y≤0`，若 `y<a`。

每条约束都在坐标 min/max 下封闭，故整个像是子格；`|det Φ|=1`，均匀体积密度满足 FKG 所需的 log-supermodularity。亦可由该来源的有限网格构造经 Riemann 极限得到此连续版本。除等值超平面上的零测集外，`{t_a<t_x}` 正是增事件 `{r_x>0}`。

**U 空的边界完全合法：** 若 `b=min_{u∈U}t_u`，约定 `U=∅` 时 `b=1`，则 `b−t_a` 在格上分别为 `min_u r_u` 或 `1+s`，两者均为增函数。

### 2.2 最短的加点积分桥梁

下面是本报告对经典机制的直接推导，并非声称文献中已原样列出这一交错公式。

在 `O(P_m)` 上取均匀体积测度，锚定 `a=c_i`。令 `A={t_{c_i}<t_x}`。

- 若 `i<m`，在 `c_i,c_{i+1}` 之间加入新点，新坐标可取区间 `(t_{c_i},t_{c_{i+1}})`；纤维长
  `W=t_{c_{i+1}}−t_{c_i}=r_{c_{i+1}}`。
- 若 `i=m`，把新点加在链顶，共同后继坐标的最小值记 `b`，则
  `W=b−t_{c_m}=min_u r_u`；`U=∅` 时为 `1+s`。

自治性保证加入内部点时原有 `D/U` 约束被相邻链点约束蕴含，原有 `I` 不产生附加限制。新偏序重命名后就是 `P_{m+1}`，且旧 `c_i` 仍是新链的第 `i` 个元素。

`1_A,W` 同增，故 FKG 给 `Cov(1_A,W)≥0`。对新点积分得

`Q_i(m+1)=E[1_A W]/E[W]`，

`Q_i(m+1)−Q_i(m)=Cov(1_A,W)/E[W]≥0`。

这里 `E[W]>0`。order polytope 被每个 LE 对应的等体积单纯形剖分，因此 `Pr(A)=Q_i(m)` 是实际均匀 LE 概率；没有改用加权 LE。对整个偏序取对偶即得另半交错。

**与主任务顶插 S 的关系。** 设 `N=|P_m|`，顶插的离散可插槽数为 `S`，那么条件于一条 LE，均匀次序统计量给 `E[b−t_{c_m}|LE]=S/(N+1)`。所以主任务的 `Cov_LE(1_A,S)=(N+1)Cov_poly(1_A,b−t_{c_m})` 方向正确。上面的内部插点法更直接，不需要对链后段再条件积分。

### 2.3 不能替换成未经证明的逐项合取相关

XYZ 的简式只断言共同源事件 `{a<x}` 与 `{a<y}` 正相关。乘入 `{y<所有U}` 不能直接保留相关性。它在锚定格上含比较 `r_y<r_u`，不是一般的坐标增事件。甚至 `i<m` 时 `{c_i<x}` 在锚 `c_m` 下也不是单个坐标符号事件。因此正确用法是锚定 `c_i`，对整个窗口长度用 FKG，而非对 `S` 的每个指示项逐项套 XYZ。

## 3. 五个最相关且实际检查的来源

### [S1] L. A. Shepp, 1980

**The FKG Inequality and Some Monotonicity Properties of Partial Orders**, SIAM J. Algebraic Discrete Methods 1(3), 295–299。DOI 10.1137/0601034。

原文全文：[作者院系 PDF](https://faculty.wharton.upenn.edu/wp-content/uploads/2012/04/Fkg-inequality-and-some-monotonicity-properties-of-partial-orders.pdf)。已逐节核 Theorem 1–2、(1.5)–(1.6)、(2.7)–(2.17)。

Theorem 2 的基准是两块完全无跨块关系的 disjoint sum；对两组同方向跨块关系断言正相关。Theorem 1 对两条链有额外条件化单调性。原文首页及第二页明确给一般已有跨块关系时的失败例。这些都是固定底集上的加关系结论；**不直接覆盖加新点**。原文的有限保序映射是证明工具，最终极限确为均匀 LE。

### [S2] G. R. Brightwell and W. T. Trotter, 2011

**Correlation**, monograph draft chapter 7，2011-03-31，尤其 §7.3.5 pp.9–10。

[完整章 PDF](https://posets.tcs.uj.edu.pl/archive/attachements/DraftChapters/7-correlation.pdf)。已读到 `Φ(ω)=(-ω(x),ω(y)−ω(x),…)`、子格证明和 Theorem 7.3.5 的完整论证；不是仅凭摘要。

这份来源明确把机制归于 Shepp 的 1982 XYZ 论文。它给本报告最关键的已核证文本：任意有限 P 的锚定差坐标格；FKG 对任意增函数适用，远强于两个事件的简式。**不能把“已核该完整重建”写成“已逐页核 Shepp 1982 原刊 PDF”。** 原刊出处是 L. A. Shepp, *The XYZ Conjecture and the FKG Inequality*, Ann. Probab. 10(3) (1982), 824–827；原官方入口被 Incapsula 拦截，旧 UPenn 下载链不可取。本报告没有绕过访问限制。

### [S3] George M. Bergman, 2018

**Some results on counting linearizations of posets**, arXiv:1802.01712，作者稿 2018-06-08；作者说明未正式发表。

[作者 PDF](https://math.berkeley.edu/~gbergman/papers/unpub/lnzn.pdf)。已核 §4–5，特别 Proposition 12(a)，PDF p.11：固定其他替换块，只改变一个替换链长度时，LE 总数是该长度的多项式，次数为对应外不可比点总数。证明按外部 LE 的可插区间大小 `d` 使用 `binom(m+d,d)`。

这是一般自治链延长的准确计数先例；没有在已核章节中给出目标概率比值交错。其 ordinary linearization-count 是实际计数，另外讨论的 sign-imbalance 不可混入概率测度。

### [S4] Eric Dolores-Cuenca, Aldo Guzmán-Sáenz and Sangil Kim, 2026 v2

**The Gold Partition Conjecture and the Lexicographic sum of posets**, arXiv:2410.12494v2，2026-09-26。

[原作者 HTML 全文](https://arxiv.org/html/2410.12494v2)。已核 Lemma 1–2、Corollary 1、Theorem 3 及末尾 balance-constant 讨论。

给出按块内 LE 与各块大小的链替换 LE 进行精确分解，块内投影均匀；推出 LE 因子分解和 `δ(lexsum)≥max δ(Q_i)`。这些结果只在固定块大小下处理块内统计，不能把块内均匀性变成外部投影均匀性，也没有给链–外点的跨长度交错。链块自身 `δ=0`，该下界对此目标没有直接力量。

### [S5] Richard P. Stanley, 1981

**Two Combinatorial Applications of the Aleksandrov–Fenchel Inequalities**, J. Combin. Theory A 31(1), 56–65。DOI 10.1016/0097-3165(81)90053-4。

[作者 PDF](https://math.mit.edu/~rstan/pubs/pubfiles/48.pdf)。已核 Theorem 3.1–3.2，PDF pp.7–8：固定一个偏序，固定链上各指定点的全局整数秩计数，改变一个指定秩时具有对数凹性；单点特例是固定元素的秩分布对数凹。

这是 actual LE 的固定偏序、固定全局秩结论；不是归一化秩，也不是加新点。仅凭这一性质不能直接宣称 `m→m+1` 的目标概率比交错。

## 4. Pólya/均匀插入的测度警戒

对外部 LE `σ` 固定，可插窗口含 `d(σ)` 个外点时，链长 m 的插入数为 `binom(m+d,d)`。于是实际 `P_m` 对 `σ` 的投影按这个数倾斜，通常不均匀。链长增加后又乘倾斜因子

`binom(m+1+d,d)/binom(m+d,d)=(m+d+1)/(m+1)`。

所以“先抽实际 P_m，按固定 σ 的均匀 Pólya 插入核加一个链点”如果不处理 σ 的重新加权，不能自动给实际均匀 P_{m+1}。本轮检索未找到可不经这一处理而直接提供目标交错的通用 Pólya 插入定理。以上仅解释测度差异，不是原猜想反例。

## 5. 与前置 t=2 成果的关系及状态

已读前置 `/workspace/shared/slot-theorem-consequences-20261019/RESULT.md`。其中 t=2 全列严格交错有完整的实际计数证明。这里的文献发现将一般弱交错置于已知 Shepp-FKG 机制下；它不否定前置证明，也不自动延伸前置 cross/完全外部 pair 的结论。

建议写法：**“一般弱交错可由 Shepp 的锚定差坐标 FKG 构造及一个加点积分论证推出。”** 不宜写“发现一般 XYZ 交错新定理”，也不宜写“没有检索结果，故新颖”。若最终需要出版级归属，原刊 Shepp 1982 的逐页原文核验仍是文献获取上的剩余项；数学机制本身已有完整可核重建，且第2节把所需适用条件明确展开。
