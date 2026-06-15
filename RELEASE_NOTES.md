# v0.2.4-beta - Maintenance Loop

This release adds a maintainer-only Maintenance Loop for Skill changes and
pre-release review.

## What changed

- Added a Maintenance Loop contract for:
  - change intake
  - impact analysis
  - contract checks
  - related eval checks
  - harness checks
  - risk classification
  - release scope freeze
  - human confirmation
  - commit / release review
- Added bilingual maintainer references and prompts for:
  - starting a maintenance loop
  - pre-commit review
  - pre-release review
  - post-release review
- Added release scope freeze rules that require maintainers to classify:
  - tracked modified files
  - untracked files
  - files included in the version
  - files excluded from the version
  - uncertain files that require human confirmation
- Added commit and release gates for sensitive files, generated harness reports,
  raw local materials, dirty worktrees, existing tags, and
  `READY_WITH_WARNINGS` explanations.

## User-flow boundary

Maintenance Loop is not a learner feature.

- It does not change ordinary learner sessions.
- It does not change Guided Learning Mode.
- It does not change Interactive Beginner Lesson Mode.
- It does not change Material-Grounded Learning Mode.
- It does not add a default learner loop.
- It does not increase user token cost by default.
- It does not create background automation tasks.
- It does not continue learner sessions without explicit user consent.

## Eval and harness coverage

- Added `harness/scripts/check_maintenance_loop.py`.
- Added `harness/contracts/maintenance-loop-contract.yaml`.
- Added Maintenance Loop eval cases for:
  - maintainer-only boundary
  - release scope freeze
  - dirty worktree release block
  - `READY_WITH_WARNINGS` explanation
- Added Maintenance Loop coverage to the executable behavior eval runner.
- Added Maintenance Loop to the full harness check list.

## Validation

- Maintenance Loop check: passed.
- Full harness: `READY_WITH_WARNINGS`.
- The remaining warnings were reviewed as change-scope review warnings caused by
  the current maintenance changes, not Maintenance Loop behavior failures.
- English behavior evals: passed.
- Chinese behavior evals: passed.

## Release note

This release is intended as a maintenance safety release. It helps maintainers
close change scope before commit or release, but it does not introduce any
default learner-facing loop or hidden background automation.
