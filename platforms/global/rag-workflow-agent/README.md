# RAG Workflow Agent Adapter

Use this adapter for platforms with a knowledge base plus workflow nodes.

## Package contents

- Core protocol documents in the knowledge base
- Templates and reference policies in the knowledge base
- Workflow nodes for intake, material registration, retrieval, learning session, assessment, review, and report output
- Variables based on `core/state-schema.{locale}.md`

## Retrieval rules

- Retrieve core protocols before every major stage.
- Retrieve material chunks by material ID and topic.
- Do not use retrieved snippets without source metadata.
- Mark low-confidence or missing retrieval as `Partially grounded` or `Unresolved extraction issue`.

## Workflow fallback

If the workflow builder cannot express all stages, keep only intake, retrieval, generation, and review as nodes. Put the remaining learning loop in the system prompt.

