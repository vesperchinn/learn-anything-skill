# Expected Outputs — Quality Standards

What constitutes qualified vs. unqualified output for each phase of the
Learn Anything Skill Pack.

## Universal Rules (Apply to All Phases)

### ✅ Qualified

- Output follows the structure defined in the corresponding `core/prompts/*.md`
- All `{variable}` placeholders are replaced with actual values
- Language matches the user's `{learning_language}` setting for repository files
- Files are written to the correct paths per the File Writing Convention
- If agent has no file I/O, every file is output as a fenced code block
  labelled `📁 Save as: path/to/file.md`

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
├── 00_domain_map.md  ← placeholder with "待生成" header
├── 01_core_concepts/ ← has .gitkeep
├── ... (all required entries present)
├── progress.md       ← 7 sections, all initialised to "尚未开始"
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
> "想象你有一个非常聪明但从未离开过房间的实习生。你可以问他任何问题，
> 他都能在书本中找到答案——但他不能帮你订机票、整理邮件、做调研。
> 现在你给他配了电脑、网络、电话，还教他遇到不懂的先查资料。
> 这个升级版实习生就是一个 AI Agent。"

**Feynman Explanation (unqualified)**:
> "AI Agent 是一种基于大语言模型的自主智能系统，能够进行多步骤推理和
> 工具调用。" ← This is a technical definition, not a Feynman explanation.

**20-60-20 Split (qualified)**:
> Must-learn (20%): Agent 定义、LLM 基础、ReAct 循环、Tool Use、Prompt 工程
> Skip (60%): LangChain API 细节、Vector DB 底层索引、多 Agent 博弈论
> Learn-later (20%): Fine-tuning、生产部署、自定义 Orchestration

**20-60-20 Split (unqualified)**:
> Must-learn: 基础知识
> Skip: 高级内容
> Learn-later: 深入研究
> ← Too vague. No specific concepts listed.

**What NOT to Learn (unqualified)**:
> "不要急于求成" ← This is advice, not a list of topics to avoid.

---

## Phase 1: Concept Breakdown

### ✅ Qualified — Concept File Example

```markdown
# Concept: Tool Use / Function Calling

## One-line Explanation
Tool Use 让 Agent 能调用外部工具——搜索、计算、API——而非仅凭记忆回答。

## Life Analogy
你需要计算 387×294。心算可能出错，拿起计算器（工具）则精确无误。
Tool Use 就是让 AI 学会「拿起计算器」。

## Technical Explanation
Function Calling 的工作流：定义 schema → LLM 判断需要工具 → 生成
JSON 调用 → 系统执行 → LLM 整合结果到回复中。

## Real-world Case
ChatGPT 联网搜索：问「今天天气」→ 不凭记忆猜测 → 调用天气 API →
获取实时数据 → 组织自然语言回复。2023年首次向 Plus 用户推出。

## Common Pitfall
❌ 给 Agent 20 个工具，导致选错率飙升
✅ 从 1-2 个工具开始，验证正确率后再扩展

## Exercise
为「帮我找附近评分最高的咖啡店」设计 2 个 tool schema。
写出名称、描述、参数（类型+是否必填）。时间：10 分钟。
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
## 复习 (Review)
昨天学了 Agent 架构的四个组件。5 个关键点：
1. LLM 是推理引擎（大脑）
2. Memory 分短期（上下文）和长期（向量库）
...

## 今天学习 (Learn)
### Concept 1: Tool Use / Function Calling
[one-liner + analogy + technical + case + pitfall + exercise]

### Concept 2: Tool Schema Design
[...]

### Concept 3: Multi-Tool Orchestration
[...]

## 练习 (Practice)
Q1 [recall]: 什么是 Tool Use？
Q2 [recall]: Function Calling 的 JSON 格式包含哪三个顶层字段？
Q3 [application]: 为「查询天气」场景设计一个 tool schema
Q4 [application]: 为「发送邮件」场景设计一个 tool schema
Q5 [integration]: 如何让 Agent 先查天气，再根据天气决定是否发邮件？

（请先提交你的答案，我会逐题评分）

## 今日任务 (Output)
**任务**: 设计一个「餐厅推荐 Agent」的工具集
**时间**: 60 分钟
**交付物**: 01_core_concepts/exercise-tool-design.md
**验收标准**:
- [ ] 至少定义 3 个 tool schema（搜索、筛选、预订）
- [ ] 每个 schema 包含 name, description, parameters
- [ ] 画出 Agent 使用这些工具的 ReAct 循环图
```

### ❌ Unqualified — Session

```
Today we'll learn about Tool Use. Tool Use is when AI agents use tools
like search engines and APIs. It's a very important concept. Let me explain
how it works... [2000 words of explanation with no quiz, no task, and no
acceptance criteria.]
```
← Pure prose. Missing: quiz, deliverable task, acceptance criteria.
  Violates the ⛔ "no prose-only sessions" rule.

---

## Phase 4: Error Diagnosis

### ✅ Qualified

```
你的回答："Tool schema 就是一个 JSON 对象，包含名称和描述。"

诊断: [expression-unclear]
你的回答方向是对的——tool schema 确实是 JSON。但你说得太模糊了。
「包含名称和描述」没有提到最关键的部分：parameters（参数定义）。

正确回答: Tool schema 是一个 JSON 对象，必须包含三个顶层字段：
1. name — 工具的唯一标识符（string）
2. description — 工具的功能描述，LLM 靠它判断何时调用（string）
3. parameters — 工具接受的参数定义，使用 JSON Schema 格式（object）

补救练习: 请改写这个错误的 schema，使其包含完整的 parameters 定义。
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
## Stage 1 测试 — Foundation (Day 1-6)

本测试共 100 分，70 分及格。

### Section A: 选择题 (10×2=20分)
Q1. 以下哪项最准确地描述了 AI Agent？
A) 微调后用于对话的大语言模型
B) 能感知环境、制定计划、执行动作并自我纠正的系统
C) 有个性和记忆的聊天机器人
D) 返回结构化 JSON 的 API

[... 完整的 19 道题 ...]

---
请提交你的全部答案。我会逐题评分和诊断。
不要只给选项字母——概念解释题和场景题请详细作答。
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
- Knowledge checklist with ✅ strong / ⚠️ weak markers
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
- Day counter: 3 → 4
- 已完成模块: adds `[x] 03 - Tool Use (Day 3)`
- 薄弱点: re-ranks, adds new `[application-failure] Tool schema JSON 格式`
- 错题摘要: adds row for each new error with date, question, type, status

**progress-log.md append**:
```markdown
## Day 3 — 2026-06-13
主题: Tool Use / Function Calling
掌握程度: ⭐⭐ (2/5)
练习结果: 2/5 — 3 题错误 (2 application-failure, 1 expression-unclear)
耗时: 2h 30min
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
