# Windsurf Adapter

## Capability Matrix

| Capability | Support |
|-----------|---------|
| File Read | ✅ Full |
| File Write | ✅ Full |
| Shell Commands | ✅ Full |
| Project Rules File | `.windsurfrules` |
| Context Window | Large |

## Setup

Copy the learning rules:

```bash
cp skills/codex/domain-learning-master/AGENTS.md ./.windsurfrules
```

## Key Differences

- Windsurf uses `.windsurfrules` (note the spelling: "windsurf" + "rules")
- Cascade mode provides the best multi-step reasoning for daily sessions

## Recommended Workflow

Same as Codex. Direct Windsurf to read from `core/prompts/`.
