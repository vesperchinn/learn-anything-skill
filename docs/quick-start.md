# Quick Start Guide

Install the Skill first, then start your first learning project from one chat
message.

## Prerequisites

- An AI agent with file read/write capability (Claude Code or Codex recommended)
- A domain you want to learn

## Step 1: Install it where your agent can read it

The simplest path is to place this repository in a directory your agent can
read:

```bash
git clone https://github.com/vesperchinn/learn-anything-skill.git
cd learn-anything-skill
```

Then connect it based on your agent:

- **Codex / Claude Code / Trae-style file agents**: open this directory or add
  it to the agent-readable workspace.
- **Agents with Skill support**: import this repository as a Skill or place it
  in the Skills directory.
- **Coze, WorkBuddy, CodeBuddy, and other Chinese agent platforms**: follow the
  adapter notes under `platforms/cn/`.
- **Chat-only agents**: copy the prompts from this repository when direct
  installation is not available.

## Step 2: Call it from the chat box

After installation, type:

```
Use learn-anything to create a learning project for "AI Agents".
My background: beginner.
My goal: understand the basics and build a small project in 30 days.
Daily time: 1 hour.
```

If you want to start from your own materials, type:

```
Use learn-anything to create a learning project from my materials.
Prioritize the provided materials and mark anything that still needs verification.
```

If your agent cannot call the Skill by name but can read files, type:

```
Read learn-anything-skill/core/prompts/en-US/init-repo.md.
Create a learning repository for "AI Agents".
```

## Step 3: Daily learning

```
Continue with learn-anything. Read my progress and run today's learning session.
```

After the session:

```
Continue with learn-anything. Review what I learned today and update my progress.
```

For a stage test:

```
Continue with learn-anything. Give me a stage test. Ask questions first, then grade after I answer.
```

## Optional: use the command line

```bash
./scripts/new-domain.sh "AI Agent" en-US
cd learn-ai-agent
```

## Learn from your own materials

If you already have PDFs, slide decks, notes, documentation exports, or pasted
course material, tell the agent where the files are, or put them in your
learning project.

The agent will treat your materials as the primary source and record extraction
issues instead of guessing unreadable PDF/PPT content.

---

That's it. After 30 days, you'll have a complete knowledge repository and a
demonstrable project.

## FAQ

**Q: My agent can't write files. What do I do?**  
A: See `adapters/chatgpt.md` or `adapters/generic-agent.md`. Use the 📁 Save
as blocks to manually create files.

**Q: Can I use ChatGPT?**  
A: Yes, but you'll need to manage files manually. Claude Code or Cursor are
recommended for the full experience.

**Q: 30 days is too long. Can I accelerate?**  
A: You can condense the 30-day plan into fewer days by increasing daily time.
A "fast track" template is planned for a future release.

**Q: Can I learn anything?**  
A: Any structured knowledge domain — programming, philosophy, nutrition,
investing, music theory. If it has core concepts, dependencies, and
exercisable skills, it works.

**Q: Can I chat in Chinese but have the learning repo in English?**  
A: Yes. Set `{interface_language}=中文` and `{learning_language}=English`
during intake. See `SKILL.md` § Language and Locale Policy.
