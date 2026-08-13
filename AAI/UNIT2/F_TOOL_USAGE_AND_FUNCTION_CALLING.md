# Topic 6: Tool Usage & Function Calling

This is where an LLM goes from **"I can tell you what to do"** to **"I can actually do things."**

We already learned ReAct:

```text
Reason → Act → Observe → Reason → ...
```

Now we'll understand the **Act** part technically.

---

# 1. ELI5 — What is Tool Usage?

Imagine you have a very smart assistant.

You ask:

> "What is 25 × 48?"

The LLM can probably answer itself.

But then you ask:

> "What's today's weather in Mumbai?"

The LLM needs access to a weather service.

So we give it a **tool**.

```text
LLM
 ↓
"I need weather information."
 ↓
Weather Tool
 ↓
Weather API
 ↓
Current weather
 ↓
LLM
 ↓
Answer
```

A **tool** is an external capability that an LLM can invoke to accomplish a task.

---

# 2. What is Function Calling?

**Function calling** is a mechanism that allows an LLM to request that a specific function be executed with specific arguments.

For example, suppose our application provides:

```python
get_weather(city)
```

The LLM might determine:

```json
{
  "name": "get_weather",
  "arguments": {
    "city": "Mumbai"
  }
}
```

The application executes the function.

The result comes back to the LLM.

---

# 3. Very Important Distinction

The LLM usually **doesn't directly execute your Python function**.

Instead:

```text id="t7r7w7"
             LLM
              ↓
       Tool/Function Call
              ↓
       Your Application
              ↓
        Execute Function
              ↓
           Result
              ↓
             LLM
```

The application is the bridge.

This distinction is extremely important when designing agents.

---

# 4. Why Do We Need Tools?

LLMs have limitations.

They may not have:

* current information
* access to private databases
* ability to perform real-world actions
* exact computation capabilities
* access to your files
* access to APIs

Tools extend their capabilities.

### Examples

| Tool             | Capability          |
| ---------------- | ------------------- |
| Calculator       | Exact arithmetic    |
| Search           | Current information |
| Weather API      | Current weather     |
| Database         | Query data          |
| Email API        | Send email          |
| Calendar API     | Create events       |
| Code interpreter | Execute code        |
| File system      | Read/write files    |

---

# 5. Tool Calling Architecture

Here's the core architecture:

```text id="x7h0qa"
                   User
                    ↓
                   LLM
                    ↓
           "I need a tool."
                    ↓
             Tool Selection
                    ↓
             Function Call
                    ↓
             Application
                    ↓
             Execute Tool
                    ↓
              Tool Result
                    ↓
                   LLM
                    ↓
              Final Answer
```

This is one of the most important diagrams in Agentic AI.

---

# 6. Example — Weather Tool

Suppose our system provides:

```python
get_weather(city)
```

User asks:

> "What's the weather in Mumbai?"

The LLM determines:

```json
{
  "name": "get_weather",
  "arguments": {
    "city": "Mumbai"
  }
}
```

The application executes:

```python
get_weather("Mumbai")
```

Suppose it returns:

```json
{
  "temperature": 29,
  "condition": "Cloudy"
}
```

That result is sent back to the LLM.

The LLM then produces:

> "Mumbai is currently 29°C and cloudy."

---

# 7. What Does a Tool Definition Contain?

A tool generally has:

### 1. Name

```text id="jv0a4y"
get_weather
```

### 2. Description

```text id="h9wr3s"
Gets the current weather for a city.
```

### 3. Parameters

```text id="y2w0hb"
city: string
```

Conceptually:

```json id="u8e7jb"
{
  "name": "get_weather",
  "description": "Gets current weather for a city",
  "parameters": {
    "city": "string"
  }
}
```

The LLM uses this information to determine **when and how to call the tool**.

---

# 8. Function Calling Step-by-Step

Let's walk through the complete process.

### User

> "What's the weather in Mumbai?"

### Step 1 — Send request to LLM

The application sends:

```text id="wy6b7d"
User message
+
Available tools
```

The model sees that `get_weather` exists.

---

### Step 2 — LLM chooses tool

It produces something conceptually like:

```text id="j1i1ny"
Tool:
get_weather

Arguments:
city = Mumbai
```

---

### Step 3 — Application executes tool

```python id="tpxg7y"
get_weather("Mumbai")
```

---

### Step 4 — Tool returns result

```text id="ivqvfo"
29°C
Cloudy
```

---

### Step 5 — Result goes back to LLM

```text id="1t3d6m"
Tool result:
29°C, Cloudy
```

---

### Step 6 — LLM responds

> "Mumbai is currently 29°C and cloudy."

Complete loop:

```text id="z7g3r4"
User
 ↓
LLM
 ↓
Tool Call
 ↓
Application
 ↓
Tool
 ↓
Result
 ↓
LLM
 ↓
Final Answer
```

---

# 9. Function Calling vs Normal Text Generation

Without function calling:

```text id="f3e2y1"
User:
What's the weather?

LLM:
"The weather might be around 29°C..."
```

Potentially a guess.

With function calling:

```text id="g8stcx"
User
 ↓
LLM
 ↓
get_weather("Mumbai")
 ↓
Real API
 ↓
Current data
 ↓
LLM
 ↓
Answer
```

Much better for tasks requiring external information.

---

# 10. Multiple Tools

An agent can have multiple tools.

For example:

```text id="2jvq3b"
Tools:
├── web_search()
├── calculator()
├── get_weather()
├── query_database()
├── send_email()
└── create_calendar_event()
```

The LLM can choose which one is appropriate.

User:

> "What's 25% of today's Bitcoin price?"

Possible workflow:

```text id="f9a4p6"
Reason
 ↓
Need current Bitcoin price
 ↓
Use price/search tool
 ↓
Get price
 ↓
Use calculator
 ↓
Calculate 25%
 ↓
Final answer
```

This is agentic behavior.

---

# 11. Tool Selection

The LLM needs to understand:

> **Which tool should I use?**

Suppose we have:

```text id="s4n1pg"
calculator()
weather()
database()
search()
```

User asks:

> "What is 123 × 456?"

The appropriate tool is:

```text id="qmz8y1"
calculator()
```

Not:

```text id="p9v5sy"
weather()
```

The tool descriptions help the model select appropriately.

---

# 12. Tool Arguments

Tool calls often require parameters.

Example:

```text id="y8uvz6"
search(query)
```

User:

> "Find information about Transformer architecture."

The LLM might generate:

```json id="fnm3o7"
{
  "name": "search",
  "arguments": {
    "query": "Transformer architecture"
  }
}
```

The application executes the function using that argument.

---

# 13. Required vs Optional Parameters

Suppose:

```text id="6yb4v7"
book_flight(
    destination,
    date,
    passengers
)
```

All three may be required.

But another tool could have:

```text id="6nb3n5"
search(
    query,
    max_results = 10
)
```

Here:

* `query` → required
* `max_results` → optional

Clear parameter definitions reduce tool-calling errors.

---

# 14. Tool Calling and Structured Data

Notice something interesting.

We previously learned **structured output**.

Function calling takes that idea further.

Instead of:

```text id="u2w6x9"
"Maybe call the weather tool for Mumbai..."
```

we want structured information:

```json id="v9b1hj"
{
  "tool": "get_weather",
  "arguments": {
    "city": "Mumbai"
  }
}
```

The application can reliably parse this.

Therefore:

> **Function calling is a structured interface between an LLM and external functions.**

---

# 15. Example — Database Agent

Suppose the company has:

```text id="h5nq1p"
Students
---------
id
name
marks
```

User:

> "How many students scored above 90?"

Available tool:

```text id="8e7c9m"
query_database(sql)
```

The LLM might generate a query:

```sql id="6sv3wq"
SELECT COUNT(*)
FROM Students
WHERE marks > 90;
```

The application sends it to the database.

Database returns:

```text id="d7m9ne"
147
```

LLM:

> "147 students scored above 90."

---

# 16. Tool Calling vs API Calling

These terms are related but not identical.

### API

An API is an interface through which software communicates with another service.

Example:

```text id="kq4e2m"
Your App → Weather API
```

### Tool

A tool is a capability exposed to an agent.

That tool may internally use an API.

```text id="f8d8q0"
LLM
 ↓
Weather Tool
 ↓
Weather API
 ↓
Weather Service
```

So:

> **A tool can be a wrapper around an API.**

---

# 17. Tool Usage in ReAct

Now connect today's topic to the previous one.

ReAct:

```text id="j8n2sv"
Reason
 ↓
Act
 ↓
Observe
```

Function calling implements the **Act** stage.

For example:

```text id="q2g5me"
Reason:
Need current weather.

        ↓

Act:
get_weather(city="Mumbai")

        ↓

Observe:
29°C, Cloudy

        ↓

Reason:
Answer user.
```

So:

> **ReAct is the agentic reasoning loop; function calling is one mechanism for executing the actions.**

---

# 18. Tool Calling with Multiple Steps

Here's a more interesting example.

User:

> "Find the weather in Mumbai and tell me whether I should go for a run."

Available tools:

```text id="k3f7tc"
get_weather()
```

### Cycle 1

Reason:

> Need current weather.

Action:

```text id="1ps2at"
get_weather("Mumbai")
```

Observation:

```text id="wh9v7n"
Rain: Heavy
Temperature: 27°C
```

### Cycle 2

Reason:

> Heavy rain makes outdoor running impractical.

Final:

> "It's currently raining heavily in Mumbai, so I'd avoid an outdoor run right now."

Notice the LLM is combining **tool data + reasoning**.

---

# 19. Tool Errors

Real systems aren't perfect.

Suppose:

```text id="m4n8x6"
get_weather("Mumbai")
```

returns:

```text id="z5f8m0"
ERROR: Service unavailable
```

The agent might:

```text id="gk3r1p"
Reason
 ↓
Tool failed
 ↓
Retry
 ↓
Observe
```

or:

```text id="j8g2ad"
Try another source
```

or:

> "I couldn't retrieve the current weather."

This is much better than inventing an answer.

---

# 20. Tool Safety

This is **extremely important**.

Imagine an agent has:

```text id="f7v3n2"
read_email()
send_email()
delete_email()
```

Giving an LLM unrestricted access could be dangerous.

A safer design:

```text id="7l0yqf"
LLM
 ↓
Tool request
 ↓
Permission / Validation
 ↓
Tool
```

For sensitive actions, the system may require human approval:

```text id="y9c5e4"
LLM
 ↓
"Send ₹50,000 payment"
 ↓
Human approval
 ↓
Payment system
```

This is called a **human-in-the-loop** approach.

---

# 21. Tool Calling Security Risks

Important risks include:

### Unauthorized actions

The model calls something it shouldn't.

### Incorrect arguments

For example:

```text id="6j2v8a"
send_money(amount=500000)
```

when the user intended ₹5,000.

### Prompt injection

Malicious text may attempt to manipulate the agent into using tools improperly.

### Excessive permissions

An agent shouldn't have access to tools it doesn't need.

### Best principle

> **Give an agent the minimum permissions necessary to accomplish its task.**

This is the principle of **least privilege**.

---

# 22. Tool Usage Architecture

A robust agent often looks like:

```text id="wz0x8m"
                    USER
                      ↓
                    LLM
                      ↓
               Decide Action
                      ↓
               ┌──────────────┐
               │ Validation   │
               │ & Permission │
               └──────┬───────┘
                      ↓
                 Tool Call
                      ↓
                 Tool/API
                      ↓
                   Result
                      ↓
                    LLM
                      ↓
                Final Answer
```

This is a much safer architecture than:

```text id="5t3p5v"
LLM → unrestricted tools
```

---

# 23. Tool Calling vs RAG

You'll study RAG next, but know this distinction now.

### Tool calling

The agent **performs an action**.

Example:

> Search the web.

### RAG

The system **retrieves relevant information** and provides it to the LLM.

Example:

> Retrieve relevant company policy documents.

Both extend the LLM, but they solve slightly different problems.

---

# 24. Real-World Agent Example

Imagine a **University Assistant Agent**.

Available tools:

```text id="7w8qvf"
get_timetable()
check_attendance()
query_courses()
send_notification()
```

User:

> "Do I have a lecture tomorrow morning?"

Agent:

```text id="q8z0c1"
Reason:
Need timetable information.

 ↓

Tool:
get_timetable()

 ↓

Observation:
9:00 AM → Machine Learning

 ↓

Reason:
There is a morning lecture.

 ↓

Final:
"Yes. You have Machine Learning at 9:00 AM."
```

Now:

> "Remind me 30 minutes before it."

Agent:

```text id="2hjxj9"
Reason:
Need to create reminder.

 ↓

Tool:
create_notification(
    time="8:30 AM",
    message="Machine Learning lecture"
)

 ↓

Observation:
Notification created.

 ↓

Final:
"Done. I'll remind you at 8:30 AM."
```

That's a genuine agent workflow.

---

# 25. Function Calling — Exam Definition

> **Function calling is a mechanism that allows an LLM to generate structured requests to invoke predefined functions or tools with specified arguments, enabling the LLM to interact with external systems.**

Memorize the keywords:

**LLM → structured request → function/tool → arguments → execution → result → LLM**

---

# 26. Quick Revision

### Tool

An external capability available to an agent.

### Function

A specific executable operation.

### Function calling

LLM generates a structured request to invoke that function.

### Tool workflow

```text
User
 ↓
LLM
 ↓
Tool selection
 ↓
Function call
 ↓
Application executes tool
 ↓
Tool result
 ↓
LLM
 ↓
Final answer
```

### Important concepts

* Tool selection
* Tool descriptions
* Parameters
* Structured arguments
* Tool results
* Error handling
* Permissions
* Human approval
* Least privilege

---

# MUST REMEMBER

### ReAct

> **Reason → Act → Observe**

### Function Calling

> **LLM requests a function → application executes it → result returns to LLM**

### Agent

> **LLM + reasoning + tools + environment + control loop**

---

# Active Learning

### Q1 — Conceptual

What is the difference between a **tool** and **function calling**?

### Q2 — Conceptual

Why doesn't the LLM usually directly execute the function?

### Q3 — Conceptual

Why is **least privilege** important when giving tools to an AI agent?

### Q4 — Practical

An AI shopping agent has these tools:

```text
search_products(query)
get_product_details(product_id)
calculator(expression)
```

The user asks:

> **"Find a laptop under ₹60,000 and calculate 18% GST on its price."**

Describe the sequence of **tool calls and results** the agent should perform.

After this, we'll move to **Topic 7: Memory in LLMs — Short-Term Memory, Long-Term Memory & Vector Databases**, which is a major Agentic AI topic.
