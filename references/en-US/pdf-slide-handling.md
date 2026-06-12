# PDF and Slide Handling

PDFs and slide decks often contain mixed content: text, images, charts, tables,
screenshots, diagrams, and speaker notes. Material-Grounded Learning Mode must
track which parts were extracted confidently and which parts need review.

## Intake Checklist

For each file, record:

- File name and format.
- Whether it is text-based, scanned, image-heavy, or mixed.
- Page count or slide count only if actually known.
- Extraction method used.
- Whether images, tables, charts, screenshots, or flowcharts are present.

## Extraction Rules

- Text can be summarized only after extraction.
- Tables must be marked as tables and should preserve rows/columns when possible.
- Charts must be described as charts and should not be converted into numeric
  claims unless values are readable.
- Screenshots must be marked as screenshots; UI text should be transcribed only
  if readable.
- Flowcharts must preserve nodes, arrows, and labels when readable.
- Speaker notes are distinct from slide text and should be labeled separately.

## Location Rules

- Use page numbers only when the extractor reports them or the user provides
  them.
- Use slide numbers only when they are available from the deck or export.
- If location is unknown, write `location unresolved`; do not guess.

## Visual Element Labels

Use these labels in `material_index.md`:

- `visual: chart`
- `visual: table`
- `visual: screenshot`
- `visual: flowchart`
- `visual: diagram`
- `visual: unreadable`

## Unresolved Issues

Log issues such as:

- scanned PDF with no OCR
- image-only slide
- unreadable chart labels
- table extraction failure
- missing speaker notes
- ambiguous page or slide order

Learning modules that depend on these sections must be marked
`Partially grounded` until the issue is resolved.
