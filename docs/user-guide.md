# User Guide

The complete manual for the Learn Anything Skill Pack.

## Table of Contents

1. [Core Concepts](#core-concepts)
2. [Detailed Learning Flow](#detailed-learning-flow)
3. [Prompt Usage Guide](#prompt-usage-guide)
4. [Progress Tracking](#progress-tracking)
5. [Error Diagnosis](#error-diagnosis)
6. [Project Design](#project-design)
7. [Cross-Agent Usage](#cross-agent-usage)
8. [FAQ](#faq)

## Core Concepts

The goal of the Learn Anything Skill Pack is to turn your AI Agent into a "Domain Learning Engineer". Rather than just lecturing you with facts, it helps you build an **executable, iterative, and reviewable learning system**.

### Five Systems

```
Knowledge Map → Glossary → Practice System → Project System → Review System
```

### Learning Rhythm

- **Daily**: Learn 3 concepts → 5 quiz questions → 60-minute task → review
- **Weekly**: Stage test (10 multiple choice + 5 concepts + 3 scenarios + 1 comprehensive)
- **Final**: Complete a demonstrable minimal project in 7 days

### Three Levels of Knowledge

- **20% Must know first**: Gatekeeper concepts
- **60% Skip for now**: Details you won't use immediately
- **20% Deep dive later**: Revisit after completing a project

## Detailed Learning Flow

> Prompt files are organized by language. English users use `core/prompts/en-US/`, Chinese users use `core/prompts/zh-CN/`. The placeholder `{locale}` is used below to represent your language choice.

### Phase 0: Initialization (Day 0)

Use `core/prompts/{locale}/init-repo.md` to create the learning repository. The Agent will generate:
- Standardized directory structure (10 directories + core files)
- README.md (Repository usage instructions)
- AGENTS.md (Agent behavioral rules)
- progress.md (Progress snapshot template)

### Phase 1: Knowledge Map (Day 0)

Use `core/prompts/{locale}/knowledge-map.md` to generate the domain landscape:
- Domain definition and Feynman explanation
- Top 20 core concepts
- Concept relationship graph
- 20-60-20 classification
- Easily confused concepts comparison
- Minimum Viable Knowledge (MVK) checklist

### Phase 2: Concept Breakdown

Use `core/prompts/{locale}/concept-breakdown.md` to generate detailed files for each core concept:
- One-line explanation
- Life analogy
- Technical explanation
- Real-world case
- Exercise

### Phase 3: 30-Day Plan

Use `core/prompts/{locale}/learning-plan.md` to generate the daily schedule.

### Phase 4: Daily Loop (Day 1-30)

Two steps every day:
1. **Learning Session** (`core/prompts/{locale}/daily-session.md`): Review → learn new concepts → practice → 60-minute task
2. **Daily Review** (`core/prompts/{locale}/daily-review.md`): Summarize → error analysis → update progress → plan tomorrow

### Phase 5: Stage Test (Every 7 Days)

Examiner Mode — The Agent becomes a strict examiner, asks questions, waits for your answers, then grades and diagnoses.

Use `core/prompts/{locale}/stage-test.md`.

### Phase 6: Project (Final 7 Days)

Use `core/prompts/{locale}/project-design.md` to design a minimal demonstrable project.

## Progress Tracking

### progress.md (Snapshot)
- Must be read by the Agent every time
- Keep ≤ 200 lines
- Contains: Current day, completed modules, weak points, error summary, test scores, project progress, next steps

### progress-log.md (Log)
- Append-only, never delete
- Detailed daily record: Content learned, mastery level, error analysis, review

## Error Diagnosis

When you answer incorrectly, the Agent determines the error type before providing the answer:

| Type | Meaning | Remediation |
|------|---------|-------------|
| Concept Gap | Don't know the concept at all | Revisit definition + analogy |
| Application Failure | Know the concept but can't apply it | Scenario questions + imitation |
| Expression Unclear | Understand it but can't explain it | Feynman output exercise |
| Knowledge Confusion | Mixed up A and B | Comparison table + distinction exercise |

See `core/prompts/{locale}/error-diagnosis.md` for details.

## Project Design

Project standards:
- Executable (not just documentation)
- Demonstrable (can show others)
- Explainable (can explain design decisions)
- Iterative (clear direction for improvement)

See `references/{locale}/project-patterns.md` for 5 project patterns.

## Cross-Agent Usage

| Agent | Adapter Notes |
|-------|---------------|
| Codex | `adapters/codex.md` — Native Skill support |
| Claude Code | `adapters/claude-code.md` — Integrate via CLAUDE.md |
| Cursor | `adapters/cursor.md` — Integrate via .cursorrules |
| ChatGPT | `adapters/chatgpt.md` — Copy/paste prompts |
| Generic Agent | `adapters/generic-agent.md` — Manual prompt copying |

> Legacy adapters have been moved to `adapters/legacy/` and are no longer maintained.

## FAQ

**Q: I paused for a few days, how do I resume?**
A: Use `core/prompts/{locale}/resume-session.md`. The Agent will read progress.md + recent logs to rebuild state.

**Q: What if I fail a stage test?**
A: The Agent will diagnose weak points, generate 3 remedial exercises, reschedule the next 3 days, and re-test after 3 days.

**Q: Can I share the learning repository?**
A: Yes. The entire repository is just Markdown files. Git push or zip it.

**Q: How do I chat in Chinese but keep repo files in English?**
A: Tell the Agent during intake: "Chat with me in Chinese, but use English for learning materials". The Agent will set `{interface_language}=中文` and `{learning_language}=English`.

**Q: What scripts are currently supported?**
A: The `scripts/` directory provides:
- `new-domain.sh` & `init_learning_repo.py` — Scaffolds the learning repository
- `validate-repo.sh` — Validates the learning repository structure
- `validate_locale.py` — Heuristic-based language bleed detection
- `generate_index.py` — Generates an index.md table of contents
- `export_flashcards.py` — Exports flashcards to Anki-compatible CSV
- `detect_language.py` & `check_untranslated_strings.py` — Development and translation tools
