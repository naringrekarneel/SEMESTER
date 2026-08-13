# Topic 9: Self-Reflection and Self-Correction

This is the **final topic in your syllabus**.

We've built our agent piece by piece:

```text
LLM
 ↓
Prompt Engineering
 ↓
Reasoning
 ↓
ReAct
 ↓
Tools
 ↓
Memory
 ↓
RAG
 ↓
Self-Reflection & Self-Correction
 ↓
🤖 More reliable Agent
```

The basic idea is:

> **Don't blindly trust the first answer. Let the agent inspect, evaluate, and improve its own output.**

---

# 1. ELI5 — What is Self-Reflection?

Imagine you write an answer in an exam.

Before submitting, you ask yourself:

> "Did I actually answer the question?"

You notice:

> "Oops, I forgot the example."

So you fix it.

That's **self-reflection**.

The AI does something similar:

```text
Generate answer
      ↓
Review answer
      ↓
Find problems
      ↓
Improve answer
```

---

# 2. What is Self-Correction?

Self-correction goes one step further.

The agent doesn't just identify a problem.

It **changes the answer to fix it**.

```text id="z7w3s1"
Initial Answer
      ↓
Evaluate
      ↓
Error found
      ↓
Correct
      ↓
Improved Answer
```

### Simple distinction

> **Self-reflection = "What's wrong with my answer?"**

> **Self-correction = "Let me fix what's wrong."**

---

# 3. Why Do We Need It?

LLMs can make mistakes.

For example:

> "What is 15 × 7?"

LLM might accidentally answer:

> 95

A self-correcting system can check:

```text id="a9m2k4"
15 × 7 = 105
```

It detects:

```text id="v8p5q2"
Initial answer = 95
Correct answer = 105
```

Then produces:

> 105

---

# 4. Basic Self-Correction Loop

Memorize this:

```text id="n4x7m2"
       Problem
          ↓
     Generate Answer
          ↓
       Evaluate
          ↓
     ┌────┴────┐
     │ Correct?│
     └────┬────┘
       No │  Yes
          │
          ↓
       Correct
          ↓
       Evaluate
          ↓
      Final Answer
```

Or simply:

```text id="r8q3v6"
Generate
   ↓
Reflect
   ↓
Correct
   ↓
Verify
   ↓
Final
```

---

# 5. Example — Writing

User:

> "Write a short explanation of cloud computing."

### First answer

> Cloud computing allows users to access computing resources over the internet.

Now the agent reflects:

> Does this explain the concept sufficiently?

It notices:

* definition present
* but no examples
* no explanation of benefits

### Corrected answer

> Cloud computing is the delivery of computing resources such as servers, storage, and databases over the internet. Examples include AWS, Azure, and Google Cloud. It allows organizations to scale resources without maintaining all infrastructure themselves.

Better.

---

# 6. Self-Reflection Architecture

A simple architecture:

```text id="c6m9p2"
                User
                 ↓
                LLM
                 ↓
            Initial Answer
                 ↓
           Reflection Module
                 ↓
          Error / Quality Check
                 ↓
             Correction
                 ↓
           Final Answer
```

Sometimes the same LLM performs both generation and evaluation.

Sometimes a separate model/evaluator is used.

---

# 7. Generator + Critic

A powerful design is to separate the system into two roles.

### Generator

Creates the answer.

### Critic

Evaluates the answer.

```text id="w3n8k5"
           Problem
              ↓
          Generator
              ↓
         Draft Answer
              ↓
            Critic
              ↓
      Feedback / Errors
              ↓
          Generator
              ↓
       Improved Answer
```

This is often called a:

> **Generator-Critic architecture**

---

# 8. Example — Coding Agent

Suppose the user asks:

> "Write Python code to check whether a number is prime."

Generator creates:

```python id="b8q4m1"
def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
```

Critic evaluates:

> Works for many positive integers, but doesn't explicitly handle values less than 2.

Correction:

```python id="y9x5c2"
def is_prime(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True
```

Now the agent has improved the solution.

---

# 9. Self-Reflection with Tests

For coding agents, a stronger approach is:

```text id="q4m8v7"
Generate Code
     ↓
Run Tests
     ↓
Observe Output
     ↓
Identify Failure
     ↓
Modify Code
     ↓
Run Tests Again
     ↓
Pass?
     ↓
Final Code
```

Notice something important:

This combines:

> **Self-correction + tool usage**

The agent isn't merely saying:

> "I think my code works."

It actually executes it.

---

# 10. Self-Correction + ReAct

Now connect today's topic to ReAct.

ReAct:

```text id="k8m2q5"
Reason
 ↓
Act
 ↓
Observe
```

Self-correction:

```text id="j4v9x2"
Generate
 ↓
Evaluate
 ↓
Correct
```

Combine them:

```text id="p7n3m8"
Goal
 ↓
Reason
 ↓
Act
 ↓
Observe
 ↓
Generate
 ↓
Reflect
 ↓
Correct
 ↓
Verify
 ↓
Final Answer
```

That's much closer to a robust agent.

---

# 11. Verification

Self-correction becomes much more reliable when the system can **verify its answer against something external**.

Example:

> "Calculate the average of 25, 40, and 55."

The agent can:

```text id="m2v7q9"
Reason
 ↓
Calculate
 ↓
Use calculator
 ↓
Observe result
 ↓
Compare with generated answer
 ↓
Correct if necessary
```

This is better than simply asking the LLM:

> "Are you sure?"

because an LLM can confidently say:

> "Yes."

even when it's wrong.

---

# 12. Important Principle

> **Reflection without verification is not guaranteed to work.**

An LLM can make a mistake and then "reflect" incorrectly.

Example:

```text id="e6x2r8"
Initial answer → Wrong

Reflection:
"The answer looks correct."

Final → Wrong
```

So external verification is often more reliable.

---

# 13. Critic Prompt

A critic can be instructed to evaluate specific criteria.

For example:

```text id="s7k3m1"
Evaluate the answer for:

1. Factual correctness
2. Completeness
3. Relevance
4. Logical consistency
5. Unsupported claims

Return:
PASS or FAIL
and explain the problem.
```

This creates a structured evaluation process.

---

# 14. Structured Self-Evaluation

Instead of:

> "Is this answer good?"

we can ask for structured evaluation:

```json id="n8x4q2"
{
  "correct": false,
  "missing_information": [
    "example"
  ],
  "factual_error": "Incorrect definition",
  "confidence": 0.72
}
```

Then the system can use the evaluation to trigger correction.

---

# 15. Reflection Loop

A more complete architecture:

```text id="g5m8v3"
              USER QUERY
                  ↓
             GENERATOR
                  ↓
             DRAFT ANSWER
                  ↓
               CRITIC
                  ↓
          ┌───────┴───────┐
          ↓               ↓
       PASS              FAIL
          ↓               ↓
        Final         Feedback
                          ↓
                      Generator
                          ↓
                       Revised
                          ↓
                        Critic
                          ↓
                         ...
```

Usually we impose a maximum number of iterations.

---

# 16. Why Maximum Iterations?

Imagine the model keeps correcting itself forever:

```text id="p8k4n2"
Generate
 ↓
Critic
 ↓
Correct
 ↓
Critic
 ↓
Correct
 ↓
Critic
 ↓
...
```

That's expensive and potentially infinite.

So we might specify:

```text id="e2v7m9"
MAX_ITERATIONS = 3
```

After three attempts:

> Return the best available answer.

---

# 17. Self-Reflection in Research Agents

Suppose an AI agent researches:

> "Compare three cloud platforms."

It might generate an initial report.

Then reflection checks:

```text id="v4n9x6"
Did I compare all three?
Did I use current information?
Did I support claims?
Did I miss important differences?
```

If something is missing:

```text id="r2m5k8"
Missing:
Pricing comparison

       ↓

Search tool

       ↓

Retrieve pricing information

       ↓

Update report
```

This combines:

```text id="f7x3q1"
RAG
+
Tools
+
ReAct
+
Self-reflection
```

That's the direction modern agentic systems take.

---

# 18. Self-Correction in Customer Support

User:

> "I want to return my laptop after 45 days."

Agent initially says:

> "You can return it."

Reflection checks the company policy retrieved through RAG:

> "Returns are allowed only within 30 days."

The agent corrects itself:

> "According to the current return policy, returns are allowed within 30 days, so a 45-day return would normally not qualify."

The key is:

```text id="y2k5m7"
RAG
 ↓
Evidence
 ↓
Reflection
 ↓
Correction
```

---

# 19. Self-Reflection vs Self-Correction

This is an easy exam question.

| Self-Reflection      | Self-Correction    |
| -------------------- | ------------------ |
| Evaluates its output | Changes its output |
| Finds weaknesses     | Fixes weaknesses   |
| Produces feedback    | Uses feedback      |
| "What's wrong?"      | "How do I fix it?" |

Usually they work together:

```text id="a4x8m2"
Reflection
 ↓
Feedback
 ↓
Correction
```

---

# 20. Self-Consistency vs Self-Reflection

Another likely confusion.

### Self-consistency

Generate multiple reasoning paths:

```text id="q6v3n9"
Answer 1 → 42
Answer 2 → 42
Answer 3 → 45
Answer 4 → 42

Majority → 42
```

### Self-reflection

Evaluate one answer:

```text id="h8m4x1"
Answer
 ↓
Critique
 ↓
Improve
```

So:

> **Self-consistency = compare multiple answers**

> **Self-reflection = critique an answer**

---

# 21. RAG + Self-Correction

This is a powerful combination.

Suppose the LLM generates:

> "The university requires 80% attendance."

The critic checks the retrieved document:

> "The document says 75%."

Correction:

> "The required attendance is 75%."

Architecture:

```text id="q8m2v5"
User
 ↓
RAG
 ↓
Retrieved Evidence
 ↓
LLM
 ↓
Draft
 ↓
Critic
 ↓
Compare with Evidence
 ↓
Correction
 ↓
Final Answer
```

This can improve factual grounding.

---

# 22. Tool Verification

Another powerful pattern:

```text id="x3n7k9"
LLM generates result
       ↓
Calculator / API / Test
       ↓
Actual result
       ↓
Compare
       ↓
Correct if needed
```

For example:

LLM says:

> 15 × 8 = 110

Calculator says:

> 120

The agent identifies the discrepancy and corrects the answer.

---

# 23. Advantages of Self-Correction

### 1. Improved accuracy

Errors can be detected.

### 2. Better completeness

Missing information can be identified.

### 3. Better code quality

Generated code can be tested and fixed.

### 4. Better reasoning

The agent can reconsider its approach.

### 5. Greater reliability

Multiple verification steps can reduce mistakes.

---

# 24. Limitations

Self-correction isn't a magic button.

### 1. Wrong self-evaluation

The model may fail to notice its own error.

### 2. Higher cost

More LLM calls mean more computation.

### 3. More latency

```text
Generate
 ↓
Critic
 ↓
Correction
```

takes longer than one generation.

### 4. Error amplification

A bad critique can cause a correct answer to be changed incorrectly.

### 5. Infinite loops

Requires iteration limits.

---

# 25. Best Practice

For serious applications:

> **Don't rely only on the LLM judging itself.**

Use external signals where possible.

For example:

### Mathematics

Use a calculator.

### Code

Run tests.

### Facts

Use RAG/search.

### Database

Query the database.

### Structured output

Use schema validation.

### Business rules

Use deterministic code.

This gives us:

```text id="u7k4m2"
LLM reasoning
+
External verification
=
More reliable system
```

---

# 26. Complete Agent Architecture

Now let's connect **your entire syllabus**.

```text id="z5m8q3"
                         USER
                           ↓
                    ┌─────────────┐
                    │     LLM     │
                    └──────┬──────┘
                           ↓
                    Prompt Engineering
                           ↓
                       Reasoning
                           ↓
                         ReAct
                      ↙    ↓    ↘
                   Tools  Memory  RAG
                     ↓      ↓      ↓
                   Result  Context  Evidence
                      ↘      ↓      ↙
                           LLM
                            ↓
                       Generate
                            ↓
                       Reflection
                            ↓
                       Correction
                            ↓
                       Verification
                            ↓
                       FINAL ANSWER
```

This is basically the mental model you want for **Agentic AI**.

---

# 27. Complete Syllabus Connection

Your syllabus can now be understood as one pipeline:

```text id="c2r7x9"
1. LLM
   ↓
2. Prompt Engineering
   ↓
3. Chain-of-Thought
   ↓
4. ReAct
   ↓
5. Tool Usage / Function Calling
   ↓
6. Memory
   ↓
7. RAG
   ↓
8. Self-Reflection
   ↓
9. Self-Correction
   ↓
10. Reliable Agent
```

Each topic solves a different limitation.

| Problem                           | Solution           |
| --------------------------------- | ------------------ |
| LLM needs instructions            | Prompt Engineering |
| Complex reasoning                 | CoT                |
| Need to interact with environment | ReAct              |
| Need external capabilities        | Tools              |
| Need persistent information       | Memory             |
| Need external/private knowledge   | RAG                |
| Need to detect mistakes           | Self-Reflection    |
| Need to fix mistakes              | Self-Correction    |

---

# 28. Exam Definition

If asked:

> **"Explain self-reflection and self-correction in LLM agents."**

Write:

> **Self-reflection is the process in which an LLM evaluates its own generated output to identify errors, missing information, inconsistencies, or weaknesses. Self-correction uses this feedback to revise and improve the output. These techniques can be implemented using generator-critic loops, verification tools, and iterative refinement.**

Then draw:

```text
Input
 ↓
Generate
 ↓
Reflect / Critique
 ↓
Error?
 ↓
Correct
 ↓
Verify
 ↓
Final Answer
```

---

# Quick Revision Sheet

### Self-Reflection

**Evaluate your own output.**

### Self-Correction

**Modify the output based on the evaluation.**

### Generator-Critic

```text
Generator → Critic → Generator
```

### Verification

Use external tools/data to check correctness.

### Iterative refinement

```text
Generate
 ↓
Critique
 ↓
Correct
 ↓
Repeat
```

### Important limitations

* incorrect self-evaluation
* higher cost
* higher latency
* error amplification
* infinite loops

---

# MUST REMEMBER

The easiest memory trick:

> **Reflection asks: "What's wrong?"**

> **Correction asks: "How do I fix it?"**

And for reliable agents:

> **Don't just ask the LLM to check itself—verify with tools, data, tests, or rules whenever possible.**

---

# Final Active Learning

Since this is the **last topic**, let's test the whole syllabus.

### Q1 — Conceptual

What is the difference between **self-reflection** and **self-correction**?

### Q2 — Conceptual

Why is external verification often better than simply asking an LLM, *"Are you sure your answer is correct?"*

### Q3 — Conceptual

Explain how **RAG + ReAct + self-correction** could work together in a single agent.

### Q4 — Practical — BIG ONE

Design an **AI College Assistant Agent** that can answer:

> **"Can I sit for tomorrow's exam, and remind me 30 minutes before the exam?"**

The agent has access to:

```text
1. Student database
2. College policy documents
3. Timetable database
4. Notification tool
```

Explain the complete flow using as many syllabus concepts as appropriate:

```text
LLM
Prompt Engineering
ReAct
Tool Calling
Memory
RAG
Self-Reflection
Self-Correction
```

After you answer these, I'll give you a **complete Agentic AI exam revision sheet + important 7/10-mark questions + final mini-quiz** covering the entire syllabus.
