---
name: learn-anything
description: >
  Use when the user wants to learn a new field through a structured study
  repository, create a study plan, learn from supplied PDFs, slide decks,
  Markdown, TXT, Word docs, or webpage exports, assess understanding through
  exercises and stage tests, or build a capstone project. Best for multi-session
  learning workflows that need progress tracking, source notes, and review.
---

# learn-anything

Turn any AI agent into a domain learning engineer — scaffold a structured
learning repository, generate knowledge maps, run daily learn→practice→output→test
cycles, diagnose errors, track progress, and guide a capstone project.

## Do Not Use When

Do not use this Skill Pack when the user only wants:

- A one-off factual answer, definition, summary, translation, or quick rewrite
- Professional advice in medical, legal, financial, safety-critical, or other
  regulated domains
- Guaranteed factual correctness without verification against authoritative
  sources
- A generic motivational study plan with no file-based learning repository
- Direct publication-ready content unrelated to learning, practice, assessment,
  or progress tracking

## Language and Locale Policy

This Skill Pack supports English and Chinese locales with full separation of
interface language and learning material language.

### Locale Variables

At intake, capture these variables. They drive every file path and content
decision:

| Variable | Description | Example values |
|----------|-------------|----------------|
| `{locale}` | Which locale pack to load | `en-US`, `zh-CN` |
| `{interface_language}` | Language for agent-user conversation | `English`, `中文` |
| `{learning_language}` | Language for learning materials (may differ) | `English`, `中文` |
| `{domain}` | What the user wants to learn | `AI Agent`, `nutrition`, `古典音乐` |
| `{domain_slug}` | Filesystem-safe domain name | `ai-agent`, `nutrition`, `classical-music` |
| `{user_background}` | Current knowledge level | `zero`, `beginner`, `intermediate`, `advanced` |
| `{daily_time}` | Available time per day | `1 hour`, `2.5 hours`, `45 minutes` |
| `{duration}` | Total learning period in days | `30`, `14`, `60` |
| `{learning_goal}` | Why they're learning | `exam`, `work`, `project`, `writing`, `product`, `research` |
| `{final_artifact}` | What they want to build or produce | `a personal research assistant`, `unsure` |
| `{web_access}` | Whether the agent can verify current sources online | `available`, `unavailable`, `unknown` |
| `{material_mode}` | Whether user-provided materials define the course scope | `true`, `false` |
| `{material_paths}` | Local files or folders supplied by the user | `slides/week1.pptx`, `docs/*.pdf` |
| `{material_urls}` | Webpage exports or URLs supplied by the user | `course-export.html` |
| `{file_read_access}` | Whether the agent can read the supplied files | `available`, `unavailable`, `unknown` |

### How Locale Works

1. **Detect**: Default `{locale}` is inferred from the user's input language.
   `scripts/detect_language.py` provides a reference implementation. The user can
   override explicitly: "Use English for the interface but Chinese for the
   learning materials."

2. **Route**: All file-paths include `{locale}`:
   - Prompts: `core/prompts/{locale}/`
   - Material-grounded prompts: `prompts/{locale}/`
   - Templates: `templates/{locale}/{{domain-slug}}/`
   - References: `references/{locale}/`
   - Examples: `examples/{locale}/`

3. **Generate**: Content language follows `{learning_language}`. If
   `{interface_language}` ≠ `{learning_language}`, the agent converses in the
   interface language but writes all learning repository files in the learning
   language.

4. **Default behavior**:
   - English input → `{locale}=en-US`, `{interface_language}=English`, `{learning_language}=English`
   - Chinese input → `{locale}=zh-CN`, `{interface_language}=中文`, `{learning_language}=中文`
   - Mixed: ask the user to clarify both languages.

### Teaching Flow by Locale

| Stage | en-US | zh-CN |
|-------|-------|-------|
| Teach | Explain | 解释 |
| Show | Demonstrate | 示例 |
| Do | Practice | 练习 |
| Verify | Check | 检查 |
| Improve | Reflect | 复盘 |

### Error Taxonomy by Locale

| Tag (locale-independent) | en-US label | zh-CN label |
|--------------------------|-------------|-------------|
| `[concept-gap]` | Conceptual misunderstanding | 不懂概念 |
| `[application-failure]` | Application gap | 不会应用 |
| `[expression-unclear]` | Unclear explanation | 表达不清 |
| `[knowledge-confusion]` | Knowledge confusion | 知识混淆 |

The tag is locale-independent (used in progress.md weak-point lists). The
label used in conversation matches `{interface_language}`.

### progress.md Section Headings

| en-US | zh-CN |
|-------|-------|
| `## Current Status` | `## 当前状态` |
| `## Completed Modules` | `## 已完成模块` |
| `## Weak Points (by priority)` | `## 薄弱点（按优先级）` |
| `## Error Summary (last 20)` | `## 错题摘要（最近 20 条）` |
| `## Stage Test Scores` | `## 阶段测试成绩` |
| `## Project Progress` | `## 项目进展` |
| `## Next Steps (next 3 days)` | `## 下一步（未来 3 天）` |

## Workflow

Every learning engagement follows these eight stages. At each stage, read the
referenced prompt file from `core/prompts/{locale}/` for the full instruction
template.

## Guided Learning Mode

Default mode is guided learning. Unless the user explicitly asks for
scaffold-only mode, after creating a learning repository, the agent must
immediately start a guided learning session. The agent must not stop after
listing generated files.

Scaffold-only mode is allowed only when the user explicitly says one of:

- "只创建项目"
- "不要开始学习"
- "scaffold only"
- "generate files only"

After repository creation, read `prompts/{locale}/start-guided-session.md` and
start Day 1 in the chat. The first response after repository creation must
include:

1. Repository location.
2. A short explanation of what was created.
3. A short Freshness Notice when the repository contains freshness files,
   freshness risk metadata, high-stakes content, fast-changing content, or
   no-web / no-retrieval uncertainty.
4. The sentence: "You do not need to open the files first." or the localized
   equivalent.
5. Today's learning goal.
6. A beginner-friendly explanation of the first concepts, or exactly one
   primary concept when Interactive Beginner Lesson Mode is active.
7. One small task that can be completed directly in the chat.
8. A copyable answer template.
9. Clear completion criteria for regular learners; for Interactive Beginner
   Lesson Mode, a plain-language "how to tell this worked" prompt after the
   worked example.
10. A prompt telling the user to reply with their answer.
11. A note that `progress.md` will be updated after the user completes the task.

### Freshness Notice in Chat Output

After creating a learning repository, if the generated repository contains any
freshness-related files or freshness risk metadata, the agent must include a
short Freshness Notice in the chat output. The notice appears together with the
repository creation summary and before or near the Day 1 guided session. The
agent must not require the learner to open `09_sources/freshness_log.md` before
knowing that freshness tracking exists.

The Freshness Notice must include:

- overall freshness status
- highest freshness risk level
- recommended review interval
- path to `09_sources/freshness_log.md`
- path to `09_sources/claims_to_verify.md`, if any claims require verification
- no-web / no-retrieval disclaimer if the agent could not verify current sources
- educational-use-only / not-final-advice wording for high-stakes domains

For high-stakes or fast-changing domains, the Freshness Notice is mandatory.
These domains include but are not limited to finance, investment, medical,
health, legal, policy, tax, immigration, AI tools, APIs, software libraries,
pricing, benchmarks, exam policies, platform rules, and market data.

Use `templates/{locale}/freshness_notice.md.template` when composing the notice.
Keep it short so it does not overwhelm Day 1 learning:

- Low-risk / stable domains: say the project is mainly stable foundational
  knowledge and point to `09_sources/freshness_log.md`.
- Medium-risk / evolving domains: say the content may evolve with tools or
  practice, recommend a 3-6 month review, and point to
  `09_sources/freshness_log.md`.
- High-risk / fast-changing domains: say the content cannot rely only on model
  memory, recommend checking official or authoritative sources before use, point
  to `09_sources/freshness_log.md`, and point to
  `09_sources/claims_to_verify.md`.

Freshness Notice template fields are `freshness_risk_label`,
`highest_freshness_risk`, `recommended_review_interval`, `freshness_log_path`,
`claims_to_verify_path`, `source_status`, and `verification_disclaimer`.

### Interactive Beginner Lesson Mode

If `{user_background}` indicates technical beginner, beginner, complete
beginner, student, no code, no coding background, non-developer, content
creator, writer, marketer, operations, teacher, self-media creator, or a user who wants a quick entry point,
enable Interactive Beginner Lesson Mode.

Trigger this mode when the user background includes:

- beginner
- complete beginner
- non-technical
- student
- no coding background
- writer
- marketer
- zero background
- quick-start learner
- 初学者
- 学生
- 非技术用户
- 内容创作者
- 自媒体
- 运营
- 老师

Rules:

- Say less about file paths and more about what to do now.
- Use familiar scenarios instead of abstract theory.
- Give one main task at a time.
- Do not require the user to open multiple Markdown files.
- Do not require code unless the user explicitly wants to learn coding.
- The first guided session must be self-contained in the chat.
- Do not rely on the user opening Markdown files first.
- Teach one primary concept at a time.
- Do not introduce more than 2 supporting terms in the first session.
- Every abstract term must be translated into plain language.
- Every abstract term must include one concrete example from the user's goal or
  background.
- Before asking the user to do a task, provide a fully worked example.
- Include one bad example and one improved example.
- Use "I do → We do → You do" structure.
- The first task must be small enough to complete in 10-15 minutes.
- The first task must ask for only one workflow step unless the user is
  advanced.
- For content creators, examples must use content creation workflows.
- Avoid jargon-heavy terms unless immediately explained.
- Avoid asking for "criteria", "rubrics", "test cases", "checkpoints", or
  "standards" before showing what they look like.
- Every daily task must include a copyable answer template.
- End with exactly one clear action instruction in the user's language. For
  Chinese, use: "请直接把模板填好发给我。"

### 1. intake — collect learner profile

Ask the user (don't guess):

- **Domain**: What do you want to learn?
- **Background**: Current knowledge level (zero / beginner / intermediate).
- **Daily time**: How many hours/minutes per day?
- **Duration**: How many days total? (default: 30)
- **Goal**: Exam / work / project / writing / product / research.
- **Final artifact**: What do you want to build or produce? ("unsure" is OK — recommend 2–3 options.)
- **Materials**: Are there PDFs, PPTs, Markdown, TXT, Word docs, webpage exports,
  or pasted notes that should define the learning scope?
- **Languages**: Confirm `{interface_language}` and `{learning_language}`.
  If the user's input language is clear, default accordingly. If the user says
  "Chat in Chinese but learning materials in English", set both explicitly.

Capture these as variables: `{domain}` `{domain_slug}` `{user_background}`
`{daily_time}` `{duration}` `{learning_goal}` `{final_artifact}` `{locale}`
`{interface_language}` `{learning_language}` `{agent_type}` `{web_access}`
`{material_mode}` `{material_paths}` `{material_urls}` `{file_read_access}`.

### 2. scaffold — create the learning repository

Read `core/prompts/{locale}/init-repo.md` for the full template.

Create this structure under `learn-{domain_slug}/`:

```
learn-{domain_slug}/
├── START_HERE.md               # Beginner-friendly first entry point
├── TODAY.md                    # Today's single learning entry point
├── README.md                   # How to use this repo
├── AGENTS.md                   # Teaching rules for the AI
├── CLAUDE.md                   # Equivalent teaching rules for Claude Code
├── 00_domain_map.md            # Knowledge landscape (Phase 3)
├── 01_core_concepts/           # One file per concept
├── 02_case_studies/            # Real-world cases
├── 03_exercises/               # Practice exercises
├── 04_projects/                # Capstone project design
├── 05_flashcards/              # Knowledge compression cards
├── 06_quizzes/                 # Stage tests
├── 07_daily_review/            # Date-stamped reviews
│   └── day-01.md               # Day 1 guided learning plan and review slot
├── 08_glossary.md              # Running terminology
├── 09_resources.md             # Recommended reading
├── learning_materials/          # User-provided material workspace
│   ├── raw/                     # Original PDFs/PPTs/docs/web exports
│   ├── extracted/               # Extracted text, OCR, tables, notes
│   ├── material_manifest.md     # Material registry and extraction status
│   ├── material_index.md        # Topic/page/slide/visual index
│   ├── material_coverage_map.md # Module-to-material grounding map
│   ├── material_learning_plan.md # Plan built from supplied materials
│   └── extraction_issues.md     # Unresolved extraction issues
├── 09_sources/                 # Knowledge reliability tracking
│   ├── sources.md              # Master source registry
│   ├── source_quality_policy.md # Source ranking and citation rules
│   ├── claim_ledger.md         # Factual claims log
│   ├── claims_to_verify.md     # Verification checklist
│   └── freshness_log.md        # Module freshness tracker
├── progress.md                 # State snapshot (≤ 200 lines)
└── progress-log.md             # Full append-only history
```

Template files live at `templates/{locale}/{{domain-slug}}/`. Copy and
populate them using the intake variables.

Every newly created learning repository must include `START_HERE.md`,
`TODAY.md`, and `07_daily_review/day-01.md` in addition to the standard
long-term learning files. `START_HERE.md` explains how to use the project
without opening every file. `TODAY.md` is the only Day 1 entry point and must
include today's goal, 2-3 concepts, beginner-friendly explanations, one life
analogy, one example tied to the user's goal, one exercise, an answer template,
completion criteria, and instructions to reply in chat. `07_daily_review/day-01.md`
records the Day 1 plan, task, checking criteria, and where the review will be
written after the user answers.

Unless scaffold-only mode was explicitly requested, do not stop after file
creation. After creating the repository, immediately output the guided Day 1
session in the conversation using the format in
`prompts/{locale}/start-guided-session.md`.

**No-filesystem fallback**: If the agent cannot create files on disk, output
every file as a fenced code block labeled with its path:

````markdown
### 📁 Save as: learn-{domain_slug}/README.md
```markdown
(content here)
```
````

Tell the user to save each block to the indicated path.

### 2a. Material-Grounded Learning Mode

Activate this mode whenever the user uploads, names, links, or pastes specific
learning materials such as PDFs, PPT/PPTX files, Markdown, TXT, Word/DOCX files,
HTML/webpage exports, OCR text, screenshots, or course notes.

Read `prompts/{locale}/material-intake.md` first, then
`prompts/{locale}/material-grounded-learning-repo.md`. Use
`prompts/{locale}/material-review-session.md`,
`prompts/{locale}/material-quiz-generation.md`, and
`prompts/{locale}/material-gap-analysis.md` during learning.

#### Grounding Rules

- User-provided materials are the primary source for the learning repository.
- Do not use generic domain knowledge to replace material content.
- External additions must be clearly marked `Supplemental` in modules,
  quizzes, coverage maps, and source notes.
- Unreadable, missing, image-only, partially extracted, or ambiguous content
  must be logged as an unresolved extraction issue in
  `learning_materials/extraction_issues.md`.
- Do not fabricate page numbers, slide numbers, chart contents, screenshot
  contents, table values, flowchart nodes, citations, or knowledge points not
  present in the materials.
- PDF/PPT charts, screenshots, tables, diagrams, and flowcharts must be
  explicitly marked in `learning_materials/material_index.md`.
- If a visual element cannot be interpreted reliably, mark the dependent
  learning module as `Partially grounded`.

#### Material Workflow

1. **Intake materials**: record every file, URL, pasted text block, and format
   in `learning_materials/material_manifest.md`.
2. **Preserve originals**: store or reference originals under
   `learning_materials/raw/` when file access exists.
3. **Extract content**: write extracted text, OCR, tables, speaker notes, and
   visual descriptions to `learning_materials/extracted/`.
4. **Index content**: build `learning_materials/material_index.md` with topics,
   available pages/slides/sections, and visual markers.
5. **Build from material**: generate `00_domain_map.md`, concept files, plans,
   exercises, quizzes, review cards, projects, and `progress.md` from the
   material index first.
6. **Track coverage**: update `learning_materials/material_coverage_map.md`
   whenever a learning module is created or changed.
7. **Analyze gaps**: use `prompts/{locale}/material-gap-analysis.md` to decide
   whether a gap should be ignored, resolved by asking the user, or filled with
   clearly labeled `Supplemental` content.

#### No File-Read Fallback

If the agent cannot read the supplied files, it must not claim to have read
them. It must downgrade to one of these options:

1. Ask the user to paste the relevant text.
2. Ask the user to provide OCR output.
3. Ask the user to convert PDFs, PPTs, Word docs, or webpages to Markdown/TXT.
4. Ask the user to export slides as text plus images.
5. Generate only a material-processing checklist, not a material-grounded course.

See `references/{locale}/material-grounding-policy.md` and
`references/{locale}/pdf-slide-handling.md`.

### 3. map — generate the knowledge map

Read `core/prompts/{locale}/knowledge-map.md`.

Write `00_domain_map.md` with these 10 sections:
1. What problem this field solves
2. Feynman explanation (a 12-year-old can understand)
3. Top 20 core concepts (one-liner + difficulty)
4. Concept dependency graph (clusters + prerequisites)
5. Top 10 confusion pairs (key difference for each)
6. Five learning stages (capability + deliverable per stage)
7. 20-60-20 split (must-learn / skip / learn-later)
8. Minimum viable knowledge (≤ 8 items)
9. What NOT to learn yet
10. Recommended learning sequence

Then read `core/prompts/{locale}/concept-breakdown.md` and populate
`01_core_concepts/`. Each concept file MUST contain: one-line explanation,
life analogy, technical explanation, real-world case, common pitfall, one
exercise.

### 4. plan — create the duration-based route

Read `core/prompts/{locale}/learning-plan.md`.

Generate a stage-by-stage schedule. Every day MUST include:
- **3 concepts** (from the must-learn-now 20%)
- **5 quiz questions** (2 recall + 2 application + 1 integration)
- **1 deliverable task** (≤ 60 minutes, with explicit acceptance criteria)

Schedule stage tests based on `{duration}`. For the default 30-day plan, use
days 7, 14, 21, and 25. For shorter or longer plans, place tests roughly every
7 days and keep the final project window proportional to the total duration.

### 5. daily — run one learning session

Read `core/prompts/{locale}/daily-session.md`.

Fixed teaching flow for every session:

**en-US**: Explain → Demonstrate → Practice → Check → Reflect
**zh-CN**: 解释 → 示例 → 练习 → 检查 → 复盘

```
1. REVIEW (5–10 min)     → 5 key points from yesterday + check weak points
2. LEARN  (30–40 min)    → 3 concepts, each with all 5 required parts
3. PRACTICE (10 min)     → 5 targeted questions (don't reveal answers yet)
4. OUTPUT  (≤ 60 min)    → One deliverable task with acceptance criteria
```

**Hard rule**: Never output an article-only session. Every session must end
with an exercise block AND a deliverable task. If the user submits work,
diagnose errors before giving the correct answer (use `error-diagnosis.md`).

### 6. assess — quiz and diagnose

Read `core/prompts/{locale}/stage-test.md` every 7 days.

Examiner mode — strict protocol:
1. Present the full test (no answers, no hints): 10 MCQ + 5 concept
   explanations + 3 scenario applications + 1 integration project (100 points
   total).
2. Wait for the user to submit all answers.
3. Grade each section. For every wrong answer, classify the error using the
   locale-independent tag:
   - `[concept-gap]` — doesn't know what the concept is
   - `[application-failure]` — knows the concept but can't use it
   - `[expression-unclear]` — understands but can't articulate
   - `[knowledge-confusion]` — mixed up with another concept
4. If score < 70: generate 3 targeted remedial exercises, re-plan the next
   3 days, schedule a re-test.
5. If score ≥ 70: confirm readiness, note residual weak spots, proceed.

For errors during daily sessions, read
`core/prompts/{locale}/error-diagnosis.md`.

### 7. review — close the day

Read `core/prompts/{locale}/daily-review.md`. After every session:

1. Summarise what was learned (3 concepts + mastery rating 1–5 each).
2. Grade today's deliverable against its acceptance criteria.
3. Diagnose any errors.
4. Update `progress.md` (snapshot — keep ≤ 200 lines):
   - Increment day counter, mark completed modules, re-rank weak points,
     add errors to summary table, update next-3-days plan.
   - Use the section headings that match `{locale}` (see table above).
5. Append to `progress-log.md` (date-stamped entry with theme, mastery,
   exercise results, error analysis, time spent).
6. Optionally generate a flashcard via
   `core/prompts/{locale}/flashcard-generate.md`.

### 8. project — build the capstone

Read `core/prompts/{locale}/project-design.md` for the final 7 days.

Design a minimum viable project that:
- Is completable in 7 days at `{daily_time}`/day
- Exercises the user's top 3 weak points from `progress.md`
- Produces a runnable, demonstrable, explainable artifact
- Has a no-code/low-code alternative if the user cannot code

Output: project name, one-line pitch, core features, tech stack, 7-day task
breakdown with daily deliverables and acceptance criteria.

## File Writing Convention

When writing to the learning repository:

| Pattern | Convention |
|---------|-----------|
| Concept files | `01_core_concepts/NN-slug.md` (NN = 2-digit sequence number) |
| Daily reviews | `07_daily_review/YYYY-MM-DD.md` |
| Flashcards | `05_flashcards/day-NN.md` |
| Stage tests | `06_quizzes/stage-test-N.md` |
| progress.md | Overwrite in-place, keep ≤ 200 lines |
| progress-log.md | Append only, never truncate |
| Glossary | Append new terms to `08_glossary.md`, sort alphabetically |

## Output Format Requirements

Every concept file must follow the locale-aware template at
`templates/{locale}/concept-template.md`:

```markdown
# Concept: {name}

## One-line Explanation
## Life Analogy
## Technical Explanation
## Real-world Case
## Common Pitfall
## Exercise
---
### Source Notes
### Freshness Risk
### Claims to Verify
**Last Verified**:
**Recommended Review Interval**:
```

Every exercise must include: task description, time budget, numbered
requirements, deliverable format, and a checkbox acceptance criteria list.

Every daily session must produce: 3 concept blocks + 5-question quiz +
1 deliverable task with acceptance criteria. Never output prose-only.

Every learning module must end with the Source Notes footer from
`templates/{locale}/source_notes.md.template`. Required footer fields:
Source Notes, Freshness Risk, Claims to Verify, Last Verified, and
Recommended Review Interval.

## No-Code / Low-Code Rule

If `{user_background}` indicates no coding ability, or the domain is
non-technical:

- Replace "build an app" with "design a detailed system spec + mockup"
- Replace "write a script" with "document a step-by-step manual workflow"
- Replace "train a model" with "curate a dataset with annotation guidelines"
- Capstone project options must include at least one zero-code alternative.

## Agent Capability Fallback

Detect the agent's capabilities at intake. Use `{agent_type}`:

| `{agent_type}` | File I/O | Behaviour |
|----------------|----------|-----------|
| `codex` | read + write | Create files directly. Run shell commands for scaffolding. |
| `cursor` / `windsurf` | read + write | Create files directly. |
| `copilot` | read + write | Create files directly. Commands run manually by user. |
| `generic` | none | Output every file as a fenced code block labelled with its path. Instruct the user to save each block. |

When `{agent_type}` is `generic`, prefix every file output with:

```
📁 Save as: learn-{domain_slug}/path/to/file.md
```markdown
(content)
```
```

## Safety and Source Rules

- **Do not invent facts.** Never fabricate books, papers, citations, URLs,
  expert claims, or statistics. If you are uncertain, mark the fact as
  uncertain and suggest the learner verify.
- **High-risk domains.** For medical, legal, financial, safety-critical, or
  professional certification domains, add a clear verification note at the
  start of the learning repository and recommend authoritative sources
  (textbooks, official documentation, accredited courses).
- **Privacy.** Do not write private user information (real name, email,
  location, health data) into a public learning repository unless the user
  explicitly requests it.
- **File safety.** Before overwriting existing files in the learning
  repository, preserve user-written content or ask for confirmation.
- **Source quality.** Prefer primary sources (original papers, official docs,
  textbooks) over secondary summaries. When the learner requests citations,
  use web search or browsing to verify before writing.
- **Answer key separation.** Stage test answers and grading rubrics must be
  written to a separate `stage-test-N.answer-key.md` file, never in the
  learner-facing test file.

For the complete knowledge reliability framework, see
**§ Knowledge Reliability Layer** below and the reference documents at
`references/{locale}/source-quality-policy.md`,
`references/{locale}/freshness-policy.md`,
`references/{locale}/high-stakes-domain-policy.md`, and
`references/{locale}/claim-verification-guide.md`.

## Key Constraints

- ⛔ Never output a prose-only learning session.
- ⛔ Never skip the exercise block or the deliverable task.
- ⛔ Never give the correct answer without diagnosing the error type first.
- ⛔ Never let progress.md exceed 200 lines — move old entries to progress-log.md.
- ✅ Every stage must produce at least one concrete file in the learning repo.
- ✅ Read references from `references/{locale}/` — `learning-principles.md`,
  `error-types.md`, `project-patterns.md`.
- ✅ Use the correct section headings in progress.md for `{locale}`.
- ✅ File names stay ASCII/English regardless of locale.
- ⛔ Never fabricate URLs, DOIs, paper titles, author names, or benchmark data.
- ⛔ Never fabricate material page numbers, slide numbers, visual content, or
  topics not present in user materials.
- ✅ When materials are supplied, create and maintain `learning_materials/`.
- ✅ Mark outside additions to material-grounded modules as `Supplemental`.
- ✅ Record unresolved extraction issues instead of guessing missing content.
- ⛔ Never present AI-generated content as professional advice in high-stakes domains.
- ✅ Tag every module with a freshness risk level (🟢/🟡/🔴).
- ✅ Mark unverifiable claims with `[unverified]`.
- ✅ When lacking web access, tag all output as "Unverified Draft".

## Knowledge Reliability Layer

This Skill Pack implements a systematic defense against AI hallucination,
stale knowledge, and fabricated citations. Every learning module generated
by the Agent must follow these five policies.

### Source-First Reliability Policy

Every factual claim generated by the Agent must either have a source,
be marked as `[unverified]`, or be removed. The source hierarchy, from
most to least trusted:

| Tier | Source Type | Examples |
|------|-------------|----------|
| Primary | Official documentation, peer-reviewed papers, textbooks | Python docs, RFC standards, university textbooks |
| Secondary | Tutorials, blog posts by domain experts, conference talks | Real Python, Martin Fowler's blog, PyCon talks |
| Tertiary | AI-generated summaries, forum answers, social media | ChatGPT output, Stack Overflow answers, Reddit threads |

Rules:
- Prefer Primary over Secondary over Tertiary.
- Never fabricate a URL, DOI, paper title, author name, or publication date.
- If the Agent has web access, it MUST search or directly verify before citing
  any current, specific, high-stakes, numeric, benchmark, legal, medical,
  financial, pricing, version, or release-date claim.
- If the Agent cannot verify a claim, it MUST mark it as `[unverified]`.
- All sources used for a module are logged in `09_sources/sources.md`.
- The learning repository must include `09_sources/source_quality_policy.md`
  so future sessions can apply the same source hierarchy.

See `references/{locale}/source-quality-policy.md` for the full policy.

### Freshness Risk Classification

Every generated module receives a freshness tag indicating how quickly the
content may become outdated:

| Tag | Meaning | Review Interval | Examples |
|-----|---------|-----------------|----------|
| 🟢 Stable | Foundational, unlikely to change | 12+ months | Math axioms, classical algorithms, physics laws |
| 🟡 Evolving | Changes every 1–3 years | 3–6 months | Framework best practices, API design patterns, industry standards |
| 🔴 Volatile | Changes monthly or faster | 1–4 weeks | Library versions, model benchmarks, pricing, regulatory updates |

Rules:
- Every concept file, daily session output, and knowledge map section must
  include a freshness tag.
- The Agent must populate `09_sources/freshness_log.md` with each module's
  freshness risk and recommended review date.
- Repository creation chat output must include a Freshness Notice when
  `09_sources/freshness_log.md`, `09_sources/claims_to_verify.md`, or any
  freshness risk metadata exists. The learner must learn the project's
  time-sensitivity status from the chat, not only by opening files.
- When generating content tagged 🔴 Volatile, the Agent must add a
  prominent warning: "This information may be outdated. Verify before use."

See `references/{locale}/freshness-policy.md` for the full policy.

### High-Stakes Domain Policy

Some domains carry elevated risk if the learner relies on incorrect
information. High-stakes domains include but are not limited to:

- **Medical / Health**: diagnosis, treatment, pharmacology
- **Legal**: regulations, compliance, contracts
- **Financial**: investment, tax, accounting
- **Safety-Critical**: aviation, nuclear, cybersecurity
- **Professional Certification**: CPA, bar exam, medical boards

Rules:
- At intake, if `{domain}` falls into a high-stakes category, the Agent
  MUST add a disclaimer to the top of the learning repository README:
  ```
  ⚠️ EDUCATIONAL USE ONLY — This repository is AI-generated learning
  material for {domain}. It is NOT a substitute for professional advice,
  official guidelines, or accredited training. Always verify critical
  information with authoritative sources before applying it.
  ```
- The Agent must prioritize Primary sources (official guidelines, textbooks,
  accredited course materials) and explicitly flag any claim not backed by
  a Primary source.
- The Agent must never present its output as professional advice.

See `references/{locale}/high-stakes-domain-policy.md` for the full policy.

### No Source, No Claim Rule

The Agent must never fabricate any of the following:
- URLs, DOIs, or hyperlinks to papers, documentation, or websites
- Publication dates, version numbers, or benchmark results
- Author names, institutional affiliations, or expert quotes
- Statistics, percentages, or numerical data presented as factual

If the Agent wants to reference a specific resource:
1. **With web access**: Search, verify the URL exists, then cite.
2. **Without web access**: Describe the resource by name and type (e.g.,
   "the official Python documentation for asyncio") without fabricating a
   URL. Mark with `[unverified — verify URL before use]`.

All claims are tracked in `09_sources/claim_ledger.md`.

See `references/{locale}/claim-verification-guide.md` for the full guide.

### No Web Access Fallback Behavior

When the Agent lacks web search or browsing capabilities (e.g., `{agent_type}`
is `generic`, `{web_access}=unavailable`, or the agent's tool set does not
include web access):

1. All generated content is tagged with:
   ```
   ⚠️ Unverified Draft — This content was generated without web access.
   Key claims should be verified against authoritative sources.
   ```
2. A `09_sources/claims_to_verify.md` checklist is populated with every
   factual claim that would benefit from external verification.
3. The learner is instructed to verify claims before relying on them for
   high-stakes decisions.
4. The Agent should recommend specific verification steps (e.g., "Check the
   official React documentation for the current Hook API").
5. The Agent must not invent links, publication dates, current version
   numbers, official documents, papers, or benchmark results to compensate
   for missing web access.
