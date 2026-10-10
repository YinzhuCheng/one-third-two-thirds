# 共同严格下集的交换平方不等式

2026 年 10 月 10 日

本文给出如下结论的完整推导：有限偏序中，两个不可比元素只要具有相同的严格下集，其合法交换数与两方向不可交换数就满足平方不等式。共同不可比元素不必成链，偏序宽度也不受限制。进一步，对任意不可比元素对，两次分别进行的精确条件化给出原均匀完整线性扩张律下的两条乘积约束。

证明的外部输入是经典的边缘对数凹性与 Busemann–Ball 定理；其余计数、几何和条件化步骤在下文展开。第八节进一步证明有限偏序的定性严格性。本文不认领文献新颖性，也不据此声称解决一般或宽度三的 1/3–2/3 猜想。

## 一 结论与计数口径

设有限偏序为 $P$，$n=|P|$，完整线性扩张集合为 $\mathrm{LE}(P)$，总数为 $E=e(P)$。以下“先于”均指在线性扩张中的先后顺序；所有概率均来自 **原偏序完整线性扩张上的均匀分布**。

取实际元素标签 $u\parallel y$，并假设其严格下集相同：

$$
D_P(u)=D_P(y)=D.
$$

将一个扩张中的实际标签 $u,y$ 互换，其他位置不动。定义：

- $H$：满足 $u$ 先于 $y$，且互换后仍为 $P$ 的线性扩张的扩张数；
- $R_u$：满足 $u$ 先于 $y$，但互换不合法的扩张数；
- $R_y$：满足 $y$ 先于 $u$，但互换不合法的扩张数。

合法交换是对合，因此反方向的合法交换数也等于 $H$，且

$$
E=2H+R_u+R_y.
$$

**定理。** 对上述任意有限偏序及元素对，

$$
\boxed{H^2\ge R_uR_y.}\tag{1}
$$

令 $p=\Pr(u\text{ 先于 }y)=(H+R_u)/E$。直接展开可得

$$
H^2-R_uR_y
=EH-(H+R_u)(H+R_y)
=(H+R_u)^2-ER_u.
$$

因此 (1) 等价于

$$
\boxed{\frac HE\ge p(1-p)},\qquad
\boxed{\frac{R_u}E\le p^2.}\tag{2}
$$

这里 $H$ 只计一个方向的合法交换扩张；将它误当作双向总数会改变常数。

## 二 四步证明

### 第一步 用真实次序多胞形纤维表示三个计数

当 $n=2$ 时，$H=1$、$R_u=R_y=0$。以下设 $n>2$，令

$$
\Omega=\mathcal O(P\setminus\{u,y\})\subset[0,1]^{n-2},
$$

其中次序多胞形采用 $v<_Pw\Rightarrow z_v\le z_w$ 的约定。对 $z\in\Omega$，定义

$$
L(z)=\max_{d\in D}z_d,\quad
T_u(z)=\min_{v>_Pu}z_v,\quad
T_y(z)=\min_{v>_Py}z_v,
$$

并约定空最大值为 $0$、空最小值为 $1$。再令

$$
A(z)=T_u(z)-L(z),\qquad B(z)=T_y(z)-L(z).
$$

由传递性，$d\in D,v>_Pu\Rightarrow d<_Pv$，故 $L\le T_u,T_y$。最小仿射函数为凹函数，最大仿射函数为凸函数，所以 $A,B$ 都非负、连续、凹，并在 $\Omega$ 的内部同时为正。

固定其余坐标 $z$ 后，$\mathcal O(P)$ 的精确二维纤维为

$$
[L,T_u]\times[L,T_y].
$$

共同下集假设恰好保证两个区间具有同一下端点。将两坐标同时减去 $L$，得到 $[0,A]\times[0,B]$，面积和两坐标的先后关系均不变。

合法交换要求两坐标都落在 $[0,\min(A,B)]$ 内，正方向区域面积为 $\min(A,B)^2/2$。若 $A<B$，正方向不可交换区域面积为 $A(B-A)$，反方向为零；$B<A$ 时对称。因此

$$
\begin{aligned}
h_0:=H/n!&=\int_\Omega\frac{\min(A,B)^2}{2}\,dz,\\
x_0:=R_u/n!&=\int_\Omega A(B-A)_+\,dz,\\
y_0:=R_y/n!&=\int_\Omega B(A-B)_+\,dz.
\end{aligned}\tag{3}
$$

归一化因子确为 $n!$：除去零测度的坐标相等处，$\mathcal O(P)$ 按每个完整线性扩张分为体积 $1/n!$ 的标准单纯形；先后关系及交换合法性在各单纯形内部恒定。这里对 $\Omega$ 使用普通 Lebesgue 积分，保留了所有插回完成权重，**没有把删除后的扩张重新均匀抽样**。

### 第二步 将凹矩形纤维变成二维递减对数凹函数

定义

$$
f(s,t)=\operatorname{vol}_{n-2}
\{z\in\Omega:A(z)\ge s,\ B(z)\ge t\},\qquad s,t\ge0.
$$

集合

$$
\{(z,s,t):z\in\Omega,\ 0\le s\le A(z),\ 0\le t\le B(z)\}
$$

是凸集，故其截面体积 $f$ 对数凹；这是边缘对数凹性，也可由截面之间的 Minkowski 包含关系及 Brunn–Minkowski 不等式直接推出。$f$ 还逐坐标非增、有界、紧支撑，并在原点附近为正。所用经典结论见 Ball 综述的 Theorem 2 及随后关于边缘的说明。[1]

令

$$
F(x_1,x_2)=f(|x_1|,|x_2|).
$$

由逐坐标三角不等式

$$
|(1-\lambda)x+\lambda y|
\le(1-\lambda)|x|+\lambda|y|
$$

及 $f$ 的单调性、对数凹性，$F$ 在整个平面上对数凹。它对两个坐标的独立变号均不变，特别是偶函数。

Tonelli 定理和矩形面积计算给出

$$
\begin{aligned}
\int_0^\infty t f(t,t)\,dt&=h_0,\\
\int_{0\le s<t}f(s,t)\,ds\,dt&=h_0+x_0,\\
\int_{0\le t<s}f(s,t)\,ds\,dt&=h_0+y_0.
\end{aligned}\tag{4}
$$

### 第三步 用 Ball 凸体精确保留两个扇区质量

Busemann–Ball 定理在 $p=2$ 时表明，对偶的、可积且积分为正的对数凹函数 $F$，

$$
x\longmapsto\left(\int_0^\infty rF(rx)\,dr\right)^{-1/2}
$$

是范数。[1, Theorem 3] 因此

$$
q(x)=\left(2\int_0^\infty rF(rx)\,dr\right)^{-1/2},\qquad
K=\{x:q(x)\le1\}
$$

定义了紧的、具有内部的凸体，且 $K$ 对各坐标变号不变。对单位方向 $v$，其径向函数满足

$$
\rho_K(v)^2=2\int_0^\infty rF(rv)\,dr.
$$

极坐标积分于是给出对任意以原点为顶点的扇区 $C$ 的精确恒等式

$$
\operatorname{area}(K\cap C)=\int_C F.\tag{5}
$$

若 $(a,a)$ 是 $K$ 的正对角线边界点，则

$$
2a^2=\rho_K((1,1)/\sqrt2)^2
=4\int_0^\infty t f(t,t)\,dt=4h_0,
$$

即 $a^2/2=h_0$。由 (4)–(5)，$K$ 在第一象限的两个对角扇区面积分别为 $h_0+x_0$ 与 $h_0+y_0$。

### 第四步 支撑直线给出两侧剩余面积的乘积界

对称性与凸性给出 $[-a,a]^2\subset K$。取 $(a,a)$ 处的一条支撑直线，写成

$$
\alpha s+\beta t=(\alpha+\beta)a,
\qquad K\subset\{\alpha s+\beta t\le(\alpha+\beta)a\}.
$$

由 $(a-\varepsilon,a),(a,a-\varepsilon)\in K$，可知 $\alpha,\beta\ge0$，且二者不同时为零。

若 $\alpha,\beta>0$，第一象限的 $K$ 包含在该直线与两坐标轴围成的三角形中。三角形在 $s\le t$ 和 $t\le s$ 中的面积分别为

$$
\frac{(\alpha+\beta)a^2}{2\beta},\qquad
\frac{(\alpha+\beta)a^2}{2\alpha}.
$$

分别减去半个正方形的面积 $a^2/2=h_0$，得到

$$
0\le x_0\le\frac{\alpha a^2}{2\beta},\qquad
0\le y_0\le\frac{\beta a^2}{2\alpha}.
$$

相乘即 $x_0y_0\le a^4/4=h_0^2$。若 $\alpha=0$，则 $K$ 在第一象限中满足 $t\le a$，其 $s\le t$ 扇区恰为半个正方形，故 $x_0=0$；$\beta=0$ 时同理有 $y_0=0$。所以退化情形也成立。最后将 (3) 代入并乘以 $(n!)^2$，即得 (1)。证毕。

## 三 适用范围与单次条件化

令

$$
N=\{v\in P\setminus\{u,y\}:v\parallel u,\ v\parallel y\}.
$$

此前以共同不可比集 $N$ 为链的版本（S103）依赖该链结构；上述证明只使用完整删除次序多胞形的凸性，没有要求 $N$ 成链，也没有限制共同下集 $D$ 的大小、结构或偏序宽度。因此它覆盖旧条件范围之外的偏序。

这不是将不同 $N$ 排序下的不等式逐个证明后任意混合。这样的捷径一般不成立：两个等权矩形 $(A,B)=(1,4),(4,1)$ 的混合给出 $h_0=1/2$、$x_0=y_0=3/2$，直接违反平方界。证明所用的关键额外结构是 **同一凸底空间上的两个凹函数**。

一个直接的原律回传形式如下。设 $P_0$ 中 $y$ 极小、$u\parallel y$，令 $D=D_{P_0}(u)$，并记

$$
\begin{aligned}
d&=\Pr_{P_0}(D\text{ 全部先于 }y),\\
p_0&=\Pr_{P_0}(u\text{ 先于 }y),\\
U_0&=\Pr_{P_0}(\exists v>_{P_0}u:\ v\text{ 先于 }y).
\end{aligned}
$$

添加关系 $D<y$ 并取传递闭包得到 $Q$。它的完整扩张恰好是上述概率为 $d>0$ 的事件；$Q$ 中 $u,y$ 具有共同下集 $D$，且 $u$ 的严格上集不变。后两个事件均包含于该条件事件，因此

$$
p_Q=p_0/d,\qquad (R_u/e(Q))=U_0/d.
$$

由 (2) 得到不要求宽度条件的归一化平方界

$$
\boxed{dU_0\le p_0^2.}\tag{6}
$$

## 四 任意不可比对的双条件化约束

现在仅设 $a\parallel b$，不要求原偏序具有共同下集或共同上集。令 $\mathcal A=\{a\text{ 先于 }b\}$，并定义

$$
\begin{aligned}
S&=\{\exists v>_Pa:\ v\text{ 先于 }b\},&
T&=\{\exists d<_Pb:\ a\text{ 先于 }d\},\\
S'&=\{\exists v>_Pb:\ v\text{ 先于 }a\},&
T'&=\{\exists d<_Pa:\ b\text{ 先于 }d\}.
\end{aligned}
$$

其中 $S,T\subset\mathcal A$，$S',T'\subset\mathcal A^c$。在原均匀完整扩张律下记

$$
\begin{aligned}
h&=\Pr(\mathcal A\setminus(S\cup T)),&
r&=\Pr(S\setminus T),&
\ell&=\Pr(T\setminus S),&
k&=\Pr(S\cap T),\\
h'&=\Pr(\mathcal A^c\setminus(S'\cup T')),&
r'&=\Pr(S'\setminus T'),&
\ell'&=\Pr(T'\setminus S'),&
k'&=\Pr(S'\cap T').
\end{aligned}
$$

实际标签交换在正方向合法，当且仅当 $S,T$ 均不发生；反方向同理。交换对合给出 $h'=h$。先列出下理想 $D_P(a)\cup D_P(b)$，再连续列出 $a,b$，最后列出其余元素，可见 $h>0$。若 $p=\Pr(\mathcal A)$，则

$$
p=h+r+\ell+k,\qquad 1-p=h+r'+\ell'+k'.\tag{7}
$$

**推论。** 对任意有限偏序的任意不可比对，

$$
\boxed{rr'\le h^2,\qquad \ell\ell'\le h^2.}\tag{8}
$$

**下集条件化。** 令 $D_*=D_P(a)\cup D_P(b)$，将 $D_*$ 中各元素置于 $a,b$ 之下，取传递闭包得到 $Q_\downarrow$。上述连续排列保证无环且 $a,b$ 仍不可比。$D_*$ 是下理想，没有新边进入其中；从 $a$ 或 $b$ 出发也不能到达 $D_*$，所以新严格下集都恰为 $D_*$，而原严格上集不变。

其完整扩张恰好是事件

$$
\mathcal E_\downarrow=\{D_*\text{ 全部先于 }a,b\}
=(T\cup T')^c,
\qquad d_\downarrow=2h+r+r'>0.
$$

保留下来的四格为正方向 $h,r$ 与反方向 $h,r'$。因此 $Q_\downarrow$ 的整数计数恰为

$$
H_\downarrow=e(P)h,\quad
R_{a,\downarrow}=e(P)r,\quad
R_{b,\downarrow}=e(P)r'.
$$

应用 (1) 后约去 $e(P)^2$，得到第一条 (8)。这些是未归一化的整数计数，不应再除以条件概率。

**上集条件化。** 对偶地令 $U_*=U_P(a)\cup U_P(b)$，将 $a,b$ 置于全部 $U_*$ 之下，得到 $Q_\uparrow$。这次严格下集不变，严格上集都成为 $U_*$。其扩张恰好对应

$$
\mathcal E_\uparrow=\{U_*\text{ 全部晚于 }a,b\}
=(S\cup S')^c,
\qquad d_\uparrow=2h+\ell+\ell'>0.
$$

保留的四格为 $h,\ell,h,\ell'$。对偶偏序 $Q_\uparrow^*$ 满足共同下集条件，交换数为 $e(P)h$，两个不可交换数为 $e(P)\ell'$ 与 $e(P)\ell$，故得到第二条 (8)。

两次条件化使用的是 **两个不同事件**；既不将两条条件分布等同，也不改为同时条件化于它们的交集。

若希望直接用阻挡事件概率表达，设 $s=\Pr(S),t=\Pr(T),s'=\Pr(S'),t'=\Pr(T')$，则

$$
(s-k)(s'-k')\le h^2,\qquad
(t-k)(t'-k')\le h^2,\tag{9}
$$

等价地，

$$
(1-t-t')(s-k)\le(p-t)^2,\qquad
(1-s-s')(t-k)\le(p-s)^2.\tag{10}
$$

交集质量 $k,k'$ 必须保留；把 $r$ 换成 $s$，或把 $\ell$ 换成 $t$，会改变事件，不能由本证明推出。

## 五 有限检验能说明什么

精确整数枚举和独立纤维积分在 2 至 6 点的全部自然标号偏序上核对了 16,502 个共同下集不可比对，其中 6,428 对的 $N$ 不是链；另外在 2 至 5 点上对 2,126 个任意不可比对核对了两次条件化的扩张集合与四格映射，均与上述公式一致。自然标号是选取拓扑标号来枚举，相关结论对重标号不变。

一个可直接复算的旧范围之外实例是：$P$ 只有关系 $u<s$、$y<t$，另有两个孤立点。此时 $N$ 包含两个不可比的孤立点，且

$$
E=180,\qquad(H,R_u,R_y)=(60,30,30).
$$

这些检查用于核对事件定义、$n!$ 因子、边界情形和实现，不是任意规模结论的证明。一般性由第二节的四步论证给出。

## 六 与平衡猜想之间仍缺少的连接

MAIN33 指：每个有限非链偏序都存在固定实际标签 $x\parallel y$，使

$$
\Pr(x\text{ 先于 }y)\in[1/3,2/3].
$$

WIDTH3 是其在宽度至多三的全部非链偏序上的版本。本文并未完成这两个目标：

1. 平方界控制一个已给定元素对的局部计数，尚未提供对所有偏序有效的平衡对选择机制。
2. 任意对的 (8) 不直接控制双重阻挡质量 $k,k'$。例如抽象质量 $h=h'=1/10$、$k=7/10$、$k'=1/10$，其余四格为零，满足 (7)–(8)，却有 $p=4/5$。这只是标量约束不足的示例，未声称它可由某个偏序实现，更不是猜想反例。
3. 条件偏序中的好对不自动成为原偏序中的好对。除 (6)、(8) 等已经逐事件证明的回传外，仍需在同一原律下保留实际完成权重、联合事件与兼容的固定标签选择。
4. 对宽度三的终端分叉或跨边界候选，还需证明全局选择、迁移或覆盖确实能够闭合；移除 $N$ 成链这一条件，本身不提供这些缺失步骤。

因此，本结果的确定推进是共同下集平方界的无宽度适用范围，以及任意不可比对的两条原律约束；从这些约束到普遍平衡对存在性的连接仍未给出。

## 七 文献位置与新颖性边界

本文使用的 $p=2$ 解析输入属于 Busemann–Ball 理论。Ball 的 2022 年本人综述给出了所需精确版本；原始 1988 年论文是该理论的基础文献。[1,2]

Kahn–Yu 的 1998 年论文已经明确使用 Brunn–Minkowski 与 Ball 定理，将偏序概率问题降至二维。其公开摘要研究从 $\Pr(x<y)$、$\Pr(y<z)$ 推出 $\Pr(x<z)$ 下界的比例传递性，以及相应凸体概率问题。[3] 因而，不能把“次序多胞形、对数凹性、Ball 凸体、二维几何”这一方法路线宣称为首创。

还应明确一个已知特例：当共同不可比集 $N=\varnothing$ 时，非严格平方界可直接由 Chan–Pak（2024）的 Theorem 1.9 推出。[4] 此时共同下集 $D$ 是一个被迫的初始块；删去它后，只有 $u,y$ 两个极小元，合法交换的正方向扩张恰好以 $u,y$ 开头，而两方向不可交换事件恰好对应该定理的前两位后继事件。所有计数共同乘以 $e(D)$，不影响平方式。一般 $N$ 下这一事件识别不成立。

目前核对到的公开材料尚未确定本文完整适用范围的实际标签交换平方式及其双条件化形式，与既有文献定理是否等价、已包含于其中，或属于可直接推出的推论。**给出完整推导，不等于确认文献新颖性。**

## 八 有限偏序的严格性补充

在第一节的共同严格下集假设下，有限偏序还满足

$$
\boxed{H^2>R_uR_y.}\tag{11}
$$

这里需要额外使用有限次序多胞形的间隔结构；一般递减对数凹函数的解析不等式可以取等号，不能单凭凸性断言严格。以下给出关键论证，完整展开及逐项核对见配套的 [严格性证明](strict_shared_downset_square.txt) 与 [独立核对报告](strict_shared_downset_square_independent_audit.txt)。

沿用第二节的 $A,B,f,K$，令 $m=n-2$，并对 $0<q<1$ 定义

$$
I(q)=\int_0^\infty r f(r,qr)\,dr
=\frac12\int_\Omega\min(A,B/q)^2\,dz.
$$

**有限多项式性质。** 在一个删除扩张的单纯形
$0=z_0<z_1<\cdots<z_m<z_{m+1}=1$ 上，存在固定指标
$0\le\ell<\min(i,j)\le m+1$，使 $A=z_i-z_\ell$、$B=z_j-z_\ell$。若 $i\le j$，该单纯形对 $I(q)$ 的贡献为常数。若 $i>j$，令

$$
a=j-\ell\ge1,\qquad b=i-j\ge1,\qquad k=a+b.
$$

均匀单纯形间隔按 $B,A-B,1-A$ 分组后，$V=B/A$ 与 $A$ 独立，且 $V\sim\mathrm{Beta}(a,b)$；若最后一组为空，则 $A=1$，同一结论仍成立。令 $\mathrm B(a,b)=\int_0^1v^{a-1}(1-v)^{b-1}dv$，则

$$
\begin{aligned}
G_{a,b}(q)
&=\mathbb E\min(1,(V/q)^2)\\
&=1-\frac{2}{\mathrm B(a,b)}
\sum_{r=0}^{b-1}
\frac{(-1)^r\binom{b-1}{r}q^{a+r}}{(a+r)(a+r+2)}.
\end{aligned}
$$

这由有限二项式展开直接积分得到。该单纯形对 $I(q)$ 的贡献为
$k(k+1)G_{a,b}(q)/(2n!)$，次数至多 $k-1\le m$。有限求和表明 $I(q)$ 在 $(0,1)$ 上是非零多项式；$m=0$ 时它是常数 $1/2$。

**等号不可能。** $H>0$，因为共同下集之后可以连续排列 $u,y$ 并合法互换。若 (1) 取等号，则两侧剩余面积均为正，第四步中的支撑系数必有 $\alpha,\beta>0$，且两项面积上界都取等号。闭凸体的第一象限部分于是必须等于整个支撑三角形，否则将缺少一块正面积区域。

沿射线 $(t,qt)$ 比较边界位置，若其对角线点为 $(d,d)$，则 Ball 径向公式给出

$$
I(q)=\frac{(\alpha+\beta)^2d^2}{2(\alpha+\beta q)^2}.
$$

左边是非零多项式；右边是非恒定一次多项式平方的倒数乘以正常数。交叉相乘将迫使次数至少为二的多项式等于正常数，矛盾。因此 (11) 成立。

这一补充给出定性严格性，不给出新的统一定量系数，也不补齐第六节的全局平衡归约。

## 参考文献

[1] Keith Ball. *Convex geometry and its connections to harmonic analysis, functional analysis and probability theory*. Proceedings of the International Congress of Mathematicians 2022, Vol. 4, 3104–3139. Theorem 2 及随后说明见印刷页 3107–3108；Theorem 3 见印刷页 3108。[出版方全文](https://ems.press/content/book-chapter-files/33237)，[DOI](https://doi.org/10.4171/ICM2022/65)。

[2] Keith Ball. *Logarithmically concave functions and sections of convex sets in Rⁿ*. Studia Mathematica 88 (1988), 69–84。[DOI 与出版记录](https://doi.org/10.4064/sm-88-1-69-84)。本文所用精确定理版本以 [1] 可核验全文为准。

[3] Jeff Kahn and Yang Yu. *Log-Concave Functions And Poset Probabilities*. Combinatorica 18 (1998), 85–99。[出版方记录与摘要](https://link.springer.com/article/10.1007/PL00009812)，[Rutgers 作者机构记录与完整摘要](https://www.researchwithrutgers.org/en/publications/log-concave-functions-and-poset-probabilities/)。上述比较限于已核对的公开摘要，不声称已完成其全文的逐定理比对。

[4] Swee Hong Chan and Igor Pak. *Correlation inequalities for linear extensions*. Advances in Mathematics 458 (2024), 109954。Theorem 1.9 及式 (1.17) 见作者版第 4 页。[作者全文](https://www.math.ucla.edu/~pak/papers/Correlation17.pdf)，[DOI](https://doi.org/10.1016/j.aim.2024.109954)。
