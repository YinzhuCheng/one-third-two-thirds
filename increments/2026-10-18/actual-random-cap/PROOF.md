# 实际独立随机 cap 槽：精确协方差恒等式与一般上界

日期：2026-10-18。范围严格限定于有限偏序均匀线性扩张中的缩链辅助槽 T、C；不转向原全局猜想，不搜索新的偏序族。下面一般恒等式及其与已知 Chan–Pak 对角界的组合是本轮推导；不声称文献首创。

## 1. 定理与结论

令

\[
U=W\sqcup V,\qquad a=|W|\ge0,\quad b=|V|\ge1,
\]

表示两个有限偏序的不交并：两块之间没有任何可比关系，各块内部关系任意。令 S 为 W 中的上理想，允许 S 为空；取两个非空 filters

\[
A=V\cup S,\qquad B=V.
\]

对 U 的均匀随机线性扩张秩函数 f，使用一基秩减一的首次槽

\[
R=\min f(A)-1,\qquad T=\min f(B)-1,
\qquad r=\mathbb ER,\quad s=\mathbb ET.
\]

则

\[
R\le T,\qquad 0\le r\le s=\frac{a}{b+1}.
\]

**精确协方差恒等式为**

\[
\boxed{
\operatorname{Cov}(R,T)
=\frac{b}{2(b+1)}\big(\mathbb E R^2+r\big).
}\tag{1}
\]

因此有比 C 更强的上界

\[
\boxed{
\operatorname{Cov}(R,T)
\le\frac{b}{b+1}\,r(r+1)
\le r(r+1).
}\tag{2}
\]

设

\[
g_R=r(r+1)-\operatorname{Var}R\ge0.
\]

则 T 与 C 有相同的**精确非负余量**

\[
\boxed{
\begin{aligned}
M
&:=r(r+1)-\operatorname{Cov}(R,T)\\
&=rs+r^2+2r-\mathbb E[RT+\min(R,T)]\\
&=\frac{r(r+1)}{b+1}+\frac{b}{2(b+1)}g_R
\ \ge\ \frac{r(r+1)}{b+1}.
\end{aligned}
}\tag{3}
\]

当 r>0 时 M 严格为正；当 r=0 时 R 恒为 0，M=0。不能在零槽退化时宣称严格不等式。对本定理的上理想 S，r>0 等价于 S≠W，即 A≠U。

本定理允许 W 任意，因而 cap 可以随机；不要求 S principal，不要求 cap 或首次槽具有 log-concavity、IFR 或 NBU。

## 2. 均匀 shuffle 与随机 cap 的实际来源

每条 U 线性扩张唯一对应三项：

1. W 的一条内部线性扩张；
2. V 的一条内部线性扩张；
3. 一个含 a 个 W 字母、b 个 V 字母的 shuffle 字。

每对内部扩张都对应恰好 \(\binom{a+b}{a}\) 个 shuffle，故在均匀 U 扩张中，三项独立，且各自在自身有限空间中均匀。这并不把内部点当作独立抽样，也不依赖任一块为链。

令 J 为 shuffle 中首次 V 前的 W 元素数。令 K 为 W 内部扩张中首次 S 前的 W 元素数：当 S 非空时

\[
K=\min f_W(S)-1\in\{0,\ldots,a-1\};
\]

当 S 为空时约定 K=a。于是 J 与 K 独立，且

\[
\boxed{T=J,\qquad R=\min(J,K).}\tag{4}
\]

逐扩张核对 (4)：

- 若 J<K，则前 J 个点均属于 W\S，第 J+1 个点在 V，首次命中 A 的槽为 J。
- 若 J>K，则前 K 个点均属于 W\S，第 K+1 个点在 S，首次槽为 K。
- 若 J=K，则前 K 个点均属于 W\S，第 K+1 个点无论在 V 还是 S，都属于 A，首次槽仍为 K。
- 若 S 为空，则 J≤a=K，A=B=V，R=T=J。

因此这里 cap 的减一偏移完全由“首次命中前的元素个数”确定，没有再加减一。

## 3. 负超几何尾与条件剩余均值

对 \(0\le i\le a\)，令

\[
t_i=\Pr(J\ge i)
=\frac{(a)_{\underline i}}{(a+b)_{\underline i}},
\qquad t_0=1,
\]

其中下标横线表示下降阶乘；对 i>a 置 \(t_i=0\)。这是 shuffle 前 i 个字母均为 W 的概率。

均值

\[
\boxed{s=\mathbb EJ=\frac{a}{b+1}}\tag{5}
\]

可由 b 个 V 将 a 个 W 分成 b+1 个间隙的对称性得到：均匀 shuffle 一一对应总和为 a 的均匀弱分拆，所有间隙等均值。

条件于 J≥i，已经读走 i 个 W，余下字仍然是含 a−i 个 W、b 个 V 的均匀 shuffle。因此

\[
\begin{aligned}
\mathbb E[J\mid J\ge i]
&=i+\frac{a-i}{b+1}\\
&=s+\frac{ib}{b+1}.
\end{aligned}
\tag{6}
\]

当 i=a 时，条件下 J=a；(6) 的右边也恰为 a。若 a=0，则以下所有正指标尾和为空，不必形成任何条件期望。

再令

\[
q_i=\Pr(K\ge i),\qquad
p_i=\Pr(R\ge i)=q_i t_i\quad(1\le i\le a).
\tag{7}
\]

(7) 只使用 J、K 独立；完全没有要求 \(q_i\) 的尾比值单调。

## 4. 精确协方差：直接对无条件尾事件求和

R 为非负整数变量，故逐样本有

\[
R=\sum_{i=1}^{a}\boldsymbol1_{\{R\ge i\}}.
\]

由独立性和 (6)，

\[
\begin{aligned}
\operatorname{Cov}(\boldsymbol1_{\{R\ge i\}},J)
&=\mathbb E[J\boldsymbol1_{\{K\ge i\}}\boldsymbol1_{\{J\ge i\}}]
-s\,q_it_i\\
&=q_it_i\big(\mathbb E[J\mid J\ge i]-s\big)\\
&=\frac{b}{b+1}\,i q_it_i.
\end{aligned}
\]

所以

\[
\boxed{
\operatorname{Cov}(R,J)
=\frac{b}{b+1}\sum_{i=1}^{a}i q_it_i.
}\tag{8}
\]

另一方面，标准离散尾和逐项给出

\[
\mathbb ER=\sum_{i=1}^{a}p_i,
\qquad
\mathbb ER^2=\sum_{i=1}^{a}(2i-1)p_i,
\]

故

\[
\boxed{\sum_{i=1}^{a}i q_it_i
=\frac{\mathbb ER^2+r}{2}.}\tag{9}
\]

结合 T=J 即得 (1)。这个推导不先条件于 K 使用二次均值上界再混合，因此不存在将 \(\mathbb E[r_K^2]\) 偷换成 \((\mathbb E r_K)^2\) 的步骤。

## 5. 实际槽的 Chan–Pak 对角界

本轮直接重开核看了 [Chan–Pak, *Correlation inequalities for linear extensions*, Theorem 1.8, (1.16)](https://arxiv.org/html/2211.16637v2)。该定理允许任意两个非空子集，未要求它们相异或不交。取两个子集都为 A，令

\[
H=\min f(A)=R+1,
\]

则定理给

\[
\mathbb E[H^2+H]\le2(\mathbb EH)^2.
\]

逐项换回零基槽：

\[
\mathbb ER^2+3r+2\le2r^2+4r+2,
\]

于是

\[
\boxed{
\mathbb ER^2+r\le2r(r+1),
\qquad \operatorname{Var}R\le r(r+1).
}\tag{10}
\]

这里使用的 R 确实是原 U 均匀线性扩张中实际非空集合 A 的首次槽，满足外部定理的全部假设。A 包含非空的 V，即使 S 为空也不会出现空集合问题。并且外部定理甚至不要求 A 为上理想。

把 (10) 代入 (1) 即得 (2)。另外

\[
\mathbb ER^2+r
=2r(r+1)-g_R,
\]

代回 (1) 后即得到 (3) 的精确余量分解。

## 6. 嵌套性与 T、C 的等价

本任务的两个辅助槽目标为

\[
\mathrm T:\quad
N:=\mathbb E[RT+\min(R,T)]
\le rs+\min\{r^2+2r,s^2+2s\},
\]

\[
\mathrm C:\quad
\operatorname{Cov}(R,T)
\le\min\{r^2+r,s^2+s\}.
\]

由于 A⊇B，逐样本 R≤T，故 r≤s、\(\min(R,T)=R\)。非负轴上 x²+2x 与 x²+x 均单调递增，因而

\[
N-rs=\operatorname{Cov}(R,T)+r,
\]

并且两个目标分别化为

\[
\operatorname{Cov}(R,T)+r\le r^2+2r,
\qquad
\operatorname{Cov}(R,T)\le r^2+r.
\]

两者严格等价，余量正是 (3)。因此 (2) 同时证明本整个结构族的 T 和 C。

关于严格性：若 S=W，则 A=U，R=0。反之，若 S 是真上理想，则 W\S 为非空下理想，包含 W 的一个极小元 x。x 也是 U 的极小元，故至少一条 U 线性扩张以 x 开始；该扩张 R≥1，且均匀概率为正，所以 r>0。由 (3)，此时 T、C 都严格。

## 7. 边界、随机性与抽象反例的界限

### 7.1 所有端点

- **a=0：** W=S=∅，A=B=U=V，J=K=R=T=0。所有正指标尾和为空，(1)–(3) 都成立且取等号。
- **S=∅：** K=a，R=T=J，q_i=1 对 1≤i≤a。没有空 filter；A=B=V 非空。
- **S=W：** K=0（a=0 时也为 0），R=0，T=J，r=0、Cov=0、M=0。
- **b=1：** 没有奇异分母；J 在 0,…,a 上均匀，(6) 中系数为 1/2。
- **S 非空且 proper：** K 可以真正随机并可取 0。证明不要求 K 确定，也不假定其分布有任何 log-concavity。

b≥1 是 B 非空及本 shuffle 等待模型的约束。本文不对空 B 定义首次槽，也不把 b=0 强行代入。

### 7.2 旧抽象随机 cap 反例为何不冲突

既有 `nested-prefix-slot-bound-20261018/RESULT.md` 附录 A 使用

\[
\Pr(J=0,1,2,3)=\left(\tfrac12,\tfrac14,\tfrac18,\tfrac18\right),
\qquad
\Pr(K=0)=\tfrac9{10},\quad\Pr(K=3)=\tfrac1{10},
\]

且 J、K 独立。该例确实否定“任意 NBU 的 J + 任意独立随机 K”能自动保留确定截断界；本文没有否定这个反例。

在该例中 R=J∧K 满足

\[
r=\frac7{80},\qquad
\mathbb ER^2=\frac3{16},\qquad
\operatorname{Var}R=\frac{1151}{6400},
\]

而

\[
r(r+1)=\frac{609}{6400},\qquad
g_R=-\frac{271}{3200}<0.
\]

所以该 R 不可能是任何均匀有限偏序扩张中某一固定非空集合的实际首次槽，已经违反 (10)。该 J 也不是本文的有限 shuffle 负超几何 J。本文同时使用特定 J 的条件均值 (6) 与实际 R 的对角界 (10)，并非声称任意独立 cap 均成立。

作为一个额外的**固定纯抽象控制**，即使只保留真正的 shuffle J，也仍不能任意选择 K：取 a=6、b=1，使 J 在 0,…,6 上均匀，独立地令 K 以 9/10 取 0、以 1/10 取 6。则

\[
r=\frac3{10},\qquad
\operatorname{Cov}(J\wedge K,J)=\frac25
>\frac{39}{100}=r(r+1),
\]

同时

\[
\operatorname{Var}(J\wedge K)=\frac{121}{100},
\qquad g_R=-\frac{41}{50}<0.
\]

该 cap 同样不是固定 S 的实际槽。这仅隔离“实际 cap”约束的作用，不是 actual 反例，也不是参数搜索。

## 8. 少量固定 exact 检查

本目录 `verify_fixed_cases.py` 只核验预先写明的 5 个小偏序和上述 2 个纯抽象控制；未生成参数空间、随机偏序或反例搜索。实际对象直接枚举其线性扩张，用 `fractions.Fraction` 精确比较：

- J、K 联合分布的独立性；
- R=J∧K 与 T=J 的逐扩张身份；
- 所有尾概率、条件均值、协方差恒等式；
- CP 对角、加强界与精确 T/C 余量。

一个真正非principal、随机 cap 的固定例为

\[
W=C_2\sqcup C_2,\qquad V=C_2,
\qquad S=\{\text{W 中两条链的顶点}\}.
\]

90 条 U 线性扩张上，

\[
\Pr(K=1)=\frac13,\qquad \Pr(K=2)=\frac23,
\]

\[
r=\frac{14}{15},\quad s=\frac43,\quad
\mathbb ER^2=\frac{22}{15},\quad
\operatorname{Cov}(R,T)=\frac45,
\]

\[
g_R=\frac{272}{225},\qquad
\sum_i i q_it_i=\frac65,
\qquad M=\frac{226}{225}.
\]

一个可取零的实际随机 cap 控制为 W 的两点反链、V 的单点、S 为 W 中一点。此时 K 在 0、1 上等概率，且

\[
r=\frac13,\qquad s=1,\qquad
\operatorname{Cov}(R,T)=\frac16,\qquad M=\frac5{18}.
\]

另外三个实际检查分别覆盖 S=∅、S=W、a=0。所有断言通过；完整有理数结果在 `verification.json`，运行记录在 `verification.log`。

## 9. 合并推论：嵌套 filters 中任意一个是独立块

设 U 为有限非空偏序，\(\varnothing\ne G\subseteq F\subseteq U\) 为两个上理想。称 H 是 U 的独立块，是指 H 与其补集之间没有任何可比关系；H 自身允许为任意偏序，甚至不连通。若 **F、G 中至少一个是独立块**，则它们的首次槽满足 T 和 C。

证明分为两个已覆盖情形，不需要它们同时为独立块。

1. **较大 filter F 是独立块。** 写 \(U=(U\setminus F)\sqcup F\)，G 为 F 中非空上理想。直接套用已审的 `nested-chain-slot-formula-20261018/RESULT.md` 主定理 (G1)–(G3)。其中 b=|F|、a=|U\F|，h 为 F 内部首次 G 的槽均值；较小均值为 \(r=a/(b+1)\)。已有精确余量
   \[
   M=\frac{a(|U|+1)(h+2)}{(b+1)^2(b+2)}\ge0.
   \]
   这里引用既有结果，不重新证明其 shuffle 间隙矩公式。
2. **较小 filter G 是独立块。** 写 \(U=W\sqcup V\)，取 V=G、W=U\G，S=F\G。由于 F 为上理想，S 是 W 中的上理想，F=V∪S。因此直接应用本报告定理，b=|G|，较小均值 r 是首次 F 的槽均值，余量由 (3) 给出。

两种情形都按较大 filter F 对应的首次槽作为较小均值侧，所以没有交换均值时遗漏嵌套方向的问题。当 F≠U 时余量严格为正；F=U 时首次 F 槽恒为 0，两目标取等号。F=G 的情形也已包含。

**范围停止于这个明确结构类。** 本报告不声称任意两嵌套 filters、任意两随机 caps、跨块存在可比关系的情形，或原全局猜想得到解决。
