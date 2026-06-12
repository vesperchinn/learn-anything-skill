# Claim Verification Guide

This guide provides a step-by-step process for learners to verify factual
claims encountered during their studies. Critical thinking and source
verification are essential skills—this document teaches you how to practice
them systematically.

## Why Verify Claims?

Even the best learning materials can contain errors. AI-generated content
is especially prone to plausible-sounding but incorrect claims (often called
"hallucinations"). By verifying key claims yourself, you:

- Build deeper understanding of the subject matter
- Develop critical thinking as a transferable skill
- Protect yourself from acting on incorrect information
- Contribute to the accuracy of your own learning materials

## Step-by-Step Verification Process

### Step 1: Identify the Claim

Not every sentence needs verification. Focus on claims that are:

- **Factual**: Specific numbers, dates, names, or technical specifications
- **Surprising**: Contradicts your existing knowledge or intuition
- **Critical**: You plan to build on this knowledge or act on it
- **Unattributed**: No source is cited for the claim

**Example claims worth verifying:**
- "Python's GIL was removed in version 3.13."
- "The time complexity of Timsort is O(n log n) in all cases."
- "React hooks were introduced in React 16.8."

### Step 2: Consult Primary Sources

Start with the highest-quality sources available for the domain:

| Domain | Where to Look |
|--------|--------------|
| Programming languages | Official language documentation, specification documents |
| Frameworks & libraries | Official docs, GitHub repos, changelogs, release notes |
| Computer science theory | Textbooks, original research papers |
| Mathematics | Textbooks, proof databases (e.g., MathWorld, OEIS) |
| Medical/scientific | PubMed, peer-reviewed journals, WHO guidelines |
| Legal | Government legal databases, official statute texts |
| Historical facts | Academic history texts, primary historical documents |

**Key principle:** Go to the original source whenever possible. A claim
about Python behavior should be verified in the Python documentation,
not in a blog post about Python.

### Step 3: Cross-Reference Multiple Sources

A single source is never proof. Look for corroboration:

1. Find **at least two independent sources** that confirm the claim.
2. "Independent" means the sources don't cite each other or share an author.
3. Pay attention to whether secondary sources all trace back to one primary
   source—if that primary source is wrong, all secondaries will be wrong too.

### Step 4: Evaluate Source Quality

For each source you find, assess it using the CRAAP framework:

- **C**urrency: Is this information up-to-date?
- **R**elevance: Does this directly address the claim in question?
- **A**uthority: Is the author or publisher an expert in this field?
- **A**ccuracy: Is the information supported by evidence?
- **P**urpose: Is this meant to inform, or to sell/persuade?

### Step 5: Handle Conflicting Sources

When sources disagree, use this resolution hierarchy:

1. **Prefer primary over secondary**: Official docs beat blog posts.
2. **Prefer recent over older**: Especially for technology topics.
3. **Prefer specific over general**: A Python 3.12 changelog beats a
   general "Python features" article.
4. **Prefer peer-reviewed over non-reviewed**: Academic rigor matters.
5. **Note the disagreement**: If you cannot resolve the conflict, record
   both positions in `claim_ledger.md` with the tag `[conflicting]`.

### Step 6: Record Your Findings

Document every verification in `claim_ledger.md` so future learners
(and your future self) benefit from your research.

## Using claims_to_verify.md

The `claims_to_verify.md` file is a running checklist of claims that need
verification. Use it as a queue to track what needs checking.

### Adding a Claim

When you encounter a claim that needs verification, add it to the checklist:

```markdown
## Claims to Verify

- [ ] "Python 3.13 removes the GIL" — Found in: 03_concurrency/01_threading.md
- [ ] "JWT tokens should never be stored in localStorage" — Found in: 05_security/02_auth.md
- [ ] "Rust guarantees memory safety without a garbage collector" — Found in: 01_intro/03_rust.md
```

### Completing a Verification

When you finish verifying a claim, check it off and add a brief result:

```markdown
- [x] "React hooks introduced in 16.8" — ✅ Confirmed via React blog and changelog
- [ ] "Python 3.13 removes the GIL" — Found in: 03_concurrency/01_threading.md
- [x] "Rust guarantees memory safety without a garbage collector" — ✅ Confirmed,
      but nuance needed: unsafe blocks can bypass this guarantee
```

## Updating claim_ledger.md

The `claim_ledger.md` is the permanent record of all verified and disputed
claims. Unlike `claims_to_verify.md` (which is a working checklist),
the ledger is a historical log.

### Ledger Entry Format

```markdown
| Claim | Module | Status | Sources Consulted | Verdict | Date |
|-------|--------|--------|-------------------|---------|------|
| "GIL removed in Python 3.13" | 03_concurrency/01_threading | ✅ Verified | PEP 703, Python 3.13 release notes | True — experimental free-threaded mode available | 2024-11-20 |
| "localStorage is insecure for JWTs" | 05_security/02_auth | ⚠️ Nuanced | OWASP guidelines, Auth0 blog | Partially true — XSS risk exists but context matters | 2024-11-20 |
| "Timsort is O(n log n) in all cases" | 02_algorithms/03_sorting | ❌ False | Python docs, original Timsort paper | False — O(n log n) worst case, O(n) best case | 2024-11-20 |
```

### Ledger Maintenance Rules

1. **Never delete entries**: The ledger is append-only.
2. **Update status if new information emerges**: Add a new row with
   the updated verdict; do not overwrite the old row.
3. **Include all sources consulted**: Even sources that didn't help
   should be listed to prevent duplicated research effort.
4. **Use clear verdict language**: "True", "False", "Partially true",
   "True with caveats", "Outdated", or "Unresolvable".

## Quick-Reference Checklist

Use this checklist when verifying any claim:

- [ ] Is the claim factual (not opinion)?
- [ ] Have I consulted at least one primary source?
- [ ] Have I found at least two independent sources?
- [ ] Have I checked the currency of my sources?
- [ ] Do my sources agree? If not, have I noted the conflict?
- [ ] Have I recorded the result in `claim_ledger.md`?
- [ ] Have I updated `claims_to_verify.md`?
