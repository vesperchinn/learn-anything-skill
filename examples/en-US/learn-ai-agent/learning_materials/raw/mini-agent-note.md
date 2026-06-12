# Mini Agent Note

An AI agent is a software system that uses a goal, available context, and tool access to decide what action to take next.

The basic loop is:

1. Observe the goal and current state.
2. Plan the next useful action.
3. Act by answering, calling a tool, editing a file, or asking for missing information.
4. Check the result and decide whether another step is needed.

Tool use matters because it lets an agent work with systems outside the chat window, such as files, calculators, search tools, browsers, or APIs.

Agents should not pretend they used a tool or read a file when they did not. If a source is unavailable, the agent should say what is missing and ask for the source text, OCR, or another readable format.
