# 变换机制：2026-10-19 小增量

本包只保存本轮新增证明、固定预算精确结果、脚本和独立审查。原 1/3–2/3 猜想仍开放，原分类 35/55 不变；未做文献新颖性检索，也不声称文献首创。旧研究与主导航见：

- [数学研究工作台](https://app.notion.com/p/3ed05a5b7caa819997e4d1db6d3c7dec)
- [方法总纲与本轮进展](https://app.notion.com/p/3f505a5b7caa81ccb953c831f2d1a29c)
- [反例放大与递降机制导航](https://app.notion.com/p/3fd05a5b7caa81f6b349c8f947fee0ce)

## 结果与阅读顺序

1. `substitution-asymptotic-kernel-20261019/RESULT.md`：固定有限非链外层 P 时，真实均匀线性扩张下 δ(P[C_m])→1/2，给实际整数秩跨块 pair 和 O_P(m^(-1/2))+O_P(exp(-c_P m)) 误差。常数可由有限 P 有效认证，未实际运行通用优化算法。固定外层不能换成增长外层的对角迭代。
2. `amplification-rank-obstruction-20261019/RESULT.md`：rank-CDF 收缩、strict gap 下的 Ferrers 必要形状、均匀 rank 半径和 CDF 距离图连通的充分障碍。无界 control 已有平衡对，不能冒充严格反例。
3. `descent-interval-cover-20261019/RESULT.md`：共同 TV 严格安全预算、共同方向锥和同核 g 的条件归并。它们是可核查的充分机制，没有证明必存在更短安全落点。t=2 加权覆盖诊断不属于 actual 均匀 LE 反例。
4. `actual-excursion-targets-20261019/RESULT.md`：冻结24个非principal相关门结构、252个实际不可比外部 pair，无两段闭平衡整数长度集。18个内部顶点满足强中项预算，却均因首项已坏而失败；另有18个整数非单调 pair。此有限阴性结果不证明一般 actual 连通性。

## 审核与复现

- 放大两稿的完整独立审查：`audit-amplification-mechanisms-20261019/REVIEW.md`。
- 递降与实际有限实验的独立审查：`audit-descent-cover-20261019/REVIEW.md`；以审查报告列明的范围为准。
- 脚本仅用 Python 标准库。实际实验目录已随附 `interval_solver.py`，可独立运行；审查脚本路径已仅作便携化调整。运行脚本可能覆盖同目录保存的结果，建议先复制目录。
- 实验脚本：`python3 actual-excursion-targets-20261019/run_test.py`；直接控制：`python3 actual-excursion-targets-20261019/verify_controls.py`。固定机制证书：`python3 descent-interval-cover-20261019/check_mechanisms.py`。
- 本次归档没有重跑实验或重新计算哈希。保存的 JSON 与日志是生产与独审已经完成的精确结果；证明由正文承担，有限核对不替代通式证明。

## 尚未解决

自代换严格反例保持、任意自代换迭代必触发障碍、一般 actual 外部闭平衡集连通性、更短共同安全整数落点必然存在，均未证明。全外部安全还不能替代全部含链点列保持，二者须在同一个整数长度处同时成立。
