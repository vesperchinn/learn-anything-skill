# Freshness Policy

This document defines how the Learn Anything Skill Pack classifies, monitors,
and maintains the currency of learning content. Outdated information can be
as harmful as incorrect information—this policy ensures learners always
study the most relevant material.

## The 3-Tier Freshness Classification

Every module, lesson, or knowledge unit must carry a freshness tag indicating
how quickly its content is likely to become outdated.

### 🟢 Stable — Review Every 12-24 Months

Content that changes rarely or never. Foundational concepts that have remained
consistent for years or decades.

**Examples:**
- Mathematical foundations (linear algebra, calculus, set theory)
- Core computer science theory (algorithms, data structures, Big-O notation)
- Fundamental physics and chemistry principles
- Human anatomy and physiology basics
- Historical facts and established literary analysis
- Core programming paradigms (OOP, functional programming concepts)

**Characteristics:**
- Rooted in well-established theory or immutable facts
- Changes occur on a timescale of decades, if at all
- Primary sources (textbooks, standards) are themselves long-lived

### 🟡 Evolving — Review Every 3-6 Months

Content that changes periodically with version updates, new editions, or
evolving best practices.

**Examples:**
- Programming language features (Python 3.x, Java 21, Rust editions)
- Framework APIs (React, Django, Spring Boot)
- Cloud platform services (AWS, GCP, Azure offerings)
- Database technologies and query optimization techniques
- DevOps tooling and CI/CD pipelines
- Professional certification exam objectives

**Characteristics:**
- Tied to specific software versions or platform releases
- Best practices shift as the ecosystem matures
- Official documentation receives regular updates
- Breaking changes may invalidate previous explanations

### 🔴 Volatile — Review Every 1-3 Months, or Every 1-4 Weeks for urgent domains

Content that changes rapidly, sometimes weekly, driven by active development,
regulatory shifts, or emerging research.
Pricing, rate limits, model capabilities, benchmarks, product availability,
security advisories, and active regulatory details change frequently and should
direct learners to official documentation or authoritative notices.

**Examples:**
- AI/ML model capabilities and prompting techniques
- Cryptocurrency and DeFi protocols
- Active regulatory frameworks (data privacy laws, AI governance)
- Cybersecurity threats and vulnerability disclosures
- Bleeding-edge library APIs (pre-1.0 releases)
- Startup ecosystem tools and emerging SaaS products

**Characteristics:**
- Subject to breaking changes with little notice
- Community consensus shifts rapidly
- News and announcements can invalidate content overnight
- Requires real-time or near-real-time monitoring

## Tagging Modules with Freshness

Every module's metadata should include a `freshness` field. Add the tag
in the module's frontmatter or metadata section:

```markdown
## Module Metadata

| Field     | Value                          |
|-----------|--------------------------------|
| Freshness | 🟡 Evolving                   |
| Last Reviewed | 2024-11-20                |
| Next Review   | 2025-05-20                |
| Review Owner  | Agent / Learner           |
```

When creating a new module, select the freshness tier by asking:

1. **Is this concept tied to a specific software version or platform?**
   If yes → at least 🟡 Evolving.
2. **Has the landscape changed significantly in the last 6 months?**
   If yes → likely 🔴 Volatile.
3. **Would a textbook from 5 years ago still be accurate on this topic?**
   If yes → likely 🟢 Stable.

## Maintaining freshness_log.md

The file `freshness_log.md` serves as the central audit trail for all
freshness reviews. Each entry should follow this format:

```markdown
| Module | Freshness Tier | Last Reviewed | Reviewer | Status | Action Taken |
|--------|---------------|---------------|----------|--------|--------------|
| 03_functions/01_basics | 🟢 Stable | 2024-11-15 | Agent | ✅ Current | None |
| 05_async/02_patterns | 🟡 Evolving | 2024-11-15 | Agent | ⚠️ Outdated | Updated examples for Python 3.13 |
| 07_ml/03_transformers | 🔴 Volatile | 2024-11-15 | Agent | ❌ Stale | Rewrote section on attention mechanisms |
```

**Log maintenance rules:**
- Add a new row for every review, even if no changes are needed.
- Never delete old rows—they form an audit history.
- Sort by most recent review date descending.
- Include the specific action taken, or "None" if content is still current.

## When Content Goes Stale

Content is considered **stale** when it has passed its review deadline without
being reviewed, or when a known change in the domain invalidates it.

### Stale Content Protocol

1. **Mark immediately**: Add a `[⚠️ STALE]` banner to the top of the module:
   ```markdown
   > [!WARNING]
   > This module was last reviewed on 2024-03-01 and may contain outdated
   > information. A review is in progress.
   ```

2. **Quarantine if necessary**: For 🔴 Volatile content that is severely
   outdated (e.g., references a deprecated API), move it to a `_stale/`
   subdirectory to prevent learners from studying incorrect material.

3. **Prioritize review**: Stale 🔴 Volatile content takes highest review
   priority, followed by 🟡 Evolving, then 🟢 Stable.

4. **Update or retire**: After review, either update the content to be
   current or retire the module entirely with a note explaining why.

5. **Record the resolution**: Log the outcome in `freshness_log.md` with
   the action taken and the new review deadline.

## Freshness and Source Interaction

Freshness classification works hand-in-hand with the Source Quality Policy:

- 🟢 Stable content can rely on Tier 1 sources (textbooks, standards)
  that are themselves long-lived.
- 🟡 Evolving content should cross-reference the latest official
  documentation and release notes.
- 🔴 Volatile content must use the most recent primary sources available
  and should note the exact version or date of the source consulted.

When a source itself becomes outdated, the freshness tier of all modules
citing that source should be re-evaluated.
