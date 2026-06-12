# Invariants

- `SKILL.md` remains the native Codex Skill entry point.
- Platform adapters live under `platforms/`, not inside `SKILL.md`.
- All checks are read-only unless a future script explicitly requires `--fix`.
- Scripts must not overwrite files by default.
- Locale directories must remain paired for `en-US` and `zh-CN`.
- Material-grounded learning must not fabricate unread materials, page numbers, slides, charts, or tables.
- Reliability rules must not claim to fully eliminate hallucinations.
- `dist/` is not a source of truth.
- Evals describe expected behavior; they do not implement behavior.
- Examples demonstrate output; they do not define templates.

