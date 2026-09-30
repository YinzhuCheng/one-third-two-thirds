# 1/3–2/3 猜想 · 数学 agent 共同研究档案

这里首先是一个**数学研究项目**。GitHub 保存证明、反例、开放路线、文献研读和必要程序；网站只辅助阅读，不承担研究调度。

> **首次迁入状态（2026-09-30）：** 核心入口、路线总图、反例护栏、文献关系和 S68 证明已写入 GitHub。完整 ZIP 尚需通过下方 Release 附件入口导入；不要把原文中的“133 份报告”“1,583 个旧文件”误读成当前远端上传完成数。完整导入完成后会生成 `archive/IMPORT_COMPLETE.md`。网站源码已准备，但本次没有成功部署 Vercel。详见 [MIGRATION.md](MIGRATION.md)。

## 新 agent 入口

先读 [AGENTS.md](AGENTS.md)（[小写入口](agents.md)）。随后按顺序阅读：

[00 · 研究入口](00_START_HERE.md) → [01 · 问题与状态](01_PROBLEM_AND_STATUS.md) → [03 · 依赖关系](03_DEPENDENCIES.md) → [05 · 优先路线与猜想](05_PRIORITIES_AND_CONJECTURES.md) → [09 · 下一会话断点](09_NEXT_SESSION.md)。

按需补读 [02 · 路线总图](02_RESEARCH_ATLAS.md)、[04 · 反例和失败版本](04_FALSE_ROUTES_AND_GUARDS.md)、[06 · 文献—定理关系](06_LITERATURE_AND_THEOREM_MAP.md)，再取相关原稿。继续最新路线可直接进入 [S68 报告](S68/REPORT.md)、[完整证明稿](S68/notes/PROOF.md)和[计数核源程序](S68/src/skeletons.py)。不要从加载全部历史开始。

## 数学研究优先

不把软件工程流程当作数学推进方法。避免非必要的编码、门限检查、哈希检查、强制 CI 和形式化工程。**数学证明暂时不需要程序性验证**；清晰、完整、可审查的数学推导是主要产物。已有程序和证书保留供按需参考，不要求每轮重跑。

可以直接记录部分证明、直觉、失败尝试和待查文献；写清条件、结论及缺口。保存一份草稿并不等于认可其中所有主张。旧交接包中有关验收、形式化和计算的要求只是历史计划，不覆盖当前 AGENTS.md。

## 当前数学边界（S68 快照）

主猜想及全部宽度三仍开放。十点种子全十参数链替换的定性 1/3 已有文献推论；非平凡膨胀的 2/5 仍未解决。S67、S68 已关闭的子参数族不能外推为全域。一般界研究稿、有限计算与外部文献有不同的适用条件和审查状态，见 01、03、06。

## 在这里协作

使用 [Issues](https://github.com/YinzhuCheng/one-third-two-thirds/issues) 讨论数学问题；直接提交或用 PR 保存研究增量均可。先看最近变更，避免覆盖他人的内容。不设置与数学无关的合并门槛。

一轮结束留下研究问题、实际结论、失败原因、未闭合的连接、所用文献和下一步。优先整理证明线路，而不是增加管理设施。

## 完整原包导入：只需一次

打开 [已创建的 Release 草稿](https://github.com/YinzhuCheng/one-third-two-thirds/releases/tag/untagged-be88c2aa7c78297ea210)（需要仓库所有者登录；也可从 [Releases](https://github.com/YinzhuCheng/one-third-two-thirds/releases) 找到）。将原先给 ChatGPT 的**完整版 ZIP 和阅读包 ZIP**作为附件加入，等上传结束后点击 **Publish release**。不必重新下载这里生成的大包，也不必先自行解压。

发布会启动已经准备的文件导入工作流。它保留两份 Release 原附件，把完整包展开到根目录、阅读包展开到 `archive/reading_kit_S68/`，并把嵌套 S67 原档展开到 `history/S67/`。旧目录和相对路径不变，发生内容冲突时保留现行文件，原版另存，不覆盖新研究。

这是一次性文件搬运，不是数学 CI，不运行历史程序或哈希验收。**已实际运行的是准备附件草稿的步骤，不是完整云端导入。** 导入进度和失败信息见 [Actions](https://github.com/YinzhuCheng/one-third-two-thirds/actions/workflows/import-archives.yml)。已发布后才补齐附件时，可从该页面手动运行。

## 阅读网站

源码是 [site/index.html](site/index.html)，配置是 [vercel.json](vercel.json)。纯静态、无外部依赖、无需密钥，提供路线入口和按打开/刷新时读取的 GitHub 文件目录。网站只发布 `site/`，不复制整个数学档案到网页服务。

在 [Vercel 新项目入口](https://vercel.com/new) 导入**这个已有仓库**，框架选 Other，根目录保持仓库根目录，输出目录为 `site`，不设置环境变量。仓库配置已指定空安装和构建命令。部署成功后，再把实际站点网址补入这里。

本仓库经所有者授权公开。公开不意味着各项数学主张已获独立审稿；也不自动为所引用的第三方文献赋予新的许可证。
