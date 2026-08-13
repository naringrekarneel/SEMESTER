# Topic 5: ReAct — Reason + Act Paradigm

Now we hit one of the **core concepts of Agentic AI**.

So far we've learned:

```text
LLM
 ↓
Prompt Engineering
 ↓
Reasoning
```

But there's a problem.

An LLM can **think about what to do**, but by itself it can't necessarily:

* search the web
* query a database
* call an API
* check today's weather
* execute code
* send an email
* interact with an external system

That's where **ReAct** comes in.

---

# 1. ELI5 — What is ReAct?

Imagine you ask a human assistant:

> "What's the weather in Mumbai right now?"

They don't just sit there and guess.

They might think:

> "I need current weather information."

Then:

> "I'll check a weather service."

They check it.

Then:

> "It's 29°C and cloudy."

Then they tell you.

That's the ReAct idea:

```text
REASON
   ↓
ACT
   ↓
OBSERVE
   ↓
REASON
   ↓
ACT
   ↓
OBSERVE
   ↓
FINAL ANSWER
```

**ReAct = Reason + Act**

It combines language-model reasoning with actions in an external environment.

---

# 2. Why Do We Need ReAct?

A normal LLM looks like:

```text
User
 ↓
LLM
 ↓
Answer
```

The problem:

> The LLM may not have the information or capabilities required to complete the task.

For example:

> "What is the current USD/INR exchange rate?"

The model shouldn't simply guess.

Instead:

```text
User
 ↓
LLM
 ↓
Need current exchange rate
 ↓
Currency API
 ↓
Result
 ↓
LLM
 ↓
Answer
```

Now the LLM is acting as an **agent**.

---

# 3. Core ReAct Loop

The fundamental loop is:

```text
┌─────────────────┐
│      Goal       │
└────────┬────────┘
         ↓
     ┌───────┐
     │Reason │
     └───┬───┘
         ↓
     ┌──────┐
     │ Act  │
     └───┬──┘
         ↓
   ┌───────────┐
   │ Observe   │
   └─────┬─────┘
         ↓
      Reason
         ↓
       Act
         ↓
     Observe
         ↓
       ...
         ↓
    Final Answer
```

This loop continues until the task is complete.

---

# 4. The Three Main Components

## 1. Reason

The LLM determines what should happen next.

Example:

> "I need the current weather, so I should call the weather tool."

---

## 2. Act

The agent performs an action.

For example:

```text
weather_api(city="Mumbai")
```

---

## 3. Observe

The agent receives the result.

Example:

```text
Temperature: 29°C
Condition: Cloudy
Humidity: 76%
```

The LLM can then reason about this new information.

---

# 5. Simple Worked Example

User asks:

> **"What's the weather in Mumbai and should I carry an umbrella?"**

### Step 1 — Reason

```text
I need current weather information.
```

### Step 2 — Act

Call weather tool:

```text
weather("Mumbai")
```

### Step 3 — Observe

Tool returns:

```text
Temperature: 28°C
Condition: Rain
Rain probability: 85%
```

### Step 4 — Reason

```text
There is a high probability of rain.
An umbrella would be useful.
```

### Step 5 — Final answer

> Mumbai is currently rainy with an 85% chance of rain, so yes, carry an umbrella.

That's ReAct.

---

# 6. ReAct vs Chain-of-Thought

This is one of the most important exam comparisons.

| Chain-of-Thought                   | ReAct                                  |
| ---------------------------------- | -------------------------------------- |
| Focuses on reasoning               | Reasoning + actions                    |
| Usually works within model context | Can interact with external environment |
| No tool required                   | Can use tools                          |
| Problem → reasoning → answer       | Reason → act → observe → repeat        |
| Good for reasoning                 | Good for agentic tasks                 |

### Remember this:

> **CoT thinks.**

> **ReAct thinks and does.**

---

# 7. ReAct Example — Web Search

Question:

> "Who won yesterday's cricket match?"

The model's internal knowledge may be outdated.

A ReAct agent can do:

```text
User question
     ↓
Reason
"Need current information."
     ↓
Act
Search web
     ↓
Observe
Search results
     ↓
Reason
"Identify the relevant match."
     ↓
Act
Open source
     ↓
Observe
Match result
     ↓
Final answer
```

This is much more reliable than guessing.

---

# 8. ReAct Example — Database

Suppose you ask:

> "How many students scored above 80 in our database?"

The agent might reason:

```text
Need student records.
        ↓
Query database.
        ↓
SELECT COUNT(*)
WHERE marks > 80
        ↓
Database result = 147
        ↓
Return answer.
```

The LLM doesn't need to memorize the student database.

It uses a **tool**.

---

# 9. ReAct Example — Calculator

Question:

> "What is 18% of ₹75,000?"

The agent could:

```text
Reason:
Need exact calculation.

Action:
calculator(75000 × 0.18)

Observation:
13500

Final:
₹13,500
```

This is useful because deterministic tools can handle exact calculations better than relying on language generation alone.

---

# 10. ReAct Agent Architecture

A simplified architecture:

```text
                 USER
                   │
                   ▼
             ┌───────────┐
             │    LLM    │
             │  Reasoner │
             └─────┬─────┘
                   │
             Decide action
                   │
          ┌────────┼────────┐
          ▼        ▼        ▼
       Search     API     Database
        Tool      Tool       Tool
          │        │        │
          └────────┼────────┘
                   ▼
              Observation
                   │
                   ▼
                  LLM
                   │
              Continue / Finish
```

This is the basic architecture behind many agentic workflows.

---

# 11. What is an Action?

An **action** is something the agent does outside pure text generation.

Examples:

```text
Search web
```

```text
Query database
```

```text
Call API
```

```text
Run calculator
```

```text
Execute code
```

```text
Send notification
```

```text
Create calendar event
```

The exact tools depend on the system.

---

# 12. What is an Observation?

An observation is the information returned after an action.

Example:

```text
Action:
Search "Mumbai weather"

Observation:
29°C, cloudy
```

Then the LLM gets this information and decides what to do next.

---

# 13. ReAct as a Feedback Loop

This is a useful mental model:

```text
Goal
 ↓
Reason
 ↓
Action
 ↓
Environment
 ↓
Observation
 ↓
Updated knowledge
 ↓
Reason
 ↓
Action
 ↓
...
```

The agent is continuously updating its understanding based on what actually happens.

This is fundamentally different from simply generating a static answer.

---

# 14. ReAct and Environment

The **environment** is whatever exists outside the LLM that the agent can interact with.

Examples:

| Environment      | Possible action     |
| ---------------- | ------------------- |
| Web              | Search              |
| Database         | SQL query           |
| Weather service  | API call            |
| File system      | Read/write file     |
| Calendar         | Create event        |
| Calculator       | Perform calculation |
| Code environment | Execute code        |

So:

```text
LLM
 ↕
Environment
```

The LLM decides actions, and the environment returns observations.

---

# 15. ReAct Example — Shopping Agent

User:

> "Find me a laptop under ₹60,000 with 16 GB RAM."

A simplified agent might perform:

### Reason

> Need current products matching constraints.

### Act

Search shopping sources.

### Observe

```text
Laptop A — ₹58,000 — 16 GB
Laptop B — ₹65,000 — 16 GB
Laptop C — ₹55,000 — 8 GB
```

### Reason

> A matches the budget and RAM requirement.

### Act

Open product details.

### Observe

```text
Laptop A:
16 GB RAM
₹58,000
512 GB SSD
```

### Final

> Laptop A meets the specified requirements at ₹58,000.

The important part isn't the specific product.

It's the **agent loop**.

---

# 16. ReAct Can Perform Multiple Actions

An agent doesn't have to use only one tool.

Suppose:

> "Find the cheapest laptop under ₹60,000 and tell me whether it can run a particular game."

It might do:

```text
Reason
 ↓
Search laptops
 ↓
Observe
 ↓
Select candidate
 ↓
Search GPU specifications
 ↓
Observe
 ↓
Compare with game requirements
 ↓
Reason
 ↓
Final answer
```

Multiple actions can be chained dynamically.

That's where Agentic AI becomes powerful.

---

# 17. ReAct vs Traditional Workflow

### Traditional workflow

The developer explicitly defines every step:

```text
Step 1 → Search
Step 2 → Parse
Step 3 → Calculate
Step 4 → Answer
```

### ReAct

The LLM can dynamically determine the next action:

```text
Goal
 ↓
LLM decides
 ↓
Tool
 ↓
Result
 ↓
LLM decides next step
 ↓
Tool
 ↓
...
```

This makes agents more flexible.

But it also introduces unpredictability.

---

# 18. Advantages of ReAct

### 1. External knowledge

Agents can obtain information beyond their internal model knowledge.

### 2. Tool usage

Agents can interact with APIs and software.

### 3. Dynamic planning

The next action can depend on the previous observation.

### 4. Better task completion

Complex tasks can be broken into multiple actions.

### 5. Adaptability

If a tool returns unexpected information, the agent can react.

---

# 19. Limitations of ReAct

This is important for exams.

### 1. Tool errors

The API may fail.

```text
API → ERROR
```

The agent needs to handle it.

### 2. Wrong actions

The LLM may select an inappropriate tool.

### 3. Infinite loops

A poorly designed agent might repeatedly:

```text
Reason → Act → Observe
```

without reaching a conclusion.

Therefore systems often have:

* maximum iterations
* timeouts
* validation
* fallback mechanisms

### 4. Cost

Every reasoning/tool interaction can require additional computation or API calls.

### 5. Security risks

Giving an LLM powerful tools can be dangerous if permissions aren't controlled.

---

# 20. ReAct and Tool Permissions

Imagine an agent has:

```text
Search
Database Read
Database Write
Send Email
Delete File
```

You probably don't want the agent to freely use everything.

A safer architecture is:

```text
LLM
 ↓
Permission layer
 ↓
Tool
```

For example:

```text
LLM requests:
DELETE file

Permission layer:
❌ Not allowed

Tool is not executed.
```

This becomes very important when building real-world agents.

---

# 21. ReAct Pseudocode

Here's the basic algorithm:

```text
Goal = user request

while task is not complete:

    reasoning = LLM(goal, observations)

    if reasoning requires an action:
        action = choose_tool(reasoning)

        observation = execute(action)

        add observation to context

    else:
        return final answer
```

Conceptually:

```text
while not done:
    Reason
    if action needed:
        Act
        Observe
    else:
        Answer
```

### MUST REMEMBER

That's basically ReAct.

---

# 22. Full ReAct Worked Example

User:

> "What is 25% of the current price of Product X?"

Suppose the agent has a product search tool and calculator.

### Cycle 1

**Reason**

> I need the current price.

**Act**

```text
search_product("Product X")
```

**Observe**

```text
Price = ₹40,000
```

### Cycle 2

**Reason**

> I need to calculate 25% of ₹40,000.

**Act**

```text
calculator(40000 × 0.25)
```

**Observe**

```text
₹10,000
```

### Final

> 25% of the current price is ₹10,000.

Notice what happened:

```text
Reason
 ↓
Search
 ↓
Observe
 ↓
Reason
 ↓
Calculate
 ↓
Observe
 ↓
Answer
```

That's a textbook ReAct workflow.

---

# 23. The Most Important Diagram

Memorize this:

```text
                 ┌─────────────┐
                 │    GOAL     │
                 └──────┬──────┘
                        ↓
                 ┌─────────────┐
                 │    REASON   │
                 └──────┬──────┘
                        ↓
                 ┌─────────────┐
                 │     ACT     │
                 └──────┬──────┘
                        ↓
                 ┌─────────────┐
                 │   OBSERVE   │
                 └──────┬──────┘
                        ↓
                     REASON
                        ↓
                      ACT
                        ↓
                    OBSERVE
                        ↓
                       ...
                        ↓
                 ┌─────────────┐
                 │ FINAL ANSWER│
                 └─────────────┘
```

---

# ReAct vs CoT vs Prompt Chaining

This comparison is **exam gold**.

| Feature                 | CoT                  | Prompt Chaining    | ReAct             |
| ----------------------- | -------------------- | ------------------ | ----------------- |
| Main idea               | Reason through steps | Connect prompts    | Reason + interact |
| Multiple steps          | Yes                  | Yes                | Yes               |
| External tools          | Not required         | Not required       | Often used        |
| Environment interaction | No                   | Usually no         | Yes               |
| Dynamic actions         | Limited              | Predefined         | Yes               |
| Main purpose            | Reasoning            | Task decomposition | Agentic behavior  |

### One-line memory trick

> **CoT = Think**

> **Prompt Chaining = Split**

> **ReAct = Think + Do**

---

# Quick Revision Sheet

### ReAct

**ReAct = Reason + Act**

Core loop:

```text
Reason → Act → Observe → Reason → Act → ...
```

### Components

* **Reason:** decide what to do
* **Act:** execute a tool/action
* **Observe:** receive result
* **Repeat:** continue until goal is achieved

### Applications

* Web search
* Database queries
* API calls
* Calculations
* Code execution
* Automation
* Research agents
* Customer-support agents

### Advantages

* Dynamic decision-making
* External information
* Tool interaction
* Complex task execution

### Limitations

* Tool failures
* Incorrect actions
* Loops
* Cost
* Security risks

---

# Exam Answer Structure — "Explain ReAct"

If this appears for 7–10 marks, write:

1. **Definition**
2. **Reason + Act concept**
3. **ReAct architecture**
4. **Reason → Act → Observe loop**
5. **Worked example**
6. **Applications**
7. **Advantages**
8. **Limitations**
9. **Conclusion**

That will give you a very solid answer.

---

# Active Learning

### Q1 — Conceptual

What are the **three main stages** in the ReAct loop?

### Q2 — Conceptual

What is the key difference between **ReAct and Chain-of-Thought**?

### Q3 — Conceptual

Why can an agent get stuck in an infinite loop, and how can we prevent it?

### Q4 — Practical

An AI assistant receives:

> **"Check my database and tell me how many students scored above 90."**

Describe the **Reason → Act → Observe** sequence the ReAct agent would follow.

Once you're comfortable, say **NEXT** and we'll move to **Topic 6: Tool Usage & Function Calling** — where we'll see exactly how an LLM actually communicates with tools.
