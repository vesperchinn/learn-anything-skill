# Capstone Project: Personal Research Agent

## Project Overview

**Project Name**: ResearchPal -- Personal Research Assistant Agent

**One-line Pitch**: Give it a research topic, and the Agent automatically searches, organizes, compares information, and generates a structured research report with citations.

**Core Features**:
1. Accept a research topic and decompose it into sub-questions
2. Automatically search multiple sources (Web + academic databases)
3. Deduplicate, rank, and filter search results by relevance
4. Generate a structured report (summary + key findings + comparison table + citation list)
5. Support follow-up questions and deep-dive expansions

**Tech Stack**: Python + OpenAI API + SerpAPI (search) + Markdown file output

## Knowledge Checklist

| Concept | Status | Notes |
|---------|--------|-------|
| Agent Architecture | Y Strong | From Day 1-2 |
| ReAct Loop | Y Strong | From Day 4-5 |
| Tool Use / Function Calling | W Weak | Needs practice with multi-tool orchestration |
| Prompt Engineering | Y Strong | System prompt design is solid |
| Memory (short-term) | Y Strong | Conversational context management |
| Memory (long-term) | W Weak | Should add but optional for MVP |
| Planning | W Weak | Task decomposition needs work |
| RAG | Y Strong | From Day 15-17 |

## 7-Day Plan

| Day | Task | Deliverable | Time |
|-----|------|-------------|------|
| 1 | Project setup + define tools | Working tool definitions + test calls | 2h |
| 2 | Implement ReAct loop | Agent that can search -> read -> decide next step | 2h |
| 3 | Add planning (task decomposition) | Agent breaks research topic into sub-questions | 2h |
| 4 | Add report generation | Agent produces structured markdown report | 2h |
| 5 | Add error handling + guardrails | Agent handles API failures, rate limits, bad results | 2h |
| 6 | Testing + refinement | Test with 3 different research topics, fix issues | 2h |
| 7 | Polish + Demo prep | README, demo script, sample output | 2h |

## Acceptance Criteria (Final)
- [ ] **Runs**: `python3 research_pal.py "AI Agent trends 2026"` produces a report
- [ ] **Demonstrates**: Someone can watch it work in real-time
- [ ] **Explains**: You can describe the architecture and why you made each design choice
- [ ] **Iterates**: README includes 3 upgrade ideas

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
