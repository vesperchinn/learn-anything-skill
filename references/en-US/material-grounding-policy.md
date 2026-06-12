# Material Grounding Policy

Material-Grounded Learning Mode is used when the learner provides PDFs, slide
decks, Markdown, TXT, Word documents, HTML exports, or other learning materials.
In this mode, the provided material defines the course scope.

## Priority Rule

1. **User-provided materials are the primary source for the learning repo.**
2. Extracted text, OCR, tables, captions, speaker notes, and user-supplied
   clarifications are derived material and inherit the same priority.
3. External knowledge may be used only when the material is incomplete, unclear,
   or explicitly asks for background. It must be marked `Supplemental`.

## Required Behavior

- Read, parse, and index the materials before generating a knowledge map.
- Generate concepts, exercises, quizzes, reviews, cards, project tasks, and
  `progress.md` from the indexed material first.
- Preserve material IDs and locations in learning outputs.
- Use `learning_materials/material_coverage_map.md` to show which learning
  modules are grounded, partially grounded, supplemental, or gaps.
- Record unreadable or partially extracted content as an unresolved extraction
  issue in `learning_materials/extraction_issues.md`.

## Prohibited Behavior

The agent must not:

- Replace the material with a generic domain course.
- Invent page numbers, slide numbers, chart contents, citations, author claims,
  definitions, examples, or topics not present in the material.
- Claim a diagram, chart, screenshot, table, or flowchart says something unless
  the content was actually extracted or visually inspected.
- Hide external content inside material-grounded outputs without the
  `Supplemental` label.

## Grounding Labels

Use these labels in modules, quizzes, and coverage maps:

- `Grounded`: directly supported by user material.
- `Partially grounded`: based on material but missing extraction details.
- `Supplemental`: added from outside the user material.
- `Unresolved extraction issue`: material exists but could not be read or
  interpreted reliably.

## No File-Read Fallback

If the agent cannot read files, it must not pretend it saw the materials.
The agent does not claim it read, summarized, visually inspected, or extracted
content from a PDF, slide deck, image, Word document, or webpage export unless
that access actually happened.
It must ask the user to:

1. Paste relevant text.
2. Provide OCR output.
3. Convert the material to Markdown or TXT.
4. Export slides as text plus images.
5. Or accept a material-processing checklist instead of a grounded course.
