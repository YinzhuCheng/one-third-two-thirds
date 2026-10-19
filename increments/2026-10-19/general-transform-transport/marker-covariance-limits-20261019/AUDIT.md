# Marker 协方差界独立审查

日期：2026-10-19。完整审读本目录 `RESULT.md`，只审本轮新增内容，不重复已有 joint-run 全部审查。结论：**PASS**，未发现实质缺口。

重点通过项：

1. 全 m 增广中固定原 LE 的精确纤维计数；末槽位移和；选最后 marker 后的实际秩常数偏移；保留计数倾斜的 JC_m。
2. 最后 marker 的全 m 单点秩计数与 LC，以及对应二项变换。没有扩张为所有中间 marker 的联合约束。
3. 一份固定正三角联合尾抽象 law 的全部有限数字；全 m 协方差六次多项式和三个末 marker 秩 LC 多项式，均由审稿者独立精确展开复算。m→m+1 的正系数展开给全 m 证明。
4. h=1 的 JC_1 无权弱投影、一般联合预算恒等式和普通重加权解权误差公式，均无丢项。
5. singleton ideal 的删除点体积倾斜、普通坐标 FKG、n+1 与 n 的秩/次序统计量转换；Cov≤r 证明成立。抽象 law 不可实现的认证由此独立得到，没有循环使用一般 T。
6. 结论严格局限于稿中逐项列出的标量不等式合取不蕴含 Target，不否定 marker 方法整体；一般 actual T 仍开放。

唯一文字建议：第 1 节 T_a 的非零主项渐近限定为固定 1≤a≤h；a>h 时整项为 0。作者已修复并锁稿，不影响主结论。

完整逐项记录见 `../review-scale-covariance-20261019/REVIEW.md` 第 2 节。审稿者独立复算入口和实际保存结果分别为 `../review-scale-covariance-20261019/verify_selected_algebra.py` 与 `../review-scale-covariance-20261019/selected_algebra_verification.json`。

控制范围仍是同一个固定抽象 law，未新增 actual 枚举，未重跑已有 1330 对，未作外部平台写入或文献新颖性认证。
