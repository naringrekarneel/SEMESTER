# Topic 14: Planning and Executing Multi-Step Tasks

This topic builds directly on **Multi-Step Task Decomposition**.

The key difference is:
> **Task decomposition breaks a goal into subtasks.**
> **Planning decides the order and method.**
> **Execution actually performs those actions.**

---

## 1. ELI5 — How Does an AI Agent Complete a Big Task?

Suppose you tell an AI agent:
> **“Create and deploy a website.”**

The agent needs to:
```text
Goal
 ↓
Understand task
 ↓
Break into subtasks
 ↓
Create a plan
 ↓
Execute first action
 ↓
Observe result
 ↓
Execute next action
 ↓
Check progress
 ↓
Replan if necessary
 ↓
Complete goal
```

So an intelligent agent doesn't simply create a list and blindly follow it.
It follows a **Plan → Act → Observe → Replan** cycle.

---

## 2. Planning vs Execution

### Planning
Planning determines:
> **What actions should be performed and in what order?**

Example:
```text
Write Code
   ↓
Run Tests
   ↓
Fix Errors
   ↓
Deploy
```

### Execution
Execution means actually performing those actions:
```text
Create files
   ↓
Run program
   ↓
Run tests
   ↓
Fix code
   ↓
Deploy application
```

---

## 3. General Architecture

A multi-step Agentic AI system can be represented as:

```text
             User Goal
                 ↓
        ┌─────────────────┐
        │ Goal Understanding│
        └────────┬────────┘
                 ↓
        Task Decomposition
                 ↓
             Planning
                 ↓
        ┌────────────────┐
        │ Action Selection│
        └───────┬────────┘
                ↓
             Execute
                ↓
          Observe Result
                ↓
           Evaluate
          ↙         ↘
      Success       Failure
        ↓              ↓
   Next Action      Replan
        ↓              ↓
        └──────→ Execute
```

This is one of the most important ideas in Agentic AI.

---

## 4. Step 1 — Goal Understanding

The agent first determines:
* What is the user's objective?
* What are the constraints?
* What resources are available?
* What counts as success?

Example:
> "Find me a laptop under ₹70,000 suitable for programming."

The agent identifies:
```text
Goal: Find suitable laptop
Budget: ₹70,000
Requirement: Programming
Success: Recommend suitable options
```

---

## 5. Step 2 — Task Decomposition

The goal is divided into smaller tasks.

```text
Find Laptop
    ↓
Search Products
    ↓
Filter by Budget
    ↓
Check Specifications
    ↓
Compare Options
    ↓
Select Suitable Options
```

---

## 6. Step 3 — Planning

Now the agent determines the correct execution order.

For example:
$$Search \rightarrow Filter \rightarrow Compare \rightarrow Select$$

Some tasks can be performed in parallel.
```text
             Search Laptop
             /           \
            ↓             ↓
       Check CPU      Check GPU
            \             /
             ↓           ↓
               Compare
                  ↓
               Select
```

---

## 7. Step 4 — Action Selection

The agent chooses the next action based on the current state.

For example:
```text
Current State:
No products found

Possible actions:
A1 → Search Web
A2 → Ask User
A3 → Stop

Policy/Planner
      ↓
Choose A1
```

The selected action is then executed.

---

## 8. Step 5 — Tool Selection

Agentic AI systems often have access to tools.
Different subtasks may require different tools.

| Task | Possible Tool |
| :--- | :--- |
| Search information | Web/Search |
| Calculate | Calculator |
| Write code | Code execution |
| Read document | File tool |
| Send email | Email tool |
| Query database | Database tool |

Therefore:
$$Task \rightarrow Appropriate\ Tool \rightarrow Action$$

Tool selection is a major part of practical agent execution.

---

## 9. Step 6 — Execute the Action

The agent performs the selected action.

Example:
```text
Plan:
Search for products
        ↓
Action:
Perform search
        ↓
Result:
20 laptops found
```

The environment now has a new state.

---

## 10. Step 7 — Observe the Result

After performing an action, the agent should inspect the result.

Example:
```text
Action: Search laptops

Result:
20 products found
```

The agent asks:
> **“Did this achieve what I expected?”**

If yes → continue.
If no → modify the plan.

---

## 11. Step 8 — Replanning

This is one of the most important characteristics of an intelligent agent.

Suppose the original plan is:
```text
Search → Compare → Buy
```

But the selected product becomes unavailable.
A rigid system might fail.
An agent can instead:

```text
Product unavailable
       ↓
Detect failure
       ↓
Search alternatives
       ↓
Compare alternatives
       ↓
Select new option
       ↓
Continue
```

This is called **replanning**.

---

## 12. Closed-Loop Execution

A simple automation system may work like:
$$Plan \rightarrow Execute$$

But an Agentic AI system generally works as:
$$Plan \rightarrow Execute \rightarrow Observe \rightarrow Evaluate \rightarrow Replan$$

This is called a **closed-loop approach**.

* **Open-loop:** Plan once → execute without checking.
* **Closed-loop:** Plan → execute → observe → adapt.

Closed-loop execution is much more suitable for uncertain environments.

---

## 13. Example — AI Coding Agent

Suppose the user says:
> **“Build a Python REST API.”**

The agent creates a plan:
```text
1. Understand requirements
2. Create project
3. Create API endpoints
4. Create database
5. Connect API to database
6. Write tests
7. Run tests
8. Fix failures
9. Run again
10. Deploy
```

Now imagine Step 7 produces:
```text
Test Failure:
Database connection error
```

The agent doesn't continue blindly. It does:
```text
Test Failure
     ↓
Analyze Error
     ↓
Identify Database Issue
     ↓
Modify Configuration/Code
     ↓
Run Tests Again
     ↓
Success
     ↓
Continue Deployment
```

This is **adaptive execution**.

---

## 14. Handling Dependencies

Some tasks depend on others.

Example:
$$A \rightarrow B \rightarrow C$$

where:
* A = Create database
* B = Connect API
* C = Test API

You cannot properly perform B before A.
A dependency graph can be represented as:

```text
Create Database
       ↓
Connect API
       ↓
Run Tests
       ↓
Deploy
```

The planner uses these dependencies to determine execution order.

---

## 15. Parallel Execution

If two tasks don't depend on each other, they can potentially execute simultaneously.

Example:
```text
                 Project
                /       \
               ↓         ↓
         Build Frontend  Build Backend
               \         /
                ↓       ↓
                 Integration
                     ↓
                   Testing
```

This can reduce total execution time.

---

## 16. Handling Failures

A robust agent needs an error-handling mechanism.

A general strategy is:
```text
Execute Action
      ↓
Did it succeed?
   /       \
 Yes        No
 ↓          ↓
Continue   Diagnose
              ↓
       Retry / Alternative
              ↓
           Replan
```

Possible responses to failure:
1. Retry the same action
2. Modify parameters
3. Choose another tool
4. Choose an alternative action
5. Ask the user for clarification
6. Abandon the failed branch

---

## 17. Goal Checking

The agent needs a **goal test**.

For example:
> Goal = Successfully deploy website.

The agent checks:
```text
Website deployed?
       ↓
     Yes → Goal achieved
     No  → Continue/Replan
```

Formally:
$$GoalTest(s) = True$$
means the current state satisfies the goal.
This connects directly to our earlier topic of **problem solving by search**.

---

## 18. Planning + MDP + RL Connection

Now connect everything we've learned:

```text
                 Complex Goal
                      ↓
             Task Decomposition
                      ↓
                   Planning
                      ↓
               Current State
                      ↓
              Choose Action
                      ↓
                 Execute
                      ↓
              New State + Reward
                      ↓
                  Evaluate
                  ↙       ↘
              Good        Bad
               ↓            ↓
           Continue       Replan
```

Different techniques can be used at different stages:

| Concept | Role |
| :--- | :--- |
| **Search** | Find a path/action sequence |
| **Planning** | Construct an action strategy |
| **MDP** | Model sequential decisions under uncertainty |
| **RL** | Learn good decisions from experience |
| **Policy** | Select actions |
| **Task decomposition** | Break complex goals into subtasks |
| **Tool use** | Execute real-world operations |

---

## 19. Advantages

1. **Adaptability:** The agent can respond to changing conditions.
2. **Error recovery:** Failures can be detected and corrected.
3. **Long-horizon task handling:** Complex tasks can be solved through multiple steps.
4. **Efficient tool usage:** Different tools can be selected for different subtasks.
5. **Better reliability:** The agent can verify results after each action.
6. **Goal-oriented behavior:** Actions are selected based on the final objective rather than generating random responses.

---

## 20. Challenges

1. **Planning errors:** A bad initial plan can lead to incorrect actions.
2. **Error propagation:** An incorrect early step may affect later steps.
3. **Tool failures:** External tools may fail or return unexpected results.
4. **Long-horizon complexity:** More steps mean more opportunities for errors.
5. **Replanning cost:** Constantly creating new plans can consume computational resources.
6. **Goal ambiguity:** If the user's objective is unclear, the agent may need clarification.

---

## 📝 Quick Revision

### Core Agentic AI loop:
$$\boxed{Plan \rightarrow Act \rightarrow Observe \rightarrow Evaluate \rightarrow Replan}$$

### Important concepts:
* **Planning** → Decide what to do.
* **Execution** → Perform the action.
* **Observation** → Check the result.
* **Evaluation** → Determine whether progress was made.
* **Replanning** → Modify the strategy when necessary.
* **Goal test** → Check whether the task is complete.

### Most important distinction:
> **A traditional automation system may follow a fixed sequence. An agentic system can observe results and adapt its next actions.**

---

## 💡 10-Mark Exam Structure

For **"Explain planning and execution of multi-step tasks in Agentic AI"**, write:
1. Definition
2. Goal understanding
3. Task decomposition
4. Planning
5. Action selection
6. Tool selection
7. Execution
8. Observation and evaluation
9. Replanning and error handling
10. Example + Agentic AI workflow

> **Next: Topic 15 — Connecting Search, Planning and Reinforcement Learning in Agentic AI.**
