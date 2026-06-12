# Release Notes: v0.2.1-beta

v0.2.1-beta focuses on the first-minute learning experience after a repository
is created.

## Highlight: Guided Learning Mode

Learn Anything now defaults to guided learning immediately after creating a
learning repository. The agent should no longer stop at a file list. Instead,
it tells the learner where the project was created, explains that they do not
need to open the files first, and starts Day 1 directly in the chat.

The first guided response includes:

- Project location
- A short explanation of what was created
- Today's learning goal
- 2-3 beginner-friendly concept explanations
- One small task that can be completed in chat
- A copyable answer template
- Completion criteria
- A direct instruction to reply in chat
- A note that `progress.md` will be updated after completion

## New Learning Repository Files

Every newly scaffolded learning repository now includes:

- `START_HERE.md` — beginner-friendly orientation
- `TODAY.md` — today's single learning entry point
- `07_daily_review/day-01.md` — Day 1 plan, checking criteria, and review slot

These files are generated in both English and Chinese template packs.

## Beginner-Friendly Defaults

For technical beginners, students, non-developers, no-code learners, content
creators, operators, teachers, self-media creators, and users who describe
themselves as beginners, the agent must:

- Give one main task at a time
- Use familiar examples and life analogies
- Avoid requiring code unless coding is the learning goal
- Avoid asking the learner to open several Markdown files before starting
- Provide a copyable answer template

## Scaffold-Only Exception

The old file-only setup flow still exists, but only when explicitly requested.
Recognized scaffold-only phrases include:

- `scaffold only`
- `generate files only`
- `只创建项目`
- `不要开始学习`

## Validation

This release adds bilingual evals and a dedicated harness check for Guided
Learning Mode. The checks cover:

- Repository creation must not stop after a file summary by default
- Explicit scaffold-only mode must not start Day 1
- Non-technical users must receive beginner-friendly behavior
- Material-grounded learning must start guided learning after material indexing

## Recommended Upgrade

Use this release if you want Learn Anything to feel like an active learning
companion immediately after project creation, especially for beginner and
non-developer users.
