# Codex / Claude Code Adapter

## Capability Matrix

| Capability | Codex | Claude Code |
|-----------|-------|-------------|
| File Read | ✅ Full | ✅ Full |
| File Write | ✅ Full | ✅ Full |
| Shell Commands | ✅ Full | ✅ Full |
| Project Rules File | `AGENTS.md` | `CLAUDE.md` + `AGENTS.md` |
| Global Rules File | N/A | `~/.claude/CLAUDE.md` |
| Native Skill Format | `SKILL.md` | `SKILL.md` |
| Context Window | Large (200K+) | Large (200K+) |

## Rule File Setup

### For Codex Users

Copy the rule file to your learning repository:

```bash
cp skills/codex/domain-learning-master/AGENTS.md ./AGENTS.md
```

Codex reads `AGENTS.md` at the start of each session in the project directory.

### For Claude Code Users

**Option A — Project-level (recommended for learning repos):**

Claude Code reads `CLAUDE.md` from the project root. Use the template:

```bash
cp skills/codex/domain-learning-master/CLAUDE.md ./CLAUDE.md
```

**Option B — Global (applies to all projects):**

Add the learning principles to `~/.claude/CLAUDE.md` so Claude Code always acts as a learning engineer when appropriate.

**Option C — Both (dual setup):**

If you use both Codex and Claude Code, maintain both files with equivalent content:

```bash
cp skills/codex/domain-learning-master/AGENTS.md ./AGENTS.md
cp skills/codex/domain-learning-master/CLAUDE.md ./CLAUDE.md
```

### AGENTS.md vs CLAUDE.md

| Aspect | AGENTS.md | CLAUDE.md |
|--------|-----------|-----------|
| **Primary consumer** | OpenAI Codex | Anthropic Claude Code |
| **Scope** | Project-level only | Global (`~/.claude/`) or project-level |
| **Layering** | Single file | Global + project-level stack, project wins on conflict |
| **Format** | Markdown | Markdown |
| **Recommended for** | Codex-only users | Claude Code users; dual users maintain both |

## Native Skill Setup

For Codex/Claude Code, you can register `domain-learning-master` as a native Skill:

```bash
# Copy the skill directory to your skills folder
cp -r skills/codex/domain-learning-master ~/.codex/skills/
# or for Claude Code:
cp -r skills/codex/domain-learning-master ~/.claude/skills/
```

Then invoke with: `/domain-learning-master`

## Recommended Workflow

1. **Initialize**: Navigate to your workspace, start the agent, say:

   ```
   Read learn-anything-skill/core/prompts/init-repo.md,
   then execute it for {domain} = AI Agent, {background} = beginner programmer.
   ```

2. **Daily learning**: Each day, say:

   ```
   Read progress.md and execute today's learning session
   using learn-anything-skill/core/prompts/daily-session.md.
   ```

3. **Stage test**: Every 7 days:

   ```
   Use learn-anything-skill/core/prompts/stage-test.md
   to test me on the past 7 days of learning.
   ```

## Known Limitations

- None significant. Codex and Claude Code have the richest capabilities and are the primary target platforms for this Skill Pack.
- If using a custom SKILL.md at the root level, note that Codex loads skills from registered skill directories, not from arbitrary paths.
