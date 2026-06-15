# Release Gates

## Gate 1: Structure Gate

All core directories exist. No empty files or obvious placeholders remain.

## Gate 2: Skill Gate

`SKILL.md` is valid, has required metadata and sections, and does not exaggerate guarantees.

## Gate 3: Locale Gate

`en-US` and `zh-CN` are basically aligned, with no obvious language residue.

## Gate 4: Learning Loop Gate

Learning loop files, prompts, templates, and evals exist and remain consistent.

## Gate 5: Reliability Gate

Source records, claim ledger, freshness log, no-web fallback, and high-stakes policies exist.

## Gate 6: Material Gate

User material intake, material manifest, material index, coverage map, and PDF/PPT rules exist.

## Gate 7: Platform Gate

All declared platforms have adapters, fallback notes, and test checklists or equivalent review docs.

## Gate 8: Eval Gate

Core evals exist and cover meaningful behavior, not only file existence.

## Gate 9: Safety Gate

Privacy, copyright, high-stakes, and dangerous-command checks pass.

## Gate 10: Maintenance Loop Gate

For maintainer-side changes, run the Maintenance Loop:

- Change Intake
- Impact Analysis
- Contract Check
- Related Eval Check
- Harness Check
- Risk Classification
- Release Scope Freeze
- Human Confirmation
- Commit / Release

This gate is maintainer-only. It must not change ordinary learner sessions,
Guided Learning Mode, Interactive Beginner Lesson Mode, Material-Grounded
Learning Mode, or default learner token cost.

Before release, scope freeze must list tracked modified files, untracked files,
files included in this version, files excluded from this version, and uncertain
files requiring human confirmation. Tag and release are blocked while scope is
unsettled, while the worktree is messy, or while unreviewed changes exist.

`READY_WITH_WARNINGS` is not a clean release state. It requires a human
explanation before release.

## Gate 11: Release Gate

README, license, roadmap, changelog, version notes, and release notes are present.

Before tag or release, confirm `CHANGELOG.md` and `RELEASE_NOTES.md` are
updated, the tag does not already exist, the worktree is clean or unpublished
changes are stashed, and harness status has no `FAIL`.
