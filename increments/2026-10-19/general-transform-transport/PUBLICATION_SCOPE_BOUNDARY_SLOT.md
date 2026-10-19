# 本轮发布范围与复现边界

日期：2026-10-19。

只发布四份完整锁定数学正文、两份最终独立审查和必要精确控制；没有原始聊天、凭据、个人隐私、缓存、软件包或重复历史大表。旧材料与历史导航完整保留。

## 保留文件

- bounded-block-limits：RESULT.md。
- effective-blowup-thresholds：RESULT.md。
- ideal-deletion-coupling：RESULT.md、verify.py、verification.json。
- safe-interface-composition：RESULT.md、check_controls.py、controls.json。
- review-boundary-effectivity：REVIEW.md。
- review-deletion-compatibility：REVIEW.md。
- 本轮短导读、固定继承输入链接、此范围说明、文件清单和更新后的 START_HERE。

正文及审稿完整保留，不以摘要替代证明；verify.py 和 check_controls.py 是作者已用的小控制脚本，保存输出来自作者实际运行。删除稿的6个预定 actual 结构及接口稿的6个预定 actual controls 均不构成偏序池搜索。独立审稿是否重跑，以对应审查正文为准；三端同步没有重跑任何数学实验。

## 明确省略与限制

省略冗余 verification.log、临时计划、探索记录、旧包重复内容。继承证明按 [固定版本链接](INHERITED_INPUTS_BOUNDARY_SLOT.md) 阅读；ZIP 是新增内容的离线小增量，不是全部历史证明的自包含重打包。

没有新增哈希门槛。小控制源码保留其生产输出位置；包内精确结果可直接阅读，不声称在任意目录可一键重跑。有效阈值稿给理论有限算法，未实现或运行量词消去程序，没有具体外商的数值 M_E。最大活跃块阈值 M_A 仍未有效化，不能把 M_E 的算法挪用到固定商有限盒的枚举上界。

各稿作者写作时的“仅本地写入”“无外部写入”是当时工作范围的历史说明，非本次已授权三端同步的状态。原 1/3–2/3 猜想仍 OPEN、35/55 不变；未证明变化外商的全局有限化、普适全边界安全递降或完整实际 witness 回传，无外部文献首创认证。
