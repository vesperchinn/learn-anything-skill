# GitHub Copilot Adapter

## Capability Matrix

| Capability | Support |
|-----------|---------|
| File Read | ✅ Full |
| File Write | ✅ Full |
| Shell Commands | ⚠️ Limited (via terminal suggestions) |
| Project Rules File | `.github/copilot-instructions.md` |
| Context Window | Moderate |

## Setup

Copy the learning rules:

```bash
mkdir -p .github
cp skills/codex/domain-learning-master/AGENTS.md ./.github/copilot-instructions.md
```

## Key Differences

- Copilot's instructions file is in `.github/copilot-instructions.md` (GitHub-specific path)
- Copilot is more code-focused; for non-code domains, explicit prompting is needed
- Copilot Chat (in VS Code) is the best interface for learning sessions
- Shell commands require manual execution

## Recommended Workflow

1. Open the learning repository in VS Code with Copilot enabled
2. In Copilot Chat, reference the core prompts:

   ```
   Read learn-anything-skill/core/prompts/daily-session.md
   and execute today's session.
   ```

3. Copilot will read the prompt, understand the instructions, and work within your repository

## Limitations

- Copilot's context window is smaller than Codex/Cursor. For sessions with many files, manually specify which files to read.
- Shell automation is limited. Run scripts manually in the VS Code terminal.
