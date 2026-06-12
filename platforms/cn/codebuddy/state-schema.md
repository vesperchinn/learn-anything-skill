# CodeBuddy State Schema

CodeBuddy 在知识库模式下可能没有稳定项目状态，因此需要显式状态字段。

| 字段 | 说明 |
| --- | --- |
| `mode` | `repo_connected` 或 `knowledge_base_only` |
| `domain` | 学习领域 |
| `current_day` | 当前学习日 |
| `current_stage` | 当前阶段 |
| `learning_goal` | 学习目标 |
| `materials_indexed` | 已登记资料 |
| `weak_points` | 薄弱点和错误类型 |
| `claims_to_verify` | 待核查主张 |
| `source_status` | 已验证、未验证草稿、部分基于资料 |
| `next_step` | 下一轮任务 |

## 规则

- 知识库模式下每轮输出 `learning_state`。
- 无联网时 `source_status` 必须包含未验证草稿。
- 无文件读取时不得假装读取本地仓库或用户资料。
