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

## 4. 孤立单点推论：原近紧族的极简形式

取 \(W=\{a_0\}\)，其中 \(a_0\) 与 \(V\) 全部互不可比，令 \(n=1+|V|\ge2\)。此时 (G1)–(G3) 简化为

\[
\boxed{
r=\frac1n,\qquad
s=\frac{(n+1)h+1}{n},\qquad
\mathbb E(R_yR_z)=\frac{h+1}{n},\qquad
N=\frac{h+2}{n}.
}\tag{1}
\]

\[
\boxed{
\operatorname{Cov}(R_y,R_z)=\frac{n-1-h}{n^2},\qquad
N-rs=\frac{2n-1-h}{n^2},\qquad
\mathrm{Tgap}=\mathrm{Cgap}=\frac{h+2}{n^2}>0.
}\tag{2}
\]

也可以直接用单点的均匀插入看见全部结构。给定 \(L=j\)，\(n\) 个插入槽中，首槽 1 个，其余首次 \(S_z\) 前槽 \(j\) 个，之后槽 \(n-1-j\) 个。因此完整联合分布为

\[
(R_y,R_z)=
\begin{cases}
(1,j+1),&\text{概率 }1/n,\\
(0,j+1),&\text{概率 }j/n,\\
(0,j),&\text{概率 }(n-1-j)/n.
\end{cases}\tag{3}
\]

原压力形式为

\[
\boxed{\delta_T=\frac{h+2}{2n+1},\qquad
\delta_C=\frac{h+2}{n+1}.}\tag{4}
\]

本族近紧的机制由此清楚：孤立单点首位事件概率为 \(1/n\)，绝对余量可以降到 \(O(n^{-2})\)。若 \(h\) 保持有界而 \(n\to\infty\)，两种相对压力都趋近 1；对固定 \(n\)，\(h\) 越小压力越大。以下三链公式正是这个推论的显式子族。

## 5. 原三链族：阈值含义已经核对

原始脚本 `large-slot-moment-stress-20261018/run_stress.py` 的 `filter_mask` 使用

`mask |= ((1<<length)-(1<<threshold)) << offset`。

因此链坐标从 0 开始；阈值 0 表示整条链纳入，阈值等于链长表示整条链排除。该含义也与原验证程序按扩张中首次命中 filter 的零基下标计算槽数一致。

现在令

\[
U=\{a\}\sqcup B\sqcup C,
\quad B=(b_0<\cdots<b_{b-1}),
\quad C=(c_0<\cdots<c_{c-1}),
\]

三条链之间没有跨链关系。三条非空链的合法参数为

\[
b,c\ge1,\qquad 0\le k\le b,\qquad n=1+b+c.
\]

阈值对子 \([1,0,0]/[1,k,0]\) 精确表示

\[
S_y=B\cup C,\qquad
S_z=\{b_k,\ldots,b_{b-1}\}\cup C.
\]

- \(k=0\)：两个 filters 相同，均为 nonprincipal。
- \(1\le k<b\)：相异、嵌套、两个均 nonprincipal；这个范围要求 \(b\ge2\)。
- \(k=b\)：\(S_z=C\) 为 principal，较小均值侧 \(S_y\) 仍是 nonprincipal。

所以主定理同时覆盖已测的相异 both-nonprincipal 近紧族和 \((1,1,c)\) 的相异近紧族，而不是只覆盖某个 principal 假设。

## 6. 三链族的 \(h\) 闭式：截断负超几何等待量

均匀 \(V=B\sqcup C\) 扩张就是均匀的 \(b\) 个 B 与 \(c\) 个 C 的 shuffle。令 \(J\) 为首次 C 之前的 B 个数。那么

\[
L=\min(J,k),\qquad
p_i:=\Pr(J\ge i)=\frac{(b)_{\underline i}}{(b+c)_{\underline i}}
=\frac{\binom{b+c-i}{b-i}}{\binom{b+c}{b}},\quad 0\le i\le k,
\]

其中 \(p_0=1\)。于是

\[
\boxed{
h=\sum_{i=1}^{k}\frac{(b)_{\underline i}}{(b+c)_{\underline i}}
=\frac{b-(b-k)p_k}{c+1}.
}\tag{6}
\]

第一式为非负整数随机变量的尾和公式。第二式可不用任何近似直接望远镜求和：

\[
(c+1)p_i=(b-i+1)p_{i-1}-(b-i)p_i,
\]

对 \(i=1,\ldots,k\) 相加即可。端点 \(k=0\) 给 \(h=0\)，\(k=b\) 给 \(h=b/(c+1)\)，均无偏移问题。

因此任意合法 \(b,c,k\) 的最终精确答案就是：令

\[
H=\frac{b-(b-k)\,(b)_{\underline k}/(b+c)_{\underline k}}{c+1},
\]

则

\[
\boxed{
r=\frac1{1+b+c},\quad
s=\frac{(b+c+2)H+1}{1+b+c},\quad
N=\frac{H+2}{1+b+c},\quad
\mathrm{Tgap}=\mathrm{Cgap}=\frac{H+2}{(1+b+c)^2}.
}\tag{7}
\]

这里 \(H=h\)。若需要完整分布，则 \(\Pr(L=j)=p_j-p_{j+1}\) 对 \(0\le j<k\)，且 \(\Pr(L=k)=p_k\)，再代入 (3) 即得。

若记号上允许长度为 0 的退化链，(6) 与 (7) 仍可沿用到 \(b,c\ge0\)、\(0\le k\le b\)，空尾和取 0、\(p_0=1\)，空 filter 的首次槽按原脚本约定取 \(n\)。但本报告的主定理及原三链范围不需要这些退化延拓。

## 7. 简化相异族 \((1,1,c)\)：覆盖整个 \(c\) 范围

取 \(b=k=1\)、\(c\ge1\)，即阈值 \([1,0,0]/[1,1,0]\)。此时

\[
h=\frac1{c+1},\qquad n=c+2,
\]

\[
\boxed{
r=\frac1{c+2},\qquad
s=\frac2{c+1},\qquad
N=\frac{2c+3}{(c+1)(c+2)}.
}
\]

还有

\[
\mathbb E(R_yR_z)=\frac1{c+1},\quad
\operatorname{Cov}(R_y,R_z)=\frac{c}{(c+1)(c+2)},\quad
\mathrm{Tgap}=\mathrm{Cgap}
=\frac{2c+3}{(c+1)(c+2)^2}>0.
\]

这是一整族的公式与证明，不是对 \(c=198\) 单点枚举的替代结论。

## 8. 与既有 exact 记录回核

以下只将一般公式代入旧记录的两个既有对象；没有生成新偏序、filter 对子或线性扩张。

### 8.1 相异 both-nonprincipal 近紧例

\((b,c,k)=(9,190,4)\)、\(n=200\)：

\[
p_4=\frac6{3018631},\qquad
h=\frac{142239}{3018631},
\]

\[
r=\frac1{200},\qquad
s=\frac{3160867}{60372620},\qquad
\mathbb E(R_yR_z)=\frac{316087}{60372620},\qquad
N=\frac{6179501}{603726200},
\]

\[
\mathrm{Tgap}=\mathrm{Cgap}=\frac{6179501}{120745240000},
\quad
\delta_T=\frac{6179501}{1210471031},\quad
\delta_C=\frac{6179501}{606744831}.
\]

扩张总数

\[
K=n\binom{b+c}{b}=224510043090132800.
\]

由 (1) 乘以 \(K\) 得到

\[
(A,B,C,D)=
(1122550215450664,11754440777494480,
1175445193371280,1122550215450664),
\]

与 `slot-filter-scope-20261018/RESULT.md` §5.2 保存的四个 exact 整数逐项相同。

### 8.2 相异 \((1,1,198)\) 近紧例

\(b=k=1,c=198,n=200\) 时 \(h=1/199\)，所以

\[
r=1/200,\qquad s=2/199,\qquad
\mathbb E(R_yR_z)=1/199,\qquad N=399/39800,
\]

\[
\mathrm{Tgap}=\mathrm{Cgap}=399/7960000,
\quad p_T=79400/79799,\quad p_C=13200/13333.
\]

与同一旧报告 §5.1 的记录一致。

## 9. 结论与停止边界

本报告已证明整个独立补块结构族 \(U=W\sqcup V\)、\(S_y=V\)、\(\varnothing\ne S_z\subseteq V\) 的 T 与 C，并给出同一个精确余量 (G3)。两块内部偏序任意，无需链假设；\(|W|>0\) 时余量严格为正。

三条不交链 \((1,b,c)\)、阈值 \([1,0,0]/[1,k,0]\) 是其显式可积的子族，全部合法参数均由 (6)–(7) 解决。两个既有近紧例与保存的 exact 整数完全一致；没有 actual 反例，也没有未决代数卡点。

这既不证明任意两个上理想的 T，也不把原 principal-filter 证明当成适用于本族的理由。本证明的承重点是独立补块的均匀 shuffle 与间隙矩，属于完全明确的结构覆盖范围。
