# Concept 02: Agent Architecture

## One-line Explanation
An Agent's architecture consists of four core components -- a brain (LLM), memory (Memory), tools (Tools), and a planner (Planner) -- that work together to let the Agent autonomously complete tasks.

## Life Analogy
Imagine you're cooking a dish you've never made before:
- **Brain (LLM)**: Your thinking ability -- understanding the recipe, judging when the pan is hot enough
- **Memory (Memory)**: You remember how you handled a similar dish before, and you know where the salt is
- **Tools (Tools)**: The pots, knives, and stove -- the things you can operate
- **Planner (Planner)**: The steps in your head -- prep ingredients first, then heat the pan, then cook, then season

Missing any one of these, and you cannot make that dish.

## Technical Explanation

```
+------------------------------------------------+
|                    AGENT                         |
|  +----------+    +-------------------+          |
|  |   LLM    |    |     Planner       |          |
|  | (Reason) |    | (Decompose goal)  |          |
|  +----+-----+    +--------+----------+          |
|       |                   |                     |
|  +----+-------------------+--------+            |
|  |           Orchestrator           |            |
|  |     (Think -> Act -> Observe)    |            |
|  +----+-------------------+--------+            |
|       |                   |                     |
|  +----+-----+    +--------+----------+          |
|  |  Memory   |    |      Tools       |          |
|  | Short/Long|    | Search/Code/     |          |
|  |           |    | API/Browser      |          |
|  +----------+    +------------------+           |
+------------------------------------------------+
```

**LLM**: Reasoning engine -- responsible for understanding, deciding, and generating
**Planner**: Breaks down complex goals into sequences of sub-tasks
**Memory**: Short-term = conversation context window; Long-term = vector database / knowledge base
**Tools**: External capabilities the Agent can operate (search, code execution, API calls, browser)
**Orchestrator**: Manages the Think -> Act -> Observe loop

## Real-world Case

**Claude Code** is a great example of Agent architecture in practice:
- LLM = Claude (the brain)
- Tools = file read/write, shell execution, web search
- Memory = conversation context + CLAUDE.md project rules
- Planner = built-in task decomposition ability

When you ask Claude Code to "fix this bug," it reads the code, locates the issue, edits the file, runs tests, and checks the result -- all autonomously.

## Common Pitfall
X Assuming that adding an LLM automatically gives you an Agent
Y An Agent needs all four components -- LLM + Memory + Tools + Planner -- working together

## Exercise
Draw the "Agent architecture" for an app on your phone. What is its LLM? What are its Tools? Where does its Memory live?

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
