# Source Quality Policy — {{domain}}

## Source Hierarchy

1. **Primary sources**: official documentation, peer-reviewed papers, textbooks, standards, official guidelines.
2. **Secondary sources**: expert tutorials, conference talks, accredited courses, expert blogs.
3. **Tertiary sources**: AI summaries, forums, social media, unattributed articles.

## Rules

- Prefer primary sources whenever a claim matters.
- Never fabricate URLs, DOIs, paper titles, author names, publication dates, official docs, or benchmark results.
- If the agent has web access, verify before citing.
- If the agent does not have web access, mark the content as an **Unverified Draft** and add claims to `claims_to_verify.md`.
- If a claim has no source, write it as `[unverified]` or remove it.
- High-stakes domains require authoritative sources and an educational-use-only notice.

## Claim Logging

Use `claim_ledger.md` for claims that were made, verified, disputed, or corrected.
Use `claims_to_verify.md` for claims that still need verification.
