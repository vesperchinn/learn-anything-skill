# Maintenance Harness

Maintenance Harness is the read-only guard layer for `learn-anything-skill`.
It does not add learning features. It helps maintainers understand impact,
check contracts, and catch structural drift before release.

## Why it exists

This project contains prompts, templates, references, examples, platform
adapters, evals, and scripts. A small edit in one area can break another area.
The harness makes those relationships visible and provides local checks that
run without CI or third-party dependencies.

## Directory guide

| Path | Purpose |
| --- | --- |
| `architecture/` | Module map, dependency rules, impact matrix, invariants, release gates |
| `contracts/` | Machine-readable-ish YAML contracts used by checks and reviewers |
| `fixtures/` | Small inputs for manual or future automated checks |
| `checklists/` | Human release and PR checklists |
| `scripts/` | Read-only check scripts |
| `reports/` | Timestamped check reports |
| `ci/` | Local preflight notes only; no CI is wired here |

## Run all checks

```bash
python3 harness/scripts/run_all_checks.py --root . --report
```

## Maintenance Loop

Maintenance Loop is for maintainers only. It does not change ordinary learner
sessions, Guided Learning Mode, Interactive Beginner Lesson Mode,
Material-Grounded Learning Mode, Day 1 behavior, progress behavior, or default
learner token cost.

Use it for:

- Skill maintenance
- Codex edits
- pre-release review
- multi-file change closure
- prompt/template/eval/README/adapter drift prevention

Loop:

```text
Change Intake
→ Impact Analysis
→ Contract Check
→ Related Eval Check
→ Harness Check
→ Risk Classification
→ Release Scope Freeze
→ Human Confirmation
→ Commit / Release
```

Run the dedicated check:

```bash
python3 harness/scripts/check_maintenance_loop.py --root . --report
```

Before release, scope freeze must classify tracked modified files, untracked
files, files included in the version, files excluded from the version, and
uncertain files requiring human confirmation. Release is blocked while scope is
unsettled, while the worktree is messy, or while unreviewed changes exist.
`READY_WITH_WARNINGS` requires a human explanation.

## Run one check

```bash
python3 harness/scripts/check_skill_manifest.py --root . --report
python3 harness/scripts/check_platform_adapters.py --root . --json
```

## Report format

Each issue contains:

- `code`
- `severity`: `PASS`, `WARN`, or `FAIL`
- `file`
- `message`
- `suggested_fix`

Reports are written to `harness/reports/` with timestamped filenames. Existing
reports are never overwritten.

## PR flow

1. Identify changed modules using `architecture/change-impact-matrix.md`.
2. Use the maintainer-only Maintenance Loop when the change touches prompts, templates, evals, README/docs, adapters, harness, reliability, material-grounding, or release files.
3. Run the relevant single checks.
4. Run `run_all_checks.py --root . --report`.
5. Complete `checklists/pr-checklist.md`.
6. Do not merge with unresolved `FAIL` items unless the release owner accepts them.

## Release flow

1. Run the maintainer-only Maintenance Loop.
2. Classify tracked modified files, untracked files, included files, excluded files, and uncertain files.
3. Run all harness checks.
4. Complete `checklists/release-checklist.md`.
5. Review `architecture/release-gates.md`.
6. Verify platform package manifests.
7. Confirm README, changelog, release notes, license, examples, evals, safety, privacy, and copyright notes.

## Add a check script

- Put it in `harness/scripts/`.
- Use only Python standard library unless there is a clear reason.
- Support `--root`, `--json`, `--strict`, and `--report`.
- Default to read-only behavior.
- Return non-zero when `FAIL` issues exist.
- Add it to `run_all_checks.py`.

## Add a platform adapter

1. Add adapter docs under `platforms/`.
2. Add knowledge-base, prompt/rules, workflow or task-flow, state/fallback, and checklist docs.
3. Add platform eval cases.
4. Update `platforms/capability-matrix.md`.
5. Run `check_platform_adapters.py`.

## Add a locale

1. Add matching `core`, `prompts`, `templates`, `references`, and `evals` files.
2. Update locale contracts.
3. Run `check_locale_parity.py`.

## Add an eval

- Place it under `evals/{locale}/`.
- Include cases with concrete input, expected behavior, quality checks, and fail conditions.
- Do not make evals a source of business logic.

## Common failures

- Locale files are not paired.
- README claims exceed what the checks can guarantee.
- Platform docs depend on Codex-only behavior.
- Material-grounded prompts lack no-file-access fallback.
- Reliability templates miss source or freshness fields.
- Placeholder text remains in docs.

## Maintenance principles

- Harness is a guard layer, not a feature layer.
- Scripts are read-only by default.
- Checks should be small and single-purpose.
- `dist/` is generated packaging documentation, not source of truth.
- Examples validate behavior but do not define templates.
- The harness reduces risk; it cannot guarantee zero mistakes.
