# CodeBuddy Workflow Template

CodeBuddy 可按仓库模式或知识库模式运行。两种模式都必须保留学习闭环、资料 grounding 和可靠性检查。

## Workflow

1. **Intake**：收集领域、基础、目标、时间、语言、资料和文件访问能力。
2. **Mode Check**：判断是仓库连接模式还是知识库模式。
3. **Knowledge Retrieval**：检索核心协议、模板、提示词和相关资料。
4. **Scaffold or Report**：能写文件时创建学习仓库；不能写文件时输出路径标记 Markdown。
5. **Daily Loop**：解释、示例、练习、检查、复盘。
6. **Reliability Check**：无联网时标记未验证草稿，并生成待核查清单。
7. **Material Check**：先登记和索引资料，不得伪造资料内容。
8. **State Output**：每轮输出 `learning_state`。

## 降级

- 不能读取本地仓库时，使用知识库模式。
- 不能联网时，不写成已验证事实。
- 不能读取资料时，要求粘贴文本、OCR 或 Markdown/TXT 转换。
