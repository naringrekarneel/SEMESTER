# Topic 6: Architecture of Intelligent Agents

Now we connect everything we've learned so far.

You already know:

* what an agent is
* Model vs Workflow vs Agent
* autonomy, memory, planning, feedback
* types of agents
* PEAS and task environments

The **architecture of an intelligent agent** answers:

> **"How are all these parts organized so the agent can actually work?"**

This is a very important exam topic.

---

# 1. ELI5 Explanation

Imagine a human body.

You have:

* **Eyes and ears** → perceive the world
* **Brain** → think and decide
* **Memory** → remember information
* **Hands and legs** → perform actions

An intelligent agent works in a similar way.

```text
Environment
     ↓
  Sensors
     ↓
   Agent
     ↓
 Actuators
     ↓
Environment
```

The agent sits between **perception** and **action**.

---

# 2. Formal Definition

The **architecture of an intelligent agent** is the structural framework that defines how an agent's perception, reasoning, memory, planning, decision-making, learning, and action components interact with the environment.

A simple representation is:

$$
\text{Agent} = \text{Architecture} + \text{Agent Program}
$$

Where:

* **Architecture** = the platform or structure on which the agent operates.
* **Agent Program** = the logic that maps percepts to actions.

---

# 3. Basic Agent Architecture

The simplest architecture is:

```text
             ENVIRONMENT
                  ↓
               Sensors
                  ↓
          ┌──────────────┐
          │    AGENT     │
          │              │
          │ Perception   │
          │ Reasoning    │
          │ Decision     │
          └──────┬───────┘
                 ↓
              Actuators
                 ↓
             ENVIRONMENT
```

The basic cycle is:

> **Sense → Think → Act**

---

# 4. Main Components

## 1. Sensors

Sensors receive information from the environment.

Examples:

* Camera
* Microphone
* GPS
* Temperature sensor
* User input

```text
Environment → Sensors → Percepts
```

---

## 2. Perception Module

The raw sensor information is interpreted.

For example:

Camera gives:

> Pixels

Perception system determines:

> "There is a pedestrian."

So:

**Raw data → Meaningful information**

---

## 3. Internal State / Memory

The agent stores information about the world and previous interactions.

Example:

> "This road was blocked 5 minutes ago."

Memory is especially important when the environment is **partially observable**.

---

## 4. Reasoning / Decision-Making

The agent determines what should happen next.

Example:

> Pedestrian detected → Slow down.

---

## 5. Planning Module

For complex tasks, the agent creates a sequence of actions.

Example:

```text
Goal: Reach destination

Find route
↓
Avoid traffic
↓
Drive
↓
Recalculate route
↓
Reach destination
```

---

## 6. Learning Module

A learning agent improves based on experience.

Example:

> Previous route had heavy traffic.

Next time:

> Choose another route.

---

## 7. Actuators

Actuators perform the chosen action.

Examples:

* Robot motors
* Steering
* Brake
* Speaker
* API calls
* Sending messages

```text
Decision → Actuator → Environment
```

---

## 8. Feedback

The agent observes the result of its action.

Example:

```text
Action:
Turn left

↓

Feedback:
Road blocked

↓

New plan:
Take another route
```

This creates the closed-loop behavior we discussed earlier.

---

# 5. A More Complete Agent Architecture

A modern agent can look like this:

```text
                  ┌──────────────────────┐
                  │      Environment     │
                  └──────────┬───────────┘
                             ↓
                          Sensors
                             ↓
                     ┌──────────────┐
                     │  Perception  │
                     └──────┬───────┘
                            ↓
                     ┌──────────────┐
                     │    Memory    │
                     └──────┬───────┘
                            ↓
                     ┌──────────────┐
                     │   Reasoning  │
                     └──────┬───────┘
                            ↓
                     ┌──────────────┐
                     │   Planning   │
                     └──────┬───────┘
                            ↓
                     ┌──────────────┐
                     │  Decision    │
                     └──────┬───────┘
                            ↓
                         Actuators
                            ↓
                     Environment
                            ↑
                         Feedback
```

This architecture is much closer to how modern agentic systems are conceptualized.

---

# 6. Types of Agent Architectures

There are several important architectures.

## A. Reactive Architecture

The agent responds directly to current input.

```text
Input → Rule → Action
```

Example:

> Obstacle detected → Stop.

### Characteristics

* Fast
* Simple
* Little/no planning
* Little/no memory

This is closely related to **Simple Reflex Agents**.

---

# B. Model-Based Architecture

The agent maintains an internal representation of the environment.

```text
Perception
   ↓
Internal State
   ↓
Reasoning
   ↓
Action
```

Useful when the world is partially observable.

Example:

A robot remembers where obstacles are located.

---

# C. Goal-Based Architecture

The architecture includes explicit goals.

```text
Current State
     +
    Goal
     ↓
  Planning
     ↓
  Action
```

Example:

> Current location = Mumbai
> Goal = reach Delhi

The agent searches for actions that achieve the goal.

---

# D. Utility-Based Architecture

Now we introduce preferences.

```text
Possible Actions
       ↓
Evaluate Utility
       ↓
Choose Best Action
```

Example:

Three routes all reach the destination.

The agent chooses the one with the best balance of:

* time
* cost
* safety

Conceptually:

$$
a^* = \arg\max_a U(a)
$$

---

# E. Learning Architecture

The system improves itself using experience.

```text
Environment
    ↓
Action
    ↓
Result
    ↓
Feedback
    ↓
Learning
    ↓
Improved Decision
```

A common conceptual structure is:

```text
              ┌─────────────────┐
              │ Learning Element│
              └────────┬────────┘
                       ↓
                  Improvement
                       ↓
                Performance
                   Element
                       ↓
                    Action
                       ↓
                 Environment
                       ↓
                   Feedback
                       ↓
                    Critic
```

---

# 7. Learning Agent Architecture: Four Components

This is worth memorizing for exams.

### 1. Performance Element

Chooses actions.

> "What should I do?"

### 2. Learning Element

Improves the system.

> "How can I perform better?"

### 3. Critic

Evaluates performance.

> "How good was that?"

### 4. Problem Generator

Suggests exploration.

> "What new thing should I try?"

---

# 8. Agent Architecture in Modern Agentic AI

Now let's connect classical AI agents to modern LLM-based agents.

A modern agent might contain:

```text
User Goal
   ↓
LLM / Reasoning Model
   ↓
Planner
   ↓
Memory
   ↓
Tool Selection
   ↓
Tool/API/Database
   ↓
Result
   ↓
Observation
   ↓
LLM
   ↓
Next Action
```

For example:

> "Find the cheapest flight and book it."

The system might:

1. Understand request.
2. Search flights.
3. Compare results.
4. Check constraints.
5. Select a flight.
6. Ask for approval.
7. Book it.
8. Verify booking.
9. Report result.

The **LLM is not necessarily the entire agent**.

That's a crucial concept.

---

# 9. Agent vs Agent Architecture

Don't confuse these.

### Agent

The **entity/system** performing the task.

### Architecture

The **internal structure** that allows the agent to operate.

Think:

> **Agent = worker**

> **Architecture = worker's organization/brain-body system**

---

# 10. Worked Example: Self-Driving Car

Let's map the architecture.

### Sensors

Camera, radar, LiDAR.

↓

### Perception

Detect:

> car ahead

> pedestrian

> traffic light

↓

### Memory

Remember:

> previous route

> map information

↓

### Reasoning

Determine:

> pedestrian is crossing

↓

### Planning

Plan:

> slow down → stop → resume

↓

### Decision

Brake.

↓

### Actuator

Apply brakes.

↓

### Feedback

Observe:

> Car stopped safely.

Then continue.

This is a complete agent architecture in action.

---

# 11. Classical vs Modern Architecture

| Classical Agent | Modern Agentic AI              |
| --------------- | ------------------------------ |
| Sensors         | User input, APIs, databases    |
| Perception      | LLM / vision model             |
| Internal state  | Context + memory               |
| Reasoning       | LLM/reasoning model            |
| Planning        | Planner/LLM                    |
| Actuators       | Tools/APIs                     |
| Feedback        | Tool results/environment       |
| Learning        | Feedback, training, adaptation |

The underlying idea hasn't disappeared.

It's still:

> **Perceive → Reason → Plan → Act → Observe → Repeat**

The technology has simply become much more powerful.

---

# Must-Remember ⭐

### Basic architecture

**Sensors → Agent → Actuators**

### More complete architecture

**Perception → Memory → Reasoning → Planning → Decision → Action → Feedback**

### Five major architecture ideas

* Reactive
* Model-based
* Goal-based
* Utility-based
* Learning

### Learning agent has four parts

* Performance Element
* Learning Element
* Critic
* Problem Generator

---

# Quick Revision

```text
ARCHITECTURE

Environment
     ↓
  Sensors
     ↓
 Perception
     ↓
  Memory
     ↓
 Reasoning
     ↓
 Planning
     ↓
 Decision
     ↓
 Actuators
     ↓
Environment
     ↑
 Feedback
```

Think of it as the agent's **brain + memory + senses + hands**.

---

# Active Learning

### Conceptual Questions

**1.** What is the difference between an **agent** and an **agent architecture**?

**2.** Why is memory important in a model-based or modern agentic architecture?

**3.** What are the four components of a classical **Learning Agent architecture**?

### Practical Question

Design a basic architecture for an **AI customer-support agent** that can:

> Understand a customer's complaint → check order history → decide the solution → issue a refund/replacement → notify the customer → verify completion.

Show the components in sequence:

**Input/Perception → Memory → Reasoning → Planning → Action/Tools → Feedback**

Reply with your answer, or type **next** for the final syllabus topic: **Applications of Agentic AI in Industry**.
