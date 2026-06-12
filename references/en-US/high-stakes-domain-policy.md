# High-Stakes Domain Policy

This document defines how the Learn Anything Skill Pack handles domains where
incorrect information could cause real-world harm. The Agent must apply extra
safeguards when generating or presenting content in these areas.

## What Qualifies as High-Stakes?

A domain is classified as **high-stakes** when inaccurate information could lead
to physical harm, financial loss, legal liability, or professional consequences.

### Category 1: Medical & Health

Topics related to human health, disease, treatment, pharmacology, mental health,
nutrition, or any clinical practice.

**Examples:**
- Drug dosage calculations
- Symptom-based diagnosis explanations
- First-aid procedures
- Mental health coping strategies
- Nutrition and dietary guidance

**Risk:** Incorrect medical information can endanger lives.

### Category 2: Legal & Regulatory

Topics involving laws, regulations, legal procedures, contracts, intellectual
property, or compliance requirements.

**Examples:**
- Copyright and licensing explanations
- Employment law overviews
- Data privacy regulations (GDPR, CCPA)
- Immigration procedures
- Criminal justice concepts

**Risk:** Incorrect legal information can lead to liability or rights violations.

### Category 3: Financial & Economic

Topics covering personal finance, investing, tax law, accounting practices,
or economic policy.

**Examples:**
- Investment strategy explanations
- Tax filing guidance
- Retirement planning concepts
- Cryptocurrency mechanics
- Corporate financial reporting

**Risk:** Incorrect financial information can cause monetary loss.

### Category 4: Safety-Critical Engineering

Topics where software or hardware failures could cause physical harm or
significant property damage.

**Examples:**
- Embedded systems in medical devices
- Automotive control software
- Aviation systems programming
- Industrial control systems (SCADA)
- Nuclear facility software

**Risk:** Bugs or misunderstandings in safety-critical code can be catastrophic.

### Category 5: Professional Certification

Topics tied to specific professional certifications where incorrect study
material could cause exam failure or professional misconduct.

**Examples:**
- Medical licensing exam preparation (USMLE, NCLEX)
- Bar exam review material
- CPA/CFA exam content
- Professional engineering (PE) exam preparation
- Cloud certification exams (AWS SAA, GCP PCA)

**Risk:** Incorrect exam content wastes time and money, and may lead to
professional practice without proper understanding.

## Required Disclaimers

Every high-stakes module **must** include the following disclaimer at the top,
adapted to the specific domain:

### General Template

```markdown
> [!CAUTION]
> **Educational Use Only**
>
> This material is provided strictly for educational and informational purposes.
> It does NOT constitute professional [medical/legal/financial] advice.
> Always consult a qualified professional [doctor/lawyer/financial advisor] for decisions
> affecting your [health/legal rights/finances].
>
> The information presented here may be incomplete, outdated, or inapplicable
> to your specific jurisdiction or situation.
```

### Domain-Specific Variations

**Medical:**
> This content is for educational purposes only and does not replace
> professional medical advice, diagnosis, or treatment. Always seek the advice
> of a licensed healthcare professional or qualified healthcare provider.

**Legal:**
> This content provides general legal education and does not constitute legal
> advice. Laws vary by jurisdiction and change over time. Consult a licensed
> attorney for your specific situation.

**Financial:**
> This content is for educational purposes only and does not constitute
> financial advice, investment advice, or tax advice. Consult a licensed
> financial advisor or qualified financial professional before making financial
> decisions.

## How to Handle High-Stakes Content Differently

### Enhanced Source Requirements

High-stakes content has stricter source requirements than general content:

| Requirement | General Content | High-Stakes Content |
|-------------|----------------|---------------------|
| Minimum source tier | Tier 2 acceptable | Tier 1 required |
| Source count | 1 source sufficient | 2+ independent sources |
| Recency | Per freshness tier | Always use most current |
| Verification | Recommended | **Mandatory** |
| Disclaimer | Optional | **Required** |

### Content Boundaries

The Agent must clearly distinguish between:

1. **Explaining concepts** (acceptable): "The principle of informed consent
   means that a patient must be given enough information to make a voluntary
   decision about their treatment."

2. **Giving advice** (prohibited): "Based on your symptoms, you should
   take ibuprofen and rest for three days."

### Prohibited Actions in High-Stakes Domains

The Agent must **never**:

- ❌ Diagnose medical conditions or recommend treatments
- ❌ Ignore emergency symptoms or replace emergency services guidance
- ❌ Provide specific legal advice for a particular situation
- ❌ Recommend specific investments or financial products
- ❌ Claim that safety-critical code is "production-ready" or "bug-free"
- ❌ Guarantee accuracy of professional certification study material
- ❌ Present outdated regulations as current law
- ❌ Omit the educational-use-only disclaimer

### Escalation Protocol

When the Agent detects a high-stakes topic:

1. **Identify**: Recognize the domain as high-stakes based on the categories above.
2. **Disclaim**: Insert the appropriate disclaimer before any content.
3. **Source strictly**: Use only Tier 1 sources; flag any Tier 2 usage explicitly.
4. **Scope narrowly**: Teach principles and concepts, not actionable advice.
5. **Flag for review**: Add the module to `claims_to_verify.md` with
   `[high-stakes]` priority tag.
6. **Log**: Record the high-stakes classification in the module metadata.

If a user describes possible emergency symptoms or immediate safety risks,
the Agent must avoid diagnosis and direct the user to emergency services or a
qualified professional in their location.

## Jurisdiction and Scope Awareness

Many high-stakes domains are jurisdiction-dependent:

- **Legal**: Laws differ by country, state, and municipality.
- **Medical**: Drug approvals, treatment protocols, and licensing vary by country.
- **Financial**: Tax codes, investment regulations, and reporting requirements
  are jurisdiction-specific.

When teaching jurisdiction-dependent content:

1. State the jurisdiction explicitly (e.g., "Under US federal law...").
2. Remind the learner that rules may differ in their jurisdiction.
3. Never assume a universal legal, medical, or financial standard.
4. Encourage learners to verify against local authoritative sources.
