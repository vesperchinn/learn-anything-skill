# Codex Adapter

## Capability Matrix

| Capability | Support |
|-----------|---------|
| File Read | ✅ Full |
| File Write | ✅ Full |
| Shell Commands | ✅ Full |
| Project Rules | `AGENTS.md` |
| Native Skill | `SKILL.md` via `~/.codex/skills/` |
| Context Window | Large (200K+) |

## Setup

**Option A — Register as a native Skill (recommended)**:

```bash
cp -r /path/to/learn-anything-skill ~/.codex/skills/learn-anything
```

Then invoke with:

```
/learn-anything
```

Install the full Skill Pack directory, not only `skills/codex/domain-learning-master`.
The full directory includes `core/prompts/`, `prompts/`, `templates/`,
`references/`, `scripts/`, and evals needed by Knowledge Reliability Layer and
Material-Grounded Learning Mode.

**Option B — Point Codex at the Skill Pack**:

```
Read learn-anything-skill/SKILL.md and follow its workflow to help me learn {domain}.
```

## Usage

### Start a new domain

```
I want to learn AI Agent. My background: beginner programmer.
Daily time: 2 hours. Goal: build a project.
```

Codex reads `SKILL.md`, runs the intake → scaffold → map → plan pipeline.
It creates files directly in the working directory and can run
`scripts/new-domain.sh "AI Agent"` for instant scaffolding.

### Learn from PDFs, slides, or documents

```
Create a learning repo from ./materials/*.pdf and ./materials/week1.pptx.
Use Material-Grounded Learning Mode.
```

Codex can read local files, copy originals into `learning_materials/raw/`,
extract readable text into `learning_materials/extracted/`, and build
`material_manifest.md`, `material_index.md`, `material_coverage_map.md`, and
`material_learning_plan.md`.

For PDFs/PPTs, Codex must mark charts, screenshots, tables, diagrams, and
flowcharts in the material index. If extraction fails or a scanned page needs
OCR, it records an unresolved issue in `learning_materials/extraction_issues.md`
instead of guessing.

Outside explanations must be labeled `Supplemental`.

### Daily session

```
Day 5. Read progress.md and run today's session.
```

Codex reads `progress.md`, finds today's concepts, executes the
learn → practice → output → test cycle, and updates progress.md.

### Stage test (every 7 days)

```
Run the stage test for days 1–7.
```

### Interrupted? Resume

```
I'm back after a week. Help me resume.
```

Codex reads `progress.md` + recent `progress-log.md` entries,
reconstructs state, and proposes a recovery path.

## Key Differences from Other Agents

- **Full automation**: Codex can scaffold the repo, write all files, run validation scripts, and execute code — zero manual file management.
- **AGENTS.md**: Codex reads `AGENTS.md` at session start. The scaffold phase writes this file with domain-specific teaching rules.
- **Skill chaining**: Codex can read `core/prompts/en-US/*.md` on demand, so SKILL.md stays lean.

## Teaching Loop Enforcement

Codex follows the Skill Pack's **explain → example → practice → check → review**
loop automatically because `AGENTS.md` encodes it as a hard rule. Every session
the agent reads `progress.md`, checks weak points, teaches 3 concepts (each with
all 5 required parts), administers 5 quiz questions, and assigns a ≤ 60-minute
deliverable task with acceptance criteria.

## No-Code Users

If the learner cannot code, Codex adapts project designs to no-code alternatives
automatically (design specs, manual workflows, curated datasets, spreadsheet
templates) per the No-Code Rule in SKILL.md.
