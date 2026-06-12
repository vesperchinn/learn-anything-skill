# 资料 Grounding 政策

当学习者提供 PDF、PPT、Markdown、TXT、Word、网页导出或其他学习资料时，使用 Material-Grounded Learning Mode。此模式下，用户资料定义学习仓库的课程范围。

## 优先级规则

1. **用户提供的资料是学习仓库的 primary source。**
2. 提取文本、OCR、表格、图注、演讲备注和用户补充说明都属于资料派生内容，继承同等优先级。
3. 外部知识只能在资料不完整、不清楚或明确需要背景知识时使用，并且必须标记为 `Supplemental`。

## 必须行为

- 先读取、解析、索引资料，再生成知识地图。
- 知识地图、概念、练习、测验、复习卡、项目任务和 `progress.md` 都必须优先来自资料索引。
- 学习输出要保留资料 ID 和位置。
- 使用 `learning_materials/material_coverage_map.md` 标明模块是 grounded、partial、supplemental 还是 gap。
- 无法读取或部分提取失败的内容必须作为 unresolved extraction issue 记录到 `learning_materials/extraction_issues.md`。

## 禁止行为

Agent 不得：

- 用泛泛的领域课程替代用户资料。
- 伪造页码、幻灯片编号、图表内容、引用、作者观点、定义、例子或材料中不存在的知识点。
- 在未提取或未视觉检查的情况下声称图表、截图、表格或流程图表达了某个结论。
- 把外部内容混入资料学习输出而不标记 `Supplemental`。

## Grounding 标签

在模块、测验和覆盖图中使用：

- `Grounded`：直接由用户资料支持。
- `Partially grounded`：基于资料，但存在提取缺口。
- `Supplemental`：来自用户资料之外的补充内容。
- `Unresolved extraction issue`：资料存在，但无法可靠读取或解释。

## 无文件读取能力时的降级

如果 Agent 不能读取文件，不得假装看过资料。必须要求用户：

1. 粘贴相关文本。
2. 提供 OCR 结果。
3. 将资料转换为 Markdown 或 TXT。
4. 将幻灯片导出为文本和图片。
5. 或只生成资料处理清单，而不是资料 grounded 课程。
