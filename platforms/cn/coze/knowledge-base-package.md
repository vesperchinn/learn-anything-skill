# Coze Knowledge Base Package

## 上传分组

### 1. 核心协议

- `core/learning-protocol.zh-CN.md`
- `core/reliability-protocol.zh-CN.md`
- `core/material-grounding-protocol.zh-CN.md`
- `core/state-schema.zh-CN.md`
- `core/output-contract.zh-CN.md`

用途：Bot 和工作流每次生成前检索，保证学习闭环、资料 grounding、来源规则和输出格式一致。

### 2. 方法与可靠性

- `references/zh-CN/learning-principles.md`
- `references/zh-CN/error-types.md`
- `references/zh-CN/project-patterns.md`
- `references/zh-CN/source-quality-policy.md`
- `references/zh-CN/freshness-policy.md`
- `references/zh-CN/claim-verification-guide.md`
- `references/zh-CN/high-stakes-domain-policy.md`
- `references/zh-CN/material-grounding-policy.md`
- `references/zh-CN/pdf-slide-handling.md`

用途：复杂学习设计、错误诊断、项目设计、事实核查和资料处理。

### 3. 输出模板

- `templates/zh-CN/concept-template.md`
- `templates/zh-CN/source_notes.md.template`
- `templates/zh-CN/material_manifest.md.template`
- `templates/zh-CN/material_index.md.template`
- `templates/zh-CN/material_coverage_map.md.template`
- `templates/zh-CN/material_learning_plan.md.template`
- `templates/zh-CN/claims_to_verify.md.template`
- `templates/zh-CN/claim_ledger.md.template`
- `templates/zh-CN/freshness_log.md.template`

用途：约束学习内容、来源记录和资料索引的格式。

### 4. 用户资料

把用户上传的课程 PDF、PPT、文档导出、笔记、OCR 文本单独建知识库分组。每个文档命名建议：

`M001-资料名-类型-日期`

## 检索要求

- 生成课程前检索核心协议。
- 生成资料课程前检索用户资料和资料 Grounding 协议。
- 引用用户资料时保留资料 ID、章节、页码、幻灯片或片段位置。
- 检索不到资料时，不得猜测。

