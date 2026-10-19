# 同步范围与恢复边界：joint-boundary increment

本增量仅加入四篇正式数学正文、两篇最终独立审稿、必要的小脚本与精确证书，以及阅读入口。历史正文、旧台账与旧成果文件不覆盖；仅在 2026-10-19/START_HERE.md 增加本轮导航。

## 保留

- branch-certificate-obstructions：RESULT.md、check_frozen.py、verification.json。
- joint-run-constraints：RESULT.md、verify.py、explore.py、check_slices.py、verification.log，以及 verification_compact.json。
- exact-interface-realizability：RESULT.md、check_controls.py、controls.json。
- multiscale-blowup-boundary：RESULT.md。
- 两路 REVIEW.md；分支/联合矩独审的 verify_independent_controls.py 和 independent_controls.json。

verification_compact.json 从已有最终 verification.json 原样提取 scope、summary、12 个原结构的名称／点数／关系／扩张数／嵌套对数量、三个直接 marker 控制、positive_cov_gap、nonMTP2_tail 与 nonactual_contrast。另加 publication_note 明确说明提取与省略；没有重新计算数学结果。

## 省略

- joint 原 3.65MB verification.json 中的 1330 项逐 ideal 精确大表。原完整表留在研究工作区；小包不声称包含全部逐例原始输出。
- PLAN、临时笔记、重复 CHECKS／controls.log、缩放 AUDIT 短记录、缓存、原始聊天、软件包及任何敏感数据。
- 既有前轮输入正文不重复打包；它们已在本仓库先前增量保存。

## 复现与证明依赖

源码逐字保留，不为发布修改数学程序。部分脚本含生产布局的绝对输出路径；因此该包是可接续的小增量，不能称为全部一键运行包。联合 verify.py 在同目录依赖 explore.py，运行时会生成完整 verification.json。该脚本重新生成行为只是源代码已有能力，本次未运行。

正文相对路径保留作者布局。部分继承输入（例如 principal-filter-slot-bound-20261018、nonprincipal-slot-mixture-20261018）在历史材料中使用不同归档层级，阅读时可从仓库 2026-10-18 机制导航定位；不把原相对路径全部可点击或所有外部依赖齐全当作已验证事实。

数学结论与适用条件以四正文和两独审为准。原猜想 OPEN、35/55 不变，无新全局排除或文献首创主张；chain+2 的结果只定位本轮端点机制分类。
