# Maintenance Loop Prompt

Audience: Codex and maintainers only.

Do not use this prompt for ordinary learner sessions. Do not change Guided
Learning Mode, Interactive Beginner Lesson Mode, Material-Grounded Learning
Mode, Day 1 behavior, progress behavior, or default user token cost unless a
maintainer explicitly requests that user-facing behavior change.

## Start Maintenance Loop

Use when a maintainer starts a Skill change:

```text
What is changing in this round?
Which module does it belong to?
Which files can it affect?
Which checks are required?
Which user-facing learning flows must remain unchanged?
```

Required output:

```text
Change type:
Impacted modules:
Files likely affected:
Checks to run:
User-flow boundary:
Risk level:
Human confirmation needed:
```

## Pre-commit Loop

Use before staging or commit:

```text
Which files are staged?
Which files are unstaged?
Which files should not be committed?
Is scope freeze required?
```

Required output:

```text
Staged files:
Unstaged files:
Untracked files:
Excluded from this commit:
Scope freeze status:
Blocked files:
Commit allowed:
```

Commit is blocked if the scope is unclear, staged files are outside the version
scope, sensitive files are present, temporary learning projects are present,
`harness/reports/*.json` is staged, raw PDF/PPT/Word materials are staged, or
local absolute paths leak into maintained files.

## Pre-release Loop

Use before tag or release:

```text
What is the version number?
Is CHANGELOG updated?
Is RELEASE_NOTES updated?
Does the tag already exist?
Is the worktree clean?
```

Required output:

```text
Version:
CHANGELOG status:
RELEASE_NOTES status:
Tag status:
Worktree status:
Harness status:
READY_WITH_WARNINGS explanation:
Release allowed:
```

Release is blocked when unreviewed changes exist, the worktree is messy, the
tag already exists, release notes are missing, changelog is missing, harness has
`FAIL`, or `READY_WITH_WARNINGS` lacks a human explanation.

## Post-release Loop

Use after release:

```text
Did the release succeed?
Did the GitHub page update?
Does stash need to be restored?
Does the next TODO need to be created?
```

Required output:

```text
Release result:
GitHub page status:
Stash status:
Next follow-up item:
Follow-up owner:
```
