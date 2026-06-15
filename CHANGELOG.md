# Changelog

## [0.2.3-beta] — 2026-06-15

Release notes: [RELEASE_NOTES.md](./RELEASE_NOTES.md)

### Added
- Freshness Notice in repository creation chat output, shown before Day 1 when freshness tracking exists.
- Short, medium, and full Freshness Notice variants for stable, evolving, and high-risk / fast-changing domains.
- Freshness Notice eval coverage for material-grounded learning, no-web / no-retrieval fallback, and latest/current-information traps.
- Freshness Notice harness contract and checker.

### Changed
- High-risk or fast-changing topics now point learners to `09_sources/freshness_log.md` and, when verification is needed, `09_sources/claims_to_verify.md`.
- Stable foundational subjects use a short notice so freshness tracking does not overwhelm Day 1 learning.
- Material-grounded repository creation now keeps Freshness Notice visible while preserving user materials as primary sources and external context as Supplemental.

### Validation
- Freshness Notice check: passed.
- Guided Learning Mode check: passed.
- Full harness: `READY_WITH_WARNINGS`.
- Harness warnings were reviewed and are mainly change-scope review warnings, not Freshness Notice behavior failures.
- English behavior evals: passed.
- Chinese behavior evals: passed.

## [0.2.2-beta] — 2026-06-12

Release notes: [RELEASE_NOTES.md](./RELEASE_NOTES.md)

### Fixed
- Interactive Beginner Lesson UX Fix for Guided Learning Mode.
- Day 1 for beginner, non-technical, student, and content-creator learners no longer starts with 3 abstract concepts.
- Interactive beginner sessions now follow: one plain-language core idea -> real user scenario -> worked example -> bad/good example -> tiny task -> reply template.
- First tasks now ask for one small workflow step instead of a full multi-step workflow when the learner is a beginner.
- English beginner experience is aligned with the Chinese beginner experience.

### Changed
- `README.md` and `README.zh-CN.md` now document Interactive Beginner Lesson Mode.
- English guided learning example and eval coverage now include a complete beginner content-creation workflow scenario.
- Release validation status: harness is `READY_WITH_WARNINGS`; warnings were manually reviewed and confirmed not to be failures.

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
