# 日常研究工具链 · 2026-10-02

数学基线仍为 S82；本次是知识组织与读写路径完善，不是新定理轮次。研究原则继续以 [AGENTS.md](AGENTS.md) 为准。

## 直接入口

- [Notion 数学研究工作台](https://app.notion.com/p/3ed05a5b7caa819997e4d1db6d3c7dec)
- [Notion 接续协议](https://app.notion.com/p/3ed05a5b7caa81149e05cebc09af0a1f)
- [Notion 攻坚路线图](https://app.notion.com/p/3ed05a5b7caa81a387d9eb6aa978f7a9)
- [Notion 文献接入实测](https://app.notion.com/p/3ed05a5b7caa81a78afcf3b16d4dfc07)
- [当前数学状态](CURRENT_RESEARCH.md)、[下一会话](09_NEXT_SESSION.md)、[五份旧原稿](core/README.md)。

Notion 未被本次操作发布为公开网站。上面链接需要相应工作区权限；公开GitHub的链接不授予Notion访问权。网站不读取私人Notion数据或持有其凭证。

## 分工与实际覆盖

GitHub 保存规范证明、精确命题与更正、必要程序和版本；Notion 保存核心对象索引、原生关系、研究路线与讨论；学术插件提供发现渠道；Vercel保留只读阅读功能。完整历史大ZIP仍是容灾、深层计算审计和平台迁移材料，本次没有上传全部历史二进制到Drive或Notion。

Notion当前核心子集：31条规范命题/目标记录、6条路线、14篇文献、10条护栏、20条有类型关系。因中断重试产生的重复记录保留为ALIAS入口，工作视图按Alias of为空过滤，不把别名算作新成果。这个核心子集不是703条历史记录的全量迁移。

## 新agent怎样开始

先读GitHub的CURRENT_RESEARCH和09，再按需要读00/01/03/05。然后用 [registry/notion_locations.json](registry/notion_locations.json) 的稳定Key、页面ID、数据源与视图定位Notion记录，读取Canonical及实际依赖。不要依靠当前聊天已经记住哪轮，也不要一开始载入完整ZIP。

选一个明确数学问题，读取原稿、反例与来源，做数学研究。新论证或状态改变先写回GitHub，再更新Notion的Source revision、条件及关系。讨论可先留Notion，但未归档内容须明确写作待归档。更新失败则记录待同步项，不能声称自动一致。冲突按具体版本和更正解决，不以更晚编辑时间自动判真。

## 免费功能的实测降级路径

本次Notion单数据源SQL返回usage_limit_reached；没有升级、订阅或付款。已保存视图的view模式查询随后仍正常工作，并完整返回31条规范命题。工具说明也区分view模式与SQL配额。

日常读取优先使用已保存视图；再以Key普通搜索，最后按已知页面ID直接fetch。不要把没有AI Search或SQL用完解释成整个Notion不能读写。若将来view也不可用，GitHub的核心索引和原稿仍可独立接续。免费额度与接口可能变动，下次以实际访问结果为准。

创建记录前先按Key查找；重试写操作之前先读状态。Alias of非空时跟随主记录。Relations的Source是输入、Target是结果；USE不是启发，OPEN不是已证依赖，REPAIR不等于整个命题被反驳。Claims的便捷Uses字段不能取代有说明的关系记录。

## 文献接入：实测而不是宣传

SciSpace已实际搜索；Sider的OpenAlex检索已实际返回Chan–Pak–Panova的宽度二Kahn–Saks论文（W3170540383）。宽泛检索有不相关命中；部分DOI查找失败。SciSpace增加Limitations列的一次请求返回not_found，未把它当作已完成的定理对照。

SciSpace一个生成TLDR把Olson–Sagan的特殊族结论写成全体有限非链，作者摘要并未这样声称。文献表已保存这项护栏。搜索结果、生成摘要、原作者摘要、定理正文和本项目重证是不同证据。

[本次来源与查询记录](literature/TOOLCHAIN_SEARCH_20261002.md)保留BW92/PEC08不可比度、CMW14线性差异及S62参考跨度的区别。两篇2026九月论文继承原档说明，但本次未重新核验的部分仍标INHERITED_UNVERIFIED。不以两个数据库没搜到证明文献不存在。

## 每轮结束的最小增量

写数学结果、适用范围、失败原因和下一步；维护当前状态/断点及受影响的少量Notion记录。无需每轮重写所有页面、填满全部数据库或生成全量ZIP。网站只在入口需要变化时修改；Git推送触发既有部署不等于后台研究。

ZIP在重大里程碑、结构迁移、深度审计或用户明确要求时生成。主攻路径的五份历史原稿现在可直接读取；历史大型证书和未迁入来源仍需原S82档案。不能宣称所有深层依赖已经在线、也不能把短期Actions产物当永久备份。

## 恢复范围与非自动化边界

[registry/RESEARCH_CORE.md](registry/RESEARCH_CORE.md)是核心数学索引和关系的文本快照，页面位置在notion_locations.json。Notion不可用时仍能找到命题、来源和路线；它不是Notion全部评论/页面历史的无损导出。

没有创建常驻同步服务器、定时自主研究或全自动多agent编排。已有连接授权下的新会话可以按此协议自己读取和写回；插件登录失效时仍需要所有者重新授权。没有更改权限模式、套餐或他人内容。
