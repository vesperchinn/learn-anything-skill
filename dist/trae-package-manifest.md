# Trae Package Manifest

## Include

- `platforms/cn/trae/README.zh-CN.md`
- `platforms/cn/trae/project_rules.md`
- `platforms/cn/trae/user_rules.md`
- `platforms/cn/trae/agent-prompt.md`
- `platforms/cn/trae/setup-guide.md`
- `platforms/cn/trae/commands.md`
- Common core files from `dist/package-manifest.md`

## Include by reference

Trae can read the repository directly, so keep these as source dependencies rather than duplicating everything:

- `SKILL.md`
- `core/prompts/{locale}/`
- `templates/{locale}/`
- `prompts/{locale}/`
- `references/{locale}/`
- `scripts/`

## Acceptance

- Trae package supports file-based repository reading.
- It preserves access to `SKILL.md`, templates, prompts, and references.

