# Source Quality Policy

This document defines how the Learn Anything Skill Pack evaluates and ranks
information sources to minimize hallucination and maximize learning accuracy.

## Source Hierarchy

### Tier 1: Primary Sources (Highest Trust)

Primary sources are the original, authoritative materials:

- **Official documentation**: Language specs, API references, framework docs
- **Peer-reviewed papers**: Published in recognized journals or conferences
- **Textbooks**: University-level, authored by recognized domain experts
- **Standards documents**: RFCs, ISO standards, W3C specifications
- **Official guidelines**: Government regulations, medical guidelines

**Trust level**: High. These sources have undergone editorial review,
peer review, or institutional vetting.

### Tier 2: Secondary Sources (Moderate Trust)

Secondary sources interpret, explain, or summarize primary sources:

- **Expert tutorials**: Written by recognized practitioners (e.g., Real Python, MDN Web Docs)
- **Conference talks**: PyCon, JSConf, academic conferences
- **Expert blog posts**: From practitioners with verifiable credentials
- **Curated courses**: From accredited institutions or recognized platforms

**Trust level**: Moderate. These sources are generally reliable but may
contain interpretation errors or become outdated faster than primaries.

### Tier 3: Tertiary Sources (Low Trust)

Tertiary sources aggregate or generate content without direct expertise:

- **AI-generated content**: ChatGPT, Claude, Gemini outputs
- **Forum answers**: Stack Overflow, Reddit, Quora
- **Social media**: Twitter threads, LinkedIn posts
- **Unattributed blog posts**: No author credentials, no citations

**Trust level**: Low. Useful for initial exploration but must be verified
against Tier 1 or Tier 2 sources before being treated as fact.

## Evaluation Criteria

When the Agent encounters or generates a factual claim, it should evaluate:

| Criterion | Question to Ask |
|-----------|----------------|
| Authority | Who created this? What are their credentials? |
| Currency | When was this published? Is it still current? |
| Accuracy | Can this be verified against a primary source? |
| Purpose | Is this educational, promotional, or opinion? |
| Corroboration | Do multiple independent sources agree? |

## Agent Behavior Rules

1. **Cite when possible**: If the Agent knows the source of a claim, cite it.
2. **Never fabricate citations**: Do not invent URLs, paper titles, or author names.
3. **Prefer primary sources**: When explaining a concept, reference official
   docs or textbooks rather than blog posts.
4. **Flag uncertainty**: Use `[unverified]` for claims the Agent cannot trace
   to a specific source.
5. **Log all sources**: Every source used must be recorded in
   `09_sources/sources.md`.

## Source Logging Format

When logging a source in `09_sources/sources.md`:

```markdown
| Source | Type | Tier | Last Verified | Notes |
|--------|------|------|---------------|-------|
| Python 3.12 Documentation | Official Docs | Primary | 2024-01-15 | Verified via web |
| "Fluent Python" by Luciano Ramalho | Textbook | Primary | N/A | Print edition |
| Real Python: Async IO Guide | Tutorial | Secondary | [unverified] | Describe, don't link |
```

## What NOT to Do

- ❌ Invent a URL like `https://docs.python.org/3/library/fake-module.html`
- ❌ Cite a paper that doesn't exist: "Smith et al. (2023)"
- ❌ Quote an expert who never said the thing: "As Linus Torvalds said..."
- ❌ Present AI-generated statistics as real data
- ❌ Use a Stack Overflow answer as the sole basis for a factual claim
