# Learning Principles

These principles are referenced by all core prompts. They define the pedagogical
foundation of the Learn Anything Skill Pack.

## Core Method: Five Systems

A complete learning system requires five interconnected subsystems:

1. **Knowledge Map** — solves "I don't know what this field contains"
2. **Glossary** — solves "I don't understand the terminology"
3. **Exercise System** — solves "I thought I understood, but I didn't"
4. **Project System** — solves "I learned a lot but can't apply it"
5. **Review System** — solves "I forget everything and never fix mistakes"

## Teaching Sequence

```
Global Map → Core Concepts → Case Studies → Exercises → Capstone Project
```

Never start with details. Always establish the landscape first.

## Teaching Flow by Locale

| Step | en-US | zh-CN |
|------|-------|-------|
| 1. Introduce | Explain | 解释 |
| 2. Show | Demonstrate | 示例 |
| 3. Do | Practice | 练习 |
| 4. Verify | Check | 检查 |
| 5. Improve | Reflect | 复盘 |

## The 20-60-20 Rule

For any domain, categorize knowledge into three tiers:

- **Top 20% (must-learn-now)**: Without this, you cannot proceed. Gatekeeping knowledge.
- **Middle 60% (skip-for-now)**: Useful but not immediately necessary. Creates a false
  sense of progress.
- **Bottom 20% (learn-later)**: Advanced/specialized. Only relevant after completing a
  project.

Focus all initial energy on the top 20%.

## Daily Learning Cycle

Every day must include all four modes:

```
Learn (input) → Practice (apply) → Output (create) → Test (verify)
```

- **Learn**: Maximum 3 new concepts per day
- **Practice**: At least 5 targeted exercises
- **Output**: One deliverable in ≤ 60 minutes
- **Test**: Self-check against acceptance criteria

## Variable Conventions

All core prompts use these standard variables:

| Variable | Description | Example |
|----------|-------------|---------|
| `{domain}` | Learning domain name | AI Agent |
| `{domain_slug}` | URL-friendly domain name | ai-agent |
| `{locale}` | Which locale pack to load | en-US, zh-CN |
| `{interface_language}` | Language for agent-user conversation | English, 中文 |
| `{learning_language}` | Language for learning materials | English, 中文 |
| `{user_background}` | User's current knowledge level | Beginner programmer |
| `{daily_time}` | Available time per day | 2 hours |
| `{learning_goal}` | Why they're learning | exam, work, project, research |
| `{final_artifact}` | Desired final deliverable | A personal research agent |
| `{day_number}` | Current day number | 3 |
| `{agent_type}` | Current agent type | codex, cursor, chatgpt, generic |

## Error Diagnosis Taxonomy

When a learner makes a mistake, classify it into one of four types before
responding. Tags are locale-independent. Labels vary by locale.

| Tag | en-US label | zh-CN label | Remediation |
|-----|-------------|-------------|-------------|
| `[concept-gap]` | Conceptual misunderstanding | 不懂概念 | Return to definition + Feynman explanation + life analogy |
| `[application-failure]` | Application gap | 不会应用 | Scenario-based exercises + case imitation |
| `[expression-unclear]` | Unclear explanation | 表达不清 | Feynman output exercise + verbal explanation practice |
| `[knowledge-confusion]` | Knowledge confusion | 知识混淆 | Comparison table + discrimination exercise + side-by-side cases |

## Output Quality Standards

Every learning artifact must be:

- **Runnable** (if code): Actually executes and produces output
- **Demonstrable**: Can be shown to someone else
- **Explainable**: User can describe what they built and why
- **Iterable**: Can be improved in a future session

## Safety Rules

- Do not invent books, papers, citations, URLs, or expert claims.
- Mark uncertain facts as uncertain and suggest verification.
- For medical, legal, financial, safety-critical, or professional certification
  domains, add a verification note and recommend authoritative sources.
- Never write private user information into the learning repository without
  explicit permission.
- Stage test answers must be in a separate `stage-test-N.answer-key.md` file,
  never in the learner-facing test file.
