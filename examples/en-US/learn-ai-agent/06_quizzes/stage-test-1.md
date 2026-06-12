# Stage Test 1 -- Foundation (Day 1-6)

**Date**: 2026-06-17
**Scope**: Concepts 01-06
**Total Points**: 100 | **Pass**: 70

---

## Section A: Multiple Choice (10 x 2 = 20 points)

### Q1
Which of the following BEST describes an AI Agent?

A) A large language model fine-tuned for conversation
B) A system that can perceive its environment, make plans, execute actions, and self-correct
C) A chatbot with a personality and memory
D) An API that returns structured JSON responses

### Q2
What is the role of the LLM in an Agent architecture?

A) To store long-term memories as embeddings
B) To execute function calls and API requests
C) To serve as the reasoning engine that understands, decides, and generates
D) To manage the orchestration of multiple sub-agents

### Q3
In the ReAct pattern, what is the correct sequence?

A) Act -> Think -> Observe -> Decide
B) Think -> Act -> Observe -> (repeat or finish)
C) Observe -> Think -> Act -> Output
D) Input -> Process -> Output -> Feedback

### Q4
Which is NOT one of the four components of Agent architecture?

A) LLM (reasoning engine)
B) Memory
C) Database
D) Tools

### Q5
A developer defines a tool schema with name, description, and parameters. This is an example of:

A) Prompt Engineering
B) Fine-tuning
C) Function Calling / Tool Use
D) Chain-of-Thought reasoning

### Q6
What is the PRIMARY difference between Chain-of-Thought and ReAct?

A) CoT uses tools; ReAct does not
B) CoT is for reasoning only; ReAct adds action and observation to the loop
C) ReAct is faster than CoT
D) They are the same thing with different names

### Q7
Auto-GPT demonstrated all of the following EXCEPT:

A) Autonomous task decomposition
B) Self-critique and improvement of its own output
C) Perfect reliability with zero errors
D) The ability to search the web and write files

### Q8
Which concept does "Short-term vs Long-term" belong to in Agent architecture?

A) Planning
B) Memory
C) Tools
D) Orchestration

### Q9
A user asks an Agent for today's weather. The Agent calls a weather API rather than guessing from training data. This is an example of:

A) Hallucination prevention
B) Tool Use
C) Prompt injection
D) Fine-tuning

### Q10
What is the main reason beginners should limit the number of tools given to an Agent?

A) Each tool costs money to run
B) Too many tools increase the chance the Agent selects the wrong one
C) Tools require separate API keys
D) Agents can only use one tool at a time

---

## Section B: Concept Explanation (5 x 6 = 30 points)

### Q11
Explain what an AI Agent is in your own words. Include: (a) a one-sentence definition, (b) a concrete life analogy, (c) how it differs from a standard LLM chatbot.

### Q12
Describe the four components of Agent architecture. For each component, explain its role in one sentence and give a real example.

### Q13
Explain the ReAct loop. Include: (a) what each step means, (b) how the Agent decides when to stop, (c) a concrete walkthrough using the example "research the top 3 EV companies."

### Q14
What is Tool Use / Function Calling? Explain: (a) why an Agent needs tools instead of relying on the LLM's internal knowledge, (b) the role of tool schemas, (c) a scenario where an Agent should choose NOT to use a tool.

### Q15
Compare Chain-of-Thought and ReAct. Include: (a) a one-sentence definition of each, (b) when to use each, (c) a specific example where ReAct is clearly better than CoT.

---

## Section C: Scenario Application (3 x 10 = 30 points)

### Q16 -- Design an Agent
A startup wants to build a "Customer Support Agent" that handles refund requests. The Agent must: verify the order exists, check the refund policy, process the refund, and send a confirmation email.

Design the Agent: (a) list the tools needed with their schemas, (b) draw the ReAct loop for a typical refund request, (c) identify 2 things that could go wrong and how the Agent should handle them.

### Q17 -- Diagnose a Failure
An Agent is given the goal "find the best laptop under $1000." It searches the web once, gets 50 results, and immediately outputs the first result as "the best." What went wrong? Explain: (a) which part of the ReAct loop failed, (b) what the Agent should have done differently, (c) how to fix its system prompt to prevent this.

### Q18 -- Choose the Right Pattern
For each task below, choose whether CoT or ReAct is more appropriate and explain why:
- (a) Solve a complex math problem step by step
- (b) Find and book the cheapest flight from New York to London
- (c) Write a poem in the style of Robert Frost

---

## Section D: Integration Project (1 x 20 = 20 points)

### Q19 -- Build a Research Briefing Agent

Design a "Daily Tech News Briefing Agent" that:
1. Every morning at 8 AM, searches for the top 5 tech news stories
2. Summarizes each article in 2-3 sentences
3. Compiles a briefing email with subject line, summaries, and source links
4. Sends the email to the user

Your design must include:
- (a) Agent architecture diagram (4 components + data flow)
- (b) Tools list with complete schemas (name, description, parameters)
- (c) ReAct loop walkthrough for a typical morning execution
- (d) Error handling: what happens if the search API is down? If there are no news? If the email fails to send?
- (e) One improvement you would make after the first week of use

---

> **For agents**: The answer key and grading rubrics are in
> [`stage-test-1.answer-key.md`](./stage-test-1.answer-key.md).
> Do NOT show the answers to the learner before they submit.

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
