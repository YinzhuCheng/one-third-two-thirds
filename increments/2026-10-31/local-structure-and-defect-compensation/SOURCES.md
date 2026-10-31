# 来源与归属（应在对外引用前逐条复查版本）

本清单反映本轮原研究记录实际核查报告；本包编写阶段没有重新联网下载所有文献。

| 来源 | 本轮用途与限制 |
|---|---|
| [Zaguia, arXiv:1610.00809v3](https://arxiv.org/html/1610.00809v3)，Order 36 (2019) 335–347，[DOI](https://doi.org/10.1007/s11083-018-9469-0) | 好对给全局平衡；非常好对；近自主删除一/两点；Lemma 7 临界交换。T03/T04 应明确标为组织/推论，不抢占基础技术优先权。 |
| [Olson–Sagan 作者发表版](https://users.math.msu.edu/users/bsagan/Papers/Old/otc-pub.pdf) | almost twin 与 very good 对照；自同构交换概率 1/2。好对结论不必指定原对本身平衡。 |
| [Dolores-Cuenca–Guzmán-Sáenz–Kim, 2410.12494v2 §2](https://arxiv.org/html/2410.12494v2#S2) | 模块/词典和计数：内部形状给乘积常因子，链替换保持模块外事件。不能直接用于非自主的六点核心。 |
| [2601.14482 §4.1](https://arxiv.org/html/2601.14482#S4.SS1) | 模块分解的交叉来源；所追溯 Habib–Möhring 1987 原文尚未读，不可标为已核。 |
| [Stanley, Two Poset Polytopes (1986)](https://math.mit.edu/~rstan/pubs/pubfiles/66.pdf) | 阶序多面体等体积单纯形、volume=e(P)/n!。T05 的连续化桥梁是经典事实。 |
| [Aires–Kahn, 2509.11549](https://arxiv.org/html/2509.11549) | 极小点局部渐近结果与条件均匀窗口；不是固定 3/4/5 点阈值的现成替代；宽度≥3 严格平衡为猜想，勿写作定理。 |
| [Breaking the Infinite Barrier, 2609.30888v2](https://arxiv.org/abs/2609.30888v2) | 2026-10-28 版；用户已知有界不可比度改进 (D+1)^[-3(D+1)]/12。D=9 为 10^-30/12 加经典基线。作者预稿主张，不是一般 1/3–2/3 证明；本包未复核全文。 |
| [Peczarski 2017 作者文](https://cdm.ucalgary.ca/article/download/62349/46785/178291) | Gold Fact 2 中 at most one slave 不能改成两个；2006 原 PDF 未读到。 |
| [Trotter–Gehrlein–Fishburn 1992](https://trotter.math.gatech.edu/papers/82.pdf) | 高度 2 局部差集工具，不自动给本包共同下集阈值。 |
| [6-thin DOI](https://doi.org/10.1007/s11083-008-9081-9)，[5-thin DOI](https://epubs.siam.org/doi/abs/10.1137/0405037) | 全文未取得或仅摘要；全局每点度数限制与指定小集的局部度数限制不同，不能直接宣称包含关系。 |
| [Eppstein 2013](https://arxiv.org/pdf/1302.5967) | 无平衡下强概率关系的传递性为已知技术。 |
| [Furman–Kye–Su 2019](https://doi.org/10.1016/j.econlet.2019.108753)，[Gasparini–Sacchetto 2020](https://link.springer.com/article/10.1007/s40300-020-00191-5) | 长度偏置与 Gini/比较概率联系；T05 截断仿射核是本轮从已知工具推导的应用，不是这些论文的原文定理。 |
| [Dümbgen–Mösching](https://arxiv.org/pdf/2209.07868) | 单调似然比推出随机序的标准工具。 |

## 待核查优先权
没有找到 T01 的三个精确局部阈值或 T05 的完整并集覆盖条件的直接同款定理，**不等于证明原创**。T02 置换机制也需查已有同下集/签名论文。T03/T04 的本质基础已知。当前只宜称“本轮整理/推导的命题”。

## 矩约束迁移（可保留但未落实成排除）
2609.30888v2 §5.4 的连续秩相关工具可转写为真实线性扩张秩差 D_xy：μ_xy=E D_xy，M_xy=E(D_xy²+|D_xy|)，
`dev²=(n+1)/(n+2) M_xy−μ_xy²`，并有
`(n+1)/(n+2)(M_xz−M_xy−M_yz)≤2μ_xy μ_yz`。
它是候选概率/矩模型的可实现性约束；本轮还没有靠它排除剩余 C2，不能写作已完成贡献。

## 用户研究的固定提交入口
[2026-10-19 START_HERE，commit 16ccf90a54f61cf6f4f4a21cd32c1ee717cfc9a0](https://github.com/YinzhuCheng/one-third-two-thirds/blob/16ccf90a54f61cf6f4f4a21cd32c1ee717cfc9a0/increments/2026-10-19/START_HERE.md)。本轮研究汇总记录已核查 S112 的混合强迫环归属。其余旧条目不能只凭标题当作完整证明；S82 原字节尚未恢复。


### T12 模块定位的文献限定（已核来源）
虽然 T12 强迫自治二元链 {d,e}，**不能自动推出已被旧模块定理解决**。
- [arXiv:2410.12494v2](https://arxiv.org/html/2410.12494v2) Theorem 3 / Corollaries 2–3 的传递入口是某个替换因子已有 Gold Partition 性质或平衡对。二元链的 balance constant δ=0，不能触发该入口。
- 同文 §3 仍把素商的正整数链膨胀作为待处理难点，不能用“有模块就可压缩”略去权重和链膨胀障碍。
- 用户公开档案 S112 §7，以及 2026-10-19 `global-counterexample-map` §3，把 G/G+ 消除真链模块列为未证。固定入口：[START_HERE](https://github.com/YinzhuCheng/one-third-two-thirds/blob/16ccf90a54f61cf6f4f4a21cd32c1ee717cfc9a0/increments/2026-10-19/START_HERE.md)。这些已核定位由本轮研究汇总记录提供；本包不补造未读取的文件字节。
因此准确定位是：T12 不属于无模块残余，但当前已核模块理论 **不自动覆盖该子域**；全面文献重合仍未知。既不能包装成模块素突破，也不能仅凭发现模块就删除其数学内容。

## T13当前有限文献/候选对照
本轮研究汇总记录报告独立检查：E16的全39个good-pair候选弧对应概率均>1/2；Zaguia Theorem 3、Olson、Gold的有限条件对照未直接包含该实例/准则。这里只记录本轮有限对照，不等于穷尽文献或证明原创。39弧的完整清单/独立日志尚未归入本包，避免冒充建档阶段重验。

### 建档追加核验39弧
现已独立重算：39是正向/对偶好对候选有向边的并集数（仅正向为27），39条均概率>1/2。完整弧及有理概率见`E16_GOOD_PAIR_VALIDATION.json`，脚本`verify_e16_good_pairs.py`。这只核查直接候选，不证明历史全部工具不覆盖。

## Notion归属对账（覆盖此前未查明状态）
T02被既有研究台账 AV-7C（本轮已核对；此处不转载私人工作台全文）完整包含；T01三点inc≤5被既有SAME-P MIW三根上例外≤3直接涵盖。两者标既有推论，不计本轮新定理，保留独立短证明。T01四点inc≤9、五点inc≤15经v45有限对照，已检范围未发现同式、历史排重未完，原创性未确认。T03混合强迫图继续归既有S112。本包记录本轮研究汇总记录对账结论，未冒充建档者直接读取Notion全部原文。


## 研究归档 v45 的有限对照（2026-10-31）

此次已恢复并读取 v45 当前接续正文与有效索引；没有将大归档、私人页面或内部路径转载到本增量。有限对照更新此前“等待 v45”的阶段状态：

- SAME-P MIW 的原条件为 a=3 时 q≤3、a≥4 时 q≤a+1。在不另计中性点信用的局部度数换算下，四根为 inc≤8、五根为 inc≤10，不能据此包含本包四根 inc≤9、五根 inc≤15。三根 inc≤5 则已被旧结论覆盖。
- T02 完整归既有 AV-7C，T03 归既有 S112。
- 四/五点阈值、T05/T07 和 T10–T13 只可说“已检范围未发现同式、历史排重未完”；关键词及当前索引未命中不能证明原创。
- v45 中 R3/R4 归 fullT2，即完整 T={b,d}；本包是 fullT3，即完整 T={b}⊔{d<e}。旧 fullT2 的固定闭合与必要类型不能自动用于 fullT3；同名 C2 或相同 |A| 不足以建立覆盖。
- 旧一般 C2 strong-first 在无平衡反设下仍可剩 Min(T)={b,d}、1≤|A|≤6、2≤|T|≤8−|A|。本包 |A|=5、|T|=3 落在该必要范围，只说明该概括排除未直接关闭此域，不等于全部细分门已查重。

历史证明字节与审查回执仍有缺失，因此不声明全历史恢复或无重复认证。
