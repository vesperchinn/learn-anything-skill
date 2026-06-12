# Day 3 -- 2026-06-13

## One-line Summary
Tool Use / Function Calling transforms the Agent from "can only talk" to "can actually do things" -- when precision is needed, it calls dedicated tools instead of guessing from memory.

## 5 Keywords
1. **Tool Use** -- The Agent's ability to call external tools (search, compute, API)
2. **Function Calling** -- The technical implementation of Tool Use: the LLM generates a JSON-formatted tool call request
3. **Schema** -- The tool definition format: name, description, parameter types, required flags
4. **Orchestration** -- Coordinating multiple tools: when to search, when to compute, when to execute code
5. **Fallback** -- The degradation strategy when a tool call fails: retry, switch tools, or ask the user for help

## 3 Application Scenarios
1. Information retrieval Agent: detects real-time data needed -> calls search_web("today's weather") -> falls back to search_weather_api() if no results
2. Data analysis Agent: user asks about last quarter's sales trends -> calls query_db(SQL) -> calls plot_chart(data) -> returns a chart
3. Code assistant Agent: user asks "refactor this function" -> calls read_file() -> calls run_tests() -> confirms tests pass before submitting

## 2 Common Pitfalls
1. X Giving the Agent too many tools (20+), causing it to pick the wrong one every time -> Y Start with 1-2 tools, verify accuracy, then add more
2. X Writing vague tool descriptions ("searches for things") -> Y Schemas must be precise: name, purpose, and every parameter's type and meaning

## 1 Classic Case
**ChatGPT Web Search** -- The 2023 plugin system turned ChatGPT from a pure language model into an Agent that could search the web, execute code, and generate images. This proved that Tool Use is the key differentiator between a "language model" and an "Agent."

## Self-Test Question
Design 2 tool schemas for the task "Find the highest-rated coffee shops near me and book a reservation." Write the complete JSON definition for each.

## Connection to Previous Knowledge
- Day 1: Agent definition -> Tool Use is the specific technology that gives an Agent its "hands and feet"
- Day 2: Agent architecture -> Tools are one of the four components, orchestrated by the Orchestrator

## What I'm Most Likely to Forget
The `description` field in a tool schema is the most important part -- the LLM relies on it to decide when to call which tool. Writing a schema is essentially "writing API documentation for an LLM to read."

## Next Review
2026-06-14 -> 2026-06-16 -> 2026-06-20

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
