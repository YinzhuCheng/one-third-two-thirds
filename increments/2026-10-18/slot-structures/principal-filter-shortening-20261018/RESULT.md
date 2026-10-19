# principal 槽矩接回 t=2 反链自治链：严格端点与列缩短保持

日期：2026-10-18。

## 0. 结论先行与准确范围

设固定有限外部偏序为

\[
R=D\sqcup\{y,z\}\sqcup U,\qquad y\parallel z,
\]

所有 D 点都小于所有 U 点，不存在 \(\{y,z\}<D\) 或 \(U<\{y,z\}\) 的关系。对每个整数 \(m\ge1\)，加入自治链

\[
C_m=(c_1<\cdots<c_m),\qquad D<C_m<U,
\]

且 y、z 均与整条链不可比，得到实际偏序 \(P_m\)。D、U 内部任意，允许为空。各概率一律取 \(P_m\) 的全部实际线性扩张上的均匀分布。

**已证一般结构子类。** 对 i=y,z，令

\[
A_i=\{d\in D:d<i\},\qquad B_i=\{u\in U:i<u\}.
\]

\(A_i\) 是 D 的下理想，在 \(D^{\rm op}\) 中是上理想；\(B_i\) 是 U 的上理想。在 \(D^{\rm op}\) 和 U 两侧，分别对这对上理想采用以下充分条件：

1. 至少一个上理想为空；或
2. 至少一个槽均值为 0；或
3. 一个达到**较小槽均值**的非空上理想是 principal。均值相等时，任意一侧 principal 即可。

若上下两侧各满足此条件，则对 i=y,z 以及所有 \(m\ge1\)，同时严格有

\[
\Pr_{P_{m+1}}(c_1<i)>\Pr_{P_m}(c_1<i),\qquad
\Pr_{P_{m+1}}(c_{m+1}<i)<\Pr_{P_m}(c_m<i).\tag{E}
\]

这里上下两侧较小均值的标签可以不同。所有条件只依赖固定 D、U 和邻域，**不随 m 改变**。

一个不需要比较均值的纯结构版本是：**四个邻域 \(A_y,A_z,B_y,B_z\) 各自为空或 principal**。在 D 中 principal 指有唯一最大元，在 U 中指有唯一最小元；不要求 D/U 自身是链，也不要求对应点互不可比。

**真实列保持推论。** 对任意 \(m\ge2\)，若某个旧列 \(C_m\times\{i\}\) 的全部概率都避开闭区间 \([1/3,2/3]\)，则将链缩至任意 \(1\le k<m\) 后，该列仍全部避开该闭区间，且保留同一稀有方向。两个旧列均无平衡对时，\(C_k\times\{y,z\}\) 均无平衡对。本结论只涉及含链点的两列；**不推出完全外部配对保持，不推出全偏序的 \(\delta\) 非增，也不作原猜想的全局分类。**

下面独立核对计数、公式、边界和列同侧步骤。

## 1. 槽变量：左右方向与 principal 的准确含义

取独立均匀的

\[
\alpha\in\operatorname{LE}(D),\qquad \beta\in\operatorname{LE}(U),
\qquad h=e(D)e(U)>0,
\]

约定 \(e(\varnothing)=1\)。这只是计算实际插入数的辅助乘积空间，不是把 \(P_m\) 或 R 上遗忘插入点后的分布误当成均匀分布。

设 \(d=|D|,n=|U|\)。中央 D/U 边界槽另计 1。对 i=y,z，定义中央槽左侧、右侧的合法旧槽数

\[
\ell_i(\alpha)=d-\max_{a\in A_i}\operatorname{rank}_\alpha(a),
\quad \max\varnothing:=0,
\]
\[
\rho_i(\beta)=\min_{b\in B_i}\operatorname{rank}_\beta(b)-1,
\quad B_i=\varnothing\text{ 时 }\rho_i:=n.
\]

反转 \(\alpha\) 是 \(D^{\rm op}\) 上的均匀线性扩张，且

\[
\ell_i=\min\operatorname{rank}_{\alpha^{\rm rev}}(A_i)-1
\]

（空集合仍取 d）。因此左侧也恰好是已审上理想槽模型，不能误把 D 中的上邻域或 \(d-1-\max\operatorname{rank}\) 接入。

置

\[
p=\mathbb E\ell_y,\quad r=\mathbb E\ell_z,
\qquad q=\mathbb E\rho_y,\quad s=\mathbb E\rho_z,
\]
\[
M=\mathbb E[\ell_y\ell_z+\min(\ell_y,\ell_z)],
\quad N=\mathbb E[\rho_y\rho_z+\min(\rho_y,\rho_z)].\tag{1}
\]

所有量非负。若 \(A_i\ne\varnothing\)，其在 \(D^{\rm op}\) 中 principal 等价于存在 \(a_i\in D\) 使

\[
A_i=\downarrow_D a_i;
\]

即 i 在 D 中的全部前驱有唯一最大元。若 \(B_i\ne\varnothing\)，principal 等价于存在 \(b_i\in U\) 使

\[
B_i=\uparrow_U b_i;
\]

即 i 在 U 中的全部后继有唯一最小元。这里说的是完整邻域，不是任选一个前驱/后继，也不是只检查某个表示中的生成元数量。

## 2. 已审槽界与空集合的补齐

### 2.1 准确使用已审 principal 定理

已独审 PASS 的结果是：任意有限非空 V 中，若一个非空上理想 S 为 principal，另一非空上理想 T 任意，槽均值分别为 a,b，则

\[
\mathbb E[XY+\min(X,Y)]-ab\le a^2+2a.\tag{P1}
\]

若两个上理想都 principal，可交换两者，得到

\[
\mathbb E[XY+\min(X,Y)]
\le ab+\min(a^2+2a,b^2+2b).\tag{T}
\]

更一般地，只要达到较小均值的一侧 principal，单侧式 (P1) 已经给出 (T)。这一步不把较大均值 principal 的单侧式偷换成另一侧的式子。

### 2.2 空 filter 不是 principal，但目标界直接成立

若 V 有 n 点，S 为空，则 X=n 确定，而 \(0\le Y\le n\)，令 \(b=\mathbb EY\)。于是

\[
\mathbb E[XY+\min(X,Y)]-nb=b.
\]

因为 \(b\le n\)，较小均值是 b，而

\[
b\le b^2+2b,
\]

故 (T) 直接成立，无须把空集称为 principal，也无须调用非空 V 的定理。两者都空以及 n=0 均包括在内。

若某个槽均值为 0，则相应非负槽变量恒为 0，混合槽矩也为 0，(T) 同样直接成立。对上理想槽，非空 V 上的零均值实际上等价于该上理想为整个 V，但不需要这个等价性来使用结论。

因此，第 0 节每侧的充分条件确实分别给出

\[
\boxed{M\le pr+\min(p^2+2p,r^2+2r)},\qquad
\boxed{N\le qs+\min(q^2+2q,s^2+2s)}.\tag{2}
\]

D 为空时 \(p=r=M=0\)，U 为空时 \(q=s=N=0\)。空的一侧自动满足 (2)，只需检查另一侧。D、U 同时为空时两侧都自动满足。

### 2.3 无条件的下界也核对了边界

需要的弱下界为

\[
M\ge pr-1,\qquad N\ge qs-1.\tag{3}
\]

它们不要求 principal。可用与已审证明相同的有限格 FKG 机制作一次直接核查：在 V 的均匀 order polytope 上令 \(Z_S=\min_{v\in S}X_v\)，空 S 取 \(Z_S=1\)。两个函数均逐坐标递增，合法域对 min/max 封闭，故 \(\operatorname{Cov}(Z_S,Z_T)\ge0\)。设槽变量为 X,Y、均值为 a,b、混合槽矩为 K，次序统计量的精确转换（空集使用第 \(n+1\) 个哨兵统计量 1）给出

\[
\mathbb EZ_S=\frac{a+1}{n+1},\qquad
\mathbb E Z_SZ_T=\frac{K+a+b+2}{(n+1)(n+2)}.
\]

所以实际还有

\[
K\ge ab-1+\frac{(a+1)(b+1)}{n+1}\ge ab-1.\tag{4}
\]

n=0 时两槽均为 0，式 (4) 正好为等式 0。下文只使用较弱的 (3)，不依靠未证的最小子集秩对数凹性。

## 3. 七类实际计数与端点核：反链情形逐项接回

固定基词 \(\alpha\beta\)。两个可区分外部点在同一侧槽中插入时，带标签的总数为

\[
\ell_y\ell_z+\min(\ell_y,\ell_z)
\quad\text{或}\quad
\rho_y\rho_z+\min(\rho_y,\rho_z).
\]

这里的 min 是同槽时第二种标签顺序的额外计数。按既有窗口七类记号，直接计数并对辅助基词求和得到

\[
\frac{A_0}{h}=M+ps,\quad \frac{B_0}{h}=N+qr,
\quad \frac{A_1}{h}=p,\quad \frac{B_1}{h}=q,
\quad \frac Hh=r+s,
\quad \frac Lh=\frac{R_2}h=1.\tag{5}
\]

这些是实际外部线性扩张数；特别地 \(L=R_2=h\) 不是自由系数假设。

置

\[
a=A_0+B_0,\quad b=A_1+B_1+H,\quad c=L+R_2=2h,
\]
\[
u=A_0+H+R_2,\quad v=A_1+L,
\qquad w=B_0+H+L,\quad x=B_1+R_2.
\]

则

\[
T_m=e(P_m)=a+b(m+1)+c\binom{m+2}{2},\tag{6}
\]
\[
Q_y^{\rm first}(m)=1-\frac{u+v(m+1)}{T_m},\qquad
Q_y^{\rm last}(m)=\frac{w+x(m+1)}{T_m}.\tag{7}
\]

归一化后，令 \(t_m=T_m/h\)，有

\[
t_m=M+N+ps+qr+(p+q+r+s)(m+1)+(m+1)(m+2),\tag{8}
\]
\[
\frac uh=M+ps+r+s+1,\quad \frac vh=p+1,
\quad \frac wh=N+qr+r+s+1,\quad \frac xh=q+1.\tag{9}
\]

独立交叉相乘得到

\[
\mathcal D_m(a_0,b_0)=cb_0\binom{m+2}{2}+ca_0(m+2)+ba_0-ab_0,
\]
\[
Q_y^{\rm first}(m+1)-Q_y^{\rm first}(m)
=\frac{\mathcal D_m(u,v)}{T_mT_{m+1}},
\]
\[
Q_y^{\rm last}(m+1)-Q_y^{\rm last}(m)
=-\frac{\mathcal D_m(w,x)}{T_mT_{m+1}}.\tag{10}
\]

并且

\[
\mathcal D_{m+1}(a_0,b_0)-\mathcal D_m(a_0,b_0)
=c[b_0(m+2)+a_0].\tag{11}
\]

本处 \(c>0,v>0,x>0\)，所以两条实际差核都严格递增。因此只需检查 \(m=1\to2\)：

\[
J_y^{\rm first}=u(b+3c)+v(3c-a)>0,
\qquad J_y^{\rm last}=w(b+3c)+x(3c-a)>0.\tag{12}
\]

## 4. 四条严格端点式；均值较小侧到底何时需要

### 4.1 y 列首端

将 (9) 代入，令 \(F_y=J_y^{\rm first}/h^2\)，准确得到

\[
F_y=(M+ps+r+s+1)(p+q+r+s+6)
 +(p+1)(6-M-N-ps-qr).
\]

不是只有一个下界，而是有精确分解

\[
\boxed{
F_y=(p+1)[(r+s)^2+qs+6(r+s)+7-N]
 +(M-pr+1)(q+r+s+5).
}\tag{13}
\]

使用 (3) 和 \(N\le qs+s^2+2s\)，立即得

\[
F_y\ge(p+1)[r^2+2rs+6r+4s+7]>0.\tag{14}
\]

正项常数 7 保证了所有零均值/空侧边界仍为严格。

### 4.2 另外三条：标签交换与全对偶均明确保留

交换 y、z 将 \((p,r,q,s)\) 变为 \((r,p,s,q)\)，M、N 不变。故 \(N\le qs+q^2+2q\) 给出

\[
\frac{J_z^{\rm first}}{h^2}
\ge(r+1)[p^2+2pq+6p+4q+7]>0.\tag{15}
\]

全偏序取对偶、链反向，则 \(D^{\prime}=U^{\rm op}\)、\(U^{\prime}=D^{\rm op}\)，且

\[
(p^{\prime},r^{\prime},q^{\prime},s^{\prime})=(q,s,p,r),
\qquad (M^{\prime},N^{\prime})=(N,M).
\]

对偶首端式就是原末端式，归一化的 \(J\) 一致。因此分别使用
\(M\le pr+r^2+2r\)、\(M\le pr+p^2+2p\)，得到

\[
\frac{J_y^{\rm last}}{h^2}
\ge(q+1)[s^2+2sr+6s+4r+7]>0,\tag{16}
\]
\[
\frac{J_z^{\rm last}}{h^2}
\ge(s+1)[q^2+2qp+6q+4p+7]>0.\tag{17}
\]

(2) 同时提供这里需要的四个单侧上界；(10)–(12) 随即证明所有 \(m\ge1\) 的 (E)。没有把 m 固定后依赖 m 的充分条件误当成全链长条件。

### 4.3 必须区分“固定一列”与“同时两列”

- **固定 y 列首端**只需要 \(N\le qs+s^2+2s\)。所以 \(B_z\) 单独 principal、\(B_y\) 任意非空时，已审单侧定理就够，**不要求 s≤q**。若任一上邻域为空，则上一节直接边界论证也够。
- **固定 y 列末端**只需要 \(M\le pr+r^2+2r\)。所以 \(A_z\) 在 \(D^{\rm op}\) 中单独 principal、\(A_y\) 任意非空时也够，**不要求 r≤p**。
- z 列完全交换标签。因此若只知一个非空上邻域 principal，想用同一个已审槽估计**同时保证 y、z 两个首端**，较小均值侧 principal 是足够的选择；对两个末端，在下邻域的对偶上作同样选择。
- 若唯一已知 principal 的一侧均值较大，只能直接获得该主侧平方的单侧估计；不能把它宣称为 min 界。但这**不是**该结构的端点或 T 失败的证明，更不是必要条件的反向刻画。空集合、零均值和其他独立条件都可使结论成立。本文给的是一般充分条件，未声称必要。

尤其，仅当“要让一个 principal 的单侧证明统一给出两个方向的平方界”时才需要上述较小均值选择；不能笼统说“principal 必须位于较小均值侧”。

## 5. 从端点到真实完整列：反链的精确内部跳幅

端点单调本身只直接控制整列已在同一侧的情形。这里利用 \(y\parallel z\) 的实际 \(L=R_2\)，把“无平衡列必定同侧”的缺失步骤完整补上。

记

\[
Q_{i,y}(m)=\Pr_{P_m}(c_i<y),\qquad 1\le i\le m.
\]

令 J 为 y 之前的链点数，则

\[
Q_{i,y}(m)-Q_{i+1,y}(m)=\Pr(J=i).
\]

对内部 \(1\le i<m\)，七类中只有 H、L、\(R_2\) 有贡献：

- H 类中 y 在唯一外部窗点的位置，固定 J=i 的插入数为 1；
- L 类中 y 先于 z，固定 J=i 后有 \(m-i+1\) 种 z 位置；
- \(R_2\) 类中 z 先于 y，固定 J=i 后有 \(i+1\) 种 z 位置。

所以精确有

\[
Q_{i,y}(m)-Q_{i+1,y}(m)
=\frac{H+L(m-i+1)+R_2(i+1)}{T_m}
=\boxed{\frac{H+h(m+2)}{T_m}},\tag{18}
\]

与内部 i 无关。由各计数非负，

\[
T_m=a+(A_1+B_1+H)(m+1)+h(m+1)(m+2)
\ge(m+1)[H+h(m+2)],
\]

故

\[
0<Q_{i,y}(m)-Q_{i+1,y}(m)\le\frac1{m+1}\le\frac13
\quad(m\ge2).\tag{19}
\]

这一步甚至不需要 principal 条件。z 列同样成立。完整列的直接公式也可写成

\[
Q_{i,y}(m)=
\frac{N+qr+q(m+1)+(m-i+1)(r+s+m+2)}{t_m},\tag{20}
\]

其首末端与 (7) 一致。

若一列所有项都不在闭区间 \([1/3,2/3]\)，但不是整列低于 \(1/3\) 或整列高于 \(2/3\)，则由于该列递减，存在相邻两项一项 \(>2/3\)、下一项 \(<1/3\)，跳幅严格 \(>1/3\)，与 (19) 矛盾。故无平衡旧列确实同侧；阈值是闭区间这一点不能省略。

现在任取 \(1\le k<m\)。若旧列低侧，则

\[
Q_{i,y}(k)\le Q_{1,y}(k)<Q_{1,y}(m)<1/3.
\]

若旧列高侧，则

\[
Q_{i,y}(k)\ge Q_{k,y}(k)>Q_{m,y}(m)>2/3.
\]

严格不等式由 (E) 沿链长迭代给出。这证明第 0 节列保持推论，且无需额外的统一 margin。

进一步，若定义该列的最坏稀有概率

\[
b_y(m)=\max_i\min\{Q_{i,y}(m),1-Q_{i,y}(m)\},
\]

则在旧列无平衡的前提下，缩短后有 \(b_y(k)<b_y(m)<1/3\)。这只是列内的严格改善，不是对完全外部配对取最大值后的全局结论。

单侧条件也可以单独使用：仅上侧满足第 0 节条件就同时保持两个已经全低侧的列；仅下侧满足就同时保持两个已经全高侧的列。对未知处于哪一侧的无平衡列，使用上下两侧条件才统一足够。

## 6. 完全外部 pair 的边界：确实不在定理控制内

对外部事件 A，其概率准确为

\[
\Pr_{P_m}(A)=
\frac{\sum_{\sigma\in\operatorname{LE}(R)}
\mathbf1_A(\sigma)\binom{m+K(\sigma)}{K(\sigma)}}
{\sum_{\sigma\in\operatorname{LE}(R)}
\binom{m+K(\sigma)}{K(\sigma)}}.
\]

缩链会改变不同 K 窗口的相对权重。上面的四条端点式没有给出这个重加权对任意 A 的符号；列同侧步骤也不适用于完全外部 pair。

有一个无需枚举的实际边界例。取

\[
D=(d_1<d_2<d_3),\quad U=\varnothing,
\]

加入 y，令全部 D<y，而 y 与 \(C_m\) 不可比；z 为孤立点。仍有 \(y\parallel z\)、\(D<C_m\)。此时

\[
A_y=D=\downarrow d_3\text{ 为 principal},\quad A_z=\varnothing,
\quad B_y=B_z=\varnothing,
\]

故满足本文件的结构充分条件。去掉 z 后，每条扩张中 \(d_2\) 的秩恒为 2；z 独立均匀插入 \(m+5\) 个槽。因此完全外部 pair 满足

\[
\Pr_{P_m}(d_2<z)=1-\frac2{m+5}.
\]

从 \(m=2\) 缩到 1 时，该概率由 \(5/7>2/3\) 变成 \(2/3\)，进入闭平衡区间。此例仅说明**上述邻域条件本身不能保证每个外部 pair 的阈值保持**。事实上旧的 \(C_2\times\{y\}\) 列恰为 \((2/3,1/3)\)，已经包含闭区间平衡对。因此它不满足“旧两列均无平衡”的完整列保持前提，不是对第 5 节推论的反例，也不被用作任何全局反例。

## 7. 依赖、独立核查与停止边界

直接前置材料：

1. `/workspace/shared/principal-filter-slot-bound-20261018/RESULT.md`，§2–7 的已证 principal 和单侧槽矩定理；
2. `/workspace/shared/audit-principal-slot-20261018/REVIEW.md`，明确 PASS，并核准空集不在原定理本身范围内；
3. `/workspace/shared/two-neighbor-count-constraints-20261018/RESULT.md`，§6 的反链七类实际计数；
4. `/workspace/shared/two-neighbor-endpoint-kernel-20261018/RESULT.md`，端点核及全部 m 的单步归约。

本文件重新从插槽计数核对了 (5)、(18)、(20)，从交叉相乘核对了 (10)–(13)，明确写出了两个标签交换和全对偶的变量变换。附带的 `verify.py` 只作符号恒等式与一个直接边界例的精确分数核对；不枚举偏序，不重跑既有大规模搜索，不作有限证据到普遍命题的升级。

一般任意两个非 principal、非退化上理想的 T 不在本文被证明或否定。仅较大均值侧 principal 的非退化对子，也未在这里得到 min 界。结论限于指定结构子类的端点、含链点列和缩短；对完全外部 pair 的剩余控制问题保留。没有对外写入，没有修改旧材料，也没有继续原猜想的全局分类。
