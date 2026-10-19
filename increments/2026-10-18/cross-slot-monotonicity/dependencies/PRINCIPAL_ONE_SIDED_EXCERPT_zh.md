# 已审 principal 单侧槽界：本补充所需摘录

摘自《两个主上理想的辅助槽界 T：Shepp–FKG 与下接链证明》（2026-10-18）第 5—7 节。这里只保留本次推广的依赖接口和关键减一，不重复旧论文 PDF、页面图像、完整证明包或其检查数据。

## 引理与方向

U 为任意非空有限偏序，f 为均匀 LE(U) 的秩函数。取 x∈U、任意非空集合 B₀⊆U，记 A=f(x)、G=min_{v∈B₀}f(v)。令 R=A−1、S=G−1、r=ER、s=ES。则已审单侧结论为

E[RS+min(R,S)]−rs≤r²+2r。

只要求第一侧为单点秩；B₀ 可特别取任意非空上理想。它不自动给交换后的第二个单侧界，不能直接推出任意两个非 principal 上理想的对称 T。

应用于本次主稿时，第一侧应取 z：若 Succ_U(z)=↑u_z，则 R=C_z，r=s_主稿；第二侧取 y 的非空后继上理想，则 S=C_y，s=q_主稿。因此恰得 N−q_主稿 s_主稿≤s_主稿²+2s_主稿，不要求 s_主稿≤q_主稿。空上理想不纳入本引理的最小值，主稿已单独处理。

## 已审推导的关键接口

旧稿利用 Shepp 差坐标格上的 FKG 及在 U 下方序和 k 点链，再取 k→∞，对 order polytope 中的连续坐标 X 给出

Cov(X_x,min_{v∈B₀}X_v)≤Var(X_x)−EX_x(E min_{v∈B₀}X_v−EX_x)/(n+2)。

按均匀线性扩张分解 order polytope，并取均匀次序统计量，使用

E[U_(i)U_(j)]=(ij+min(i,j))/((n+1)(n+2))，

得离散秩式

Q−μν≤Var(A)+μ，

其中 Q=E[AG+min(A,G)]，μ=EA，ν=EG。Chan–Pak 对角秩界给 Var(A)≤μ(μ−1)。减一时

E[RS+min(R,S)]=Q−μ−ν，rs=μν−μ−ν+1，

所以左侧差为 Q−μν−1≤μ²−1=r²+2r。

本摘录保留依赖链和使用接口；Shepp 差坐标格、Beta 分解与极限的完整已审论证仍见此前 principal 引理主稿，不在本小补充中重复。

## 来源

- L. A. Shepp, The XYZ Conjecture and the FKG Inequality, Annals of Probability 10(3) (1982), 824–827. DOI：https://doi.org/10.1214/aop/1176993791
- Swee Hong Chan and Igor Pak, Correlation inequalities for linear extensions, Advances in Mathematics 458 (2024), 109954，Theorem 1.2 的对角特例。DOI：https://doi.org/10.1016/j.aim.2024.109954
- 已有 Notion principal 槽界归档：https://app.notion.com/p/3fd05a5b7caa8176b9c5cb4c6e697693

此处未重新检索文献或声称新颖性；仅保存本次已审推广所调用的旧引理。
