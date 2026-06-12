# 扣子 Coze 适配包

本目录把 Learn Anything 从 Codex 原生 Skill 拆成扣子可配置的 Bot、知识库、工作流、变量、记忆和测试清单。不要假设扣子能直接读取仓库根目录的 `SKILL.md`。

## 推荐配置

| 模块 | 使用文件 |
| --- | --- |
| 智能体人设 / Prompt | `bot-prompt.zh-CN.md` |
| 知识库文档 | `knowledge-base-package.md` |
| 工作流节点 | `workflow-blueprint.md` |
| 变量 | `variables-schema.md` |
| 记忆 | `memory-schema.md` |
| 资料上传 | `material-upload-flow.md` |
| 可靠性流程 | `reliability-flow.md` |
| 发布检查 | `publishing-checklist.md` |

## 知识库建议上传内容

- `core/learning-protocol.zh-CN.md`
- `core/reliability-protocol.zh-CN.md`
- `core/material-grounding-protocol.zh-CN.md`
- `core/state-schema.zh-CN.md`
- `core/output-contract.zh-CN.md`
- `references/zh-CN/source-quality-policy.md`
- `references/zh-CN/freshness-policy.md`
- `references/zh-CN/claim-verification-guide.md`
- `references/zh-CN/material-grounding-policy.md`
- `templates/zh-CN/*.template`
- `prompts/zh-CN/*.md`

## 使用边界

- Coze Bot 默认不等于文件型工程 Agent，不能要求它自动创建本地学习仓库。
- 如果没有文件读取插件，用户资料必须通过上传知识库、粘贴文本或 OCR 进入系统。
- 如果没有联网插件，所有当前事实输出都应标记为未验证草稿。
- 如果没有工作流，使用 `bot-prompt.zh-CN.md` 的单 Bot 降级模式。

