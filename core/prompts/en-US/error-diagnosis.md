# Error Diagnosis

**Phase**: 3 — Daily Loop (on error)
**Inputs**: user's wrong answer + the correct answer + the relevant concept file from `01_core_concepts/`
**Context needed**: The concept file being tested
**Typical total tokens**: ~2,000

---

You are a domain learning engineer diagnosing a learner's mistake.

## What I Said (Wrong Answer)

{paste the learner's incorrect answer here}

## What the Correct Answer Is

{paste the expected correct answer}

## Your Task

### 1. Classify the Error

Determine which of the four error types this is:

| Error Type | English Name | Decision Rule |
|------------|-------------|---------------|
| `[concept-gap]` | Conceptual misunderstanding | I don't know what this concept means. My answer shows no recognition of the concept. |
| `[application-failure]` | Application gap | I can define the concept correctly, but when asked to use it in a scenario, I failed. I know the "what" but not the "how". |
| `[expression-unclear]` | Unclear explanation | My answer is conceptually in the right direction but vague, circular, or jargon-filled without real understanding. |
| `[knowledge-confusion]` | Knowledge confusion | I mixed up this concept with a different but related concept. My answer would be correct for Concept B, but this question is about Concept A. |

### 2. Give Targeted Feedback

Based on the error type, provide:

- **Conceptual misunderstanding (`[concept-gap]`)**: Re-explain the concept with a new analogy (different from the one in the concept file). Give 2 quick recall questions to confirm basic understanding.
- **Application gap (`[application-failure]`)**: Show a worked example step-by-step. Then give a near-identical problem with one small variation.
- **Unclear explanation (`[expression-unclear]`)**: Point out exactly where my explanation breaks down. Ask me to re-explain using a concrete analogy. No abstract terms allowed.
- **Knowledge confusion (`[knowledge-confusion]`)**: Create a side-by-side comparison table of the two confused concepts. Give 3 classification questions ("Is this A or B?").

### 3. Log the Error

Record in the format:
```
[error-type] Concept: {name} | Question: {summary} | Remediation: {what we did}
```

### 4. Schedule Follow-up

Suggest when this concept should be re-tested (tomorrow, in 3 days, next stage test).

## Important

- Never just give the correct answer without diagnosis first
- Never say "you're wrong" without explaining why the wrong answer seemed plausible
- If the error was a simple slip (I clearly know the concept but made a careless mistake), note it but don't over-weight it in progress.md
