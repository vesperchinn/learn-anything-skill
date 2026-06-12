# Knowledge Map

**Phase**: 1 — Map the Domain
**Inputs**: `{domain}`, `{user_background}`, `{learning_language}`, `{locale}`
**Context needed**: None (standalone)
**Typical total tokens**: ~800

---

You are a domain learning engineer. Your task is to build a comprehensive knowledge map for a new field.

## Domain

**{domain}**

## My Background

**{user_background}**

## Learning Language

**{learning_language}**

## Task

Generate the knowledge map by answering all 10 questions below. Write the results to `00_domain_map.md`. Use the Feynman technique throughout — explain concepts as if to a motivated beginner.

### 1. What problem does this field solve?
Define the field's reason for existence in 2-3 sentences. What would be impossible or much harder without it?

### 2. Feynman Explanation
Explain {domain} in language a 12-year-old can understand. Use a concrete metaphor or everyday analogy.

### 3. Top 20 Core Concepts
List the 20 most important concepts in this field. For each: one-line definition + difficulty level (Beginner / Intermediate / Advanced).

### 4. Concept Relationship Map
Describe how these concepts connect. Which are prerequisites for others? Group related concepts into clusters (3-5 clusters). Format as a dependency outline.

### 5. Top 10 Confusion Pairs
List the 10 pairs of concepts beginners most often confuse. For each pair: one sentence explaining the key difference.

### 6. Five Learning Stages
Define 5 stages from absolute beginner to project-capable. For each stage:
- What you can do after completing it
- A concrete deliverable or artifact you must produce
- Estimated days needed

### 7. The 20-60-20 Split
Categorize knowledge into:
- **Must-learn-now (20%)**: Gatekeeping knowledge. Cannot proceed without it.
- **Skip-for-now (60%)**: Useful but not urgent. Creates false sense of progress.
- **Learn-later (20%)**: Advanced. Only relevant after completing a project.

### 8. Minimum Viable Knowledge
What is the absolute minimum someone needs to know to build something useful in this field? List only essentials — aim for ≤ 8 items.

### 9. What NOT to Learn Yet
List 5-10 topics, tools, or subfields that beginners should actively avoid. These are distractions that feel productive but aren't.

### 10. Recommended Learning Order
Propose a sequence for learning the top 20 concepts. Mark which ones are prerequisites for others. Note where case studies or projects should be inserted.

## Knowledge Reliability Requirements

- Do not fabricate citations, URLs, publication dates, papers, official documents, or benchmark data.
- If web access is unavailable, add an **Unverified Draft** notice at the top of `00_domain_map.md`.
- Do not present current versions, latest rankings, prices, regulations, or benchmark numbers as verified unless they were checked against authoritative sources.
- Append the Source Notes footer from `templates/{locale}/source_notes.md.template`.
- Update `09_sources/claims_to_verify.md` with specific claims needing verification.
- Add `00_domain_map.md` to `09_sources/freshness_log.md` with a suitable freshness risk and review interval.

## Output Format

Write directly to `00_domain_map.md` using clear markdown headings (# for title, ## for each of the 10 sections). Do not output the content in this conversation — write it to the file. All content in {learning_language}.
