# Coze Variables Schema

| 变量名 | 类型 | 默认值 | 用途 |
| --- | --- | --- | --- |
| `locale` | string | `zh-CN` | 语言包 |
| `interface_language` | string | `中文` | 对话语言 |
| `learning_language` | string | `中文` | 学习内容语言 |
| `domain` | string | 空 | 学习领域 |
| `domain_slug` | string | 空 | ASCII 短名 |
| `user_background` | string | 空 | 用户基础 |
| `daily_time` | string | 空 | 每日学习时间 |
| `duration_days` | integer | `30` | 学习周期 |
| `learning_goal` | string | 空 | 学习目标 |
| `final_artifact` | string | 空 | 最终作品 |
| `material_mode` | boolean | `false` | 是否基于资料学习 |
| `web_access` | string | `unknown` | `available` / `unavailable` / `unknown` |
| `file_read_access` | string | `unknown` | 是否可读文件 |
| `workflow_access` | string | `available` | 是否启用工作流 |
| `current_day` | integer | `0` | 当前学习天数 |
| `weak_points` | array | `[]` | 薄弱点 |
| `claims_to_verify` | array | `[]` | 待核查主张 |
| `extraction_issues` | array | `[]` | 资料提取问题 |
| `next_3_days` | array | `[]` | 未来三天计划 |

## 更新规则

- Intake 节点负责初始化。
- Daily Session 后更新 `current_day`、`weak_points`、`next_3_days`。
- Reliability Flow 更新 `claims_to_verify`。
- Material Upload Flow 更新 `material_mode` 和 `extraction_issues`。

