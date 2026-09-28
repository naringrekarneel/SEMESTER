# Topic 4: Agents in LangChain

This is one of the **most important topics** in your syllabus because Agents combine what we've learned so far:

**LLM + Tools + Decision-making**

---

## 1. ELI5: What is an Agent?

Imagine you have an AI assistant.
You say:
> "Find the weather in Mumbai and tell me whether I should carry an umbrella."

A normal chain might have a fixed workflow:
```text
Question
 ↓
Weather API
 ↓
LLM
 ↓
Answer
```

But an **agent** can decide what to do.
It might think conceptually:
```text
What does the user need?
        ↓
I need current weather.
        ↓
Use weather tool.
        ↓
Check the result.
        ↓
Do I need another operation?
        ↓
No.
        ↓
Give answer.
```

So:
> **An agent is an LLM-powered system that decides which actions or tools to use to accomplish a goal.**

---

## 2. Agent = Brain + Tools

Remember our previous topic:
> **Tool = ability**

Now add an agent:
```text
                 AGENT
                   │
             ┌─────┼─────┐
             ↓     ↓     ↓
          Search  API  Calculator
             │     │     │
             └─────┼─────┘
                   ↓
                Results
                   ↓
                Agent
                   ↓
             Final Answer
```

The **agent decides which tool is appropriate**.

---

## 3. Why Do We Need Agents?

Chains work well when the workflow is known beforehand.
For example:
```text
Input
 ↓
Translate
 ↓
Summarize
 ↓
Format
```

But some tasks don't have a fixed sequence.
Example:
> "Research the latest developments in AI, compare them, calculate the percentage change in model performance, and summarize the findings."

The system might need to:
```text
Search
 ↓
Read information
 ↓
Search again
 ↓
Calculate
 ↓
Compare
 ↓
Summarize
```

The exact sequence isn't necessarily known in advance.
That's where agents become useful.

---

## 4. Basic Agent Architecture

```text
                    User
                      │
                      ▼
                  Agent / LLM
                      │
              "What should I do?"
                      │
          ┌───────────┼───────────┐
          ▼           ▼           ▼
       Search     Calculator    Database
          │           │           │
          └───────────┼───────────┘
                      ▼
                   Results
                      │
                      ▼
                  Agent / LLM
                      │
                More actions?
                 /         \
               Yes          No
                │            │
                ▼            ▼
             Tool          Answer
```

The key feature is the **decision loop**.

---

## 5. Agent Loop

An agent commonly follows this conceptual cycle:
```text
Observe
   ↓
Reason / Decide
   ↓
Act
   ↓
Observe Result
   ↓
Reason / Decide
   ↓
Act
   ↓
...
   ↓
Final Answer
```

This is sometimes called an **agent loop**.

### Example
User:
> "What is 15% of the current Bitcoin price?"

The agent might:
```text
1. Need current Bitcoin price
        ↓
2. Use price/search tool
        ↓
3. Get current price
        ↓
4. Need 15% calculation
        ↓
5. Use calculator
        ↓
6. Return result
```

The important part is that the agent can choose the next action based on what it observes.

---

## 6. Agent Components

A basic agent system contains:

```text
Agent
 │
 ├── LLM
 │
 ├── Tools
 │
 ├── Prompt / Instructions
 │
 ├── State / Context
 │
 └── Execution Loop
```

### LLM
Provides reasoning and language understanding.

### Tools
Provide capabilities.

### Prompt
Defines the agent's role and behavior.

### State
Keeps relevant information about the current task.

### Execution loop
Allows repeated tool use until the task is complete.

---

## 7. Agent vs Chain

This is **exam gold**.

| Feature | Chain | Agent |
| :--- | :--- | :--- |
| **Workflow** | Predefined | Dynamic |
| **Decision-making** | Limited | Yes |
| **Tool selection** | Usually fixed | Dynamic |
| **Flexibility** | Lower | Higher |
| **Predictability** | Higher | Lower |
| **Best for** | Structured tasks | Open-ended tasks |
| **Example** | Translate → Summarize | Research → Decide → Search → Calculate → Answer |

### Easy memory trick
> **Chain:** "Follow this path."
> **Agent:** "Find the path."

---

## 8. Example: Travel Assistant

Suppose the user says:
> "Plan a 3-day trip to Goa under ₹20,000."

Available tools:
```text
Flight Search
Hotel Search
Weather
Calculator
Maps
```

A fixed chain could struggle because the exact sequence might change.
An agent could reason:

```text
User wants Goa trip
        ↓
Search transportation
        ↓
Search hotels
        ↓
Check weather
        ↓
Calculate total cost
        ↓
Budget exceeded?
       / \
     Yes  No
      ↓    ↓
Search    Finish
cheaper
options
```

The agent dynamically determines what it needs.

---

## 9. Agent Tool Selection

Suppose the agent has:
```text
calculator
weather
web_search
database
email
```

User:
> "What's 45% of 800?"

Agent: `calculator`

User:
> "What's the weather tomorrow?"

Agent: `weather`

User:
> "Find my attendance."

Agent: `database`

User:
> "Send my professor an email."

Agent: `email`

The agent uses the **tool descriptions and input schemas** to determine which tool is appropriate.

---

## 10. Worked Example — Research Agent

Suppose the user asks:
> "Research the advantages and disadvantages of electric vehicles and give me a short report."

Available tools:
```text
Web Search
Calculator
Document Writer
```

### Step 1 — Understand task
```text
Need research
```

### Step 2 — Search
```text
Web Search
```

### Step 3 — Analyze information
The LLM processes the retrieved information.

### Step 4 — More research?
The agent may determine that additional information is needed.
```text
Search again
```

### Step 5 — Generate report
```text
Information
    ↓
LLM
    ↓
Report
```

The key difference is that the agent isn't forced to follow exactly:
```text
Search → Search → Calculator → Write
```
It can decide what actions are necessary.

---

## 11. Agents and Tool Calling

Modern agent systems commonly use **tool calling**.

Conceptually:
```text
User
 ↓
LLM
 ↓
Tool Call
 ↓
Tool Execution
 ↓
Tool Result
 ↓
LLM
 ↓
Another Tool?
 ↓
Yes → repeat
No → final answer
```

Example:
```text
User:
"Calculate the cost of 5 laptops at the current price."

        ↓
Agent
        ↓
Search Tool
        ↓
Price = ₹50,000

        ↓
Calculator
        ↓
₹2,50,000

        ↓
Agent
        ↓
Final Answer
```

---

## 12. Agent Types — Important Concept

You may encounter different agent designs.
Historically, LangChain included patterns such as:
* ReAct-style agents
* Tool-calling agents
* Structured chat agents

The exact APIs and recommended implementations can change between LangChain versions, so for exams focus first on the **architecture and concept**, rather than memorizing deprecated class names.

---

## 13. ReAct Concept

A famous agent pattern is **ReAct**:
> **Reason + Act**

The basic idea is:
```text
Reason
  ↓
Action
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
```text
Question
 ↓
Reason: Need weather
 ↓
Action: weather_tool
 ↓
Observation: 28°C, rain expected
 ↓
Reason: Need recommendation
 ↓
Final Answer
```

The important exam concept is:
> **ReAct combines reasoning with actions so an agent can interact with external tools and use their results to continue solving a task.**

---

## 14. Agents Can Use Multiple Tools

This is where agents become powerful.

Imagine:
```text
                 Agent
                   │
       ┌───────────┼────────────┐
       ↓           ↓            ↓
   Web Search   Calculator   Database
       │           │            │
       └───────────┼────────────┘
                   ↓
              Final Answer
```

The agent acts as an **orchestrator**.
It coordinates different capabilities.

---

## 15. Agent Advantages

1. **Flexibility:** Can handle tasks where the exact workflow isn't known beforehand.
2. **Tool usage:** Can interact with external systems.
3. **Dynamic decision-making:** Can determine which tool is appropriate.
4. **Multi-step problem solving:** Can perform several actions sequentially.
5. **Automation:** Can automate complex workflows.

---

## 16. Agent Limitations

Agents aren't automatically better at everything.

1. **Less predictable:** The exact sequence of actions can vary.
2. **Higher cost:** Multiple LLM calls and tool calls can consume more resources.
3. **Latency:** Several iterations may take longer.
4. **Errors:** A wrong decision can lead to the wrong tool or incorrect result.
5. **Security risks:** Tools may perform sensitive operations.

For example:
```text
Agent
 ↓
Delete Database
```
That's obviously something that should have strong safeguards.

---

## 17. Agent Safety

When agents interact with real systems, permissions matter.

A useful architecture is:
```text
                 Agent
                   ↓
              Tool Request
                   ↓
             Permission Check
              /          \
          Allowed       Denied
             ↓             ↓
       Execute Tool      Reject
             ↓
          Result
```

For sensitive operations, human confirmation may be appropriate.
Example:
> "I found the email. Do you want me to send it?"
rather than automatically sending it.

---

## 18. Chain → Tool → Agent

You should now see how the topics connect.

### Chain
```text
Fixed workflow
```

### Tool
```text
Specific capability
```

### Agent
```text
Dynamic decision-maker
```

Together:
```text
                 AGENT
                   │
          decides what to do
                   │
          ┌────────┴────────┐
          ↓                 ↓
        TOOL              TOOL
          │                 │
     Search API        Calculator
          │                 │
          └────────┬────────┘
                   ↓
                RESULT
```

---

## 19. Exam-Ready Definition

> **An agent in LangChain is an LLM-powered component that dynamically decides which actions or tools to execute to accomplish a user's goal. Unlike a fixed chain, an agent can select tools, use their results, perform multiple iterations and determine when the task is complete.**

---

## 📝 Quick Revision

### Remember these four words:
```text
LLM → DECIDE
Tool → ACT
Observation → RESULT
Agent → REPEAT
```

### Agent loop
```text
User
 ↓
Agent
 ↓
Decide
 ↓
Tool
 ↓
Observe result
 ↓
Decide again
 ↓
...
 ↓
Final Answer
```

### Most important distinction
> **Chain = fixed sequence**
> **Agent = dynamic sequence**

### Agent consists of
* LLM
* Tools
* Instructions/prompts
* State/context
* Execution loop

### ReAct
**Reason → Act → Observe → Repeat**

---

## 🧠 Active Learning

### Conceptual
**Q1.** What is an Agent, and how is it different from a Chain?
**Q2.** What is the role of tools in an agent?
**Q3.** Explain the basic **Reason → Act → Observe** cycle.

### Practical
You have an agent with these tools:
```text
1. Calculator
2. Weather API
3. Web Search
4. Database
5. Email
```

The user asks:
> **"Check tomorrow's weather in Mumbai. If rain is expected, email me a reminder to carry an umbrella."**

**Q4.** Which tools should the agent use, and in what order?

> *Reply **N** when you're ready for **Topic 5 — AutoGen Framework**.*
