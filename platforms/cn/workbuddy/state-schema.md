# WorkBuddy State Schema

WorkBuddy 不一定提供长期记忆或本地文件写入能力，因此每次任务报告末尾都要保留一份可复制状态。

## 必需字段

| 字段 | 说明 |
| --- | --- |
| `domain` | 学习领域 |
| `interface_language` | 对话语言 |
| `learning_language` | 学习内容语言 |
| `current_stage` | 当前阶段 |
| `completed_modules` | 已完成模块 |
| `weak_points` | 薄弱点，使用四类错误标签 |
| `materials` | 用户资料 ID、类型、可读状态 |
| `claims_to_verify` | 待核查主张 |
| `next_actions` | 下一步任务 |

## 输出规则

- 无长期记忆时，每轮输出 `learning_state`。
- 无文件写入时，把状态放在报告末尾。
- 无联网时，状态必须标记 `未验证草稿`。
