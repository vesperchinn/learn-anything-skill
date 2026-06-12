# Exercise: Design a Simple Agent

## Task
Design a "Daily News Briefing Agent" that collects top headlines and emails a summary each morning.

## Requirements
1. Define the Agent's goal in one sentence
2. List the tools it needs (3-5 tools)
3. Define each tool's schema (name, description, parameters)
4. Draw the ReAct loop for a typical morning execution
5. Define the output format (what the email looks like)
6. List 3 things that could go wrong and how the Agent should handle them

## Acceptance Criteria
- [ ] Goal is specific and measurable
- [ ] Each tool has a clear schema with parameter types
- [ ] The ReAct loop covers: Think -> Act -> Observe -> Decide (continue/finish)
- [ ] Output format is complete (subject, body structure)
- [ ] Error handling covers: API failure, no news, email send failure

## Time Budget
60 minutes

## Deliverable
A markdown file saved to `03_exercises/news-briefing-agent-design.md`

---

## Example Answer (Partial -- for reference after you attempt)

### Goal
Every morning at 8:00 AM, automatically collect the top 5 AI news stories from the past 24 hours, generate summaries, and email them to the user.

### Tools
1. `search_news(query, hours=24, limit=10)` -- Search for recent news articles
2. `summarize(text, max_length=200)` -- Compress an article body into a short summary
3. `send_email(to, subject, body)` -- Send an email
4. `log_result(status, details)` -- Record the execution log

### ReAct Loop
```
Think: "Need today's AI news" -> search_news("AI news", 24h)
Observe: Got 10 articles
Think: "Summarize top 5" -> summarize(article) x 5
Observe: Got 5 summaries
Think: "Ready to send" -> send_email(user, "AI Daily Brief", summaries)
Observe: Email sent successfully -> DONE
```

---

### Source Notes
- Material Sources: M001 Mini Agent Note where applicable.
- Supplemental Sources: Older example content outside M001 is supplemental and should be verified before reuse.
- Unresolved Extraction Issues: none for M001.

### Freshness Risk: 🟢 Stable

### Claims to Verify
- [ ] Verify supplemental examples, product names, dates, and claims before using this as a live course.

**Last Verified**: 2026-06-12
**Recommended Review Interval**: 12 months
