# Concept 03: Tool Use / Function Calling

## 一句话解释
Tool Use 是 Agent 调用外部工具（搜索引擎、计算器、API、代码执行器）的能力——它让 Agent 从「只会说话」变成「能做事」。

## 生活类比
你需要计算 387 × 294。你可以在脑子里心算（可能出错），也可以拿起计算器按一下（精确）。Tool Use 就是让 AI 学会「拿起计算器」——需要精确能力时，不依赖自己的知识猜测，而是调用专门的工具。

## 技术解释

Function Calling 的工作流程：
1. 定义工具的 schema（名称、描述、参数）
2. LLM 判断当前情境需要调用哪个工具
3. LLM 生成结构化的工具调用请求（JSON）
4. 系统执行工具调用，返回结果
5. LLM 将结果整合到回复中

```python
# 工具定义示例
tools = [{
    "name": "search_web",
    "description": "Search the web for current information",
    "parameters": {
        "query": "string — search query",
        "num_results": "int — number of results (default 5)"
    }
}]
```

## 真实案例

ChatGPT 的联网搜索就是 Tool Use：当用户问「今天天气如何」，ChatGPT 不会凭记忆回答（它的训练数据是旧的），而是调用天气 API 获取实时数据，再组织成自然语言回复。

## 常见误区
❌ 给 Agent 太多工具，导致它选错工具  
✅ 从 1-2 个工具开始，确认 Agent 能正确选择和调用后再增加

## 练习
为「帮我找附近评分最高的咖啡店」这个任务定义 2 个工具（写出工具名称、描述、参数）。

---

### 来源注释
- 资料来源：适用处引用 M001 Mini Agent Note。
- Supplemental 来源：M001 未覆盖的旧示例内容属于 supplemental，复用前需要验证。
- 未解决提取问题：M001 无未解决提取问题。

### 时效性风险：🟢 稳定

### 待验证主张
- [ ] 复用为正式课程前，验证 supplemental 示例、产品名、日期和事实主张。

**最后验证日期**：2026-06-12
**建议复查间隔**：12 个月
