# Changelog

## [0.2.1-beta] — 2026-06-12

Release notes: [docs/release-notes-v0.2.1-beta.md](./docs/release-notes-v0.2.1-beta.md)

### Added
- Guided Learning Mode: newly created learning repositories now default to starting Day 1 immediately in the chat instead of stopping after a file list.
- Beginner-friendly Day 1 entry files: `START_HERE.md`, `TODAY.md`, and `07_daily_review/day-01.md`.
- Bilingual guided-session prompts, templates, references, examples, and eval coverage.
- Harness contract and check script for Guided Learning Mode.

### Changed
- Repository initialization prompts and scripts now include the guided Day 1 entry files.
- README, Quick Start, generated repository rules, and major adapters now describe the create repo -> start guided session flow.
- Daily session and review prompts now require a copyable answer template and only update `progress.md` after the learner completes the task.

### Fixed
- The default product experience no longer leaves beginner users at a file list after repository creation.
- Scaffold-only behavior remains available only for explicit requests such as `scaffold only`, `generate files only`, `只创建项目`, or `不要开始学习`.

## [0.2.0-beta] — 2026-06-12

Release notes: [docs/release-notes-v0.2.0.md](./docs/release-notes-v0.2.0.md)

### Added
- Full zh-CN locale support (13 Chinese prompt modules)
- Claude Code adapter (`adapters/claude-code.md`)
- ChatGPT adapter (`adapters/chatgpt.md`)
- Generic agent adapter (`adapters/generic-agent.md`)
- `{duration}` variable for configurable learning period
- `{interface_language}` / `{learning_language}` dual-language support
- `scripts/detect_language.py` — language detection
- `scripts/check_untranslated_strings.py` — localization validation
- `scripts/init_learning_repo.py` — Python-native cross-platform scaffolding
- `scripts/validate_locale.py` — Heuristic language bleed detection
- `scripts/generate_index.py` — Dynamic repository index generation
- `scripts/export_flashcards.py` — Anki-compatible CSV flashcard export
- `evals/run_e2e_evals.py` — Mock end-to-end learning loop evaluation runner
- Eval test suites for both en-US and zh-CN
- Chinese example: `examples/zh-CN/learn-ai-agent/`
- `.github/workflows/ci.yml` — GitHub Actions CI
- `CLAUDE.md` templates for generated learning repositories
- `ROADMAP.md` and v0.2.0-beta release notes
- Acceptance record documenting manual/live-agent verification limits
- `--dry-run` support for repository scaffolding scripts

### Changed
- Renamed adapter files: `codex-adapter.md` → `codex.md`, etc.
- Moved legacy adapters to `adapters/legacy/`
- Unified variable names across all prompts: `{language}` → `{interface_language}` / `{learning_language}`
- `scripts/new-domain.sh` — cross-platform sed (macOS + Linux)
- Updated `docs/user-guide.zh-CN.md` with current paths and adapter names
- Claude Code and Cursor support wording now reflects documented workflows rather than unverified full automation

### Fixed
- zh-CN prompts: `{daily_time}` / `{duration}` variable confusion
- Template READMEs: `your-org` placeholder → actual org
- `adapters/claude-code.md`: removed hardcoded local path
- `SKILL.md`: narrowed the trigger description, added non-trigger cases, and replaced the legacy concept-template path
- `adapters/cursor.md`: removed legacy wrapper installation instructions
- `core/prompts/*/init-repo.md`: scaffold output now includes `CLAUDE.md`
- `core/prompts/zh-CN/concept-breakdown.md`: aligned concept file naming with the ASCII filename rule
- `evals/README.md`: clarifies that behavior evals are policy checks, not proof of live agent behavior

## [0.1.0-dev] — 2026-06-08

### Added
- Initial repository skeleton
- 12 core prompts covering the full learning lifecycle (en-US)
- Standard learning repository template
- Codex/Claude Code native Skill definition
- Reference docs: learning principles, error types, project patterns
- Example: learn-ai-agent (en-US)
- Scripts: new-domain.sh, validate-repo.sh
- User documentation (quick-start, user guide)
