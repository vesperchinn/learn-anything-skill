# Expected Outputs — Quality Standards

What constitutes qualified vs. unqualified output for each phase of the
Learn Anything Skill Pack.

## Universal Rules (Apply to All Phases)

### ✅ Qualified

- Output follows the structure defined in the corresponding `core/prompts/en-US/*.md`
- All `{variable}` placeholders are replaced with actual values
- Language matches the user's `{learning_language}` setting for repository files
- Files are written to the correct paths per the File Writing Convention
- If agent has no file I/O, every file is output as a fenced code block
  labelled `Save as: path/to/file.md`

### ❌ Unqualified

- Prose-only output with no file writes or copyable blocks
- Output that ignores the prompt's structure and writes a freeform essay
- Generic advice ("just practice more") without specific actionable steps
- Content that could apply to any domain without customization

---

## Phase 0: Scaffold

### ✅ Qualified

```
learn-{domain}/
├── README.md         ← explains how to use the repo
├── AGENTS.md         ← contains 8 teaching rules
├── CLAUDE.md         ← equivalent Claude Code teaching rules
├── 00_domain_map.md  ← placeholder with "To be generated" header
├── 01_core_concepts/ ← has .gitkeep
├── ... (all required entries present)
├── progress.md       ← 7 sections, all initialised to "Not started"
└── progress-log.md   ← only header line
```

### ❌ Unqualified

- Missing any required entry
- AGENTS.md or CLAUDE.md is empty or contains a generic "be helpful" instruction
- README.md doesn't explain the learning methodology
- progress.md has fewer than 7 sections
- Directories exist as empty (missing .gitkeep)
- Agent outputs a tree diagram but doesn't create files

---

## Phase 1: Knowledge Map

### ✅ Qualified — Section Quality Examples

**Feynman Explanation (qualified)**:
> "Imagine you have a very bright intern who has never left their room. You
> can ask them any question, and they can find the answer in a book — but
> they can't book flights for you, organize your email, or do research.
> Now you give them a computer, internet, a phone, and teach them to look
> things up when they don't know. That upgraded intern is an AI Agent."

**Feynman Explanation (unqualified)**:
> "An AI Agent is an autonomous intelligent system based on large language
> models, capable of multi-step reasoning and tool calling."
> ← This is a technical definition, not a Feynman explanation.

**20-60-20 Split (qualified)**:
> Must-learn (20%): Agent definition, LLM basics, ReAct loop, Tool Use, Prompt engineering
> Good-to-know (60%): LangChain API details, Vector DB indexing internals, Multi-agent game theory, RAG pipeline design, Fine-tuning workflows
> Learn-later (20%): Production deployment, Custom orchestration, Model training from scratch

**20-60-20 Split (unqualified)**:
> Must-learn: Basics
> Good-to-know: Advanced content
> Learn-later: Deep study
> ← Too vague. No specific concepts listed.

**What NOT to Learn (unqualified)**:
> "Don't rush things." ← This is advice, not a list of topics to avoid.

---

## Phase 1: Concept Breakdown

### ✅ Qualified — Concept File Example

```markdown
# Concept: Tool Use / Function Calling

## One-line Explanation
Tool Use lets an Agent call external tools — search, calculation, API — rather than answering from memory alone.

## Life Analogy
You need to calculate 387 x 294. Doing it in your head is error-prone; picking up a calculator (a tool) gives you the exact answer.
Tool Use is teaching AI to "pick up the calculator."

## Technical Explanation
Function Calling workflow: define schema -> LLM determines a tool is needed -> generates a JSON call -> system executes it -> LLM integrates the result into the response.

## Real-world Case
ChatGPT web search: ask "What's the weather today?" -> doesn't guess from memory -> calls a weather API -> fetches real-time data -> composes a natural language reply. First launched for Plus users in 2023.

## Common Pitfall
❌ Giving the Agent 20 tools at once, causing tool selection accuracy to plummet
✅ Start with 1-2 tools, verify correctness, then expand

## Exercise
Design 2 tool schemas for: "Find the highest-rated coffee shop near me."
Write name, description, and parameters (type + required/optional). Time: 10 minutes.
```

### ❌ Unqualified — Concept File

```markdown
# Tool Use

Tool Use is when an agent uses tools. Tools are important for agents
because agents need to interact with the world. There are many kinds of
tools like search, calculator, and API. Tool Use helps agents be more useful.
```
← Missing: life analogy, real case (named), pitfall, exercise.
  The explanation is circular and generic.

---

## Phase 3: Daily Session

### ✅ Qualified — Session Structure

```
## Review
Yesterday we learned the four components of Agent architecture. 5 key points:
1. LLM is the reasoning engine (the brain)
2. Memory is divided into short-term (context) and long-term (vector store)
...

## Learn
### Concept 1: Tool Use / Function Calling
[one-liner + analogy + technical + case + pitfall + exercise]

### Concept 2: Tool Schema Design
[...]

### Concept 3: Multi-Tool Orchestration
[...]

## Practice
Q1 [recall]: What is Tool Use?
Q2 [recall]: What are the three top-level fields in Function Calling's JSON format?
Q3 [application]: Design a tool schema for a "check weather" scenario
Q4 [application]: Design a tool schema for a "send email" scenario
Q5 [integration]: How could an Agent first check the weather, then decide whether to send an email based on the result?

(Please submit your answers first — I will score each question one by one)

## Output
**Task**: Design a tool set for a "Restaurant Recommender Agent"
**Time**: 60 minutes
**Deliverable**: 01_core_concepts/exercise-tool-design.md
**Acceptance Criteria**:
- [ ] Define at least 3 tool schemas (search, filter, book)
- [ ] Each schema includes name, description, parameters
- [ ] Draw a ReAct loop diagram showing how the Agent uses these tools
```

### ❌ Unqualified — Session

```
Today we'll learn about Tool Use. Tool Use is when AI agents use tools
like search engines and APIs. It's a very important concept. Let me explain
how it works... [2000 words of explanation with no quiz, no task, and no
acceptance criteria.]
```
← Pure prose. Missing: quiz, deliverable task, acceptance criteria.
  Violates the "no prose-only sessions" rule.

---

## Phase 4: Error Diagnosis

### ✅ Qualified

```
Your answer: "A tool schema is just a JSON object with name and description."

Diagnosis: [expression-unclear]
Your answer is on the right track — a tool schema is indeed JSON. But your
description is too vague. Saying "name and description" leaves out the most
critical part: parameters (parameter definitions).

Correct answer: A tool schema is a JSON object with three required top-level fields:
1. name — the unique identifier for the tool (string)
2. description — what the tool does; the LLM uses this to decide when to call it (string)
3. parameters — the parameter definitions the tool accepts, using JSON Schema format (object)

Remedial exercise: Rewrite the incorrect schema above so that it includes a complete parameters definition.
```

### ❌ Unqualified

```
Wrong. The correct answer is: Tool schema must include name, description,
and parameters in JSON Schema format.
```
← No error type diagnosis. No explanation of WHY the answer was wrong.
  No targeted remedial exercise. Just the answer.

---

## Phase 4: Stage Test

### ✅ Qualified — Examiner Mode

```
## Stage 1 Test — Foundation (Day 1-6)

This test is worth 100 points total. Pass threshold: 70 points.

### Section A: Multiple Choice (10 x 2 = 20 points)
Q1. Which of the following best describes an AI Agent?
A) A large language model fine-tuned for conversation
B) A system that perceives its environment, makes plans, executes actions, and self-corrects
C) A chatbot with personality and memory
D) An API that returns structured JSON

[... full 19 questions ...]

---
Please submit all of your answers. I will score and diagnose each question.
Do not just give letter choices — concept and scenario questions require detailed answers.
```

### ❌ Unqualified

```
Let's do a test. Question 1: What is an agent? [gives answer immediately]
Question 2: Explain ReAct. [gives answer immediately]
You got most of them right! Good job!
```
← Answers given with questions. No scoring. No error diagnosis.
  Not examiner mode — still in teacher mode.

---

## Phase 5: Project Design

### ✅ Qualified — Capstone Project

Must include ALL of:
- Project name + one-line pitch
- 3-5 core features
- Tech stack (or no-code alternative)
- Knowledge checklist with strong / weak markers
- 7-day breakdown: task, deliverable, time, concepts used
- Each day has acceptance criteria
- Final checklist: runs, demonstrates, explains, iterates
- No-code alternative if user can't code
- References user's weak points from progress.md

### ❌ Unqualified

```
Your project: Build a chatbot. Use Python and LangChain. It should be good.
Spend 7 days on it. Good luck!
```
← Missing: daily breakdown, acceptance criteria, knowledge checklist,
  weak point targeting, no-code alternative.

---

## Phase 3: Daily Review

### ✅ Qualified — Review Output

A qualified daily review updates all 3 target files:

**progress.md changes**:
- Day counter: 3 -> 4
- Completed Modules: adds `[x] 03 - Tool Use (Day 3)`
- Weak Points: re-ranks, adds new `[application-failure] Tool schema JSON format`
- Error Summary: adds row for each new error with date, question, type, status

**progress-log.md append**:
```markdown
## Day 3 — 2026-06-13
Topic: Tool Use / Function Calling
Mastery: ⭐⭐ (2/5)
Practice results: 2/5 — 3 wrong (2 application-failure, 1 expression-unclear)
Time spent: 2h 30min
...
```

**07_daily_review/2026-06-13.md**:
Full review with all sections per the template.

### ❌ Unqualified

- progress.md unchanged after session
- progress-log.md overwritten instead of appended
- Review file contains only "Good session today"
- Error type tags missing from weak points

---

## Summary: The Litmus Test

For any output, ask:

1. **Structure**: Does it follow the prompt template? Or is it freeform prose?
2. **Specificity**: Are concepts named, cases cited, schemas defined? Or is everything abstract?
3. **Exercises**: Are there questions with right/wrong answers and a deliverable task? Or just reading material?
4. **Acceptance criteria**: Can the user tell when they're "done"?
5. **Error handling**: If the user made a mistake, was it diagnosed before corrected?
6. **Files**: Were files created/updated at the correct paths? Or is everything only in the chat?
7. **State**: Is progress.md updated? Or is the session ephemeral?

If any answer is NO, the output is unqualified.
