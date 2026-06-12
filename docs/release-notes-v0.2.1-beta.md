# Release Notes: v0.2.1-beta

v0.2.1-beta improves the product experience after creating a learning
repository.

## Guided Learning Mode

After creating a learning repository, the default behavior is now:

```text
Create repo -> show project location -> start Day 1 in chat -> give one task -> wait for the learner's answer -> update progress.md
```

The agent must not stop after listing generated files unless the user explicitly
asks for scaffold-only mode.

The Day 1 chat response includes:

- Project location
- A short explanation of what was created
- "You do not need to open the files first." or the localized equivalent
- Today's learning goal
- 2-3 beginner-friendly concept explanations
- One small task that can be completed directly in chat
- A copyable answer template
- Completion criteria
- A direct request for the learner to reply in chat
- A note that `progress.md` will be updated after completion

## New Repository Entry Files

New learning repositories now include:

- `START_HERE.md`
- `TODAY.md`
- `07_daily_review/day-01.md`

These files make the first day usable without asking the learner to inspect a
folder full of Markdown files.

## Scaffold-Only Mode

File-only setup is still supported when explicitly requested with:

- `scaffold only`
- `generate files only`
- `只创建项目`
- `不要开始学习`

## Validation

Added:

- `evals/en-US/guided_learning_cases.yaml`
- `evals/zh-CN/guided_learning_cases.yaml`
- `harness/contracts/guided-learning-contract.yaml`
- `harness/scripts/check_guided_learning_mode.py`

The release was validated with:

- Total harness
- Guided Learning Mode harness
- English and Chinese behavior evals
- Real temporary repository smoke test
