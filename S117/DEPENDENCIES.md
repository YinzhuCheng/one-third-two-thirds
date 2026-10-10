# S117 依赖地图

本文件替代旧研究运行中的 dependencies/ 文件夹与来源 manifest；它们不重复打包。下面全部前置证明已存在于仓库 S114/S115/S116。路径相对于本文件，可在同一仓库检出中直接打开。下载独立 S117 ZIP 时，可使用最后的固定版本入口在线读前置证明；S117 所附计算源码本身不需要这些旧目录作为运行输入。

## 逻辑方向

结构 good-pair／实际扩张概率律 → 终端混合、秩链、交织约束 → 第四终端秩与 gamma 全局界 → 新补域精确枚举。

另两块小外权重 census 各自使用同一批已证前提，互不依赖，也不参与证明全局有限化。最后的全七权重结论才合并三块分域。辅助 d5 纤维障碍与未证明的一般原子截断不参与闭合。

## 旧名到已发布原文的对应

- 结构归约：[原文](../S114/references/S112/structural_reductions.md)、[审查](../S114/references/S112/structural_audit.md)。外部 good-pair 输入为 [Zaguia，Definition 1 / Theorem 2](https://arxiv.org/html/1610.00809)。
- GENERAL_TERMINAL_RANK_BOUNDS.md：[S116终端秩证明](../S116/general-terminal-rank-bounds/GENERAL_TERMINAL_RANK_BOUNDS.md)；GENERAL_TERMINAL_RANK_AUDIT.md：[审查](../S116/general-terminal-rank-independent-audit/AUDIT.md)。只用其混合律、端口下界、乘积约束及V(1),V(2),V(3)，不借其另一个依赖有限 census 的推论。
- GENERALIZED_SHUFFLE_BOUND.md：[S114交织证明](../S114/generalized-seven-core-shuffle/GENERALIZED_SHUFFLE_BOUND.md)；GENERALIZED_SHUFFLE_AUDIT.md：[审查](../S114/generalized-seven-core-shuffle-independent-audit/AUDIT.md)。
- RANK_CHAIN_PROOF.md：[S114秩链来源](../S114/single-outer-spine-exclusion/SINGLE_OUTER_SPINE_EXCLUSION.md)；RANK_CHAIN_AUDIT.md：[秩链和内单点审查](../S114/generalized-seven-core-shuffle-independent-audit/RANK_AND_INNER_SINGLETON_AUDIT.md)。
- WEIGHTED_COUNT_FORMULAS.md：[实际完整扩张计数](../S114/references/S113/weighted_analytic_result.md)；WEIGHTED_COUNT_AUDIT.md：[审查](../S114/references/S113/weighted_audit.md)。
- FOUR_TAIL_CERTIFICATE.md：[S115四尾联合证书](../S115/four-tail-rank-certificate/FOUR_TAIL_CERTIFICATE.md)；FOUR_TAIL_PROOF_REVIEW.md：[审查](../S115/four-tail-independent-audit/PROOF_REVIEW.md)。任意c的适用说明见S116终端秩证明。

旧审查记录里的 source_snapshot、SOURCE_INTEGRITY、MANIFEST、SHA256SUMS 是研究当时的来源核对记录，不是本次的运行输入；不要求读者重建它们。完整数学论证保留，新的包布局及生成命令见 [REPRODUCE.md](REPRODUCE.md)。

前置版本固定入口：[S114](https://github.com/YinzhuCheng/one-third-two-thirds/tree/7a4a88b87994742589021756d64f711f759614ed/S114)、[S115](https://github.com/YinzhuCheng/one-third-two-thirds/tree/7a4a88b87994742589021756d64f711f759614ed/S115)、[S116](https://github.com/YinzhuCheng/one-third-two-thirds/tree/7a4a88b87994742589021756d64f711f759614ed/S116)。
