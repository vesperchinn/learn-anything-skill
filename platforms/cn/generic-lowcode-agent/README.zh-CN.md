# 通用低代码 Agent 适配包

本目录适用于没有专门适配的中文低代码 Agent 平台。目标是用 system prompt、workflow、knowledge base、state schema 和 fallback mode 复现 Learn Anything 的核心能力。

## 文件说明

| 文件 | 用途 |
| --- | --- |
| `system-prompt.zh-CN.md` | 系统提示词 |
| `workflow-template.md` | 工作流模板 |
| `knowledge-base-template.md` | 知识库上传模板 |
| `state-schema.md` | 状态字段 |
| `fallback-mode.md` | 缺能力时的降级说明 |

## 最小可用配置

1. 把 `system-prompt.zh-CN.md` 放入系统提示词。
2. 上传 `knowledge-base-template.md` 中列出的核心协议和引用文档。
3. 按 `state-schema.md` 配置变量；如果平台不支持变量，就让 Agent 每轮输出状态摘要。
4. 能配置工作流时，按 `workflow-template.md` 建节点。
5. 不能配置工作流时，使用 `fallback-mode.md`。

