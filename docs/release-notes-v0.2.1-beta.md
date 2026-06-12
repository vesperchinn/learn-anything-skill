# Guided Learning Mode

This release improves the first-use learning experience.

Previously, after creating a learning repository, the agent could stop after listing generated files. This was not friendly for beginners, students, non-technical users, or content creators.

Now, by default, the agent starts the first guided learning session immediately after creating the repository.

## What changed

- Added Guided Learning Mode.
- Added `START_HERE.md`.
- Added `TODAY.md`.
- Added `07_daily_review/day-01.md`.
- Added guided session prompts for en-US and zh-CN.
- Added beginner-friendly Day 1 output behavior.
- Added scaffold-only exception.
- Added guided learning evals.
- Added harness checks for guided learning behavior.

## New default behavior

After creating a learning repository, the agent must:

- show the repository location
- avoid stopping at a file list
- start Day 1 immediately
- explain today's goal
- introduce 2-3 beginner-friendly concepts
- provide one small task
- provide a copyable answer template
- define completion criteria
- ask the user to reply in the chat

## Scaffold-only mode

If the user only wants files, they can say:

```text
scaffold only
```

or:

```text
只创建项目，不要开始学习
```

## Why this matters

The project is now more useful for beginners and non-technical learners.
Users no longer need to open multiple Markdown files before knowing what to do next.
