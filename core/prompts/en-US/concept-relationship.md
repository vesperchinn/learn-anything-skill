# Concept Relationship

**Phase**: 1 — Map the Domain (on-demand)
**Inputs**: Concept A name, Concept B name, `{learning_language}`, `{locale}`
**Context needed**: `01_core_concepts/` files for both concepts
**Typical total tokens**: ~2,500

---

You are a domain learning engineer. The learner is confused about the relationship between two concepts. Clarify the distinction.

## Task

Compare **{concept_a}** and **{concept_b}**. Read their files from `01_core_concepts/` first.

## Output Format

### 1. One-Sentence Distinction
"{concept_a} is ___, while {concept_b} is ___. The key difference is ___."

### 2. Side-by-Side Comparison

| Dimension | {concept_a} | {concept_b} |
|-----------|-------------|-------------|
| Definition | ... | ... |
| Purpose | ... | ... |
| When to use | ... | ... |
| When NOT to use | ... | ... |
| Prerequisites | ... | ... |
| Real example | ... | ... |

### 3. Dependency Relationship
Which depends on which?
- A → B ({concept_a} requires understanding {concept_b} first)
- B → A ({concept_b} requires understanding {concept_a} first)
- Independent (can learn in any order)
- Bidirectional (they reinforce each other)

### 4. Confusion Diagnosis
Why do learners confuse these? (choose the most likely reason)
- Similar names
- Overlapping use cases
- One is a subset or superset of the other
- Often mentioned together in introductory materials
- Different schools of thought use them differently

### 5. Discrimination Exercise
Give 3 scenarios. For each, ask: "Is this {concept_a}, {concept_b}, or both?"
Provide the answer key after the learner responds.

### 6. Visual Comparison (if helpful)
Describe how you would draw the relationship (e.g., Venn diagram, hierarchy, flow).

All output in {learning_language}.
