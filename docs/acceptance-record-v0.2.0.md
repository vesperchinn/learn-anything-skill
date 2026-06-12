# Acceptance Record: v0.2.0

Date: 2026-06-12

## Completion Criteria

- A generated learning repository contains required root files, learning
  directories, material workspace files, and source tracking files.
- `AGENTS.md` and `CLAUDE.md` are both generated from templates.
- English and Chinese template checks pass.
- English and Chinese behavior-policy checks pass.
- Mock end-to-end checks pass for English and Chinese.
- No-web fallback, material-grounding rules, source notes, claim ledger, and
  freshness tracking are represented in prompts, templates, and examples.

## Must-Pass Manual Checks

| Area | Result | Notes |
|------|--------|-------|
| Initialization | Pass | `scripts/new-domain.sh` and `scripts/init_learning_repo.py` scaffold required files without overwriting existing directories. |
| Daily learning loop | Pass by policy/template inspection | Prompts and rules require concept teaching, practice, deliverable, review, and progress updates. |
| Error diagnosis | Pass by policy/template inspection | Rules require error classification before correction. |
| Material mode | Pass by policy/template inspection | User materials must be registered, indexed, and treated as primary source. |
| No-web fallback | Pass by policy/template inspection | Unverified Draft and `claims_to_verify.md` are required when verification is unavailable. |
| Live Agent run | Not yet a release gate | No live multi-turn Agent transcript is included in v0.2.0. |

## Evidence

- `evals/en-US/test-templates.sh`
- `evals/zh-CN/test-templates.sh`
- `evals/run_behavior_evals.py --locale en-US`
- `evals/run_behavior_evals.py --locale zh-CN`
- `evals/run_e2e_evals.py --mode mock --locale en-US`
- `evals/run_e2e_evals.py --mode mock --locale zh-CN`

## Open Risk

Current evals verify files, policy text, and mock flows. They do not prove that
a live Agent will always maintain the full learning loop over many sessions.
Live Agent outcome evals are tracked for v1.0.0 in `ROADMAP.md`.
