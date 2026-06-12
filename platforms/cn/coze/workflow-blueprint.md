# Coze Workflow Blueprint

## 节点总览

| 节点 | 输入 | 输出 | 说明 |
| --- | --- | --- | --- |
| 1. Intake | 用户消息、变量 | `learning_state` | 收集领域、基础、时间、目标、资料、语言、平台能力 |
| 2. Material Register | 上传文件、粘贴文本、知识库命中 | `materials.items` | 登记资料 ID、名称、类型、读取状态 |
| 3. Material Extract / Retrieve | 资料 ID、问题 | 资料片段、位置 | 从知识库或上传文件中取回内容 |
| 4. Grounding Check | 资料片段、生成草稿 | grounding 标签 | 判断 Grounded、Partially grounded、Supplemental、Unresolved |
| 5. Knowledge Map | `learning_state`、资料索引 | 知识地图 | 生成领域地图和学习阶段 |
| 6. Plan | 知识地图、用户时间 | 学习计划 | 每天概念、练习、输出任务 |
| 7. Daily Session | 当前天、薄弱点、资料片段 | 学习课 | 解释、示例、练习、任务、来源 |
| 8. Assessment | 学习范围、当前阶段 | 测试题 | 先输出题目，不输出答案 |
| 9. Grading | 用户答案、答案标准 | 分数、错误归因 | 用户提交后评分 |
| 10. Review Update | 课程结果、错误归因 | 新状态 | 更新进度、薄弱点、待核查 |
| 11. Report | 状态、来源、资料覆盖 | 报告 | 输出阶段报告或学习仓库文件块 |

## 条件分支

- `file_read_access = false`：跳过资料提取，进入“要求粘贴/OCR/转换”分支。
- `web_access = false`：所有事实进入未验证草稿分支。
- `material_mode = true`：生成内容前必须经过 Material Register 和 Grounding Check。
- `workflow_access = false`：使用 `bot-prompt.zh-CN.md` 的单 Bot 降级模式。

## 节点提示词引用

每个生成节点都应检索知识库中的：

- `core/learning-protocol.zh-CN.md`
- `core/reliability-protocol.zh-CN.md`
- `core/material-grounding-protocol.zh-CN.md`
- `core/output-contract.zh-CN.md`

