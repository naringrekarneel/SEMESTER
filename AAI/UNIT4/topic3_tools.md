# Topic 3: Tools in LangChain

## 1. ELI5: What is a Tool?

Imagine an AI assistant that knows how to talk but **can't actually do things**.

You ask:
> "What is 25 × 48?"

The LLM can probably calculate it.
But now ask:
> "What's the weather in Mumbai right now?"

The model needs access to **current information**.
Or:
> "Send an email to my professor."

The model needs access to an **email service**.

That's where **tools** come in.
> **A tool gives an LLM the ability to perform an external action or obtain information.**

Think of the LLM as the **brain**, and tools as its **hands and senses**.

---

## 2. Basic Architecture

```text
                 User
                  ↓
                 LLM
                  ↓
          Decide what to do
                  ↓
             Use Tool
          ↙      ↓       ↘
     Search   Calculator  API
          ↘      ↓       ↙
                Result
                  ↓
                 LLM
                  ↓
             Final Answer
```

The LLM doesn't necessarily perform the external operation itself.
It **requests the tool**, receives the result, and uses that result.

---

## 3. Examples of Tools

A LangChain application can have tools for:

| Tool | Purpose |
| :--- | :--- |
| **Calculator** | Mathematical calculations |
| **Web search** | Find current information |
| **Weather API** | Get weather data |
| **Database tool** | Query databases |
| **Python tool** | Execute Python operations |
| **File tool** | Read/write files |
| **Email tool** | Send/read emails |
| **Calendar tool** | Create/manage events |
| **Custom API** | Interact with your application |

---

## 4. Tool vs LLM

This distinction is important.

### LLM
Good at:
* Understanding language
* Reasoning
* Generating text
* Summarizing
* Explaining
* Deciding what action might be useful

### Tool
Good at:
* Performing a specific operation
* Accessing external data
* Interacting with an external system

Example:
```text
User:
"What is 12345 × 678?"

        ↓
       LLM
"Use calculator."

        ↓
   Calculator
"8,381,910"

        ↓
       LLM
"12345 × 678 = 8,381,910."
```

---

## 5. Why Tools Are Important

LLMs have limitations.
For example, an LLM may not inherently have:
* Live weather data
* Your database
* Your files
* Your calendar
* Your bank application
* Your company's internal systems

Tools bridge that gap.
So:
> **LLM + Tools = AI system capable of interacting with the outside world**

---

## 6. How a Tool Works

A tool normally has three important parts:

### 1. Name
Identifies the tool.
Example: `calculator`

### 2. Description
Explains what the tool does.
Example: `"Use this tool to perform mathematical calculations."`

### 3. Input schema
Defines what information the tool expects.
Example: `expression: string`

So conceptually:
```text
Tool
 ├── Name
 ├── Description
 └── Input Schema
```

The description is especially important for agents because it helps the LLM understand **when the tool should be used**.

---

## 7. Example: Calculator Tool

Suppose we have:
```text
calculator("25 * 48")
```

The tool receives:
```text
25 * 48
```
and returns:
```text
1200
```

The overall flow:
```text
User
 │
 ▼
"What is 25 × 48?"
 │
 ▼
LLM
 │
 ▼
Calculator Tool
 │
 ▼
1200
 │
 ▼
LLM
 │
 ▼
"25 × 48 = 1200"
```

---

## 8. Tool Calling

Modern LLM applications often use **tool calling**.

The model doesn't necessarily execute the tool directly.
Instead, it produces a structured request such as:
```text
Tool: calculator

Input:
{
    "expression": "25 * 48"
}
```

The application executes the tool.
Then the result is returned to the model.

```text
LLM
 ↓
Tool Call
 ↓
Application executes tool
 ↓
Tool Result
 ↓
LLM
 ↓
Final Response
```

This distinction is worth remembering:
> **The LLM decides/request a tool call; the application executes the tool.**

---

## 9. Custom Tools

One of the coolest things about LangChain is that you can create your **own tools**.

Suppose you're building a college assistant.
You could create:
```text
get_student_attendance()
```

The tool could access your attendance database.
Then the AI could respond to:
> "What's my attendance in Machine Learning?"

Conceptually:
```text
User
 ↓
LLM
 ↓
get_student_attendance()
 ↓
Database
 ↓
Attendance = 82%
 ↓
LLM
 ↓
"Your ML attendance is 82%."
```

---

## 10. Tool with an API

Suppose you create a weather tool.
```text
get_weather(city)
```

Internally:
```text
get_weather("Mumbai")
        ↓
Weather API
        ↓
JSON response
        ↓
Tool
        ↓
LLM
```

The user doesn't need to know about the API details.
The tool acts as the bridge.

---

## 11. Tools + Agents

This is where **Tools** and **Agents** connect.

A chain might say:
```text
Step 1 → Search
Step 2 → Calculator
Step 3 → Answer
```

But an agent can decide:
```text
User Question
      ↓
     Agent
      ↓
"What do I need?"
      ↓
 ┌────┴─────┐
 ↓          ↓
Search   Calculator
 ↓          ↓
 └────┬─────┘
      ↓
    Answer
```

For example:
> "Find the price of a laptop and calculate its price after 10% discount."

The agent might decide:
1. Search for laptop price.
2. Use calculator.
3. Return result.

---

## 12. Tool Selection

Imagine an AI has these tools:
```text
Tools:
├── calculator
├── weather
├── web_search
├── database
└── email
```

User:
> "What's 100 × 25?"

Agent chooses: `calculator`

User:
> "What's the weather in Mumbai?"

Agent chooses: `weather`

User:
> "Find my attendance."

Agent chooses: `database`

The **tool description and schema** help the model understand what each tool is designed for.

---

## 13. Worked Example — Student Assistant

Let's design an AI student assistant.

Available tools:
```text
1. calculator
2. attendance_database
3. timetable_database
```

User asks:
> "How many lectures can I bunk while maintaining 75% attendance?"

### Step 1
LLM understands the task.

### Step 2
It needs current attendance.
`attendance_database`

### Step 3
Database returns:
```text
Attended = 36
Total = 40
```

### Step 4
Calculator determines the allowable absences.

Current attendance:
$$\text{Attendance} = \frac{36}{40} \times 100 = 90\%$$

Suppose the student can miss $x$ more lectures while maintaining at least 75%:
$$\frac{36}{40+x} \geq 0.75$$

Solve:
$$36 \geq 30 + 0.75x$$
$$6 \geq 0.75x$$
$$x \leq 8$$

Therefore:
```text
Maximum additional lectures = 8
```
This demonstrates how multiple capabilities can work together.

---

## 14. Tool Safety

Tools can be powerful, so **giving an AI a tool also gives it potential ability to affect the real world**.

For example:
```text
read_email()
```
is relatively low risk.

But:
```text
send_email()
delete_database()
transfer_money()
```
can have significant consequences.

Good tool design therefore considers:
* Input validation
* Authentication
* Authorization
* Permissions
* Error handling
* Rate limits
* Logging
* Human confirmation for sensitive actions

This becomes especially important when we reach **Agents**.

---

## 15. Tool vs Chain vs Agent

You now have three important concepts:

| Concept | Meaning |
| :--- | :--- |
| **Tool** | Performs a specific action |
| **Chain** | Connects predefined steps |
| **Agent** | Decides which actions/tools to use |

### Memory trick
> **Tool = ability**
> **Chain = workflow**
> **Agent = decision-maker**

That's a very useful mental model.

---

## 16. Exam-Ready Definition

> **A tool in LangChain is a callable function or interface that allows an LLM-powered application to interact with external systems, retrieve information, or perform specific actions. Tools can include calculators, search engines, APIs, databases, file systems and custom functions.**

---

## 📝 Quick Revision

```text
             TOOLS
                │
       Give AI external abilities
                │
       ┌────────┼─────────┐
       ↓        ↓         ↓
   Calculator  Search     API
       ↓        ↓         ↓
       └────────┼─────────┘
                ↓
               LLM
```

### Must remember
* Tool = **specific capability**
* Tools can access **external systems**
* Tools can be built as **custom functions**
* Tools generally have:
  * Name
  * Description
  * Input schema
* LLM can request a tool call.
* Application executes the tool.
* Result is returned to the LLM.
* Agents can dynamically select among multiple tools.

### The golden distinction
> **LLM thinks → Tool does → LLM responds**

---

## 🧠 Active Learning

### Conceptual
**Q1.** What is a Tool in LangChain?
**Q2.** Why can't an LLM alone reliably provide current weather information?
**Q3.** What are the three important parts that describe a tool?

### Practical
You are building a **college AI assistant** with these capabilities:
* Check attendance
* Calculate marks
* Read timetable
* Send an email

**Q4.** Which of these should be implemented as tools, and what would you name each tool?

> *Answer whenever you're ready. Then we'll move to **Topic 4 — Agents**, where everything starts becoming much more autonomous.*
