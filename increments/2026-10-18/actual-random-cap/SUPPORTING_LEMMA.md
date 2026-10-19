本文件仅为合并推论较大 filter 独立块分支所需的旧已审定理 §§1–3 摘录，保留其自含证明。未重复旧实验或其余历史材料。

# 独立补块与嵌套 filter 的精确辅助槽公式

日期：2026-10-18。范围仅为本轮辅助槽矩目标 T，以及嵌套时与之等价的协方差目标 C。本文没有转向原全局猜想，没有扩大反例搜索，也没有运行新的偏序 DP。

## 1. 主结果：任意独立补块，而不要求链

设 \(U=W\sqcup V\) 为两个有限偏序的不交并：两块之间完全没有可比关系，但各块内部偏序任意。记

\[
a=|W|\ge0,\qquad b=|V|\ge1,\qquad n=a+b,\qquad d=b+1.
\]

取

\[
S_y=V,\qquad \varnothing\ne S_z\subseteq V,
\]

其中在原问题里要求 \(S_z\) 是 \(V\) 的上理想，故也是 \(U\) 的上理想。令 \(f_U\) 为均匀随机线性扩张的秩函数，定义首次出现槽

\[
R_y=\min_{v\in V}f_U(v)-1,\qquad
R_z=\min_{v\in S_z}f_U(v)-1.
\]

另在 \(V\) 的均匀随机线性扩张 \(f_V\) 中定义

\[
L=\min_{v\in S_z}f_V(v)-1,\qquad h=\mathbb EL,
\]

所以 \(0\le h\le b-1\)。则下面全部为精确等式：

\[
\boxed{
r=\mathbb ER_y=\frac{a}{b+1},\qquad
s=\mathbb ER_z=\frac{(n+1)h+a}{b+1},\qquad
\mathbb E\min(R_y,R_z)=r.
}\tag{G1}
\]

\[
\boxed{
\operatorname{Cov}(R_y,R_z)
=\frac{a(n+1)(b-h)}{(b+1)^2(b+2)},\qquad
N:=\mathbb E[R_yR_z+\min(R_y,R_z)]
=\frac{a(n+1)(h+2)}{(b+1)(b+2)}.
}\tag{G2}
\]

两均值满足 \(r\le s\)。目标

\[
\mathrm{T}:\quad N\le rs+\min\{r^2+2r,s^2+2s\}=rs+r^2+2r
\]

以及协方差目标

\[
\mathrm{C}:\quad \operatorname{Cov}(R_y,R_z)\le
\min\{r^2+r,s^2+s\}=r^2+r
\]

在这一整个结构族都成立，而且有完全相同的精确余量：

\[
\boxed{
rs+r^2+2r-N
=r^2+r-\operatorname{Cov}(R_y,R_z)
=\frac{a(n+1)(h+2)}{(b+1)^2(b+2)}.
}\tag{G3}
\]

当 \(a>0\) 时余量严格为正；\(a=0\) 时 \(R_y=0\)，两个目标都是等号。证明事实上只用 \(S_z\) 是 \(V\) 中的非空集合；上理想条件保证它属于原 filter 模型，却不是本 shuffle 机制所需的额外条件。

此结论不要求 \(W\) 或 \(V\) 是链，也不要求两个 filters 都 principal。它仍然要求 \(W,V\) 之间完全不交，且 \(S_y=V\)，没有推广成任意两个 filters 的结论。

## 2. 机制：均匀 shuffle 等价于均匀弱分拆

每条 \(U\) 扩张唯一分解成：一条 \(W\) 的扩张、一条 \(V\) 的扩张，以及一个由 \(a\) 个 W、\(b\) 个 V 组成的 shuffle 字。反之每个这样的三元组都给出合法 \(U\) 扩张。

每对内部扩张都对应完全相同的 \(\binom{a+b}{a}\) 个 shuffle。因此均匀 \(U\) 扩张可由独立均匀的内部扩张与 shuffle 生成。特别是下面的间隙向量与 \(f_V\)、\(L\) 独立。

令 \(G_0\) 是首个 V 前的 W 数，\(G_i\) 是第 \(i\) 个与第 \(i+1\) 个 V 之间的 W 数，\(G_b\) 是最后一个 V 后的 W 数。shuffle 字与

\[
(G_0,\ldots,G_b)\in\mathbb Z_{\ge0}^{b+1},\qquad
\sum_{i=0}^{b}G_i=a
\]

一一对应，故间隙向量是在总和为 \(a\) 的弱分拆上均匀分布，**不是**把每个 W 独立投入槽的 multinomial 分布。

以下矩可由星条计数或生成函数直接得到。对不同的 \(i,j\)，

\[
\mathbb EG_i=\frac ad,\qquad
\mathbb E[G_i(G_i-1)]=\frac{2a(a-1)}{d(d+1)},\qquad
\mathbb E(G_iG_j)=\frac{a(a-1)}{d(d+1)}.
\]

例如总弱分拆数为 \(\binom{a+d-1}{d-1}\)，而上述三个加权总数依次为

\[
\binom{a+d-1}{d},\qquad
2\binom{a+d-1}{d+1},\qquad
\binom{a+d-1}{d+1};
\]

二项系数超出范围时取 0。于是

\[
\boxed{
\operatorname{Var}G_i=\frac{ab(n+1)}{d^2(d+1)},\qquad
\operatorname{Cov}(G_i,G_j)=-\frac{a(n+1)}{d^2(d+1)}\quad(i\ne j).
}\tag{G4}
\]

## 3. 条件协方差与完成 T、C

逐扩张有

\[
R_y=G_0,\qquad
R_z=L+\sum_{j=0}^{L}G_j,\qquad R_y\le R_z.
\]

条件于 \(L=\ell\)，独立性给出

\[
\mathbb E[R_y\mid L=\ell]=r=\frac ad,\qquad
\mathbb E[R_z\mid L=\ell]=\ell+(\ell+1)r,
\]

\[
\operatorname{Cov}(R_y,R_z\mid L=\ell)
=\operatorname{Var}G_0+\ell\operatorname{Cov}(G_0,G_1)
=\frac{a(n+1)(b-\ell)}{d^2(d+1)}.
\]

第一侧条件均值不依赖 \(\ell\)，故全协方差公式中的“条件均值之间的协方差”为 0。对最后一式取期望，得到 (G2) 的协方差式；对条件均值取期望得到 (G1)。

又因 \(\min(R_y,R_z)=R_y\)，

\[
N=rs+r+\operatorname{Cov}(R_y,R_z)
=\frac{a(n+1)(h+2)}{d(d+1)}.
\]

最后

\[
r(r+1)=\frac{a(n+1)}{d^2},
\]

故将协方差从中减去恰给 (G3)。T 与 C 的等价不是额外假设：嵌套已经使两目标的左右两边分别只相差同一个 \(r\)。

若 \(a>0\)，沿用原报告的相对压力口径还可写成

\[
\delta_C=\frac{h+2}{b+2},\qquad
\delta_T=\frac{(n+1)(h+2)}{(b+2)(a+2b+2)}.
\]

