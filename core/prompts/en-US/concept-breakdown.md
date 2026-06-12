# Concept Breakdown

**Phase**: 1 — Map the Domain
**Inputs**: `{domain}`, `{learning_language}`, `{locale}`
**Context needed**: `00_domain_map.md` (for the concept list)
**Typical total tokens**: ~2,000

---

You are a domain learning engineer. Break down each core concept from the knowledge map into a complete learning file.

## Source

Read `00_domain_map.md` Section 3 (Top 20 Core Concepts). For each concept in the must-learn-now (20%) list, create a file in `01_core_concepts/`.

## File Format

Name each file as `NN-concept-slug.md` (e.g., `01-what-is-agent.md`). Use the template from `templates/{locale}/concept-template.md`:

```markdown
# Concept: {Name}

## One-line Explanation
{single sentence}

## Life Analogy
{concrete, everyday comparison}

## Technical Explanation
{precise but accessible}

## Real-world Case
{specific, named example}

## Common Pitfall
{#1 beginner mistake}

## Exercise
{one targeted exercise}

---

### Source Notes
- {source description} - [verified] or [unverified]

### Freshness Risk: 🟢 Stable / 🟡 Evolving / 🔴 Volatile

### Claims to Verify
- [ ] {claim} - suggested verification: {method}

**Last Verified**: {date or "not yet verified"}
**Recommended Review Interval**: {interval}
```

## Quality Requirements

- **One-line explanation**: Must pass the "grandmother test" — would someone with zero domain knowledge get the gist?
- **Life analogy**: Must use everyday objects or experiences (cooking, driving, sports, etc.). No tech analogies for tech concepts.
- **Technical explanation**: Accurate but avoids unnecessary jargon. Define any technical term used.
- **Real-world case**: Must name a specific product, paper, event, or person. Not hypothetical.
- **Exercise**: Must be completable in 10-15 minutes. Must have a clear right or wrong answer, not open-ended reflection.
- **Sources**: Do not fabricate citations, links, publication dates, papers, official documents, or benchmark data. If web access is unavailable, mark the file as **Unverified Draft** and add specific items to `09_sources/claims_to_verify.md`.
- **Freshness**: Add the Source Notes footer from `templates/{locale}/source_notes.md.template` and update `09_sources/freshness_log.md`.

## Prioritization

Generate files for the must-learn-now (20%) concepts first. These are the gatekeeping concepts — without them, nothing else makes sense.

All output in {learning_language}. Write directly to `01_core_concepts/`.
