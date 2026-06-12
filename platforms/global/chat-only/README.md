# Chat-Only Agent Adapter

Use this adapter for ordinary chat agents that cannot read files, write files, run workflows, or keep reliable long-term memory.

## Package contents

- `core/learning-protocol.{locale}.md`
- `core/reliability-protocol.{locale}.md`
- `core/material-grounding-protocol.{locale}.md`
- `core/state-schema.{locale}.md`
- `core/output-contract.{locale}.md`
- A short system prompt assembled from the above files

## Operating mode

The agent must output learning repository files as path-labeled Markdown blocks. It must ask the user to paste material text or OCR when file reading is unavailable. At the end of every session, it must output `learning_state` so the next chat can continue.

## Fallback requirements

- No file read: do not claim uploaded materials were read.
- No file write: use `Save as:` blocks.
- No web: mark outputs as unverified drafts.
- No workflow: run the learning loop through manual conversation steps.
- No memory: include compact state in every response.

