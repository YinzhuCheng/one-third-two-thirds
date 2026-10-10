# S109：任意宽度的共同下集交换平方

[中文完整说明与证明](GENERAL_SQUARE_NOTE.md)是本目录的阅读入口。

对任意有限偏序、具有相同严格下集的不可比实际标签 u,y，令 H 为正方向合法交换扩张数，Ru,Ry 为两个方向不可交换扩张数，则 **H² > Ru Ry**。共同不可比集不必成链，偏序宽度不限。

对任意不可比对，分别作下集和上集条件化，可在同一原均匀完整扩张律中得到 rr′≤h²、ll′≤h²；有限偏序的严格性进一步给出两个严格号。事件交集质量必须保留。此处严格性仅为定性结果，不提供新的统一余量或维数系数。

## 证明与审查

- [一般非严格平方证明](general_shared_downset_ball_proof.txt)
- [任意不可比对的双条件化](universal_double_conditioning_corollary.txt)
- [上述两份证明的独立研究审查](general_square_ball_independent_audit.txt)
- [有限偏序严格性证明](strict_shared_downset_square.txt)及[独立研究审查](strict_shared_downset_square_independent_audit.txt)
- [二维对数凹解析引理的另一路独立审查](logconcave-audit/independent_analytic_audit.md)
- [文献比较及读取边界](prior_art_swap_square.txt)

证明使用经典边缘对数凹性与 Busemann–Ball 定理。Kahn–Yu（1998）已有相关二维几何路线；无共同不可比元素的特殊情形可由 Chan–Pak（2024）Theorem 1.9 直接推出。**不认领新颖性。** Kahn–Yu 全文的逐定理比较尚未完成。

这些审查是本研究中的独立数学复核，不是外部同行评审或 Lean 等形式化认证。**MAIN33、WIDTH3、TEN40 仍 OPEN；U58 仍 UNDER_AUDIT。** 局部平方约束没有消去任意对的双重阻挡质量，也没有给出普遍平衡对选择机制。

## 可复算的有限核对

三个 Python 检查器仅用标准库；运行会更新相邻 JSON 结果文件：

- `python audit_general_square_exact.py`：2 至 6 点自然标号偏序的共同下集交换计数，以及 2 至 5 点的单次条件化。
- `python audit_universal_conditioning_exact.py`：2 至 5 点任意不可比对的两次条件化与精确四格映射。
- `python logconcave-audit/check_logconcave_exact.py`：有理多边形、齐次势与多项式存活函数的解析校准。

[发布侧复算记录](PUBLICATION_CHECKS.md)给出实际范围和限制；[SHA256SUMS](SHA256SUMS)只覆盖本目录这次新增的交付文件。程序、哈希和仓库回读用于复算及版本一致性，不替代数学证明。
