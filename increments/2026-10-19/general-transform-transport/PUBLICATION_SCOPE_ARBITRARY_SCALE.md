# 本轮发布范围

日期：2026-10-19。

本轮只发布四份完整锁定新增稿、两份最终独审、各稿局部审查记录和必要小控制代码/精确结果。旧材料与仓库历史保留。新稿的独审状态只覆盖其明确新增论证及继承依赖，不认证文献新颖性。

## 保留

- arbitrary-scale-blowup：RESULT.md、AUDIT.md。
- marker-covariance-limits：RESULT.md、AUDIT.md、verify.py、verification.json。
- global-branch-witnesses：RESULT.md、check_frozen.py、verification.json、check_joint.py、joint_verification.json。
- interface-safe-descent：RESULT.md、check_controls.py、controls.json。
- review-scale-covariance：REVIEW.md、verify_selected_algebra.py、selected_algebra_verification.json。
- review-witness-descent：REVIEW.md。
- 本轮短导读、此范围说明、继承输入链接与文件清单。

## 省略与复现边界

省略探索脚本 symbolic_probe.py、PLAN、冗余 CHECKS/verification 日志和旧包的重复大表。所有新增正式论证均完整保留，未只保存摘要。继承的旧证明留在已有仓库和先前归档中，见 [继承输入](INHERITED_INPUTS.md) 的固定版本链接；本 ZIP 是小增量而非全历史离线重打包。

本次未重跑实验、未新增数值控制或哈希门槛。有限控制只支持其精确数据，不代替解析定理。部分控制源码保留生产时的输出路径，包内精确结果可直接阅读；不声称全包在任意目录一键重跑。SymPy 是 marker 精确多项式控制的依赖；一般区间根隔离和窗口最大流算法没有实现或测试。

未包含聊天、私密资料、凭据、缓存或软件包。原猜想仍 OPEN，35/55 不变；没有外部文献首创认证，也没有全局有限化或严格反例保持结论。
