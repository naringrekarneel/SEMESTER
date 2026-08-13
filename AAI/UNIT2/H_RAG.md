# Topic 8: Retrieval-Augmented Generation (RAG)

This is a **must-know topic** for Agentic AI, LLM interviews, and exams.

The core problem RAG solves is simple:

> **LLMs don't automatically know your private or up-to-date information.**

RAG gives the LLM access to relevant external information **before generating the answer**.

---

# 1. ELI5 — What is RAG?

Imagine you're writing an exam.

Your brain knows many things, but the question asks:

> "According to this 200-page textbook, what is the university's definition of RAG?"

Instead of guessing, you:

1. Open the textbook.
2. Find the relevant page.
3. Read it.
4. Answer using that information.

That's basically RAG.

> **RAG = Retrieve relevant information + Augment the prompt + Generate an answer.**

```text
Question
   ↓
Retrieve relevant information
   ↓
Add information to prompt
   ↓
LLM
   ↓
Answer
```

---

# 2. Why Do We Need RAG?

Suppose you ask a general LLM:

> "What is our company's refund policy?"

The model may not know your company's private policy.

You could fine-tune the model, but that's often unnecessary.

Instead:

```text
Company Documents
       ↓
   RAG System
       ↓
Relevant Policy
       ↓
      LLM
       ↓
Answer
```

Now the LLM can answer using the retrieved company information.

---

# 3. Problems RAG Helps Solve

RAG is useful for:

### Private knowledge

```text
Company documents
Internal manuals
University notes
```

### Frequently changing information

```text
Product catalog
Policies
Documentation
News
```

### Reducing hallucination

The model can ground its answer in retrieved information.

### Large knowledge bases

Instead of putting every document into the prompt, retrieve only relevant parts.

---

# 4. Basic RAG Architecture

Memorize this diagram.

```text
                 USER QUERY
                     ↓
               Query Embedding
                     ↓
              ┌──────────────┐
              │ Vector DB /  │
              │ Search Index │
              └──────┬───────┘
                     ↓
             Relevant Documents
                     ↓
              Context + Query
                     ↓
                    LLM
                     ↓
                  Answer
```

This is the basic RAG pipeline.

---

# 5. The Three Words of RAG

Remember:

## R — Retrieve

Find relevant information.

## A — Augment

Add the retrieved information to the LLM's context.

## G — Generate

Generate an answer using the query + retrieved context.

```text
R → Retrieve
A → Augment
G → Generate
```

---

# 6. RAG Pipeline — Step by Step

Suppose we have a university knowledge base.

Documents:

```text
Doc 1 → Attendance policy
Doc 2 → Examination rules
Doc 3 → Hostel rules
Doc 4 → Fee structure
```

User asks:

> "What is the minimum attendance required?"

---

## Step 1 — User Query

```text id="5g8j1d"
"What is the minimum attendance required?"
```

---

## Step 2 — Convert Query to Embedding

An embedding model converts the query into a vector.

```text id="l9p4c2"
Query
 ↓
Embedding Model
 ↓
[0.23, -0.51, 0.72, ...]
```

---

## Step 3 — Search

The vector database searches for similar vectors.

It may retrieve:

```text id="r4q7x2"
Doc 1:
Attendance policy
```

rather than:

```text id="x5j8m1"
Doc 3:
Hostel rules
```

---

## Step 4 — Retrieve Relevant Chunks

Instead of retrieving the entire document, the system may retrieve a relevant section:

> "Students must maintain a minimum attendance of 75%."

---

## Step 5 — Augment the Prompt

The system constructs something conceptually like:

```text id="n8y2q5"
Question:
What is the minimum attendance required?

Relevant context:
Students must maintain a minimum attendance
of 75%.

Answer using the provided context.
```

---

## Step 6 — Generate

The LLM receives the context and answers:

> "The minimum required attendance is 75%."

That's RAG.

---

# 7. Why Do We Use Chunks?

Imagine a document has 500 pages.

We don't want to send all 500 pages to the LLM for every question.

Instead, divide the document into smaller pieces called **chunks**.

```text id="u3m9x7"
500-page document
       ↓
 ┌─────┬─────┬─────┬─────┐
 ↓     ↓     ↓     ↓
Chunk1 Chunk2 Chunk3 ... ChunkN
```

Then retrieve only the relevant chunks.

---

# 8. Chunking

**Chunking** means dividing documents into smaller pieces suitable for retrieval.

Example:

```text id="s5n2k8"
Original document
        ↓
Paragraph 1
Paragraph 2
Paragraph 3
Paragraph 4
...
        ↓
Chunks
```

A chunk might contain:

* several sentences
* one paragraph
* a section
* a fixed number of tokens

---

# 9. Why Chunking Matters

### Chunks too large

You retrieve lots of irrelevant information.

```text id="7x4m2q"
Relevant information
+
Lots of unrelated information
```

### Chunks too small

You may lose important context.

```text id="k8v3n5"
"Attendance must be..."
```

but the rest of the sentence is in another chunk.

Therefore:

> **Good chunking balances context and retrieval precision.**

---

# 10. Overlapping Chunks

Sometimes chunks overlap.

For example:

```text id="b7k4m2"
Chunk 1:
A B C D E

Chunk 2:
D E F G H

Chunk 3:
G H I J K
```

The overlap helps preserve context across boundaries.

This is called:

> **Chunk overlap**

---

# 11. Embeddings in RAG

After chunking, each chunk is converted into an embedding.

```text id="q6p3v8"
Document
 ↓
Chunks
 ↓
Embedding Model
 ↓
Vectors
 ↓
Vector Database
```

Example:

```text id="e7m2x9"
Chunk:
"Students must maintain 75% attendance."

        ↓

Embedding:
[0.18, -0.42, 0.71, ...]
```

---

# 12. Vector Database

The embeddings are stored in a vector database.

Conceptually:

```text id="p9w5r3"
Vector DB

Chunk A → [0.12, 0.43, ...]
Chunk B → [0.72, 0.11, ...]
Chunk C → [0.19, 0.81, ...]
Chunk D → [0.33, 0.21, ...]
```

When a query arrives:

```text id="m8x4q2"
Query
 ↓
Embedding
 ↓
Similarity Search
 ↓
Top relevant chunks
```

---

# 13. Similarity Search

A common method is cosine similarity.

Formula:

$$
\text{Cosine Similarity}(A,B)
=============================

\frac{A\cdot B}
{|A||B|}
$$

Higher similarity generally indicates greater semantic similarity.

For example:

```text id="e2m8k4"
Query:
"attendance requirement"

       ↓

Similarity search

       ↓

Chunk A → 0.92
Chunk B → 0.81
Chunk C → 0.24
Chunk D → 0.11
```

The system might retrieve A and B.

---

# 14. Top-K Retrieval

We usually don't retrieve every document.

We retrieve the **top K** most relevant chunks.

For example:

```text id="r5m1q7"
K = 3
```

The system retrieves:

```text id="y3v8n2"
Chunk 17 → similarity 0.94
Chunk 42 → similarity 0.91
Chunk 8  → similarity 0.87
```

These are passed to the LLM.

---

# 15. Full RAG Pipeline

This is the architecture you should memorize:

```text id="w6r4k2"
             DOCUMENTS
                 ↓
              Chunking
                 ↓
             Embeddings
                 ↓
           Vector Database
                 ↓
                 │
                 │
USER QUERY → Embedding
                 ↓
          Similarity Search
                 ↓
          Top-K Documents
                 ↓
        Context + User Query
                 ↓
                LLM
                 ↓
             Final Answer
```

---

# 16. RAG Has Two Major Phases

This is an important way to understand the architecture.

## Phase 1 — Indexing

Prepare the documents.

```text id="a8j3n5"
Documents
 ↓
Clean
 ↓
Chunk
 ↓
Embed
 ↓
Store
```

This usually happens before the user asks questions.

---

## Phase 2 — Retrieval + Generation

When the user asks something:

```text id="c7m2v9"
Query
 ↓
Embed
 ↓
Retrieve
 ↓
Augment
 ↓
Generate
```

---

# 17. RAG Indexing Pipeline

More formally:

```text id="n5x8q3"
Documents
    ↓
Document Processing
    ↓
Chunking
    ↓
Embedding Model
    ↓
Vector Database
```

Example:

```text id="t7p4m2"
Company PDF
    ↓
100 chunks
    ↓
100 embeddings
    ↓
Vector DB
```

---

# 18. RAG Query Pipeline

At query time:

```text id="u4k8z1"
User Query
    ↓
Query Embedding
    ↓
Vector Search
    ↓
Top-K Chunks
    ↓
Prompt Construction
    ↓
LLM
    ↓
Answer
```

---

# 19. RAG vs Normal LLM

| Normal LLM                | RAG                                |
| ------------------------- | ---------------------------------- |
| Uses model knowledge      | Uses model + retrieved information |
| May lack private data     | Can access private documents       |
| Knowledge may be outdated | Can retrieve updated data          |
| More hallucination risk   | Can ground responses               |
| No retrieval step         | Retrieval step                     |

---

# 20. RAG vs Fine-Tuning

Another **very important exam question**.

### RAG

Knowledge stays outside the model.

```text id="c8v5m3"
Documents
 ↓
Retriever
 ↓
LLM
```

### Fine-tuning

Model parameters are modified using training data.

```text id="w2n7q9"
Training Data
 ↓
Training
 ↓
Updated Model
```

### Simple distinction

> **RAG teaches the model what information to look at.**

> **Fine-tuning changes how the model behaves/learns patterns through parameter updates.**

---

# 21. When Should You Use RAG?

Use RAG when you have:

* company documents
* research papers
* product catalogs
* technical documentation
* policies
* manuals
* private knowledge bases
* frequently changing information

Example:

> "Answer questions about our company's internal HR policies."

Perfect RAG use case.

---

# 22. When RAG May Not Be Necessary

Suppose you ask:

> "What is 2 + 2?"

No retrieval required.

Or:

> "Write a Python function to reverse a string."

You may not need RAG.

So:

> Don't add RAG just because you're building an LLM application.

Use it when **external knowledge retrieval is actually needed**.

---

# 23. Hybrid Search

Vector search isn't the only retrieval method.

Sometimes exact keyword matching is important.

Example:

> "Error code `ERR_5007`"

Semantic search may not be ideal.

A good system may combine:

```text id="j5k9r2"
Keyword Search
      +
Vector Search
      ↓
Hybrid Retrieval
```

This can combine:

* lexical matching
* semantic similarity

---

# 24. Re-Ranking

Suppose retrieval returns:

```text id="q3x7m8"
Chunk A → 0.91
Chunk B → 0.89
Chunk C → 0.87
Chunk D → 0.85
```

A second model can re-rank the retrieved chunks based on the actual query.

```text id="m8v2k5"
Initial Retrieval
       ↓
Top 20 chunks
       ↓
Re-ranker
       ↓
Best 5 chunks
       ↓
LLM
```

This can improve retrieval quality.

---

# 25. RAG and Hallucination

Suppose the knowledge base says:

> "The refund period is 30 days."

The user asks:

> "What is the refund period?"

RAG retrieves the relevant policy.

The LLM answers:

> "The refund period is 30 days."

The answer is **grounded** in retrieved evidence.

However:

> **RAG does not eliminate hallucinations.**

The model can still:

* misinterpret context
* ignore retrieved information
* combine unrelated chunks
* generate unsupported claims

So good RAG systems need evaluation and sometimes citations/grounding checks.

---

# 26. RAG Example — College Assistant

Imagine we create a university chatbot.

Documents:

```text id="n7x2m5"
Academic Rules.pdf
Exam Rules.pdf
Attendance Policy.pdf
Fee Structure.pdf
Hostel Rules.pdf
```

User:

> "Can I sit for exams if my attendance is 68%?"

### Retrieval

Query:

```text id="r8k4z1"
"exam eligibility attendance 68%"
```

Retriever finds:

```text id="f5m3q8"
Attendance Policy:
Minimum attendance = 75%
```

and perhaps:

```text id="t2y7n4"
Exam Rules:
Students below minimum attendance may be restricted from examinations.
```

### Augmentation

```text id="c4v8m2"
User question
+
Attendance policy
+
Exam rules
```

### Generation

LLM:

> "According to the retrieved university policies, the minimum attendance is 75%, so 68% attendance may make you ineligible to sit for the examination, subject to any approved exception."

Notice the cautious wording.

The model shouldn't invent exceptions.

---

# 27. RAG + Memory

Now connect this with our previous topic.

An advanced agent could use:

```text id="v2m9x5"
User Memory
+
RAG Knowledge
+
Current Conversation
+
Tools
 ↓
LLM
```

For example:

> "Based on my attendance and the university rules, am I eligible?"

The system might:

```text id="d8x3q1"
Memory:
User attendance = 68%

        +

RAG:
Minimum attendance = 75%

        +

LLM
        ↓
Reasoned answer
```

This is becoming a proper agentic system.

---

# 28. RAG vs Vector Memory

Don't confuse these.

### Vector memory

Stores information about the user/agent/past interactions.

Example:

```text
"User prefers Python."
```

### RAG

Stores/retrieves external knowledge.

Example:

```text
"Company policy allows 30-day returns."
```

Both may use:

> Embeddings + Vector Database + Similarity Search

But their **purpose differs**.

---

# 29. Common RAG Problems

### 1. Poor chunking

Relevant information gets split incorrectly.

### 2. Bad embeddings

Semantic relationships aren't represented well.

### 3. Wrong retrieval

The system retrieves irrelevant documents.

### 4. Too much context

The LLM receives too much irrelevant information.

### 5. Missing information

The required answer isn't in the knowledge base.

### 6. Outdated documents

The retrieved information may no longer be valid.

### 7. Hallucination

The LLM may still generate unsupported information.

---

# 30. RAG Optimization Techniques

To improve RAG:

```text id="v6k2p8"
Better documents
      ↓
Better chunking
      ↓
Better embeddings
      ↓
Better retrieval
      ↓
Re-ranking
      ↓
Good prompt
      ↓
Grounded generation
```

Important techniques include:

* chunk optimization
* metadata filtering
* hybrid search
* re-ranking
* top-K tuning
* query rewriting
* source attribution
* retrieval evaluation

---

# 31. Query Rewriting

Sometimes the user's query isn't ideal for retrieval.

User:

> "Can I give the exam?"

A query rewriting system might convert it into:

```text id="c2m8q7"
"exam eligibility minimum attendance requirements"
```

Then retrieval can work better.

```text id="e9v4m1"
User Query
 ↓
Query Rewriter
 ↓
Improved Search Query
 ↓
Retriever
```

---

# 32. Metadata Filtering

Documents can contain metadata:

```text id="f7k2m9"
Document:
Exam Rules

Metadata:
department = Computer Science
year = 4
semester = 8
```

A query can filter using metadata before/alongside semantic search.

This can dramatically reduce irrelevant results.

---

# 33. Exam Definition

If asked:

> **"What is Retrieval-Augmented Generation?"**

Write:

> **Retrieval-Augmented Generation (RAG) is an architecture that retrieves relevant information from an external knowledge source and provides it as context to a language model so that the model can generate a more relevant and grounded response.**

Then explain:

```text
Query
 ↓
Retrieve
 ↓
Augment
 ↓
Generate
```

---

# Quick Revision Sheet

## RAG

> **Retrieve → Augment → Generate**

### Indexing

```text
Documents
 ↓
Chunking
 ↓
Embeddings
 ↓
Vector DB
```

### Querying

```text
Query
 ↓
Embedding
 ↓
Similarity Search
 ↓
Top-K chunks
 ↓
Context
 ↓
LLM
 ↓
Answer
```

### Important concepts

* Chunking
* Embeddings
* Vector database
* Similarity search
* Top-K retrieval
* Hybrid search
* Re-ranking
* Query rewriting
* Metadata filtering
* Grounding

---

# MUST REMEMBER

If you remember only **five things**, remember these:

1. **RAG = Retrieve + Augment + Generate**
2. Documents are usually **chunked**.
3. Chunks are converted into **embeddings**.
4. Relevant chunks are retrieved using **similarity search**.
5. Retrieved context is given to the **LLM before generation**.

And the biggest distinction:

> **RAG retrieves knowledge; memory retrieves past/user information.**

---

# Active Learning

### Q1 — Conceptual

What are the **three stages of RAG**, and what happens in each stage?

### Q2 — Conceptual

Why do we split documents into chunks instead of embedding an entire 500-page document as one piece?

### Q3 — Conceptual

What is the difference between **RAG and fine-tuning**?

### Q4 — Practical

You are building a chatbot for a college that has:

```text
500 PDFs
↓
Exam rules
Attendance rules
Fee policies
Hostel rules
Academic regulations
```

A student asks:

> **"What is the minimum attendance required for exams?"**

Explain the complete RAG pipeline from **PDF → final answer**, including **chunking, embeddings, vector database, retrieval, and generation**.

After this, we'll finish the syllabus with **Topic 9: Self-Reflection and Self-Correction**, and then I'll give you a **complete Agentic AI revision sheet + mini quiz**.
