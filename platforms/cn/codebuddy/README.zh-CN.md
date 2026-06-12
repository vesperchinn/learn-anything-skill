# CodeBuddy 适配包

CodeBuddy 适配面向代码/文档 Agent。推荐把 Learn Anything 的 `references`、`templates`、`prompts` 和 `core` 打成知识库包，再在代码或文档任务中调用。

## 文件说明

| 文件 | 用途 |
| --- | --- |
| `knowledge-base-upload-guide.md` | 知识库打包和上传 |
| `agent-rules.md` | Agent 调用规则 |
| `setup-guide.md` | 配置步骤 |
| `test-checklist.md` | 测试清单 |

## 使用模式

- 仓库连接模式：CodeBuddy 能读取当前仓库，按 `agent-rules.md` 调用。
- 知识库模式：上传核心协议、引用文档、模板和提示词，Agent 通过检索使用。
- 文档任务模式：输出学习计划、报告、测验和复盘文档。

