# 学术插件接入与原文核对 · 2026-10-02

这是实际检索和适用范围记录，不是新数学结果，也不是全面查新。

## 从一个真实研究问题走通

任务：S62的参考跨度五，与5-thin、6-thin及线性差异文献究竟是什么关系？

SciSpace使用完整数学问句检索：哪些论文研究每点有界不可比邻居，并与宽度/参考扩张跨度区分。返回了BW92、CMW14等。Sider用短关键词Kahn Saks inequality width two，实际返回OpenAlex W3170540383（Chan–Pak–Panova）、W4404220299、W2075164088。另一宽泛查询返回低相关结果，CMW14的DOI查找也曾失败；不将这种失败解释成文献不存在。

最终依据作者或出版社原文决定记录，不按学术插件的生成TLDR断言定理。

## 可核对的一手资料

| Key | 入口 | 本次读取与作用 |
|---|---|---|
| L-BW92 | https://epubs.siam.org/doi/10.1137/0405037 | 出版社摘要：每点最多五个不可比邻居的1/3结论；未重审计算 |
| L-PEC08 | https://link.springer.com/article/10.1007/s11083-008-9081-9 | 出版社摘要：6-thin的Gold Partition，蕴含1/3；S62原稿已有引用，此次恢复连接 |
| L-CMW14 | https://link.springer.com/article/10.1007/s11083-013-9302-8 | 出版社摘要与元数据：linear discrepancy的定义；宽度二的floor((3r−1)/2)界，不能用于任意宽度 |
| L-OS17 | https://arxiv.org/abs/1706.04985v2 | 作者摘要明确只解决若干特殊族，版本v2 2018-01-31 |
| L-AK25 | https://arxiv.org/html/2510.26134v1 | 对照1.3、1.5、1.6、1.7的定理陈述；全局、固定宽度、条件蕴含不可混用 |
| L-CPP23 | https://escholarship.org/uc/item/4bd6q0m1 | 两个学术渠道发现同文；最后一次直接页面读取被机器人验证挡住，不升级为全文已读 |

5-thin/6-thin的数字是最大不可比度；S62是存在一条参考线性扩张，其不可比距离至多五，且宽度至多三。CMW14定义的ld是对参考扩张再取最小值。因此它提供命名与结构参数接口，而不自动说明S62被已有平衡度结论包含。也不能把5-thin称作当前已知最强thin阈值，至少PEC08已有六的结果。

## 发现的自动摘要错误

SciSpace一次生成TLDR把Olson–Sagan的特殊族结论写成所有有限非链成立；同条记录的作者摘要及arXiv原文与之不符。丢弃该TLDR中的全称断言，Notion的G-TLDR专门保留此护栏。AK25的条件结果也不能被短摘要改写成已经无条件证明Kahn–Saks。

SciSpace add-column的Limitations请求对所给ID返回not_found；没有产出可用定理对照表，不声称该功能本次已成功。Sider检索与单文献详情、全文读取也不能混为一项成功。

## 更新后的具体数学任务

在R-LOCAL/R-LIT路线下，对齐BW92、PEC08、CMW14与S62的假设及证据。先读S62 §§1、4、5、12和原始文献相应定理，确定哪些只是命名重叠，哪些是真正的范围包含。目标是找到真实完成权重与前沿延伸之间缺失的一个联合约束，不继续盲目提高枚举跨度。

Notion读取等级使用DISCOVERED、ABSTRACT_CHECKED、STATEMENT_CHECKED、PROOF_SECTION_READ、FULL_PROOF_AUDITED、INHERITED_UNVERIFIED。等级记录的是对应版本及本次实际读取，不由页面导入或自动摘要提升。
