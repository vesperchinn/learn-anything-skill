# Capstone Project Design

**Phase**: 5 — Capstone Project
**Inputs**: `{domain}`, `{user_background}`, `{daily_time}`, `{final_artifact}`, `{interface_language}`, `{locale}`
**Context needed**: `00_domain_map.md` + `progress.md` + user's strong/weak areas
**Typical total tokens**: ~2,500

---

You are a domain learning engineer. Your task is to design a minimum viable project (MVP) that proves the learner has truly mastered {domain}.

## Learner Profile

- **Domain**: {domain}
- **Background**: {user_background}
- **Available time per day**: {daily_time}
- **Project duration**: 7 days
- **Desired output**: {final_artifact} (if "unsure", recommend 2-3 options)
- **Interface language**: {interface_language}

Read `progress.md` to understand the learner's specific strengths and weak points. Design the project to leverage strengths and shore up weaknesses.

## Project Design Requirements

Design a project that is:

1. **Minimal** — Small enough to complete in 7 days at {daily_time}/day
2. **Complete** — Runnable, demonstrable, and explainable end-to-end
3. **Relevant** — Uses the core concepts from the knowledge map
4. **Targeted** — Exercises the learner's identified weak points
5. **Extensible** — Can be improved after the 30-day program ends

## Output Structure

Write the project design to `04_projects/capstone-project.md` with the following sections:

### Project Overview
- **Project Name**: A catchy but descriptive name
- **One-line Pitch**: What it does in one sentence
- **Core Features** (3-5): The essential functionality
- **Tech/Tools Stack**: What the learner will use to build it

### Knowledge Checklist
List the specific concepts from `01_core_concepts/` that this project requires. Mark each as:
- ✅ Strong area (from progress.md)
- ⚠️ Weak area (from progress.md — will need extra attention)

### 7-Day Plan

| Day | Task | Deliverable | Time | Concepts Used |
|-----|------|-------------|------|---------------|
| 1 | ... | ... | {daily_time} | ... |
| 2 | ... | ... | {daily_time} | ... |
| ... | ... | ... | ... | ... |
| 7 | Polish + Demo | Working demo | {daily_time} | All |

Each day must produce a concrete, checkable deliverable.

### Day-by-Day Detail
For each day, provide:
1. **Goal**: What should be accomplished
2. **Input**: What to read/review first
3. **Steps**: 3-5 actionable steps
4. **Acceptance Criteria**: How to know it's done
5. **Common Pitfalls**: What might go wrong

### Acceptance Criteria (Final)
The completed project must pass these checks:
- [ ] **Runs**: The project actually executes or works
- [ ] **Demonstrates**: Can be shown to another person and they understand what it does
- [ ] **Explains**: Learner can describe the architecture, design decisions, and trade-offs
- [ ] **Iterates**: Clear path for future improvements documented

### No-Code Alternative
If {user_background} suggests coding is not appropriate, provide a low-code or no-code alternative that still demonstrates domain mastery (e.g., a detailed system design doc, a workflow automation, a content product).

### Upgrade Path
After completing this MVP, what are 2-3 directions the learner could take to make it more advanced? Each direction should reference specific concepts from the "learn-later (20%)" section of the knowledge map.

### Source Notes
End `04_projects/capstone-project.md` with:
- Source Notes
- Freshness Risk
- Claims to Verify
- Last Verified
- Recommended Review Interval

## Important

- If the learner's weak points from progress.md are critical to the project, explicitly allocate extra time or practice for those areas in the 7-day plan.
- The project should feel like a real achievement — something the learner would be proud to share or put in a portfolio.
- Do not fabricate citations, URLs, publication dates, official documents, papers, or benchmark data.
- If web access is unavailable and the design uses current tools, versions, platforms, exams, or regulations, mark it as **Unverified Draft** and update `09_sources/claims_to_verify.md`.
- All output in {interface_language}.
