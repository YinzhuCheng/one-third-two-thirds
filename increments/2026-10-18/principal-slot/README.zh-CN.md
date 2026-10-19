# principal 辅助槽界：证明、独审与结构范围小增量

日期：2026-10-18。本文是本轮五项新增机制结果的概览；原 1/3–2/3 主猜想仍未解决，原主目录 35/55 不增加。本包不重复此前四个已交付研究包。

## 一、已证且独立审核 PASS

U 为任意有限非空偏序，f 为其全部完整线性扩张上的均匀随机秩。对实际非空上理想 S，R_S 是首个 S 元素前的点数；设 r=E R_y、s=E R_z、N=E[R_yR_z+min(R_y,R_z)]。

- 两个上理想均 principal 时，N ≤ rs + min(r²+2r,s²+2s)。生成元可相同、可比或不可比；n=1 与零均值边界均包括。
- 一侧 principal 时，可控制该侧：若 R_y=f(x)−1，则 N−rs ≤ r²+2r。另一侧可为任意非空上理想，证明实际允许任意非空子集。
- 因而 principal 恰在较小均值侧 r≤s 时，也得到目标 min 界。仅较大均值侧 principal 时，不能凭本证明获得较小侧界。
- 证明链：Shepp 差坐标有限分配格 FKG → 在 U 下方序和 C_k → Beta(k,n+1) 分解 → 固定 U 取 k→∞ → 次序统计量精确离散转换 → Chan–Pak Theorem 1.2 的单点对角界。
- 独审结果为 PASS；一般证明是结论依据，小模型 exact 检查仅控制符号、偏移和边界。没有据此证明更强 Cov 候选。

## 二、精确实验，不能当证明

大参数原计划 33 对象，实际测试 31 对象、5,073 个 filter 对，n=20…200。30 对象完整完成，另 1 对象完成 49/64 对；最后 2 个计划对象未开始。按预算在 29,964,136 pair×ideal-state 停止。本次打包没有重跑或补算。

全部已测对子均未发现 T 或 Cov 反例。每一对的矩来自实际 U 的全部完整 LE 的任意精度整数计数；随机性用于选择对象、filter 池和对子，没有随机抽 LE，没有 Monte Carlo。有限、定向样本不证明任意 U 或任意 filter 对的全称结论。

原实验及结构报告写作时 principal 证明尚未独审，因此原文件、原状态字段中的“未证”“待独审”保留为历史记录。后续独审已 PASS，当前已证范围以本概览和独审报告为准；一般 T、一般 Cov 仍未证。

## 三、5,073 对的结构标签与剩余障碍

互斥分类：含空 filter 64；both principal 855；仅较小均值侧 principal 517；仅较大均值侧 principal 1,319；both nonprincipal 2,318。

- 非空对子中 855+517=1,372 对命中新 T 证明条件，其中 90 个为对角对子；含空类另有 11 对命中已证单侧的均值条件。
- 1,319 个“仅较大侧 principal”和 2,318 个“both nonprincipal”共 3,637 个非空对子没有命中本证明条件。这是本证明的范围标签，不声称它们不受其他结果覆盖，也不把零均值平凡例当作新的困难。
- 剔除对角及零均值后，3,217 个正均值、相异非空对子没有命中新证明条件。
- 最紧相异非空例仍在证明条件之外：U=C₁⊔C₁⊔C₁₉₈，S_y={b}∪C₁₉₈ 为 nonprincipal，S_z=C₁₉₈ 为 principal；r=1/200<s=2/199。T 压力 79400/79799，Cov 压力 13200/13333；两绝对余量均为 399/7960000。较小均值侧是 nonprincipal，不能因另一侧 principal 而误归入覆盖范围。

## 四、clone/subset 路线：确切翻译，未闭合一般目标

取 d=E[R_z·1_{R_y=0}]、e=E[R_y·1_{R_z=0}]，L=N−r−s+d+e。Chan–Pak 的 minimal-subset 事件计数可推出：

N ≤ r+s−d−e+2(r−e)(s−d)，以及 (r+s−d−e)² ≥ (d+e+2)L。

三 clone 的两个 all-U 控制为 N≤2(r+1)(s+1)、2N≤(r+s+2)²。它们没有补齐一般不等均值的 T；实际槽的边界修正可以同时为零。该路线是可复用精确恒等式与有界机制分析，不是 T 已证，也不是断言所有 Chan–Pak 迭代路线都不可能成功。

## 五、原始论文链接

- L. A. Shepp, The XYZ Conjecture and the FKG Inequality, Annals of Probability 10(3), 1982, 824–827。DOI：https://doi.org/10.1214/aop/1176993791 。原始扫描：https://repository.upenn.edu/server/api/core/bitstreams/dc03f00d-299d-45e9-b52a-4c98a8026617/content 。本包只链接，不收录原扫描、OCR 或页面图像。
- Swee Hong Chan and Igor Pak, Correlation inequalities for linear extensions, Advances in Mathematics 458, 2024, 109954。DOI：https://doi.org/10.1016/j.aim.2024.109954 。作者稿：https://www.math.ucla.edu/~pak/papers/Correlation17.pdf 。arXiv 原文：https://arxiv.org/html/2211.16637v2 。principal 证明使用 Theorem 1.2 对角特例；subset 路线使用 Theorems 1.9–1.10。
- Max Aires, Proof of the Kahn–Saks Conjecture, arXiv:2609.30895v1，定位线索：https://arxiv.org/html/2609.30895v1#S2 。本轮 principal 证明不以其主定理承重，也不据标题认定本研究主猜想已解决。

## 六、归档内容与恢复

保留五个原目录中的证明/报告、独立核验源码与精确输出、必要 C++/Python 源码、实验固定计划、实际对象/filter、5,073 对完整整数矩、结构标签与汇总。本包仅新增本轮机制结果，不纳入旧历史包、原论文扫描、OCR、图像、编译可执行文件、缓存、软件包、聊天或凭据。文件清单见 MANIFEST.json；打包只检查文件清单，没有重跑大计算，没有计算散列。

本包代码按原样留存，未作便携化改写。前三个小证明/独审/翻译脚本可在其目录单独运行；大参数 run_stress.py 的旧夹具核对以及 scope 的旧小批次标签段依赖先前已交付的小批次文件及原路径。不要以缺少旧包为由复制旧包到本增量。已保存的 input.txt、objects.json、raw_results.jsonl 与汇总足以查阅本轮所有精确样本和范围；代码如何恢复运行见原报告。任何重算属于单独工作，不是本次归档验证。
