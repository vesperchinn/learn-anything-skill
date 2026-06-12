# Quick Start Guide

From zero to your first learning repository in 5 minutes.

## Prerequisites

- An AI agent with file read/write capability (Claude Code or Codex recommended)
- A domain you want to learn

## Step 1: Clone the repo

```bash
git clone https://github.com/vionlabs/learn-anything-skill.git
cd learn-anything-skill
```

## Step 2: Create your learning repository

**Using the script (recommended)**:
```bash
./scripts/new-domain.sh "AI Agent"
cd learn-ai-agent
```

**Manual**: Copy the template from `templates/en-US/{{domain-slug}}/` to your
working directory.

## Step 3: Tell your agent to get started

Start your AI agent in the directory, then say:

```
Read learn-anything-skill/core/prompts/en-US/init-repo.md.
Create a learning repository for "AI Agents".
My background: beginner programmer, 2 hours/day, goal is to build a project in 30 days.
```

The agent will scaffold all the files. Then:

```
Read learn-anything-skill/core/prompts/en-US/knowledge-map.md.
Generate the knowledge map for AI Agents. Write it to 00_domain_map.md.
```

## Step 4: Daily learning

Each day, open the directory and tell your agent:

```
Read progress.md, then read learn-anything-skill/core/prompts/en-US/daily-session.md.
Run today's learning session.
```

After the session:

```
Read learn-anything-skill/core/prompts/en-US/daily-review.md.
Run today's review.
```

## Step 5: Stage test (Day 7)

```
Read learn-anything-skill/core/prompts/en-US/stage-test.md.
Give me the stage test. Present all questions first, wait for my answers, then grade.
```

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
