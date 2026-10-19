# 独立审稿：NBU 截断协方差引理与单链前缀 actual 槽

日期：2026-10-18。

## 结论

**PASS。** 在非负整数截断参数 `0≤k≤l` 下，候选 NBU 引理成立。它确实证明了下述完整 actual 结构族的原辅助目标 T；没有证明任意嵌套 filters 的一般情形，也没有研究原全局猜想。

独立审稿核验了两种证明：经 `Cov(R,J)` 的原三步证明，以及 producer 后来提出的直接截断证明。后者还给出更强的

\[
\operatorname{Cov}(R,T)\le r(1+r-p_k)\le r(r+1).
\]

目前无承重缺口。唯一必须写清的表述条件是：`k,l` 为非负整数；actual 的 `suffix_k` 指删除链最前面 k 点后的后缀，而不是长度为 k 的后缀。下文固定零基链标号，消除这一歧义。

## 1. 精确定义

J 为非负、有限支持的整数随机变量，

\[
p_i=\Pr(J\ge i),\qquad p_0=1.
\]

有限支持外令 `p_i=0`。假定对所有非负整数 i,j 都有

\[
p_{i+j}\le p_i p_j.\tag{NBU}
\]

取非负整数 `0≤k≤l`，定义

\[
R=\min(J,k),\quad T=\min(J,l),\quad r=\mathbb ER,\quad s=\mathbb ET.
\]

待证结论为

\[
\operatorname{Cov}(R,T)\le r(r+1).\tag{L}
\]

这里 r 是截断变量 R 的均值，不是 J 的均值。

## 2. 原三步证明：逐步独立复核

### 2.1 协方差比较方向正确

对 J 的独立同分布副本 J'，任意两个递增函数 f,g 满足

\[
2\operatorname{Cov}(f(J),g(J))
=\mathbb E[(f(J)-f(J'))(g(J)-g(J'))]\ge0.
\]

取 `f(x)=min(x,k)`、`g(x)=x-min(x,l)`。二者均递增，所以

\[
\operatorname{Cov}(R,J)-\operatorname{Cov}(R,T)
=\operatorname{Cov}(R,J-T)\ge0.\tag{1}
\]

这一步不需要 NBU，但需要 J 的相关矩存在；有限支持已经充分保证。

### 2.2 NBU 条件剩余均值界正确

令 `μ=EJ`。对于 `p_i>0`，

\[
m_i:=\mathbb E[J-i\mid J\ge i]
=\sum_{h\ge1}\frac{p_{i+h}}{p_i}
\le\sum_{h\ge1}p_h=\mu.\tag{2}
\]

`p_i=0` 时不定义条件期望，原协方差展开中的该项本来就是零，直接略过即可。利用整数尾和 `R=Σ_{i=1}^k 1_{J≥i}`，得到

\[
\begin{aligned}
\operatorname{Cov}(R,J)
&=\sum_{i=1}^k p_i\bigl(\mathbb E[J\mid J\ge i]-\mu\bigr)\\
&=\sum_{i=1}^k p_i(i+m_i-\mu)
\le\sum_{i=1}^k i p_i.\tag{3}
\end{aligned}
\]

没有除以零，也没有遗漏 `i=0` 项；后者的 R 尾和中本来不存在。

### 2.3 三角尾和的计数与 NBU 使用正确

对每个 `i≥2`，正整数对 `(u,v)` 满足 `u+v=i` 的个数恰为 `i−1`，因此

\[
\begin{aligned}
\sum_{i=1}^k i p_i
&=r+\sum_{u,v\ge1,\ u+v\le k}p_{u+v}\\
&\le r+\sum_{u,v\ge1,\ u+v\le k}p_u p_v
\le r+r^2.\tag{4}
\end{aligned}
\]

最后一个不等式只是将非负三角和补成 `[1,k]×[1,k]` 的矩形和。结合 (1)–(4)，(L) 成立。

## 3. producer 新增直接证明和加强式也成立

令 `W=min(J,l)=T`。W 的尾列是 `q_i=p_i`（`0≤i≤l`）、`q_i=0`（`i>l`）。如果 `i+j≤l`，NBU 由原尾列直接继承；如果 `i+j>l`，左侧为零。因此截断保留 NBU。

由于 `R=min(W,k)`，可以直接把第 2.2 节的 J 换成 W、μ 换成 s，得

\[
\operatorname{Cov}(R,T)\le\sum_{i=1}^k i p_i.
\]

这个版本完全绕过 J 的协方差比较。事实上只要 J 的尾列满足 NBU、k,l 有限，就不再需要 J 本身有有限均值；但本次原定理使用有限支持假设已足够，不必扩大表述范围。

对 `k≥1`，还有

\[
\begin{aligned}
\sum_{i=1}^k i p_i
&=\sum_{u=0}^{k-1}\ \sum_{v=1}^{k-u}p_{u+v}\\
&\le\sum_{u=0}^{k-1}\ \sum_{v=1}^{k}p_u p_v\\
&=r\left(\sum_{u=0}^{k-1}p_u\right)
=r(1+r-p_k).\tag{5}
\end{aligned}
\]

每个 `p_i` 在第一行恰被计 i 次；`u=0` 的 NBU 是等式，故没有特殊例外。`k=0` 时 R 恒为零，单独判定即可。

## 4. actual 结构应用：全部映射与偏移

令

\[
U=C_a\sqcup V,\qquad
C_a=(c_0<c_1<\cdots<c_{a-1}),\qquad
|V|=b\ge1,
\]

其中 `a≥0`，V 内部可以是任意有限偏序，两块之间完全没有可比关系。

对整数 `0≤k≤l≤a`，令

\[
A=\{c_k,\ldots,c_{a-1}\}\cup V,
\qquad
B=\{c_l,\ldots,c_{a-1}\}\cup V.
\]

当 k 或 l 等于 a 时，对应链后缀为空。两集合始终为非空上理想，且 `A⊇B`。

### 4.1 uniform-LE 因子分解无隐藏加权

每条 U 的线性扩张唯一对应：V 的一条线性扩张，以及含 a 个 C、b 个 V 的一个 shuffle 字。反之每个这样的二元组产生一条 U 扩张。因此

\[
e(U)=e(V)\binom{a+b}{a}.
\]

每条 V 内部扩张都配同样多的 shuffle，故均匀 U 扩张的 shuffle 是均匀的，并且与 V 的内部扩张独立。**V 内部偏序无需为链，也不会改变 J 的分布。**

令 J 是 shuffle 开头连续 C 的个数。则 J 的支持为 `{0,…,a}`，且

\[
p_i=\Pr(J\ge i)
=\frac{\binom{a+b-i}{a-i}}{\binom{a+b}{a}}
=\frac{(a)_{\underline i}}{(a+b)_{\underline i}}
\quad(0\le i\le a),
\]

`p_i=0` 对 `i>a`。

### 4.2 actual 尾列确实满足 NBU

对 `0≤j<a`，令

\[
q_j=\frac{p_{j+1}}{p_j}=\frac{a-j}{a+b-j}.
\]

相邻之差

\[
q_{j+1}-q_j
=-\frac{b}{(a+b-j-1)(a+b-j)}<0
\]

在两者均处于定义范围时成立。因此若 `i+j≤a`，

\[
\frac{p_{i+j}}{p_i}
=\prod_{h=0}^{j-1}q_{i+h}
\le\prod_{h=0}^{j-1}q_h=p_j.
\]

`i+j>a` 时左侧尾概率为零；`p_i=0` 时也无需取比值，直接判零。故 NBU 覆盖所有非负整数参数，包括支撑边界。

### 4.3 首次槽恰为截断量，无一位偏移

f_U 为一基秩，槽是首次命中 filter 之前的旧 U 点数：

\[
R_A=\min_{x\in A}f_U(x)-1,
\qquad R_B=\min_{x\in B}f_U(x)-1.
\]

如果首个 V 早于 `c_k` 出现，则此前恰有 J 个 C，槽数为 J；否则扩张首 k 个位置恰为 `c_0,…,c_{k-1}`，首次 A 是 `c_k`，槽数为 k。`k=a` 时 A=V，槽数为 J。因此逐条扩张都有

\[
R_A=\min(J,k)=R,\qquad R_B=\min(J,l)=T.
\]

这里没有再加中央槽，没有把一基首次秩直接当作槽数。

## 5. 与原辅助目标 T 的等价核验

为避免随机变量 T 和目标名称 T 混淆，本节把目标称作 `目标 (T_slot)`。因为逐点 `R≤T`，所以 `r≤s`、`min(R,T)=R`。于是

\[
N=\mathbb E[RT+\min(R,T)]=\mathbb E[RT]+r,
\]

且函数 `x²+2x` 在非负半轴递增，故

\[
\begin{aligned}
N\le rs+\min(r^2+2r,s^2+2s)
&\iff \mathbb E[RT]+r\le rs+r^2+2r\\
&\iff \operatorname{Cov}(R,T)\le r^2+r.
\end{aligned}
\]

因此本族的目标 (T_slot) 与协方差目标完全等价，且两个余量恰相等：

\[
rs+r^2+2r-N=r(r+1)-\operatorname{Cov}(R,T).
\]

这个等价依赖逐点嵌套，不应迁移到一般非嵌套 filters。

## 6. 边界与退化核验

- `a=0`：必有 `k=l=0`，A=B=V=U，J=R=T=0，两目标等号。
- `k=0`：A=U，R=r=0，不论 l，混合矩和协方差均为零，两目标等号。
- `l=0`：由 `k≤l` 也有 k=0，仍为上一情形。
- `k=l`：R=T，证明给出对应方差界，未要求 filters 相异。
- `l=a`：B=V，T=J；原经 J 证明第一步为等式。
- `k=l=a`：A=B=V，R=T=J；`p_a>0`，全部公式成立。
- `a>0,k>0`：因 `k≤a`，有 `r>0,p_k>0`，加强式给出实际正余量 `r(r+1)−Cov(R,T)≥r p_k>0`。因此本 actual 族只有零均值边界能取等号。
- `b=1` 已在主定理范围内。producer 最终稿另补 `b=0` 退化，亦已独核：此时 J=a 确定，若沿原模型对空 filter 定义槽 n=a，则所有阈值都有 R=k,T=l、Cov=0；尾在 0,…,a 上为 1、之后为 0，直接满足 NBU。该退化必须避开 q_a 的 0/0 比值，最终稿已明确避开；若不采用空 filter 槽约定，则只保留非空后缀。
- 对抽象引理，允许 k、l 超出 J 的支撑；条件概率为零的项略去即可。无需预设 `p_k>0`。

## 7. 独立 exact 控制：固定极小诊断，不作大枚举

已运行 `check_exact.py`，完整有理结果保存于 `exact_controls.json`。

### 7.1 四个固定抽象分布

1. `J=0,k=l=0`：两侧为零。
2. `J=min(G,3)`，`P(G≥i)=2^(−i)`，`k=2,l=3`：`r=3/4,s=7/8,Cov=27/32`，原界 `21/16`，加强界 `9/8`。
3. `J~Binomial(3,1/2)`，`k=1,l=3`：`r=7/8,s=3/2,Cov=3/16`，原界 `105/64`，加强界 `7/8`。
4. 必要性反向控制：`P(J=0)=9/10,P(J=3)=1/10,k=1,l=3`。该分布不满足 NBU，`p_2=1/10>p_1²`。其 `Cov=27/100>r(r+1)=11/100`。这个例子仅说明不能无条件删除 NBU，不是 actual 反例。

### 7.2 七个固定 actual 对象

逐条直接枚举这七个指定小偏序的线性扩张，共 167 条；逐条按首次 filter 命中计算槽，独立对照 `min(J,k),min(J,l)`。

- `a=0,b=2,k=l=0`，V 为两点反链：2 条 LE，r=s=Cov=0。
- `a=3,b=2,k=0,l=3`，V 为两点链：10 条 LE，r=0,s=1,Cov=0。
- `a=3,b=2,k=1,l=3`，V 为两点链：10 条 LE，`r=3/5,s=1,Cov=2/5`，原余量 `14/25`。
- 同一 `a,b,k,l`，V 改为两点反链：20 条 LE，归一化完整联合槽分布与上一项完全相同。
- `a=3,b=2,k=l=3`，V 为两点反链：20 条 LE，`r=s=1,Cov=1`，原余量 1。
- `a=4,b=3,k=2,l=4`，V 为向上二分叉：70 条 LE，`r=6/7,s=1,Cov=6/7`，原余量 `36/49`。
- 同一 `a,b,k,l`，V 改为三点链：35 条 LE，归一化完整联合槽分布与上一项完全相同。

全部逐条槽恒等式、tail 比值公式、NBU、协方差界、加强界和两个目标的余量等式均通过。这些控制只检查计算与偏移，定理的全参数有效性来自上述证明。

## 8. 随机 cap 的独立附录控制

父任务另外给出的随机 cap 边界控制已用直接有理矩独立复核，无新搜索。取

\[
\Pr(J=0,1,2,3)=(1/2,1/4,1/8,1/8),
\]

其尾为 `1,1/2,1/4,1/8,0,…`，满足 NBU。令 K 与 J 独立，`P(K=0)=9/10`、`P(K=3)=1/10`，并令 R=J∧K、T=J。

设 B 是事件 K=3 的指示变量，则 R=BJ，B 与 J 独立。直接算得

\[
\mathbb EJ=7/8,\qquad \mathbb E J^2=15/8,
\qquad\operatorname{Var}J=71/64,
\]

\[
r=7/80,\qquad
\operatorname{Cov}(R,T)=\tfrac1{10}\operatorname{Var}J=71/640,
\]

\[
r(r+1)=609/6400,\qquad
\operatorname{Cov}(R,T)-r(r+1)=101/6400>0.
\]

全部给定分数正确。这个例子仅否定把确定 cap 引理无条件推广成独立随机 cap 的抽象命题；并未实现为 actual poset，不是 actual 槽目标或原猜想的反例。特别地，此例中 T 不依赖 K，条件均值的协方差项实际为零，混合失效仍可发生，原因是对条件右侧的平均不能用无条件 r(r+1) 替换。

## 9. producer 最终稿的二次复核

已逐式阅读最终源稿 `nested-prefix-slot-bound-20261018/RESULT.md`（其中包含无除法 D1/D2 证明、b=0 退化及随机 cap 附录），整体 **PASS**。

- `E[T 1_{J≥i}]=i p_i+Σ_{j=i+1}^l p_j` 正确，故最终式 (N1) `Cov(R,T)=H_k−D1` 是精确恒等式；逐项 NBU 给 D1≥0，完全避免零概率条件期望。
- 矩形余量 `D2=r(1+r−p_k)−H_k≥0` 正确，因此最终式 (N3) `r(r+1)−Cov=rp_k+D1+D2` 是精确非负分解。
- 最终式 (P5) 的混合矩来自函数 `(j∧k)(j∧l)` 的相邻差：在 1,…,k 为 2i−1，在 k+1,…,l 为 k，故公式正确。
- 最终式 (P6) 由 `(b+1)p_i=(a−i+1)p_{i−1}−(a−i)p_i` 望远镜正确。
- 对唯一旧例 `(a,b,k,l)=(10,190,7,9)`，另以 `P(J=j)=p_j−p_{j+1}` 直接求原始 PMF 矩（不复用 producer 的尾矩式），其 r、s、N 与共同 gap 四项，逐项等于最终稿保存的分数。

二次复核未发现新增问题，无需修订结论。上述旧例与随机 cap 两项的独立复核源码为 `check_final_addenda.py`，精确输出为 `final_addenda_checks.json`。

## 10. 审稿状态及范围

**最终判定：PASS；无待补数学缺口。** 此结论新增的是明确的全参数结构覆盖：一个独立链块与任意非空独立偏序块之并，两个 filters 都包含整个偏序块并在该链上取嵌套后缀。

结论没有扩张到任意 uniform-LE 槽尾列 NBU、任意两嵌套上理想、跨块存在可比关系的偏序，或原全局猜想。计算仅限本地固定控制，没有对外写入。
