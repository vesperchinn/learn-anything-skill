# Cursor Adapter

## Capability Matrix

| Capability | Support |
|-----------|---------|
| File Read | ✅ Full |
| File Write | ✅ Full |
| Shell Commands | ✅ Full (via terminal) |
| Project Rules File | `.cursorrules` |
| Context Window | Large |

## Setup

Copy the learning rules to your project as `.cursorrules`:

```bash
cp skills/codex/domain-learning-master/AGENTS.md ./.cursorrules
```

Cursor reads `.cursorrules` automatically for every conversation in the project. The rules define how the agent should teach, test, and track progress.

## Key Differences from Codex

- Cursor uses `.cursorrules` instead of `AGENTS.md`. The content is the same.
- Cursor's chat and composer modes can both follow `.cursorrules`.
- Use **Composer** (Cmd+I) for multi-file operations (generating concept files, quizzes, etc.)
- Use **Chat** (Cmd+L) for Q&A and quick explanations

## Recommended Workflow

Same as Codex. Point Cursor to the core prompts:

```
Read learn-anything-skill/core/prompts/daily-session.md
and execute today's learning session.
```

## Limitations

- Cursor's `.cursorrules` has practical length limits. Keep the rules file concise (the provided template is optimized for this).
- Cursor's context is focused on code files. For non-code domains, explicitly ask it to read markdown files.
