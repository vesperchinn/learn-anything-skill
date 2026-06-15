# Contracts

Contracts define expected repository behavior in reviewable form. The YAML files
under `harness/contracts/` are intentionally simple so they can be read by
humans and checked by standard-library Python scripts.

## Contract groups

- `skill-contract.yaml`: native Skill metadata and required sections
- `locale-contract.yaml`: locale pairing and terminology
- `learning-repo-contract.yaml`: generated learning repository shape
- `reliability-contract.yaml`: source, claim, freshness, no-web, and high-risk requirements
- `freshness-notice-contract.yaml`: repository creation chat output freshness notice requirements
- `material-grounding-contract.yaml`: user-material handling requirements
- `platform-adapter-contract.yaml`: adapter package requirements
- `eval-contract.yaml`: expected eval coverage
- `script-contract.yaml`: read-only script behavior

## Contract interpretation

- `required_paths` are structural requirements.
- `required_terms` are textual requirements.
- `forbidden_terms` are claims or patterns that should not appear.
- Checks may produce `WARN` when a contract is hard to verify statically.
