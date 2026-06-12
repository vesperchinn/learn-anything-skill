# Material-Grounded Learning Repository

**Mode**: Material-Grounded Learning
**Inputs**: `learning_materials/material_manifest.md`, extracted materials, `{domain}`, `{duration}`, `{daily_time}`, `{locale}`
**Output files**: `00_domain_map.md`, `01_core_concepts/`, `learning_materials/material_index.md`, `learning_materials/material_coverage_map.md`, `learning_materials/material_learning_plan.md`, `progress.md`, `09_sources/claim_ledger.md`

---

Build the learning repository from the indexed user materials, not from a generic syllabus.

## Grounding Priority

1. User materials in `learning_materials/raw/`.
2. Extracted content in `learning_materials/extracted/`.
3. Supplemental outside knowledge, only when needed and clearly labeled `Supplemental`.

## Required Outputs

1. `learning_materials/material_index.md`
   - Index each material by topic and available page, slide, or section.
   - Mark charts, tables, screenshots, diagrams, and flowcharts.
2. `00_domain_map.md`
   - Build the knowledge map from material topics and structure.
   - Include material IDs and locations for each major concept.
3. `01_core_concepts/`
   - Create concept files only for concepts present in the material or explicitly marked `Supplemental`.
4. `learning_materials/material_coverage_map.md`
   - Map every learning module back to material IDs and locations.
5. `learning_materials/material_learning_plan.md`
   - Create a day-by-day plan that follows the material order where useful.
6. `progress.md`
   - Initialize progress with material coverage, current extraction issues, and next steps.
7. `09_sources/claim_ledger.md`
   - Log key factual claims derived from materials with Source Type = `Material`, Material ID / Location, Confidence, and Freshness Risk.
   - Log outside additions with Source Type = `Supplemental`.
8. `START_HERE.md`, `TODAY.md`, and `07_daily_review/day-01.md`
   - Create the guided Day 1 entry points after the material index is available.
   - Day 1 must be grounded in the available material index and must not require
     the learner to open several files before starting.

## Rules

- User materials are the primary source.
- Do not replace material content with generic domain knowledge.
- External additions must be marked `Supplemental`.
- Unreadable or unextracted content must remain an unresolved extraction issue.
- Do not fabricate page numbers, slide numbers, visual content, citations, or material topics.
- If visual content matters but cannot be extracted, mark the related module as `Partially grounded`.
- Material-derived claims must be auditable in `09_sources/claim_ledger.md`.
- After the material index and repository are created, do not stop after a file
  summary. Start the guided Day 1 session in chat unless the user explicitly
  requested scaffold-only mode.
- The guided session must tell the learner they do not need to open the files
  first, include one small chat task, an answer template, completion criteria,
  and note that `progress.md` will be updated after completion.

End generated learning modules with the standard Source Notes and freshness footer.
