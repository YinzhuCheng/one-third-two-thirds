# 2026-10-19 外部仓库稿：固定来源与本轮复核

这些是协作研究备注，不是发表、同行评审或优先权认定。作者仓库中同名“Independent audit”仍由同一仓库作者提交，不能仅据标题视作外部审稿。下面分开列来源主张与本项目本轮复核；未执行作者代码，未转载原文全文。

## 1. rooted-five 的真实外边界平衡定理

[固定原文 b4b4ccbc](https://github.com/eliottcassidy2000/math/blob/b4b4ccbc0ff5da92ec1156b9eff821d85960a697/05-knowledge/results/rooted_five_logconcave_balance_20261019.md)。

精确假设：有限P中x∥y，I(x)∪I(y)恰为{b,x,z,y,a}，诱导关系恰由b<z<a、x<a、b<y生成，I表示偏序不可比邻域。结论：真实全局均匀扩张律下，(x,y)、(x,z)、(z,y)至少一对平衡；不要求width、最大不可比度或外点数上界。

本轮另行逐步审查了marker插入双射、Stanley rank-LC、ideal初始run的尾次乘性与矩界、真实两侧均匀平均、11核心词乘积计数及严格端点代数，没有发现证明缺口；独立小计数控制核对了11词与81组参数。无限结论依据证明而不是有限控制。Stanley输入见[1981原文](https://math.mit.edu/~rstan/pubs/pubfiles/48.pdf)，印刷页62–63，Theorem 3.1及k=1特例。

有用护栏：实际边界矩满足1≤c≤u≤c²、1≤d≤v≤d²。旧抽象正混合d=19/7、v=59/7违反v≤d²，差52/49，不能冒充本类actual偏序边界律；必要矩条件也未被证明足以刻画全部实际边界律。结论不能外推为一般五点核心、七薄残余或全局1/3–2/3猜想。

## 2. Gold 两问不能总局限于指定五核心端点

[固定原文 d73da7a7](https://github.com/eliottcassidy2000/math/blob/d73da7a75ecf6ee01b45a3510aa535986ab3fffe/05-knowledge/results/rooted_five_core_gold_obstruction_20261019.md)。

八点实际P由b<z<a、x<a、b<y以及t1<t2<t3、每个ti<x,y,a生成。真实扩张数E=53、width=3、最大不可比度5。核心内即使第二问可依第一问自适应，最佳首问x:z的重分支有34条，最佳二问仍留20条，34+20=54>53。允许外点策略先比较b:t2、再z:t3，四格为[[19,3],[16,15]]，所有路径余量至少6。

本轮用自写8!整数枚举核验；另一次分开实现得到相同结果。随附[项目自写控制](check_rooted_five_obstruction.py)和[保存的精确回执](rooted_five_obstruction_receipt.json)。同步阶段没有重跑该枚举。

准确否定对象是“Gold自适应两问的端点总能限制在该指定五核心内”。它不是Gold或MAIN33/WIDTH3的反例：外点策略成功，核心x:z=19/53、x:y=35/53本身也都平衡。后续若研究Gold局部化，须允许外部端点或加入能排除此例的实质假设；现有模块替换/局部对偶定理不依赖该局部化假设。
