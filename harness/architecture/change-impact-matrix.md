# Change Impact Matrix

## `SKILL.md`

Must check:

- Skill manifest
- Adapter consistency
- README consistency
- Eval coverage for new triggers

## `prompts/en-US/`

Must check:

- Whether `prompts/zh-CN/` needs a matching update
- Template references
- Example updates
- Eval additions

## `templates/`

Must check:

- Learning repo contract
- Examples
- Initialization scripts
- Material and reliability templates remain connected

## `references/`

Must check:

- `SKILL.md` references
- Adapter updates
- Docs updates

## `platforms/`

Must check:

- Capability matrix
- Platform evals
- `dist` package manifests
- No dependency on Codex private capability for low-code platforms

## `scripts/`

Must check:

- Script contract
- Dry-run behavior
- README usage notes
- Cross-platform path handling

## `evals/`

Must check:

- Expected behavior is concrete
- README test notes
- Release gates

## `README.md`

Must check:

- `README.zh-CN.md`
- No exaggerated anti-hallucination claims
- Platform support table synchronization

## `docs/`

Must check:

- README links and summary consistency
- Locale parity for paired user-facing docs
- Release notes or acceptance records when the documented feature changes
- No exaggerated reliability, privacy, or material-processing claims

## `CONTRIBUTING.md` and `CONTRIBUTING.zh-CN.md`

Must check:

- Bilingual contributor guidance stays aligned
- Required local checks are current
- Prompt, template, adapter, and release-update rules match the maintained repo structure

## Knowledge Reliability Layer

Must check:

- Claim ledger
- Source notes
- Freshness log
- High-stakes policy
- No-web fallback
- Material mode integration

## Material-Grounded Learning Mode

Must check:

- `learning_materials`
- Source tracking
- Claim ledger
- Extraction issues
- Copyright rules
- PDF/PPT handling
- No-file-access fallback
