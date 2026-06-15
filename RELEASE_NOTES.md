# v0.2.3-beta - Freshness Notice in Chat Output

This release adds Freshness Notice visibility to the repository creation chat
output.

## What changed

- After a learning repository is created, the chat output now shows a Freshness
  Notice before Day 1 when the repository has freshness tracking or freshness
  risk metadata.
- High-risk or fast-changing topics point learners to
  `09_sources/freshness_log.md` and, when verification is needed,
  `09_sources/claims_to_verify.md`.
- Stable foundational subjects use a short notice, so freshness tracking is
  visible without interrupting the first learning session.
- Material-grounded learning keeps user-provided PDF / PPT materials as primary
  sources, marks outside context as Supplemental, and routes unverifiable claims
  to the verification checklist.

## Eval and harness coverage

- Added Freshness Notice eval cases for:
  - material-grounded learning
  - no-web / no-retrieval fallback
  - latest API / pricing / policy / model trap cases
- Added a Freshness Notice harness contract and checker.
- The checker verifies:
  - stable / evolving / high-risk notice variants
  - no forced full verification checklist for stable foundational knowledge
  - `claims_to_verify.md` for high-risk or fast-changing content
  - creation summary -> Freshness Notice -> Day 1 order
  - overclaiming phrases such as unsupported latest or fully verified claims

## Validation

- Freshness Notice check: passed.
- Guided Learning Mode check: passed.
- Full harness: `READY_WITH_WARNINGS`.
- The remaining warnings were reviewed and are mainly change-scope review
  warnings, not Freshness Notice behavior failures.
- English behavior evals: passed.
- Chinese behavior evals: passed.

## Reliability note

Freshness Notice does not guarantee that generated content is current or fully
accurate. It reduces risk by making freshness status visible, pointing to review
logs, and recording claims that need authoritative verification.
