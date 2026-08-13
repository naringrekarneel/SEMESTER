# Agentic AI — Complete Revision Sheet

You've now completed the entire syllabus. Let's compress everything into one **exam-ready mental model**.

---

# 1. Complete Roadmap

```text
LLMs
 ↓
Prompt Engineering
 ↓
Chain-of-Thought Reasoning
 ↓
ReAct
 ↓
Tool Usage / Function Calling
 ↓
Memory
 ↓
RAG
 ↓
Self-Reflection
 ↓
Self-Correction
 ↓
Agentic AI System
```

Think of this as progressively giving an LLM more capabilities.

---

# 2. LLM — Large Language Model

## Definition

A **Large Language Model (LLM)** is a neural network trained on large amounts of text to understand and generate human-like language.

Examples include models used for:

* question answering
* summarization
* translation
* coding
* reasoning
* content generation

### Basic flow

```text
Prompt
  ↓
LLM
  ↓
Generated Response
```

### Limitation

A standalone LLM may:

* hallucinate
* lack private information
* have outdated knowledge
* have no direct access to tools
* have limited persistent memory

Agentic AI addresses these limitations.

---

# 3. Prompt Engineering

Prompt engineering means designing instructions that guide an LLM toward the desired output.

### Basic prompt

> Explain databases.

### Better prompt

> Explain databases to a beginner using a real-world analogy, followed by three exam points.

---

## Important Prompting Techniques

### Zero-shot

No examples.

```text
Translate:
"Hello"
```

### Few-shot

Provide examples.

```text
English → Hindi

Hello → नमस्ते
Thank you → धन्यवाद

Good morning → ?
```

### Role prompting

```text
You are an expert Python tutor.
```

### Structured prompting

Specify output format.

```text
Return:
1. Definition
2. Advantages
3. Example
```

### Chain-of-thought prompting

Encourages multi-step reasoning for complex problems.

---

# 4. Chain-of-Thought Reasoning

CoT involves solving complex problems through intermediate reasoning steps.

Instead of:

```text
Question
 ↓
Answer
```

conceptually:

```text
Question
 ↓
Step 1
 ↓
Step 2
 ↓
Step 3
 ↓
Answer
```

Useful for:

* mathematics
* logic
* planning
* multi-step problems

### Important caution

The useful concept for exams is **decomposing complex problems into intermediate steps**. In real systems, you don't necessarily need to expose private internal reasoning to the user.

---

# 5. ReAct

**ReAct = Reason + Act**

It combines reasoning with actions such as tool calls.

```text
Goal
 ↓
Reason
 ↓
Act
 ↓
Observe
 ↓
Reason
 ↓
Act
 ↓
...
 ↓
Final Answer
```

### Example

User:

> What's the weather in Mumbai?

Agent:

```text
Reason
 ↓
Call weather tool
 ↓
Observe result
 ↓
Generate response
```

### Key idea

> **LLM + reasoning + actions + observations**

---

# 6. Tool Usage / Function Calling

Tools give an LLM capabilities it doesn't inherently possess.

Examples:

* calculator
* search
* database
* weather API
* code execution
* email system
* calendar

---

## Function Calling

The LLM produces a structured request:

```json
{
  "function": "get_weather",
  "arguments": {
    "city": "Mumbai"
  }
}
```

The application executes the function.

```text
LLM
 ↓
Function Call
 ↓
Tool
 ↓
Tool Result
 ↓
LLM
 ↓
Answer
```

### Important

The LLM usually **decides what tool to call**; the actual application/tool environment executes it.

---

# 7. Memory

Memory allows agents to retain useful information.

## Short-Term

Current conversation/context.

```text
Current messages
      ↓
LLM
```

## Long-Term

Persistent information.

```text
Important information
       ↓
Database
       ↓
Future retrieval
```

## Vector Memory

Uses embeddings for semantic retrieval.

```text
Text
 ↓
Embedding
 ↓
Vector
 ↓
Vector DB
```

---

# 8. Embeddings

An embedding converts information into a numerical vector.

```text
"Python programming"
        ↓
Embedding model
        ↓
[0.21, -0.43, 0.77, ...]
```

Semantically related text tends to have similar vector representations.

---

# 9. Cosine Similarity

A common similarity measure:

$$
\text{Cosine Similarity}(A,B)
=============================

\frac{A\cdot B}
{|A||B|}
$$

Higher similarity generally means the vectors are more semantically related.

---

# 10. RAG

**RAG = Retrieval-Augmented Generation**

It allows an LLM to retrieve relevant external information before generating an answer.

### Three stages

```text
R → Retrieve
A → Augment
G → Generate
```

---

# 11. RAG Pipeline

### Indexing

```text
Documents
 ↓
Chunking
 ↓
Embeddings
 ↓
Vector Database
```

### Query time

```text
User Query
 ↓
Query Embedding
 ↓
Similarity Search
 ↓
Top-K Chunks
 ↓
Context + Query
 ↓
LLM
 ↓
Answer
```

---

# 12. Why Chunking?

A huge document shouldn't be sent to the LLM every time.

So:

```text
500-page document
       ↓
Smaller chunks
       ↓
Relevant chunks retrieved
```

Good chunking balances:

> **Context + retrieval precision**

---

# 13. RAG vs Memory

This is a very common confusion.

| Memory                | RAG                 |
| --------------------- | ------------------- |
| Past/user information | External knowledge  |
| User preferences      | Company documents   |
| Previous interactions | Policies/manuals    |
| Persistent state      | Knowledge retrieval |
| Can use vector DB     | Can use vector DB   |

Example:

> "User prefers Python." → **Memory**

> "Company allows 30-day returns." → **RAG**

---

# 14. RAG vs Fine-Tuning

Another common exam question.

| RAG                             | Fine-Tuning                      |
| ------------------------------- | -------------------------------- |
| Retrieves external information  | Updates model parameters         |
| Knowledge remains outside model | Training changes model           |
| Good for changing knowledge     | Good for behavior/style/patterns |
| Can update documents easily     | Requires additional training     |
| Retrieval at inference time     | Learned during training          |

Mental shortcut:

> **RAG = give the model information at runtime.**

> **Fine-tuning = modify the model through training.**

---

# 15. Self-Reflection

Self-reflection means evaluating the generated output.

```text
Generate
 ↓
Evaluate
 ↓
Identify weaknesses
```

Questions might include:

* Is it correct?
* Is anything missing?
* Is it relevant?
* Are there contradictions?
* Is it supported by evidence?

---

# 16. Self-Correction

Self-correction uses the evaluation to improve the answer.

```text
Generate
 ↓
Reflect
 ↓
Find error
 ↓
Correct
 ↓
Verify
 ↓
Final
```

### Memory trick

> **Reflection = Find the problem**

> **Correction = Fix the problem**

---

# 17. Generator-Critic Architecture

```text
             Problem
                ↓
           Generator
                ↓
             Draft
                ↓
             Critic
                ↓
        ┌───────┴───────┐
        ↓               ↓
      PASS             FAIL
        ↓               ↓
      Final          Feedback
                        ↓
                    Generator
```

A maximum iteration count should normally be imposed.

---

# 18. Complete Agentic AI Architecture

Here's the **big picture**.

```text
                         USER
                           ↓
                    ┌─────────────┐
                    │     LLM     │
                    └──────┬──────┘
                           ↓
                  Prompt Engineering
                           ↓
                      Reasoning
                           ↓
                         ReAct
                    ↙      ↓      ↘
                 Tools   Memory    RAG
                   ↓       ↓        ↓
                 Result  Context  Evidence
                    ↘      ↓      ↙
                           LLM
                            ↓
                        Generate
                            ↓
                       Reflection
                            ↓
                       Correction
                            ↓
                       Verification
                            ↓
                       FINAL ANSWER
```

This is the architecture you should have in your head.

---

# 19. One Example Connecting Everything

Suppose you build a **College AI Assistant**.

Student asks:

> "Can I attend tomorrow's exam? Also remind me 30 minutes before it."

The agent could work like this:

### Step 1 — Understand

LLM interprets the request.

### Step 2 — Memory

Retrieve student's relevant information.

```text
Student attendance = 78%
```

### Step 3 — RAG

Retrieve college examination policy.

```text
Minimum attendance = 75%
```

### Step 4 — Tool Calling

Query timetable database.

```text
Exam:
Tomorrow
10:00 AM
```

### Step 5 — Reason

```text
Attendance = 78%
Required = 75%

Therefore:
Eligible
```

### Step 6 — Self-Reflection

Check:

> Did I use the correct attendance policy?

### Step 7 — Self-Correction

If the policy actually says 80%, correct the conclusion.

### Step 8 — Notification Tool

Call:

```text
schedule_notification(
    time = 9:30 AM
)
```

### Final

> "You meet the stated attendance requirement for the exam. Your exam is at 10:00 AM tomorrow, and I've scheduled a reminder for 9:30 AM."

That's **Agentic AI** in action.

---

# 20. The Most Important Connections

## LLM + Prompt Engineering

Controls **what the model should do**.

## LLM + CoT

Helps with **complex multi-step problems**.

## LLM + ReAct

Allows **reasoning and action**.

## LLM + Tools

Provides **external capabilities**.

## LLM + Memory

Provides **persistence**.

## LLM + RAG

Provides **external knowledge**.

## LLM + Reflection

Provides **evaluation**.

## LLM + Correction

Provides **iterative improvement**.

---

# 21. One-Line Definitions — Exam Revision

| Topic                  | One-line definition                                                          |
| ---------------------- | ---------------------------------------------------------------------------- |
| **LLM**                | Neural model trained on large-scale text to understand and generate language |
| **Prompt Engineering** | Designing effective instructions for an LLM                                  |
| **Chain-of-Thought**   | Breaking complex problems into intermediate reasoning steps                  |
| **ReAct**              | Combining reasoning with actions and observations                            |
| **Tool Calling**       | Allowing an LLM to invoke external functions/tools                           |
| **Short-Term Memory**  | Maintaining current conversational context                                   |
| **Long-Term Memory**   | Persistently storing useful information                                      |
| **Embedding**          | Numerical representation of data capturing semantic properties               |
| **Vector DB**          | Database optimized for vector similarity search                              |
| **RAG**                | Retrieving external information and using it to ground generation            |
| **Self-Reflection**    | Evaluating generated output for errors or weaknesses                         |
| **Self-Correction**    | Revising output based on evaluation                                          |

---

# 22. Most Important Diagrams to Practice

For your exam, practice drawing these **five**.

### 1. ReAct

```text
Reason → Act → Observe → Reason
```

### 2. Tool Calling

```text
LLM → Tool → Result → LLM
```

### 3. Memory

```text
Conversation
 ↓
Memory
 ↓
Storage
 ↓
Retrieval
 ↓
LLM
```

### 4. RAG

```text
Documents
 ↓
Chunk → Embed → Vector DB
                       ↑
Query → Embed → Search
                       ↓
                  Context
                       ↓
                      LLM
```

### 5. Self-Correction

```text
Generate
 ↓
Critique
 ↓
Correct
 ↓
Verify
 ↓
Final
```

---

# 23. High-Priority Exam Questions

If you're short on time, study these first.

### 10-mark / long-answer questions

1. **Explain the architecture and working of an LLM-based Agentic AI system.**
2. **Explain Prompt Engineering and its major techniques with examples.**
3. **Explain Chain-of-Thought reasoning and its applications.**
4. **Explain the ReAct paradigm with architecture and example.**
5. **Explain tool usage and function calling in LLM agents.**
6. **Explain short-term and long-term memory in LLM-based agents.**
7. **Explain embeddings and vector databases for AI memory.**
8. **Explain RAG architecture and its complete pipeline.**
9. **Compare RAG with fine-tuning.**
10. **Explain self-reflection and self-correction in LLM agents.**

---

# 24. Very Likely Comparison Questions

### ReAct vs normal LLM

| Normal LLM                   | ReAct Agent          |
| ---------------------------- | -------------------- |
| Generates response           | Reasons + acts       |
| No inherent tool interaction | Can use tools        |
| Usually one-shot             | Iterative            |
| Limited external interaction | Observes environment |

### RAG vs Fine-Tuning

Already covered above.

### Short-term vs Long-term Memory

```text
Short-term → Current context
Long-term → Persistent information
```

### Reflection vs Correction

```text
Reflection → Identify problem
Correction → Fix problem
```

---

# 25. Final Mental Model

If you forget everything during the exam, remember this:

```text
                 🧠 LLM
                   │
          "What should I do?"
                   │
          Prompt Engineering
                   │
          "How should I reason?"
                   │
              Reasoning
                   │
          "I need to act."
                   │
                ReAct
                   │
          "I need capabilities."
                   │
                Tools
                   │
          "I need information."
                   │
              Memory + RAG
                   │
          "Did I get it right?"
                   │
             Reflection
                   │
          "Let me fix it."
                   │
             Correction
                   │
                AGENT
```

### The ultimate one-liner:

> **An Agentic AI system turns an LLM from a text generator into a system that can reason, remember, retrieve information, use tools, act on the environment, evaluate its work, and improve its results.**

---

# Final Mini Quiz

Try answering these **without looking above**.

### 1.

What does **ReAct** stand for, and what are its three main steps?

### 2.

Why does an agent need **tool calling** if an LLM is already powerful?

### 3.

Differentiate **short-term memory, long-term memory, and RAG**.

### 4.

What is the role of **embeddings** in a vector database?

### 5.

Explain the complete **RAG pipeline** in 5–7 steps.

### 6.

Differentiate **self-reflection** and **self-correction**.

### 7. BIG QUESTION

Design an Agentic AI system for a **college assistant** that can:

* answer questions from college PDFs
* remember student preferences
* check the timetable
* calculate attendance
* send reminders
* verify its final answer

Identify where you would use:

**LLM → Prompt Engineering → ReAct → Tools → Memory → RAG → Self-Reflection → Self-Correction.**

If you can answer **Q7 cleanly**, you've basically got the entire Agentic AI syllabus conceptually locked in.
