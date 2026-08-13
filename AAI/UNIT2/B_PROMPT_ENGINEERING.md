# Topic 2: Prompt Engineering

Now we move from **"What is an LLM?"** to **"How do I communicate with an LLM effectively?"**

This is where Agentic AI starts becoming practical.

---

# 1. ELI5 — What is Prompt Engineering?

Imagine you have a really smart assistant.

You say:

> "Tell me about Python."

It might give you a huge answer.

Instead, you say:

> "Explain Python to a beginner in 5 bullet points with one simple example."

You'll usually get a much more useful response.

That is the basic idea of **Prompt Engineering**:

> **Designing instructions that guide an LLM toward the desired output.**

A **prompt** is the input/instructions given to the model.

---

# 2. Why is Prompt Engineering Important?

LLMs don't simply respond based on *what* you ask.

They also respond based on **how you ask**.

Compare:

### Weak prompt

> Explain AI.

### Better prompt

> Explain Artificial Intelligence to a first-year computer science student using simple language and 3 real-world examples.

### Even better

> Explain Artificial Intelligence to a first-year computer science student. Start with a one-sentence definition, then explain the concept using 3 real-world examples. Avoid advanced mathematics. End with 5 exam revision points.

The third prompt gives the model:

* role/audience
* task
* format
* constraints
* desired depth

That's good prompt engineering.

---

# 3. Anatomy of a Good Prompt

A useful prompt can contain several components:

```text
┌──────────────────────┐
│ Role / Persona       │
├──────────────────────┤
│ Task                 │
├──────────────────────┤
│ Context              │
├──────────────────────┤
│ Constraints          │
├──────────────────────┤
│ Output Format        │
├──────────────────────┤
│ Examples              │
└──────────────────────┘
```

Not every prompt needs all of them.

---

# 4. Component 1 — Role

Tell the model what role it should perform.

Example:

> "You are an expert Python tutor."

Instead of:

> "Explain Python."

The first establishes a context for the response.

### Examples

```text
You are a cybersecurity instructor.
```

```text
You are a senior software engineer.
```

```text
You are an exam tutor.
```

```text
You are a product manager analyzing user feedback.
```

### Important

A role doesn't magically give the model new knowledge.

It mainly helps **frame the task and expected style**.

---

# 5. Component 2 — Task

Clearly state what you want.

Weak:

> "Machine learning."

Better:

> "Explain supervised learning."

Even better:

> "Explain supervised learning and compare classification and regression with examples."

Be explicit about the actual task.

---

# 6. Component 3 — Context

Context tells the model information it needs to perform the task.

Example:

> "I'm a beginner in Python and understand variables, loops, and functions."

Then:

> "Explain object-oriented programming assuming I have this background."

Without context, the model has to guess your knowledge level.

With context, it can adapt.

---

# 7. Component 4 — Constraints

Constraints tell the model what it **should or shouldn't do**.

Examples:

> "Keep the answer under 300 words."

> "Use simple language."

> "Don't use external libraries."

> "Give exactly 5 examples."

> "Avoid mathematical notation."

Constraints are extremely useful when building reliable AI applications.

---

# 8. Component 5 — Output Format

This is HUGE in real-world Agentic AI.

Instead of saying:

> "Analyze this customer review."

You could specify:

> "Return the result with these fields:
> sentiment, main_issue, urgency, suggested_action."

Now the output becomes predictable.

For example:

```text
sentiment: negative
main_issue: delayed delivery
urgency: medium
suggested_action: contact customer
```

This is much easier for software to process.

---

# 9. Structured Output

Suppose you're building an AI system that analyzes resumes.

You don't want:

> "This candidate seems pretty good and has experience with Python..."

You may want:

```json
{
  "candidate": "Rahul",
  "skills": ["Python", "SQL", "React"],
  "experience_years": 2,
  "recommendation": "Interview"
}
```

Why?

Because another program can easily consume structured data.

This becomes especially important with:

> **Function calling and agents**

which we'll study later.

---

# 10. Component 6 — Examples

You can show the LLM examples of the desired behavior.

For example:

> Input: "I love this product."
> Output: Positive
>
> Input: "This product is terrible."
> Output: Negative
>
> Input: "The product is okay."
> Output:

The model can infer:

> Neutral

This is the basic idea behind **few-shot prompting**, which we'll cover in the next topic.

---

# 11. Zero-Shot Prompting

You give the model a task **without examples**.

Example:

> Classify this review as positive or negative:
>
> "The camera quality is excellent."

The model has to perform the task without being shown examples.

```text
Prompt
  ↓
LLM
  ↓
Answer
```

This is called:

> **Zero-shot prompting**

---

# 12. One-Shot Prompting

Give **one example**.

Example:

> Review: "Amazing product!"
> Sentiment: Positive
>
> Review: "The battery is terrible."
> Sentiment:

The model can infer:

> Negative

---

# 13. Few-Shot Prompting

Give several examples.

```text
Review: "Absolutely fantastic!"
Sentiment: Positive

Review: "Worst purchase ever."
Sentiment: Negative

Review: "It works fine."
Sentiment: Neutral

Review: "The delivery was awful."
Sentiment:
```

Expected:

```text
Negative
```

The examples demonstrate the desired pattern.

---

# 14. Instruction Prompting

Clearly tell the model what to do.

Example:

> "Summarize the following article in exactly 5 bullet points."

The model receives:

```text
Instruction
+
Content
```

and produces:

```text
Output
```

This is one of the most fundamental prompting approaches.

---

# 15. Context + Instruction

A very useful pattern:

```text
Context
   +
Instruction
   ↓
LLM
   ↓
Output
```

Example:

> Context: The student has an exam tomorrow and knows basic Python.
>
> Instruction: Explain recursion using a simple analogy and one Python example.

The model now knows:

* who the answer is for
* what knowledge level to assume
* what it needs to explain
* how to explain it

---

# 16. Delimiters

When prompts contain lots of information, delimiters help separate different sections.

For example:

```text
Analyze the text between <TEXT> and </TEXT>.

<TEXT>
The customer reported that the package arrived late...
</TEXT>
```

Other delimiters:

```text
"""
text
"""
```

or:

```text
###
text
###
```

The exact delimiter isn't magical.

The purpose is **clear separation of information**.

---

# 17. Positive and Negative Instructions

Suppose you want an answer without jargon.

Instead of:

> "Explain databases."

Use:

> "Explain databases using simple language. Avoid advanced technical terminology unless necessary."

You can specify both:

### Do

> Use simple language.

### Don't

> Don't assume prior database knowledge.

This reduces ambiguity.

---

# 18. Prompt Templates

In real applications, prompts are rarely written manually every time.

Instead, we create templates.

For example:

```text
You are a customer-support assistant.

Customer message:
{customer_message}

Task:
Identify the customer's main issue.

Return:
1. Issue
2. Urgency
3. Recommended action
```

Then:

```text
customer_message =
"My order hasn't arrived after 10 days."
```

The application inserts the data into the template.

This is extremely important for AI applications.

---

# 19. Prompt Engineering in Agentic AI

Here's where things get interesting.

A normal chatbot might use:

```text
User → Prompt → LLM → Answer
```

An agent may use a much more detailed instruction:

```text
User Goal
   ↓
Agent Prompt
   ↓
LLM
   ↓
Decide what to do
   ↓
Use tool
   ↓
Observe result
   ↓
LLM
   ↓
Final answer
```

The prompt can define:

* what the agent's job is
* what tools it has
* when tools should be used
* what information it should remember
* what format it should return
* what constraints it must follow

So prompt engineering becomes part of **agent design**.

---

# 20. Example — Building a Travel Agent

Imagine we're building an AI travel agent.

### Bad prompt

> You are a travel assistant. Help users travel.

Too vague.

### Better prompt

> You are a travel planning assistant. Help users create practical itineraries based on their destination, budget, interests, and available time.

Better.

### Agent-oriented prompt

> You are a travel planning agent.
>
> Your responsibilities:
>
> * Understand the user's destination and dates.
> * Ask for missing critical information.
> * Search for relevant information when necessary.
> * Use available travel tools when real-time information is required.
> * Never invent booking availability.
> * Return the final itinerary in a day-by-day format.

Now we're defining **behavior**, not just asking a question.

---

# 21. Prompt Engineering vs Programming

This is an important distinction.

### Traditional programming

You explicitly define logic:

```text
IF temperature > 30
    THEN output "Hot"
```

### Prompt engineering

You describe desired behavior:

```text
Classify the temperature as:
Cold, Moderate, or Hot.
Explain your classification briefly.
```

The LLM uses learned patterns to perform the task.

But here's the skeptical bit:

> Prompting is powerful, but it isn't a replacement for deterministic programming.

For critical operations, we often combine both.

```text
LLM
 ↓
Decision
 ↓
Program logic / validation
 ↓
Tool
```

That's much safer.

---

# 22. Common Prompt Engineering Mistakes

### 1. Being too vague

❌

> "Tell me about databases."

### 2. No output format

❌

> "Analyze this data."

### 3. Too many contradictory instructions

❌

> "Be extremely detailed but keep it under 20 words."

### 4. Missing context

❌

> "Fix this code."

What code?

What language?

What's wrong?

### 5. Assuming the model knows hidden information

❌

> "Use our company's latest sales data."

Unless the model has access to that data, it can't magically retrieve it.

That's where **RAG and tools** become important.

---

# 23. A Powerful General Prompt Structure

For many tasks, this structure works well:

```text
ROLE
You are ...

CONTEXT
Here is the relevant background...

TASK
Your task is to...

CONSTRAINTS
- ...
- ...
- ...

OUTPUT FORMAT
Return the answer as...

EXAMPLES
Example 1...
Example 2...
```

You don't need every section every time.

Think of it as a **prompt toolbox**.

---

# 24. Worked Example

Suppose we want an AI to analyze student feedback.

### Weak prompt

> Analyze this feedback.

### Improved prompt

> You are a student-feedback analyst.
>
> Analyze the following feedback and identify the main complaint.
>
> Return:
>
> * sentiment
> * main_issue
> * urgency
> * recommended_action
>
> Feedback:
> "The professor explains concepts well, but the lecture slides are often uploaded several days late."

Expected output:

```text
sentiment: mixed
main_issue: delayed lecture slides
urgency: medium
recommended_action: upload slides promptly
```

Notice how the prompt defines:

```text
Role
+
Task
+
Output format
+
Input
```

That's good prompt engineering.

---

# Quick Revision Sheet

### Prompt Engineering

> **The process of designing effective instructions and context for an LLM to produce a desired output.**

### Important techniques

| Technique                 | Idea                            |
| ------------------------- | ------------------------------- |
| **Instruction prompting** | Clearly state the task          |
| **Zero-shot**             | No examples                     |
| **One-shot**              | One example                     |
| **Few-shot**              | Multiple examples               |
| **Role prompting**        | Define a role/persona           |
| **Context prompting**     | Provide relevant background     |
| **Structured output**     | Specify output format           |
| **Delimiters**            | Separate prompt sections        |
| **Constraints**           | Control length/style/behavior   |
| **Prompt templates**      | Reusable prompts with variables |

### MUST REMEMBER

**Good prompt = Clear task + relevant context + constraints + desired output format.**

And for Agentic AI:

> **The prompt isn't merely asking a question—it can define how the agent behaves.**

---

# Active Learning

### Conceptual Q1

What is the difference between **zero-shot** and **few-shot prompting**?

### Conceptual Q2

Why is specifying an **output format** useful when building an AI application?

### Conceptual Q3

Why isn't prompt engineering a complete replacement for traditional programming?

### Practical Q4

You want an LLM to classify customer complaints.

Write a prompt that tells the LLM to:

* act as a customer-support analyst
* classify the complaint as **Low / Medium / High**
* identify the main issue
* provide the output in a structured format

Send me your prompt. I'll evaluate it, and then we'll move to **Topic 3: Prompt Engineering Techniques**.
