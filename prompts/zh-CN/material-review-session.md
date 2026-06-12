# 资料复习会话

**模式**：Material-Grounded Learning
**输入**：`progress.md`、`learning_materials/material_index.md`、`learning_materials/material_learning_plan.md`、相关提取资料
**输出文件**：每日复盘、progress 更新、可选闪卡

---

运行基于用户资料的每日学习会话。

## 会话结构

1. 复习上一轮资料范围。
2. 教授最多 3 个来自指定资料范围的概念。
3. 优先展示资料中的例子。
4. 提出 5 个基于资料的问题。
5. 布置一个与资料相关的交付任务。
6. 更新进度和覆盖情况。

## Grounding 要求

- 每个概念必须列出资料 ID，以及已知页码、幻灯片或章节。
- 如果位置未知，写 `location unresolved`。
- 如果加入外部背景，标记为 `Supplemental`。
- 涉及表格、图表、截图、图示或流程图时，必须明确指出。
- 不得编造资料中没有的细节。

## 提取不完整时

- 只教授已可用内容。
- 受影响章节标记为 `Partially grounded`。
- 将后续事项写入 `learning_materials/extraction_issues.md`。
