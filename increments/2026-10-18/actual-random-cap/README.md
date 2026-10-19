# 实际随机 cap 槽：小补充

日期：2026-10-18。状态：主证明 §§1–9 和合并推论已获最终逐稿独立审核 PASS。

## 新结果

对 U=W⊔V、B=V、A=V∪S，其中 S 为 W 的上理想、V 非空，两块之间无可比关系，实际槽满足 R=min(J,K)、T=J。K 可以真正随机；精确协方差恒等式结合实际 R 的 Chan–Pak 对角界得到 T 和 C。

合并旧定理后：两个非空嵌套 filters 中任意一个是与补集无可比关系的独立块，T 和 C 均成立。较大 filter 不等于 U 时严格；等于 U 时取等号。两块内部关系任意。

这是对前包抽象随机 cap 障碍的实际结构回应。前包抽象反例仍有效；任意抽象独立 cap 不享有本定理。原 1/3–2/3 猜想、一般辅助槽界及全外部 pair 问题仍未解决。35/55 台账不变。前包覆盖表中的数值是其固定截点，本补充不重算或刷新该表。

## 内容

- PROOF.md：本轮逐稿通过的完整证明、边界、旧抽象障碍说明及合并推论。
- SUPPORTING_LEMMA.md：合并推论所需的旧已审独立补块定理 §§1–3，含自含 shuffle/gap 矩证明；不需旧包即可读懂两个分支。
- verify_fixed_cases.py / verification.json：5 个固定实际例和2个固定抽象控制的精确分数核验。
- audit/REVIEW.md：最终逐稿独立审核，含对合并推论的检查。
- audit/verify.py / audit/verification.json：独立固定控制和精确结果。

只含证明、审稿及必要 fixed exact 控制。未包含缓存、扫描历史、原始聊天、旧28文件包或大实验。未执行 GitHub 写入。

## 复核

Python 3 标准库即可运行：

python3 verify_fixed_cases.py
python3 audit/verify.py

两个脚本只枚举事先固定的少量小偏序或既有抽象控制，无随机或参数空间搜索。脚本重写各自 verification.json。有限核验用于回核指定数据，不替代通式证明。

## 来源与衔接

- Chan–Pak, Correlation inequalities for linear extensions, Theorem 1.8 (1.16)：https://arxiv.org/html/2211.16637v2
- 前包 Notion「槽机制与缩链：一般结构定理」：https://app.notion.com/p/3fd05a5b7caa8190ae0ccd508e7e7d9d?pvs=204
- 本补充 Notion 链接见 NOTION_URL.txt。
