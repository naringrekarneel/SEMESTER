# Agentic AI Roadmap

We'll learn the syllabus in the order that builds the strongest foundation.

| Module       | Topics                                                                    | Importance |
| ------------ | ------------------------------------------------------------------------- | ---------- |
| **Module 1** | Introduction to Artificial Intelligence Agents                            | ⭐⭐⭐⭐⭐      |
| **Module 2** | Agent vs Model vs Workflow                                                | ⭐⭐⭐⭐⭐      |
| **Module 3** | Characteristics of Agentic Systems (Autonomy, Memory, Planning, Feedback) | ⭐⭐⭐⭐⭐      |
| **Module 4** | Types of Intelligent Agents                                               | ⭐⭐⭐⭐⭐      |
| **Module 5** | PEAS Description & Task Environments                                      | ⭐⭐⭐⭐☆      |
| **Module 6** | Architecture of Intelligent Agents                                        | ⭐⭐⭐⭐⭐      |
| **Module 7** | Applications of Agentic AI in Industry                                    | ⭐⭐⭐⭐☆      |
| **Revision** | Quick Revision Sheet + Mini Quiz + Connections                            | ⭐⭐⭐⭐⭐      |

---

# Topic 1: Introduction to Artificial Intelligence Agents

This is the **most important topic** because every other concept is built on it.

---

# ELI5 Explanation 🧒

Imagine you have two things:

* A **calculator**
* A **personal assistant**

The calculator only gives answers when you press buttons.

The personal assistant can:

* understand your request
* think about it
* plan what to do
* perform actions
* check whether the task is completed

The assistant is an **agent**.

An AI Agent is exactly like this digital assistant.

Instead of only answering questions, it can **observe, think, decide, and act** to achieve a goal.

---

# Formal Definition (Exam)

**Artificial Intelligence Agent**

> An AI Agent is an intelligent software system that perceives its environment, reasons about the information, makes decisions, and performs actions autonomously to achieve specific goals.

**Keywords to remember**

* Perceive
* Reason
* Decide
* Act
* Goal
* Autonomy

These words appear frequently in university exams.

---

# Real-Life Examples

## Example 1: Google Maps

You ask

> "Take me to college."

Google Maps

* observes traffic
* plans route
* changes route if traffic increases
* reaches destination

It behaves like an AI agent.

---

## Example 2: ChatGPT with Tools

You ask

> "Book my meeting and send an email."

The AI

* understands request
* checks calendar
* books meeting
* sends email
* confirms completion

This is an AI Agent.

---

## Example 3: Robot Vacuum

Robot vacuum

* senses dirt
* avoids walls
* remembers cleaned rooms
* goes to charging station

Again,

Observe → Think → Act

---

# The Agent Cycle

Every AI Agent follows the same loop.

```text
Environment
      │
      ▼
Observe (Sensors/Input)
      │
      ▼
Reason / Think
      │
      ▼
Plan
      │
      ▼
Take Action
      │
      ▼
Receive Feedback
      │
      ▼
Repeat
```

This loop is the heart of Agentic AI.

---

# Components of an AI Agent

| Component       | Purpose                         |
| --------------- | ------------------------------- |
| Environment     | World where the agent operates  |
| Sensors         | Collect information             |
| Memory          | Stores previous information     |
| Reasoning       | Makes decisions                 |
| Planner         | Creates action plan             |
| Actuators/Tools | Performs actions                |
| Feedback        | Checks whether action succeeded |

---

# How an AI Agent Works (Step by Step)

Suppose the task is:

**"Order a pizza."**

### Step 1

User gives instruction.

> Order a large cheese pizza.

↓

### Step 2

Agent understands request.

↓

### Step 3

Searches restaurants.

↓

### Step 4

Compares prices.

↓

### Step 5

Chooses best option.

↓

### Step 6

Places order.

↓

### Step 7

Checks confirmation.

↓

### Step 8

Reports success.

Notice that the AI didn't just answer—it **performed actions**.

---

# Core Idea of Agentic AI

Traditional AI:

```text
Question
      ↓
Answer
```

Agentic AI:

```text
Goal
   ↓
Think
   ↓
Plan
   ↓
Use Tools
   ↓
Take Actions
   ↓
Observe Result
   ↓
Improve
```

This is why Agentic AI is becoming so powerful.

---

# Key Concepts

### 1. Perception

Collecting information from the environment.

Examples:

* Camera
* Microphone
* Text input
* Sensors

---

### 2. Reasoning

Thinking about the collected information.

Example:

Traffic is heavy.

Take another route.

---

### 3. Planning

Breaking a large goal into smaller tasks.

Example:

Goal:

Book vacation.

Plan:

* choose destination
* compare hotels
* book flight
* reserve hotel
* send itinerary

---

### 4. Action

Executing the plan.

Examples:

* Send email
* Search internet
* Open application
* Book ticket
* Generate report

---

### 5. Feedback

Checking whether the task succeeded.

If not,

Plan again.

---

# Worked Example

### Problem

User:

> "Find the cheapest laptop under ₹60,000."

### Agent Workflow

**Observe**

Read user request.

↓

**Reason**

Budget = ₹60,000

Need laptop.

↓

**Plan**

* Search websites
* Compare prices
* Check ratings

↓

**Action**

Collect information.

↓

**Feedback**

Found 5 laptops.

↓

**Final Answer**

Recommend the best laptop.

Notice that the agent performs a sequence of decisions rather than giving an immediate response.

---

# Difference Between Normal AI and AI Agent

| Normal AI         | AI Agent                        |
| ----------------- | ------------------------------- |
| Answers questions | Completes tasks                 |
| Single response   | Multi-step workflow             |
| No planning       | Plans actions                   |
| No memory         | Can use memory                  |
| Usually passive   | Acts autonomously               |
| Limited tool use  | Uses tools and external systems |

---

# Exam Points (7–10 Marks)

A good answer should include:

1. Definition of AI Agent.
2. Components (Environment, Sensors, Memory, Reasoning, Planner, Actuator, Feedback).
3. Agent cycle (Observe → Reason → Plan → Act → Feedback).
4. Real-world examples (Google Maps, Robot Vacuum, ChatGPT with tools).
5. Advantages:

   * Automation
   * Better decision-making
   * Reduced human effort
   * Adaptability

---

# Must-Remember Points ⭐

* AI Agent = **Perceives + Reasons + Acts**
* Goal-oriented system
* Can work autonomously
* Uses planning and memory
* Interacts with the environment
* Learns from feedback
* Performs actions, not just predictions

---

# Quick Revision (30 Seconds)

* AI Agent = software that observes, thinks, plans, and acts.
* Main loop: **Observe → Reason → Plan → Act → Feedback → Repeat**.
* Goal-oriented and autonomous.
* Uses sensors, memory, planning, and tools.
* Examples: Google Maps, robot vacuum, autonomous customer support, AI assistants.

---

# Active Learning

### Conceptual Questions

1. What is an AI Agent? Write its definition in your own words.
2. Why is an AI Agent considered **goal-oriented** rather than just a question-answering system?
3. Explain the **Agent Cycle** (Observe → Reason → Plan → Act → Feedback) with a real-life example.

### Practical Question

A smart home AI receives this command:

> "I'm leaving for work."

Describe **step by step** how an AI agent would process this command using the **Observe → Reason → Plan → Act → Feedback** cycle.

Reply with your answers, and I'll review them before moving to **Topic 2: Agent vs Model vs Workflow**.
