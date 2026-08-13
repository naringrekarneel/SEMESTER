# Topic 3: Characteristics of Agentic Systems

Now we get into the **core characteristics that make a system truly agentic**.

The four big ones in your syllabus are:

1. **Autonomy**
2. **Memory**
3. **Planning**
4. **Feedback**

A useful way to remember them:

> **Agent = Can act independently + remember + plan + learn from results**

---

# 1. Autonomy

## ELI5

Suppose you tell your friend:

> "Clean my room."

A non-autonomous system might ask you:

> "Should I pick up the clothes?"

> "Should I organize the books?"

> "Should I clean the desk?"

An autonomous agent decides these things **by itself**.

So:

**Autonomy = ability to make decisions and perform actions without constant human instructions.**

---

## Example

You tell an AI:

> "Manage my calendar."

The agent can:

* inspect your schedule
* identify conflicts
* move meetings
* send invitations
* notify participants

You gave the **goal**, not every individual instruction.

---

## Levels of Autonomy

| Level  | Behavior                                    |
| ------ | ------------------------------------------- |
| Low    | Needs instructions for every action         |
| Medium | Makes some decisions independently          |
| High   | Plans and executes most tasks independently |

### Must remember

**Autonomy ≠ no human involvement.**

An agent can still ask for human approval for sensitive actions.

For example:

> "I found a ₹50,000 laptop. Should I purchase it?"

That's still an agentic system because it autonomously performed the research but requests approval before a high-risk action.

---

# 2. Memory

## ELI5

Imagine talking to someone who forgets everything immediately.

You say:

> "I prefer vegetarian food."

Five minutes later:

> "Here's a chicken restaurant!"

Not very useful.

An agent with memory can remember relevant information and use it later.

---

## Types of Memory

### Short-Term / Working Memory

Stores information needed **right now**.

Example:

```text
User wants:
- Delhi trip
- 3 days
- Budget ₹20,000
```

The agent uses this during the current task.

---

### Long-Term Memory

Stores information that can be used across future interactions.

Example:

> User prefers window seats.

Next time the agent books a flight, it can remember this preference.

---

## Why Memory Matters

Without memory:

```text
Conversation 1 → forgotten
Conversation 2 → starts from zero
```

With memory:

```text
Conversation 1
      ↓
Store useful information
      ↓
Conversation 2
      ↓
Use previous information
```

Memory gives agents **continuity**.

---

# 3. Planning

This is probably the **most important characteristic** for understanding agentic behavior.

## ELI5

Suppose I tell you:

> "Build me a house."

You don't randomly start putting bricks everywhere.

You create a plan:

```text
Choose land
↓
Create design
↓
Build foundation
↓
Build structure
↓
Install electricity
↓
Paint
```

That's planning.

An AI agent does the same thing with tasks.

---

## Definition

**Planning** is the process of deciding a sequence of actions required to achieve a goal.

The agent takes:

**Goal → Break into subtasks → Choose actions → Execute**

---

## Example: "Plan my trip to Goa"

An agent might create:

```text
Goal: Goa trip

1. Find travel dates
2. Search transportation
3. Compare hotels
4. Check budget
5. Book transportation
6. Book hotel
7. Create itinerary
```

The important thing is that the agent doesn't just generate text.

It creates a **sequence of actions**.

---

# Planning Can Change

Suppose the agent planned:

```text
Fly to Goa
↓
Check in
↓
Beach visit
```

But then it discovers:

> Flight cancelled.

A good agent doesn't say:

> "My plan has failed. Goodbye."

It replans:

```text
Flight cancelled
↓
Search trains
↓
Find available train
↓
Update hotel arrival time
↓
Continue trip
```

This is called **dynamic planning / replanning**.

---

# 4. Feedback

## ELI5

Imagine throwing a ball at a basket.

You check:

> Did I score?

If no:

> Try again differently.

That's feedback.

An agent does something similar.

---

## Definition

**Feedback is information obtained after an action that helps an agent evaluate the result and adjust future actions.**

---

# Example

Agent wants to send an email.

```text
Action:
Send email

↓

Feedback:
Delivery failed

↓

Reason:
Invalid email address

↓

New action:
Find correct address

↓

Send again
```

The agent uses the outcome to modify its behavior.

---

# Feedback Loop

```text
Goal
 ↓
Plan
 ↓
Action
 ↓
Observe Result
 ↓
Evaluate
 ↓
Feedback
 ↓
Update Plan
 ↓
Action Again
```

This loop is fundamental to intelligent behavior.

---

# Putting All Four Together

Let's take one example:

> **"Manage my travel booking."**

### Autonomy

Agent independently searches and compares options.

### Memory

Agent remembers:

* preferred airline
* budget
* window seat preference

### Planning

Agent creates a sequence:

```text
Search flights
↓
Compare options
↓
Check hotel
↓
Book
↓
Create itinerary
```

### Feedback

Suppose the flight becomes unavailable.

The agent notices this and replans.

---

# Complete Agentic Loop

```text
                ┌───────────────┐
                │     GOAL      │
                └───────┬───────┘
                        ↓
                  ┌───────────┐
                  │  PLANNING │
                  └─────┬─────┘
                        ↓
                  ┌───────────┐
                  │   ACTION  │
                  └─────┬─────┘
                        ↓
                  ┌───────────┐
                  │  OBSERVE  │
                  └─────┬─────┘
                        ↓
                  ┌───────────┐
                  │  FEEDBACK │
                  └─────┬─────┘
                        ↓
                  ┌───────────┐
                  │  MEMORY   │
                  └─────┬─────┘
                        │
                        └────────→ Replan
```

Autonomy controls **how independently** the agent operates throughout this loop.

---

# How the Four Characteristics Interact

This is a very important conceptual connection.

| Characteristic | Main Question                            |
| -------------- | ---------------------------------------- |
| **Autonomy**   | "Can it act independently?"              |
| **Memory**     | "Can it remember useful information?"    |
| **Planning**   | "Can it decide what to do next?"         |
| **Feedback**   | "Can it evaluate the result and adjust?" |

Together:

$$
\text{Agentic Intelligence} \approx \text{Autonomy} + \text{Memory} + \text{Planning} + \text{Feedback}
$$

This is a **conceptual formula**, not a mathematical equation used to calculate agent intelligence.

---

# Real-World Example: AI Customer Support Agent

Customer says:

> "My package hasn't arrived."

### Step 1 — Memory

Retrieve:

* customer details
* order ID
* previous complaints

### Step 2 — Planning

Decide:

```text
Check order
↓
Check shipment status
↓
Contact delivery service if needed
↓
Choose resolution
```

### Step 3 — Autonomy

The agent performs these actions without asking the employee at every step.

### Step 4 — Feedback

Suppose shipment tracking says:

> Package lost.

The agent updates its plan:

```text
Lost package
↓
Create replacement order
↓
Notify customer
```

That's a proper agentic system.

---

# Agentic vs Non-Agentic System

| Non-Agentic          | Agentic                  |
| -------------------- | ------------------------ |
| Gives one response   | Pursues a goal           |
| Mostly reactive      | Can proactively act      |
| Fixed behavior       | Can adapt                |
| Little/no memory     | Uses memory              |
| No planning          | Multi-step planning      |
| Limited feedback use | Continuous feedback loop |

---

# Exam Answer Structure

For a **7-mark question**:

### Introduction

Define Agentic AI.

### Main Body

Explain:

1. Autonomy
2. Memory
3. Planning
4. Feedback

For each, give:

* definition
* explanation
* example

### Conclusion

State that these characteristics allow an AI system to behave more like an autonomous problem-solving system rather than a simple input-output model.

---

# Must-Remember ⭐

**A = Autonomy → Act independently**

**M = Memory → Remember**

**P = Planning → Decide sequence**

**F = Feedback → Check and improve**

So remember:

> **A-M-P-F**

And the overall loop:

> **Goal → Plan → Act → Observe → Feedback → Replan**

---

# Quick Revision

* **Autonomy:** independent decision-making.
* **Memory:** retaining useful information.
* **Planning:** determining actions needed to reach a goal.
* **Feedback:** using results to improve or modify actions.
* Agentic systems combine all four to handle multi-step tasks dynamically.

---

# Active Learning

### Conceptual Questions

**1.** What is the difference between **autonomy** and **planning**?

**2.** Why is memory important for an AI agent?

**3.** Explain why feedback is necessary for an agent to adapt to changing situations.

### Practical Question

An AI agent is asked:

> **"Manage my online shopping order until it reaches my house."**

Explain how the agent would use **autonomy, memory, planning, and feedback** to complete this task.

Reply with your answers, or type **next** to move to **Topic 4: Types of Agents — Simple Reflex, Model-Based, Goal-Based, Utility-Based, and Learning Agents**.
