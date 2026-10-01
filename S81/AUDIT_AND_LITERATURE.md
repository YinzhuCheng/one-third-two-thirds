# S81审查责任、文献读取层次与技术路线

日期2026-10-01。目标是数学审查与S78–S81接续，不是给全部历史加认证标签。

## 1. 本次真正检查的接口

- S78-POWER：辅助g不必是归一化生存函数；Stieltjes端点、两零矩、−+−交叉、初段非减与d≥1、全部止损比较，而非仅整数矩。
- S79：N=n+1、q=r+1、d=N−q；W≤cx(μ/q)Beta(q,d)与指数总长独立乘法；T|Z~Gamma(Z,1)；D=VarG−VarT而非VarG−VarZ。固定q、有界均值的TV逆向需要共同指数矩。
- S80：Laguerre有限多项式比较与C_j常数；相邻重排改变局部槽位、原像≤s!；半径二窗口用真实局部边缘；联合Gamma核只条件独立，且可数误差和与原级数收敛条件分开。
- S53：按原eσ/E混合、稳定排序、图边界缺失词和TV展开。未重审另引Wilson谱隙全部规范化。
- U58：复算末端有理式和S80全局极值选点的自含论证。没有重新逐行完成全部ACPP/BFT原始输入、Haqi全文、S57几何至G<2^25及S58整段优化。因此仍不认证一般纪录。

这些选定部分未发现内部致命错误。S81新稿是从核对后的接口推导，尚未外部审查。没有宣称“未发现错误”等于所有手稿已获证明。

## 2. 明确排除的推理捷径

1. T近Gamma的中心极限不直接给Z同样方差：E(T−Z)²=μ，在sqrt(q)尺度不消失。应撤销噪声，留下θ(θ−1)。
2. 固定局部块的NB极限不能套到占整个链固定比例的块；真实方差有1−α修正。
3. 离散分布对连续正态的TV始终为1；本轮使用W₂，不声称TV收敛。
4. 指定阈值的新正余量属于G/Z比较，不代表G/T缺陷曲线已由面积D/2逐点控制。
5. E j_Z(t)>0不是统一平衡度改进，也不能省略候选兼容和有限端部。Fibonacci无限律仍满足它。
6. U58末端小数与分数正确，不等于全部全局作用域正确。

## 3. 当前一手文献位置

### ACPP26：2609.30888，2026-09-25

Aires–Chan–Pak–Panova，Breaking the Infinite Barrier in the 1/3–2/3 Conjecture。一手摘要与作者论文目录再次确认一般BFT常数之上的统一ε改进。S80曾读到检索返回的一手正文片段，见[S80记录](../S80/ACPP_SOURCE_RECHECK.md)；S81直接HTML/abs/PDF尝试仍失败，不能说本轮重审全文，也不能抹去先前记录。这里不复制外部论文。

作者目录：https://sites.math.rutgers.edu/~sc2518/papers.html
预印本：https://arxiv.org/abs/2609.30888

项目U58若成立是另一项显式优化，但未获本轮完整认证，更不登记已确认纪录。ACPP的有限全局选点不能从局部窗口改进中省略。

### Aires26与Aires–Kahn25：大宽度/大不可比度

Aires，Proof of the Kahn Saks Conjecture，2609.30895，2026-09-25，一手摘要陈述大宽度迫使δ→1/2；本轮不重新审全文。
Aires–Kahn，Variance vs. range...，2510.26134v1，2025-10-30，HTML相关定理正文可读。Theorem1.6固定宽度大π给全局近半，Theorem1.7结合KS主结论推广至一般大π。

https://arxiv.org/abs/2609.30895
https://arxiv.org/html/2510.26134v1

采用上述文献后有界局部复杂度仍是重要核心，但有界π不等于有界总点数。固定模板膨胀的全局定性极限不重新登记原创。S75/S76留下的不同输出是定位与有效常数。

### 窗口与经典概率接口

Aires–Kahn，Balancing extensions in posets of large width，2509.11549v1，相关HTML窗口/order-polytope框架可读：https://arxiv.org/html/2509.11549v1 。它是技术背景，不是本轮新定理的全部前提。

Leskelä–Vihola，Conditional convex orders and measurable martingale couplings，Bernoulli23(4A),2017；作者机构页可读，明确Strassen与条件核背景：https://math.aalto.fi/~lleskela/paper018.html 。本轮不把联合核乘积当原创概率定理。

NIST DLMF8.4的整数不完全Gamma/Poisson有限和、18.12的Laguerre生成函数可读：https://dlmf.nist.gov/8.4 ，https://dlmf.nist.gov/18.12 。Gamma/Beta-binomial中心极限与有限总体修正是经典基础；S81输出是自治窗口缺陷的准确判别及指定阈值应用，未完成其等价表述的优先权调查。

## 4. 下一步应保留的图

    有限无1/3对反设
      -> 有限全局极值锚点 / 端部约束
      -- 未证 --> 特定阈值联合预算或可用的小排序缺陷ρ
      -> S53整份局部律稳定性
      -> 同一个实际标签对。

S78–S81提供不同窗口信息，但第一条虚线未完成。S81高斯判别需要D/q→0，没有证明潜在反例产生这种块；S81阈值余量可传入无限Fibonacci障碍，不能承担有限性的最后一步。

## 5. 同步责任

GitHub发布S78–S80关键数学稿的明确整理版，不反向改写此前R/S报告来隐藏过程。完整原始上传内容与原脚本在S81合并ZIP的originals/中。旧证据不被标为本轮新运行。当前研究、下一断点、网站进展入口更新到S81，主问题仍开放；仅以实际提交和HTTP读取确认同步，不以生成本地文件代替发布。
