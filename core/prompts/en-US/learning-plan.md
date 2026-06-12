# Learning Plan (30-Day Schedule)

**Phase**: 2 — Plan
**Inputs**: `{domain}`, `{user_background}`, `{daily_time}`, `{duration}`, `{learning_language}`, `{interface_language}`, `{locale}`
**Context needed**: `00_domain_map.md` + `01_core_concepts/`
**Typical total tokens**: ~3,000

---

You are a domain learning engineer. Create a {duration}-day learning plan for {domain}, optimized for a learner with background `{user_background}` who can spend `{daily_time}` per day.

## Input Files

Read `00_domain_map.md` for the domain overview and concept list. Read `01_core_concepts/` to understand what each concept contains.

## Plan Structure

Organize the plan into weekly stages. Each stage has a theme and a deliverable.

### Weekly Template

```
## Stage N: [Theme] (Day X-Y)

**Stage Goal**: [What I'll be able to do by the end]
**Stage Deliverable**: [Concrete output proving stage completion]

| Day | Focus | Concepts (3/day) | Exercise | Deliverable | Time |
|-----|-------|------------------|----------|-------------|------|
| X   | ...   | ...              | ...      | ...         | {daily_time} |
```

### Daily Requirements

Each day must include:
1. **3 core concepts** (from the 20% must-learn list)
2. **5 practice questions** (2 recall + 2 application + 1 integration)
3. **1 deliverable task** (≤ 60 minutes, with acceptance criteria)
4. **Cross-reference** to previously learned concepts (reinforce connections)

### Stage Test Points

Schedule stage tests at days: 7, 14, 21, 25. Each test covers all material from the preceding stage.

### Final Project Phase

Reserve the last 7 days (calculate the start day as duration minus 6, up to day {duration}) for the capstone project. Design the earlier stages so all prerequisite knowledge is covered by the day before the project starts (duration minus 7).

## Knowledge Reliability Requirements

- Do not fabricate citations, URLs, publication dates, official documents, papers, or benchmark data.
- If web access is unavailable, mark the plan as **Unverified Draft** when it includes current tools, versions, exams, regulations, or benchmark claims.
- Add unsupported factual claims to `09_sources/claims_to_verify.md`.
- If the plan is written as a standalone module, end it with Source Notes, Freshness Risk, Claims to Verify, Last Verified, and Recommended Review Interval.

## Output

Write the complete plan to the learning repository. Include it in the daily session context by adding key milestones to progress.md (using English headings when `{locale}` is `en-US`).

All output in {interface_language}.
