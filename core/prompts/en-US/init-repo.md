# Init Learning Repository

**Phase**: 0 — Initialize
**Inputs**: `{domain}`, `{domain_slug}`, `{user_background}`, `{learning_goal}`, `{daily_time}`, `{interface_language}`, `{learning_language}`, `{locale}`
**Context needed**: None
**Typical total tokens**: ~500

---

You are a domain learning engineer. Your task is to create a structured learning repository for mastering a new field.

## Domain Information

- **Domain**: {domain}
- **Background**: {user_background}
- **Learning goal**: {learning_goal}
- **Duration**: 30 days ({daily_time} per day)
- **Interface language**: {interface_language}
- **Learning material language**: {learning_language}
- **Locale**: {locale}

## Task

Create a learning repository in the current directory with the following structure and content. The template system lives at `templates/{locale}/{{domain-slug}}/` — locale-aware templates guide file generation throughout the learning journey.

```
{domain_slug}/
├── README.md                   # How to use this learning repository
├── AGENTS.md                   # Teaching rules for the AI agent
├── CLAUDE.md                   # Equivalent teaching rules for Claude Code
├── 00_domain_map.md            # (placeholder — will be filled by knowledge-map.md)
├── 01_core_concepts/           # (placeholder — will be filled by concept-breakdown.md)
│   └── .gitkeep
├── 02_case_studies/            # Real-world cases and examples
│   └── .gitkeep
├── 03_exercises/               # Practice exercises
│   └── .gitkeep
├── 04_projects/                # Project designs and deliverables
│   └── .gitkeep
├── 05_flashcards/              # Generated knowledge compression cards
│   └── .gitkeep
├── 06_quizzes/                 # Quiz questions and answers
│   └── .gitkeep
├── 07_daily_review/            # Daily review records
│   └── .gitkeep
├── 08_glossary.md              # (placeholder — will grow over time)
├── 09_resources.md             # (placeholder — recommended learning resources)
├── learning_materials/          # user-provided material workspace
│   ├── raw/                     # original PDFs/PPTs/docs/web exports
│   │   └── .gitkeep
│   ├── extracted/               # extracted text, OCR, tables, notes
│   │   └── .gitkeep
│   ├── material_manifest.md     # material registry
│   ├── material_index.md        # page/slide/topic/visual index
│   ├── material_coverage_map.md # learning-module coverage map
│   ├── material_learning_plan.md # plan grounded in materials
│   └── extraction_issues.md     # unresolved extraction issues
├── 09_sources/                 # source, claim, and freshness tracking
│   ├── sources.md              # source registry
│   ├── source_quality_policy.md # source quality rules
│   ├── claim_ledger.md         # factual claim log
│   ├── claims_to_verify.md     # verification checklist
│   └── freshness_log.md        # freshness review tracker
├── progress.md                 # Current state snapshot (≤ 200 lines)
└── progress-log.md             # Full history log (append-only)
```

## Content Requirements

### README.md
Write a README that explains:
1. What this repository is and how to use it
2. The learning methodology (5 systems)
3. Daily routine expectations
4. How to use the AI agent for each phase

### AGENTS.md and CLAUDE.md
Write both `AGENTS.md` and `CLAUDE.md` with equivalent teaching rules:
1. You are my domain learning engineer. The goal is mastering {domain} in 30 days ({daily_time} per day) and completing a demonstrable project.
2. Teaching workflow: Global map first → then local details → then exercises → then output → then review
3. Each concept must include: one-line explanation, life analogy, technical explanation, real case, one exercise
4. No theory-only sessions. Every day must include a deliverable task (≤ 60 minutes)
5. After each session: update progress.md (snapshot, ≤ 200 lines), append progress-log.md
6. Every 7 days: conduct a stage test (use `core/prompts/{locale}/stage-test.md`)
7. When I answer wrong: diagnose the error type before giving the answer — Conceptual misunderstanding, Application gap, Unclear explanation, or Knowledge confusion
8. Adjust the learning plan based on weak points identified in progress.md
9. End goal: guide me to complete a demonstrable capstone project
10. Do not fabricate citations, URLs, publication dates, official documents, papers, or benchmark results
11. Every generated learning module must include Source Notes, Freshness Risk, Claims to Verify, Last Verified, and Recommended Review Interval
12. If there is no web access, mark generated content as Unverified Draft and populate `09_sources/claims_to_verify.md`
13. If the user provides learning materials, treat them as the primary source and use Material-Grounded Learning Mode

### learning_materials/
Create the material-grounding files:

- `raw/`: originals or references to PDFs, PPTs, Markdown, TXT, Word, and webpage exports.
- `extracted/`: extracted text, OCR, tables, speaker notes, and visual descriptions.
- `material_manifest.md`: registry of supplied materials and extraction status.
- `material_index.md`: topic index with page, slide, section, and visual markers.
- `material_coverage_map.md`: map learning modules back to user materials.
- `material_learning_plan.md`: plan built from the supplied materials.
- `extraction_issues.md`: unreadable, missing, or partially extracted content.

Do not fabricate page numbers, slide numbers, chart contents, screenshots,
table values, citations, or material topics. External additions must be marked
`Supplemental`.

### 09_sources/
Create the knowledge reliability files:

- `sources.md`: master source registry for all cited or consulted sources.
- `source_quality_policy.md`: local copy of the source hierarchy and no-fabrication rules.
- `claim_ledger.md`: append-only log of factual claims and verification status.
- `claims_to_verify.md`: checklist for claims needing authoritative verification.
- `freshness_log.md`: module freshness risk and next review dates.

If `{domain}` is medical, legal, financial, safety-critical, cybersecurity, or professional certification related, add an educational-use-only disclaimer to the top of README.md and prioritize authoritative primary sources.

### progress.md (snapshot template)
Create with all 7 required sections. When `{locale}` is `en-US`, use English headings:

- ## Current Status
- ## Completed Modules
- ## Weak Points
- ## Error Summary
- ## Stage Test Scores
- ## Project Progress
- ## Next Steps

### progress-log.md
Initialize as empty with the header: `# Learning Progress Log — {domain}`

## Output

Create all files now. For placeholder files (00_domain_map.md, 08_glossary.md, 09_resources.md), write a brief header in {interface_language} indicating they will be populated in the next phase. For `learning_materials` and `09_sources`, use the files under `templates/{locale}/{{domain-slug}}/` as the template. For .gitkeep files, create them as empty files.
