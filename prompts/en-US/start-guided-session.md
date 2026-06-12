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

For regular learners, start Day 1 in chat with a short goal, the first concepts,
one task, a copyable answer template, completion criteria, and a note that
`progress.md` will be updated after review.

When Interactive Beginner Lesson Mode is active, use the fixed structure below.

## Beginner Day 1 Output Structure

````markdown
Created learning project: {project_path}

You do not need to open the files first. We will understand Day 1 here.

## Today, learn just one sentence first

{Explain the primary concept in one plain sentence.}

## Put it into your real situation

{Tell one concrete scenario using the learner's background and goal. For content creators, use a content creation workflow.}

## I do

{Give a fully worked example. Show the exact thinking and final answer.}

## Look at a bad example

{Give one bad example. Keep it short and explain plainly why it is hard to use.}

## Now look at a better example

{Give one improved example. Explain what makes it easier to use.}

## Your turn: do one very small task

{Ask for only one workflow step unless the learner is advanced. The task must be doable in 10-15 minutes and answerable directly in chat.}

## Copy this template and reply

```markdown
## My Day 1 Answer

1. My workflow step:

2. What I want this step to produce:

3. One simple way I can tell whether this step worked:

4. What I am still unsure about:
```

After you reply, I will check your answer and update `progress.md`.

Please fill in the template above and send it to me directly.
````

## Interactive Beginner Lesson Mode

Enable this when the learner is a beginner, complete beginner, non-technical
user, student, non-developer, no-code learner, learner with no coding
background, content creator, writer, marketer, operator, teacher, self-media
creator, or explicitly says they are new.

- The first guided session must be self-contained in chat.
- Do not rely on the learner opening Markdown files first.
- Teach one primary concept at a time.
- Do not introduce more than 2 supporting terms in the first session.
- Translate every abstract term into plain language.
- Pair every abstract term with one concrete example from the learner's goal or
  background.
- Provide a fully worked example before asking the learner to do a task.
- Include one bad example and one improved example.
- Use "I do → We do → You do": show, compare together, then ask the learner
  to answer.
- The first task must be small enough to complete in 10-15 minutes.
- The first task must ask for only one workflow step unless the learner is
  advanced.
- For content creators, examples must use content creation workflows.
- Avoid jargon-heavy terms unless immediately explained.
- Do not ask for "criteria", "rubrics", "test cases", "checkpoints", or
  "standards" before showing what they look like.
- End with a copyable answer template.
- End with one clear action instruction: "Please fill in the template above and send it to me directly."
