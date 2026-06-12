# Material Intake

**Mode**: Material-Grounded Learning
**Inputs**: `{domain}`, `{material_paths}`, `{material_urls}`, `{agent_type}`, `{file_read_access}`, `{locale}`
**Output files**: `learning_materials/material_manifest.md`, `learning_materials/extraction_issues.md`, `09_sources/sources.md`

---

You are preparing a learning repository from user-provided materials.

## Task

Collect and classify the learning materials before generating any course content.
User-provided materials are the primary source for this learning repo.

## Supported Materials

- PDF
- PPT / PPTX
- Markdown
- TXT
- Word / DOCX
- HTML or webpage export
- OCR text or pasted text

## Required Steps

1. List every supplied file, URL, or pasted text block in `learning_materials/material_manifest.md`.
2. Copy or reference original files under `learning_materials/raw/` when file access exists.
3. Extract readable text into `learning_materials/extracted/`.
4. Identify whether each material contains charts, screenshots, tables, diagrams, flowcharts, or speaker notes.
5. Record unreadable, missing, or partially extracted content in `learning_materials/extraction_issues.md`.
6. Register every user material in `09_sources/sources.md` with Source Type = `Material`, Tier = `Primary`, and Status = verified / partially extracted / unresolved.

## No File-Read Fallback

If the agent cannot read files, do not claim to have read them. Ask the user to:

- paste the relevant text,
- provide OCR output,
- convert the file to Markdown or TXT,
- export slides as text plus images,
- or approve a material-processing checklist only.

## Prohibited

- Do not generate a generic course before indexing the materials.
- Do not invent page numbers, slide numbers, chart contents, citations, or topics.
- Do not infer visual details from file names.
- Do not treat outside knowledge as material content.
- Do not skip `09_sources/sources.md`; user materials must be tracked as sources.

All output must be in `{locale}`-appropriate language unless the user specifies otherwise.
