# Material Quiz Generation

**Mode**: Material-Grounded Learning
**Inputs**: `learning_materials/material_index.md`, extracted materials, quiz scope
**Output files**: `06_quizzes/material-quiz-N.md`, optional answer key

---

Generate a quiz from user-provided materials.

## Quiz Structure

- 5 recall questions
- 3 application questions
- 2 integration questions
- Optional visual/table/chart interpretation questions when the material includes them

## Requirements

- Every question must cite a material ID and location.
- If the location is unresolved, state `location unresolved`.
- Questions may use `Supplemental` content only if clearly labeled.
- Visual questions must identify the visual type: chart, table, screenshot, diagram, or flowchart.
- Learner-facing quiz files must not include answers; write answer keys separately.

## Prohibited

- Do not invent page numbers or slide numbers.
- Do not ask about facts not present in the material unless marked `Supplemental`.
- Do not invent chart values or table entries.

Use `templates/{locale}/material_quiz.md.template` as the format.
