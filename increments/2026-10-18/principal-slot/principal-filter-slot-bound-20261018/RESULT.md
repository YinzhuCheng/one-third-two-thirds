# 两个主上理想的辅助槽界 T：Shepp–FKG 与下接链证明

日期：2026-10-18。范围限本辅助槽矩问题。本文不讨论原全局猜想的分类，不声称原创，也不将两个主上理想的结论推广为任意两个上理想的结论。

## 结论

**目标子类已经证明。** 设 U 是任意非空有限偏序，n=|U|≥1，x,y∈U 可以相同。设 f:U→[n] 是均匀随机线性扩张的秩函数，且

\[
S_y=\uparrow x,\qquad S_z=\uparrow y.
\]

那么它们的首次出现槽数恰为

\[
R_y=f(x)-1,\quad R_z=f(y)-1.
\]

置

\[
r=\mathbb E R_y,\quad s=\mathbb E R_z,\quad
N=\mathbb E\big[R_yR_z+\min(R_y,R_z)\big].
\]

则

\[
\boxed{N\le rs+\min\{r^2+2r,\ s^2+2s\}.}\tag{T-principal}
\]

这对 n=1、x=y、r=0 或 s=0 都成立。证明没有用“任意子集最小秩已经满足 T”，没有用子集最小秩的未证对数凹性，也没有用把单坐标条件耦合直接改成多元素最小值条件耦合的假命题。

还可得到一个直接的单侧推论：若只有 S_y=↑x 是主上理想，而 S_z 是任意非空上理想，则

\[
N-rs\le r^2+2r.\tag{one-sided}
\]

因此，若主上理想那侧满足 r≤s，T 也成立。**这不解决任意两个非主上理想。** 推论见第 7 节。

## 1. 原始来源、精确适用性与发表状态

1. L. A. Shepp, *The XYZ Conjecture and the FKG Inequality*, **The Annals of Probability 10(3) (1982), 824–827**，已发表，DOI [10.1214/aop/1176993791](https://doi.org/10.1214/aop/1176993791)。本次实际取得并核看了 [Penn 库原始扫描本](https://repository.upenn.edu/server/api/core/bitstreams/dc03f00d-299d-45e9-b52a-4c98a8026617/content)（[库记录](https://repository.upenn.edu/handle/20.500.14332/47708)）。承重点为 pp.824–826：FKG 的式 (1.3)–(1.5)，§2 的差坐标偏序 (2.1)、格运算 (2.2)–(2.3)，以及偏序条件信息的保持性 (2.9)–(2.10)。这些允许任意递增实函数，不要求有关三点互不可比。
2. Swee Hong Chan and Igor Pak, *Correlation inequalities for linear extensions*, **Advances in Mathematics 458 (2024), 109954**，已发表，DOI [10.1016/j.aim.2024.109954](https://doi.org/10.1016/j.aim.2024.109954)。[作者存稿](https://www.math.ucla.edu/~pak/papers/Correlation17.pdf) p.2, Theorem 1.2，及 [arXiv v2 的同一定理](https://arxiv.org/html/2211.16637v2) 给出含对角的秩混合矩界；这里只使用其 x=y 的特例。
3. Max Aires, *Proof of the Kahn–Saks Conjecture*, [arXiv:2609.30895v1](https://arxiv.org/html/2609.30895v1#S2), 2026-09-25，§2 式 (8) 明确陈述下文的连续协方差式，量词为任意相异三点，并归于 Shepp。这里只把它作为定位线索；本证明从 Shepp 原始有限格 FKG 论证直接推出所需连续式，不依赖 Aires 主定理或其发表状态。

**引用精度提醒。** Shepp 原文显式陈述的主结果 (1.1) 是比较事件的 XYZ 不等式。这里的连续协方差式不是原文原样列出的编号命题；它是原文差坐标格上 FKG 的直接推论。下面展开这一推论，避免把事件版不经论证地替换成随机变量版。

## 2. 从 Shepp 原始格序得到连续差值协方差

设 P 是任意有限偏序，F 在其 order polytope

\[
\mathcal O(P)=\{u\in[0,1]^P:u_i\le u_j\text{ whenever }i<_Pj\}
\]

中均匀分布。固定中心 b∈P。所需结论是

\[
\operatorname{Cov}(F(a)-F(b),F(c)-F(b))\ge0,\tag{same-center}
\]

从而

\[
\boxed{\operatorname{Cov}(F(b)-F(a),F(c)-F(b))\le0.}\tag{XYZ-cont}
\]

a,b,c 相异时正是所用的三点形式；相同点造成的退化情况也无问题。

为完整核查，用整数 m≥1 作有限格逼近。令 q_i∈{0,…,m} 且 q_i≤q_j 当 i<_Pj；所有合法 q 等可能。变换为

\[
t=-q_b,\qquad d_i=q_i-q_b\quad(i\ne b),\qquad d_b=0.
\]

合法域由

\[
-m\le t\le0,\quad t\le d_i\le t+m,\quad
 d_i\le d_j\ (i<_Pj)
\]

刻画，其中涉及 b 的 d_b 解释为常数 0。该变换是整数点一一对应，并且是原始连续空间的行列式绝对值为 1 的线性变换。

此域对所有变量 (t,(d_i)_{i≠b}) 的坐标 min、max 封闭。理由是每条约束均为单坐标界或差值界 u_i≤u_j+c；两组满足这种界的点，其坐标 min 和坐标 max 也满足同一界。因此它是有限乘积格的分配子格，均匀权重满足 FKG 的 log-supermodularity 条件。两个坐标函数 d_a,d_c 都递增，所以

\[
\operatorname{Cov}(q_a-q_b,q_c-q_b)\ge0.
\]

除以 m² 后，让 m→∞。均匀格点 Riemann 和收敛到满维多面体 O(P) 上的均匀 Lebesgue 分布；其边界测度为零，所有函数有界，故前两阶矩均收敛。这证明 (same-center) 和 (XYZ-cont)。这里不需要三点间的任何可比性假设，也不需要中心为极小或极大点。

这与 Shepp (2.1) 的偏序完全一致：它是对 (−q_b,(q_i−q_b)_{i≠b}) 施加普通坐标序。原文 (2.2)–(2.3) 给出同一 min/max 格运算。

## 3. 在 U 下方序和一条 k 点链：分布逐项核查

固定原来的 U、n、x、y，不改变 U 的均匀 order-polytope 分布。对每个正整数 k，构造

\[
P_k=C_k\oplus U,
\]

即 k 点链的每一点都小于 U 的每一点。令链末点为 z，F^(k) 在 O(P_k) 中均匀，记 Z=F^(k)(z)。在 Z=z_0 条件下：

- 其余 k−1 个链坐标形成 [0,z_0] 中的有序单纯形，体积 z_0^{k−1}/(k−1)!；
- U 的坐标域是 z_0+(1−z_0)O(U)，体积 (1−z_0)^n vol(O(U))。

所以

\[
Z\sim\operatorname{Beta}(k,n+1),\qquad S:=1-Z\sim\operatorname{Beta}(n+1,k).
\]

而归一化的 U 坐标

\[
X_v=\frac{F^{(k)}(v)-Z}{1-Z}
\]

条件于 Z 总是在 O(U) 中均匀，因此 X 与 S 独立，X 的分布对每个 k 都是**同一个固定 U 的均匀分布**。可写

\[
F^{(k)}(v)=Z+SX_v.
\]

Beta 矩为

\[
\mathbb ES=\frac{n+1}{n+k+1},\qquad
\mathbb ES^2=\frac{(n+1)(n+2)}{(n+k+1)(n+k+2)},
\]

\[
\operatorname{Var}S=\frac{(n+1)k}{(n+k+1)^2(n+k+2)},\qquad
\kappa_k:=\frac{\operatorname{Var}S}{\mathbb ES^2}
=\frac{k}{(n+2)(n+k+1)}
\longrightarrow\frac1{n+2}.
\]

维度 n+k、n+1、n+2 的偏移均如上，没有把链末点误算为第 k+1 个链点。

## 4. 连续协方差界与安全取极限

先取 x≠y。对 P_k 的三点 (z,x,y) 应用 (XYZ-cont)：

\[
0\ge\operatorname{Cov}(F^{(k)}(x)-Z,F^{(k)}(y)-F^{(k)}(x))
=\operatorname{Cov}(SX_x,S(X_y-X_x)).
\]

置 a=EX_x,b=EX_y。利用独立性展开，得到

\[
0\ge \mathbb ES^2\big(\operatorname{Cov}(X_x,X_y)-\operatorname{Var}X_x\big)
+\operatorname{Var}S\,a(b-a).
\]

于是对每个有限 k 都有

\[
\operatorname{Cov}(X_x,X_y)
\le\operatorname{Var}X_x-\kappa_k a(b-a).
\]

U、X、a、b 以及两个协方差/方差在此全部固定。只对这个已经成立的实数不等式取 k→∞，得

\[
\boxed{\operatorname{Cov}(X_x,X_y)
\le\operatorname{Var}X_x-\frac{a(b-a)}{n+2}.}\tag{continuous-bound}
\]

无需假定 b≥a；即使差为负，数列右侧仍收敛，取极限仍然合法。没有把 n 固定的分布误换成另一个极限分布。

## 5. 精确离散转换

设 A=f(x),B=f(y),μ=EA,ν=EB，并令

\[
Q=\mathbb E[AB+\min(A,B)].
\]

O(U) 按各线性扩张分成等体积单纯形，所以可先均匀选 f，再独立取 n 个独立 U[0,1] 的次序统计量 U_(1)<…<U_(n)，令 X_v=U_(f(v))。对 1≤i,j≤n，

\[
\mathbb E U_{(i)}=\frac{i}{n+1},\qquad
\mathbb E[U_{(i)}U_{(j)}]
=\frac{ij+\min(i,j)}{(n+1)(n+2)}.
\]

第二式可直接由 n+1 个均匀次序统计量间距的 Dirichlet(1,…,1) 矩核查：异位置间距乘积的期望为 1/((n+1)(n+2))，同位置为其两倍；U_(i)U_(j) 的展开恰有 min(i,j) 个同位置项。它对 i=j 同样成立，给出 i(i+1) 的分子。因此

\[
a=\frac\mu{n+1},\quad b=\frac\nu{n+1},
\]

\[
\operatorname{Cov}(X_x,X_y)
=\frac Q{(n+1)(n+2)}-\frac{\mu\nu}{(n+1)^2},
\]

\[
\operatorname{Var}X_x
=\frac{\mathbb EA^2+\mu}{(n+1)(n+2)}-\frac{\mu^2}{(n+1)^2}.
\]

代入 (continuous-bound)，乘以 (n+1)(n+2)，并合并乘积均值项，得到

\[
Q\le \mathbb EA^2+\mu+\mu\nu-\mu^2,
\]

即

\[
\boxed{Q-\mu\nu\le\operatorname{Var}A+\mu.}\tag{discrete-bound}
\]

交换 x,y 同样得到 Q−μν≤Var B+ν。若 x=y，此时 Q=EA²+μ，(discrete-bound) 本身就是等式，无须调用相异三点的 XYZ。

## 6. Chan–Pak 对角界与完成 T

Chan–Pak Theorem 1.2 取 x=y，得

\[
\mathbb EA^2+\mathbb EA\le2(\mathbb EA)^2,
\]

所以

\[
\operatorname{Var}A\le\mu(\mu-1).
\]

同理 Var B≤ν(ν−1)。另一方面，对槽变量的减一逐项计算是

\[
N=Q-\mu-\nu,\qquad rs=(\mu-1)(\nu-1),
\]

故

\[
N-rs=Q-\mu\nu-1
\le\operatorname{Var}A+\mu-1
\le\mu^2-1=r^2+2r.
\]

交换两侧再取较小值，得到 (T-principal)。当 x=y，直接由同一 Chan–Pak 对角界得到同一个计算。n=1 时唯一秩为 1，两个槽变量都是 0，等号成立。

## 7. 同证法的单侧推论：一个主上理想足够控制该侧

这里仍要求第一侧是单点秩 A=f(x)。令 B_0⊆U 为任意非空集合（特别可取任意非空上理想），置

\[
G=\min_{v\in B_0}f(v),\quad H=\min_{v\in B_0}X_v.
\]

第 2 节以 x 为中心的差坐标中，

\[
H-X_x=\min_{v\in B_0}(X_v-X_x)
\]

是递增函数，包括 x∈B_0 时的常数 0 分量也无妨。与同一个差坐标 F^(k)(z)−F^(k)(x) 应用 FKG，得

\[
\operatorname{Cov}(F^{(k)}(x)-Z,\min_{v\in B_0}F^{(k)}(v)-F^{(k)}(x))\le0.
\]

因为 S≥0，min_v F^(k)(v)=Z+SH。因此第 4 节同样适用于 (X_x,H)，并给

\[
\operatorname{Cov}(X_x,H)\le\operatorname{Var}X_x-
\frac{\mathbb EX_x(\mathbb EH-\mathbb EX_x)}{n+2}.
\]

关键离散转换也完全相同：给定 f，H=U_(G)，所以

\[
\mathbb E[X_xH]=
\frac{\mathbb E[AG+\min(A,G)]}{(n+1)(n+2)}.
\]

于是

\[
\mathbb E[AG+\min(A,G)]-(\mathbb EA)(\mathbb EG)
\le\operatorname{Var}A+\mathbb EA.
\]

令 R=A−1,T=G−1,r=ER,s=ET，仅使用 A 的 Chan–Pak 对角界，就得到 (one-sided)。若 r≤s，函数 u↦u²+2u 在 u≥0 上递增，故这恰为 T 所需的较小侧界。

这一步**没有**将多元素最小值作为新的格中心，没有使用其条件耦合，也没有得到交换后的第二个单侧界。两个非主上理想时，原证明仍缺少单点中心。

## 8. 少量实际偏序独立检查

实际运行 `python check_actual.py`，输出保存在 `actual_checks.json`。这是预先固定的七个小结构：单点、三点反链、四点链、二点链加孤点、菱形、3链与2链的不交并、一个六点非对称偏序。全部通过枚举排列筛选合法线性扩张，用 Python Fraction 作精确有理数运算。

- 共 35 条实际线性扩张；没有抽样扩张、没有蒙特卡洛。
- 检查 26 个 Chan–Pak 对角边际，112 个有序 principal 对的 T。
- 检查 194 个“第一侧 principal、第二侧非空 upset”组合的单侧结论。
- 对 112 个有序 principal 对各取 k=1,2,5，336 次直接在 C_k⊕U 的秩次序统计量中算差值协方差，并与 Beta 分解展开结果精确比较；两者相等，且协方差均≤0。

这些只用来检测符号、偏移、有限 k 与取极限前的公式，不是一般定理的证明，不是任何规模的偏序穷尽分类，也没有扩大参数反例搜索。

## 交付与证明状态

一般性的两个 principal-filter 结论 (T-principal) 已由上述完整推导证明，依赖已发表的有限格 FKG/Shepp 格构造和 Chan–Pak 对角界。一个 principal-filter 的单侧推论也由同样论证证明。任意两个上理想的 T 未在本文证明或否定。

本目录包含本结果、精确检查脚本及输出、核对用的 Shepp 原始 PDF 与页面 OCR/图像；没有对外写入或计算文件散列值。
