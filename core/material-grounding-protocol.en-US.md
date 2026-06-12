# Material Grounding Protocol

Activate this protocol when the user uploads, pastes, links, or names learning materials. User materials define the learning scope; outside knowledge is supplemental only.

## Material types

- PDF, PPT/PPTX, Markdown, TXT, Word/DOCX
- Webpage exports, HTML, Notion/Feishu/Yuque exports
- Screenshots, scans, images, tables, flowcharts
- Pasted course notes, meeting notes, handouts

## Processing flow

1. **Register**: Record material ID, name, type, source, status, and access method.
2. **Extract**: Extract text, page numbers, slides, tables, captions, OCR, and speaker notes.
3. **Index**: Map topics to material locations.
4. **Cover**: Mark each learning module's relationship to the materials.
5. **Generate**: Build the map, plan, concepts, exercises, and tests from the material index first.
6. **Supplement**: Mark outside background knowledge as `Supplemental`.
7. **Log gaps**: Record unreadable or ambiguous content as unresolved extraction issues.

## Grounding labels

| Label | Meaning |
| --- | --- |
| `Grounded` | Directly supported by user materials |
| `Partially grounded` | Supported but affected by extraction gaps |
| `Supplemental` | Outside the supplied materials |
| `Unresolved extraction issue` | Material exists but cannot be read or interpreted reliably |

## Forbidden behavior

- Summarizing materials that were not read.
- Fabricating page numbers, slide numbers, chart values, screenshot meanings, author views, or concepts absent from materials.
- Replacing user materials with a generic course.
- Presenting supplemental knowledge as material content.

## No-file-read fallback

Clearly state that the agent cannot directly read the materials and choose one:

- Ask the user to paste key text.
- Ask for OCR or exported Markdown/TXT.
- Ask the user to export slides as text plus images.
- Output only a material-processing checklist and learning repository template, not grounded content.

