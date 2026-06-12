# Cursor Adapter

## Capability Matrix

| Capability | Support |
|-----------|---------|
| File Read | ✅ Full |
| File Write | ✅ Full |
| Shell Commands | ✅ Full (via integrated terminal) |
| Project Rules | `.cursorrules` |
| Native Skill | ❌ No skill system — use `.cursorrules` as equivalent |
| Context Window | Large |

## Setup

**Step 1 — Create or open a learning repository**:

Use the root Skill Pack scaffold, not the legacy wrapper under
`skills/codex/domain-learning-master/`:

```bash
python3 /path/to/learn-anything-skill/scripts/init_learning_repo.py "AI Agent" --locale en-US
cd learn-ai-agent
```

**Step 2 — Add Cursor project rules**:

Copy the generated repository rules into `.cursorrules`:

```bash
cp AGENTS.md .cursorrules
```

Cursor reads `.cursorrules` for every conversation in the project. The generated
repository remains the source of truth; update `.cursorrules` from `AGENTS.md`
if the teaching rules change.

**Step 3 — Open the Skill Pack for reference**:

Keep `learn-anything-skill/` accessible in your workspace so Cursor can read
`core/prompts/en-US/*.md` when instructed.

## Usage

### Start a new domain

Open a terminal in Cursor, scaffold the repo:

```bash
./learn-anything-skill/scripts/new-domain.sh "AI Agent" en-US
cd learn-ai-agent
cp AGENTS.md .cursorrules
```

Then in Cursor Chat (Cmd+L):

```
Read learn-anything-skill/SKILL.md. I want to learn AI Agent.
My background: beginner. Daily time: 2 hours. Goal: build a project.
Start with intake and scaffold.
```

Cursor reads the skill workflow, runs intake, and fills in the repository files.
Use **Composer** (Cmd+I) when you need multi-file edits (concept files, quizzes).

### Learn from PDFs, slides, or documents

Put materials in the workspace, then ask Cursor:

```
Read SKILL.md and use Material-Grounded Learning Mode for the files in ./materials.
Build the learning_materials index first.
```

Cursor can work well with Markdown, TXT, HTML exports, and extracted text. For
PDF/PPT files, prefer converting them to Markdown/TXT or exporting slides with
speaker notes before asking Cursor to build lessons. If Cursor cannot read a
file or parse a chart/table/diagram, it must record the issue in
`learning_materials/extraction_issues.md` and ask for OCR or a converted export.

Do not let Cursor replace the material with a generic course; external content
must be labeled `Supplemental`.

### Daily session

In Cursor Chat:

```
Read progress.md and run Day 5 per the learn-anything skill.
```

### Stage test

```
Run the stage 1 test per the learn-anything skill. Be a strict examiner —
present the test, wait for my answers, then grade.
```

### Resume after break

```
I'm back after a gap. Read progress.md and help me resume my AI Agent learning
per the learn-anything skill.
```

## Key Differences from Codex / Claude Code

| Aspect | Codex / Claude Code | Cursor |
|--------|---------------------|--------|
| Rule file | `AGENTS.md` / `CLAUDE.md` | `.cursorrules` |
| Chat vs Composer | Single interface | Chat (Q&A) + Composer (multi-file edits) |
| Skill system | Native `/skill-name` | No skill system — reference SKILL.md manually |
| Auto-read rules | Automatic on session start | Automatic via `.cursorrules` |

**Recommendation**: Use Composer (Cmd+I) for scaffold, concept files, quizzes,
and project design. Use Chat (Cmd+L) for daily Q&A and quick explanations.

## Teaching Loop Enforcement

Cursor follows the **explain → example → practice → check → review** loop
because `.cursorrules` encodes it. The agent:

1. Reads `progress.md` before every session
2. Teaches 3 concepts with all 5 required parts per concept
3. Administers 5 quiz questions (without revealing answers upfront)
4. Grades your deliverable against acceptance criteria
5. Diagnoses errors by type before giving the correct answer
6. Updates `progress.md` and appends `progress-log.md`

## No-Code Users

Same as Codex — Cursor adapts to no-code via `.cursorrules` instructions.
Project designs default to spec documents, workflows, or curated content
when the user cannot code.

## Limitations

- `.cursorrules` has practical length limits. The provided template is concise.
- Cursor's context is oriented toward code files. For non-code domains, tell it
  explicitly to read and write markdown files.
- No native skill invocation. You must reference `SKILL.md` or specific
  `core/prompts/en-US/*.md` files by path in each conversation.
