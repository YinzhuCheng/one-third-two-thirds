# S77 · 文献前沿、覆盖关系与读取边界

核查日期：2026-10-01。这里区分作者公开陈述、已发表结果、项目继承的逐段笔记、本轮实际读取；不把所有项目草稿都称为原创，也不把预印本标题中的Proof当作独立认证。

## 1. 当前最重要的外部节点

| 键 | 文献/版本 | 与本项目有关的内容 | 应怎样使用 |
|---|---|---|---|
| ACPP26 | Aires–Chan–Pak–Panova, *Breaking the Infinite Barrier in the 1/3–2/3 Conjecture*, arXiv:2609.30888，2026-09-25首次提交 | 在BFT常数c=(5−√5)/10上给统一ε>0 | 一般正改进已有前沿；S50–58实际借用其分类/残差/选点。不能说直到现在BFT仍是未被改进的现行界 |
| AIRES26 | Aires, *Proof of the Kahn Saks Conjecture*, arXiv:2609.30895，2026-09-25首次提交 | 作者证明大宽度迫使δ趋近1/2，并给两类近均匀图案 | 与AKV25合用将大不可比度排除；不需要把整篇放进每个特殊族证明 |
| AKV25 | Aires–Kahn, *Variance vs. range for linear extensions, and balancing extensions in posets of bounded width*, arXiv:2510.26134v1，2025-10-30 | Thm1.3 π大⇒某处方差大；Thm1.5 固定宽度、大方差标签有近半伙伴；Thm1.6 固定宽度＋π大⇒全局近半；Thm1.7 KS⇒一般π版本 | 大参数定性渐近已涵盖固定模板膨胀。Thm1.3的方差大点不必是原来π大的点；Thm1.6不定位任意预选模块 |
| AKW25 | Aires–Kahn, *Balancing extensions in posets of large width*, arXiv:2509.11549，2025-09 | 大宽度/高度及窗口工具，带各自范围假设 | 新KS主定理覆盖部分定性目标，不能丢掉其概率窗口工具；特殊域的1/e不能说成所有偏序统一1/e |
| HAQI26 | Haqi, *On the Gap of Finite Posets*, arXiv:2608.12678，首发2026-08-13；项目旧账本记录v2为09-02 | 全体平均秩的gap≤2w−1；同时有每条极大链平均秩gap都很大的宽度二反例 | 全局平均秩密集不等于存在一条均匀好链，更不等于最近均值对平衡；理想权重可用，强选择器不可偷用 |
| GUPTA26 | Gupta, *Balance Constants, Majority Cycles, and the Gold Partition Conjecture through Fourteen Elements*, arXiv:2607.23926v2，2026-07-30 | 作者报告14点无标号普查、Gold Partition及1/3验证；128个等号类皆为指定序和族 | 是外部计算报告，未由本项目重跑。不能排除n>14的对象，不替代结构归约 |
| VHYZ24 | van Handel–Yan–Zeng, *The extremals of the Kahn-Saks inequality*, Advances in Mathematics 456 (2024),109892；arXiv:2309.13434 | 秩差对数凹序列的等号/几何级数结构刻画 | 为近等号路线提供结构目标；等号刻画不自动给近等号稳定模量，也不能只凭矩接近推断偏序接近 |

ACPP作者说明给出的显式ε下限是3^(−3^(16×10^18))。它的尺度不代表离1/3还差多少结构步骤；其意义是严格利用有限性跨越旧的“无限障碍”。本轮不声称精算该巨大常数或新论文全部推导。

## 2. 旧文献与项目接口的归属

**Zaguia（1610.00809v3，2017）**：good/very-good pair与近自治情形是S72–74的定性基础。两侧全链的存在性、S74尾部族的定性1/3、十点模板的全十参数定性1/3不能重新认领。S73–74另行提供了允许分叉的充分条件、窗口和定量族，是否已有等价表述仍需查新。

**Bergman（1802.01712v2，2018）**：词典序和、链替换的扩张计数属于已有研究。项目S68账本定位到Theorem13/Corollary16的多项式性与次数。本轮只复核原作者摘要/机构存档，不将其定理全文作为重新审查完成。sign-imbalance是扩张奇偶符号差，不是δ的同义词。

**Chan–Pak（2212.11954；Pacific J. Math. 323 (2023)）**：Fishburn、多变量P-partition与四函数框架提供真实权重相关约束。它们并不授权把任意所需的原线性扩张cross-product猜想当作已证一般定理；应按具体版本核对。

**Sah（1811.01500v2；Combinatorica 41 (2021)）**：宽度二排除已知序和等号族后有(-3+5√17)/52的统一改进。另有β≈0.348843的极限构造及可能最优性的讨论。项目R55–56记录的反例针对后一个具体最优性猜测，不针对已发表下界，也不反驳原猜想；该反例稿自身仍需按原文审查。

**Chan–Pak综述（2311.02743v2，2025）**：适合建立历史定理地图，不应把2025综述的“最新状态”覆盖2026新进展。

## 3. 必须恢复的继承关系

S68的06文献账本已登记ACPP26、AIRES26、HAQI26；S50的AUDIT.md还记录了关键量词、条件化及边界修补。本轮不是第一次发现这些文献。近期S75/S76重点聚焦局部模块，导致最新数学叙述没有充分承接旧文献链；S77补齐这一点。

S50旧审查明确区分：

    ACPP一般ε改进：小π / 大宽度 / 有界宽度大π的组合
    Aires完整KS + AKV Thm1.7：所有大π均近半

前者不需要后者的完整KS主定理。项目U58后期链也不以完整KS为必要输入。依赖图不能画成相互循环。

旧审查还对AKV的零方差、空集合、固定秩排字与条件化概率损失作了项目修补。这是历史审查意见，不是本轮发现作者正式勘误；也不是推翻主定理。若再以其精确常数作为新证明输入，需要明确重述修正后的引理。

## 4. 本轮实际读取层次及失败披露

- AKV25：成功读取HTML相关论证，PDF第2–3页截图核对Theorems1.3、1.5、1.6、1.7。未重新从头认证整个困难方差证明。
- ACPP26、AIRES26：成功核对一手arXiv检索摘要与作者署名、提交时间；ACPP另核对Pak作者说明。直接重新打开9月两篇的arXiv正文/全文入口反复Cache miss，未完成本轮全文重读。细节审查只继承S50账本，并标为历史记录。
- HAQI26：成功得到一手摘要和作者主页条目；v2日期来自旧账本，本轮未独立核对其完整版本页/证明。
- GUPTA26：成功读版本页及HTML有关结果；未复跑1,338,193,159,771类普查。
- Zaguia：成功读arXiv版本页、摘要；PDF提取部分可见，但本轮截图失败，具体经典接口结合既有项目原稿使用，不声称此次重审全篇。
- Sah、Bergman、Chan–Pak、VHYZ：复核一手摘要、出版社或机构元数据及相关研究位置，不声称逐行重建每份证明。

因此本文使用“按文献陈述”“采用所述定理后”的表述。找不到本轮可读全文不等于文献不存在，也不等于可以用二手摘要填补证明细节。检索未构成对全部2026文献的穷尽查新。

## 5. 一手入口

- ACPP26: https://arxiv.org/abs/2609.30888
- Pak作者说明: https://igorpak.wordpress.com/2026/09/25/how-to-make-small-improvements-and-break-barriers/
- AIRES26: https://arxiv.org/abs/2609.30895
- AKV25: https://arxiv.org/abs/2510.26134 ; https://arxiv.org/pdf/2510.26134
- AKW25: https://arxiv.org/abs/2509.11549
- HAQI26: https://arxiv.org/abs/2608.12678
- GUPTA26: https://arxiv.org/abs/2607.23926v2
- Zaguia: https://arxiv.org/abs/1610.00809v3
- Bergman: https://arxiv.org/abs/1802.01712 ; https://escholarship.org/uc/item/4jn1t5v7
- Sah: https://arxiv.org/abs/1811.01500v2
- Chan–Pak相关性: https://arxiv.org/abs/2212.11954
- Chan–Pak综述: https://arxiv.org/abs/2311.02743v2
- van Handel–Yan–Zeng: https://arxiv.org/abs/2309.13434 ; https://doi.org/10.1016/j.aim.2024.109892

不附复制的外部论文全文；旧项目来源/审查文字按研究资料保留。
