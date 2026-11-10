# 2026-11-10｜结构进展续编：D9 解析替代 607 次与 EL10 精确 lift 闭包

这是本项目的数学研究记录。各项已列研究内独立审核，不是外部同行评审、形式化或文献优先权认证。两类成果的原合同不同，不能拼成一般 1/3–2/3 猜想或 D10 证明。旧冻结稿和旧反控保留；本增量只更新下面明确范围内的旧未付状态。

## A. D9：从证书提炼解析结构

固定文献起点为 Kevin Fathi, *Gold Certificates and Balanced Pairs*, v22，[原始记录](https://zenodo.org/records/23933091)，主要 §24.4.1。已有作者定理、项目的解析重组、有限节点映射与研究内审查分别记录，不主张原创。

**当前去重并集为 607/3469 次 source-bank occurrences 采用解析替代；原 2862 次银行及结构阶段覆盖仍未解析化。** 次数不是不同偏序数、同构类或新增平衡类。此前公开 400 次是本并集的子集，不再相加；[去重计数账本](d9/PROOF_STYLE_LEDGER.json)保存计数及 Q8/rank-gap 的部分节点身份，不包含全部 607 个源键；本公开包不是可以独立重放全部 607 映射的完整公开证书。

在此前 400 的基础上，本续编记录：

- [Q8 原五事件银行的完整解析证明](d9/Q8_COMPLETE_ANALYTIC_PROOF.md)：两条原 symbolic 行改为解析；不是新增两次再计。真实外词根压缩、12 个结构截止次序、最大间隙仿射化、边界多项式和整数判别式取代旧 1512/81 正系数表依赖。仍有有限结构分类与整数阈值，不能称“无任何分支”或“无系数”。[组装独审](d9/Q8_COMPLETE_ANALYTIC_INDEPENDENT_REVIEW.md)。
- [原词秩间隙界](d9/RANK_GAP_ANALYTIC.md)净增 2；[同完整下集的四点门](d9/FOUR_EQUAL_DOWNSET_ANALYTIC.md)净增 30；[私人根秩门](d9/PRIVATE_ROOT_RANK_GATE.md)净增 49。后者用原私人最小点的实际不可比伙伴数 r≤2 和 r(|H|−2)≤6，不是任意 rank law。
- [参考首点完整下集支配的四点门](d9/REFERENCE_FIRST_DOWNSET_DOMINANT_FOUR_GATE.md)匹配 155 次、与前 483 次重叠 32，净增 123。它保物理参考顺序：第一点下集包含其余点下集，不声称任意参考都可用，也不单独声称四点中必有平衡对。
- [孤立共同头与根分支门](d9/ISOLATED_HEAD_ROOTED_BRANCH_GATE.md)形状一致但原树净增仅 1，不能因定理参数化而虚增节点数量。

总计 400+2+2+30+49+123+1=607。原前置 three-fork 的 978-profile 初序步骤也有[解析替代](d9/THREE_FORK_INITIAL_ORDER_ANALYTIC.md)，它不在 3469 账本内，不能与这张树的分子相加；后来 174-word / 1,820,185-profile three-fork 树并未由此移除。

[参考末点单度界加强](d9/FOUR_BANK_LAST_ONLY_DEGREE_INDEPENDENT_REVIEW.md)另核：上述四点相邻反转和严格大于 1，只需物理参考最后一点的完整不可比度≤9。第一点的下集支配角色与最后一点的度角色不同；此参数加强不增加 D9 原节点计数。

### D9 的准确止线

- 此续编不是整个 D9 的无证书重证。原 structural phase/canonical-child/reference 覆盖、2862 个其他银行和别的证书族仍保留。
- Q8 细投影 margin 可以为负，而完整原对象银行为正；不得删去真实标记或把合法插回权均匀化。
- 私人根 rank cutoff、四点度界和固定 rooted-branch 权重均有各自真实失败控制。它们只否定精确辅助银行或过强概率界，另有平衡对，绝非 NB / D10 猜想反例。
- [旧 400 次增量](../d9-certificate-extraction/READ_FIRST.md)保存相邻路径有限事实与前轮门。参数化相邻银行仍是研究方向，不是由 607 次映射自动得到的一般定理。

## B. EL10：全部 exact-T3 / E-induced private-predecessor lift 的普通平衡

**[精确总定理](b1-exact-lift/EXACT_D10_ORDINARY_CLOSURE.md)**及**[最终独立组合审查](b1-exact-lift/EXACT_D10_ORDINARY_COMPOSITION_INDEPENDENT_REVIEW.md)**为本部分入口。

取任意有限原种子 P：恰两极小元 a,b；a 在除 a,b 外每点下；整个 b-private 部分恰为三点反链 T={x,y,z}，各点与 b 不比、严格下集均为 {a}；余点 C 全在 b 上，内部序及完整 T 签名可变。令 E 是诱导 C 中的理想，每点完整旧 T 签名恰为 {y,z}。加一个 u，仅由 a<u<x、u<C−E 生成新比较并取传递闭包，保 P induced。要求**完整实际 P+**的最大不可比度≤10。

则同一原均匀 LE(P+) 中存在某个不可比物理对，其先后概率在闭区间 [1/3,2/3]。无需 OLD seed moment；C 与真实尾部任意有限；无需 prime、Γ-all-high 或条件后缀均匀假设。不同分支可能返回不同原 pair，不授全类统一指定(u,b)或同一小菜单。

这不是所有 B1、所有 T4、任意 degree-ten 偏序或全 D10。旧指定(u,b)失效实例继续有效，因为普通存在性允许另一对平衡。也不证明 NB / 完整历史 guard 排除对象存在，或新增全历史净人口。

### EL10 的解析依赖与完备分支

[依赖读法](b1-exact-lift/DEPENDENCIES.md)列出本公开包中的承重组件。完整实际度给 0≤m=|E|≤k=|C−U(x)|≤7。

- 有含 x 的实际 C-minimum：既有 RC1/TL1/SG1/SP1/OP1 及原 dual-VG 守卫已穷尽；无此 minimum 且无 empty minimum 也已穷尽。
- zero-frontier+empty 部分经原单槽门仅剩六格。若至少两个 missing-x low C-minima、其中一个 empty，直接 [DG2 双 gap 定理](b1-exact-lift/TWO_LOW_MINIMUM_DOUBLE_GAP_CLOSURE.md)付款，允许任意额外 minima。
- 恰一个 low minimum 时，六格由 EC3/EC4、WB5/WB6、WB4/UL1 的真实原 root-bank 解析证明覆盖。这里 low 明确指**缺 x 且旧支持≤1的实际 C-minimum**，不能把 x-only 点送进 DG2。
- 每个银行候选保各自原上界（u/b≤5/9、y/b 与 z/b≤1/2），所以银行正性才能推出某一原 pair 平衡；不能裸把任意 signed bank 正性当作平衡对。

最终普通存在性路线**无 OLD moment、无计算机辅助正性证书依赖**。MC1/RT1/AFC1/TC1、ND1 与旧 fixed-pair 分类的 CA 状态并未被改写，它们不是 EL10 此证明的输入。此处“纯解析”仍包含明确的有限结构分类、闭式有限和、原词注入和代数不等式，不表示没有分类讨论。

## 文件与版本范围

本包包含数学正文、承重解析组件与研究内独审、部分原节点身份与去重计数摘要。旧组件稿中的 candidate / earlier residual 标签作为历史保留；当前状态以两份总入口及最终审查为准。原数学结论不由上传、哈希或程序运行成功来认证。

[SOURCE_BINDINGS.json](SOURCE_BINDINGS.json)列出原稿与公开副本的绑定及必要编辑说明。只省略本地执行路径或发布过程措辞，未复制原聊天、凭据或不相关个人资料。旧 400 次 D9 及 Q18 δ3 增量不删除。
