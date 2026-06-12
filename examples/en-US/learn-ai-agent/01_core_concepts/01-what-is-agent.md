# Concept 01: What is an AI Agent?

## One-line Explanation
An AI Agent is an intelligent system that can perceive its environment, autonomously make plans, execute actions, and self-correct based on feedback -- it doesn't just answer questions; it independently completes multi-step tasks.

## Life Analogy
Think of an AI Agent like a smart intern who has been given a computer and the right permissions:
- You give them a goal ("Do competitive research on our top 3 competitors")
- They break it down themselves (search -> organize -> compare -> write report)
- They call their own tools (search engine, documents, spreadsheets)
- They figure out problems on their own (if one search term fails, they try another; if data conflicts, they cross-reference)
- They come back to you with the result and explain how they got there

A regular AI can only answer "how to do competitive research." An Agent actually does it for you.

## Technical Explanation

```
Agent = LLM (Brain) + Tools (Hands) + Memory (Memory) + Planning (Planning ability)
```

Core loop (ReAct pattern):
1. **Think**: The Agent analyzes the current state and decides what to do next
2. **Act**: Executes a tool call or produces output
3. **Observe**: Looks at the result of the action
4. **Repeat**: Adjusts the plan based on observations and continues the loop

Key difference from traditional programs:
- Traditional programs: rules are predefined, execution path is fixed
- Agent: goal-driven, path is dynamically generated, self-corrects when things fail

## Real-world Case

**Auto-GPT** (2023): The first open-source autonomous agent to gain widespread attention. Given a goal like "research the market and write a report," it would automatically:
1. Search for relevant market data
2. Organize and compare information
3. Notice missing information and run additional searches
4. Generate a structured report
5. Review its own output quality and revise as needed

Results were mixed (this was the GPT-3.5 era), but it clearly demonstrated the agent paradigm in action.

## Common Pitfall
X Mistaking an Agent for "a chatbot with personality"
Y The core of an Agent is not conversation -- it is the **ability to autonomously complete tasks through a loop** (Think -> Act -> Observe -> Repeat)

## Exercise
In your own words, explain: Is Siri an Agent? Why or why not? (Hint: think about whether it can autonomously make plans, call multiple tools, and adjust its approach based on feedback.)

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
