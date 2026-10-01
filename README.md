# 1/3–2/3 猜想 · 数学 agent 共同研究档案

这是一个**数学研究项目，不是软件工程项目**。GitHub保存证明、反例、开放路线、文献研读和有数学用途的程序；Vercel仅辅助阅读。

## 最新研究：S81（2026-10-01）

[当前状态](CURRENT_RESEARCH.md) · [S78–S81四轮入口](RECENT_AUDITS.md) · [S81报告](S81/REPORT.md) · [审查与文献](S81/AUDIT_AND_LITERATURE.md) · [下一会话断点](09_NEXT_SESSION.md)

这几轮检查窗口凸序、真实局部律、方差缺陷与联合重叠，区分有限端部和无限局部极限。S81给出增长自治块的正确高斯波动判别，以及每个指定阈值的显式平滑余量。

**主猜想、一般宽度三、全十参数非平凡2/5仍未解决；U58仍为待独立审查的一般下界稿，不是已认证纪录。** 每项新结论的条件与证据范围见对应原稿；保存草稿不等于认可所有主张。

## 新 agent 入口

先读[AGENTS.md](AGENTS.md)（[小写入口](agents.md)）、[CURRENT_RESEARCH.md](CURRENT_RESEARCH.md)、[09最新断点](09_NEXT_SESSION.md)。需要旧背景再读：

[00研究入口](00_START_HERE.md) → [01定义与状态](01_PROBLEM_AND_STATUS.md) → [03历史依赖](03_DEPENDENCIES.md) → [05优先路线](05_PRIORITIES_AND_CONJECTURES.md)。

00–07主要保留S68背景；[S77定理链](S77/THEOREM_GRAPH.md)和[综合](S77/REPORT.md)提供全局地图，最新增量以当前状态及S78–S81为准。按需补读[反例护栏](04_FALSE_ROUTES_AND_GUARDS.md)、[文献图](06_LITERATURE_AND_THEOREM_MAP.md)。不要从加载全部历史开始。

## 工作方式

优先梳理证明线路、定义、反例和文献。避免非必要编码、门限/哈希检查、强制CI或形式化工程。**数学证明暂时不需要程序性验证**；已有程序和证书按需使用，不要求每轮重跑。

允许直接保存直觉、部分证明、失败尝试和待查文献，写清适用条件与缺口。旧包的工程化验收建议不覆盖当前AGENTS.md。[Issues](https://github.com/YinzhuCheng/one-third-two-thirds/issues)用于数学讨论，提交或PR用于保存增量。每轮留下实际结论、失败原因、依赖和下一步，不以提交数衡量研究。

## 档案策略：关键资料优先

所有者已明确允许公开，并选择先研究、按需上传关键文件，不以原始两个ZIP全量迁入为门槛。最近S78–S80同步的是明确标注的数学阅读整理版；完整原始快照、原代码和所有旧输出保存在S81合并阅读包，具体范围见[RECENT_AUDITS](RECENT_AUDITS.md)。旧检查数量不冒称本轮重跑。

历史入口里的“133份报告”“1,583个旧文件”描述原交接包，不是当前远端上传数量。[旧全档迁入说明](MIGRATION.md)和导入工作流仅作为可选历史工具保留，不要求执行。真实密钥和不相关私人资料不得进入公开仓库。

## 阅读网站

[研究工作台](https://one-third-two-thirds.vercel.app/) · [S81页面](https://one-third-two-thirds.vercel.app/S81.html) · [Vercel项目](https://vercel.com/borancheng949-8918s-projects/one-third-two-thirds)

网站源码在[site/](site/)，只部署这个静态目录。页面提供研究摘要、GitHub原稿链接及实际文件目录，不运行数学agent或计算任务。研究通过GitHub接续，不另维护一套数学主档。

本仓库公开不表示各项主张已获外部审稿，也不自动给引用的第三方文献赋予新许可证。
