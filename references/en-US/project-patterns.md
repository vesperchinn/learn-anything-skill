# Project Patterns

Reference for designing capstone projects. Used by the project-design prompt.

## What Makes a Good Learning Project

A good capstone project is:

1. **Real** — It does something genuinely useful, even if small
2. **Complete** — It has a beginning, middle, and end, not a fragment
3. **Verifiable** — Success is objectively measurable (it runs, compiles, or produces output)
4. **Shareable** — The learner would be proud to show it to someone
5. **Small** — Fits within 7 days at the learner's daily time budget

## Project Patterns by Domain Type

### Pattern A: Build a Tool (Technical Domains)

**For**: Programming, AI/ML, DevOps, Security, Data Engineering

**Template**: Build a small but functional tool that solves a real problem.

**Example**: Learning AI Agents -> Build a personal research agent that auto-collects and summarizes information on a topic.

**Deliverables**: Working code, README with usage instructions, demo video or screenshot.

### Pattern B: Create a Framework (Conceptual Domains)

**For**: Product Management, Design, Strategy, Methodology

**Template**: Create a structured framework, playbook, or decision tree.

**Example**: Learning Product Management -> Build a product requirement template with a prioritization matrix and stakeholder checklist.

**Deliverables**: Framework document, worked example applying the framework to a real case.

### Pattern C: Produce Content (Knowledge Domains)

**For**: Writing, History, Philosophy, Science Communication

**Template**: Produce a comprehensive piece of content that demonstrates deep understanding.

**Example**: Learning Nutrition Science -> Write a 7-day meal plan with nutritional analysis, shopping lists, and evidence citations.

**Deliverables**: Published content piece, sources cited, peer feedback incorporated.

### Pattern D: Analyze Data (Research Domains)

**For**: Data Science, Economics, Sociology, Market Research

**Template**: Collect, clean, analyze, and visualize a dataset to answer a specific question.

**Example**: Learning Data Analysis -> Build a sales dashboard from public e-commerce data with trend analysis and recommendations.

**Deliverables**: Analysis notebook or report, visualizations, actionable insights.

### Pattern E: Design a System (Engineering Domains)

**For**: System Design, Architecture, Network Engineering, SRE

**Template**: Design a system that meets specified requirements, with diagrams and trade-off analysis.

**Example**: Learning System Design -> Design a URL shortener with scalability analysis, database schema, and API design.

**Deliverables**: Architecture diagram, design document, trade-off analysis, capacity estimates.

## Project Sizing Formula

```
Project scope = (daily_time_hours x 7 days) x 0.7

The 0.7 factor accounts for learning overhead, debugging, and iteration.
```

| Daily Time | 7-Day Project Budget | Recommended Pattern |
|------------|---------------------|-------------------|
| 1 hour/day | ~5 hours | Single-feature tool, short framework, one analysis |
| 2 hours/day | ~10 hours | Multi-feature tool, full framework, dataset analysis |
| 4 hours/day | ~20 hours | Full-stack mini-app, comprehensive framework, multi-analysis report |

## No-Code Alternatives

For learners without a coding background, adapt technical projects:

| Instead of... | Do this... |
|---------------|-----------|
| Building an app | Design a detailed system spec + Figma mockup |
| Writing a script | Document a step-by-step manual workflow |
| Training a model | Curate a dataset with annotation guidelines |
| Building a dashboard | Create spreadsheet templates with manual analysis |

## Project Quality Checklist

Before finalizing a project design, verify:

- [ ] Every core concept from the 20% "must-learn" list is exercised
- [ ] The learner's top 3 weak points from progress.md are addressed
- [ ] Each day has a concrete, verifiable deliverable
- [ ] The final result is demonstrable in under 5 minutes
- [ ] Failure modes are anticipated (common pitfalls section per day)
- [ ] An upgrade path exists (how to make it better after the program ends)
