# ChatGPT Adapter

## Capability Matrix

| Capability | Support |
|-----------|---------|
| File Read | ❌ None |
| File Write | ❌ None |
| Shell Commands | ❌ None |
| Project Rules | ❌ None |
| Context Window | 8K–128K (model-dependent) |
| Persistent Memory | ⚠️ Partial (ChatGPT Memory feature, unreliable) |

## The Fundamental Shift

ChatGPT cannot touch your file system. This means **you** are the file manager —
ChatGPT is the content engine. For every file the Skill Pack would normally
create, ChatGPT outputs it as a copyable block, and you save it to disk.

This adds ~5 minutes of manual work per session but preserves the full
learning methodology.

## Setup

No installation needed. Just have the Skill Pack files open for reference,
or paste prompt contents directly into ChatGPT.

**Before starting**: Create the directory structure manually:

```bash
mkdir -p learn-{domain}/01_core_concepts
mkdir -p learn-{domain}/02_case_studies
mkdir -p learn-{domain}/03_exercises
mkdir -p learn-{domain}/04_projects
mkdir -p learn-{domain}/05_flashcards
mkdir -p learn-{domain}/06_quizzes
mkdir -p learn-{domain}/07_daily_review
mkdir -p learn-{domain}/learning_materials/raw
mkdir -p learn-{domain}/learning_materials/extracted
mkdir -p learn-{domain}/09_sources
```

Or run the Skill Pack script in your terminal:

```bash
./scripts/new-domain.sh "AI Agent"
```

## Usage

### Start a new domain

Copy `core/prompts/en-US/full-workflow.md`, replace the variables:

```
{domain} → AI Agent
{user_background} → beginner programmer
{daily_time} → 2 hours
{duration} → 30
{learning_goal} → build a project
{final_artifact} → personal research assistant
{interface_language} → English
{learning_language} → English
```

Paste into ChatGPT. It will output every file as a labeled code block:

```
📁 Save as: learn-ai-agent/00_domain_map.md
```markdown
# Domain Map: AI Agent
...
```
```

Save each block to the indicated path.

### Learn from PDFs, slides, or documents

ChatGPT cannot read your local files directly in this adapter. To use
Material-Grounded Learning Mode, provide the material content in the chat:

- paste the relevant text,
- provide OCR output,
- convert PDFs/PPTs/Word docs to Markdown or TXT,
- export slides as text plus images,
- or paste a webpage export.

Then ask:

```
Use Material-Grounded Learning Mode. Treat the pasted material as the primary
source. Build material_manifest.md, material_index.md, material_coverage_map.md,
and material_learning_plan.md as copyable files.
```

ChatGPT must not claim it has read an uploaded/local file unless the file
content is actually available in the conversation. If material is missing, it
should output a material-processing checklist rather than a grounded course.
Any outside explanation must be labeled `Supplemental`.

### Daily session

Copy `core/prompts/en-US/daily-session.md`, replace `{day_number}` → 5, then also
paste the contents of your `progress.md` so ChatGPT knows your current state.

```
Here is my current progress:

[paste progress.md contents]

Now run today's session per the prompt above.
```

ChatGPT outputs: 3 concept blocks → 5 quiz questions → 1 deliverable task.
Answer the questions in the chat. ChatGPT grades them, diagnoses errors,
and outputs the updated `progress.md` for you to save.

### Stage test

Copy `core/prompts/en-US/stage-test.md`. ChatGPT presents the test. You answer in
chat. It grades, diagnoses, and outputs updated progress files.

### Resume after break

Paste your `progress.md` + the last 3 entries from `progress-log.md` into
ChatGPT along with `core/prompts/en-US/resume-session.md`.

## Teaching Loop Enforcement

Even without file I/O, ChatGPT can enforce the **explain → example → practice →
check → review** loop — but **you must prompt it explicitly each time**.
ChatGPT has no persistent `AGENTS.md` or `.cursorrules` to auto-enforce rules.

**Template prompt to start every session**:

```
You are my domain learning engineer per the Learn Anything Skill Pack.

Rules you must follow:
1. Explain: 3 concepts today, each with one-liner, analogy, technical depth, real case, pitfall.
2. Example: Every concept must include a named real-world case.
3. Practice: Give me 5 quiz questions. Do NOT reveal answers until I submit mine.
4. Check: Grade my work against acceptance criteria. Diagnose error type (concept-gap / application-failure / expression-unclear / knowledge-confusion) before giving the correct answer.
5. Review: Output the updated progress.md for me to save. Include a daily review summary.

Never output theory without exercises. Never skip the deliverable task.
```

## Key Workflow: File Generation Pattern

For every file that needs to be created or updated, use this pattern:

```
You: Generate the knowledge map for AI Agent. Output it as a file.
ChatGPT: 📁 Save as: learn-ai-agent/00_domain_map.md
         ```markdown
         # Domain Map: AI Agent
         [full content]
         ```
You: [Saves the file]
```

## Limitations

| Limitation | Mitigation |
|-----------|-----------|
| No persistent state | Paste `progress.md` at the start of every session |
| No auto-enforcement of rules | Paste the template prompt above every time |
| Manual file management | Budget 5 min/session for saving files |
| Context window limits | For large repos, paste only `progress.md` + today's concept files |
| ChatGPT Memory is unreliable | Don't rely on it — files on disk are the source of truth |
| Model may revert to prose-only | Re-paste the rules if it starts lecturing without exercises |

## When to Upgrade

If you find yourself doing this more than a few times, upgrade to an agent with
file system access (Claude Code, Codex, or Cursor). The methodology is identical;
the only difference is whether you or the agent presses "save."
