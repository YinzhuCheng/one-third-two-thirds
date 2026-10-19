# t=2 实际纤维计数：I 成链时两条端点不等式的证明

日期：2026-10-18。

## 0. 结论、量词与范围

**已证的非空结构子类。** 设有限实际偏序

\[
R=D\sqcup\{y,z\}\sqcup U
\]

满足全部 \(D<U\)，不存在 \(\{y,z\}<D\) 或 \(U<\{y,z\}\) 的关系，且 \(y,z\) 在 R 中可比。对每个整数 \(m\ge1\)，在 D/U 之间加入自治链 \(C_m=(c_1<\cdots<c_m)\)，两个外部点均与整条链不可比，所得实际偏序记为 \(P_m\)。D、U 的内部结构与大小任意，也允许空集。

则在各 \(P_m\) 的**全部实际线性扩张的均匀分布**下，严格有

\[
\Pr_{P_{m+1}}(c_1<y)>\Pr_{P_m}(c_1<y),
\qquad
\Pr_{P_{m+1}}(c_{m+1}<y)<\Pr_{P_m}(c_m<y).
\]

所以对全部 \(m\ge2\)，缩链 \(m\to m-1\) 的首/末端单调方向均正确。末端事件比较各自的末点，不把两个不同的原标签当成同一点。

证明同时得到题设两条七类实际计数不等式的**严格版本**。这里只完成 I 成链的子类；I 为反链的一般情形仍未证明，也未给出实际反例。不据此声称整列阈值保持或原猜想结论。

## 1. 七类计数与端点差：自含的计数核

对每个 \(\sigma\in\operatorname{LE}(R)\)，窗口是最后一个 D 点之后、最先一个 U 点之前的区段；D/U 为空时使用词首/词尾边界。窗内 I 点数记为 K。

- K=0：y 在窗前、窗后，分别计 \(A_0,B_0\)。
- K=1：y 在窗前、窗后、窗内，分别计 \(A_1,B_1,H\)。
- K=2：y 是两个窗内点中的第一、第二个，分别计 \(L,R_2\)。

这些数均直接计实际的外部线性扩张，不是任意指定的非负参数。置

\[
a=A_0+B_0,\quad b=A_1+B_1+H,\quad c=L+R_2,
\]
\[
u=A_0+H+R_2,\quad v=A_1+L,
\qquad
w=B_0+H+L,\quad x=B_1+R_2.
\]

每条 K 类外部扩张可插入自治链的方式数为 \(\binom{m+K}{K}\)，所以

\[
T_m=e(P_m)=a+b(m+1)+c\binom{m+2}{2}.
\]

逐窗数首端事件的补事件、以及末端事件，得到

\[
F_m:=\Pr_{P_m}(c_1<y)
=1-\frac{u+v(m+1)}{T_m},
\]
\[
G_m:=\Pr_{P_m}(c_m<y)
=\frac{w+x(m+1)}{T_m}.
\]

例如首端补事件 \(y<c_1\) 在 K=0 的窗前类贡献 \(A_0\)，在 K=1 的三类贡献 \((m+1)A_1+H\)，在 K=2 两类贡献 \((m+1)L+R_2\)，恰为上式分子。末端分子同理为 \(B_0+(m+1)B_1+H+L+(m+1)R_2\)。

对任意 r,s 定义

\[
\Delta_m(r,s)=cs\binom{m+2}{2}+cr(m+2)+br-as.
\]

交叉相乘直接给出

\[
F_{m+1}-F_m=\frac{\Delta_m(u,v)}{T_mT_{m+1}},
\qquad
G_{m+1}-G_m=-\frac{\Delta_m(w,x)}{T_mT_{m+1}}.
\]

并且

\[
\Delta_{m+1}(r,s)-\Delta_m(r,s)=c\,[s(m+2)+r].
\]

因此只要 r,s 非负、\(c>0\)、\(r+s>0\)，\(\Delta_m\) 随 m 严格增加。证明对全部 \(m\ge1\) 的严格单调，只需证明

\[
\boxed{u(b+3c)+v(3c-a)>0},\tag{E1}
\]
\[
\boxed{w(b+3c)+x(3c-a)>0}.\tag{E2}
\]

## 2. 实际可实现性提供的槽阶乘矩界

### 2.1 已核的外部定理与发表状态

只使用 Swee Hong Chan、Igor Pak 的 [Correlation inequalities for linear extensions，arXiv v2 PDF](https://arxiv.org/pdf/2211.16637v2)，**Theorem 1.1，第 1 页**的上界。精确形式是：若 Q 为 n>2 点有限偏序，\(a,b\) 是其中两个**不同的极小元**，则

\[
\frac{n}{n-1}
\le
\frac{e(Q)e(Q-a-b)}{e(Q-a)e(Q-b)}
\le 2.\tag{CP}
\]

不要求 a,b 是 Q 的全部极小元。本证明完全不用左侧下界，也不用任何未经核验的 FKG、正相关或子集秩对数凹断言。

[arXiv 官方记录](https://arxiv.org/abs/2211.16637) 给出的期刊信息为：Advances in Mathematics 458 (2024), Article 109954, 33 pp；[期刊 DOI](https://doi.org/10.1016/j.aim.2024.109954)。核定理用的是 2024-09-12 的 v2 预印本（25 页），不是把它误记为尚未发表的结果。

### 2.2 同后继极小克隆：适用条件逐项验证

令 V 为任意有限偏序，S 为 V 的一个上理想，允许 \(S=\varnothing\)。对均匀的 \(\beta\in\operatorname{LE}(V)\)，定义 Z 为：在第一个 S 点之前的 V 点数；S 空时取 \(Z=|V|\)。于是一个没有前驱、后继集恰为 S 的新点，可合法插入的槽数是 \(Z+1\)，包括最左边的槽。

构造 Q：在 V 上加入两个新点 a,b，它们互不可比，均无前驱，后继集均恰为 S。S 是上理想保证构造传递且没有额外旧点关系；a,b 确实是两个不同极小元。删一个/删两个均为 (CP) 所需的诱导子偏序。

记 \(k=e(V)>0\)、\(s=\mathbb E Z\)。固定一条旧扩张 \(\beta\)：

- 单克隆插入数为 \(Z+1\)。
- 双克隆若落在不同旧槽，有 \((Z+1)Z\) 种带标签分配；若同槽，有 \(2(Z+1)\) 种次序。合计 \((Z+1)(Z+2)\)。

因此

\[
e(Q-a-b)=k,\qquad e(Q-a)=e(Q-b)=k(s+1),
\]
\[
e(Q)=k\,\mathbb E[(Z+1)(Z+2)].
\]

若 V 非空，则 \(|Q|>2\)，可用 (CP)，得

\[
\mathbb E[(Z+1)(Z+2)]\le 2(s+1)^2.
\]

**完整保留槽偏移后**展开、移项：

\[
\mathbb E Z^2+3s+2\le 2s^2+4s+2
\quad\Longrightarrow\quad
\boxed{\mathbb E[Z(Z+1)]\le2s(s+1)}.\tag{FM}
\]

V 空时 Q 是两点反链，虽然不满足 (CP) 的 n>2，但 Z=s=0，(FM) 直接成立。这也处理了零槽及全部边界；没有除以 s。

## 3. I={y<z}：槽表示与实际均匀计数

置 \(h=e(D)e(U)>0\)，约定空偏序的扩张数为 1。删去 y,z 后，R 的每条基词唯一为

\[
\alpha\beta,\quad
\alpha\in\operatorname{LE}(D),\quad
\beta\in\operatorname{LE}(U),
\]

因为所有 D 都在所有 U 下方。在这个**辅助乘积计数空间**上取独立均匀的 \(\alpha,\beta\)；它不被混同为 R 上的均匀概率。每条 R 扩张与“基词＋带标签合法插入”唯一对应，故对辅助空间的插入数求和，恰给出真实外部计数。最终的 \(P_m\) 概率仍由实际整数计数除以 \(T_m\) 得到。

对 \(i\in\{y,z\}\)，记

- \(\ell_i(\alpha)\)：中央 D/U 边界槽左侧的合法旧槽数；
- \(r_i(\beta)\)：中央边界槽右侧的合法旧槽数。

中央槽永远合法，因此另计 1，不含在上述任一数中。左槽集合是 D 词槽的后缀，右槽集合是 U 词槽的前缀。由 y<z 的传递性，

\[
\operatorname{Pred}_D(y)\subseteq\operatorname{Pred}_D(z),
\quad
\operatorname{Succ}_U(z)\subseteq\operatorname{Succ}_U(y),
\]

所以逐词有

\[
\ell_y\ge\ell_z\ge0,\qquad 0\le r_y\le r_z.
\]

定义

\[
p=\mathbb E\ell_y,\qquad s=\mathbb E r_z,
\]
\[
M=\mathbb E\left[\ell_y\ell_z-\binom{\ell_z}{2}\right],
\quad
N=\mathbb E\left[r_y r_z-\binom{r_y}{2}\right].
\]

M,N 非负。固定 \(\alpha,\beta\) 后，要求 y 在 z 之前，直接数同侧槽及跨侧槽，七类贡献分别为

\[
L=1,\ R_2=0,\ A_1=\ell_y,\ B_1=0,\ H=r_z,
\]
\[
A_0=\ell_y\ell_z-\binom{\ell_z}{2}+\ell_y r_z,
\qquad
B_0=r_y r_z-\binom{r_y}{2}.
\]

这里等槽只有 y,z 一个合法次序，故减项是 \(\binom{\ell_z}{2}\) 或 \(\binom{r_y}{2}\)，不是减 \(\binom{\ell_z+1}{2}\) 等偏移版本。

对全部基词求和，并利用左右只分别依赖 \(\alpha,\beta\) 的独立性，得到真实七类计数

\[
\frac{A_0}{h}=M+ps,\quad \frac{B_0}{h}=N,
\quad \frac{A_1}{h}=p,\quad B_1=0,\quad\frac Hh=s,
\quad \frac Lh=1,\quad R_2=0.
\]

即

\[
\frac ah=M+ps+N,\quad\frac bh=p+s,\quad\frac ch=1,
\]
\[
\frac uh=M+ps+s,\quad\frac vh=p+1,
\quad\frac wh=N+s+1,\quad x=0.
\]

## 4. 用真实矩界闭合两条承重式

先控制唯一可能产生负项的 N。对每条 \(\beta\)，令 \(a=r_y,b=r_z\)，有 \(0\le a\le b\) 且

\[
ab-\binom a2\le\frac{b(b+1)}2,
\]

因为右侧减左侧恰为 \((b-a)(b-a+1)/2\ge0\)。对 \(U\) 的均匀扩张取期望，使用第 2 节的 (FM)，其中 S 取真实上理想 \(\operatorname{Succ}_U(z)\)，得到

\[
\boxed{N\le\frac12\mathbb E[r_z(r_z+1)]\le s(s+1)}.\tag{N}
\]

将七类计数代入 (E1)，除以 \(h^2\)：

\[
\begin{aligned}
\frac{u(b+3c)+v(3c-a)}{h^2}
&=(M+ps+s)(p+s+3)+(p+1)(3-M-ps-N)\\
&=M(s+2)+ps^2+3ps+3p+s^2+3s+3-(p+1)N\\
&\ge M(s+2)+2ps+3p+2s+3\\
&>0.
\end{aligned}
\]

最后一步只用 \(M,p,s\ge0\)，因此包括 p=s=0 的边界。此为首端承重式。

末端因为 x=0，直接有

\[
\frac{w(b+3c)+x(3c-a)}{h^2}
=(N+s+1)(p+s+3)>0.
\]

两条式子均严格，且 \(u+v\ge h>0,w+x\ge h>0,c=h>0\)，故第 1 节的差核把结论提升为**全部整数 m≥1**的严格单调。

## 5. I={z<y} 的对偶

将整个偏序取对偶，保留指定标签 y。此时 D/U 互换、链顺序反转，I 变为 y<z，满足上文所有条件。反转线性扩张是两个实际均匀分布之间的保测双射。

原偏序的 \(\Pr(c_1<y)\) 等于对偶的 \(1-\Pr(c_m^*<y)\)，原偏序的 \(\Pr(c_m<y)\) 等于对偶的 \(1-\Pr(c_1^*<y)\)。因此首、末两条严格单调交换后保留正确方向。

在七类记号上，这也体现为 z<y 时 v=0，首端承重式自动正；末端承重式由对偶的上面矩证明给出。不是假设未验证的 y,z 交换对称性。

## 6. 最初尝试与反链剩余 gap（未作推论）

最初对 I 反链也用了同一真实基词分解。若 \(p=E\ell_y,r=E\ell_z,q=Er_y,s=Er_z\)，并记

\[
M_0=E[\ell_y\ell_z+\min(\ell_y,\ell_z)],
\quad
N_0=E[r_y r_z+\min(r_y,r_z)],
\]

则精确有

\[
A_0/h=M_0+ps,\quad B_0/h=N_0+qr,
\quad A_1/h=p,\ B_1/h=q,\ H/h=r+s,\ L/h=R_2/h=1.
\]

第一条承重式因而精确变为

\[
(M_0+ps+r+s+1)(p+q+r+s+6)
 +(p+1)(6-M_0-N_0-ps-qr)\ge0.
\]

同样的双极小元定理确实可推出 \(N_0\le2qs+q+s\)，但这个粗混合矩上界代入后不保证所需式子非负；且反链时不再有 \(r_y\le r_z\) 的嵌套槽条件，不能使用链情形的逐词三角估计。这是该尝试的精确 gap。没有把任意形式参数的负值误称为实际反例，也没有重复有限枚举。

本文件只在本地写入。未修改其他项目、35/55 或外部文档。
