# 1/3–2/3 猜想：完整交接入口（至 S68）

日期：2026-09-30。本包覆盖 R1–R65、S1–S68，共 **133 份规范轮次报告**。主猜想、全部宽度三仍未证明；项目中的一般界和结构定理均须按各自证据等级阅读，不是已获独立审稿或形式化认证的结论。

## 新会话只需先读这些

1. 本页及 `01_PROBLEM_AND_STATUS.md`：定义、最新结果和证据责任。
2. `02_RESEARCH_ATLAS.md`、`03_DEPENDENCIES.md`：路线及依赖；不要开始就载入全部历史。
3. `05_PRIORITIES_AND_CONJECTURES.md` 和 `09_NEXT_SESSION.md`：已排除版本、当前断点、可执行目标。
4. 继续本轮才读 `S68/REPORT.md`、`S68/notes/PROOF.md`，再按需取源程序和证书。

`04_FALSE_ROUTES_AND_GUARDS.md` 是提出新加强式前的必查表；`06_LITERATURE_AND_THEOREM_MAP.md` 区分经典定理、新预印本、项目推导及文献归属。

## 本轮新增的三个接口

- **S68-GAP（无限类，解析归约＋完整有限核验）**：十点种子中，四个链外点的任一可比对 `(u,w),(u,z),(v,w),(v,z)` 各自膨胀为任意正长度链，其余八点不变。非原种子时 `δ≥898/1997`，且14点对象达到等号。有限域28,684个模型，两套计数的21,789,616项比较流逐字节相同。
- **S68-FIRST（一般组合恒等式）**：任意模板所有顶点同时作链替换，用首次出现顺序与活跃理想极大元表达成非负有理生成核。不是任意十参数的平衡证明。
- **S68-RUN（一般组合恒等式）**：可变模板点形成链时，骨架事件计数在二项式基 `∏ binom(m_i−1,α_i)` 中有非负整数系数，总阶不超过固定外点数。多项式性的已有文献归 Bergman；本轮提取可核验的事件接口，未完成首创性调查。

原十点种子的十参数 **1/3 定性结论已经是 very-good-pair 定理的推论**；十参数非平凡膨胀的 **2/5** 仍未证明。不能把二者混同。

## 完整档案在哪里

- `archive/S67_original.zip`：原累计包原字节保存，包含 **1,583 个旧文件**，未解压体积约185.6MB；所有旧程序、证据、过程和旧入口仍在其中。
- `reports/`：133份规范报告的扁平副本，方便检索；不是删减版。旧报告的相对链接需回到原目录，见下列工具。
- `legacy_registries/through_S48_unified_records.json`：703条既有记录及其历史状态，原样保存。
- `legacy_guides/`：S48的大型路线图、定理图谱和停止规则，补充本次跨阶段综述。
- `S68/`：本轮自含证明、代码、完整压缩计数流与验证记录。
- `registry/rounds.json`、`registry/dependencies_S68.json`：报告映射和有类型的依赖图。
- `literature/`：历史参考文献总表、BibTeX、各轮来源账本及本次核对清单。

**历史恢复限制继续保留**：S62累计包曾损坏，S63已用完好的S61累计包与S62独立包恢复。此包保留原恢复说明，不声称补回未知的丢失顶层元数据，也不声称补回从未写入档案的对话或私有思考。

## 只取需要的旧材料

```sh
python tools/history.py find 'S65/'
python tools/history.py round S65
python tools/history.py read '<find返回的精确path>'
python tools/history.py extract '<旧目录path>/' --to /tmp/poset_S65
```

`extract` 去掉所选前缀后保存文件，并逐项检查SHA-256；不要解压一切再把一切读进上下文。完整复现说明见 `07_CODE_AND_EVIDENCE.md`。

## 检查

```sh
python tools/verify_handoff.py
python tools/verify_handoff.py --math
```

第二条重算本轮有限数学，不是自动认证一般证明或全部历史结果。顶层清单验证文件字节；原档逐项检查不等于数学审查。
