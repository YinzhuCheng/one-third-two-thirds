# 自主模块局部对偶：秩反射、插入窗口与最小失效边界

## 0. 范围与主结论

只把偏序的一个自主模块内部反序，外部元素及所有跨模块关系保持原状。这里不重证全局对偶保持 balance，也不研究原 1/3–2/3 猜想的反例。

记
\[
\pi_P(x,y)=\Pr_{L\sim\operatorname{UnifLE}(P)}(x\text{ 先于 }y),\quad
\beta(t)=\min(t,1-t),\quad
\delta(P)=\max_{x\parallel_Py}\beta(\pi_P(x,y));
\]
没有不可比对时取最大值为 0。称 pair 为 \(\tau\)-balanced，指其概率在 \([\tau,1-\tau]\)，通常 \(\tau=1/3\)。

本文的已证结果：

1. 局部对偶有精确的内部秩反射双射。模块内 pair 概率互补，模块外 pair 概率不变；唯一非平凡变化来自跨模块 pair。
2. 跨模块概率由同一个外部插入窗口 law 与原/反射的内部 rank law 配对。若所有相关窗口关于模块中点对称，则逐跨 pair 的 balance 保持，因而 \(\delta\) 保持。
3. 窗口对称有不要求内部或上下环境互为对偶的无界结构充分族。更一般还给出内部 rank-law 反射匹配、任意窗口下的 witness 传递，以及有明确常数的稳定性界。
4. 无条件 \(\delta\) 保持是假的，最小实际反例有 6 点，\(\delta=4/9\to1/2\)。无条件保持同一带标签 pair 的 balance 已在最小 4 点例失效。这些均不否定原猜想。

## PD1. 合法操作与均匀双射

设 \(M\ne\varnothing\) 是有限偏序 \(P\) 的自主模块，\(m=|M|\)：对每个 \(y\notin M\)，以下三种情形恰有一种成立：

- \(y<a\) 对所有 \(a\in M\)；
- \(a<y\) 对所有 \(a\in M\)；
- \(a\parallel y\) 对所有 \(a\in M\)。

记对应外部集合为 \(D,U,V\)。令 \(P^{\langle M\rangle}\) 只把 \(P[M]\) 的序反转，所有其他关系原样保留。这仍是偏序：它就是把商偏序中的指定点替换为 \(P[M]^d\)，不存在可穿过一个外点再回到模块的非平凡中间约束。

把 \(M\) 替换为固定链 \(1<\cdots<m\)，外部不变，所得偏序记为 \(R\)。每个 \(P\) 的扩张唯一分解为：

- \(R\) 的一个扩张，记录外部带标签元素和 \(m\) 个模块 slots；
- \(P[M]\) 的一个内部扩张，依次填入这些 slots。

因此
\[
\operatorname{LE}(P)\simeq \operatorname{LE}(R)\times\operatorname{LE}(P[M]).
\tag{PD1.1}
\]
两个因子在均匀扩张下独立且各自均匀。每个 skeleton 的纤维大小都是 \(e(P[M])\)。局部对偶保留 skeleton，把填入的内部扩张逆序；这是一个双射，故
\[
e(P^{\langle M\rangle})=e(P),
\tag{PD1.2}
\]
且双射两侧均为均匀 law。注意：模块在完整扩张中不必连续；这里保留的是其所有 slots。

该操作保持全部可比/不可比的无向点对，故大小、最大不可比度、宽度和高度也都保持；它本身不提供参数放大。

立即得到完整 pair 分类：

- 模块内部：\(\pi_{P^{\langle M\rangle}}(a,b)=1-\pi_P(a,b)\)，故 balance 保持。
- 模块外部：\(\pi_{P^{\langle M\rangle}}(x,y)=\pi_P(x,y)\)，故 balance 保持。这里的概率是完整偏序的外部边缘分布，不能无证明地换成诱导外部偏序的均匀 law。
- 模块与 \(D\cup U\)：本来可比，仍然可比且方向不变。
- 模块与 \(V\)：全部不可比，变化恰如下述公式。

## PD2. 跨模块的秩反射公式

对 \(a\in M\)，令
\[
\mu_a(i)=\Pr(\operatorname{rank}_{L_M}(a)=i),\qquad
F_a(q)=\sum_{i\le q}\mu_a(i),\quad F_a(0)=0.
\]
在均匀 \(\operatorname{LE}(R)\) 中，对 \(y\in V\) 定义
\[
T_y=\#\{\text{位于 }y\text{ 之前的模块 slots}\}\in\{0,\ldots,m\},\qquad
K_y(i)=\Pr(T_y\ge i).
\]
由 PD1 的独立性，
\[
\boxed{\begin{aligned}
 p_{a,y}:=\pi_P(a,y)&=\sum_i\mu_a(i)K_y(i)=\mathbb E F_a(T_y),\\
 p'_{a,y}:=\pi_{P^{\langle M\rangle}}(a,y)
 &=\sum_i\mu_a(i)K_y(m+1-i)\\
 &=1-\mathbb E F_a(m-T_y).
\end{aligned}}
\tag{PD2.1}
\]
特别地，内部逆序虽是均匀双射，但不意味着固定跨模块 pair 的概率保持或互补。关键是内部 rank 的反射与外部窗口是否匹配。

## PD3. 外部插入窗口的精确 law

以下把 PD2 中的 \(T_y\) 完全写成外部偏序的数据。设 \(N=P\setminus M\)，取外部偏序 \(P[N]\) 的一个线性扩张 \(L\)，长度为 \(n\)。定义
\[
b(L)=\max\{\operatorname{pos}_L(d):d\in D\},\quad
\nu(L)=\min\{\operatorname{pos}_L(u):u\in U\},
\]
空集时分别用 \(0,n+1\)。由于每个 \(d\in D\) 都小于每个 \(u\in U\)，有 \(b<\nu\)。令
\[
r(L)=\nu-b-1.
\]
模块 slots 只能插入最后一个 \(D\) 之后、第一个 \(U\) 之前，与窗口中的 \(r\) 个已固定相对次序的外点交织。故该外部扩张的 skeleton 纤维大小为
\[
w(L)=\binom{m+r(L)}m.
\tag{PD3.1}
\]
因此均匀 skeleton 投影到外部扩张时，\(L\) 的权重正比于 \(w(L)\)，通常不是均匀分布。这一偏权只依赖模块大小，完全不依赖模块内部偏序。

固定 \(y\in V\)，令 \(k=\operatorname{pos}_L(y)\)。给定 \(L\)：

- 若 \(k\le b\)，则 \(T_y=0\)；
- 若 \(k\ge\nu\)，则 \(T_y=m\)；
- 若 \(b<k<\nu\)，置 \(t=k-b\in\{1,\ldots,r\}\)，则
\[
\Pr(T_y=q\mid L)
 =\frac{\binom{q+t-1}{q}\binom{m-q+r-t}{m-q}}
        {\binom{m+r}{m}},\qquad 0\le q\le m.
\tag{PD3.2}
\]
分子分别数 \(y\) 前后的交织。对所有外部 \(L\) 按 PD3.1 的权重混合即得完整 law。

条件窗口具有严格反射恒等式
\[
h_{m,r,t}(q)=h_{m,r,r+1-t}(m-q).
\tag{PD3.3}
\]
故一种可核验的充分条件是：加权的外部窗口描述 law 在交换“窗口前/窗口后”、以及 \((r,t)\leftrightarrow(r,r+1-t)\) 下不变。这保证 \(T_y\overset d=m-T_y\)。其成立不要求完整外部偏序有反自同构。

## PD4. 保持结论的充分条件

### PD4a. 窗口对称：任意内部模块均适用

若对每个 \(y\in V\)，
\[
T_y\overset d=m-T_y,
\tag{PD4.1}
\]
则由 PD2 得
\[
p'_{a,y}=1-p_{a,y}\quad(a\in M,y\in V).
\]
结合完整 pair 分类，每个相同带标签不可比 pair 的 balance 均保持，从而
\[
\boxed{\delta(P^{\langle M\rangle})=\delta(P).}
\tag{PD4.2}
\]
所有 \(\tau\)-balanced pair 的存在性也保持，原 witness 本身仍可使用。

更一般，只需存在外部不可比点集上的一个置换 \(\sigma:V\to V\)，使 \(T_{\sigma(y)}\overset d=m-T_y\)。此时 \(p'_{a,y}=1-p_{a,\sigma(y)}\)，跨 pair 的 balance 集合在置换下保持，仍有 \(\delta\) 保持；\(\sigma\) 不必延伸为整个偏序的反自同构。逐点窗口对称是 \(\sigma=\operatorname{id}\) 的特例。

逐点窗口对称 (PD4.1) 的等价纯核条件为
\[
K_y(i)+K_y(m+1-i)=1\quad(1\le i\le m).
\tag{PD4.3}
\]
证明等价性：反射变量 \(m-T_y\) 的第 \(i\) 个 tail 是 \(1-K_y(m+1-i)\)，而离散 tail 全部相同当且仅当 law 相同。

### PD4b. 无界的等长上下环境族，不需互为对偶

设
\[
P=(D\oplus M\oplus U)\sqcup\{y\},\qquad d=|D|,\ u=|U|,
\]
其中 \(D,U\) 可为空，\(y\) 与其他所有点不可比；\(D,U,M\) 的内部结构任意。

每条 core 扩张中，模块恰占 core 的第 \(d+1,\ldots,d+m\) 个位置。孤立点 \(y\) 在 core 的 \(d+m+u+1\) 个 gaps 中均匀插入，与内部扩张独立。因此
\[
\Pr(T_y=0)=\frac{d+1}{s},\quad
\Pr(T_y=q)=\frac1s\ (1\le q\le m-1),\quad
\Pr(T_y=m)=\frac{u+1}{s},\quad s=d+m+u+1.
\tag{PD4.4}
\]
若 \(d=u\)，窗口对称，所以 PD4.2 成立。特别地，\(D,U\) 不必同构或互为对偶。例如上部、下部可取同样多点但结构不同的两个偏序；这是窗口位置的对称，不依赖全局对偶同构。

若 \(d\ne u\)，令 \(r_a=\mathbb E\operatorname{rank}_{L_M}(a)\)，则精确地
\[
p_{a,y}=\frac{m+u+1-r_a}{s},\qquad
p'_{a,y}=\frac{u+r_a}{s},\qquad
\boxed{p_{a,y}+p'_{a,y}-1=\frac{u-d}{s}.}
\tag{PD4.5}
\]
所以不对称的上下长度产生共同的互补缺陷，甚至与目标元素的 rank law 无关。

### PD4c. 内部 rank-law 反射匹配：任意外部环境均适用

定义 \((R\mu)(i)=\mu(m+1-i)\)。若对某 \(a\in M\) 存在 \(b\in M\) 使
\[
\mu_b=R\mu_a,
\tag{PD4.6}
\]
则对每个 \(y\in V\)，
\[
\pi_{P^{\langle M\rangle}}(a,y)=\pi_P(b,y).
\tag{PD4.7}
\]
因此原来 \((b,y)\) 的 balanced witness 可传为新的 \((a,y)\)，不要求窗口对称。

若所有元素的 rank laws 的集合在反射下闭合，则各 \(y\) 的可实现 cross 概率集合不变；加上模块内、外 balance 保持，仍有 \(\delta\) 完全保持。内部自对偶是此 rank 条件的一个结构充分条件，但证明实际只用 rank-law 闭合。

若 \(\mu_a=R\mu_a\)，则同一个 \((a,y)\) 的概率保持。具体无界族：内部模块为 \(A\oplus\{a\}\oplus B\)，\(|A|=|B|\)，则 \(a\) 具有确定的中间 rank，不论 \(A,B\) 是否互为对偶，该元素与每个外部不可比点的概率均在局部对偶后保持。

### PD4d. 已有非跨模块 witness 无条件保留

若某 \(\tau\)-balanced pair 完全在 \(M\) 内，或者完全在 \(P\setminus M\) 内，则该 pair 在局部对偶后仍然 \(\tau\)-balanced。只有“全部可用 witness 均跨模块”的情形，才必须额外控制窗口或 rank 反射。

## PD5. 非对称窗口的定量稳定性

令
\[
D_y(i)=K_y(i)+K_y(m+1-i)-1,\qquad
\epsilon_y=\max_{1\le i\le m}|D_y(i)|.
\]
PD2 给出精确互补误差
\[
p_{a,y}+p'_{a,y}-1=\sum_i\mu_a(i)D_y(i).
\tag{PD5.1}
\]
因为 \(\beta\) 是 1-Lipschitz 且 \(\beta(1-p)=\beta(p)\)，
\[
|\beta(p'_{a,y})-\beta(p_{a,y})|\le\epsilon_y.
\tag{PD5.2}
\]
令 \(\epsilon=\max_{y\in V}\epsilon_y\)，\(V\) 为空时取 0。完整 pair 分类遂给出
\[
\boxed{|\delta(P^{\langle M\rangle})-\delta(P)|\le\epsilon.}
\tag{PD5.3}
\]
更粗但易计算的上界为
\[
\epsilon_y\le d_{\rm TV}(\mathcal L(T_y),\mathcal L(m-T_y)).
\]
因此若一个跨模块 pair 原本有 \(\beta(p_{a,y})\ge\tau+\epsilon_y\)，局部对偶后仍有 \(\beta(p'_{a,y})\ge\tau\)。这是真正有余量的 witness 传递；没有余量时不能凭内部均匀逆序宣称同一 witness 保持。

对 PD4b 的环境，PD4.5 的误差恒定，故
\[
\epsilon=|u-d|/(d+m+u+1).
\]

## PD6. 无条件逐 pair balance 保持的最小实际反例：4 点

取
\[
P=(z<a<b)\sqcup\{y\},\qquad M=\{a<b\}.
\]
局部对偶只把 \(a<b\) 改为 \(b<a\)，得到 \(P'=(z<b<a)\sqcup\{y\}\)。每个偏序有 4 条扩张，即把 \(y\) 均匀插入对应三链的 4 个 gaps。于是
\[
\pi_P(a,y)=1/2,\qquad \pi_{P'}(a,y)=1/4.
\]
同一个 \(1/3\)-balanced witness 丢失了；但 \((b,y)\) 变为概率 \(1/2\)，所以两边 \(\delta\) 均为 \(1/2\)。

这是逐带标签 pair 的 balance 保持失败的最小点数：总点数至多 3 时，模块大小 1 不改变偏序；模块为全体时任意 pair 只互补；唯一其余非平凡情形是大小 2 的模块加一个外点。该外点若可比则没有 cross pair，若不可比则 \(T_y\) 在 \(0,1,2\) 上均匀且反射对称，因此每个 cross pair 的 balance 仍保持。

## PD7. 无条件 \(\delta\) 保持的最小实际反例：6 点

令
\[
M=\{a,b,c,d\},\qquad a<b<c,\quad a<d,
\]
并加外点 \(z<M\)，以及与其他所有点不可比的孤立点 \(y\)。即
\[
P=\bigl(z\oplus[a\oplus((b<c)\sqcup\{d\})]\bigr)\sqcup\{y\}.
\]
只反转 \(M\) 内部，得到 \(P'\)。原 core 的 3 条扩张为

- z a b c d
- z a b d c
- z a d b c

新 core 的 3 条扩张为

- z c b d a
- z c d b a
- z d c b a

在每个 core 词的 6 个 gaps 插入 \(y\)，各得全部 18 条扩张。模块内唯一的不可比对为 \(b,d\) 与 \(c,d\)，它们两侧的 balance 均为 \(1/3\)。全部涉及 \(y\) 的概率为
\[
\begin{array}{c|ccccc}
x&z&a&b&c&d\\\hline
\pi_P(x,y)&5/6&2/3&4/9&2/9&1/3\\
\pi_{P'}(x,y)&5/6&1/6&7/18&11/18&1/2
\end{array}
\]
其他 pair 都可比。因此
\[
\boxed{\delta(P)=4/9,\qquad\delta(P')=1/2.}
\tag{PD7.1}
\]
这也可直接从 PD4.5 取得：\(d=1,u=0,m=4\)，共同互补缺陷为 \(-1/6\)。

### 6 点最小性的严格证明

设总点数不超过 5，考虑任意自主模块 \(M\)。

1. \(|M|\le2\)：模块内部自对偶；一个反同构延伸为固定外点的 \(P\to P'\) 同构，故 \(\delta\) 保持。
2. \(|M|=3\)：所有三点偏序中，链、三点反链、二链并孤立点都是自对偶；唯一非自对偶两型为 V 与倒 V。后两型都有可交换的两个不可比分支，内部概率 \(1/2\)，由 PD1 其在完整偏序中仍为 \(1/2\)，故两侧 \(\delta=1/2\)。
3. \(|M|\ge4\)：至多一个外点。没有外点时每个 pair 内部互补。只有一个外点时，自主性使其要么小于全模块、要么大于全模块、要么与全模块不可比。前两种不产生 cross 不可比对；第三种的孤立点均匀插入 \(m+1\) 个 gaps，\(T_y\) 均匀于 \(0,\ldots,m\)，由 PD4a 得 \(\delta\) 保持。

以上覆盖总点数至多 5 的全部模块大小与所有合法外部关系。因此 PD7.1 确为最小实际反例，而不是“搜索到的最小”。局部对偶是对合，反向使用同例即得到 \(1/2\to4/9\)，所以 \(\delta\) 也不存在任一普适单调方向。

## 8. 结论边界、核验与接续

- 无条件 \(\delta\) 保持已被严格否定；同一 balanced cross witness 的无条件保持更早在 4 点失败。
- 尚未证明或否定“任意局部对偶都保持存在至少一个 1/3-balanced pair”。本文反例两侧都有此类 pair，不得把 \(\delta\) 的变化或单一 witness 丢失说成原猜想的反例。
- 可用的非平凡传递机制已精确归结为：外部窗口反射对称、内部 rank-law 反射匹配、或足够的 balanced 余量。模块外 law 的不均匀偏权已在 PD3 明确控制。
- 本轮只构造并核验两组 control，共 4 个不同的带标签偏序，未进行批量 poset 搜索。`verify.py` 直接逐排列枚举上述 4 点/6 点对象的全部扩张，输出在 `verification.txt`。6 点反例、两项最小性证明、PD4b 的结构窗口公式，以及一般 PD3/PD4c/PD5 的权重、反射闭合与误差界，均已由独立 worker 解析复核通过。审稿指出的 PD3 记号不一致已统一为 \(\nu(L)\)。

继承来源：`/workspace/shared/self-substitution-fibers-20261018/RESULT.md` 的均匀纤维方法、记号与 balance 定义。本文的局部双射只替换一个模块，并不假设所有模块等大小，也不把外部 pair 的边缘 law 当作诱导偏序的均匀 law。
