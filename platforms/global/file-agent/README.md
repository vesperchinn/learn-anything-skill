# File Agent Adapter

Use this adapter for agents that can read and write a workspace but do not use Codex native Skill discovery.

## Package contents

- Core protocol files for the selected locale
- `templates/{locale}/`
- `prompts/{locale}/`
- `references/{locale}/`
- File creation and validation instructions from the native Skill, adapted into regular project rules

## Operating mode

The agent reads the packaged protocol files, creates the learning repository directly, writes source logs, and updates progress files after each session. If web access is missing, it keeps source claims as unverified drafts.

## Required checks

- Do not overwrite existing learner files.
- Keep `progress.md` compact and append history to `progress-log.md`.
- Preserve material IDs and source notes.
- Record extraction issues instead of guessing unreadable content.

