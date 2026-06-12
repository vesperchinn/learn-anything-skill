# Module Map

## 1. Core Skill

Files:

- `SKILL.md`
- `core/*-protocol.*.md`
- core usage and fallback rules

Responsibility: define the agent-facing learning protocol, usage rules, safety
boundaries, locale policy, reliability behavior, and material-grounded behavior.

## 2. Learning System

Files:

- `core/prompts/`
- `prompts/`
- `templates/`
- learning repository structure
- progress, exercises, quizzes, projects

Responsibility: generate and maintain learning repositories and sessions.

## 3. Localization

Files:

- `en-US` and `zh-CN` paths under `core/prompts`, `prompts`, `templates`,
  `references`, `examples`, and `evals`

Concepts:

- `interface_language`
- `learning_language`
- `material_language`
- `locale`

Responsibility: keep behavior aligned across locales without mixing UI language,
learning language, and material language.

## 4. Knowledge Reliability Layer

Files:

- source templates
- source notes
- claim ledger
- claims to verify
- freshness log
- high-stakes policy
- no-web fallback

Responsibility: prevent unsupported certainty, stale claims, fabricated sources,
and missing high-risk disclaimers.

## 5. Material-Grounded Learning Mode

Files:

- material prompts
- material templates
- PDF/PPT handling references
- `learning_materials` templates and examples

Responsibility: make user materials the primary source, track extraction issues,
and label supplemental knowledge.

## 6. Platform Adapters

Platforms:

- Codex
- Claude Code
- Cursor
- ChatGPT
- Generic Agent
- Coze
- WorkBuddy
- Trae
- CodeBuddy
- Generic Low-Code Agent

Responsibility: adapt the core protocols without making core depend on any one
platform.

## 7. Examples

Files:

- `examples/en-US/`
- `examples/zh-CN/`
- material examples
- reliability examples

Responsibility: demonstrate expected outputs. Examples do not define template
truth.

## 8. Evals

Files:

- base learning evals
- localization evals
- reliability evals
- material-grounded evals
- platform evals
- hallucination trap evals

Responsibility: test behavior expectations. Evals do not become business logic.

## 9. Scripts

Files:

- initialization scripts
- validation scripts
- packaging scripts
- release checks

Responsibility: automate repeatable checks without silently changing files.

