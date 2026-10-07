# 文献与定理接口 · S98 · 2026-10-08

本表区分来源陈述、实际读取层级和本项目用途。历史更完整的文献条目继续保留于[HANDOFF_S96/LITERATURE.md](../HANDOFF_S96/LITERATURE.md)、[S77/LITERATURE_REVIEW.md](../S77/LITERATURE_REVIEW.md)、[旧总图](../06_LITERATURE_AND_THEOREM_MAP.md)。本轮没有把所有旧引用重新逐行审核，缺失原历史大包中的条目不靠记忆补造。

## 本轮直接输入

### CP-2024：首两步完成数矩阵

Swee Hong Chan、Igor Pak，Correlation inequalities for linear extensions，arXiv:2211.16637v2，2024-09-12。原文 https://arxiv.org/html/2211.16637v2 。

实际核对§6.1 Proposition6.1、(6.1)、Lemma6.2的矩阵陈述。给原偏序附加孤立标记、取k=2、限制到原极小元，得到首两步矩阵：非对角删去两个不同极小元；对角删去首个极小元后再删一个新放行后继。矩阵至多一个正特征值。S98§2.1逐项写出对应，而不是把任意删除数组当作此矩阵。

这是已有定理输入；原文进一步引CP24 Proposition14.9，不声称本轮重证整个atlas。其Theorem1.1的两侧相关界也是旧背景，不作为新纪录。

### OAI115：局部Pair summation，而非整套算法

OpenAI，Exact Uniform Sampling of Contingency Tables with Arbitrary Margins，稿件日期2026-09-24；固定发布源码版本`adc7f1241b42e322a6451854ab7e4b4c146bf78a`。

https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Exact-Uniform-Sampling-of-Contingency-Tables-with-Arbitrary-Margins-September-24-2026/build/sections/signatures.tex

实际逐式阅读Pair summation中的正方向投影、共享相邻块和二次差分望远镜；S98在自己的端点E0>0、g0=0情形重推，并保留非负余项和线性权重。没有将偏序变成列联表；没有运行该文采样器或Lean验证；不能说整篇全部独立审计通过。原文任意矩阵之和不保持惯性指数的限制仍然保留。

目录115的精确采样与带cell bounds的FPRAS是不同范围；本项目无需将整套算法作为依赖。

## 当前研究干线的经典输入

|来源|准确用途|适用/读取边界|
|---|---|---|
|Shepp，1982 XYZ|同端点顺序事件正相关；S94的uv≤T≤min(u,v)，安全联合区间[1/3,4/9]；S97多私有候选迁移|经典定理；此前实际核对Pak2209.06142§6.4、Aires–Kahn2510.26134的陈述，不重新认领|
|Fortuin–Kasteleyn–Ginibre，1971|有限分配格上的增加事件正相关；S93非一致放行槽位控制|必须在真实合法槽位格证明条件；并非任意线性扩张分布都是产品律|
|Stanley，1981 Aleksandrov–Fenchel应用|单标签秩计数对数凹；辅助门点把E_j、C_j^z、D_j实现为秩计数，得到S96尾界|辅助偏序只用于同一整数序列性质，不能倒推原律；两个对数凹序列之和不自动对数凹|
|Chan–Pak，2024 atlas/相关式|共享多标签矩阵与条件删除量|S98借其已知首两步输入，不认领新的普遍相关理论|
|Brightwell–Felsner–Trotter，1995|经典普遍常数c=(5−sqrt5)/10及三元组几何框架|U58依赖链尚待审查，末端有理数优化不能认证全证明|

## 结构类与外部渐近背景

Sah，1811.01500v2：宽度二及排除等号族后的改进；不是全部宽度三。Zaguia，1610.00809：覆盖图森林类的定性结论；同属该类的项目例子不能重新认领类别突破。Peczarski的thin结果控制最大不可比度，不是参考跨度。Fishburn/Tanenbaum/Trenk等的linear discrepancy与不可比图带宽关系用于S62精确查重，不能把参数名近似就视为同一定理。

Aires–Kahn，2510.26134v1：固定宽度、最大不可比度增大迫使全局δ趋1/2。TEN40定性多尺度趋半由此已有背景，项目应保留有效截断/标签定位/2/5全域尚缺范围。2026-09 ACPP2609.30888及Aires2609.30895的状态与精确定理以当次源核对为准，不将全部摘要或第三方TLDR当认证定理；S98主结果不依赖它们。

Bergman1802.01712：词典序和/链替换计数背景；项目新公式要标清有限标签与原律，不重新认领基本插回。

## 新发布中暂不作主输入的来源

169自然单位区间图e-positivity的置换过程类别受限，不能直接覆盖含3+1的当前入口模型。093次高斯对数凹LSI需要统一线性次高斯参数，序多面体有界不自动提供所需无维数控制。091对数Brunn–Minkowski有中心对称性假设，一般序多面体不满足。标题带one-third的Brenier稳定性与原猜想的1/3概率阈值不是同一问题。

## 依赖纪律

网页/目录可更新；存固定版本、定理号、假设与读取层级。调用工具成功不代表论文正确，有Lean目录也不代表本轮已编译审计。S98当前可信链条是“明确CP背景定理 + 本稿可逐式检查的合同与望远镜”，不是“OpenAI发布很多数学证明所以本命题已获证明”。
