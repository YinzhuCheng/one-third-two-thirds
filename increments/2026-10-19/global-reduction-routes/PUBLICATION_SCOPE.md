# 发布范围与复现边界

本增量只含最小反例图谱、全局链压缩、有界度核心三份主稿，实验与文献说明，最终合并独审，以及必要的自有源码和精确控制摘要。正文中“仅本地”“未同步”等句子记录原成稿时点，不表示本次发布尚未发生。

## 控制资料保留

- 有界度核心：`check_controls.py`、`controls.json`，用于预先指定的路径族、模块、trace 与锥恒等式核对。
- 全局回传控制：`check_frozen.py`、`audit_fixed.py`、`summary.json`、`independent_audit.json`。
- CUT-SELECT 零新计数提取：`extract_cutselect.py`、`cutselect_extraction.json`。
- 独审固定 witness：`independent-fixed-witness.json`；若最终独审另有必要自有核验代码，随清单列入。
- 边界 trace / pair-only 专审：最终 `REVIEW.md`、`check_controls.py` 与 `controls.json`。其固定核验不追加全局搜索预算。

672 个实际模型的完整 pair 整数矩阵 `all_exact_counts.jsonl.gz`、644 个逐控制记录 `control_records.jsonl.gz`、可生成的 `frozen_cases.json` 未重复附入。完整本地来源为 `/workspace/shared/global-pullback-tests-20261019/`；本包已保存需要阅读结论的精确摘要与全部 13 个同侧结构前件真控制的独立核验细节。

## 在可写副本内再生成

进入 `global-pullback-tests-20261019`，依次执行：

```bash
python3 check_frozen.py
python3 audit_fixed.py
python3 extract_cutselect.py
```

第一步由写定的 28 个族生成冻结关系、672 个模型的全部精确矩阵及 644 个控制；第二步对既定前件真控制作独立核验；第三步只读取已有证书并代入组合公式。程序均用 Python 标准库，路径基于自身目录。重跑会覆盖生成结果；数学判定使用精确整数/Fraction，耗时展示值可变。本次三端同步没有执行这些程序，也没有生成新哈希。

有界度控制可在其目录执行 `python3 check_controls.py`，仅核预设控制而非 D≥7 全偏序搜索。研究结论由正文证明承担，有限控制不替代一般证明。

## 继承与省略

旧论文/旧主稿均用固定 GitHub 链接衔接，未重复保存旧大包、第三方原文 PDF 或图谱 `sources/` 中的本地镜像。全文提到的前轮输入、临时计划与生产日志未一并搬运；复现本轮控制不需要这些日志。继承证明未由本轮统一重新审查，见 `INHERITED_INPUTS.md`。

不含原始聊天、内部指令、密钥、凭据、个人隐私、缓存或软件包。`PUBLICATION_INVENTORY.json` 列出实际保留文件、字节数与省略项；没有新增独立哈希门槛。

原猜想 OPEN，历史 35/55 不变。XP 核心输入 0 命中，不能将 vacuous 检查表述为验证；一般 GCC 回传、G/G+ 及 D≥7 全长锥证书仍开放。
