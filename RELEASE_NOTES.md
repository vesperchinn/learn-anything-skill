# v0.2.2-beta - Interactive Beginner Lesson UX Fix

This release is a Guided Learning Mode beginner teaching experience fix.

It improves the first Day 1 chat session for beginners, complete beginners,
non-technical users, students, content creators, writers, marketers, teachers,
and learners with no coding background.

## What changed

- Day 1 no longer starts with 3 abstract concepts for beginner learners.
- Interactive Beginner Lesson Mode now uses this structure:
  - one plain-language core idea
  - real user scenario
  - worked example
  - bad example and better example
  - tiny task
  - copyable reply template
- The first beginner task asks for one small workflow step instead of a full
  multi-step workflow.
- Content creator examples now use content creation workflows.
- English beginner behavior is aligned with the Chinese beginner behavior.
- `README.md` and `README.zh-CN.md` now describe the beginner interactive
  lesson flow.
- English examples and eval coverage now include a complete beginner content
  creation workflow scenario.

## Validation

- Guided Learning Mode check: passed.
- Full harness: `READY_WITH_WARNINGS`.
- Harness warnings were manually reviewed and confirmed not to be failures.
- English behavior evals: passed.
- Chinese behavior evals: passed.

## Scaffold-only behavior

Scaffold-only mode is unchanged. If the user only wants files, they can say:

```text
scaffold only
```

or:

```text
只创建项目，不要开始学习
```
