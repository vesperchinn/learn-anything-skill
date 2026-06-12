# Agent Adapters

Each AI agent has different capabilities. This directory contains
agent-specific instructions for using the Learn Anything Skill Pack.

## Adapter Index

| Adapter | Agent | File I/O | Shell | Best For |
|---------|-------|----------|-------|----------|
| [codex.md](./codex.md) | OpenAI Codex | ✅ | ✅ | Full automation, native Skill support |
| [claude-code.md](./claude-code.md) | Anthropic Claude Code | ✅ | ✅ | Documented workflow, project + global rules |
| [cursor.md](./cursor.md) | Cursor IDE | ✅ | ✅ | Documented workflow, multi-file editing |
| [chatgpt.md](./chatgpt.md) | ChatGPT (web) | ❌ | ❌ | Quick start, no install needed |
| [generic-agent.md](./generic-agent.md) | Any agent | varies | varies | Building custom agents, minimal protocol |

## Capability-Based Routing

If you're unsure which adapter to use, answer these questions:

```
Can the agent read files from disk?    → YES: codex / claude-code / cursor
                                         NO: chatgpt / generic-agent

Can the agent write files to disk?     → YES: codex / claude-code / cursor
                                         NO: chatgpt (manual save)

Can the agent run shell commands?      → YES: codex / claude-code (auto scaffold)
                                         NO: cursor (user runs scripts manually)

Does the agent have a skill system?    → YES: codex / claude-code (/skill-name)
                                         NO: cursor / chatgpt (reference SKILL.md by path)
```

## The Adaptation Principle

All adapters enforce the same teaching contract:

> **Explain → Example → Practice → Check → Review**

The only difference between adapters is **how files get created and state gets tracked**:

| Capability Level | File Strategy | State Tracking |
|-----------------|---------------|----------------|
| Full I/O (Codex) | Agent writes files directly | Agent reads/writes progress.md automatically |
| Documented file workflow (Claude Code, Cursor) | Agent writes files directly when configured with project rules | Agent reads/writes progress.md according to adapter instructions |
| No I/O (ChatGPT, generic agents) | Agent outputs `📁 Save as: path/file` blocks | User pastes progress.md into each session |

## Material-Grounded Learning

When users provide PDFs, PPTs, Markdown, TXT, Word docs, webpage exports, OCR,
or pasted notes, adapters must use Material-Grounded Learning Mode:

- User materials are the primary source.
- Build `learning_materials/material_manifest.md` and `material_index.md` before generating lessons.
- Mark outside additions as `Supplemental`.
- Record unreadable pages, slide images, charts, tables, screenshots, and flowcharts that cannot be extracted in `learning_materials/extraction_issues.md`.
- Never fabricate page numbers, slide numbers, visual contents, citations, or topics not present in the material.

If an agent cannot read files, ask the user to paste text, provide OCR, convert
the file to Markdown/TXT, export slides as text plus images, or accept a
material-processing checklist only.

## Adding a New Adapter

1. Copy the closest existing adapter as a template
2. Fill in: capability matrix, setup, usage, key differences, limitations
3. Ensure the adapter enforces the teaching loop
4. Document the fallback behaviour when capabilities are limited
5. Add a row to the index table above

## Legacy Adapters

Earlier versions of some adapters are archived in [legacy/](./legacy/).
These are superseded by the main adapters listed above and are not actively
maintained.
