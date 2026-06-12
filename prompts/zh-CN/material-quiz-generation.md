# 基于资料的测验生成

**模式**：Material-Grounded Learning
**输入**：`learning_materials/material_index.md`、提取资料、测验范围
**输出文件**：`06_quizzes/material-quiz-N.md`、可选答案文件

---

从用户提供的资料生成测验。

## 测验结构

- 5 道记忆题
- 3 道应用题
- 2 道综合题
- 如果资料包含图表、表格或视觉内容，可加入解读题

## 要求

- 每道题必须标出资料 ID 和位置。
- 如果位置未知，写 `location unresolved`。
- 只有明确标记 `Supplemental` 时，才可使用补充内容。
- 视觉题必须标明类型：图表、表格、截图、图示或流程图。
- 面向学习者的测验文件不得包含答案；答案另写文件。

## 禁止

- 不得伪造页码或幻灯片编号。
- 不得询问资料中不存在的事实，除非标记为 `Supplemental`。
- 不得编造图表数值或表格内容。

使用 `templates/{locale}/material_quiz.md.template` 格式。
