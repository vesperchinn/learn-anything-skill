# Extracted Material: M001 Mini Agent Note

Source file: `learning_materials/raw/mini-agent-note.md`
Extraction method: direct Markdown read
Extraction status: complete

## Section 1: Agent Definition

An AI agent is a software system that uses a goal, available context, and tool access to decide what action to take next.

## Section 2: Basic Loop

1. Observe the goal and current state.
2. Plan the next useful action.
3. Act by answering, calling a tool, editing a file, or asking for missing information.
4. Check the result and decide whether another step is needed.

## Section 3: Tool Use and Honesty

Tool use lets an agent work with files, calculators, search tools, browsers, or APIs. Agents should not pretend they used a tool or read a file when they did not.
