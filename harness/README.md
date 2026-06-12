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
python harness/scripts/run_all_checks.py --root . --report
```

## Run one check

```bash
python harness/scripts/check_skill_manifest.py --root . --report
python harness/scripts/check_platform_adapters.py --root . --json
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
2. Run the relevant single checks.
3. Run `run_all_checks.py --root . --report`.
4. Complete `checklists/pr-checklist.md`.
5. Do not merge with unresolved `FAIL` items unless the release owner accepts them.

## Release flow

1. Run all harness checks.
2. Complete `checklists/release-checklist.md`.
3. Review `architecture/release-gates.md`.
4. Verify platform package manifests.
5. Confirm README, changelog, license, examples, evals, safety, privacy, and copyright notes.

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

