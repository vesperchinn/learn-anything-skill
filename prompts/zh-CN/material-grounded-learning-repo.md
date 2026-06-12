# 基于资料的学习仓库

**模式**：Material-Grounded Learning
**输入**：`learning_materials/material_manifest.md`、提取资料、`{domain}`、`{duration}`、`{daily_time}`、`{locale}`
**输出文件**：`00_domain_map.md`、`01_core_concepts/`、`learning_materials/material_index.md`、`learning_materials/material_coverage_map.md`、`learning_materials/material_learning_plan.md`、`progress.md`、`09_sources/claim_ledger.md`

---

基于用户资料创建学习仓库，而不是生成泛泛课程。

## Grounding 优先级

1. `learning_materials/raw/` 中的用户资料。
2. `learning_materials/extracted/` 中的提取内容。
3. 外部补充知识，仅在需要时使用，并明确标记 `Supplemental`。

## 必须输出

1. `learning_materials/material_index.md`
   - 按主题和可用页码、幻灯片或章节索引资料。
   - 标记图表、表格、截图、图示和流程图。
2. `00_domain_map.md`
   - 从资料主题和结构生成知识地图。
   - 每个主要概念包含资料 ID 和位置。
3. `01_core_concepts/`
   - 只为资料中出现的概念创建文件；外部补充必须标记 `Supplemental`。
4. `learning_materials/material_coverage_map.md`
   - 将每个学习模块映射回资料 ID 和位置。
5. `learning_materials/material_learning_plan.md`
   - 生成按天学习计划，优先遵循资料本身顺序。
6. `progress.md`
   - 初始化资料覆盖、当前提取问题和下一步。
7. `09_sources/claim_ledger.md`
   - 记录来自资料的关键事实主张，Source Type 设为 `Material`，包含 Material ID / Location、可信度和时效性风险。
   - 外部补充主张的 Source Type 设为 `Supplemental`。
8. `START_HERE.md`、`TODAY.md` 和 `07_daily_review/day-01.md`
   - 在资料索引完成后创建第 1 天陪跑入口。
   - 第 1 天内容必须基于可用的资料索引，不要求学习者先打开多个文件。

## 规则

- 用户资料是 primary source。
- 不得用通用领域知识替代资料内容。
- 外部添加必须标记 `Supplemental`。
- 无法读取或未提取的内容必须保持 unresolved extraction issue。
- 不得伪造页码、幻灯片编号、视觉内容、引用或资料主题。
- 如果视觉内容重要但无法提取，相关模块标记为 `Partially grounded`。
- 来自资料的主张必须可在 `09_sources/claim_ledger.md` 中审计。
- 资料索引和学习仓库创建完成后，不得只输出文件清单后停止。除非用户明确要求 scaffold-only，否则必须立刻在聊天里开始第 1 天陪跑学习。
- 陪跑学习必须告诉学习者不用先翻文件，包含一个聊天小任务、作答模板、完成标准，并说明完成后会更新 `progress.md`。

生成的学习模块末尾必须包含标准来源注释和时效性尾部。
