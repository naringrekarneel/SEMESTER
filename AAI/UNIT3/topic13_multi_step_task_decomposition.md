# Topic 13: Multi-Step Task Decomposition

Now we move into the **core Agentic AI part** of the syllabus.

---

## 1. ELI5 — What is Task Decomposition?

Suppose you tell an AI agent:
> **“Plan a trip to Goa.”**

That's a big task. The agent shouldn't try to solve everything in one step.
It can break it into:

```text
Plan Goa Trip
      ↓
 ┌────┼────────┐
 ↓    ↓        ↓
Travel Hotel  Activities
 ↓     ↓        ↓
Search Book   Research
```

This is called **task decomposition**.
> **Task decomposition = Breaking a complex goal into smaller, manageable tasks.**

---

## 2. Why is Task Decomposition Needed?

Real-world tasks are usually **multi-step**.

For example:
> "Build and deploy a website."

This involves:
1. Understand requirements
2. Design UI
3. Create frontend
4. Create backend
5. Connect database
6. Test application
7. Fix errors
8. Deploy application
9. Verify deployment

An AI agent that can decompose the task can handle each step systematically.

---

## 3. Basic Structure

A complex task can be represented as:
$$Goal \rightarrow Subtasks \rightarrow Actions$$

Example:
```text
Goal: Order a Pizza
        ↓
   ┌────┴────┐
   ↓         ↓
Select      Pay
Pizza        ↓
   ↓       Confirm
Customize
   ↓
Add to Cart
```

Each subtask may itself contain smaller subtasks.
This creates a **hierarchical task structure**.

---

## 4. Task Decomposition Process

A typical agent follows these steps:

### Step 1: Identify the Goal
Determine exactly what needs to be achieved.
Example:
> "Book a hotel in Mumbai."

### Step 2: Break the Goal into Subtasks
For example:
```text
Book Hotel
   ↓
Find hotels
   ↓
Filter by price/location
   ↓
Compare options
   ↓
Select hotel
   ↓
Enter details
   ↓
Confirm booking
```

### Step 3: Determine Dependencies
Some tasks must happen before others.
For example:
```text
Search Hotel
     ↓
Compare Hotels
     ↓
Select Hotel
     ↓
Book Hotel
```
You can't properly book the hotel before selecting one.

### Step 4: Execute Subtasks
The agent executes each task in the appropriate order.

### Step 5: Monitor Results
After each step, the agent checks:
> Did the action succeed?

If not, it can modify the plan.

### Step 6: Replan if Necessary
If something changes:
```text
Original Plan
     ↓
Action fails
     ↓
Analyze problem
     ↓
Create alternative plan
     ↓
Continue
```
This ability is particularly important in **Agentic AI**.

---

## 5. Hierarchical Task Decomposition

Large tasks can be divided into multiple levels.
Example:
```text
Goal
│
├── Task 1
│   ├── Subtask 1.1
│   └── Subtask 1.2
│
├── Task 2
│   ├── Subtask 2.1
│   └── Subtask 2.2
│
└── Task 3
    ├── Subtask 3.1
    └── Subtask 3.2
```

This is called **hierarchical decomposition**.

### Example
Goal:
> Develop a mobile application.

```text
Develop App
│
├── Requirements
│   ├── Identify features
│   └── Define users
│
├── Development
│   ├── Frontend
│   └── Backend
│
├── Testing
│   ├── Unit testing
│   └── Integration testing
│
└── Deployment
    ├── Build
    └── Release
```

---

## 6. Types of Task Decomposition

### 1. Sequential Decomposition
Tasks are performed one after another.
```text
A → B → C → D
```
Example:
```text
Login → Select Product → Pay → Confirm
```

### 2. Parallel Decomposition
Independent tasks can be performed simultaneously.
```text
       ┌→ A ─┐
Start ─┤     ├→ Final
       └→ B ─┘
```
Example:
While planning a trip, the agent can simultaneously:
* Search flights
* Search hotels
* Search activities

### 3. Conditional Decomposition
The next task depends on the result of a previous task.
```text
Check Availability
       ↓
   Available?
    /      \
  Yes       No
  ↓         ↓
Book     Search Alternative
```

### 4. Recursive Decomposition
A task is repeatedly broken down until it becomes simple enough to execute.
```text
Large Task
   ↓
Task A + Task B
   ↓
Task A1 + Task A2
   ↓
Simple Actions
```

---

## 7. Task Dependencies

Not every subtask can be performed independently.
Suppose:
```text
Write Code → Test Code → Deploy Code
```
There is a dependency:
$$Write \rightarrow Test \rightarrow Deploy$$
Testing depends on the code being written.

This can be represented using a **Directed Acyclic Graph (DAG)**.
```text
Requirements
     ↓
Development
   ↙   ↘
Testing  Documentation
   ↓       ↓
   └──→ Deployment
```
Task dependencies help an agent determine the correct execution order.

---

## 8. Task Decomposition in Agentic AI

A typical Agentic AI workflow looks like:
```text
User Goal
    ↓
Goal Understanding
    ↓
Task Decomposition
    ↓
Planning
    ↓
Tool Selection
    ↓
Task Execution
    ↓
Observe Result
    ↓
Evaluate
    ↓
Replan if Needed
    ↓
Final Result
```

This is different from a simple chatbot that only generates a response.
An agent can **plan, act, observe, and adapt**.

---

## 9. Example — AI Coding Agent

User says:
> "Create a Python REST API and deploy it."

The agent could decompose it into:

### High-level task
$$Create\ and\ Deploy\ API$$

### Subtasks
```text
1. Understand requirements
       ↓
2. Create project structure
       ↓
3. Implement API
       ↓
4. Connect database
       ↓
5. Write tests
       ↓
6. Run tests
       ↓
7. Fix errors
       ↓
8. Build application
       ↓
9. Deploy
       ↓
10. Verify deployment
```

If testing fails:
```text
Test
 ↓
Failure
 ↓
Analyze Error
 ↓
Modify Code
 ↓
Run Test Again
```
This is **adaptive multi-step execution**.

---

## 10. Benefits of Task Decomposition

1. **Reduces complexity:** Large problems become smaller and easier to manage.
2. **Improves planning:** The agent can determine what must happen first.
3. **Enables parallel execution:** Independent tasks can be executed simultaneously.
4. **Easier error handling:** The agent can identify which subtask failed.
5. **Supports replanning:** The agent can change the remaining plan when the environment changes.
6. **Improves reliability:** Breaking a task into smaller steps makes verification easier.
7. **Enables tool usage:** Different subtasks can use different tools.

Example:
```text
Search → Web Tool
Calculate → Calculator
Code → Programming Tool
Email → Email Tool
```

---

## 11. Challenges

Task decomposition is powerful, but it has problems.

1. **Incorrect decomposition:** The agent may break a task into inappropriate subtasks.
2. **Missing dependencies:** The agent may execute tasks in the wrong order.
3. **Error propagation:** An early mistake can affect later tasks.
4. **Too many subtasks:** Excessive decomposition can make planning inefficient.
5. **Changing environments:** A plan may become invalid when new information appears.
6. **Long-horizon planning:** The more steps involved, the harder it becomes to maintain a correct plan.

---

## 12. Task Decomposition vs Planning

These are related but different.

| Task Decomposition | Planning |
| :--- | :--- |
| Breaks a large goal into smaller tasks | Determines how to achieve those tasks |
| Focuses on **what needs to be done** | Focuses on **how/when to do it** |
| Creates subtasks | Creates action sequence/strategy |
| Example: Search → Compare → Book | Example: Search flights before booking hotel |

### Easy memory:
> **Decomposition = WHAT?**
> **Planning = HOW?**

---

## 13. Connection with Previous Topics

This topic connects almost everything we've learned:

```text
Goal
 ↓
Task Decomposition
 ↓
State-Space Representation
 ↓
Search / Planning
 ↓
Action Selection
 ↓
MDP / RL
 ↓
Execute Action
 ↓
Observe Result
 ↓
Replan
```

So Agentic AI combines:
* Search
* Planning
* MDP
* Reinforcement Learning
* Policies
* Task decomposition

to create agents capable of solving complex tasks.

---

## 📝 Quick Revision

### Definition
> **Multi-step task decomposition is the process of breaking a complex goal into smaller, manageable subtasks that can be planned and executed individually.**

### Main process
$$Goal \rightarrow Decompose \rightarrow Plan \rightarrow Execute \rightarrow Observe \rightarrow Replan$$

### Types
1. Sequential
2. Parallel
3. Conditional
4. Recursive/hierarchical

### Important distinction
* **Decomposition → What tasks?**
* **Planning → How to accomplish them?**
* **Execution → Perform them.**
* **Replanning → Adapt when something changes.**

---

## 💡 10-Mark Exam Structure

For **"Explain Multi-Step Task Decomposition in Agentic AI"**, write:
1. Definition
2. Need for task decomposition
3. Basic decomposition process
4. Hierarchical decomposition
5. Sequential decomposition
6. Parallel decomposition
7. Conditional decomposition
8. Task dependencies
9. Example of an Agentic AI system
10. Benefits and challenges

> **Next: Topic 14 — Planning and Executing Multi-Step Tasks.**
