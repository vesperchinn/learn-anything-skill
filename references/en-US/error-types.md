# Error Diagnosis Reference

How to classify and remediate learner errors. Used by the error-diagnosis and stage-test prompts.

## The Four Error Types

### 1. Conceptual Misunderstanding `[concept-gap]`

**Definition**: The learner does not know what the concept means. They cannot define it, recognize it, or distinguish it from unrelated concepts.

**Signals**:
- Blank response or "I don't know"
- Wildly incorrect definition
- Cannot answer basic recall questions (e.g., "What is X?")

**Remediation**:
1. Return to the concept definition in `01_core_concepts/`
2. Re-explain using the Feynman technique (simpler language, concrete analogy)
3. Give 3 recall-style questions to confirm basic understanding
4. Do NOT move to application until recall is solid

**Example**:
> Learner: "An embedding is... a type of database?"
> -> Conceptual Misunderstanding. The learner does not know what an embedding is at all.

### 2. Application Gap `[application-failure]`

**Definition**: The learner can define the concept correctly but cannot use it to solve a problem. They know the "what" but not the "how."

**Signals**:
- Correct definition, wrong application
- "I know what it is but I don't know how to use it here"
- Can answer recall questions but fails scenario questions

**Remediation**:
1. Show a worked example of the concept being applied
2. Give a near-identical scenario with small variations
3. Ask the learner to imitate the pattern
4. Gradually increase the distance from the original example

**Example**:
> Learner correctly defines "tool use in agents" but cannot write a tool definition in code.
> -> Application Gap.

### 3. Unclear Explanation `[expression-unclear]`

**Definition**: The learner understands the concept but cannot articulate it clearly. Their explanation is vague, circular, or uses the term to define itself.

**Signals**:
- "It's like... you know... it's when you..."
- Circular definitions ("An agent is something that acts agentically")
- Overly technical jargon without understanding
- Can solve problems but cannot explain the solution

**Remediation**:
1. Ask the learner to explain the concept to a specific audience (e.g., "Explain this to a 12-year-old")
2. Require a concrete analogy — no abstract terms allowed
3. Have them write the explanation down (not just speak it)
4. Review and point out where the explanation breaks down
5. Repeat until the explanation is clear, concise, and grounded in an analogy

**Example**:
> Learner: "ReAct is like... a pattern where the agent thinks and then acts. It's a reasoning-action loop. It's good for agents."
> -> Unclear Explanation. Circular reasoning, no concrete example, vague.

### 4. Knowledge Confusion `[knowledge-confusion]`

**Definition**: The learner confuses two or more related concepts. They understand each individually but blur the boundaries between them.

**Signals**:
- "Isn't that the same as X?"
- Using terms interchangeably that have distinct meanings
- Correct answer to the wrong question (applied Concept A's logic to Concept B's problem)

**Remediation**:
1. Create a side-by-side comparison table
2. Highlight the key distinguishing feature (one sentence that captures the difference)
3. Give paired examples: "This is X because... This is Y because..."
4. Discrimination exercise: present 5 cases and ask the learner to classify each as X or Y

**Example**:
> Learner uses "fine-tuning" and "RAG" interchangeably.
> -> Knowledge Confusion. They are different approaches to adding knowledge to LLMs.

## Diagnostic Decision Tree

```
Learner makes an error
|
+-- Can they define the concept?
|   NO -> [concept-gap]
|   YES -> continue
|
+-- Can they apply it to a problem?
|   NO -> [application-failure]
|   YES -> continue
|
+-- Can they explain it clearly?
|   NO -> [expression-unclear]
|   YES -> continue
|
+-- Are they confusing it with another concept?
    YES -> [knowledge-confusion]
    NO -> This might just be a slip — note it but do not over-weight it
```
