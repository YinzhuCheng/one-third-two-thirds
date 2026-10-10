# S103：真实后端约束、旧能量反例与联合切口

日期：2026-10-10。父提交：18549739c494d1d34a96510fb2b86d75ec291a7c。保留S102和全部旧版本；这是一份分清适用范围的研究快照，不是外部认证。

## 当前结论及准确范围

**共享严格下集且中性集N为链的H²≥RuRy，以及width≤3归一化平方dU≤p²：本轮完整证明及独立研究审查通过。**

- [路径谱证明](schur_path_spectral_proof.txt)＋[独立全链审查](path_spectral_closure_audit.txt)：Jacobi形式、梯度谱、正确双线性正交与兼容退化极限。
- [离散Brascamp–Lieb证明](backend_second_order_bl_proof.txt)＋[独立审查](backend_second_order_bl_audit.txt)：有限出生死亡算子的自含BL不等式，直接在零Δ兼容子空间完成闭合。
- 二阶标量闭合是自含线性代数证明。偏序应用条件于明确的S102真实计数接口、Stanley秩对数凹与Chan–Pak一正方向块；外部长证明未在此重证。不是外部认证、形式化验证或首创性确认。
- **任意宽度、一般非链中性集下的原始归一化平方候选仍OPEN。** 不把width≤3子命题升级成一般命题，更不由此宣布WIDTH3或主猜想已解。

### 原律归一化

对原P中极小y与u∥y，令D=D_P(u)，Q为添加D<y所得偏序，d=e(Q)/e(P)>0。Q的完整扩张恰是原P条件于D全部先于y的完整扩张，因此p_Q=p_P/d，U_Q=U_P/d。若Q中性集成链（特别是width(P)≤3，添加关系不会增宽），Q的已证U_Q≤p_Q²给dU_P≤p_P²。没有删点后重新均匀化。

## 中间结果与独立保留的特殊类

1. [单共同前驱特殊类](single_predecessor_case.txt)：D={d}且与d不可比的中性前缀长度k≤3时，S102平方候选成立。新证明用单调质量上的精确路径二次型和全部顺序主子式，条件于S102已审查的外部输入。k是前缀长度，不是D的大小。
2. [完整Schur分解](backend_matrix_constraints.txt)：在真实Chan–Pak首两步块输入下，保留曲率与秩一残差，得到精确的 energy−variance+curvature+backend_slack 恒等式。退化Δ=0与末端分别处理，不能以任意0/0极限替代兼容条件。
3. [相邻多数切口](adjacent_majority_extrema.txt)：同一原律的相邻不可比标签，直接拼接计数给p_a p_b=z Pr(J)。条件XYZ的切口下界再给(2m−1)^8≤m(1−m)这一必要条件；并未给出存在性矛盾。

4. [链区间联合切口](joint_cut_migration.txt)：精确恒等式z=P(Ea)P(Eb)∏P(Ecj)/∏P(Ji)；外插质量归属至多四个固定少数事件，深插进入交换阻挡，头/尾残项尚未消去。[发布侧独立阅读](joint_cut_publication_review.txt)及1115有限整数实例支持自含计数；不推出链长界、无条件正相关或终止迁移。

上述独立研究审查详见[s103_live_audit.txt](s103_live_audit.txt)。自含计数、条件证明、精确有限证书及实验明确分开；外部输入的长证明未在这里重证。

## 真实有限证书：准确否定什么

[完整搜索报告](real_direction_search/REPORT.md)保存模型、预算、来源及边界。

- **旧S102能量充分闭合：REFUTED。** 13点真实宽三例E=10053，实际q_j上的旧归一化能量减方差为−4165/2156006592，而目标(H²−RuRy)/E²=8727397/101062809仍严格为正。不是平方候选反例，也不是主猜想反例。
- **单共同前驱不限前缀的旧闭合：REFUTED。** 21点例D={d}，中性不可比前缀长度16，E=120288；旧能量负、目标正，不与k≤3特殊类矛盾。
- **实际方向q_j单调性：REFUTED。** 9点例q_1>q_0而q_2<q_1，完整288扩张核对。
- 12点诱导负例的Ru=0，目标平凡；只证明它在指定13点例保留入口与非空D的诱导子序中最小，不主张全局最小。
- 原报告2000个加强式样本全部通过只属有限诊断；谱实验不是证明。长独立双臂本来就有目标缺口趋零，不以小缺口包装“接近反例”。

## 证据与复现

发布侧实际运行和未运行范围见[PUBLICATION_CHECKS.md](PUBLICATION_CHECKS.md)。

从本目录执行：

    python check_single_predecessor_case.py
    python real_direction_search/verify_frozen_certificates.py
    python check_backend_schur.py real_direction_search/minimal_single_gate_negative_energy.json

符号检查使用SymPy；精确证书及Schur检查使用Python标准库。随机谱实验另用NumPy，且不参与任何已证状态。搜索脚本可能覆盖其同目录输出；只复核时使用verify_frozen_certificates.py。冻结原研究源的SOURCE_SHA256SUMS与发布目录PUBLICATION_SHA256SUMS只用于文件一致性，不是数学认证。

## 继承护栏与下一步

MAIN33 / WIDTH3 / MC3 / TEN40仍OPEN；U58仍UNDER_AUDIT。S102的G7/G10反驳兄弟菜单及第一层共同上界菜单，S99条件约化保留。不要重启已反驳加强，不假设删共同前驱后仍均匀，不把不同条件律或随机标签概率拼接成同一固定对的原律概率。

下一步应研究这个新平方子命题如何与全局多数极值、固定事件容量或头尾穿插余项结合；不预设它自动关闭终端双分叉，也不启动无界的同族数值放大。旧正文中的OPEN仅表示推导时历史状态，显著前置更新说明其被覆盖的准确范围。
