# Platform Adapter Layer

`platforms/` contains distribution adapters for Agent platforms that cannot consume the native Codex `SKILL.md` directly.

The native Codex Skill remains in `SKILL.md` and `skills/codex/`. Platform adapters must not require a platform to read `SKILL.md`; they should package the platform-neutral protocols, prompts, knowledge-base documents, workflow steps, variables, memory schemas, and test checklists in the format that platform expects.

## Directory map

| Path | Target |
| --- | --- |
| `cn/coze/` | Coze bot, knowledge base, workflow, variables, memory, publishing checklist |
| `cn/workbuddy/` | Office task Skill package for file processing, study material handling, and report output |
| `cn/trae/` | File-based engineering Agent that can read repository files |
| `cn/codebuddy/` | Code/document Agent with uploaded knowledge-base packages |
| `cn/generic-lowcode-agent/` | Generic Chinese low-code Agent builders |
| `global/chat-only/` | Chat-only agents with no file or workflow support |
| `global/file-agent/` | Agents with file read/write support |
| `global/rag-workflow-agent/` | Agents with retrieval and workflow support |

## Adapter rule

Every adapter must preserve:

- Learning loop: intake, map, plan, learn, practice, deliver, assess, diagnose, review, project
- Material-grounded learning when user materials exist
- Source records, freshness checks, and anti-hallucination rules
- Fallback behavior for no file read, no file write, no web, no workflow, or no memory
- Locale separation between `zh-CN` and `en-US`

## Canonical core files

Use these files as the platform-neutral source:

- `core/learning-protocol.{locale}.md`
- `core/reliability-protocol.{locale}.md`
- `core/material-grounding-protocol.{locale}.md`
- `core/state-schema.{locale}.md`
- `core/output-contract.{locale}.md`

