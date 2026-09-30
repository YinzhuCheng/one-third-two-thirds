# 档案迁入状态与组织

2026-09-30。所有者明确允许公开这两个研究包及其研究内容。

## 实际状态

GitHub 已保存核心入口、研究原则、路线与文献说明、S68 完整证明稿及网站源码。**这不表示两个 ZIP 的全部文件已经进入远端仓库。** 本次运行环境不能直接联网传输二进制；GitHub 连接器支持文本写入，但没有上传本地 ZIP / Release 附件的接口。

本地已展开完整包 215 个文件、阅读包 213 个文件，以及嵌套 S67 原档 1,583 个文件。这个本地组织完成数不冒充远端上传完成数。完整的云端导入尚待原始 ZIP 附件。

原文中的“本包”“本轮”指 S68 交接包及其原有研究，不是这次网站迁移，也不是对迁移完整性的确认。旧原稿中的验证建议保留历史语境；当前研究原则以 [AGENTS.md](AGENTS.md) 为准，数学证明不要求程序性验证。

## 原档布局

| 原始材料 | 导入后的路径 |
|---|---|
| 完整 S68 包的 215 个文件 | 仓库根目录下原有相对路径 |
| 阅读包的 213 个文件 | `archive/reading_kit_S68/` |
| 完整包所含 S67 原始 ZIP | `archive/S67_original.zip` |
| S67 ZIP 内 1,583 个旧文件的展开副本 | `history/S67/`，保持全部原相对目录 |
| 133 份扁平规范报告 | `reports/` |
| 现有文献、注册表和旧指南 | `literature/`、`registry/`、`legacy_registries/`、`legacy_guides/` |

这样既能直接读取历史证明和程序，也保留原始累计 ZIP。阅读包不是完整备份，其特有的限制说明和清单也保留。旧报告中的相对链接应在 `history/S67/` 的原目录中使用。

如果导入材料与现行同路径文件不同，现行研究不被覆盖，原字节保存到 `archive/source_*`。不改写已失败路线，不将旧状态自动升级为新结论。

## 已经准备的附件入口

已创建 [Release 草稿](https://github.com/YinzhuCheng/one-third-two-thirds/releases/tag/untagged-be88c2aa7c78297ea210)，标签为 `s68-source-archives`。此草稿需要所有者登录查看。将原先提供的两个 ZIP 拖入附件区，上传完后发布。

准备草稿的实际运行已成功：[运行记录](https://github.com/YinzhuCheng/one-third-two-thirds/actions/runs/36698284721)。其中 `prepare` 成功、`import` 尚未运行。不能把这个绿色运行记录当作全部档案已导入。

发布后 `.github/workflows/import-archives.yml` 下载这两个原附件，调用 `tools/import_archives.py` 展开文件，提交到 main；原附件继续保留。只使用该仓库工作流提供的临时 GitHub 权限，无需提供个人密钥。

完整导入后会写入 `archive/IMPORT_COMPLETE.json` 和 `.md`，记录源文件数量、时间和冲突保存情况。它们只表示所在副本的文件搬运状态，不证明数学正确。没有新增数学测试、形式化或哈希验收门槛。

文件导入脚本已在本地对原来的两个 ZIP 实际执行，读取 215 + 213 + 1,583 个原始文件条目；没有运行旧研究程序。云端下载、提交的完整路径仍需附件到位后实际完成。

## Vercel 状态

`site/index.html` 为自含静态阅读入口，`vercel.json` 仅发布 `site/`。无数据库、环境变量、在线数学程序或自主后台 agent。已做本地桌面/手机排版查看；这不是线上部署验证。

**本次没有成功部署 Vercel。** 已连接的部署操作返回 `Tool deploy_to_vercel not found`；设计导入操作又只接受其指定来源主机，不支持本仓库 HTML。配置文件不等于成功部署。

在 [Vercel](https://vercel.com/new) 导入 `YinzhuCheng/one-third-two-thirds`，框架 Other，根目录为仓库根目录、输出目录 `site`，不需要环境变量。部署成功后才记录真实网址。无需把完整 ZIP 或大计数表再上传到 Vercel。

## 后续更新

完整导入之后，直接提交新增 Markdown、必要程序或文献笔记，不再反复复制整包。网站源文件变更走其普通 Git 部署；目录在读者打开或刷新时读取 GitHub 的实际文件。它不自动研究，也不把草稿合并解释为定理认证。
