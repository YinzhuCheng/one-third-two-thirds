# S99 稳定编号与有类型依赖

日期：2026-10-10。所有状态表示研究稿中的证明地位；不表示外部审稿、首创或形式化认证。概率与范围见规范证明。

| 稳定编号 | 状态 | 准确内容 | 规范位置 |
|---|---|---|---|
| S99-RELEASE-SQUARE | PROOF_DRAFT | 原双极小入口、避入口链下，U=p²−Δ；单后继和双后继的两个充分闭合区间 | notes/PROOF.md B |
| S99-PREDECESSOR-GATE | PROOF_DRAFT | y 极小、u∥y，可非极小；U≥2p−d | notes/PROOF.md C |
| S99-MAJORITY-FORK | PROOF_DRAFT | 固定极小 y 无伙伴且有多数前置标签时，宽三终端必为双私有后继，p∈(2/3,7/9)、d>7/9 | notes/PROOF.md D |
| S99-MC3-R1 | PROOF_DRAFT | B={a} 时 min(Pr(a<x),Pr(a<y))<2/3，无宽度限制 | notes/MC3_R1.md |
| S99-GOOD-PAIR-INTERFACE | KNOWN_COROLLARY | 私有整个上集差为链时，Zaguia good-pair 的同一原律选择 | notes/PROOF.md E；LITERATURE.md 3 |
| S99-FIXED-MINIMUM-GUARD | FINITE_POSET | 五点真实宽三例：极小 y 无任何伙伴，虽有 7/10 多数入口 | notes/PROOF.md F.4 |
| S99-NONMINIMAL-SQUARE-GUARD | FINITE_POSET | C9⊔{y} 的第二链点使一般非极小版本 U≤p² 失败 | notes/PROOF.md F.2 |
| S99-NO-UNIFORM-MENU-MARGIN | INFINITE_FAMILY_OF_FINITE_POSETS | 真实 MC3 前提下菜单唯一好对余量趋零，并实现第2步联合大跳 | notes/EARLY_JUMP_FAMILY.md |
| S99-GATE-SQUARE-OPEN | OPEN | 候选 dU≤p²；已给相同严格下集条件模型的等价变换，无证明 | notes/PROOF.md G |

Notion Guards 的现有 Kind 枚举没有“有限偏序无限族”；对应无限参数族在那里使用 FINITE_POSET，并在范围中明确每个对象有限、参数无界，不把它误填为 INFINITE_LAW。

## 证明边与文献边

- S97-SHARED → S99-RELEASE-SQUARE：PROOF_DEPENDENCY，真实事件 U=R_x/E。
- S98-CHAIN-MARGINAL → S99-RELEASE-SQUARE：PROOF_DEPENDENCY，H²≥R_xR_y，即 Δ≥0。
- XYZ → S99-RELEASE-SQUARE：LITERATURE_INPUT，仅双后继分支。
- S99-PREDECESSOR-GATE + XYZ + w(P)≤3 → S99-MAJORITY-FORK：PROOF_DEPENDENCY。
- Chan–Pak §6.1 首两步矩阵 → S99-MC3-R1：LITERATURE_INPUT；不依赖 S98 的全链消元。
- S99-MC3-R1 + S95-AVOIDANCE → MC3 失败时第2–5步定位无R1例外：CONDITIONAL_SCOPE_REFINEMENT，未证明失败不存在。
- Zaguia good-pair → S99-GOOD-PAIR-INTERFACE：KNOWN_SPECIALIZATION，不是 S99 新的存在性定理。

## 精确反驳边

- S99-FIXED-MINIMUM-GUARD → “固定极小 y 有多数前置点便一定有伙伴”：REFUTES。
- S99-NONMINIMAL-SQUARE-GUARD → “上移后可继续无条件使用 U≤p²”：REFUTES。
- S99-NO-UNIFORM-MENU-MARGIN → “MC3 指定菜单有统一正平衡余量”：REFUTES。
- 同一无限族 → “所有真实早期联合大跳均不可能”：REFUTES。
- 以上反例均不反驳 MAIN33、WIDTH3、MC3、S98 原假设下的矩阵或能量定理。

## 尚缺的连接

- S99-MAJORITY-FORK → 原律兄弟对或下覆盖前沿的兼容平衡选择：OPEN_DIRECTION，尚无共同计数不等式。
- 相同严格下集两个标签 → S99-GATE-SQUARE-OPEN：OPEN，删除共同下集不保均匀律。
- S98 能量 + 实际候选的结构余量 → 原律同标签平衡：OPEN，必须配对标签、前缀质量和量级。
- MAIN33、一般 WIDTH3、MC3、TEN40 均维持 OPEN；U58 维持 UNDER_AUDIT。
