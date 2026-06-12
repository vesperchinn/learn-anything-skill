# State Schema

If a platform supports variables, memory, or database records, store learning state with this structure. If not, output the same summary at the end of each session for the user to keep.

```yaml
learning_state:
  locale: en-US
  interface_language: English
  learning_language: English
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

## Field rules

- `progress` is the current snapshot and should stay compact.
- `recent_errors` keeps only the latest 20 entries; full history belongs in a log or report.
- `sources` must not contain fabricated links.
- `claims_to_verify` is required when web access is unavailable.
- `extraction_issues` is required when materials cannot be read.

