# Release Checklist

Use this checklist before publishing a public release.

## Required Files

- [ ] `README.md`
- [ ] `README.zh-CN.md`
- [ ] `SKILL.md`
- [ ] `LICENSE`
- [ ] `CHANGELOG.md`
- [ ] `ROADMAP.md`
- [ ] `CONTRIBUTING.md`
- [ ] `CONTRIBUTING.zh-CN.md`
- [ ] `SECURITY.md`
- [ ] `CODE_OF_CONDUCT.md`
- [ ] `RELEASE_NOTES.md`

## Safety Review

- [ ] No `.env` files
- [ ] No API keys, tokens, passwords, or private keys
- [ ] No private PDFs, PPTs, notes, screenshots, or user data
- [ ] No logs, temporary files, generated check reports, or cache directories
- [ ] No local machine paths in public documentation

## Documentation Review

- [ ] README explains the project in one sentence
- [ ] README explains the problem it solves
- [ ] README covers Quick Start, Codex usage, generic Agent usage, and platform
      capability differences
- [ ] README describes Knowledge Reliability Layer and Material-Grounded
      Learning Mode with bounded claims
- [ ] Chinese README matches the English README in scope
- [ ] Documentation says the project reduces hallucination risk, not that it
      eliminates hallucinations

## Verification

- [ ] `python3 harness/scripts/run_all_checks.py --root . --report`
- [ ] Review warning items from the harness report
- [ ] Confirm `git status --short` contains only intended release files
- [ ] Confirm ignored files are not staged
- [ ] Confirm GitHub CLI is authenticated before pushing

## GitHub Release

- [ ] Commit release preparation changes
- [ ] Push `main`
- [ ] Create annotated tag
- [ ] Push tag
- [ ] Create GitHub Release from `RELEASE_NOTES.md`
- [ ] Confirm repository description and topics
