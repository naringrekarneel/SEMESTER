# Topic 7: Memory in LLMs

This is one of the **most important concepts in Agentic AI**.

An LLM by itself doesn't automatically remember everything from every interaction.

So if we want an agent to behave like a persistent assistant, we need **memory systems**.

---

# 1. ELI5 — Why Do Agents Need Memory?

Imagine you meet an assistant today.

You say:

> "My name is Alex."

Tomorrow you ask:

> "What's my name?"

A good assistant should say:

> "Alex."

But a basic LLM doesn't magically have a permanent notebook containing every conversation you've ever had.

So we build memory around it.

```text id="h9q8l3"
              AGENT
                ↓
        ┌───────────────┐
        │    MEMORY     │
        └───────────────┘
          ↓     ↓     ↓
      Short   Long   Vector
      Term    Term   Memory
```

Memory allows an agent to **retain, retrieve, and use information across interactions**.

---

# 2. Why Does an LLM Need Memory?

Without memory:

```text id="o1d9p4"
Conversation 1
     ↓
Answer
     ↓
Conversation ends
     ↓
Future conversation
     ↓
No previous context
```

With memory:

```text id="h0d7k2"
Conversation
     ↓
Important information
     ↓
Memory storage
     ↓
Future conversation
     ↓
Retrieve relevant memory
     ↓
LLM
```

This allows agents to become more personalized and persistent.

---

# 3. Three Important Types

For your syllabus, focus on:

1. **Short-term memory**
2. **Long-term memory**
3. **Vector-based memory**

Let's understand them one by one.

---

# 4. Short-Term Memory

## ELI5

Short-term memory is like your **working memory**.

Suppose we're having this conversation:

> User: My exam is tomorrow.
> Assistant: What subject?
> User: Agentic AI.
> Assistant: Which topic are you studying?
> User: Memory.

The model needs the earlier messages to understand what "Memory" refers to.

That conversation history acts as short-term context.

---

# 5. Short-Term Memory = Current Context

Conceptually:

```text id="7h1j2s"
User message 1
       ↓
Assistant response 1
       ↓
User message 2
       ↓
Assistant response 2
       ↓
Current user message
       ↓
LLM
```

The model receives relevant previous conversation as part of its context.

---

# 6. Example

User:

> My name is Rahul.

Assistant:

> Nice to meet you, Rahul.

User:

> What is my name?

If the previous message is still available in the context:

```text id="8e3z9f"
"My name is Rahul."
```

the LLM can answer:

> Rahul.

This is short-term conversational memory.

---

# 7. Context Window

Here's an important technical concept.

LLMs have a **context window**.

It represents how much input/context the model can process in a single request.

Conceptually:

```text id="u0j4ts"
┌──────────────────────────────┐
│       Context Window         │
│                              │
│ Previous messages            │
│ Instructions                 │
│ Retrieved information        │
│ Current user message         │
└──────────────────────────────┘
                 ↓
                LLM
```

If the conversation becomes extremely long, the application may need to:

* summarize old messages
* remove irrelevant messages
* retrieve relevant memories
* store information externally

---

# 8. Short-Term Memory Techniques

Common approaches include:

### Conversation buffer

Store recent messages.

```text id="d8p5z1"
Message 1
Message 2
Message 3
Message 4
```

### Sliding window

Keep only the most recent messages.

```text id="x8t6w2"
Old → removed

Recent:
M10
M11
M12
M13
M14
```

### Conversation summary

Instead of storing everything:

```text id="p6j9q3"
100 messages
     ↓
Summary
     ↓
LLM
```

Example:

> "User is building a Python project and prefers simple explanations."

This saves context space.

---

# 9. Long-Term Memory

Now imagine the user tells the agent:

> "I prefer Python over Java."

And they want the assistant to remember that **weeks later**.

That's long-term memory.

```text id="v6x5u2"
Conversation
     ↓
Important information
     ↓
Persistent storage
     ↓
Future conversation
     ↓
Retrieve information
     ↓
LLM
```

Long-term memory exists outside the immediate context window.

---

# 10. Examples of Long-Term Memory

An agent could remember:

### User preferences

> Prefers concise explanations.

### Project information

> User is building a student attendance application.

### Important facts

> Current project uses Flutter and Riverpod.

### Past decisions

> The user chose PostgreSQL instead of MongoDB.

The important point:

> **The information can survive beyond the current conversation context.**

---

# 11. Short-Term vs Long-Term Memory

| Short-Term                | Long-Term                            |
| ------------------------- | ------------------------------------ |
| Current conversation      | Persistent information               |
| Temporary                 | Persistent                           |
| Usually context-based     | External storage                     |
| Recent messages           | Important historical information     |
| Limited by context window | Can be much larger                   |
| Fast access               | Requires retrieval/storage mechanism |

### Memory trick

> **Short-term = What's happening now?**

> **Long-term = What should I remember later?**

---

# 12. Where Do We Store Long-Term Memory?

Possible storage systems include:

* relational databases
* document databases
* key-value stores
* vector databases
* files/object storage

For AI systems, **vector databases** are particularly important.

---

# 13. What is a Vector?

This is where things get interesting.

Computers don't naturally understand the meaning of:

> "I love playing football."

as humans do.

We can convert text into a numerical representation called an **embedding**.

For example:

```text id="v7p8q2"
"I love football"
        ↓
Embedding model
        ↓
[0.21, -0.73, 0.44, 0.18, ...]
```

This numerical vector captures semantic information.

---

# 14. Embeddings

An embedding is a numerical representation of data in a high-dimensional vector space.

Conceptually:

```text id="h1z5j9"
Text
 ↓
Embedding Model
 ↓
Vector
```

Example:

```text id="q9m2c7"
"football"
   ↓
[0.12, 0.87, -0.21, ...]
```

and:

```text id="n4x6b1"
"soccer"
   ↓
[0.11, 0.84, -0.19, ...]
```

Because the meanings are related, their vectors may be relatively close.

---

# 15. Semantic Similarity

Suppose we store:

```text id="9q6b2m"
Memory 1:
"I like playing football."

Memory 2:
"I enjoy cricket."

Memory 3:
"I love soccer."
```

User asks:

> "What sport do I enjoy playing?"

We can convert the query into an embedding:

```text id="b8d1f4"
"What sport do I enjoy playing?"
              ↓
           Vector
```

Then search for vectors that are semantically similar.

Likely relevant:

```text id="x8m4z2"
"I like playing football."
"I love soccer."
```

---

# 16. Vector Database

A **vector database** stores embeddings and allows efficient similarity search.

Conceptually:

```text id="q2k8n4"
                 Vector Database
              ┌────────────────────┐
              │ Text + Embeddings  │
              ├────────────────────┤
              │ Memory A → Vector  │
              │ Memory B → Vector  │
              │ Memory C → Vector  │
              │ Memory D → Vector  │
              └────────────────────┘
                         ↑
                         │
                      Query
                         │
                    Embedding
```

---

# 17. Why Not Just Search Keywords?

Consider:

> "I enjoy coding in Python."

User later says:

> "Which programming language do I prefer?"

Keyword search might struggle because:

```text
"coding in Python"
```

doesn't literally contain:

```text
"programming language"
"prefer"
```

Semantic/vector search can recognize the relationship.

That's the power of embeddings.

---

# 18. Similarity Search

Suppose we have vectors:

```text id="0e2x9j"
A = [1, 2]
B = [2, 3]
C = [10, 10]
```

Query:

```text id="s7h4n1"
Q = [1, 2]
```

A is clearly closest.

The database returns the most similar vectors.

Common similarity measures include:

* cosine similarity
* Euclidean distance
* dot product

---

# 19. Cosine Similarity

This is particularly important for exams.

Cosine similarity measures the angle between two vectors.

Formula:

$$
\text{Cosine Similarity}(A,B)
=============================

\frac{A \cdot B}
{|A||B|}
$$

where:

* $A \cdot B$ = dot product
* $|A|$ = magnitude of vector $A$
* $|B|$ = magnitude of vector $B$

The value is generally between:

$$
-1 \leq \text{cosine similarity} \leq 1
$$

For many embedding applications, higher similarity means greater semantic relatedness.

---

# 20. Worked Example

Suppose:

$$
A = [1,2]
$$

and

$$
B = [2,4]
$$

### Step 1: Dot product

$$
A \cdot B = (1)(2)+(2)(4)
$$

$$
=2+8=10
$$

### Step 2: Magnitudes

$$
|A| = \sqrt{1^2+2^2}
=\sqrt{5}
$$

$$
|B| = \sqrt{2^2+4^2}
=\sqrt{20}
$$

### Step 3: Cosine similarity

$$
\text{Similarity}
=================

\frac{10}{\sqrt{5}\sqrt{20}}
$$

Since $B$ is exactly a scaled version of $A$:

$$
\text{Similarity}=1
$$

They point in exactly the same direction.

---

# 21. Memory Retrieval Pipeline

Now let's put everything together.

Suppose the user asks:

> "What programming language do I usually prefer?"

### Step 1

Convert query to embedding.

```text id="h3n7q9"
Question
 ↓
Embedding Model
 ↓
Query Vector
```

### Step 2

Search vector database.

```text id="m9v2r1"
Query Vector
 ↓
Similarity Search
 ↓
Relevant memories
```

### Step 3

Retrieve memory.

```text id="7w5d2k"
"I prefer Python."
```

### Step 4

Give it to LLM.

```text id="p8c4z6"
User Question
+
Retrieved Memory
 ↓
LLM
```

### Step 5

Answer:

> "You usually prefer Python."

---

# 22. Memory Architecture

A basic agent memory architecture:

```text id="a6r4y2"
                 USER
                   ↓
                  AGENT
                   ↓
             ┌───────────┐
             │    LLM    │
             └─────┬─────┘
                   │
          ┌────────┴────────┐
          ↓                 ↓
   Short-Term          Long-Term
     Memory               Memory
          │                 │
    Conversation       Persistent DB
                            │
                     Vector Database
                            │
                       Embeddings
```

---

# 23. Memory + LLM

The LLM itself doesn't necessarily need to permanently store everything.

Instead:

```text id="r7q3k9"
External Memory
      ↓
Retrieve relevant information
      ↓
Context
      ↓
LLM
```

This is a key architectural idea.

The memory system acts like an **external knowledge store**.

---

# 24. Memory + Agentic AI

Imagine a personal AI assistant.

### First conversation

User:

> I prefer morning workouts.

The agent stores:

```text id="s8k2d4"
Preference:
Morning workouts
```

### Two months later

User:

> Suggest a workout time.

Agent:

```text id="j2v5m8"
Query memory
 ↓
Retrieve:
"User prefers morning workouts"
 ↓
LLM
 ↓
"Morning would suit your preference."
```

Now the agent feels persistent.

---

# 25. Important Problem: What Should Be Remembered?

You don't want to store every single message forever.

For example:

> "What's 2 + 2?"

Probably not worth long-term storage.

But:

> "I prefer Python for backend development."

might be useful later.

Therefore an agent needs a **memory management strategy**.

Potential process:

```text id="m2f8k1"
Conversation
 ↓
Extract important information
 ↓
Decide whether worth storing
 ↓
Store
 ↓
Retrieve when relevant
```

---

# 26. Memory Retrieval is Critical

Having huge memory isn't enough.

Suppose the agent has:

```text id="a5j9x3"
1,000,000 memories
```

and retrieves random memories.

That's useless.

The system needs:

> **Relevant memory retrieval**

So:

```text id="j5r2k7"
Query
 ↓
Retrieve relevant memories
 ↓
Rank/filter
 ↓
Send useful memories to LLM
```

This is closely related to **RAG**, which is our next major topic.

---

# 27. Memory vs RAG

Very important distinction.

### Memory

Usually focuses on information about:

> **the user, agent, previous interactions, or persistent state**

Example:

> "User prefers Python."

### RAG

Usually focuses on retrieving:

> **relevant external knowledge/documents**

Example:

> "Company refund policy says customers can return products within 30 days."

Both can use vector databases.

So don't think:

> Vector database = only RAG.

Vector databases can support **both memory and RAG**.

---

# 28. Short-Term + Long-Term + RAG

A sophisticated agent might have all three:

```text id="c6y8v2"
                    USER
                      ↓
                    AGENT
                      ↓
                     LLM
                 ↙    ↓    ↘
                /     |     \
               ↓      ↓      ↓
         Short-term Long-term RAG
           Memory     Memory
              │          │      │
              ↓          ↓      ↓
          Conversation   DB   Documents
```

The LLM combines relevant information from all sources.

---

# 29. Memory Lifecycle

A useful way to understand memory:

```text id="z7m1x4"
Capture
  ↓
Store
  ↓
Index
  ↓
Retrieve
  ↓
Use
  ↓
Update/Delete
```

### Capture

Identify useful information.

### Store

Save it.

### Index

Make it searchable.

### Retrieve

Find relevant memories.

### Use

Provide them to the LLM.

### Update/Delete

Keep memory accurate.

---

# 30. Problems with Long-Term Memory

### Outdated information

User's preference may change.

```text id="v4m8q2"
Old:
"I prefer Java."

New:
"I now prefer Python."
```

The system needs to update memory.

### Contradictions

Two memories may conflict.

### Privacy

Memory can contain sensitive information.

### Storage cost

Large memory systems require infrastructure.

### Retrieval errors

The wrong memory may be retrieved.

---

# 31. Exam-Friendly Architecture

If asked:

> "Explain memory in LLM-based agents."

Draw:

```text id="n2x8w5"
                  User
                   ↓
                 Agent
                   ↓
                  LLM
                   ↓
       ┌───────────┼───────────┐
       ↓           ↓           ↓
 Short-Term    Long-Term    Vector DB
   Memory        Memory      / Retrieval
       ↓           ↓           ↓
 Current       Persistent   Semantic
 Context       Storage      Search
       └───────────┼───────────┘
                   ↓
              Relevant Context
                   ↓
                  LLM
                   ↓
                Response
```

Then explain each component.

---

# Quick Revision Sheet

## Short-Term Memory

> Maintains recent conversation/context.

## Long-Term Memory

> Stores useful information persistently across interactions.

## Embeddings

> Numerical representations of text/data that capture semantic relationships.

## Vector Database

> Stores embeddings and supports similarity-based retrieval.

## Semantic Search

> Finds information based on meaning rather than exact keyword matching.

## Memory Pipeline

```text id="x5n7c3"
Store → Embed → Index → Retrieve → Use
```

## Similarity

Common measures:

* Cosine similarity
* Euclidean distance
* Dot product

---

# MUST REMEMBER

The most important mental model:

> **Short-term memory = current conversation**

> **Long-term memory = persistent information**

> **Vector memory = semantic retrieval of relevant information**

And:

> **The LLM + external memory = persistent agent behavior**

---

# Active Learning

### Q1 — Conceptual

What is the main difference between **short-term memory** and **long-term memory** in an AI agent?

### Q2 — Conceptual

Why are embeddings useful for memory retrieval?

### Q3 — Conceptual

Why isn't simply storing millions of memories enough to create a good memory system?

### Q4 — Practical

An AI assistant has stored these memories:

```text
M1: User prefers Python.
M2: User likes football.
M3: User owns a gaming laptop.
M4: User prefers studying at night.
```

The user asks:

> **"What programming language should I use for my next backend project?"**

Explain how the agent could use **vector-based memory retrieval** to answer this question.

After that, we'll move to **Topic 8: Retrieval-Augmented Generation (RAG)** — one of the biggest topics in modern LLM systems.
