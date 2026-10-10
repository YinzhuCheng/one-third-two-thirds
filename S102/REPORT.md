# S102：方法主线、两类真实反例与尚未闭合的接口

日期：2026-10-10。父版本：fc7999aa4cdcb8ef2fcb8bb44a51560ec0b78764。研究记录归档，不等于外部审稿或独立认证。

## 当前结论

- MAIN33 / WIDTH3 / MC3 / TEN40：**OPEN**。U58：**UNDER_AUDIT**。
- 终端兄弟必平衡、仅四标签菜单必有好对：**REFUTED**。G7 有62条扩张，Pr(s<t)=17/62。
- 四标签加第一层最小共同上界菜单必有好对：**REFUTED**。G10 有372条扩张，菜单无好对，全偏序仍有6对。
- 以上反例不反驳 S99 的障碍约化，不反驳主猜想；未声称全局最小反例。
- [S100 联合计数勘误](S100_ERRATUM.md)：3/20、3/20 改为4/20、2/20，总边缘和兄弟对1/2不变。
- 归一化平方候选 dU≤p²、共享下集行列式 H²≥RuRy 仍 **OPEN**。

## 按方法阅读

先读 [方法总纲](method_research_overview.txt) 与 [依赖地图](research_dependency_map.txt)，而非把轮次先后当成证明依赖。

1. [全局极值与双侧交换](global_extremal_exchange.txt)：共同原律、有限迁移、阻挡守恒 B−H=2p−1。固定少数事件充电仍缺失。
2. [共享下集与真实插槽](weighted_square_interfaces.txt)：归一化、真实纤维行列式、缺陷减方向方差；不能无偏删除共同前驱。
3. [阻挡充电尝试](blocker_charging_attempt.txt)：稳定旋转合法但不单射；G7 给局部条件压缩后的容量障碍，未否定完整全局反设下的目标。
4. [秩原子兼容性](rank_atom_compatibility.txt)：标准多数切口与连续块计数接口；不把单点原子下界当作联合下界。
5. [有界不可比度前沿](bounded_range_frontiers.txt)：跨度、漂移和有限状态精确表示；状态类型有限不等于概率类型有限，不给有限反例点数核。
6. [共享前缀行列式新接口](shared_prefix_determinant_attempt.txt)：[独立研究审查](shared_prefix_determinant_audit.txt)支持 W=Σf_jV_j 与能量减方差接口，条件于明确引用的 Stanley/Chan–Pak 定理；非形式化或外部认证，外部定理长证明未重证；普遍标量闭合失败不反驳实际方向向量的原候选。

文稿中的“已核查／已建立”描述各原研究的证据范围，不能只凭状态文字当作本次发布者的独立数学认证。外部文献结论需按正文版本与假设使用；没有宣称本轮全面审完全部文献或旧证书。

本轮外部来源及适用边界见 [文献接口核对](literature_interfaces_20261010.txt)。外部稿件的版本、报告计算范围与本次独立检查分列。

## 反例与完整证书

- [G7 报告](COUNTEREXAMPLE_REPORT.md)、[全部62扩张及矩阵](terminal_fork_minimal_induced.json)。
- [G10/G11 报告](EXPANDED_MENU_COUNTEREXAMPLE.md)、[G10命名证书](expanded_menu_10_named_certificate.json)、[G11命名证书](expanded_menu_11_named_certificate.json)。
- 同目录保留原始数字标签证书、九点辅助证书、固定种子搜索源码及相应核查源码。没有上传编译产物、依赖包或原始聊天。

## 实际复核与运行

发布前实际运行：
- python3 verify_certificates_standalone.py --permutations：G7/G10 均 PASS，递归枚举、子集DP及全排列过滤一致。
- 六份7/9/10/11点证书逐份重算全部合法扩张与全点对计数：均与保存证书一致；命名和数字标签的重复表示不重复计作独立证据。
- python3 shared_prefix_determinant_check.py：标量闭合反例的有理数及一个7点非对称实例 PASS；不证明一般行列式候选。

搜索源码仅将工作目录绝对路径改为相对路径；如需重新运行搜索，在本目录执行。没有为此次发布扩展随机搜索或重跑旧大型证书。历史搜索次数属于原报告，不是此次复跑次数。

远端已检查两个 GitHub Actions 工作流：只由其工作流文件变更、手动或Release事件触发，本次研究文件提交没有适用数学CI。提交成功不表示数学认证。

## 下一断点

优先保留同一全局无平衡反设、实际标签及共同后端完成数，研究跨前沿的固定事件容量或实际方向序列约束。不得继续证明已反驳的兄弟菜单，不把无约束标量反例当成原候选反例；不假设一般迁移终止、普遍局部核心或联合切口正相关。
