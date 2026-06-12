---
name: domain-learning-master
description: >
  Legacy wrapper only. Do not install this directory by itself. Use the
  repository root learn-anything SKILL.md so core/prompts, prompts, templates,
  references, scripts, and evals are available.
---

# Domain Learning Master Legacy Wrapper

> [!WARNING]
> This directory is not a complete installable Skill package.
>
> Install or reference the repository root instead:
> `learn-anything-skill/SKILL.md`.
>
> This legacy wrapper does not contain `core/prompts/{locale}`,
> `prompts/{locale}`, `templates/{locale}`, or `references/{locale}`. Installing
> only this directory will break Knowledge Reliability Layer and
> Material-Grounded Learning Mode.

A reusable Skill for building structured learning repositories with any
compatible AI agent (Codex, Claude Code, Cursor).

## When to Activate

When the user says:
- "I want to learn X"
- "Help me master Y"
- "Create a learning plan for Z"
- "Continue my learning on X"

## Core Workflow

1. **Intake** → Collect `{domain}`, `{user_background}`, `{daily_time}`,
   `{learning_goal}`, `{final_artifact}`, `{locale}`, `{interface_language}`,
   `{learning_language}`.
2. **Scaffold** → Read `core/prompts/{locale}/init-repo.md`, create from
   `templates/{locale}/`.
3. **Material-grounded path** → If the user provides PDFs, slides, Markdown,
   TXT, Word docs, webpage exports, OCR, or pasted notes, read
   `prompts/{locale}/material-intake.md` and build `learning_materials/` before
   generating lessons.
4. **Knowledge map** → Read `core/prompts/{locale}/knowledge-map.md`, write to
   `00_domain_map.md`.
5. **Concept breakdown** → Read `core/prompts/{locale}/concept-breakdown.md`,
   write to `01_core_concepts/`.
6. **30-day plan** → Read `core/prompts/{locale}/learning-plan.md`.
7. **Daily loop** → Read `core/prompts/{locale}/daily-session.md` +
   `core/prompts/{locale}/daily-review.md`.
8. **Stage tests** → Read `core/prompts/{locale}/stage-test.md` every 7 days.
9. **Capstone project** → Read `core/prompts/{locale}/project-design.md` in
   final week.

## Key Rules

- Always read `progress.md` before any session.
- Always append to `progress-log.md` after any session.
- Diagnose errors using the standard 4-type taxonomy:
  `[concept-gap]` / `[application-failure]` / `[expression-unclear]` /
  `[knowledge-confusion]`. See `references/{locale}/error-types.md`.
- Never lecture without exercises. Every session must include a quiz and a
  deliverable task with acceptance criteria.
- Never reveal quiz answers before the learner submits.
- See `references/{locale}/` for detailed methodology.
- Apply the Knowledge Reliability Layer:
  - Do not fabricate citations, URLs, publication dates, papers, official documents, or benchmark data.
  - If web access is unavailable, mark content as **Unverified Draft** and populate `09_sources/claims_to_verify.md`.
  - Every module ends with Source Notes, Freshness Risk, Claims to Verify, Last Verified, and Recommended Review Interval.
  - Update `09_sources/sources.md`, `claim_ledger.md`, and `freshness_log.md` as modules are generated.
- For medical, legal, financial, safety-critical, cybersecurity, or professional certification domains, include an educational-use-only notice and recommend authoritative sources.
- Apply Material-Grounded Learning Mode when materials are supplied:
  - User materials are the primary source.
  - Do not replace material contents with generic domain knowledge.
  - Label outside additions as `Supplemental`.
  - Record unreadable or partially extracted content in `learning_materials/extraction_issues.md`.
  - Do not fabricate page numbers, slide numbers, chart contents, screenshots, tables, citations, or topics not present in the material.

## Safety

- Do not invent books, papers, citations, or URLs.
- Mark uncertain facts as uncertain.
- For regulated domains, recommend the learner verify with a qualified
  professional.
