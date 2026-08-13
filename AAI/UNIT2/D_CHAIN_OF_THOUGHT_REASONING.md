# Topic 4: Chain-of-Thought Reasoning

Now we're entering one of the most important ideas behind modern LLM reasoning.

So far:

```text
LLM → generates text
Prompt Engineering → tells it what we want
Prompting Techniques → improves how we ask
```

Now:

```text
Chain-of-Thought → helps with multi-step problems
```

---

# 1. ELI5 — What is Chain-of-Thought?

Imagine asking a student:

> If I have 3 boxes with 5 apples each, how many apples do I have?

They might think:

```text
3 boxes
×
5 apples
=
15 apples
```

The student didn't jump directly from question → answer.

They followed a sequence of intermediate steps.

That's the basic intuition behind **Chain-of-Thought (CoT) reasoning**.

> **Chain-of-Thought is a prompting/reasoning approach that encourages an LLM to solve a problem through multiple intermediate reasoning steps rather than jumping directly to the final answer.**

---

# 2. Why is Chain-of-Thought useful?

Simple questions don't need much reasoning.

Example:

> What is the capital of France?

Answer:

> Paris.

But consider:

> A train travels 60 km/h for 2.5 hours. How far does it travel?

The model needs to reason:

```text
Speed = 60 km/h
Time = 2.5 hours

Distance = Speed × Time

Distance = 60 × 2.5
         = 150 km
```

That's a multi-step problem.

CoT can help LLMs handle tasks involving:

* mathematics
* logic
* planning
* multi-step decisions
* code reasoning
* puzzles

---

# 3. Direct Answer vs Chain-of-Thought

### Direct prompting

```text
Question
   ↓
LLM
   ↓
Answer
```

### Chain-of-Thought

```text
Question
   ↓
Step 1
   ↓
Step 2
   ↓
Step 3
   ↓
Final Answer
```

The second approach gives the model a reasoning structure.

---

# 4. Simple Example

Question:

> John has 10 apples. He gives 3 to Sarah and buys 5 more. How many does he have?

### Direct

> 12

### Reasoning process

```text
Start = 10
Give away 3 → 10 - 3 = 7
Buy 5 → 7 + 5 = 12
```

Final:

> 12 apples.

The important idea is the **sequence of intermediate operations**.

---

# 5. Chain-of-Thought Prompting

A classic prompting approach is:

> **"Let's think step by step."**

For example:

> A store has 20 laptops. It sells 7 and receives 5 more. How many laptops are there now? Think step by step.

The model may produce:

```text
Initial = 20

After selling 7:
20 - 7 = 13

After receiving 5:
13 + 5 = 18

Answer = 18
```

The prompt encourages intermediate reasoning.

---

# 6. Why Does This Help?

One hypothesis is that difficult problems require multiple intermediate computations.

Without decomposition:

```text
Complex problem
      ↓
   Direct guess
```

With reasoning:

```text
Complex problem
      ↓
Break into steps
      ↓
Solve each step
      ↓
Combine results
```

It's similar to how humans solve complex problems.

---

# 7. Chain-of-Thought vs Normal Prompting

| Normal prompting      | Chain-of-Thought               |
| --------------------- | ------------------------------ |
| Direct answer         | Intermediate reasoning         |
| Good for simple tasks | Useful for multi-step tasks    |
| Less computation      | Potentially more computation   |
| Shorter output        | Often longer reasoning process |
| Simple classification | Math, logic, planning          |

---

# 8. Zero-Shot Chain-of-Thought

This is an important technique.

Instead of giving examples, you simply encourage reasoning.

Example:

> Solve the following problem step by step.

This is called:

> **Zero-Shot Chain-of-Thought**

The model doesn't receive worked examples.

It receives the reasoning instruction.

---

# 9. Few-Shot Chain-of-Thought

Now we combine:

```text
Few-shot examples
+
Reasoning demonstrations
```

Example:

```text
Question:
A box contains 5 red balls and 3 blue balls.
How many balls are there?

Reasoning:
5 + 3 = 8.

Answer:
8
```

Then provide another problem.

The model can follow the demonstrated reasoning pattern.

This is:

> **Few-Shot Chain-of-Thought**

---

# 10. Important Difference: Prompt Chaining

This confuses a LOT of students.

### Chain-of-Thought

One problem is solved through intermediate reasoning:

```text
Problem
 ↓
Reasoning step 1
 ↓
Reasoning step 2
 ↓
Answer
```

### Prompt Chaining

Multiple separate prompts/calls are connected:

```text
Prompt 1
 ↓
Output 1
 ↓
Prompt 2
 ↓
Output 2
 ↓
Prompt 3
```

### Remember:

> **CoT = reasoning steps**

> **Prompt chaining = multiple prompt executions**

---

# 11. Chain-of-Thought in Agentic AI

CoT becomes especially interesting when an agent needs to make decisions.

Suppose an AI agent is asked:

> "Find me the cheapest flight that arrives before 10 AM."

The agent may need to reason about:

```text
Destination
   ↓
Available flights
   ↓
Arrival times
   ↓
Prices
   ↓
Constraints
   ↓
Best option
```

But an actual agent also needs **actions**.

That leads us toward:

> **ReAct**

which combines reasoning with actions.

We'll study that next.

---

# 12. CoT and Tool Usage

Consider a math question.

The LLM can reason:

```text
I need to calculate 127 × 394.
```

Instead of relying entirely on internal reasoning, an agent could use a calculator tool:

```text
Reason
 ↓
Calculator tool
 ↓
Result
 ↓
Continue reasoning
```

So:

```text
CoT
+
Tools
=
More capable agent workflows
```

This distinction matters because LLM reasoning isn't always the best place to perform exact computation.

---

# 13. Chain-of-Thought and Hallucinations

CoT can sometimes improve reasoning accuracy, but it **doesn't guarantee correctness**.

An LLM can produce:

```text
Step 1 → incorrect
Step 2 → logically follows from Step 1
Step 3 → confidently wrong
```

So:

> **More reasoning ≠ guaranteed truth**

This is a crucial skeptical point.

For reliable systems, we can combine reasoning with:

* tools
* retrieval
* verification
* external computation
* self-correction

---

# 14. Self-Consistency

Now we combine CoT with another technique.

Suppose we ask the model to solve a difficult problem several times.

```text
             Problem
                ↓
      ┌─────────┼─────────┐
      ↓         ↓         ↓
   Reason 1  Reason 2  Reason 3
      ↓         ↓         ↓
     42        42        45
      └─────────┼─────────┘
                ↓
          Majority = 42
```

Instead of trusting one reasoning path, we look for agreement.

This is called:

> **Self-consistency**

---

# 15. Why Self-Consistency Can Help

Suppose:

```text
Path 1 → 42
Path 2 → 42
Path 3 → 42
Path 4 → 38
Path 5 → 42
```

Four paths agree.

Therefore:

```text
Final = 42
```

The intuition:

> Correct reasoning may converge on the same answer even if the intermediate paths differ.

---

# 16. Important Limitation

Self-consistency isn't magic either.

If the model consistently makes the same wrong assumption:

```text
Path 1 → Wrong
Path 2 → Wrong
Path 3 → Wrong
Path 4 → Wrong
Path 5 → Wrong
```

Majority voting still gives:

> Wrong.

So we should not confuse **agreement** with **truth**.

---

# 17. CoT in Mathematical Problems

Consider:

> A student scores 70, 80, and 90 in three tests. What is the average?

Reasoning:

```text
Sum = 70 + 80 + 90
    = 240

Number of tests = 3

Average = 240 / 3
        = 80
```

Final:

> 80

The reasoning decomposes the problem into smaller operations.

---

# 18. CoT in Logical Problems

Example:

> All cats are animals. Tom is a cat. Is Tom an animal?

Reasoning:

```text
All cats → animals

Tom → cat

Therefore:

Tom → animal
```

Final:

> Yes.

This kind of structured reasoning is useful for logical inference.

---

# 19. CoT in Coding

Suppose you're debugging:

```python
x = 10
y = 0
print(x / y)
```

A reasoning process might identify:

```text
x = 10
y = 0

Operation:
10 / 0

Division by zero is invalid.

Therefore:
ZeroDivisionError
```

Then the model can suggest:

```python
if y != 0:
    print(x / y)
```

Again, the task is decomposed into smaller reasoning steps.

---

# 20. CoT in Planning

Suppose an agent needs to organize a study plan.

Goal:

> Complete 20 chapters in 5 days.

The reasoning structure might be:

```text
20 chapters
÷
5 days
=
4 chapters/day
```

Then:

```text
Day 1 → Chapters 1–4
Day 2 → Chapters 5–8
Day 3 → Chapters 9–12
Day 4 → Chapters 13–16
Day 5 → Chapters 17–20
```

Planning problems benefit heavily from decomposition.

---

# 21. Chain-of-Thought vs ReAct

This distinction is **very important for Agentic AI exams**.

### Chain-of-Thought

```text
Reason
 ↓
Reason
 ↓
Reason
 ↓
Answer
```

### ReAct

```text
Reason
 ↓
Act
 ↓
Observe
 ↓
Reason
 ↓
Act
 ↓
Observe
 ↓
Answer
```

CoT focuses primarily on **reasoning**.

ReAct adds **interaction with the external world**.

---

# 22. A Simple Agent Example

User:

> "What is the population of Mumbai?"

### CoT-style system

```text
Question
 ↓
Reason using available knowledge
 ↓
Answer
```

Problem:

The information might be outdated.

### ReAct-style system

```text
Question
 ↓
Reason:
Need current information.
 ↓
Search tool
 ↓
Observe result
 ↓
Reason:
Use verified result.
 ↓
Answer
```

That's much closer to a true agent.

---

# 23. Modern Best Practice

Here's an important real-world lesson:

You don't always want the model to expose a huge chain of internal reasoning.

For many applications, it's better to ask for:

> **A concise explanation or brief justification**

rather than requiring verbose hidden reasoning.

For example:

Instead of:

> "Print every internal thought you have."

Use:

> "Solve the problem and provide a concise explanation of the key steps."

This keeps the output useful without unnecessarily exposing lengthy internal reasoning.

---

# Quick Revision Sheet

### Chain-of-Thought

> **A reasoning approach that decomposes complex problems into intermediate steps before reaching a final answer.**

### Main flow

```text
Problem
 ↓
Intermediate reasoning
 ↓
Conclusion
```

### Important variants

| Technique            | Meaning                                               |
| -------------------- | ----------------------------------------------------- |
| **Zero-shot CoT**    | Ask for step-by-step reasoning without examples       |
| **Few-shot CoT**     | Provide examples containing reasoning                 |
| **Self-consistency** | Generate multiple reasoning paths and compare answers |
| **Prompt chaining**  | Connect multiple LLM calls                            |
| **ReAct**            | Reason + Act + Observe                                |

### MUST REMEMBER

> **CoT helps an LLM decompose complex reasoning tasks.**

But:

> **CoT does not guarantee correctness.**

And:

> **ReAct extends reasoning by allowing the system to interact with tools/environment.**

---

# Active Learning

### Q1 — Conceptual

What is the main purpose of Chain-of-Thought reasoning?

### Q2 — Conceptual

What is the difference between **Chain-of-Thought** and **prompt chaining**?

### Q3 — Conceptual

Why doesn't self-consistency guarantee a correct answer?

### Q4 — Practical

An AI agent is asked:

> "Find the current price of a laptop online and tell me whether it is cheaper than ₹60,000."

Would **Chain-of-Thought alone** be enough? Explain what the agent would need to do differently.

Answer these, and then we'll move to the **big one: Topic 5 — ReAct (Reason + Act) Paradigm**.
