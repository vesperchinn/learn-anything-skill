# Generic Low-Code Workflow Template

## 节点

1. **Input Intake**
   - 收集学习变量。
   - 判断是否有资料、是否可联网、是否可读取文件。

2. **Knowledge Retrieval**
   - 检索核心协议。
   - 如果有用户资料，检索资料片段。

3. **Material Grounding**
   - 登记资料。
   - 标记 Grounded / Partially grounded / Supplemental / Unresolved。

4. **Learning Map**
   - 生成知识地图。

5. **Learning Plan**
   - 生成阶段计划和每日任务。

6. **Daily Session**
   - 生成 3 个概念、5 道练习、1 个任务。

7. **Assessment**
   - 生成阶段测试。
   - 用户提交答案后评分。

8. **Review and State Update**
   - 归因错误。
   - 更新薄弱点、来源、待核查和下一步。

9. **Report Output**
   - 输出学习报告、任务单或路径标记 Markdown。

## 条件分支

- 无文件读取：进入资料降级节点。
- 无联网：进入未验证草稿节点。
- 无记忆：输出状态摘要节点。
- 无知识库：用 system prompt 中的最小规则执行。

