# Concept 03: Tool Use / Function Calling

## One-line Explanation
Tool Use is the Agent's ability to call external tools (search engines, calculators, APIs, code interpreters) -- it transforms the Agent from "can only talk" to "can actually do things."

## Life Analogy
You need to calculate 387 x 294. You could do mental math (prone to errors) or pick up a calculator and press some buttons (accurate). Tool Use is teaching the AI to "pick up a calculator" -- when precision is needed, it calls a dedicated tool instead of guessing from its internal knowledge.

## Technical Explanation

Function Calling workflow:
1. Define the tool schema (name, description, parameters)
2. The LLM decides which tool is appropriate for the current situation
3. The LLM generates a structured tool call request (JSON)
4. The system executes the tool call and returns the result
5. The LLM incorporates the result into its response

```python
# Tool definition example
tools = [{
    "name": "search_web",
    "description": "Search the web for current information",
    "parameters": {
        "query": "string — search query",
        "num_results": "int — number of results (default 5)"
    }
}]
```

## Real-world Case

ChatGPT's web search feature is a perfect example of Tool Use. When a user asks "what's the weather today," ChatGPT does not answer from memory (its training data is outdated) -- instead, it calls a weather API to fetch real-time data, then formats the response in natural language.

## Common Pitfall
X Giving the Agent too many tools at once, causing it to pick the wrong one
Y Start with 1-2 tools. Confirm the Agent can select and call them correctly before adding more.

## Exercise
Define 2 tools (name, description, and parameters) for the task: "Find the highest-rated coffee shops near me and book a table."

---

### Source Notes
- Material Sources: M001 Mini Agent Note where applicable.
- Supplemental Sources: Older example content outside M001 is supplemental and should be verified before reuse.
- Unresolved Extraction Issues: none for M001.

### Freshness Risk: 🟢 Stable

### Claims to Verify
- [ ] Verify supplemental examples, product names, dates, and claims before using this as a live course.

**Last Verified**: 2026-06-12
**Recommended Review Interval**: 12 months
