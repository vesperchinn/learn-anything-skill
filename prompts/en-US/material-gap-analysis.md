# Material Gap Analysis

**Mode**: Material-Grounded Learning
**Inputs**: `learning_materials/material_index.md`, `learning_materials/material_coverage_map.md`, `progress.md`
**Output files**: updated `material_coverage_map.md`, `claims_to_verify.md`, `extraction_issues.md`

---

Analyze what the provided materials cover, what they miss, and what needs extraction review.

## Required Analysis

1. Identify concepts covered directly by the materials.
2. Identify partially covered concepts.
3. Identify gaps that block the learner's goal.
4. Identify unresolved extraction issues.
5. Recommend whether each gap should be:
   - ignored for now,
   - resolved by asking the user for better material,
   - handled with clearly labeled `Supplemental` material.

## Output Rules

- Update `learning_materials/material_coverage_map.md`.
- Update `learning_materials/extraction_issues.md` for unreadable content.
- Update `09_sources/claims_to_verify.md` for external supplemental claims.
- Do not present supplemental content as if it came from the user material.
