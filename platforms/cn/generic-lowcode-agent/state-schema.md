# Generic Low-Code State Schema

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| `locale` | string | 是 | 默认 `zh-CN` |
| `domain` | string | 是 | 学习领域 |
| `domain_slug` | string | 是 | 英文短名 |
| `user_background` | string | 是 | 用户基础 |
| `daily_time` | string | 是 | 每天学习时间 |
| `duration_days` | number | 是 | 学习周期 |
| `learning_goal` | string | 是 | 学习目标 |
| `final_artifact` | string | 否 | 最终作品 |
| `material_mode` | boolean | 是 | 是否基于资料 |
| `current_day` | number | 是 | 当前天数 |
| `completed_modules` | array | 是 | 已完成模块 |
| `weak_points` | array | 是 | 薄弱点 |
| `recent_errors` | array | 是 | 最近错误 |
| `sources` | array | 是 | 来源记录 |
| `claims_to_verify` | array | 是 | 待核查主张 |
| `extraction_issues` | array | 是 | 资料提取问题 |
| `next_3_days` | array | 是 | 后续计划 |

## 无状态平台

如果平台没有变量或记忆，每轮末尾输出：

```yaml
learning_state:
  domain:
  current_day:
  completed_modules:
  weak_points:
  recent_errors:
  claims_to_verify:
  extraction_issues:
  next_3_days:
```

