# 任意 t 自治链严格交错与精确插入运输：2026-10-19 接续

两份完整新增主稿通过共同最终全文独立解析审查；严格性承重步骤另经第二份独立专审。概率底座始终是实际有限偏序的均匀有标签完整线性扩张。原 1/3–2/3 猜想仍 OPEN，35/55 台账不变。

## 1. 一般严格交错及其出处定位

[完整证明](general-chain-interlacing-20261019/RESULT.md) · [共同全文终审](review-general-insertion-20261019/REVIEW.md) · [strict 专审](review-strict-interlacing-20261019/REVIEW.md)

固定任意有限外偏序 R=D⊔I⊔U，加入自治链 D<C_m<U，所有 x∈I 与整条链不可比。允许 I 内部任意、D/U 为空，且 t=|I| 任意。对每个 m≥1、1≤i≤m、x∈I，有

    Q_{i,x}(m+1)>Q_{i,x}(m)>Q_{i+1,x}(m+1)，
    Q_{i,x}(m)=Pr(c_i<x)。

证明在指定 c_i 后插入新点，删除后的旧连续坐标边缘按真实 gap 长度倾斜。以 c_i 为锚的 Shepp 差坐标格给非负关联；真实归一化的两层切片 FKG、LE 极端 rank 的幂次和跨切片全协方差给严格性。最后对整个偏序取对偶得到右不等式。既没有假定删除投影均匀，也没有仅凭两个函数非恒定就宣称 strict FKG。

这是经典 Shepp 锚定差坐标 FKG 工具的应用推导，不主张首创。文献报告已核 Brightwell–Trotter 对该机制的完整重建，并准确归于 Shepp 1982；未逐页核 Shepp 1982 原刊 PDF，获取限制如实保留。报告落稿时只主张弱交错，最终严格性由本轮主稿与两份解析审查承担。[定向文献比对及来源](chain-interlacing-literature-20261019/RESULT.md)。

## 2. 交错能保持什么，不能保持什么

对1≤k<m、1≤i≤k，重复交错给

    Q_i(m)>Q_i(k)>Q_{i+m−k}(m)。

因此旧整列若全部在低侧 Q_1(m)<1/3，或全部在高侧 Q_m(m)>2/3，则任意更短正整数长度仍保持同一侧，并严格改善该列最坏稀有概率。

但“旧整列避开闭带”一般不等于“旧列同侧”。实际解析反控 C₂⊔C₅ 中，选 C₅ 中点，旧列是5/7、2/7，缩至C₁后为1/2。它与严格交错一致，只否定无附加条件的列缩短断言；不是全偏序无平衡或原猜想反例。[独立的全部6/21条LE计数](review-general-insertion-20261019/independent_crossed_column.json)。

一般相邻列跳幅至多 t/(m+t)。故 m≥2t 时，任何避开闭带 [1/3,2/3] 的旧列必同侧，从而可任意缩短。m≥2t 只是统一充分条件，未称最优；t=2 已有更强专用结论。这些全是链–外点列性质，完全外部 pair、共同安全落点和总体 δ 普适安全仍未推出。

## 3. 精确插入运输与有限同时证书

[完整运输主稿](insertion-transport-criteria-20261019/RESULT.md) · [独立固定实际微核源码](review-general-insertion-20261019/independent_transport_check.py) · [18条精确记录](review-general-insertion-20261019/independent_transport_check.json)

固定外部LE的中央窗口长为K，其链插入纤维有 binom(m+K,K) 个完整LE。全槽插入和均匀随机链秩删除按 m+K+1 倾斜；固定删链秩还会在同一外部词纤维内按该gap槽数再次倾斜。

令J为x前链点数，R为扩展窗口秩，窗左取0、窗右取K+1。在旧实际均匀律下，设γ=Cov(K,1{J≥i})，B=E[(i−1+R)1{J=i−1}]，C=E[(m+K+1−i−R)1{J=i}]。两条交错差分别为 (γ+B)/(m+1+EK)、(C−γ)/(m+1+EK)，故双边交错当且仅当 −B≤γ≤C；严格号也精确对应。

结合第1节一般定理，全部实际输入自动满足严格预算 −B<γ<C。这不表示更强的共同绝对预算 η=E|K−EK|/2 总能成功，也不表示全部实际双变量行列式F/G的单项式或双Newton系数总非负。后两项仍是独立可检查的充分证书，F/G次数至多2t−1。

主稿给 I 与 D∪U 完全无关系、I内部任意的真实结构类的正因子系数锥证明；另给全支持共同外权模型的解析失败。人工权重失败不能写成真实均匀偏序反例。

## 4. 冻结实验只作有限支持

[冻结范围与方法](general-interlacing-tests-20261019/RESULT.md) · [预算](general-interlacing-tests-20261019/BUDGET.md) · [控制摘要](general-interlacing-tests-20261019/summary.json) · [最小gap证书](general-interlacing-tests-20261019/minimum_gap_certificate.json) · [独立计数核对](general-interlacing-tests-20261019/minimum_gap_independent_check.json)

冻结的28个多门结构族给336个字面有标签外偏序，在预定长度和t∈{3,4,5,6}上没有失败。已执行的100个小对照是84个tiny加16个clone重数对照；另有最小gap的5个独立计数检查，不能说成105个结构。该实验未被本轮同步者或共同审稿者重跑。一般定理由完整证明承担，有限实验不能替代它。

包内保留生成和验证程序、控制摘要及指定证书，大型全部计数表不重复上传。[发布范围与完整本地再生成来源](PUBLICATION_SCOPE_GENERAL_INTERLACING.md)。

## 5. 接续与未解范围

[固定继承输入](INHERITED_INPUTS_GENERAL_INTERLACING.md)给此前已公开版本的精确定位。旧 START_HERE 与旧稿保留历史，当前结论以前述两份新稿和终审为准。一般t交错由本轮证明闭合；一般全外部pair保持、全局共同安全缩短、系数锥自动成功及原全局猜想仍未闭合。本轮没有扩大原台账、没有重跑实验，没有文献优先权或新全局排除主张。
