# Flashcard Generate

**Phase**: 3 — Daily Loop (after review)
**Inputs**: today's concepts + today's errors from progress.md
**Context needed**: Today's concept files + progress.md weak points
**Typical total tokens**: ~2,500

---

You are a domain learning engineer. Compress today's learning into a knowledge compression card.

## Input

- Today's 3 concepts (from `01_core_concepts/`)
- Today's errors (from progress.md weak points section)

## Card Format

Save to `05_flashcards/day-{day_number}.md`:

```markdown
# Day {day_number} — {date}

## One-line Summary
{what today was about in one sentence}

## 5 Keywords
1. {keyword} — {one-line definition}
2. ...
3. ...
4. ...
5. ...

## 3 Application Scenarios
1. {real scenario where today's knowledge applies}
2. ...
3. ...

## 2 Common Pitfalls
1. ❌ {mistake} → ✅ {correction}
2. ❌ {mistake} → ✅ {correction}

## 1 Classic Case
{the most illustrative real-world example from today}

## Self-Test Question
{a question that tests the most important concept from today}

## Connection to Previous Knowledge
- Connects to Day X: {how today's concepts relate to earlier ones}

## What I'm Most Likely to Forget
{based on today's errors and weak points}

## Next Review
Suggested review date: {date, based on spaced repetition — 1 day, 3 days, 7 days, 30 days}

---

### Source Notes
- {source description} - [verified] or [unverified]

### Freshness Risk: 🟢 Stable / 🟡 Evolving / 🔴 Volatile

### Claims to Verify
- [ ] {claim} - suggested verification: {method}

**Last Verified**: {date or "not yet verified"}
**Recommended Review Interval**: {interval}
```

Do not fabricate sources, URLs, dates, papers, official documents, or benchmark data. If web access is unavailable, mark factual claims as `[unverified]` and add them to `09_sources/claims_to_verify.md`.

## Spaced Repetition Schedule
- Day 1: Review tomorrow's 5 key points reference
- Day 3: Re-read this card
- Day 7: Re-do the self-test question
- Day 30: Final review before program completion

All output in {interface_language}. Write to `05_flashcards/`.
