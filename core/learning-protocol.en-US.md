# Learn Anything Learning Protocol

This protocol defines the platform-neutral learning loop. Every platform adapter must preserve these behaviors even when the platform lacks file access, web access, workflow nodes, or long-term memory.

## When to use

- The user wants to learn a domain systematically, not get a one-off answer.
- The user needs a plan, knowledge map, exercises, tests, reviews, or a capstone project.
- The user supplies PDFs, slides, Markdown, TXT, Word docs, webpage exports, screenshots, or course notes.
- The user needs progress and weak-point tracking across sessions.

## Variables

| Variable | Meaning |
| --- | --- |
| `domain` | Learning domain |
| `domain_slug` | ASCII slug used in files or state |
| `user_background` | zero, beginner, intermediate, advanced |
| `daily_time` | Time available per day |
| `duration` | Total learning days, default 30 |
| `learning_goal` | exam, work, project, writing, research |
| `final_artifact` | Final project or artifact |
| `interface_language` | Language used in conversation |
| `learning_language` | Language used for learning outputs |
| `material_mode` | Whether user materials define the scope |
| `web_access` | Whether source verification is available |
| `file_read_access` | Whether user materials can be read |
| `file_write_access` | Whether files can be written |
| `workflow_access` | Whether workflow nodes are available |

## Required learning loop

1. **intake**: Confirm domain, background, time, goal, final artifact, materials, languages, and platform capability.
2. **map**: Produce a knowledge map with core concepts, dependencies, confusion pairs, stages, and minimum viable knowledge.
3. **plan**: Produce a staged plan with concepts, exercises, deliverables, and acceptance criteria.
4. **learn**: Teach through Explain -> Demonstrate -> Practice -> Check -> Reflect.
5. **practice**: Include at least five questions per session across recall, application, and integration.
6. **deliver**: End every session with one checkable artifact.
7. **assess**: Run a stage test every seven days; show questions first, grade only after the user answers.
8. **diagnose**: Classify errors before giving the final answer and remediation.
9. **review**: Update progress, weak points, next steps, and source records.
10. **project**: Use the final stage to validate transfer through a capstone project.

## Error tags

| Tag | Meaning | Response |
| --- | --- | --- |
| `[concept-gap]` | Concept is not understood | Return to definitions, analogies, and minimal examples |
| `[application-failure]` | Concept is known but not usable | Add scenario practice and step decomposition |
| `[expression-unclear]` | Understanding is hard to express | Ask for restatement and rewrite |
| `[knowledge-confusion]` | Concepts are mixed up | Use contrast tables and discrimination questions |

## Non-negotiable rules

- Never produce a lecture-only session with no exercise and no task.
- Never reveal test answers before the user submits answers.
- Never turn a stage test into generic Q&A.
- Never make the plan a vague advice list; it must contain doable tasks.
- Never let platform limitations remove the learning loop; downgrade instead.

## Capability fallback

| Missing capability | Fallback |
| --- | --- |
| No file write | Output path-labeled Markdown code blocks for the user to save |
| No file read | Ask for pasted text, OCR, Markdown/TXT conversion, or output only a material-processing checklist |
| No web access | Mark content as an unverified draft and produce a verification checklist |
| No workflow engine | Simulate stages with one prompt or a multi-turn prompt sequence |
| No long-term memory | Output a compact `learning_state` summary for the user to keep |

