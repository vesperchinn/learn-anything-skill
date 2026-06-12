# Claude Code Adapter

## Capability Matrix

| Capability | Support |
|-----------|---------|
| File Read | ✅ Full |
| File Write | ✅ Full |
| Shell Commands | ✅ Full |
| Project Rules | `CLAUDE.md` (project-level) + `~/.claude/CLAUDE.md` (global) |
| Native Skill | `SKILL.md` via `~/.claude/skills/` |
| Context Window | Large (200K+) |

## Setup

**Option A — Register as a native Skill (recommended)**:

```bash
cp -r /path/to/learn-anything-skill ~/.claude/skills/learn-anything
```

Then invoke with:

```
/learn-anything
```

Install the full Skill Pack directory, not only `skills/codex/domain-learning-master`.
The full directory includes `core/prompts/`, `prompts/`, `templates/`,
`references/`, `scripts/`, and evals needed by Knowledge Reliability Layer and
Material-Grounded Learning Mode.

**Option B — Global rule (applies to all projects)**:

Add to `~/.claude/CLAUDE.md`:

```markdown
## Learn Anything Skill

When I want to learn a new domain, read
/path/to/learn-anything-skill/SKILL.md
and follow its workflow.
```

**Option C — Project-level (per learning repo)**:

Claude Code auto-reads `CLAUDE.md` in the project root. The scaffold phase
writes this file with domain-specific teaching rules. Prefer the generated
learning repository `CLAUDE.md` instead of copying the legacy wrapper files.
If you need a manual starter, copy from the root template set used by the
scaffold workflow, not from `skills/codex/domain-learning-master/`.

```bash
python3 /path/to/learn-anything-skill/scripts/init_learning_repo.py "My Domain" --locale en-US
```

### CLAUDE.md vs AGENTS.md

Claude Code reads `CLAUDE.md` (not `AGENTS.md`) at session start. Both files
are maintained in the Skill Pack with equivalent content:

| File | Consumer | Scope |
|------|----------|-------|
| `AGENTS.md` | OpenAI Codex | Project-level |
| `CLAUDE.md` | Anthropic Claude Code | Global (`~/.claude/`) or project-level; project wins on conflict |

If you use both tools, let the scaffold phase write both files.

## Usage

### Start a new domain

```
I want to learn AI Agent. My background: beginner programmer.
Daily time: 2 hours. Goal: build a project. Follow the learn-anything skill.
```

When configured with this Skill Pack, Claude Code reads the SKILL.md workflow,
runs intake → scaffold → map → plan, creates files in the working directory,
and writes `CLAUDE.md` for future session continuity.

### Learn from PDFs, slides, or documents

```
Use Material-Grounded Learning Mode on ./course/*.pdf and ./slides/*.pptx.
```

Claude Code can read local files and should register them in
`learning_materials/material_manifest.md`, preserve or reference originals in
`learning_materials/raw/`, extract text into `learning_materials/extracted/`,
then build the course from `material_index.md`.

PDF/PPT visual elements such as charts, screenshots, tables, diagrams, and
flowcharts must be marked explicitly. Unreadable scans, missing speaker notes,
or failed table extraction go into `learning_materials/extraction_issues.md`.
External background is allowed only when labeled `Supplemental`.

### Daily session

```
Read progress.md and run today's learning session per the learn-anything skill.
```

Claude Code reads `progress.md`, finds today's concepts, runs the four-part
session, grades your work, and updates progress.

### Stage test

```
Run the stage 1 test per the learn-anything skill.
```

### Resume after break

```
I haven't studied in 2 weeks. Resume my AI Agent learning.
```

Claude Code reads `progress.md` + recent `progress-log.md`, reconstructs state,
warm-up quizzes you on the last session, and proposes a recovery path.

## Key Differences from Codex

| Aspect | Codex | Claude Code |
|--------|-------|-------------|
| Project rules file | `AGENTS.md` | `CLAUDE.md` |
| Global rules | N/A | `~/.claude/CLAUDE.md` (stackable) |
| Skill loading | `~/.codex/skills/` | `~/.claude/skills/` |
| Custom slash commands | `/skill-name` | `/skill-name` |

## Teaching Loop Enforcement

Claude Code enforces the **explain → example → practice → check → review**
loop through `CLAUDE.md` project rules:

1. **Explain**: 3 concepts/day, each with one-liner, analogy, technical depth, real case, pitfall
2. **Example**: Every concept includes a named real-world case
3. **Practice**: 5 quiz questions (2 recall + 2 application + 1 integration) before revealing answers
4. **Check**: Grade against acceptance criteria; diagnose error type before giving the correct answer
5. **Review**: Update `progress.md` snapshot, append `progress-log.md`, generate flashcard

The agent cannot skip exercises — `CLAUDE.md` forbids prose-only sessions.

## No-Code Users

Claude Code automatically offers no-code alternatives when the learner cannot
code. The capstone project phase proposes design specs, manual workflows,
or curated datasets instead of code projects.

## Agent Capability Fallback

Claude Code has file I/O and shell access. Use the generated `CLAUDE.md` plus
the root Skill Pack files as the enforcement layer, and use the no-file fallback
only if a specific environment blocks local file access.
