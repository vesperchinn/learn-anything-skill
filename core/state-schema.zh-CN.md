# 状态结构

平台如果支持变量、记忆或数据库，应按此结构保存学习状态。平台如果不支持，应在每轮结束输出同名摘要，让用户复制保存。

```yaml
learning_state:
  locale: zh-CN
  interface_language: 中文
  learning_language: 中文
  domain: ""
  domain_slug: ""
  learner:
    background: ""
    daily_time: ""
    duration_days: 30
    goal: ""
    final_artifact: ""
  platform:
    name: ""
    file_read_access: unknown
    file_write_access: unknown
    web_access: unknown
    workflow_access: unknown
    memory_access: unknown
  progress:
    current_day: 0
    completed_modules: []
    weak_points: []
    recent_errors: []
    stage_test_scores: []
    next_3_days: []
  materials:
    material_mode: false
    items: []
    extraction_issues: []
    coverage_map: []
  reliability:
    sources: []
    claims_to_verify: []
    freshness_log: []
    status: unverified_draft
  session:
    last_activity: ""
    last_output: ""
    pending_user_action: ""
```

## 字段规则

- `progress` 是当前快照，应保持短小。
- `recent_errors` 只保留最近 20 条，完整历史放入日志或报告。
- `sources` 不允许填入伪造链接。
- `claims_to_verify` 在无联网时必须存在。
- `extraction_issues` 在资料无法读取时必须存在。

