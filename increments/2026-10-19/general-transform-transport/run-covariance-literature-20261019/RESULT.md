# Ideal-run 有限 n 协方差界：定向文献定位

核验日期：2026-10-19。范围：只读核验五项紧邻来源；不作首创调查，不联系作者，不改变原全局猜想状态。输入为 `ideal-deletion-coupling-20261019/RESULT.md` 的已独审结论。本报告的文献对应与代数平移由本报告作者核对；不把这次定位误称为对输入全部证明的第二次独立审稿。

## 结论先行

1. **找到了核心删除比较 D5 的准确已发表祖先。** L. A. Shepp (1980), Theorem 2, eqs. (1.6), (2.17)，直接给出 D5。只需把被删 ideal 与一个独立 marker 放在一组，其余元素放在另一组；原跨边和 marker 事件都是同方向跨组不等式的交。完整离散映射见第 2 节。
2. 因此输入的 **C1、C3 及一般 slot T 可以可靠地称为 Shepp 单调性定理/FKG 的应用推论**：Shepp 提供 D5；精确 prefix 条件化、尾和及取 Y=X 闭合提供剩余初等推导。输入的连续合法纤维证明则把这个既有单调性机制具体展开，并额外保留了可计算的 FKG slack。**不能把核心单调性机制说成文献未见。**
3. 在所核五项来源中，**没有核到逐字陈述与输入 C1/C3 相同的有限 n 协方差公式**，也没有核到一个可直接替换 C3、在其全部参数上更强的标准公式。这只是本轮定向核验结果，不是新颖性或不存在性结论。
4. Chan–Pak 的已发表 rank-minimum 相关不等式非常接近，但 **1 起点到 0 起点的偏移不能省掉**。正确平移后，它给 `N−rs ≤ rs+r+s`，而不是输入的一般 slot T；其同变量特例只给 `Var X≤r(r+1)`。输入的有限 n 界更精细。
5. 负超几何分布解释了锐性族，不能无条件替代一般 ideal-run 分布。Chan–Pak 2024 的 Example 3.8 正使用两条不交链所产生的这一模型；它与输入界相容。

## 1. 对象与精确变量映射

P 是 n 点有限偏序，f 是均匀随机线性扩张。K,L 为 ideals，令

- X 为首次离开 K 前的元素数，Y 为首次离开 L 前的元素数；
- r=EX，s=EY，M=E[X(X+1)/2]；
- N=E[XY+min(X,Y)]。

若 K,L 都不是 P，则令 `S=P\K`、`T=P\L`，两者均非空，并记

`U=f_min(S)=X+1，V=f_min(T)=Y+1。`

任意非空子集的 rank minimum 也可用它的上闭包代替：`f_min(S)=f_min(S↑)`，所以 rank-minimum 文献覆盖这里的上理想情形。若 K=P 或 L=P，对应 run 是常数 n，应直接处理；不能把空集合的最小值塞入定理。

输入欲定位的公式为

`Cov(X,Y) ≤ (n−s)M/(n+1)`  (C1)

以及

`M ≤ (n+1)r(r+1)/(n+r+2)`，

`Var X ≤ (n−r)r(r+1)/(n+r+2)`，

`Cov(X,Y) ≤ (n−s)r(r+1)/(n+r+2)`。  (C3)

交换 X,Y 可取两侧最小值。一般 slot T 为

`N−rs ≤ min{r²+2r, s²+2s}`。

## 2. Shepp 1980：D5 是直接推论

### 来源与已发表状态

L. A. Shepp, *The FKG Inequality and Some Monotonicity Properties of Partial Orders*, SIAM Journal on Algebraic and Discrete Methods **1**(3) (September 1980), 295–299，DOI [10.1137/0601034](https://doi.org/10.1137/0601034)。

核对的原刊扫描：[原文 PDF](https://faculty.wharton.upenn.edu/wp-content/uploads/2012/04/Fkg-inequality-and-some-monotonicity-properties-of-partial-orders.pdf)。定理在 **Theorem 2, p. 296, eq. (1.6)**；证明的无歧义乘积式在 **p. 299, eq. (2.17)**。期刊网页显示的 2006 年是数字化上线日期，不能替代原刊年份 1980。

### 准确可用命题

把标号分为两组 A₀、B₀。Q₀ 只施加各组内部的任意偏序关系，**没有跨组关系**。E,F 都是若干同方向关系 `a<b`（a∈A₀，b∈B₀）的交。则在均匀随机排列下

`Pr(E∩F | Q₀) ≥ Pr(E | Q₀) Pr(F | Q₀)`。

等价地，`Pr(F | Q₀∩E) ≥ Pr(F | Q₀)`。不得将它误用成“在已经含任意跨组约束的基底上，继续加入跨边总提高同向事件概率”；Shepp 原文开头就给出这种强化的反例。

### 对输入 D5 的完整离散实现（本报告推导）

固定输入第 2 节中的 ideal `A⊆L`，`|A|=i`，置 `Q=P\A`。加入一个新元素 c。分组为

`A₀=A∪{c}，B₀=Q`。

- Q₀ 只保留 P[A] 和 P[Q] 的内部关系，c 完全自由。
- E 是 P 中所有跨边 `a<q` 的交，其中 a∈A、q∈Q。
- F 是 `c<v` 对所有 `v∈P\L` 的交。

A 是 ideal，保证原跨边只有 A→Q，故 E 合法。A⊆L 保证 P\L⊆Q，故 F 也合法。于是 Shepp Theorem 2 适用。

设 `μ_A=E_{LE(Q)} R_{L\A}`，且先取 L≠P。在 Q₀∩E 下，原 n 点满足完整 P，c 与全部原点独立无序。给定任意原扩张，c 有 n+1 个等可能插入槽，其中 Y+1 个在首个 P\L 元素之前。因此

`Pr(F | Q₀∩E)=(s+1)/(n+1)`。

在 Q₀ 下，删去 A 后，Q∪{c} 的相对排列是 `LE(Q+{c})` 的均匀分布。理由是每个固定的 Q∪{c} 扩张都恰有 `e(P[A]) binom(n+1,i)` 个前像，数量相同。因此

`Pr(F | Q₀)=(μ_A+1)/(n−i+1)`。

两式代入 Shepp 不等式得到

`(μ_A+1)/(n−i+1) ≤ (s+1)/(n+1)`，

即输入 D5：

`μ_A ≤ s−i(s+1)/(n+1)`。

L=P 时 `s=n，μ_A=n−i`，同一公式直接为等号，无须定义空集合最小值。

这个映射也说明输入的 `+1` 与维数因子来自真实插入槽数，不是记号上的可选偏移。

### 与输入连续纤维证明的关系

输入证明把一般删除后的残余边缘写成 `W_A(u)dν_Q/E W_A`，并利用 H、W_A 同向递增得到比较。这与 Shepp 的 FKG 单调性同属一个机制：给独立两组加入 A→Q 约束，会提高适当的同向跨组事件概率。离散 marker 版本已足以给本题所需的 H 均值比较；输入的显式 W_A 还提供逐纤维 slack 恒等式，后者不是 Shepp 原文已陈述的公式。

## 3. 从已发表 Shepp 定理到 C1/C3：需要补上的准确步骤

以下是本报告对“直接推论”一词的数学解释，**不声称这些公式已印在 Shepp 论文中**。

固定一个长度 i 的合法精确 K-prefix word w，记其元素集合 A。条件于 w 后，残余扩张与 `LE(P\A)` 一一对应，所以残余确实均匀。

若 A⊆L，利用第 2 节的 D5，得到

`E[Y | prefix=w] ≤ s+i(n−s)/(n+1)`。

若 A⊄L，prefix 内已经出现 L 外元素，Y 被该 word 确定，且 `Y≤i−1`，同一个上界仍成立。因此不需要 K⊆L。对所有真实 prefix 条件权混合，得到

`E[Y | X≥i]−s ≤ i(n−s)/(n+1)`。

利用整数变量的尾和恒等式，

`Cov(X,Y)=Σ_{i≥1} Pr(X≥i)(E[Y|X≥i]−s)`，

立即给出 C1。再取 Y=X，并用 `Var X=2M−r(r+1)`，有

`2M−r(r+1) ≤ (n−r)M/(n+1)`。

移项就是 C3 中的 M 界；回代得到方差与一般协方差界。最后 `E min(X,Y)≤min(r,s)` 导出一般 slot T。

所以，**把整项结果定位为“由经典 Shepp/FKG 单调性，通过 prefix 条件化与二阶矩自闭合得到的有限 n 推论”是有充分来源支撑的。** 是否历史上已有人以相同公式明确写过，需要另一项专门历史调查；本轮未做，也不能据检索未命中作否定断言。

## 4. Chan–Pak 2024：紧邻但较弱的 rank-minimum 定理

### 来源、版本与发表状态

Swee Hong Chan and Igor Pak, *Correlation inequalities for linear extensions*, **Advances in Mathematics 458 (2024), article 109954**，DOI [10.1016/j.aim.2024.109954](https://doi.org/10.1016/j.aim.2024.109954)。发表信息由作者机构的[出版记录](https://www.researchwithrutgers.org/en/publications/correlation-inequalities-for-linear-extensions/)核实。

阅读的是作者网站 [Correlation17.pdf](https://www.math.ucla.edu/~pak/papers/Correlation17.pdf)，首页日期 **September 12, 2024**，25 页。对应 arXiv [2211.16637v2](https://arxiv.org/abs/2211.16637v2) 的修订日期为 2024-09-12；v1 初次提交为 2022-11-30。作者稿/预印本载体与已发表论文是同一项文献，不能称它仍仅为未发表预印本。

### 准确结论与偏移（Thm 1.8, eq. (1.16), p. 3；证明 §6.3, pp. 16–17）

任意有限 P，任意非空子集 S,T：

`E[UV]+E[min(U,V)] ≤ 2 EU EV`，

其中 U=f_min(S)、V=f_min(T)。**无需 S,T 不交、principal、嵌套或仅含极小元。** 其证明添加两个新极小 marker，再使用扩张数相关不等式。

代入 U=X+1、V=Y+1 后：

`E[UV]+E min(U,V)=N+r+s+2`，

`2 EU EV=2rs+2r+2s+2`，

故正确结果为

`N−rs ≤ rs+r+s`。  (CP-shift)

若 K⊆L，则 min(X,Y)=X，故 CP-shift 只给

`Cov(X,Y) ≤ s(r+1)`。

若取 S=T（即 X=Y），则给

`E[(X+1)(X+2)] ≤ 2(r+1)²`，

等价于 `Var X≤r(r+1)` 或 `E binom(X,2)≤r²`。

输入 C3 在有限 n 增加因子 `(n−r)/(n+r+2)`，而非仅重复该弱二阶矩界。对一般 slot T，若 r≤s，则

`(rs+r+s)−(r²+2r)=(s−r)(r+1)≥0`，

所以 CP-shift 不能直接推出输入 T；对 r≠s，其右侧还严格更大。

**编号提醒：** 阅读的 2024 作者稿中一般 log-concave 二阶矩结论编号为 **Proposition 3.6**，几何型锐性例为 **Example 3.8**。旧版本或后来的 survey 可能使用不同编号；引用时应写清版本，不能拼接旧编号和新页码。

## 5. 负超几何模型与锐性：可以核对什么，不能偷换什么

Chan–Pak 2024 **Example 3.8, p. 8** 取两条不交链 `P=C_m+C_{n−m}`，并取 C_m 的最小元 x，给出 f(x) 的组合求和；随 `m→∞，m=o(n)`，二阶矩比趋于 2。令 K 为另一整条链，则 `X=f(x)−1`，即首次抽到 C_m 颜色前另一颜色的数量。

下面是对同一模型的自含计算，未依赖新增统计文献：若 K 与 B=P\K **完全没有跨边**，且 `|K|=h，|B|=b=n−h≥1`，各块内部偏序任意，均匀扩张的二色 word 是均匀 shuffle。因此

`Pr(X=j)=binom(n−j−1,b−1)/binom(n,b)`，`0≤j≤h`，

`EX=h/(b+1)`，

`E[X(X−1)]=2h(h−1)/((b+1)(b+2))`，

`Var X=hb(n+1)/((b+1)²(b+2))`。

这就是“直到首个 B 为止、此前 K 数量”的负超几何约定。若统计首次 B 的秩，变量应为 X+1；若文献统计总抽取数，均值也随之加 1。

代入 r=h/(b+1)，有

`(n−r)/(n+r+2)=b/(b+2)`，

所以以上精确方差正等于输入 C3b 右侧。反链是这一无跨边模型的特例，两条不交链是同一模型的另一特例。因此 CP 的渐近锐性例与我们的有限 n 锐性并不冲突。

**边界：** 一般 ideal K 可以有 K→B 跨边，二色 word 不再均匀 shuffle，run 通常不服从同参数负超几何。精确负超几何矩公式只核对等号模型；要把它扩成一般矩上界，必须另有已证比较。这里承担该工作的正是 Shepp/D5 与 prefix 推导。

## 6. 另外三项来源：各自承担什么

### 6.1 Fortuin–Kasteleyn–Ginibre 1971：基础关联定理

C. M. Fortuin, P. W. Kasteleyn, J. Ginibre, *Correlation Inequalities on Some Partially Ordered Sets*, **Communications in Mathematical Physics 22 (1971), 89–103**，DOI [10.1007/BF01651330](https://doi.org/10.1007/BF01651330)。核对[原刊扫描](https://math.bme.hu/~balint/oktatas/perkolacio/percolation_papers/fortuin_kasteleyn_ginibre.pdf) **Proposition 1, p. 91, eqs. (2.1)–(2.2)**。

有限 distributive lattice 上的非负权 μ 满足 `μ(x∧y)μ(x∨y)≥μ(x)μ(y)` 时，两同向单调函数关联非负。输入的 order-polytope 网格是合法子格；取均匀权再作 Riemann 极限，正是经典 FKG 应用。该定理本身没有陈述 run 的 C1/C3，关键专用化是第 2 节的删除事件。Shepp 已明确完成了对应排列单调性定理。

### 6.2 Stanley 1986：均匀 order polytope 与均匀扩张的桥

Richard P. Stanley, *Two Poset Polytopes*, **Discrete & Computational Geometry 1 (1986), 9–23**，DOI [10.1007/BF02187680](https://doi.org/10.1007/BF02187680)。核对[作者网站原刊扫描](https://math.mit.edu/~rstan/pubs/pubfiles/66.pdf) **Corollary 4.2, p. 15** 与 **§5, p. 17, eq. (11)**。

order polytope 按线性扩张三角剖分，每个满维顺序单形体积 1/n!，总 volume=e(P)/n!。所以输入通过“均匀扩张＋独立均匀次序统计量”得到连续表示，是标准桥接。第 6 节另讨论单点 rank 的 Stanley log-concavity；它没有给出任意 ideal run 的这条有限 n 协方差界。

### 6.3 Chan–Pak 2025 survey：版本与错误泛化警示，非新的证明来源

Swee Hong Chan and Igor Pak, *Linear extensions of finite posets*。读取[作者稿 LEsurvey11.pdf](https://www.math.ucla.edu/~pak/papers/LEsurvey11.pdf)，首页日期为 **2025-02-25**；arXiv [2311.02743v2](https://arxiv.org/abs/2311.02743v2) 修订于 **2025-02-26**。出版社已确认 **EMS Surveys in Mathematical Sciences, online first, 2025-03-17**，DOI [10.4171/EMSS/97](https://doi.org/10.4171/EMSS/97)。arXiv 页面仍写 “to appear”，不能据此误记为未发表。

其 **§8.7, Theorem 8.18** 指回 CP2024 Thm1.8；**§9.9–9.10** 及脚注记录：把单点 rank 的概率质量 log-concavity 无条件推广到任意集合 minima 是错误的；旧的统一 second-moment 4/3 猜想也已被两不交链例否定。本报告只把它用于版本/边界核对，主定理仍引用原论文。

## 7. “标准矩界已经够了吗”的准确回答

### 7.1 普通 log-concavity 或 tail log-concavity 不足以单独给 C3b

这是一个抽象分布控制，**不是偏序反例**。取 n=4，在 {0,1,2,3} 上令

`Pr(Z=j)=2^(3−j)/15`。

它的质量序列 log-concave（实际上是几何列），尾序列也 log-concave，但

`EZ=11/15`，`Var Z=194/225`，

`(4−EZ)EZ(EZ+1)/(4+EZ+2)=14014/22725 <194/225`。

故“有界支持＋普通 LC”不能自动代替有限 n 修正；需要本题实际偏序结构带来的额外条件。这个检查也避免把来源中的 generic log-concave 二阶矩上界误读为我们的有限 n 结论。

### 7.2 常见支持界/Cauchy–Schwarz 不是一个遗漏的统一更强替代

只用 0≤X,Y≤n，逐点 XY≤nX 及 XY≤nY 给

`Cov(X,Y)≤min{r(n−s),s(n−r)}`。

输入 C3 的相应右侧多乘 `(r+1)/(n+r+2)<1`，因而更强。由输入 C3b 配 Cauchy–Schwarz所得平方根界，也被输入两侧 C3 最小值支配：令

`B₁=(n−s)r(r+1)/(n+r+2)`，

`B₂=(n−r)s(s+1)/(n+s+2)`，

则 `B₁B₂=V(r)V(s)`，其中 V(t)=(n−t)t(t+1)/(n+t+2)，所以 `min(B₁,B₂)≤sqrt(V(r)V(s))`。

这并不排除利用更细结构信息、实际二阶矩或支持端点的其他不相容强化；输入本身 C1 就保留了实际 M，可能比只用 r 的 C3 更细。

## 8. 建议用于正式文本的定位措辞

> 利用 Shepp 的偏序单调性定理（1980, Theorem 2），对 ideal 删除引入一个独立 marker，可得归一化首次外点秩的均值比较。对精确 prefix 条件化后作尾和，并以同变量情形闭合二阶矩，得到以下有限 n 的 ideal-run 协方差界。它细化了 Chan–Pak 的 rank-minimum 相关不等式在 0 起点变量下给出的二阶矩控制。我们不就该推论的历史优先性作断言。

不建议写：“删除比较是新机制”“FKG 不能处理一般 ideal”“Chan–Pak Thm1.8 本身就是一般 slot T”或“未搜索到所以是新定理”。

## 9. 交付边界与可复核材料

- 文献内容只聚焦上述 **五项**；没有泛扫原全局猜想文献。
- 明确核对了原文定理条件、0/1 起点、加 marker 后的 n+1 与 n−i+1，以及作者稿/发表状态差别。
- 保存的 PDF/text 只供本地复核；对外同步请只取本报告的论证和公开来源链接，不必复制来源全文。
- 本轮既没有证明，也没有反驳原全局猜想；没有改变其 OPEN 状态。

最终状态：本轮定向定位报告已锁稿。上列负超几何矩代入已另作小参数精确算术检查（n≤10），仅用于公式抄录核对，不替代解析推导；未作新增偏序搜索。
