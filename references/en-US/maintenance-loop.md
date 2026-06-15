# Maintenance Loop

Maintenance Loop is a maintainer-only safety loop for changing this Skill Pack.
It is not a learner feature and must not change the default behavior of Guided
Learning Mode, Interactive Beginner Lesson Mode, or Material-Grounded Learning
Mode.

## Boundary

- Use this loop for developer maintenance, Codex edits, release review, and
  multi-file change closure.
- Do not use it inside ordinary learner sessions.
- Do not add default learner loops, default extra conversation rounds, or
  default token cost.
- Do not continue a learner session without explicit user consent.
- Do not present this loop as a user-facing selling point.

## Loop Definition

1. Change Intake
2. Impact Analysis
3. Contract Check
4. Related Eval Check
5. Harness Check
6. Risk Classification
7. Release Scope Freeze
8. Human Confirmation
9. Commit / Release

## Change Intake

Classify the current change before editing or release review:

- SKILL.md change
- prompt change
- template change
- eval change
- harness change
- README / docs change
- platform adapter change
- reliability layer change
- material-grounding change
- release-only change

## Impact Analysis

Use `harness/architecture/change-impact-matrix.md` as the source map.

Required impact review:

| Change type | Required review |
| --- | --- |
| SKILL.md change | prompts, README, evals, adapters |
| prompt change | templates, examples, evals |
| template change | init scripts, examples, harness |
| reliability layer change | freshness notice, claim ledger, evals |
| material-grounding change | material prompts, templates, examples, evals |
| platform adapter change | capability matrix, platform package docs |
| README / docs change | bilingual sync and actual behavior consistency |

## Required Checks

Every maintenance round must run:

```bash
python3 harness/scripts/run_all_checks.py --root . --report
```

Run targeted checks when the changed area requires them:

```bash
python3 harness/scripts/check_guided_learning_mode.py --root . --report
python3 harness/scripts/check_freshness_notice.py --root . --report
python3 harness/scripts/check_material_grounding.py --root . --report
python3 harness/scripts/check_platform_adapters.py --root . --report
```

## Scope Freeze

Before release, freeze the version scope:

- List tracked modified files.
- List untracked new files.
- Classify files included in this version.
- Classify files excluded from this version.
- Pause for human confirmation on uncertain files.
- Do not tag or release while scope is unsettled.

## Commit Gate

Before commit, confirm:

- No sensitive files.
- No temporary learning projects.
- No `harness/reports/*.json`.
- No `.env`, token, or secret.
- No PDF/PPT/Word raw materials.
- No leaked local absolute paths.
- Staged files belong to the version scope.

## Release Gate

Before tag or release, confirm:

- Worktree is clean, or unpublished changes are stashed and documented.
- Tag does not already exist.
- `RELEASE_NOTES.md` is updated.
- `CHANGELOG.md` is updated.
- Harness status has no `FAIL`.
- `READY_WITH_WARNINGS` has a human explanation.
- A messy or unreviewed worktree blocks release.

## Risk Classification

- Low: docs-only change with clear bilingual parity and no behavior change.
- Medium: prompt, template, eval, adapter, or harness change with bounded scope.
- High: SKILL.md, release gate, reliability, material-grounding, or platform
  behavior change.
- Blocked: uncertain scope, unreviewed files, missing checks, missing warning
  explanation, existing tag conflict, sensitive material, or dirty release state.

## Release Scope Closure

Use this closure before release:

```text
Tracked changes:

Untracked files:

Included in this version:

Excluded from this version:

Uncertain files requiring human confirmation:

Harness status:

READY_WITH_WARNINGS explanation, if any:
```

Release remains blocked until every uncertain file is classified and every
warning has a human explanation.
