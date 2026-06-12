# Guided Learning Mode

Guided Learning Mode makes repository creation feel like the start of a class,
not the end of a setup task.

## Default Behavior

After a learning repository is created, the agent starts Day 1 immediately in
the chat. It may mention where files were saved, but it must not stop after a
file list.

The first guided response must include:

- Repository location
- Short explanation of what was created
- "You do not need to open the files first."
- Today's learning goal
- Beginner-friendly explanation of 2-3 concepts
- One small chat task
- Copyable answer template
- Completion criteria
- Instruction to reply in chat
- Note that `progress.md` will be updated after completion

## Scaffold-Only Exception

The agent may stop after file creation only when the user explicitly says:

- "scaffold only"
- "generate files only"

`SKILL.md` also lists the equivalent Chinese scaffold-only phrases.

## Beginner-Friendly Guided Mode

Use this mode for beginners, students, non-developers, no-code learners,
content creators, operators, teachers, self-media creators, and anyone who says
they are new.

Rules:

- Give one main task at a time.
- Use familiar examples and life analogies.
- Avoid sending the learner to several Markdown files.
- Avoid code unless coding is the learning goal.
- Include a copyable answer template every day.
- End with a clear action instruction.
