# Platform Capability Matrix

Capabilities vary by product version, workspace policy, connector setup, and user permissions. This matrix describes the intended adapter design, not a guarantee that every installation has every feature.

| Platform | Region | Primary form | Reads repo files | Writes files | Knowledge base | Workflow | Memory/variables | Web access | Main fallback |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Codex native Skill | Global | `SKILL.md` + repo files | Yes | Yes | Repo references | Scripts/shell | Files | Depends on session | Use existing no-filesystem prompt blocks only when needed |
| Coze | CN | Bot + KB + workflows | No by default | No by default | Yes | Yes | Variables and memory | Depends on plugin | Split Skill into prompt, KB, workflow, variables, memory |
| WorkBuddy | CN | Office task Skill | Usually uploaded files | Task artifacts/reports | Yes | Task workflow | Task fields | Depends on workspace | Treat as task package with report output |
| Trae | CN | File engineering Agent | Yes | Yes | Repo files | Commands/rules | Project state files | Depends on environment | Keep repository file reading and command guide |
| CodeBuddy | CN | Code/document Agent | Yes when repo connected | Yes when repo connected | Yes | Limited/custom | Agent rules | Depends on environment | Upload references/templates/prompts as KB |
| Generic low-code Agent | CN | System prompt + workflow | No by default | No by default | Optional | Optional | Optional | Optional | Prompt-only state summary and manual material intake |
| Chat-only Agent | Global | Conversation prompt | No | No | No | No | Conversation only | Optional | Path-labeled Markdown blocks and compact state |
| File Agent | Global | File workspace | Yes | Yes | Repo files | Optional | Files | Optional | Use direct file outputs and source logs |
| RAG workflow Agent | Global | KB + workflow | Uploaded docs | Usually no | Yes | Yes | Variables | Optional | Use retrieval chunks, workflow state, and reports |

## Required behavior by capability

| Capability gap | Required fallback |
| --- | --- |
| No direct `SKILL.md` reading | Upload or paste platform adapter documents and core protocol files |
| No file read | Ask for pasted text/OCR/Markdown/TXT, or produce a material-processing checklist |
| No file write | Output path-labeled Markdown blocks or report sections |
| No web | Mark current claims as unverified drafts and create verification tasks |
| No workflow | Use a single system prompt plus staged user prompts |
| No memory | Emit `learning_state` after every session |

