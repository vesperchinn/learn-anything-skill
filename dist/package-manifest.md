# Package Manifest

This file is a manifest only. It documents which source files belong in a
platform package; it is not itself a generated runtime package.

## Common files by locale

For every platform package, include:

- `core/learning-protocol.{locale}.md`
- `core/reliability-protocol.{locale}.md`
- `core/material-grounding-protocol.{locale}.md`
- `core/state-schema.{locale}.md`
- `core/output-contract.{locale}.md`

## Locale-specific source sets

| Locale | References | Templates | Prompts |
| --- | --- | --- | --- |
| `zh-CN` | `references/zh-CN/` | `templates/zh-CN/` | `prompts/zh-CN/` |
| `en-US` | `references/en-US/` | `templates/en-US/` | `prompts/en-US/` |

## Packaging rules

- Do not overwrite existing package files.
- Do not include credentials, local secrets, generated learner repositories, or private user materials.
- Do not require low-code platforms to read `SKILL.md`.
- Mark low-code platform packages as beta / experimental until they are
  validated in the target workspace.
- Keep Codex native Skill files intact.
