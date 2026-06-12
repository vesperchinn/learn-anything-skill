# Generic LLM Adapter

For LLMs without file system access (ChatGPT web, Claude web, Gemini, etc.).

## Capability Matrix

| Capability | Support |
|-----------|---------|
| File Read | ❌ None |
| File Write | ❌ None |
| Shell Commands | ❌ None |
| Context Window | Varies (8K-200K) |
| Instruction Following | ⚠️ Varies by model |

## How to Use

Without file system access, you'll use the Skill Pack as a **manual workflow guide**:

### Phase 0: Initialize

1. Read `core/prompts/init-repo.md` to understand the target directory structure
2. Manually create the directories and files on your local machine
3. Copy `templates/standard/{{domain-slug}}/` as your starting point

### Phase 1-5: Learning Sessions

For each session:

1. Copy the relevant prompt from `core/prompts/`
2. Replace all `{variable}` placeholders with your actual values
3. Paste the prompt into the LLM chat
4. Copy the LLM's output and save it to the appropriate file manually

### Example: Starting a Learning Session

**Step 1**: Copy `core/prompts/knowledge-map.md`

**Step 2**: Replace variables:
```
{domain} → "AI Agent"
{background} → "beginner programmer"
{language} → "Chinese"
```

**Step 3**: Paste into ChatGPT/Claude web

**Step 4**: Copy the output → Save as `00_domain_map.md`

### Manual File System Setup

Since the LLM can't create files, set up your directory structure manually:

```bash
mkdir -p learn-{domain}/01_core_concepts
mkdir -p learn-{domain}/02_case_studies
mkdir -p learn-{domain}/03_exercises
mkdir -p learn-{domain}/04_projects
mkdir -p learn-{domain}/05_flashcards
mkdir -p learn-{domain}/06_quizzes
mkdir -p learn-{domain}/07_daily_review
```

Or use the Skill Pack's script:
```bash
./scripts/new-domain.sh {domain}
```

### Progress Tracking

Without the agent managing progress.md automatically, you must:
1. Update `progress.md` manually after each session
2. Append to `progress-log.md` with date-stamped entries
3. Manually run `scripts/validate-repo.sh` periodically to check consistency

## Known Limitations

- **No state persistence**: The LLM won't remember your progress across sessions. You must re-provide `progress.md` context each time.
- **Manual file management**: All file I/O is on you. This adds ~5-10 min of overhead per session.
- **No shell automation**: Scripts like `new-domain.sh` and `validate-repo.sh` must be run separately in your terminal.
- **Context window**: If the LLM has a small context window (e.g., 8K), use the prompts individually rather than `full-workflow.md`.

## Recommended Workflow

For the best experience with a generic LLM:

1. Use it for **Phase 1 (knowledge map)** and **concept breakdown** — these are content-generation tasks where LLMs excel
2. Use it for **daily Q&A** — paste today's concepts and ask questions
3. Do the file management yourself — the LLM is your content engine, you're the file manager
4. Consider upgrading to a file-access-capable agent (Codex, Cursor, etc.) if you plan to do this regularly
