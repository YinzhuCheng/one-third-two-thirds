# 初始 run 的全阶矩 LC、自主模块拼接与实际混合预算

日期：2026-10-19。只研究有限偏序的均匀线性扩张与其 run/首次槽；不外写，不转向原全局猜想。下述一般推论为本轮推导，不声称文献首创。

## 0. 新结果与继承输入

继承输入是 marker 插入与 Stanley 单点秩 LC，因而实际初始 ideal run 的尾 `q_k=P(R≥k)` 为 LC。此前已证明的 `q_{i+j}≤q_iq_j` 与 `E binom(R,r)≤(ER)^r` 不作为新成果。

本轮新增三个可直接复用的结论：

1. **全阶相邻矩约束：** `M_r=E binom(R,r)`、`M_0=1` 的整条有限序列为 LC，即 `M_r²≥M_{r−1}M_{r+1}`；非零有限run的正支撑内实际严格。这严格强于仅保留每一阶的几何上界。给出不依赖额外 LC 保持定理的平移 ODE 证明。
2. **自主 ideal 模块的精确尾通道：** 将内部模块嵌入任意上方/不可比外壳后，`q_global(k)=q_internal(k)t_shell(k)`。由真实 uniformLE 常纤维导出独立性，而非假设任意 cap；因此 LC 曲率、NBU、hazard-rate 比较与等尾替换精确保留。外壳允许与模块有比较关系，超出旧独立块负超几何 cap 定理。
3. **混合 LC 的精确预算：** 任意候选 profile 混合在每一阶保持 LC，当且仅当层间比值方差不超过层内曲率预算。对来自同一 uniformLE 的合法分层，其实际计数权重必满足该预算。非自主三点实际偏序明确否定上述独立尾通道，给出失败边界。

只作 **11 个固定实际偏序 controls + 1 个明确标为非实际的逻辑强度对照**，共12个，未搜索偏序族。脚本与有理数证书见 `verify_controls.py`、`controls.json`、`verification.log`。

## 1. 定义、适用范围与任意首次命中集

设 P 为有限偏序，L 为其均匀随机线性扩张。对固定集合 I⊆P，令 R 为 L 的初始连续 I 元素数；I=P 时 R=|P|。令

\[
q_k=\Pr(R\ge k),\qquad M_r=\mathbb E\binom Rr,\qquad M_0=1.
\]

所有越过最大可能 run 的 q、M 都置0。若 I 为 ideal，最大可能 run 为 h=|I|，且 q_0,…,q_h 均正，因为将整个 I 先输出是合法的。

事实上，**I 不必是 ideal**。令

\[
I^\circ=\{x\in P:\ \downarrow x\subseteq I\}
=P\setminus\uparrow(P\setminus I).
\]

这是 I 内最大的 ideal，并且逐扩张 initial-I run 等于 initial-I° run。因为任意 x∈I\I° 都有一个 P\I 中的前驱，故它不可能出现在首次离开 I 之前。于是后文一般矩定理也适用于任意固定非空命中集 A 的首次槽 `R=min rank_L(A)−1`，取 I=P\A 即可。A=P 与 I=∅ 给 R=0；空 A 用 I=P 的全长约定。

另一种直接的 marker 说明：加新极小元 t，规定 t<a 对所有 a∈A，再取传递闭包。无需假定 t 与 P\A 全部不可比。删除 t 的反向插入位置恰是首次 A 之前的全部槽，因此

\[
N_{k+1}(t)=e(P)q_k.
\]

Stanley Theorem 3.1 的 k=1 情形给 qLC。此处非ideal推广只澄清适用范围，并未把旧 marker→LC 链再次计为新成果。

## 2. 新定理 FM-LC：整个二项阶乘矩序列为 LC

**定理 FM-LC。** 对上述任意实际 run，

\[
\boxed{\quad M_r^2\ge M_{r-1}M_{r+1}\qquad(r\ge1).\quad}\tag{F1}
\]

只需其尾 qLC、q_0=1、正支撑无缺口，因而定理也适用于满足这些条件的抽象非负整数变量。本文应用始终来自实际 uniformLE。

### 2.1 自足平移引理

设

\[
A(z)=\sum_{j=0}^{d}a_jz^j,
\]

其中 a_0,…,a_d>0 且为 LC。对 t≥0 定义

\[
b_j(t)=[z^j]A(z+t),\qquad b_{d+1}(t)=b_{d+2}(t)=0.
\]

则 b_0(t),…,b_d(t) 为 LC。d=0,1 显然；一般情形中 b_j(t)>0 对 j≤d。令

\[
\Delta_j(t)=b_j(t)^2-b_{j-1}(t)b_{j+1}(t),\quad1\le j\le d,
\]

其中 Δ_d=b_d²。由 b'_j=(j+1)b_{j+1} 直接计算，1≤j≤d−1 时

\[
\begin{aligned}
\Delta'_j
&=(j+2)(b_jb_{j+1}-b_{j-1}b_{j+2})\\
&=(j+2)\left(\frac{b_{j+1}}{b_j}\Delta_j
 +\frac{b_{j-1}}{b_j}\Delta_{j+1}\right).
\end{aligned}\tag{F2}
\]

初始 Δ_j(0)≥0，顶层 Δ_d(t)=a_d²≥0。由 j=d−1 向下递推，每个方程都为

\[
\Delta'_j=c_j(t)\Delta_j+f_j(t),\quad c_j(t)\ge0,\ f_j(t)\ge0.
\]

积分因子公式保证 Δ_j(t)≥0。因此引理成立。没有除以零，也不需要援引未核验的 Pascal/ULC 卷积保持性。

### 2.2 应用于 run 矩

设最大 run 为 h。h=0 时所有正阶 M 为0，结论显然。h≥1 时 q_1,…,q_h>0，并且

\[
A(z)=\sum_{j=0}^{h-1}q_{j+1}z^j
\]

的系数 LC。离散尾和给

\[
M_r=\sum_{k\ge r}\binom{k-1}{r-1}q_k\qquad(r\ge1).
\tag{F3}
\]

因此

\[
[z^j]A(1+z)=\sum_{k\ge j+1}\binom{k-1}{j}q_k=M_{j+1}.
\tag{F4}
\]

平移引理说明 M_1,M_2,…,M_h 为 LC，即(F1)中 r≥2 的全部非平凡情形。要把 M_0=1 接上，使用已知 NBU 尾约束的一次尾和：

\[
M_2=\sum_{i,j\ge1}q_{i+j}\le\sum_{i,j\ge1}q_iq_j=M_1^2.
\tag{F5}
\]

r≥h 时右侧含 M_{h+1}=0，亦自动成立。证毕。

**有限正支撑上的严格性。** 若 h>0，则1≤r≤h时(F1)实际严格。r=1时(F5)双和至少有 i=j=h 一项产生严格差 q_h²>0；r=h时 M_h²>0 而右侧为0。中间 r 由平移ODE得到：顶层 Δ_d=a_d²>0，各层的正强迫项逐层向下传播，使t>0时所有 Δ_j(t)>0。h=1,2没有需要该递推的额外中间指标。

### 2.3 新信息与实用形式

在 M_r>0 的区间内，相邻比值递减：

\[
\frac{M_{r+1}}{M_r}\le\frac{M_r}{M_{r-1}}.
\tag{F6}
\]

特别地，对任意 0≤a<b<c≤h，

\[
M_b^{\,c-a}\ge M_a^{\,c-b}M_c^{\,b-a}.
\tag{F7}
\]

即不仅 M_r≤M_1^r，还必须满足例如 M_3≤M_2²/M_1（M_1>0）、M_4≤M_3²/M_2（M_2>0），以及全部跨阶插值约束。

严格强度对照，**仅为抽象分布，不是偏序实际 law**：

\[
\Pr(R=0,1,2,3)=(9/20,1/2,0,1/20).
\]

它给

\[
(M_0,M_1,M_2,M_3)=(1,13/20,3/20,1/20),
\]

满足全部逐项 M_r≤M_1^r，却有

\[
M_2^2=9/400<13/400=M_1M_3.
\]

所以 FM-LC 能排除旧单项上界排不掉的 profile。它不可能来自固定集合的实际 uniformLE 首次槽。

## 3. 新定理 AMG：任意上方外壳中的自主 ideal 模块

### 3.1 结构与真实乘积概率空间

设 Q⊆P 是一个非空自主模块：每个 x∈P\Q 对 Q 全体有相同关系，即全在其下、全在其上或全不可比。再假设 **无外点在 Q 下方**，故 Q 是 P 的 ideal。令 n=|Q|，J⊆Q 是 Q 内的 ideal。

把 Q 替换为 n 点链 C_n，外部点和所有块外关系保持，得到 S。把链点都视为标签 Q，S 的每条 LE 对应一个 skeleton：含 n 个 Q 标签和全部外部标签；外部顺序及外部与 Q 的先后受到原关系约束。

对任一 skeleton，按 Q 标签出现顺序填入 Q 的任意一条内部 LE，恰得到 P 的一条 LE。自主性保证所有填法合法；反向读出内部限制与 skeleton 唯一。因此有集合双射

\[
\operatorname{LE}(P)\simeq\operatorname{LE}(S)\times\operatorname{LE}(Q),
\qquad e(P)=e(S)e(Q).
\tag{G1}
\]

特别地，均匀 P-LE 对应 **两个独立的均匀 LE**。并非把内部秩或边界事件任意假定独立。

令

- K：Q 内部 LE 的 initial-J run；J=Q 时 K=n；
- T：S-LE 的首次外部点前的 Q 标签数；无外部点时 T=n；
- R：P-LE 的 initial-J run。

逐扩张有

\[
\boxed{\quad R=\min(K,T),\qquad K\perp T.\quad}\tag{G2}
\]

若首先遇到外部点则 R=T；若首先在 Q 内遇到 Q\J 则 R=K；两者相等时也是同一个值。因为 J 是总体 ideal，此 run 确实是前述实际对象。

### 3.2 精确尾传递和性质

写 a_k=P(K≥k)、t_k=P(T≥k)，则

\[
\boxed{\quad q_k=a_kt_k\qquad(k\ge0).\quad}\tag{G3}
\]

a 为 Q 内部 ideal-run 尾；t 为 S 中整个 ideal C_n 的 run 尾。二者均 LC、均从1开始且正支撑无缺口。因此：

(a) **全 LC / NBU 保持。** q 为 LC，故 NBU；FM-LC 同时适用于此拼接的全部二项阶乘矩。

(b) **局部曲率精确相乘。** 在所有分母为正的内点，

\[
\frac{q_k^2}{q_{k-1}q_{k+1}}
=\frac{a_k^2}{a_{k-1}a_{k+1}}
 \frac{t_k^2}{t_{k-1}t_{k+1}}.
\tag{G4}
\]

所以任一因子在该点严格 LC，则总体也严格 LC。零尾端点直接使用交叉相乘不等式，不定义曲率比。

(c) **同大小模块替换的完整 run law 传递。** 在相同外壳中将 Q,J 换为同大小 Q′,J′，共享 t。若 a′=a，则 q′=q，全部 run 矩保持；若 a′_k≤a_k 对所有 k 成立，则 q′_k≤q_k，即实际全局 run 保持随机序。

(d) **hazard-rate order 精确保持。** 在共同正支撑上，对0≤k<n，

\[
\frac{q'_{k+1}}{q'_k}\le\frac{q_{k+1}}{q_k}
\quad\Longleftrightarrow\quad
\frac{a'_{k+1}}{a'_k}\le\frac{a_{k+1}}{a_k},
\tag{G5}
\]

因为共同因子 t_{k+1}/t_k 为正。不同支撑按尾已归零处理，不在零处相除。

(e) **固定外壳的逆向识别。** t_0,…,t_n 均正，因为 Q 整块先输出合法。因此 q_k/t_k 精确恢复 a_k，0≤k≤n。这里无需遍历所有环境；这个单一自主-ideal外壳已不会丢失内部整个 run law。

### 3.3 它超出旧独立 cap，但不声称协方差界自动推广

旧 `/workspace/shared/actual-random-cap-slot-bound-20261018/RESULT.md` 中 U=W⊔V 是两块完全独立，cap 的另一因子是特定负超几何尾，并用其仿射剩余均值推出协方差公式。AMG 允许外部点在 Q 上方，T 不必是该负超几何变量。本文只推广尾/矩/序的传递，**没有把旧协方差恒等式或 T/C 余量公式移植到任意外壳**。

明确非独立外壳：Q 是任意 n 点偏序；加入 z 在所有 Q 上方，再加入与 Q,z 都不可比的 w。S 由链 C_n<z 与 w 的均匀交织组成，故

\[
t_k=\frac{n+2-k}{n+2}\qquad(0\le k\le n).
\tag{G6}
\]

这是 n+2 个插入槽中要求 w 不在前 k 个 Q 之前的直接计数。它不同于把两个外部点都作为独立失败点的负超几何尾。

取 Q=C_2⊔C_2，J 为两个链底点：a=(1,1,2/3,0,0)。总体 e(P)=36，

\[
q=(1,5/6,4/9,0,0,0,0),\qquad
M_1=23/18,\quad M_2=4/9.
\]

## 4. 真实失败边界：失去自主性，独立尾通道立刻失败

取 P={a,b,z}，唯一非平凡关系 a<z。让 Q={a,b}，J={a}。Q 的诱导偏序是二点反链，J 是 ideal；总体中 Q 也是 ideal，但 **不是自主模块**，因为 z 只在 a 上方。

Q 内部均匀 LE 为 ab、ba，所以

\[
\Pr(K\ge1)=1/2.
\]

P 的三条等概率 LE 是 abz、azb、baz，所以

\[
\Pr(R\ge1)=2/3>1/2.
\tag{B1}
\]

因此不可能存在任何随机变量 T 使该总体 run 具有独立 min(K,T) 表示；事实上任何耦合的 min(K,T) 都必≤K，不可能使该尾从1/2增为2/3。这里 K 特指内部 **均匀** LE law。

失败原因可直接看见：总体限制到 Q 的内部词 ab、ba 的实际权重为2:1，不再均匀。AMG 的常纤维双射正是在此断裂。这个反例是真实 uniformLE，不是任意正混合。

注意总体尾 (1,2/3,0,0) 仍为 LC，FM-LC 仍成立。反例否定的是自主模块乘积通道，而不是 universal run LC；无论如何拼接，最终若仍是固定偏序的均匀 LE 与固定命中集，普适约束都不可能被破坏。

## 5. 混合何时破坏 LC：精确方差—曲率预算

这个代数恒等式同时适用于 run tails 与全阶 M profiles。它给的是可检验充要条件，不声称任意权重可由偏序实现。

设 x^θ=(x^θ_j) 为有限个非负 LC 序列，且每个序列的正支撑都为从0开始的初始区间（允许只有x^θ_0>0），给定权重 p_θ≥0、Σp_θ=1，令

\[
X_j=\sum_\theta p_\theta x^\theta_j.
\]

固定 j，假设 X_{j−1}>0，且各序列的正支撑无内零。对 x^θ_{j−1}>0 的层定义倾斜权重及局部比值

\[
\nu_\theta=\frac{p_\theta x^\theta_{j-1}}{X_{j-1}},\qquad
u_\theta^{\rm loc}=\frac{x^\theta_j}{x^\theta_{j-1}}=:u_\theta,
\qquad
v_\theta=\frac{x^\theta_{j+1}}{x^\theta_j}.
\]

当 x^θ_j=0 时置 u_θ=v_θ=0；由无内零且 x^θ_{j−1}>0 可知 x^θ_{j+1}=0。令 E_ν、Var_ν 表示按倾斜权重 ν 计算。于是

\[
\frac{X_j}{X_{j-1}}=E_\nu u,\qquad
\frac{X_{j+1}}{X_{j-1}}=E_\nu(uv),
\]

从而精确有

\[
\boxed{\quad
\frac{X_j^2-X_{j-1}X_{j+1}}{X_{j-1}^2}
=E_\nu[u(u-v)]-\operatorname{Var}_\nu(u).
\quad}\tag{M1}
\]

每层 LC 给 u≥v，故第一项是非负层内曲率预算；第二项是非负层间比值波动。因此

\[
\boxed{\quad
X_j^2\ge X_{j-1}X_{j+1}
\iff \operatorname{Var}_\nu(u)\le E_\nu[u(u-v)].
\quad}\tag{M2}
\]

方差超过预算时，该点混合 LC **恰好**失败；等于时恰好取等号。不需要猜混合项的符号。

### 实际 uniformLE 分层的含义

若一个真实 P-LE 空间被不交事件 E_θ 分割，而且每层排列集合恰为某个添加关系的偏序 P_θ 的全部 LE，则

\[
p_\theta=\frac{e(P_\theta)}{e(P)}
\]

是强制的实际权重。对同一个固定命中集，每层与总体都是实际首次槽，因此它们的 q profiles 与 M profiles 都 LC。实际权重必在每一个 j 满足(M2)。任意重配这些权重时，即便每层模板单独合法，也可能超过预算；那只是候选 profile 的不可实现性诊断，不能声称构成 P 的反例。

一个非零层间方差的实际分层控制：取P为a<b<c与d<e<f的不交并，I=P\{f}。按首元素为a还是d分层，恰等于加入a<d或d<a的两个refinement，各有10条LE，因此实际权重各1/2。第j=3个尾LC预算精确为

\[
\operatorname{Var}_\nu(u)=1/400,\qquad E_\nu[u(u-v)]=21/200,\qquad q_3^2-q_2q_4=41/400.
\]

此时q_2=1，无额外归一化因子。脚本同时核验这两个refinement在全部合法阶的q与M预算身份，使用强制计数权重；不是任意正混合。

AMG 给出的是更强的正面机制：在其自主边界，实际均匀权重不是任意 profile 混合，而是独立常纤维，化为(G3)的逐点乘积，层间损失可完全避免。

## 6. 核验、审查状态与边界

`verify_controls.py` 使用理想前缀/后缀 DP 和 Fraction，逐个检查11个预先固定偏序：

1. 内部二点反链；
2. n=2 的非独立 successor 外壳；
3. 该二点模块拼接，总e=8、q_1=3/8；
4. 内部 C_2⊔C_2，J 为两底；
5. n=4 的 successor 外壳；
6. 该四点模块拼接，总e=36；
7. 三点非自主失败边界；
8. C_3⊔C_3、去掉一条链顶点的五点ideal，用于多阶非零矩；
9. 非ideal允许集：a<b、c孤立，I={b,c}，其实际run等于I°={c}的run；
10. 第8例加入a<d的refinement；
11. 第8例加入d<a的refinement。

每个实际 control 均检查全部尾 LC 与全部 M-LC；两个模块拼接逐项检查(G3)。第8例

\[
(M_0,\ldots,M_5)=(1,17/4,73/10,127/20,14/5,1/2).
\]

另一个固定抽象分布仅证明新旧约束的逻辑强度差异，明确不作为实际偏序 control。总计12个controls，不超过12。

独立解析审查已通过第0–5节全部新承重论证：平移引理、M全序列及严格LC、任意集合ideal核、模块常纤维/尾通道、三点失败边界和修正后的初始正支撑混合预算。审查者已终核全部11项实际control与1项形式control的代码及保存证书，未独立重跑；其中两个refinement只用于同一预算恒等式的定点回归，不承担新证明。未建立任意非自主边界的乘积通道，也未把任意正profile混合视为 uniformLE 实现。未给出原平衡对猜想的新全局结论。

## 7. 原始来源

- R. P. Stanley, *Two Combinatorial Applications of the Aleksandrov–Fenchel Inequalities*, JCTA 31 (1981), 56–65，Theorem 3.1，pp.62–63（本文只用单点秩LC输入）：https://math.mit.edu/~rstan/pubs/pubfiles/48.pdf 。本轮已重开原PDF核对准确量词。
- 新 rooted-five 原稿，固定commit b4b4ccbc0ff5da92ec1156b9eff821d85960a697，Section2与Section7给继承marker-tail机制及正混合失真背景：https://github.com/eliottcassidy2000/math/blob/b4b4ccbc0ff5da92ec1156b9eff821d85960a697/05-knowledge/results/rooted_five_logconcave_balance_20261019.md 。本轮通过GitHub只读工具读取全文。
- 本地旧cap结果：`/workspace/shared/actual-random-cap-slot-bound-20261018/RESULT.md`。本文明确未重复其协方差结论。
