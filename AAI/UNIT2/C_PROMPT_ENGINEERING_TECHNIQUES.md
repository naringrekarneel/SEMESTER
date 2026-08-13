# Topic 3: Prompt Engineering Techniques

Now we level up from **"how to write a good prompt"** to **"which prompting technique should I use for a particular problem?"**

This is very exam-friendly and also directly useful when building agents.

---

# 1. Big Picture

The major prompting techniques you should know are:

```text
Prompt Engineering
│
├── Zero-Shot Prompting
├── One-Shot Prompting
├── Few-Shot Prompting
├── Role Prompting
├── Instruction Prompting
├── Context / Delimiter Prompting
├── Structured Output
├── Prompt Chaining
├── Self-Consistency
└── ReAct Prompting
```

Some of these overlap with later topics, but understanding the progression is important.

---

# 2. Zero-Shot Prompting

## ELI5

You give the model a task but **no examples**.

It's basically:

> "Here's the job. Figure it out."

### Example

> Classify this sentence as Positive or Negative:
>
> "I absolutely love this phone."

Output:

> Positive

No examples were provided.

### When to use

Good when:

* task is simple
* model already understands the task
* you want a short prompt

### Structure

```text
Instruction
   ↓
LLM
   ↓
Output
```

---

# 3. One-Shot Prompting

Give the model **one example** before asking it to perform the task.

Example:

> Sentence: "This product is amazing."
> Sentiment: Positive
>
> Sentence: "The battery is terrible."
> Sentiment:

The model infers:

> Negative

### Why use it?

The example tells the model exactly what kind of output you expect.

---

# 4. Few-Shot Prompting

Give **multiple examples**.

Example:

```text
Sentence: "Amazing product!"
Sentiment: Positive

Sentence: "Worst purchase ever."
Sentiment: Negative

Sentence: "It works as expected."
Sentiment: Neutral

Sentence: "The screen quality is fantastic."
Sentiment:
```

Expected:

```text
Positive
```

---

## Zero vs One vs Few Shot

| Technique |  Examples |
| --------- | --------: |
| Zero-shot |         0 |
| One-shot  |         1 |
| Few-shot  | 2 or more |

### MUST REMEMBER

> **Few-shot prompting teaches the model the desired pattern through examples without changing the model's parameters.**

That's an important distinction from **fine-tuning**.

---

# 5. Role Prompting

Here we tell the model **who it should act as**.

Example:

> You are a senior Python developer. Review the following code and identify bugs.

Compared with:

> Review this code.

The first establishes a role and expected perspective.

### Examples

```text
You are a cybersecurity analyst.
```

```text
You are a mathematics tutor.
```

```text
You are a technical interviewer.
```

```text
You are a product manager.
```

### Important

Role prompting doesn't literally transform the model into that profession.

It provides **behavioral and contextual guidance**.

---

# 6. Instruction Prompting

This is probably the simplest technique.

Tell the model explicitly what to do.

### Weak

> Python loops.

### Strong

> Explain Python `for` loops to a beginner. Give the syntax, explain each component, and provide two examples.

The second prompt has:

```text
Task
+
Audience
+
Expected content
+
Examples
```

---

# 7. Context Prompting

LLMs perform better when relevant information is included in the prompt.

Example:

> I'm a beginner who understands Python variables and loops but hasn't learned functions yet. Explain recursion without assuming knowledge of functions.

Now the model knows your background.

### General structure

```text
Context
   +
Task
   ↓
LLM
   ↓
Context-aware answer
```

This becomes extremely important for **RAG**, because retrieved documents become additional context.

---

# 8. Delimiter Prompting

Suppose the user gives a long document.

We want the model to distinguish:

* instructions
* data
* user content

We can use delimiters.

Example:

```text
Summarize the document inside <DOCUMENT>.

<DOCUMENT>
Artificial intelligence is...
...
</DOCUMENT>
```

The delimiters clearly mark the boundaries.

Common delimiters:

```text
###
---
"""
<tag></tag>
```

---

# 9. Structured Output Prompting

Instead of asking:

> Analyze this review.

We can say:

> Return the answer as JSON with the fields `sentiment`, `issue`, and `urgency`.

Example:

```json
{
  "sentiment": "negative",
  "issue": "late delivery",
  "urgency": "high"
}
```

### Why is this important?

Because software can consume structured output.

For example:

```text
LLM
 ↓
JSON
 ↓
Python program
 ↓
Database
```

This is extremely important for **function calling and agentic systems**.

---

# 10. Prompt Chaining

This is a very important technique.

Instead of asking one prompt to perform a huge task, **break the task into multiple prompts**.

### Example

Suppose we want to create a blog article.

Instead of:

```text
Write a complete article about AI.
```

We can do:

```text
Step 1:
Generate 5 possible topics.

        ↓

Step 2:
Choose the best topic.

        ↓

Step 3:
Generate an outline.

        ↓

Step 4:
Write the article.

        ↓

Step 5:
Review the article.
```

This is called:

> **Prompt chaining**

---

## Why does chaining help?

Large tasks can be difficult to control.

Breaking them down gives:

* better organization
* easier debugging
* intermediate results
* greater control
* easier validation

---

# 11. Real-World Prompt Chain

Imagine an AI resume analyzer.

### Prompt 1

Extract candidate skills.

```text
Resume
 ↓
Skills
```

### Prompt 2

Compare skills against job requirements.

```text
Skills + Job requirements
 ↓
Match analysis
```

### Prompt 3

Generate recommendation.

```text
Match analysis
 ↓
Interview / Reject
```

So:

```text
Resume
 ↓
[Prompt 1]
 ↓
Skills
 ↓
[Prompt 2]
 ↓
Match
 ↓
[Prompt 3]
 ↓
Recommendation
```

This is much more controllable than one giant prompt.

---

# 12. Self-Consistency

Now we get into reasoning-oriented prompting.

Suppose the model has a difficult problem.

Instead of asking it to generate one answer, we can generate **multiple reasoning paths** and compare the resulting answers.

Conceptually:

```text
                Problem
                   ↓
        ┌──────────┼──────────┐
        ↓          ↓          ↓
     Path 1     Path 2     Path 3
        ↓          ↓          ↓
     Answer A   Answer A   Answer B
        └──────────┼──────────┘
                   ↓
             Majority answer
```

For example:

```text
Path 1 → 42
Path 2 → 42
Path 3 → 38
Path 4 → 42
Path 5 → 42
```

Final answer:

> 42

The idea is that agreement across independent reasoning paths can improve reliability on some reasoning tasks.

---

# 13. Chain-of-Thought Prompting

This deserves its own topic later, but understand the basic idea now.

Instead of:

> Solve this problem.

A prompt may encourage the model to work through the problem step by step.

Conceptually:

```text
Problem
 ↓
Intermediate reasoning
 ↓
Conclusion
```

For example:

> Solve the problem step by step and provide the final answer.

This can help with multi-step reasoning tasks.

### Important distinction

**Chain-of-Thought** is about reasoning through intermediate steps.

**Prompt chaining** is about breaking a task into multiple separate LLM calls.

They are NOT the same thing.

---

# 14. ReAct Prompting

ReAct stands for:

> **Reason + Act**

Instead of the LLM only generating an answer, it can alternate between reasoning and taking actions through tools.

Conceptually:

```text
Question
   ↓
Reason
   ↓
Action / Tool
   ↓
Observation
   ↓
Reason
   ↓
Action
   ↓
Observation
   ↓
Final Answer
```

Example:

User:

> "What's the weather in Mumbai?"

Agent:

```text
Reason:
I need current weather information.

Action:
Call weather tool.

Observation:
28°C, cloudy.

Reason:
I now have the current weather.

Final:
Mumbai is currently 28°C and cloudy.
```

This is a foundation of **Agentic AI**.

We'll study ReAct properly in Topic 5.

---

# 15. Prompt Decomposition

A complicated problem can be decomposed into smaller tasks.

Suppose:

> "Analyze this company's performance and recommend whether we should invest."

That's huge.

Break it down:

```text
1. Extract financial metrics
        ↓
2. Analyze revenue
        ↓
3. Analyze profitability
        ↓
4. Analyze risks
        ↓
5. Compare competitors
        ↓
6. Generate recommendation
```

This is often more reliable than asking one LLM call to do everything.

---

# 16. Constraint-Based Prompting

You can restrict the model's behavior.

Example:

> Explain neural networks in **exactly 100 words**, using **no mathematical formulas**, and give **two examples**.

The constraints are:

```text
100 words
+
No formulas
+
2 examples
```

This is useful when output must fit a specific format.

---

# 17. Negative Constraints

Sometimes we tell the model what **not** to do.

Example:

> Summarize this article. Do not include opinions that aren't supported by the article.

Or:

> Explain SQL to a beginner. Do not use advanced database terminology unless you define it.

This can reduce unwanted behavior.

But here's the catch:

> Negative instructions aren't always perfectly obeyed.

For high-stakes applications, use **validation and programmatic checks**, not prompts alone.

---

# 18. Prompt Templates

Instead of manually constructing prompts:

```text
Explain Python.
```

every time, create a reusable template:

```text
You are a {role}.

User level:
{level}

Topic:
{topic}

Explain it using:
{format}
```

Then your program can insert values.

Example:

```text
role = "Python tutor"
level = "beginner"
topic = "recursion"
format = "simple explanation + example"
```

Result:

```text
You are a Python tutor.

User level:
beginner

Topic:
recursion

Explain it using:
simple explanation + example
```

This is how prompt engineering becomes part of an actual software system.

---

# 19. Technique Selection Cheat Sheet

| Situation                           | Good technique                       |
| ----------------------------------- | ------------------------------------ |
| Simple task                         | Zero-shot                            |
| Need to demonstrate desired pattern | Few-shot                             |
| Need specific behavior/persona      | Role prompting                       |
| Need background information         | Context prompting                    |
| Long/complex input                  | Delimiters                           |
| Program needs predictable data      | Structured output                    |
| Large multi-step task               | Prompt chaining                      |
| Difficult reasoning                 | Chain-of-Thought / reasoning methods |
| Need multiple reasoning paths       | Self-consistency                     |
| Need external actions               | ReAct + tools                        |

---

# 20. One Big Example

Let's build a simple **customer-support AI**.

### Step 1 — Role

```text
You are a customer-support analyst.
```

### Step 2 — Task

```text
Analyze the customer's complaint.
```

### Step 3 — Context

```text
The company sells electronic products.
```

### Step 4 — Constraints

```text
Do not invent information.
```

### Step 5 — Output format

```json
{
  "issue": "...",
  "urgency": "...",
  "sentiment": "...",
  "action": "..."
}
```

### Step 6 — Example

```text
Example:

Complaint:
"My laptop arrived two weeks late."

Output:
{
  "issue": "late delivery",
  "urgency": "medium",
  "sentiment": "negative",
  "action": "contact customer"
}
```

### Step 7 — Actual input

```text
Complaint:
"My laptop arrived damaged and the screen is broken."
```

Now the model has a clear behavioral specification.

---

# 21. The Agentic AI Connection

Here's the progression you should understand:

```text
Basic LLM
   ↓
Prompt Engineering
   ↓
Better instructions
   ↓
Reasoning techniques
   ↓
Tool usage
   ↓
Memory
   ↓
RAG
   ↓
Self-correction
   ↓
AGENT
```

Prompt engineering is therefore the **communication layer** between you/application and the LLM.

---

# Quick Revision

### Zero-shot

No examples.

### One-shot

One example.

### Few-shot

Multiple examples.

### Role prompting

Tell the model what role it should perform.

### Context prompting

Provide relevant background.

### Structured prompting

Specify the desired output structure.

### Prompt chaining

Break a complex task into multiple LLM calls.

### Self-consistency

Generate multiple reasoning paths and use agreement to improve reliability.

### Chain-of-Thought

Encourage multi-step reasoning.

### ReAct

Combine reasoning with actions/tools.

---

# MUST REMEMBER FOR EXAM

The easiest way to remember the major techniques:

> **Zero/Few-shot = Examples**
> **Role = Who**
> **Instruction = What**
> **Context = Background**
> **Constraints = Rules**
> **Structured output = Format**
> **Chaining = Break the task**
> **Self-consistency = Multiple paths**
> **ReAct = Reason + Act**

---

# Active Learning

### Q1 — Conceptual

What is the difference between **few-shot prompting** and **fine-tuning**?

### Q2 — Conceptual

How is **prompt chaining** different from **Chain-of-Thought reasoning**?

### Q3 — Conceptual

Why is structured output particularly useful when an LLM is part of a software application?

### Q4 — Practical

You need an AI to process a resume and return:

* candidate name
* technical skills
* years of experience
* recommendation: **Interview / Reject**

Which **prompting techniques** would you combine, and why?

Answer these, and then we'll move to **Topic 4: Chain-of-Thought Reasoning**.
