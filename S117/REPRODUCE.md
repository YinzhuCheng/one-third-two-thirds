# S117 复现入口与生成文件

在 S117 目录执行以下命令。Python 3.10+ 标准库；C++步骤需要已有 g++ 与 GMP 开发库。程序无需联网，不自动安装任何依赖。以下是按需复现方法，出版同步没有重新执行这些完整数学运行，也不要求日常把两套实现全部重跑。

所有大记录可从本包源码重建；没有遗漏必须另行下载的大型输入。已有摘要记录的是已完成、独立 PASS 的研究运行。耗时字段随机器变化。

## 一、新补域：通常只需这一个入口

```sh
python full-seven-core-resolution/reproduce.py
```

它生成／更新 domain_intervals.txt、domain_summary.json、exact_counts.txt、independent_intervals.txt、verification.json，重建新补域、计算6,088向量并逐项核验。临时编译程序自动清理。不会重跑旧两块大型 census。

原本已附 domain_intervals.txt、domain_summary.json、verification.json；未附 exact_counts.txt、independent_intervals.txt。生成完成后可单独运行：

```sh
python full-seven-core-resolution/verify_resolution.py
```

可选的独立词递推与实际标签 DP 回放，在上述作者计数生成后执行：

```sh
python full-seven-core-independent-audit/check.py
```

生成本审查目录的 independent_intervals.txt、recurrence_counts.txt、results.json 和本地 recurrence 程序。默认 SOURCE 已从机器绝对路径改为相邻 full-seven-core-resolution，数学逻辑未改。这里仅预附 results.json。

## 二、第四终端秩和全局解析界

```sh
python fourth-terminal-rank-barrier/verify_fourth_rank_tradeoff.py
python fourth-terminal-rank-independent-audit/check.py
python global-seven-weight-reduction/verify_global_bound.py
python global-seven-weight-reduction/count_outer_port_domain.py
python global-seven-weight-independent-audit/check.py
```

均为独立的标准库精确算术检查，不需要账本输入。独立第四秩程序写 results.json；其余主要将报告输出到终端。小型预附 JSON 是既有结果摘要。对所有整数成立的结论来自证明文本中的解析论证，不能把有限算术检查当成全整数采样证明。

## 三、a,d≤2 完整域（按需生成较大账本）

```sh
python bounded-outer-spine-census/census.py
python bounded-outer-spine-census/verify_census.py
python bounded-outer-spine-independent-audit/audit.py --source bounded-outer-spine-census/census.json --output bounded-outer-spine-independent-audit/replayed
python bounded-outer-spine-independent-audit/compare_author.py --author bounded-outer-spine-census/verification.json --independent bounded-outer-spine-independent-audit/replayed --output bounded-outer-spine-independent-audit/comparison.replayed.json
```

生成作者 census.json（约17MB）、verification.json（约2.4MB）、summary.json；独立生成 reason_ledger.json（约17MB）、occupancy_counts.json、summary.json 与比较报告。包内仅保留作者和独立摘要、证明审查及必要源码；不附这些大账本或重复 normal/optimized/source_snapshot。代码中既有输出摘要里的校验字段无需另行操作。

## 四、a,d≤3 且 max(a,d)=3 完整域

作者回放：

```sh
cd outer-three-census
python census.py --domain-only
python verify_bounds.py
g++ -O3 -std=c++17 verify_domain.cpp -o verify_domain
./verify_domain independent_domain.txt > independent_domain_summary.txt
g++ -O3 -std=c++17 count_endpoints.cpp -lgmpxx -lgmp -o count_endpoints
./count_endpoints analytic_survivors.txt exact_counts.txt
python summarize.py
python verify_exact.py
cd ..
```

生成 analytic_survivors.json/txt、independent_domain.txt、independent_domain_summary.txt、exact_counts.txt（约38MB）以及摘要。census.py 的本地 explore.py、verify_exact.py、summarize.py 均已附齐；不带 --domain-only 时可用纯 Python 生成全部计数，替代 C++计数步骤，但独立域生成步骤仍需执行才能运行 verify_exact.py。

独立回放（在作者计数完成后）：

```sh
cd outer-three-independent-audit
g++ -std=c++17 -O2 reconstruct_domain.cpp -lgmpxx -lgmp -o reconstruct_domain
./reconstruct_domain survivors.txt interval_certificate.tsv domain_summary.tsv
python verify_intervals.py
g++ -std=c++17 -O2 recur_endpoints.cpp -lgmpxx -lgmp -o recur_endpoints
./recur_endpoints survivors.txt recurrence_counts.txt
python verify_and_ideal.py --source ../outer-three-census
cd ..
```

生成全部 survivors.txt、interval_certificate.tsv、recurrence_counts.txt 以及验证摘要。未附大型 tsv/gz 或递推计数；已附 domain_summary.tsv、interval_verification.json、verification.json（含30个实际标签 DP样本记录）。verify_and_ideal.py 的默认 --source 也已改成相邻作者目录；仍支持显式 --source。

## 本次便携化检查

仅对两处 Python 默认源目录作相对路径改动；证明／审查增加本精简版的保留边界说明和路径对应，完整数学论证不变。出版前进行一次 Python 语法、C++语法及路径／本地导入配置检查；没有再次运行上述整个数学审查。历史原文内的旧命令和文件保留说明，请以本页的新布局为准。
