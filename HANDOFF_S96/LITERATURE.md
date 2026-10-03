# 文献—定理—项目接口 · S96

本页不是穷尽书目。原S82大包里的完整旧BibTeX和逐次阅读笔记尚未取回；根目录06_LITERATURE_AND_THEOREM_MAP.md及S77/S80/S81原账本保留。用户ZIP另有27条详细记录的literature.json/tsv和参考BibTeX，逐条写明作者、版本、可用结论、项目接口与读取边界。

**读取陈述不等于重审证明；摘要不等于完整定理。** 2026预印本的旧读取和本轮抓取失败分别注明。S96只使用Stanley单标签秩对数凹及S95真实前缀计数，不以2026前沿论文或U58为证明输入。

## 1. 当前共享完成数路线

### Stanley1981：单标签秩对数凹

R. P. Stanley, Two combinatorial applications of the Aleksandrov–Fenchel inequalities, JCTA31(1981),56–65。单标签秩计数N_k满足N_k²≥N_(k−1)N_(k+1)，单标签版为原Thm3.1；固定其它链标签秩的推广见Thm3.2。

本轮核对两个一手重述：
- Chan–Pak, Correlation inequalities for linear extensions, arXiv:2211.16637v2, Thm1.3，明确引用Stanley Thm3.1：https://arxiv.org/html/2211.16637v2 。
- Zhao Yu Ma; Yair Shenfeld, The extremals of Stanley’s inequalities for partially ordered sets, arXiv:2211.14252v2(2023),§1.2 (1.1)–(1.2)，引用更一般Thm3.2：https://arxiv.org/abs/2211.14252 。

S96门点实现使前缀完成数成为这种秩计数；这是已有定理应用。没有重新证明Alexandrov–Fenchel，也不把等号分类自动变为近等号稳定性模量。Ma–Shenfeld实际读到PDF文本，截图请求失败。

### Shepp XYZ及Pak的明确陈述

Shepp1982的XYZ：三个两两不可比标签a,x,y满足Pr(a<x且a<y)≥Pr(a<x)Pr(a<y)。Pak, What is a combinatorial interpretation?, arXiv:2209.06142v1 §6.4（PDF第17页）给计数/概率式和归属：https://arxiv.org/pdf/2209.06142 。

项目用途：S94安全联合区间[1/3,4/9]，S95实际避入口链选择。S96几何尾证书不需要XYZ；MC3问题的背景使用它。未重审Shepp原证明。

### Chan–Pak2024相关不等式

Swee Hong Chan; Igor Pak, Correlation inequalities for linear extensions, arXiv:2211.16637v2(2024-09-12)。Thm1.1：n>2且x,y极小时，n/(n−1)≤e(P)e(P−x−y)/(e(P−x)e(P−y))≤2，下界归Fishburn、上界归该文。

Thm1.9/1.10给不交极小元集合首两位事件的相关约束，可能用于S96下一步共享删除计数。必须按原文主上集定义使用，不猜省略项。该文Conjecture1.5是扩展Stanley猜想，不能当已证群体首出现对数凹。本轮读HTML陈述，未重审atlas证明。

https://arxiv.org/html/2211.16637v2

### FKG及双链单调性

Fortuin–Kasteleyn–Ginibre, Correlation inequalities on some partially ordered sets, CMP22(1971),89–103，DOI10.1007/BF01651330：有限分配格与log-supermodular权重，同向单调函数正相关。

Björner, A q-analogue of the FKG inequality and some applications, arXiv:0906.1389v3 Thm1.1重述经典版本。S93实际读第2页并截图；S96仅核对元数据。项目用q=1，不认领其基础原理：https://arxiv.org/abs/0906.1389 。

Graham–Yao–Yao, Some Monotonicity Properties of Partial Orders, SIAM J. Algebraic Discrete Methods1(3)(1980),251–258，DOI10.1137/0601028；Shepp, The FKG Inequality and Some Monotonicity Properties of Partial Orders，同卷295–299，DOI10.1137/0601034。S93只读出版社摘要/元数据。固定双链或纤维的单调性不能外推为任意P逐次追加比较时所有目标概率同向移动。

### 相关背景，不重复计作新工具

Chan–Pak, Log-concave poset inequalities, arXiv:2110.10740v3；Journal of Association for Mathematical Research2(1)(2024),53–153。本轮核对摘要/发表元数据；有组合线性代数重证Stanley与等号背景，未读全证明：https://arxiv.org/abs/2110.10740 。

Chan–Pak, Multivariate correlation inequalities for P-partitions, arXiv:2212.11954；Linear extensions of finite posets, arXiv:2311.02743。分别是多变量相关性与综述入口，本轮以摘要/历史笔记为限，不把未证cross-product加强当作工具。

## 2. 与全局1/3猜想的关系

### Aires–Kahn固定宽度大不可比度

Aires; Kahn, Variance vs. range for linear extensions, and balancing extensions in posets of bounded width, arXiv:2510.26134v1。

本轮读到HTML相应定理：1.3大π迫使大秩方差；1.5固定宽度的大方差点有近半伙伴；1.6固定宽度且π→∞推出δ→1/2；1.7与Kahn–Saks猜想连接。

用途：width3可优先研究π有界但n无界；十模板的最大模块增长使π增长，因此全局渐近近半已有归属。它不定位任意预选模块，也不代表已提取实用有限盒界。

https://arxiv.org/html/2510.26134v1

### Aires–Kahn大宽度

Balancing extensions in posets of large width, arXiv:2509.11549v1。宽度、高度或反链等条件下近半/1/e−o(1)结论；例如Thm1.7须宽度远大于sqrt(n)或高度o(n)。不能写成所有有限偏序统一1/e。本轮核对HTML条件，不重审全部证明。

https://arxiv.org/html/2509.11549v1

### 2026前沿条目：保持读取等级

- Aires–Chan–Pak–Panova, Breaking the Infinite Barrier in the 1/3–2/3 Conjecture, arXiv:2609.30888，首发2026-09-25。作者声明BFT常数(5−sqrt5)/10之上有统一正改进。S80历史上读过源引理片段；本轮可检索摘要，但直接arXiv正文抓取失败，不称全文独立认证。U58不因末端算数通过自动继承该结论。https://arxiv.org/abs/2609.30888
- Aires, Proof of the Kahn Saks Conjecture, arXiv:2609.30895，同日首发。作者声明大宽度使δ任意接近1/2。旧摘要/元数据记录保留，本轮直接原文未取到；仅研究width3可不引入这个更强依赖。https://arxiv.org/abs/2609.30895
- Alireza Haqi, On the Gap of Finite Posets, arXiv:2608.12678。摘要声明全体平均秩gap≤2w−1，并含最大链均值方面的反例；本轮核对一手索引摘要及作者目录，未读完整证明。不能从全体均值密集推出预选链或最近均值标签平衡。https://arxiv.org/abs/2608.12678
- Gupta, Balance Constants, Majority Cycles, and the Gold Partition Conjecture through Fourteen Elements, arXiv:2607.23926v2。旧账本记录14点有限计算声明；本轮一手抓取未成功，未取得独立证书，不纳入主证明依赖，也不把全14点枚举称廉价任务。https://arxiv.org/abs/2607.23926v2

## 3. 特殊类查重和参数边界

Ashwin Sah, Improving the 1/3–2/3 conjecture for width two posets, arXiv:1811.01500v2。宽度二及指定等号序和类外的统一改进；本轮读摘要，具体最优常数应对照正文。S65近链κ不是宽度。https://arxiv.org/abs/1811.01500v2

Imed Zaguia, The 1/3–2/3 Conjecture for ordered sets whose cover graph is a forest, arXiv:1610.00809。森林覆盖图类已有定性结论；一个新例覆盖图有圈只说明不被该单一类覆盖，不能代替全面查新。https://arxiv.org/abs/1610.00809

George M. Bergman, Some results on counting linearizations of posets, arXiv:1802.01712v2。词典序和、块形状因子、链替换计数背景；sign-imbalance是排列奇偶差，不是δ。S82/S87/S92的基础插回思想不重新认领。https://arxiv.org/abs/1802.01712

Fishburn–Tanenbaum–Trenk的linear discrepancy等于不可比图带宽，Rautenbach DIMACS2002-53作者摘要记录该等价。本轮读摘要而非FTT全证明。S62可精确查找“宽度≤3且ld≤5”，不能混同最大不可比度≤5。https://archive.dimacs.rutgers.edu/TechnicalReports/abstracts/2002/2002-53.html

Peczarski6-thin Gold Partition结果，DOI10.1007/s11083-008-9081-9。6-thin指每点最多6个不可比邻居，不是参考跨度≤6。本轮继承旧引用，未重审全文。

## 4. 窗口、等号与概率工具

van Handel–Yan–Zeng, The extremals of the Kahn-Saks inequality, arXiv:2309.13434；Adv.Math.456(2024)109892。秩差对数凹等号分类不自动给近等号误差速率，亦不等于S53小rho。本轮核对摘要/元数据。https://arxiv.org/abs/2309.13434

Klartag–Lehec, Poisson processes and a log-concave Bernstein theorem, arXiv:1802.04176v2。Laplace变换、交错Taylor系数对数凹和Poisson平均背景；本轮核对摘要。https://arxiv.org/abs/1802.04176v2

Langharst–Putterman, Weighted Berwald’s Inequality, arXiv:2210.04438v7；Indiana Univ.Math.J.74(1)(2025)。加权Berwald与等号背景；本轮核对元数据/摘要，S78所需全止损形式仍有独立论证责任。https://arxiv.org/abs/2210.04438

Strassen1965；Leskelä–Vihola, Conditional convex orders and measurable martingale couplings, arXiv:1404.0999、Bernoulli23(4A)(2017)。S79/S80凸序条件核背景，本轮继承记录未读全文，不能据边缘律识别P或随意独立拼接。https://arxiv.org/abs/1404.0999

NIST DLMF §5.12的Euler Beta积分及其它Gamma/Poisson恒等式是经典背景；S91等将它们用于有序交错原子，不认领新的特殊函数式。https://dlmf.nist.gov/5.12

## 5. 下一步读文献的范围

只围绕共享完成数缺口读Chan–Pak极小元集合的首两位定理和Stanley/XYZ的精确组合接口。不要扩大书目而不产生实际使用，也不要把每个相关论文都升级为必须先证明的更强猜想。旧文献笔记的继承读取层次与本轮实际取到的内容需分开。
