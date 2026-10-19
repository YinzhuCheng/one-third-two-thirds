# 非principal首次槽的赢家分解：精确混合项、可证子类与正号障碍

日期：2026-10-18。仅研究实际有限偏序均匀线性扩张的辅助槽矩不等式，不涉及原全局猜想的分类。以下一般公式与充分条件为本轮推导；不声称原创或文献完备。

## 结论先行

设有限非空偏序为 U，A,B 是非空上理想，f 是均匀随机线性扩张，

\[
R=\min f(A)-1,\quad T=\min f(B)-1,\quad r=\mathbb ER,\ s=\mathbb ET,
\quad N=\mathbb E[RT+\min(R,T)].
\]

将 A 按“哪一个极小元最先出现”分层，记赢家为 I，条件均值为

\[
r_i=\mathbb E[R\mid I=i],\quad s_i=\mathbb E[T\mid I=i],\quad d_i=s_i-r_i.
\]

得到精确等式

\[
\boxed{N-rs=\operatorname{Var}R+r+\Delta-\bar\epsilon,\qquad
\Delta=\operatorname{Cov}_I(r_i,d_i),\quad \bar\epsilon\ge0.}\tag{M}
\]

其中每层的 \(\epsilon_i\) 是已证 single-center 不等式的精确余量，并非未定符号项。由此：

1. **已证新充分条件。** 若所有赢家的 \(r_i\) 相等，则对任意非空 B（甚至无需 B 为上理想），
   \[
   \boxed{N-rs\le r^2+2r.}\tag{SC-equal}
   \]
   保持 A 的偏序自同构群在 \(\min_U A\) 上传递，足以保证赢家等均值。**自同构不必保持 B。** 全目标 T 另外要求 \(r\le s\)，或交换两侧后使用相同条件。
2. **混合项没有无条件负号。** 六点实际模型 \(U=C_2\sqcup C_3\sqcup\{x\}\)，取 A 为“C₂顶和 x”，B 为“C₃顶和 x”，两侧都非principal、互不包含，而且 \(r=23/12<s=43/20\)，但 \(\Delta=161/720>0\)。这不是已有三点 \(\operatorname{Cov}(R,T)\le\operatorname{Var}R\) 失败例。
3. **真正剩余条件更弱。** 当 \(r\le s\)，目标 T 恰好等价于
   \[
   \boxed{\Delta\le g_R+\bar\epsilon,\qquad
   g_R=r(r+1)-\operatorname{Var}R\ge0.}\tag{Slack}
   \]
   因而 \(\Delta\le0\) 只是充分条件，绝不是必要条件；正号示例仍满足 T。

## 1. 赢家分层确实是一个均匀偏序模型

令

\[
C=\min_U A=\{a\in A:\ \nexists b\in A\text{ with }b<_U a\}.
\]

C 是非空反链。每个 A 元素都在某个 C 元素上方，因此

\[
\min f(A)=\min_{c\in C}f(c).
\]

f 为严格秩排列，故赢家 \(I=\arg\min_{c\in C}f(c)\) 唯一。对每个 \(i\in C\)，定义 \(U_i\) 为在 U 中加入

\[
i<c\qquad(c\in C\setminus\{i\})
\]

再取传递闭包所得的关系。

### 1.1 无环及所有赢家概率为正

所有新边均从 i 出发。一条新产生的有向圈必须包含从某个 \(c\in C\setminus\{i\}\) 返回 i 的原 U 路径；这与 C 是反链矛盾。所以 \(U_i\) 是偏序。有限偏序存在至少一条线性扩张，故 \(e(U_i)>0\)。

### 1.2 事件与扩张集合逐一对应

U 的一个线性扩张 f 满足 \(I=i\)，当且仅当它同时满足 \(f(i)<f(c)\) 对所有 \(c\ne i\)；这又当且仅当 f 是 \(U_i\) 的线性扩张。因此，作为排列集合，

\[
\{f\in\operatorname{LE}(U):I(f)=i\}=\operatorname{LE}(U_i).
\]

原分布对每个排列等权，所以

\[
p_i:=\Pr(I=i)=\frac{e(U_i)}{e(U)}>0,
\qquad
\mathcal L(f\mid I=i)=\operatorname{Unif}\operatorname{LE}(U_i).
\]

这是对特定赢家事件的精确识别；没有把 \(R=k\) 或连续最小值等于 t 的条件分布冒充某个均匀偏序。

### 1.3 A 在每层成为 principal

每个 \(a\in A\) 位于某个 \(c\in C\) 上方，而 \(i\le_{U_i}c\)，故 \(i\le_{U_i}a\)。反过来，A 原为上理想；从 i 沿原边只能走在 A 内，沿新边也只到 A 内。因此 \(\uparrow_{U_i}i=A\)。特别地，条件于 \(I=i\)，

\[
R=f(i)-1.
\]

B 加关系后未必仍是上理想，但已有 single-center 结论允许另一侧为任意非空子集，所以不需要这一保持性。

## 2. 每层不等式、精确余量及总混合公式

沿用已证 principal 报告第 7 节的 single-center 结论：对任意有限偏序、固定点 i、任意非空子集 B，若 \(R=f(i)-1\) 且 \(T=\min f(B)-1\)，则

\[
\mathbb E[RT+\min(R,T)]-(\mathbb ER)(\mathbb ET)
\le\operatorname{Var}R+\mathbb ER.\tag{SC}
\]

在 \(U_i\) 中令

\[
v_i=\operatorname{Var}(R\mid I=i),\quad
N_i=\mathbb E[RT+\min(R,T)\mid I=i],
\]

并**定义精确非负余量**

\[
\epsilon_i=v_i+r_i-(N_i-r_is_i)\ge0,
\qquad \bar\epsilon=\sum_i p_i\epsilon_i.
\]

由定义和全期望公式，

\[
N-rs=\sum_i p_iv_i+r+
\underbrace{\left(\sum_i p_ir_is_i-rs\right)}_{\operatorname{Cov}_I(r_i,s_i)}
-\bar\epsilon.
\]

再用全方差公式

\[
\operatorname{Var}R=\sum_i p_iv_i+\operatorname{Var}_I(r_i)
\]

即得 (M)，因为

\[
\operatorname{Cov}_I(r_i,s_i)-\operatorname{Var}_I(r_i)
=\operatorname{Cov}_I(r_i,s_i-r_i)=\Delta.
\]

等价的两两表达式是

\[
\boxed{\Delta=\frac12\sum_{i,j\in C}p_ip_j(r_i-r_j)(d_i-d_j).}\tag{pair}
\]

这清楚显示：逐层 FKG 都成立，并不保证它们混合后仍满足同一个 single-center 界。缺的正是赢家均值与赢家相对延迟之间的协变方向，扣掉已有层内余量后才是实际损失。

## 3. 与连续 Shepp–FKG 证明逐项对齐

令 \(n=|U|\)、\(D=n+1\)，X 在 \(\mathcal O(U)\) 中均匀，

\[
W=\min_{a\in A}X_a,\quad V=\min_{b\in B}X_b,
\quad a=\mathbb EW,\ b=\mathbb EV.
\]

同一个赢家 I 只由坐标相对次序决定；条件于 \(I=i\)，X 在 \(\mathcal O(U_i)\) 均匀，边界重合为零测集。写 \(a_i=\mathbb E[W\mid I=i]=(r_i+1)/D\)、\(b_i=(s_i+1)/D\)。原 single-center 加下接链证明在每层给

\[
h_i:=\operatorname{Var}(W\mid I=i)-\operatorname{Cov}(W,V\mid I=i)
-\frac{a_i(b_i-a_i)}{D+1}\ge0.
\]

用全协方差及全方差公式，连续总体缺口恰为

\[
\boxed{\begin{aligned}
h&:=\operatorname{Var}W-\operatorname{Cov}(W,V)-\frac{a(b-a)}{D+1}\\
&=\sum_i p_ih_i-\frac{D}{D+1}\operatorname{Cov}_I(a_i,b_i-a_i).
\end{aligned}}\tag{OP-mix}
\]

因此，不能把 minimum 当新中心直接套 FKG；混合后有一个明确的中心切换项，而非遗失了一维普通坐标。

次序统计量的精确转换给

\[
D(D+1)h_i=\epsilon_i,\quad
D^2\operatorname{Cov}_I(a_i,b_i-a_i)=\Delta,
\]

以及

\[
D(D+1)h=\operatorname{Var}R+r-(N-rs)=\bar\epsilon-\Delta.
\]

这与 (M) 完全一致，保留了 \(n+1,n+2\) 偏移；没有从粗连续方差支配遗漏有限维校正。

## 4. Chan–Pak 对角界及准确的充分/必要关系

已直接核看 [Chan–Pak, Theorem 1.8，式 (1.16) 与 §6.3](https://arxiv.org/html/2211.16637v2)：量词为任意非空子集 A,B，**不要求相异或不交**。取两个子集都为 A，令 \(K=\min f(A)=R+1\)，得到

\[
\mathbb E[K^2+K]\le2(\mathbb EK)^2.
\]

逐项减一后

\[
\mathbb ER^2+3r+2\le2r^2+4r+2,
\qquad
\boxed{\operatorname{Var}R\le r(r+1).}\tag{CPdiag}
\]

故 \(g_R=r(r+1)-\operatorname{Var}R\ge0\)。由 (M)，无须假定 \(r\le s\)，总有精确恒等式

\[
\boxed{r^2+2r-(N-rs)=g_R+\bar\epsilon-\Delta.}\tag{exact-slack}
\]

所以：

- **单侧界的充要条件：** \(\Delta\le g_R+\bar\epsilon\)。当 \(r\le s\) 时，这也正是全目标 T 的充要条件。
- **只用边际余量的充分条件：** \(\Delta\le g_R\)。这比 \(\Delta\le0\) 弱，且不需计算层内混合矩。
- **简明充分条件：** \(\Delta\le0\)。由 (pair)，若对所有 i,j，\((r_i-r_j)(d_i-d_j)\le0\)，即赢家条件平均相对延迟与赢家槽均值反向排序，就满足此条件。
- **赢家等均值条件：** 若所有 \(r_i\) 相等，则 \(\Delta=0\)，对任意 B 得 (SC-equal)。这里不要求所有 \(s_i\) 相等。

也可只用条件 T 余量写出等价形式：令

\[
\eta_i=r_i(r_i+1)-v_i\ge0,\quad
\tau_i=\eta_i+\epsilon_i=r_i^2+2r_i-(N_i-r_is_i).
\]

则

\[
\Delta+2\operatorname{Var}_I(r_i)\le\sum_i p_i\tau_i
\]

与单侧目标等价。直接混合每层的二次均值界时多出的两个赢家均值项，正由全局边际余量与层内余量来支付；不能默认为零。

## 5. 自同构传递：一个真正的非principal一般子类

设 G 是 U 的一个自同构群，且每个 \(g\in G\) 保持 A，即 \(g(A)=A\)。假设 G 在 C 上作用传递。将扩张排列中的每个元素以 g 重命名，给出 \(\operatorname{LE}(U)\) 的保均匀双射，且

\[
I(gf)=gI(f),\qquad R(gf)=R(f).
\]

因此，它把 \(\{I=i,R=k\}\) 逐一对应到 \(\{I=gi,R=k\}\)，从而赢家概率相等，且 R 在各赢家条件下的**整个分布**相同。特别地，\(r_i=r\) 对所有 i 成立。

此论证从未作用到 T；所以 **g 不必保持 B**。一旦得到 \(r_i\) 等均值，对原本给定的任意 B，无论 \(s_i\) 如何变动，都有 \(\Delta=0\)。结合 (CPdiag) 与 (M) 证明 (SC-equal)。

例：U 中有两条等长同构链，A 是这两条链的顶点集合，其余偏序与两链的连接对交换两链保持对称，则 A 通常非principal，而赢家均值相等。本次固定精确检查还用了

\[
U=C_2\sqcup C_2\sqcup C_3,
\quad A=\{\text{前两链顶}\},\quad
B=\{\text{第一链顶、第三链顶}\}.
\]

交换前两链保持 A，却不保持 B。210 条扩张上，\(r_b=r_d=49/15\)，但 \(s_b=44/15\ne22/5=s_d\)；仍有 \(\Delta=0\)，且 \(r=49/15<s=11/3\)，所以新条件确实在 B 不对称时生效。

这是一项充分条件定理；不声称自同构传递是赢家等均值的必要条件，也不声称赢家等均值覆盖任意非principal A。

## 6. 六点正号障碍：较小均值侧也不能要求 Δ≤0

取

\[
U=\{a<b\}\sqcup\{c<d<e\}\sqcup\{x\},
\qquad A=\{b,x\},\quad B=\{e,x\}.
\]

A,B 均为非principal上理想，且互不包含。总扩张数为 \(6!/(2!3!)=60\)。C={b,x}；条件 \(I=b\) 等价于新增 b<x，得到两条 3 链，20 条扩张；另一层40条。

| I | p_i | r_i | s_i | d_i | v_i | N_i | ε_i |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| b | 1/3 | 5/2 | 7/2 | 1 | 21/20 | 109/10 | 7/5 |
| x | 2/3 | 13/8 | 59/40 | −3/20 | 539/320 | 209/40 | 77/160 |

于是

\[
\Delta=\frac13\frac23\left(\frac52-\frac{13}8\right)
\left(1+\frac3{20}\right)=\boxed{\frac{161}{720}>0}.
\]

总体精确数据为

\[
r=\frac{23}{12}<\frac{43}{20}=s,\quad
\operatorname{Var}R=\frac{1183}{720},\quad N=\frac{427}{60},
\]

\[
g_R=\frac{1421}{360},\qquad
\bar\epsilon=\frac{63}{80},\qquad
rs+r^2+2r-N=\frac{203}{45}>0.
\]

所以该例**只否定混合项的无条件非正性**，不否定 T；也没有再用一个 \(\operatorname{Cov}(R,T)>\operatorname{Var}R\) 例子替代本任务。

### 6.1 不是孤立的偶然正号：同一个可解家族

上述结构推广为

\[
U=C_2\sqcup C_m\sqcup\{x\},\quad
A=\{b,x\},\quad B=\{q,x\},
\]

其中 b,q 为两链顶，\(m\ge1\)。这不是扩大枚举，而是同一结构的显式积分计算。赢家 b/x 的概率始终为 1/3,2/3，并有

\[
r_b=\frac{m+2}{2},\quad r_x=\frac{3m+4}{8},
\]
\[
s_b=\frac{3m+8}{4}-\frac3{m+1},\qquad
s_x=\frac{3m+4}{8}-\frac3{(m+1)(m+2)}.
\]

推导：条件 b 获胜时三个元素 a,b,x 为一条 3 链；其顶坐标生存函数为 \(1-t^3\)。条件 x 获胜时三个元素为 \(a,x<b\)，x 的密度是 \(\tfrac32(1-t^2)\)，生存函数为 \(1-\tfrac32t+\tfrac12t^3\)。Cm 的顶坐标与它们独立，生存函数为 \(1-t^m\)。分别积分两生存函数之积，再乘总维度因子 \(n+1=m+4\) 并减一，即给上述 s 公式。r 公式来自同样条件坐标的一阶矩。

故

\[
\boxed{\Delta=\frac{(m+4)(m^2+6m-4)}{144(m+2)}>0\qquad(m\ge1).}
\]

同时

\[
r=\frac{5m+8}{12},\quad
s=\frac{m+2}{2}-\frac{m+4}{(m+1)(m+2)},
\]
\[
s-r=\frac{(m+4)(m+5)(m-2)}{12(m+1)(m+2)}.
\]

因此对所有 \(m\ge2\)，A 正是较小均值侧（m=2 为等均值），但 \(\Delta\) 仍严格正。这进一步排除了“只在较小均值侧，赢家混合项自动非正”这条补法。本报告没有用这一家族声称任何 T 反例。

## 7. 退化边界与既有principal结果的回收

- A 为 principal 时，C 只有一个元素，I 确定，\(\Delta=0\)；(M) 正好回收已证单中心界。A,B 都 principal 时，对两侧分别应用即可取最小二次项。这没有扩大既有定理的量词。
- 若只有 B principal 且 \(s\le r\)，交换两侧直接回收已证“较小均值侧principal”结论。若 principal 恰在较大均值侧，单靠该事实不够，不在本文中冒称已经覆盖。
- A=B 时，R=T、每个 \(d_i=0\)，所以 \(\Delta=0\)；逐层 \(\epsilon_i=0\)。此时 \(N-r^2=\operatorname{Var}R+r\)，T 直接由 (CPdiag) 得到，不需要任何自同构。
- 若 r=0，则 R=0 几乎处处、N=0，T 为等号；所有赢家层都正概率，故各 \(r_i=0\)，\(\Delta=0\)。s=0 同理交换。n=1 自动包含在内。
- 本文非空 A,B 假设保证最小值已定义；没有把空集哨兵约定悄然用于证明。

## 8. 计算范围与交付

`check_mixture.py` 只对预先固定的四个实际模型作精确有理数核查：家族 m=1,2,3，以及第5节 B 不保对称的七点模型；没有搜索偏序空间、没有抽样、没有增加有限分类。

脚本逐排列筛选实际扩张，核查：每个赢家概率严格正；赢家条件扩张集合与加入关系后的扩张集合逐一相同；每层 A 等于 principal 上理想；(M)、(OP-mix) 的连续/离散换算及所有表中数值。`verification.json` 保存完整精确数据，并保存六点正号例全部60条扩张。

**研究状态：** 已证明赢家等均值/自同构传递的非principal单侧子类；已准确定位并否定混合项 Δ 的无条件非正性；一般非principal槽目标未证明、未否定。最窄的剩余量为 (Slack)，而不是笼统地要求单中心 FKG 在最小值中心下仍成立。
