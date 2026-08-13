# Topic 4: Types of Intelligent Agents

This is a **very important exam topic**. You should know the five major types, their architecture, and the difference between them.

The five types are:

1. **Simple Reflex Agent**
2. **Model-Based Reflex Agent**
3. **Goal-Based Agent**
4. **Utility-Based Agent**
5. **Learning Agent**

The easiest way to understand them is as a progression:

> **React → Remember → Goal → Optimize → Learn**

---

# 1. Simple Reflex Agent

## ELI5

Imagine an automatic street light.

If:

> Dark → Turn ON

If:

> Bright → Turn OFF

It doesn't remember yesterday.

It doesn't think about tomorrow.

It simply follows a rule.

That's a **Simple Reflex Agent**.

---

## Definition

A **Simple Reflex Agent** selects actions based only on the **current percept** using predefined condition-action rules.

The basic rule is:

```text
IF condition THEN action
```

---

## Example

Automatic door:

```text
IF person detected
      ↓
Open door
```

```text
IF no person detected
      ↓
Close door
```

---

## Architecture

```text
Environment
     ↓
   Sensors
     ↓
Current Percept
     ↓
Condition-Action Rules
     ↓
   Actuators
     ↓
  Environment
```

---

## Advantages

* Very simple
* Fast
* Easy to implement
* Works well in predictable environments

## Disadvantages

* No memory
* Cannot handle hidden information well
* Cannot plan
* Cannot learn
* Fails when current perception is insufficient

---

# 2. Model-Based Reflex Agent

Now we make the agent a little smarter.

## ELI5

Suppose you're walking through a dark room.

You can't see everything at once.

But you remember:

> "There is a chair near me."

That internal knowledge helps you decide what to do.

That's the basic idea of a **Model-Based Reflex Agent**.

---

## Definition

A **Model-Based Reflex Agent** maintains an **internal state** representing aspects of the world that cannot be directly observed.

It uses:

* current percept
* previous information
* internal model

to choose an action.

---

## Architecture

```text
                 ┌────────────────┐
Environment ───→ │    Sensors     │
                 └───────┬────────┘
                         ↓
                  Current Percept
                         ↓
              ┌────────────────────┐
              │   Internal State   │
              │    + World Model   │
              └─────────┬──────────┘
                        ↓
                   Rules/Logic
                        ↓
                   Actuators
                        ↓
                   Environment
```

---

## Example: Robot Vacuum

A simple reflex vacuum might:

> IF obstacle → turn.

A model-based vacuum can remember:

> "I've already cleaned this room."

and maintain an internal representation of where it has been.

---

## Advantages

* Handles partially observable environments
* Maintains internal state
* More robust than simple reflex agents

## Disadvantages

* More complex
* Still mainly reactive
* Doesn't necessarily reason about long-term goals

---

# 3. Goal-Based Agent

Now the agent becomes **goal-oriented**.

## ELI5

Imagine you're going to college.

Your goal is:

> **Reach college.**

You can choose:

* Bus
* Train
* Auto
* Bike

The agent isn't just reacting.

It asks:

> **"Which actions will help me reach my goal?"**

---

## Definition

A **Goal-Based Agent** chooses actions by considering the **desired goal state** and determining which actions can lead to that goal.

---

## Example

Goal:

> Reach destination.

Possible actions:

```text
Take bus
Take train
Walk
Take taxi
```

The agent evaluates which actions can eventually reach the goal.

---

## Architecture

```text
Environment
     ↓
   Sensors
     ↓
Percepts + Internal State
     ↓
     Goals
     ↓
   Planning
     ↓
    Action
     ↓
Environment
```

---

## Example: Chess AI

Goal:

> **Checkmate the opponent.**

The agent considers possible moves and chooses actions that move toward the goal.

---

## Advantages

* Goal-oriented
* Can perform planning
* Handles multiple possible action sequences
* More flexible than reflex agents

## Disadvantages

* Planning can be computationally expensive
* Doesn't always distinguish between multiple equally successful solutions

For example, two routes may both reach college, but one takes 20 minutes and another takes 60.

A goal-based agent only needs to achieve the goal.

---

# 4. Utility-Based Agent

This is where things get interesting.

## ELI5

Suppose there are two routes to college:

**Route A**

* 20 minutes
* ₹50

**Route B**

* 30 minutes
* ₹20

Both reach college.

A goal-based agent says:

> "Both satisfy my goal."

A utility-based agent asks:

> "Which one is **better**?"

That's the key difference.

---

# Definition

A **Utility-Based Agent** chooses an action that maximizes a **utility function**, which measures how desirable or beneficial a particular outcome is.

---

## Utility Function

Conceptually:

$$
a^* = \arg\max_a U(a)
$$

where:

* $a$ = possible action
* $U(a)$ = utility of that action
* $a^*$ = best action

---

## Example

Suppose:

| Route |   Time | Cost | Utility |
| ----- | -----: | ---: | ------: |
| A     | 20 min |  ₹50 |    0.80 |
| B     | 30 min |  ₹20 |    0.65 |
| C     | 45 min |  ₹10 |    0.40 |

The agent chooses:

> **Route A**

because it has the highest utility.

---

## Utility vs Goal

This distinction is **very important**.

### Goal-Based Agent

Asks:

> "Does this action achieve the goal?"

### Utility-Based Agent

Asks:

> "Which action gives me the **best outcome**?"

---

## Advantages

* Handles competing objectives
* Makes better decisions under uncertainty
* Can compare different successful outcomes
* Useful for optimization

## Disadvantages

* Utility function can be difficult to design
* Requires more computation
* More complex than goal-based agents

---

# 5. Learning Agent

Now we reach the most advanced type in your syllabus.

## ELI5

Imagine teaching a child to play chess.

At first:

> Child = bad at chess.

After playing many games:

> Child = learns from mistakes.

Eventually:

> Child = becomes much better.

A **Learning Agent** improves its behavior based on experience.

---

# Definition

A **Learning Agent** is an agent that improves its performance over time by learning from experience, feedback, or interaction with the environment.

---

# Architecture of Learning Agent

A classical learning agent has **four major components**.

```text
                  ┌──────────────────┐
                  │    Environment   │
                  └────────┬─────────┘
                           ↓
                    ┌─────────────┐
                    │ Performance │
                    │   Element   │
                    └──────┬──────┘
                           ↓
                         Action
                           ↓
                    ┌─────────────┐
                    │ Environment │
                    └─────────────┘

          ┌────────────────────────────┐
          │       Learning Element     │
          └─────────────┬──────────────┘
                        ↓
                 Improves behavior

          ┌────────────────────────────┐
          │      Critic                │
          │  Provides feedback         │
          └────────────────────────────┘

          ┌────────────────────────────┐
          │ Problem Generator          │
          │ Suggests exploration       │
          └────────────────────────────┘
```

---

# Four Components

### 1. Performance Element

Chooses the actual action.

> "What should I do now?"

---

### 2. Learning Element

Improves the agent based on experience.

> "How can I do better next time?"

---

### 3. Critic

Evaluates performance.

> "Was that action good or bad?"

---

### 4. Problem Generator

Encourages exploration and tries new actions.

> "Let's try something different."

---

# Example: Recommendation System

Imagine Netflix recommending movies.

Initially:

```text
User watches random movies.
```

The system collects feedback:

```text
Watched fully → Positive signal
Skipped quickly → Negative signal
Liked → Strong positive signal
```

Over time, the system learns:

> "This user likes sci-fi and action."

Recommendations improve.

That's learning-agent behavior.

---

# Comparison of All Five Agents

This table is **exam gold**.

| Agent Type        | Main Idea               | Memory | Goals    | Utility  | Learning |
| ----------------- | ----------------------- | ------ | -------- | -------- | -------- |
| **Simple Reflex** | Condition → Action      | ❌      | ❌        | ❌        | ❌        |
| **Model-Based**   | Internal state          | ✅      | ❌        | ❌        | ❌        |
| **Goal-Based**    | Achieve desired goal    | ✅      | ✅        | ❌        | ❌        |
| **Utility-Based** | Maximize usefulness     | ✅      | ✅        | ✅        | ❌        |
| **Learning**      | Improve from experience | ✅      | Can have | Can have | ✅        |

---

# The Evolution of Intelligent Agents

Think of the agents as becoming progressively smarter:

```text
Simple Reflex
      ↓
Model-Based
      ↓
Goal-Based
      ↓
Utility-Based
      ↓
Learning Agent
```

### Simple Reflex

> "What should I do RIGHT NOW?"

### Model-Based

> "What is happening, considering what I know?"

### Goal-Based

> "What should I do to achieve my goal?"

### Utility-Based

> "Which option gives the BEST outcome?"

### Learning Agent

> "How can I get BETTER over time?"

---

# One Example Using All Five

Consider a **self-driving car**.

### Simple Reflex

> If obstacle → brake.

### Model-Based

> Track nearby vehicles and remember their positions.

### Goal-Based

> Reach destination safely.

### Utility-Based

Choose a route balancing:

* safety
* speed
* fuel
* comfort

### Learning Agent

Improve driving decisions from previous experiences and feedback.

This is a fantastic example to use in exams.

---

# Must-Remember ⭐

### Simple Reflex

**Condition → Action**

### Model-Based

**Condition + Internal State → Action**

### Goal-Based

**Goal → Plan → Action**

### Utility-Based

**Goal + Utility → Best Action**

### Learning

**Experience → Learn → Improve**

---

# Quick Revision Sheet

```text
Simple Reflex
→ Reacts to current percept

Model-Based
→ Uses internal state

Goal-Based
→ Plans toward a goal

Utility-Based
→ Chooses the best outcome

Learning Agent
→ Improves from experience
```

### Memory Trick

> **R-M-G-U-L**

**R**eact
**M**odel
**G**oal
**U**tility
**L**earn

---

# Exam Question Pattern

A very common question is:

> **"Explain different types of intelligent agents with suitable examples."**

For a strong 10-mark answer:

1. Define intelligent agent.
2. Explain Simple Reflex Agent.
3. Explain Model-Based Agent.
4. Explain Goal-Based Agent.
5. Explain Utility-Based Agent.
6. Explain Learning Agent.
7. Draw/describe architectures.
8. Give comparison table.
9. Conclude with progression from reactive to learning agents.

---

# Active Learning

### Conceptual Questions

**1.** What is the main difference between a **Goal-Based Agent** and a **Utility-Based Agent**?

**2.** Why does a **Model-Based Agent** need an internal state?

**3.** What are the four main components of a **Learning Agent**?

### Practical Question

A navigation AI has the following behavior:

> It remembers traffic conditions, has a goal of reaching the destination, compares routes based on time, cost, and safety, and improves its route selection from previous trips.

**Which type of agent is it? Explain exactly why.**

Reply with your answers, or type **next** for **Topic 5: PEAS Description and Task Environments**.
