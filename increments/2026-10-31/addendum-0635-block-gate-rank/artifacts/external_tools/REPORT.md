# 外部工具核验：真实首分叉权重与同下集首次命中

2026-10-31；只读公开来源和恢复档案；未改仓库、发布或联系作者。

## 可直接保留的结论

1. **已发表 Chan–Pak 的 unique-cover 四删除不等式有一个精确 C2 接口。** 它保留全部 A/F 完成权重，无需新预稿。但下面的两式只是必要一致性条件，尚不能排除困难残余。
2. **同严格下集反链的首次命中秩可接入一个比单元素 Stanley 更合适的预稿定理。** 必须保留 P-consistent 条件；任意集合版已经被同文四点例反驳。
3. **相邻秩前缀包含耦合预稿值得独审，但不能把它当作已公认或高效算法。** 在当前 C2 四点前缀上，它给的唯一非平凡 Hall 约束恰可从第1项已发表工具得到，因此不必新增承重依赖。

## 1. 已发表四删除工具与保真映射

来源：S. H. Chan–I. Pak, *Correlation inequalities for linear extensions*, Advances in Mathematics 458 (2024), 109954，Corollaries 3.10、3.11。
原文：https://arxiv.org/html/2211.16637#S3.SS3
发表记录：https://doi.org/10.1016/j.aim.2024.109954

**术语防火墙。** 文中“v is a unique cover of x”意为 **v 覆盖 x 且不覆盖其他元素**；不要求 x 仅有 v 一个上覆盖。若 x 极小，则这等价 D(v)={x}。下文对 c2、e 使用的正是这一方向。

原工具：
- x,y 为不同极小点，D(v)={x}, D(w)={y}，则
  `e(Q−x−y)^2 >= e(Q−x−v) e(Q−y−w)`。
- x,y,z 为三个不同极小点，D(u)={z}，则
  `e(Q−u−z) e(Q−x−y) <= 2 e(Q−x−z) e(Q−y−z)`。
其他极小点可以存在；没有宽度、不可比度或尾部自主假设。

采用本地 THEOREMS.md 的 C2 全部关系与 T08 的 B、Z。新增临时记号（不分配项目定理编号）：

```
R = P−{v,c1},                  m=|R|,
B = e(P−{v,c1,b}),             C = e(P−{v,c1,d}),
D0= e(P−{v,c1,b,d}),           E0= e(P−{v,c1,d,e}),
Z = e(P−{c1,c2}),              V0= e(P−{v,d,e}).
```

### (A) BE0 <= 2 C D0

在 R 中 b,d 极小，且 D_R(e)={d}。给 R 添加一个**孤立新点 t**，取上述第二条的 `(x,y,z,u)=(t,b,d,e)`。含孤立 t 的两项分别为 `(m−1)E0` 与 `(m−1)D0`，另两项是 B、C；正因子 m−1 消去，得到

`B E0 <= 2 C D0`。

这是完整扩张计数的恒等因子化，不是把父偏序的条件剩余词误作等权。也没有给 t 继承原 degree cap。

### (B) C² >= Z V0

在 Q=P−v 中，c1,d 极小，D_Q(c2)={c1}，D_Q(e)={d}。第一条给

`C² >= e(P−{v,c1,c2}) V0`。

C2 中 v 在 P−{c1,c2} 的每个其余点之前，因此 v 必为首项，`e(P−{v,c1,c2})=Z`，得所述式。

### 精确前缀解释

以 c1 为 pivot，其不可比集恰 Y={v,b,d,e}，关系为 v<b,d<e。条件 c1 前恰2点时，两个前缀集合 `{v,b}`,`{v,d}` 的权重为 B、C；恰3点时，`{v,b,d}`,`{v,d,e}` 的权重为 **2D0、E0**。2 是内部前缀扩张数，不可丢弃。包含耦合要求

`B/(B+C) <= 2D0/(2D0+E0)`，恰与(A)等价。

所以该式约束了首处分叉两条支路跨秩的真实重加权；不是已被 E08 反驳的 B<=Z。

### 现有实例诊断与准确缺口

附带脚本仅重算已归档 E08/E13/E16/E17 的上述六个删除数，不做新穷举。全部满足两式。特别 E17：

```
B=84, C=126, D0=60, E0=30, Z=35, V0=50;
BE0/(2CD0)=1/6,   ZV0/C²=125/1134.
```

但 E17 的原概率为 q0=9/29<1/3、p(c1<d)=97/145>2/3，指定两对菜单仍全不平衡。故(A)(B)即使有真实可实现性，也**不能单独推出该菜单**。E17含旧VG/模块，非已筛尽的A5残余，也非全局猜想反例。

待补桥仍是：将这些跨删除/跨秩约束与**同一原P**的多对事件、degree预算或净坏质量 E−G 联结，导出一个改变见证的原偏序出口。目前无此证明。仅再加两个二次不等式不算残余闭合。

## 2. 同下集 H 的首次命中：精确适用域

来源：J. Leake–K. Lindberg–S. Oveis Gharan, *Optimal Trickle-Down Theorems for Path Complexes via C-Lorentzian Polynomials…*, arXiv:2503.01005v3，2025-12-08 版本，Definition 1.18、Theorem 1.20、§6.2.2。
https://arxiv.org/html/2503.01005v3
状态：本轮读取定理、定义与专门推导入口；**预稿定理，未独审整套谱/Lorentzian证明**。摘要笼统称证明Chan–Pak猜想，不能替代正文限制。

H称P-consistent，若 a,c∈H、b∉H、b<c，则 a 至少与 b,c 中一个可比。
若 H 是相同严格下集的反链，则 b<c∈H 蕴含 b∈D(c)=D(a)，故 b<a；条件自动成立。

令 `M_k=# {L∈LE(P): min_{h∈H} rank_L(h)=k}`。该定理给 `M_k²>=M_{k−1}M_{k+1}`，原文显式范围为 n=d+1、2<=k<d。对|H|>=2，k=n−1的缺失边界因M_n=0自动成立；单点用经典Stanley即可。

**可实际尝试的接口：** 在共同下集候选群中，除了逐点秩曲线，记录每个非空子群的首次命中计数 M_k，并作为真实权重模型的一致性约束。若条件在一个真实已排前缀 ideal J 上且 J∩H=∅，剩余 H 在 P−J 仍同下集，因此可在该真正均匀剩余偏序使用；不得对任意人工事件/自由混合律宣布继承。

**不能扩张：** 同文Lemma1.17的 P={a}⊔(b<c<d)、H={a,d} 有首次秩计数(1,1,2,0)，在k=2失败。T11的 `{d}∪S` 往往恰不consistent：c1<s，而d同时不可比c1,s。因此这个定理不是任意E/G首次坏点的自动控制。它也不直接控制 H 中哪一个标签先出现，更不独自给1/3阈值。**M_k的k是完整原P中的秩；删外部标签后的核心词秩不保真，不能把该LC直接加到只存核心相对顺序的人工law。要先保留原秩/前缀统计，或给出其投影保持证明。**

## 3. 前缀包含耦合：待独审的广义工具

来源：J. T. Virtanen, *An inclusion coupling of prefix laws and the Chan–Pak rank inequality for all finite posets*, arXiv:2610.25227v1，2026-10-18。
https://arxiv.org/html/2610.25227v1

作者Theorem6.1声称：固定pivot x，条件rank(x)=p+1的前缀集合律

`mu_p(I) = e(P[I]) e(P−I−x) / N_{p+1}`

在相邻可行p上存在仅添加一标签的包含耦合；Cor6.3可拼成整个嵌套链。其随机加入顺序**不宣称在LE(I(x))上均匀**。

本轮逐读了§3因子化/端点Fishburn、§4细致平衡/连通性、§5五类联合跳率/非负预算及§6平稳律边际论证，未在这一段定位到具体缺口；这不是独立同行审查或整篇正确性背书。作者整体rank不等式、§7等号/缺陷与穷举附录未被本轮完整独验。精确跳率本身需要扩张数，原文也不声称高效采样。

附录声称提供anc/check_generator.py和anc/verify_chan_pak.py；本轮尝试直接读取附属文件URL均返回cache miss，**未取得代码字节、未重跑作者的全阶数计算**。不是权限拒绝。普通GitHub搜索未找到一个比上述原始论文更直接、可核保真映射的独立实现，因此没有拿无关实验仓库充作数学证据。

## 4. 已核但不优先的工具/误用边界

- Chan–Pak–Panova的[交叉乘积论文](https://www.cambridge.org/core/journals/canadian-journal-of-mathematics/article/on-the-crossproduct-conjecture-for-the-number-of-linear-extensions/044B8106B0B02D7C13219FA9AE438EDF)给真实三标签间隔计数的弱CPC及反向界，并反驳其更强广义CPC；不能从该文借到系数1的普遍TP2，也不能把正gap数组不等式直接施加到有符号E−G或任意外词混合。
- 同pivot FKG、Fishburn、序多面体等体积单纯形已存在于恢复v45/本地来源；本轮不把再次找到它们计新成果。连续坐标正相关不等于离散秩两变量任意相关，投影掉核心标签时必须保留插入体积/完成数因子。

## 5. v45对账范围与停止结论

已读当前`readable_current`定向条目，并扫描`偏序研究-v45逻辑体系索引.zip`中去重的.md/.tex/.txt/.html文本（单文件<=2MB）。已核旧档案明确使用：
- `advance_c1_private_activation_20261028/DELAYED_ACTIVATION_MOTHER.md` §末：Chan–Pak Thm1.1；
- `analyze_pendant_deck_witnesses_20261027/PROOF.md`及独审：两极小删除上/下界；
- `POSTRECOVERY_MECHANISMS.md` §同pivot部分：真实e(I)e(P−I−x)权重、Fishburn与FKG；
- `MECHANISM_PROOFS_68_72.md`/`PROOFS_87_88_ZH.md`：有限n Fishburn、单点rank/ideal-marker survival。

未在该次定向检索中找到Cor3.10/3.11、unique-cover四删除式、2503.01005/2610.25227的显式接入。**这不是证明旧母定理逻辑上不包含它们，也不是外部优先权或原创性结论。** 未把分片.bin内容当作已逐篇阅读。

建议只保留一个接续动作：对一个确实存活、具有共同下集群且保存完整原秩/前缀统计的真实权重模型，加入“子群首次命中LC”与四删除关系，检查它是否否定当前人工强向量；若仍可行，应报告一致性层未闭而不是继续宣称逼近分类。当前没有证明新增全局覆盖。
