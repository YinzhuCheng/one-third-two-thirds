# S99 文献接口核查

日期：2026-10-10。状态：本轮一手来源定理陈述及相关证明段落核查；不是穷尽查新。MAIN33、一般 WIDTH3、MC3 仍未解决。

## 1. Chan–Pak：S98 基底准确，双插回总计数已有直接出处

Swee Hong Chan and Igor Pak, *Correlation inequalities for linear extensions*, arXiv:2211.16637v2。

- [§6.1 Proposition 6.1、equation (6.1)、Lemma 6.2](https://arxiv.org/html/2211.16637v2#S6.SS1)：给 R0 加孤立标记 a，取 k=2、a固定第三位，down 极小元主子矩阵恰是 S98 的真实首两步矩阵。非对角 e(R0−x−y)，对角为第一 x、第二新放行后继的完成数之和。|R0|≥2 时参数合法。
- [§6.3 Proof of Theorem 1.8](https://arxiv.org/html/2211.16637v2#S6.SS3)：原文已明确计算双极小元插回总数 ab+min(a,b)。S97 应据此归属；带方向 H/R 拆分及项目接口可作为自行推导记录。
- [§3.3 Corollary 3.10](https://arxiv.org/html/2211.16637v2#S3.SS3)：x,y 极小，v仅覆盖x、w仅覆盖y，给 e(P−x−y)^2≥e(P−x−v)e(P−y−w)。这里“unique cover”描述覆盖者无其他下覆盖点。Theorem 1.9 控制相应对角总和。

本轮未找到整条避入口链消元后的 W 或原律 p_s≤p² 的同一现成陈述；这不构成原创性认证。不能只靠每个局部2×2不等式任意求和，S98共享块与消元仍是当前证明的必要部分。

## 2. Shepp XYZ：本轮核对的可用形式

[Aires–Kahn, arXiv:2510.26134v1, Theorem 2.1](https://arxiv.org/html/2510.26134v1#S2) 载明同端点多事件正相关：Pr(z 在全部Y之前)≥∏_{y∈Y}Pr(z在y之前)，以及对偶形式。本轮核对的是该一手研究论文的定理表述，没有重审Shepp原始证明。

S99双私有后继只需经典三个标签的XYZ：若q_s=Pr(s<y)、q_t=Pr(t<y)，则 U=Pr(s<y或t<y)≤q_s+q_t−q_sq_t。它不提供单独的平方上界。

## 3. Zaguia：私有上锥链分支是已知 good-pair 结论

[Imed Zaguia, arXiv:1610.00809v3](https://arxiv.org/html/1610.00809v3)。D、U在该文指严格下集、上集。

- **Definition 1、Theorem 2：** D(a)⊆D(b)，U(b)\U(a)为链，Pr(a<b)≤1/2时，P有平衡对。项目中 y极小、↑u\↑y为链、Pr(u<y)>2/3，取(a,b)=(y,u)即适用。
- **§2无编号引理：** 交换移动点与私有链元素，证明逐个插槽质量单调不增；这正是本轮重推的链分支。应标为已知闭合接口。
- **Definition 5：** very good 要求相同下集且两个独占上集都为链；其自身不一定平衡。
- **Lemma 7、Theorem 8：** 若x<z、y⊥x,z且(y,z) critical，Q=P+(y<z)，则 q_Q<q_P≤2q_Q/(1+q_Q)，q_R=Pr_R(x<y)。因此q_Q∈[1/3,1/2]可安全传回P。critical条件是D(y)⊆D(z)、U(z)⊆U(y)。

本轮已核原文没有找到明确写为 U≥2p−d 的真实前驱门事件公式；该式须由S99自身交换证明支撑，不声称首创。

## 4. 待证平方门界的准确重述

S99记y极小、u⊥y，d=Pr_P(D_P(u)<y)，p=Pr_P(u<y)，U=Pr_P(某个u的私有后继<y)。以下只是等价变换，**不是 dU≤p² 的证明**。

令 Q=P+{v<y:v∈D_P(u)}。其均匀扩张律是原P条件D_P(u)<y的律；且D_Q(u)=D_Q(y)=D_P(u)，p_Q=p/d，U_Q=U/d。因此

    dU≤p²  ⇔  U_Q≤p_Q²。

它把候选化成相同严格下集的两个入口。删去共同下集通常不保均匀律，不能据此直接调用S98的最小入口结论；本轮没有找到合法的Stanley或Kahn–Saks秩计数实现。候选必须保持OPEN。
