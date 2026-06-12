# Release Notes: v0.2.0

Release date: 2026-06-12

## Summary

v0.2.0 is the first release candidate intended for public use. It turns the
project from an early Codex-focused learning prompt set into a bilingual Skill
Pack with templates, source tracking, material-grounded learning, adapters,
scripts, examples, and evals.

## Highlights

- Added full zh-CN prompt, template, reference, eval, and example coverage.
- Added Material-Grounded Learning Mode for user-provided PDFs, slide decks,
  Markdown, TXT, Word docs, webpage exports, OCR, screenshots, and pasted notes.
- Added Knowledge Reliability Layer: `sources.md`, `claim_ledger.md`,
  `claims_to_verify.md`, `freshness_log.md`, and source quality policy files.
- Added generated `CLAUDE.md` templates so Claude Code project rules match the
  documented workflow.
- Added `--dry-run` support to both scaffolding scripts.
- Added roadmap and manual acceptance record.

## Safety Notes

- Scripts refuse to overwrite an existing `learn-{domain-slug}` directory.
- `--dry-run` shows the target path, template path, required files, and required
  directories without creating files.
- If scaffolding fails after creating a new directory, scripts clean up that new
  target directory.
- Generated content is not guaranteed factually correct. Current, high-stakes,
  numeric, legal, medical, financial, release, pricing, and benchmark claims
  still require source verification.
- Behavior evals are policy checks. They do not replace live Agent outcome
  evaluations.

## Known Limits

- Codex has the strongest verified workflow.
- Claude Code and Cursor are documented workflows, not fully proven live-agent
  release gates.
- Material examples are intentionally small and should be expanded in a later
  release.
- Live multi-turn Agent evals remain a v1.0 goal.
