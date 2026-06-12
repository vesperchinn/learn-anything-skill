# CodeBuddy Setup Guide

## 仓库连接模式

1. 连接 `learn-anything-skill` 仓库。
2. 让 CodeBuddy 读取 `platforms/cn/codebuddy/agent-rules.md`。
3. 需要创建学习仓库时，检查目标目录是否存在。
4. 使用 `templates/zh-CN/` 和 `core/prompts/zh-CN/` 生成文件。

## 知识库模式

1. 按 `knowledge-base-upload-guide.md` 上传文件。
2. 将 `agent-rules.md` 放入 Agent 规则。
3. 用户资料单独上传为“用户资料”分组。
4. 每次生成前检索核心协议和相关资料。

## 文档输出模式

如果当前环境不适合写入文件：

- 输出学习计划报告。
- 输出阶段测试文档。
- 输出资料覆盖报告。
- 输出 `learning_state` 供下次继续。

