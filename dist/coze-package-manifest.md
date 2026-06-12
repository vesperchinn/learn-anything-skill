# Coze Package Manifest

## Include

- `platforms/cn/coze/README.zh-CN.md`
- `platforms/cn/coze/bot-prompt.zh-CN.md`
- `platforms/cn/coze/workflow-blueprint.md`
- `platforms/cn/coze/knowledge-base-package.md`
- `platforms/cn/coze/variables-schema.md`
- `platforms/cn/coze/memory-schema.md`
- `platforms/cn/coze/material-upload-flow.md`
- `platforms/cn/coze/reliability-flow.md`
- `platforms/cn/coze/publishing-checklist.md`
- Common core files from `dist/package-manifest.md`

## Exclude

- `SKILL.md` as a required runtime dependency
- Local scripts that Coze cannot execute
- Private learner materials

## Acceptance

- Coze package works as Bot Prompt + KB + Workflow + Variables + Memory.
- The package does not depend on direct `SKILL.md` reading.

