# Topic 7: API Integrations & Tool Building

## 1. What is API Integration?

An **API (Application Programming Interface)** allows one software application to communicate with another software system.

### ELI5

Think of an API like a **waiter in a restaurant**:
* You = AI application
* Waiter = API
* Kitchen = External service
* Food = Data/result

You don't directly enter the kitchen. You send a request through the waiter, and the waiter brings back the result.

```text
AI Application
      │
      │ API Request
      ▼
   External API
      │
      │ API Response
      ▼
AI Application
```

---

## 2. Why APIs are Important in Agentic AI

An LLM by itself mainly generates and processes information.
APIs allow an AI agent to **interact with external systems**.

For example:

| API | Agent capability |
| :--- | :--- |
| **Weather API** | Get weather |
| **Maps API** | Find locations/routes |
| **Payment API** | Process payments |
| **Database API** | Read/write data |
| **Email API** | Send emails |
| **Calendar API** | Create events |
| **News API** | Retrieve news |
| **Stock API** | Retrieve market data |

So:
> **API = Bridge between an AI system and an external service.**

---

## 3. What is Tool Building?

A **tool** is a function or interface that an AI agent can call to perform a specific action.

For example, suppose we create:
```text
get_weather(city)
```

The agent can decide:
> "I need the current weather, so I should use the weather tool."

The tool then communicates with the weather API.

```text
User
 │
 ▼
AI Agent
 │
 │ decides to use tool
 ▼
Weather Tool
 │
 ▼
Weather API
 │
 ▼
Weather Data
 │
 ▼
AI Agent
 │
 ▼
Final Answer
```

---

## 4. API vs Tool

This distinction is **very important**.

| API | Tool |
| :--- | :--- |
| Interface provided by an external service | Interface exposed to the AI agent |
| Allows software to communicate with a service | Allows agent to perform a specific operation |
| Example: Weather API | Example: `get_weather()` tool |
| Usually defined by service provider | Usually created/configured by developer |

### Simple relationship
```text
External Service
      │
      ▼
     API
      │
      ▼
    Tool
      │
      ▼
  AI Agent
```
A tool can use an API internally.

---

## 5. Example: Weather Tool

Suppose we want our AI assistant to answer:
> "What's the weather in Mumbai?"

The system could contain:
```text
Tool:
get_weather(city)
```

### Execution
```text
User:
What's the weather in Mumbai?

        ↓

Agent:
I need current weather information.

        ↓

Tool:
get_weather("Mumbai")

        ↓

Weather API

        ↓

Temperature / humidity / conditions

        ↓

Agent

        ↓

"Currently, Mumbai is ..."
```

The important point is that the **LLM does not need to know the live weather itself**. It uses a tool to obtain the information.

---

## 6. Anatomy of a Good Tool

A well-designed tool generally contains:

### 1. Name
Clearly identifies the tool.
Example: `get_weather`

### 2. Description
Explains what the tool does.
Example: `Gets current weather information for a city.`

### 3. Input
Defines what information the tool requires.
Example: `city = "Mumbai"`

### 4. Input Schema
Specifies valid input types and structure.
Example: `city: string`

### 5. Function Logic
The actual code that performs the operation.

### 6. Output
Returns a useful result to the agent.

---

## 7. Example Tool Structure

Conceptually:

```python
def get_weather(city: str):
    # Call external weather API
    response = weather_api(city)

    # Return useful information
    return response
```

The AI agent doesn't need to understand the internal implementation.
It only needs to know:

```text
Tool name: get_weather

Description:
Get current weather for a city.

Input:
city → string
```

---

## 8. Tool-Calling Workflow

A typical agentic tool workflow looks like this:

```text
        User Request
             │
             ▼
        ┌──────────┐
        │   LLM    │
        └────┬─────┘
             │
       Decide action
             │
             ▼
        ┌──────────┐
        │   Tool   │
        └────┬─────┘
             │
             ▼
       External API
             │
             ▼
        Tool Result
             │
             ▼
        ┌──────────┐
        │   LLM    │
        └────┬─────┘
             │
             ▼
       Final Response
```

### Remember:
> **LLM decides → Tool acts → Result returns → LLM responds**

---

## 9. Multiple Tools

An agent can have multiple tools.
For example:

```text
AI Assistant
     │
     ├── Web Search
     │
     ├── Calculator
     │
     ├── Weather
     │
     ├── Database
     │
     ├── Email
     │
     └── Calendar
```

Suppose the user says:
> "Find tomorrow's weather, calculate how much my trip will cost, and add the trip to my calendar."

The agent could potentially use:
```text
Weather Tool
      ↓
Calculator Tool
      ↓
Calendar Tool
```
This is where tools become especially useful in **agentic AI**.

---

## 10. Building a Custom Tool

A general process is:

### Step 1 — Identify the capability
Example:
> "I want my agent to search my company's database."

### Step 2 — Create a function
```python
def search_database(query):
    ...
```

### Step 3 — Define inputs
```text
query → string
```

### Step 4 — Connect to the external system
```text
search_database()
       ↓
Database/API
```

### Step 5 — Return structured output
```json
{
    "results": [...],
    "count": 10
}
```

### Step 6 — Give the tool to the agent
The agent can now decide when to call it.

---

## 11. Structured Output

Tools should ideally return **structured data** instead of messy text.

For example:
```json
{
  "city": "Mumbai",
  "temperature": 29,
  "humidity": 78,
  "condition": "Cloudy"
}
```

The agent can then easily interpret the result.

### Why?
Structured data improves:
* Reliability
* Parsing
* Validation
* Consistency
* Agent reasoning

---

## 12. API Authentication

Many APIs require authentication.
Common mechanisms include:
* API keys
* OAuth tokens
* Access tokens
* JWTs

Example:
```text
Agent
  │
  ▼
Tool
  │
  ├── API Key
  │
  ▼
External API
```

### Important security rule
**Never hard-code sensitive API keys into publicly shared source code.**
Instead, developers commonly use environment variables or secure secret-management systems.

---

## 13. Error Handling

APIs can fail.
Possible problems:
* Network failure
* Invalid input
* Authentication failure
* Rate limit
* Server error
* Timeout
* Invalid response

A robust tool should handle these cases.

```text
Tool Call
   │
   ▼
API Request
   │
   ├── Success ──→ Return result
   │
   └── Error ────→ Handle error
                       │
                       ▼
                  Retry / message
```

For example:
```python
try:
    result = call_api()
    return result
except Exception:
    return "API request failed."
```

In production systems, error handling should be more specific than this simplified example.

---

## 14. Security Considerations

Tool building becomes especially important from a security perspective because an agent may have the ability to **take actions**.

Important practices:

### Input Validation
Don't blindly trust agent-generated inputs.

### Authentication
Verify users and services.

### Authorization
Only allow permitted actions.

### Rate Limiting
Prevent excessive API calls.

### Logging
Record important tool activity.

### Least Privilege
Give an agent only the permissions it actually needs.

### Human Confirmation
For sensitive actions, require approval.
Example:
```text
Agent:
Send ₹50,000 payment?

       ↓
Human Approval
       ↓

Payment Tool
```

This is particularly important for actions involving money, deletion, account changes, or other irreversible operations.

---

## 15. API Integration Example

Imagine building an **AI travel assistant**.

Available tools:
```text
Search Flights
Search Hotels
Weather
Maps
Currency Converter
Calendar
```

User:
> "Plan my 3-day trip to Goa."

The agent can potentially:
```text
User
 │
 ▼
Travel Agent
 │
 ├── Search Flights
 │
 ├── Search Hotels
 │
 ├── Weather
 │
 ├── Maps
 │
 └── Calendar
 │
 ▼
Trip Plan
```

This demonstrates how **APIs + tools + agents** combine to create an intelligent application.

---

## 16. Tool Building in LangChain/CrewAI

Conceptually, the frameworks provide mechanisms to:

```text
Create Tool
     ↓
Describe Tool
     ↓
Define Input Schema
     ↓
Attach Tool to Agent
     ↓
Agent Selects Tool
     ↓
Execute Tool
     ↓
Return Result
```

The exact APIs and decorators can vary between framework versions, so for your exam, focus on the **architecture and workflow** rather than memorizing version-specific syntax.

---

## 17. API Integration vs Tool Building

| Aspect | API Integration | Tool Building |
| :--- | :--- | :--- |
| **Purpose** | Connect application to external service | Expose an action to AI agent |
| **Main focus** | Communication | Agent usability |
| **Example** | Connect Weather API | Create `get_weather()` |
| **Input** | API request | Tool arguments |
| **Output** | API response | Agent-readable result |
| **Used by** | Applications | Agents/LLM systems |

---

## 18. Exam-Ready Answer

> **API integration in agentic AI refers to connecting an AI system with external services through APIs. Tool building involves creating callable functions or interfaces that allow AI agents to use these external capabilities. The agent decides when a tool is required, the tool executes the operation through an API or other system, and the result is returned to the agent for further reasoning or response generation.**

### Architecture
```text
User
 ↓
AI Agent
 ↓
Tool Selection
 ↓
Custom Tool
 ↓
API / Database / External Service
 ↓
Tool Result
 ↓
AI Agent
 ↓
Final Response
```

---

## 📝 Quick Revision

```text
API      → Communication interface
Tool     → Action available to the agent
Agent    → Decides which tool to use
Function → Actual implementation of the tool
Schema   → Defines valid inputs
Response → Result returned by tool
```

### Golden line:
> **API connects systems; a tool exposes a capability to the agent.**

### Tool workflow:
> **Decide → Call Tool → Execute → Observe Result → Continue → Respond**

---

## 🧠 Active Learning

1. **Conceptual:** What is the difference between an API and a tool?
2. **Conceptual:** Why should an agent not be given unlimited permissions to every tool?
3. **Practical:** Design three tools for an **AI college assistant** and mention what API or external service each tool could use.

> *When you're ready, say **N** → **Topic 8: Memory Management**.*
