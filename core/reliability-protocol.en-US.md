# Reliability Protocol

This protocol reduces hallucinations, stale information, and fabricated-source risk. Every platform adapter must preserve it.

## Source hierarchy

| Tier | Sources | Use |
| --- | --- | --- |
| Primary | Official docs, textbooks, peer-reviewed papers, standards, government or professional guidance | Factual grounding |
| Secondary | Expert tutorials, course notes, conference talks, institutional courses | Explanation and interpretation |
| Tertiary | Forums, social media, AI summaries, anonymous articles | Discovery only; never sole support for key claims |

## Required behavior

- Specific, current, numeric, versioned, pricing, exam, legal, medical, financial, or safety claims must be verified or marked `[unverified]`.
- Used sources must record name, type, tier, status, and last verification date.
- Without web access, do not claim that "official docs say", "latest research shows", or "data shows".
- High-stakes domains require an educational-use-only note.
- Every learning module must record freshness risk: stable, evolving, or volatile.

## Forbidden behavior

- Fabricating URLs, DOIs, paper titles, authors, publication dates, benchmarks, or legal clauses.
- Treating AI-generated content as a real source.
- Using an unverified forum answer as the basis for a key claim.
- Claiming confirmation when the material or webpage was not read.

## Freshness checks

| Risk | Applies to | Suggested review |
| --- | --- | --- |
| Stable | Basic math, classic concepts, historical facts | 180-365 days |
| Evolving | Tool usage, framework practice, industry cases | 30-90 days |
| Volatile | Pricing, versions, rankings, policies, exam outlines, model capabilities | 7-30 days |

## No-web fallback

Output must include:

- `Status: Unverified Draft`
- Claims requiring web verification
- Suggested verification sources
- Uncertainty notes
- Source records to complete once web access exists

