# Generic Agent Adapter — Minimal Protocol

## What This Is

The minimal, lowest-common-denominator protocol for using the Learn Anything
Skill Pack with **any** AI agent — including agents you build yourself.

If an agent can read text and generate text, it can follow this protocol.

## The Protocol (5 Rules)

### Rule 1: All State Lives in Files

The agent does not need memory. The file system IS the memory.

| File | Role | Read | Write |
|------|------|------|-------|
| `progress.md` | Current state snapshot | Every session | Every session |
| `progress-log.md` | Full history | On resume | Append every session |
| `00_domain_map.md` | Knowledge landscape | When lost | Once (map phase) |
| `01_core_concepts/*.md` | Concept files | When teaching | Once per concept |
| `07_daily_review/*.md` | Session records | Yesterday's | Every session |

### Rule 2: Detect Capabilities, Adapt Behaviour

At the start of a learning engagement, determine what the agent can do:

```
CAN_READ_FILES   = true/false
CAN_WRITE_FILES  = true/false
CAN_RUN_COMMANDS = true/false
CAN_READ_MATERIAL_FILES = true/false
```

Then select the appropriate mode:

| CAN_WRITE_FILES | CAN_RUN_COMMANDS | Mode |
|-----------------|------------------|------|
| true | true | **Full**: Create files directly, run `new-domain.sh` for scaffolding. |
| true | false | **Edit**: Create files via agent's edit tool. User runs scripts manually. |
| false | false | **Copy**: Output every file as `📁 Save as: path/to/file.md` + fenced code block. User saves manually. |

For PDF/PPT/Word/webpage material handling:

| CAN_READ_MATERIAL_FILES | Material Mode |
|-------------------------|---------------|
| true | Read, extract, index, and create `learning_materials/` files before course generation. |
| false | Ask the user to paste text, provide OCR, convert to Markdown/TXT, export slides, or accept a material-processing checklist. |

### Rule 3: Every Session = 4 Parts (Non-Negotiable)

Regardless of agent capability, every learning session must contain:

```
1. EXPLAIN  → 3 concepts (one-liner + analogy + technical + case + pitfall)
2. PRACTICE → 5 quiz questions (2 recall + 2 application + 1 integration)
              Do NOT reveal answers until user submits theirs.
3. OUTPUT   → 1 deliverable task (≤ 60 min, with checkbox acceptance criteria)
4. REVIEW   → Grade work, diagnose errors (concept-gap / application-failure /
              expression-unclear / knowledge-confusion), update progress.md
```

**⛔ No session may be prose-only.** If the agent outputs an explanation with
no exercise block and no deliverable task, the session is incomplete.

### Rule 4: Error Diagnosis Before Correction

When the user makes a mistake:

```
1. Classify: [concept-gap] | [application-failure] | [expression-unclear] | [knowledge-confusion]
2. Give the correct answer
3. Provide a targeted remedial exercise matching the error type
4. Record in progress.md weak points
```

Never skip step 1. "Wrong, the answer is X" is not acceptable.

### Rule 5: progress.md Is the Dashboard

`progress.md` must be readable by any agent at the start of any session.
It is a structured snapshot with 7 required sections:

```markdown
## 当前状态       (day N/M, stage, last studied)
## 已完成模块      (checkbox list with dates)
## 薄弱点          (ranked, with error type tags)
## 错题摘要        (table: #, date, question, error type, status)
## 阶段测试成绩     (table: stage, date, score, issues)
## 项目进展        (status, start date, notes)
## 下一步          (next 3 days plan)
```

Keep it ≤ 200 lines. Move old entries to `progress-log.md`.

### Rule 6: User Materials Are Primary When Provided

If the user provides PDFs, PPTs, Markdown, TXT, Word docs, webpage exports, OCR,
or pasted notes, the agent must use Material-Grounded Learning Mode:

1. Register materials in `learning_materials/material_manifest.md`.
2. Extract readable content into `learning_materials/extracted/`.
3. Build `learning_materials/material_index.md`.
4. Generate learning modules from the material index first.
5. Mark outside additions as `Supplemental`.
6. Record unreadable content in `learning_materials/extraction_issues.md`.

Never fabricate page numbers, slide numbers, chart contents, table values,
citations, or topics not present in the material.

## How to Implement This Protocol

### If you're building an agent

1. Read `SKILL.md` for the full 8-stage workflow
2. Read `core/prompts/{locale}/*.md` for the prompt template at each stage
3. Read `references/{locale}/` for the methodology (error types, project patterns)
4. Copy `templates/{locale}/{{domain-slug}}/` for the directory structure
5. Implement capability detection (Rule 2) at intake
6. Enforce the 4-part session structure (Rule 3) in your system prompt

### If you're using an existing agent

1. Identify its capabilities using the matrix in Rule 2
2. Choose the corresponding adapter (see `adapters/README.md`) for agent-specific instructions
3. If no specific adapter exists, use this generic protocol

## Minimum Viable Session Prompt

The shortest prompt that still enforces the methodology:

```
You are a domain learning engineer. Follow these rules:

1. Teach 3 concepts. Each must include: one-liner, analogy, technical
   explanation, real case, common pitfall, and one exercise.
2. Give 5 quiz questions. Do NOT reveal answers until I submit mine.
3. Assign 1 deliverable task I can complete in ≤ 60 minutes with checkbox
   acceptance criteria.
4. When I answer wrong: diagnose the error type (concept-gap /
   application-failure / expression-unclear / knowledge-confusion)
   BEFORE giving the correct answer.
5. After the session: output the updated progress.md for me to save.

Never output theory without exercises.
```

Copy, paste, replace `{domain}` and `{day_number}`. This is the contract.
