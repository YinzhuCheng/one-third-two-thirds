# D9 证书精简：解析引理、有限路径支撑与 D10 止线

研究日期：2026-11-10。本增量把有限证书作为发现结构和猜想的材料，不把有限检查升级为一般定理。所有结果以 Kevin Fathi, *Gold Certificates and Balanced Pairs*, v22, [固定原始记录](https://zenodo.org/records/23933091)，尤其 Theorem 2.3 与 §24 为文献起点。项目的解析重组、原作者结论、有限数值重放和研究内独审分开记录，不作外部同行评审、形式化或优先权认证。

## 1. 已审解析替代

- [四个同下集标记点](analytic/FOUR_MARK_ANALYTIC_REPLACEMENT.md)：原插入律、区间分块和严格二次不等式覆盖整个相应截止域，替代原 74 向量检查的平衡用途；不声称复现原 141/140 常数。[独审](analytic/FOUR_MARK_INDEPENDENT_REVIEW.md)。
- [私人三点叉形](analytic/PRIVATE_FORK_ANALYTIC_REPLACEMENT.md)：固定银行 `2 Pr(b首位)+Pr(s<t)≥1` 及反向。统一因式分解替代 285 fork profiles；把 diamond 顶点放回真实外词后，同一引理吸收 1110 表的普通排除用途，不复现 107/140 强数值界。结合原解析大小界：**要么 P 已有平衡对，要么相应私人理想是至多四点链**。只有在原 P 无平衡反设下，才可直接说该理想必为链。[独审](analytic/PRIVATE_FORK_INDEPENDENT_REVIEW.md)。
- [二点主干与四点反链尾](finite-path/FOUR_EVENT_STEM_ANTICHAIN.md)：原例六个正权事件压为四个固定物理事件，`8Pr(b<a2)+Pr(t2<t1)+Pr(t3<t2)+Pr(t4<t3)≥11/3`。首次外点前实际子集与完整后缀权保留，不需要度数上限。[独审](finite-path/FOUR_EVENT_STEM_ANTICHAIN_INDEPENDENT_REVIEW.md)。

## 2. 原给定 v-first 树的 400 次解析替代

计数单位是原证明树的 **bank occurrences**，不是不同偏序、不同同构类或新的平衡类。总数 3469 = 3049 unconditional + 420 terminal；8 次无银行 pivot 切换另计。

1. [单前沿交换](chain/SINGLE_FRONTIER_ANALYTIC_REPLACEMENT.md) 353 次；[独审](chain/INDEPENDENT_REVIEW.md)。
2. [私人前驱支撑的两阻挡门](chain/TWO_BLOCKER_FORK_GATE.md) 匹配 62 次，其中 25 次与上项重叠，净增 37；合计 390。[独审](chain/TWO_GATE_INDEPENDENT_REVIEW.md)。
3. [三共同尾的四事件银行](chain/THREE_TAIL_FOUR_EVENT_ANALYTIC.md) `6Pr(u<b)+Pr(v<u)+Pr(t2<t1)+Pr(t3<t2)>3`，用三叶实际度≤9解析替代该门 2408-profile 正证书，净增 6 至 396。[独审](chain/THREE_TAIL_INDEPENDENT_REVIEW.md)。
4. [中间头受支持的记忆门](chain/MIDDLE_HEAD_MEMORY_GATE.md) 保持同一银行，匹配 10 次，其中 6 次已在上项，净增 4。当前去重并集 **400/3469，尚余 3069**。[独审](chain/MIDDLE_HEAD_INDEPENDENT_REVIEW.md)。

400 只指这棵给定树中已找到解析替代的行；结构分支覆盖、其余 3069 行以及其他 D9 证书族并未因此被删除。它不是“整个 D9 已纯解析”。对应原节点与替代映射保存在本增量的 JSON 中；先前 58、34、9 等诊断计数均包含于这里，不得再相加。

## 3. 已审有限路径事实与未证猜想

[13 相邻替代独审](finite-path/THIRTEEN_ADJACENT_INDEPENDENT_REVIEW.md)核查了原 packet 的 13 处非相邻事件：9 个全域、4 个终端，可分别改成 1–3 个等权相邻事件。原整数 verifier 对 55,987 条适用不等式通过；未改原树或终端条件。原完整结构与原银行算术另行重放通过。因此：**这棵 supplied v-first 树的全部 3469 次银行使用可以只用 reference 顺序中的相邻不可比反转**。权重仍可随完整带记忆状态变化。

这不是所有 D9/D10 状态的定理，不说明相邻银行具有相同最优值，也不证明每个记忆状态都存在银行。原生成器未取得，不能排除生成选择偏差。[猜想与最小判伪目标](finite-path/CONJECTURE_AND_NEXT_TEST.md)。

## 4. 必须保留的真实止线

- D10 中，四标记相邻和、私人 fork 银行、四私链旧银行以及新三尾银行都有各自真实失效控制；这些对象另有平衡对，绝非猜想或 NB 反例。
- [三个事件仍不足](chain/DEFECT3_THIRD_EVENT_RESULT.md)：固定原两个锚事件后，加任意一个第三事件也可能不存在跨真实完成律的统一银行。混合并不等于某单一原偏序的投影律。
- [细投影可负](chain/Q8_PROJECTED_WORD_CONTROL.md)：完整原对象源银行 margin +674，但合法细投影词为 −88；真实插回完成权不能丢失。
- [下一 pivot 出口](chain/Q8_FIRST_HEAD_EXIT_MAP.md)只保证合法曝光接口，尚未证明新状态都可付款。

## 5. 文件范围与接续

本公开增量保留审校后的数学正文、研究内独审、原节点替代映射和 13 行整数重放输入；不复制原作者整个 523MB 项目包、原始聊天、私人笔记或无关资料。原作者 packet/verifier/full proof 按固定文献记录获得；[重放说明](finite-path/REPRODUCTION.md)列出精确目录与统计口径。源文档与本公开副本的 SHA 对应见 [SOURCE_BINDINGS.json](SOURCE_BINDINGS.json)。数学正确性不由哈希或上传成功来认证。

下一步优先：从相邻路径支撑提炼参数化不等式；对剩余多阻挡行寻找联合事件或保记忆 pivot 法。合法曝光本身不是付款或统一停机证明，不将这些已审小门外推至全 D10。
