# 1/3–2/3 猜想：R1–R65 / S1–S82 交接入口

日期：2026-10-01。最新专门研究 **S82**。完整交接ZIP提供147份规范轮次报告索引、703条原历史记录、当前可恢复的原稿／程序／证据／过程日志，以及本次挂载的近期增量。**主猜想、一般宽度三、全十参数非平凡2/5仍未由项目闭合；U58仍不是已认证一般界纪录。** GitHub只同步核心数学与导航，下面history/originals/core等档案路径指完整ZIP，不表示全部历史已经上传仓库。

## 新会话只先读五份

本页 → [01问题与状态](01_PROBLEM_AND_STATUS.md) → [03实际依赖](03_DEPENDENCIES.md) → [05优先路线](05_PRIORITIES_AND_CONJECTURES.md) → [09下一断点](09_NEXT_SESSION.md)。随后只读选中路线的原稿。

最小阅读ZIP不是完整备份。完整包中的history、originals、reports不要整批装进上下文。数学推导优先，不要求Lean、全库回归、哈希或CI作为继续研究的门槛。已保留的旧程序仅按需使用。

## 本轮真正改变了什么

S82检查S58§4的单点／整块窗口混用。计数对数凹结论可由S78整块定理修补，并有精确关系：

    D_r=(r+1)(r+2)[a_(r+1)^2−a_r a_(r+2)]/a_r^2。

固定外部、只增加自治块时，外部投影以显式O(1/r)趋向D(x)、I(x)、U(x)各自均匀后串接的律。相应窗口趋于最大插槽；它给出S81高斯条件θ>1不可删除的真实反例，也显示固定标签可在无限极限中失去有限对象的好对。见 [S82证明](S82/notes/PROOF.md)。这些结论不认证U58，不完成主猜想。

## 版本优先级

1. 当前总图、[10审查状态](10_AUDIT_STATUS.md)、S82修补决定当前使用范围。
2. S71现行为GitHub **399项**修订稿；624项原版在ZIP的originals中，不得混报。
3. S78–S80仓库文件是S81上传的标注阅读整理版；逐行原稿、旧检查与脚本保存在完整ZIP的originals/expanded和originals/conversation_loose。
4. S58§4计数推论使用S82修补；S58窗口主证明与U58最终链并不靠该§4，不能扩大撤回范围。
5. 旧报告保留当时OPEN／PROVED措辞，只作历史；不能覆盖后续状态，也没有因为重新入库而获得外部认证。

## 完整ZIP去哪里找材料

- [02总路线图](02_RESEARCH_ATLAS.md)、[04反例护栏](04_FALSE_ROUTES_AND_GUARDS.md)、[06文献关系](06_LITERATURE_AND_THEOREM_MAP.md)。
- `reports/ROUND_INDEX.md`：147轮统一导航；JSON/CSV索引在registry。
- `history/through_S68/`：完整迁入版的全部已恢复内容，包括展开的1,583个S67旧文件与原S67 ZIP，保留原相对路径。
- `originals/input_archives/`：S71–S81各增量原ZIP；originals/expanded供无需再次解压地取文件。
- `originals/repository/`：本轮实际取回的GitHub源码快照；以ZIP的SYNC_STATUS区分提交版本。
- `core/`：S50、S53、S57、S58、S62、S65等按需阅读的旧原稿副本，来源在registry/core_sources.json。
- [08档案范围](08_ARCHIVE_INVENTORY_AND_LIMITS.md)：源条目映射、修订差异、历史损坏恢复限制；不是保存未记录聊天或私有思考的声明。

[AGENTS.md](AGENTS.md)是所有者研究方式指示，优先于旧包内工程化流程建议。干净会话可直接粘贴09末段。
