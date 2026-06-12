# Start Guided Session

**Mode**: Guided Learning Mode
**Inputs**: `{project_path}`, `{domain}`, `{user_background}`, `{learning_goal}`, `{daily_time}`, `{duration}`, `{interface_language}`, `{locale}`
**Context needed**: newly created learning repository, especially `TODAY.md`, `START_HERE.md`, `progress.md`, and `07_daily_review/day-01.md`

---

After creating a learning repository, start Day 1 immediately in the chat unless
the user explicitly requested scaffold-only mode with one of the scaffold-only
phrases listed in `SKILL.md`, such as "scaffold only" or "generate files only".

Do not stop after file summary. Do not make opening local files the only first
step. The repository is the long-term asset; the chat is today's classroom.

## Required Response Format

```markdown
Created learning project: {project_path}

You do not need to open the files first. We will start Day 1 now.

## Day 1 Goal

{State in one sentence what the learner should understand or produce today.}

## First understand 3 concepts

### 1. {Concept A}
{Beginner-friendly explanation}
{Life analogy}
{Example connected to the user's goal}

### 2. {Concept B}
{Beginner-friendly explanation}
{Life analogy}
{Example connected to the user's goal}

### 3. {Concept C}
{Beginner-friendly explanation}
{Life analogy}
{Example connected to the user's goal}

## Today's 1-hour plan

| Time | What to do |
|---|---|
| 10 min | Understand the goal and the 3 concepts |
| 20 min | Read the explanations and examples in this chat |
| 20 min | Complete the small task below |
| 10 min | Check your answer against the completion criteria |

## What you must submit today

{One small deliverable that can be completed directly in the chat.}

## Copy this template and reply

```markdown
## My Day 1 Answer

1. The idea I understood best:

2. The idea I am still unsure about:

3. My small deliverable:

4. One example from my own goal or work:

5. My question:
```

## Completion Criteria

- {Criterion 1}
- {Criterion 2}
- {Criterion 3}

After you finish, reply directly with the filled template. I will check it using
the learning project rules and update `progress.md`.
```

## Beginner-Friendly Guided Mode

Enable this when the learner is a beginner, student, non-developer, no-code
learner, content creator, operator, teacher, self-media creator, or explicitly
says they are new.

- Use one main task only.
- Avoid asking the learner to open several Markdown files.
- Avoid code unless the learner explicitly wants coding.
- Prefer everyday analogies and examples from the learner's goal, such as a
  content workflow when the learner is a content creator.
- End with a clear action instruction: "Please fill in the template above and send it to me directly."
