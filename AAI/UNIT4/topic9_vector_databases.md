# Topic 9: Vector Databases — FAISS & Chroma

## 1. What is a Vector Database?

A **vector database** is a system used to store and search **vector representations (embeddings)** of data.
Instead of searching only for exact words, it can search based on **meaning and similarity**.

### ELI5

Suppose your database contains:
> "Python is my favorite programming language."

You search:
> "Which programming language do I like?"

There is no exact word match between the two sentences, but their **meaning is similar**.
A vector database can find the stored sentence because their embeddings are close.

---

## 2. Why Do We Need Vector Databases?

Traditional databases are excellent for structured information.
Example:

```text
ID     Name      Age
101    Rahul     20
102    Amit      21
103    Neel      20
```

You can easily search:
```sql
SELECT * FROM students WHERE age = 20;
```

But semantic questions such as:
> "Find documents discussing neural networks."
are more naturally handled using embeddings and vector similarity.

---

## 3. Embeddings

An **embedding** converts data into a numerical vector that represents its meaning.

For example:
```text
"Deep learning uses neural networks"
              ↓
          Embedding
              ↓
[0.21, -0.17, 0.83, 0.42, ...]
```

Another sentence:
```text
"Neural networks are used in deep learning"
```
would produce a vector that is likely close in the embedding space.

Conceptually:
```text
          Vector Space

       A ●
         \
          \  similar meaning
           \
            ● B

A = "Deep learning uses neural networks"
B = "Neural networks are used in deep learning"
```

---

## 4. Vector Similarity

Once information has been converted into vectors, we need to determine **how similar two vectors are**.
Common similarity/distance measures include:

### 1. Cosine Similarity
Measures the angle between vectors.
$$\text{Cosine Similarity}(A,B) = \frac{A\cdot B}{\|A\|\|B\|}$$
A value closer to **1** generally indicates greater directional similarity.

### 2. Euclidean Distance
Measures the straight-line distance between vectors.
$$d(A,B)=\sqrt{\sum_{i=1}^{n}(A_i-B_i)^2}$$
Smaller distance means the vectors are closer.

### 3. Dot Product
$$A\cdot B=\sum_{i=1}^{n}A_iB_i$$
The appropriate metric depends on the embedding model and retrieval setup.

---

## 5. Basic Vector Database Workflow

```text
Documents
    ↓
Split into chunks
    ↓
Embedding Model
    ↓
Vectors
    ↓
Vector Database
    ↓
Similarity Search
    ↓
Relevant Documents
    ↓
LLM
    ↓
Answer
```

This is the foundation of **Retrieval-Augmented Generation (RAG)**.

---

## 6. What is FAISS?

**FAISS** stands for:
> **Facebook AI Similarity Search**

It is a library designed for **efficient similarity search and clustering of dense vectors**.
It is widely used when applications need to search through large collections of embeddings efficiently.

### Simple mental model
> **FAISS = Fast vector similarity-search library.**

---

## 7. FAISS Architecture

Conceptually:
```text
Documents
    ↓
Embedding Model
    ↓
Vectors
    ↓
FAISS Index
    ↓
Similarity Search
    ↓
Nearest Vectors
```

For example:
```text
Query:
"How does CNN work?"

       ↓
   Query embedding

       ↓
FAISS index
       ↓
 ┌───────────────┐
 │ Similar vector│
 │ Similar vector│
 │ Similar vector│
 └───────────────┘
       ↓
Relevant documents
```

---

## 8. What is an Index?

An **index** is a data structure that makes searching vectors more efficient.
Imagine 1 million vectors.
Instead of comparing the query with every vector in the simplest possible way, specialized indexing methods can make similarity search much faster.

```text
1,000,000 vectors
       │
       ▼
     Index
       │
       ▼
Efficient search
```

Different indexing strategies provide different trade-offs between:
* Search speed
* Memory usage
* Accuracy
* Build time

For an exam, remember:
> **Index = structure that helps efficiently search vectors.**

---

## 9. What is Chroma?

**Chroma** is a vector database/system designed for applications involving **embeddings, semantic search, and AI/RAG workflows**.
It can store information such as:
* Documents
* Embeddings
* Metadata
* IDs
and retrieve relevant records based on similarity.

### Mental model
> **Chroma = Developer-friendly vector storage and retrieval system for AI applications.**

---

## 10. Chroma Architecture

```text
Documents
    │
    ▼
Embedding Model
    │
    ▼
Embeddings
    │
    ▼
Chroma
 ┌───────────────┐
 │ Embeddings    │
 │ Documents     │
 │ Metadata      │
 │ IDs           │
 └───────────────┘
    │
    ▼
Similarity Search
    │
    ▼
Relevant Results
```

---

## 11. FAISS vs Chroma

This is a very important exam/interview comparison.

| Feature | FAISS | Chroma |
| :--- | :--- | :--- |
| **Full form** | Facebook AI Similarity Search | Chroma |
| **Main purpose** | Efficient vector similarity search | Vector storage + retrieval for AI applications |
| **Type** | Similarity-search library | Vector database/system |
| **Focus** | High-performance vector search | Developer-friendly AI/RAG workflows |
| **Metadata/doc storage** | Not its primary focus | Supported |
| **Persistence** | Depends on how it is configured/used | Designed to support persistent collections |
| **Typical use** | Fast local similarity search | RAG, semantic search, AI applications |
| **API simplicity** | More low-level | More application-oriented |

### Easy memory trick
> **FAISS → Focus on similarity search**
> **Chroma → Focus on AI application storage + retrieval**

These aren't mutually exclusive: systems can combine a vector index/library with other storage components.

---

## 12. FAISS Example — Conceptual

Suppose we have three documents:
```text
D1: "CNN is used for image processing."
D2: "RNN is useful for sequential data."
D3: "Transformers use attention mechanisms."
```

We convert them into embeddings:
```text
D1 → [0.1, 0.8, 0.2, ...]
D2 → [0.7, 0.2, 0.5, ...]
D3 → [0.3, 0.6, 0.9, ...]
```

Then store them in a FAISS index.

User asks:
> "Which model is used for image processing?"

Query → embedding → FAISS search.
The nearest vector corresponds to:
```text
D1: CNN is used for image processing.
```

---

## 13. Chroma Example — Conceptual

Suppose we store:
```text
Document:
"Python is widely used in machine learning."

Metadata:
{
    "topic": "Programming",
    "source": "Notes"
}
```

Chroma can maintain the document, its embedding, and metadata.

A query such as:
> "What programming language is used in ML?"
can retrieve the relevant document based on semantic similarity.

---

## 14. Metadata

Metadata is additional information associated with stored data.
Example:
```json
{
  "topic": "Deep Learning",
  "chapter": "CNN",
  "source": "Lecture Notes",
  "page": 25
}
```
Metadata is useful for **filtering and organization**.
For example:
> "Search only documents from the CNN chapter."

Conceptually:
```text
Query
  │
  ├── Semantic similarity
  │
  └── Metadata filter
          │
          ▼
     Relevant results
```

---

## 15. Vector Database in RAG

Vector databases are heavily used in **RAG — Retrieval-Augmented Generation**.

### RAG workflow
```text
             Documents
                 │
                 ▼
              Chunking
                 │
                 ▼
             Embeddings
                 │
                 ▼
          Vector Database
                 │
          ┌──────┴──────┐
          │             │
      User Query     Query Embedding
          │             │
          └──────┬──────┘
                 ▼
          Similarity Search
                 │
                 ▼
        Relevant Documents
                 │
                 ▼
               LLM
                 │
                 ▼
              Answer
```

### Why?
The LLM can use retrieved information rather than relying only on information encoded in its parameters.

---

## 16. FAISS + Chroma + LangChain

These technologies can work together.
For example:
```text
             User
               │
               ▼
          LangChain
               │
               ▼
        Retriever / Agent
               │
               ▼
       FAISS or Chroma
               │
               ▼
       Relevant Documents
               │
               ▼
             LLM
               │
               ▼
            Answer
```
The exact integration APIs depend on the framework versions, but the architecture remains similar.

---

## 17. Advantages of Vector Databases

1. **Semantic Search:** Find information based on meaning rather than exact keywords.
2. **Fast Retrieval:** Indexes can make similarity search efficient.
3. **RAG Support:** Useful for retrieving relevant information before generation.
4. **Large-Scale Search:** Can manage large collections of embeddings depending on the system and configuration.
5. **Metadata Filtering:** Useful for narrowing search results.
6. **AI Memory:** Can be used as part of long-term semantic memory systems.

---

## 18. Limitations

1. **Embedding Quality Matters:** Poor embeddings can lead to poor retrieval.
2. **Storage Cost:** Large embedding collections require storage.
3. **Retrieval Errors:** The most relevant document may not always be retrieved.
4. **Chunking Matters:** Poorly chosen document chunks can reduce retrieval quality.
5. **Similarity ≠ Truth:** A highly similar document isn't automatically factually correct. This is especially important in RAG systems.

---

## 19. Exam-Ready Definition

> **A vector database is a system used to store, index, and retrieve vector embeddings based on similarity. It enables semantic search and is commonly used in RAG and AI memory systems. FAISS is a high-performance similarity-search library, while Chroma provides a more application-oriented system for storing and retrieving embeddings, documents, and metadata.**

---

## 📝 Quick Revision

```text
Embedding
   ↓
Numerical representation of meaning

Vector Database
   ↓
Stores + retrieves embeddings

FAISS
   ↓
Fast similarity search

Chroma
   ↓
Vector storage + retrieval for AI applications

Similarity
   ↓
Cosine / Euclidean / Dot Product

RAG
   ↓
Retrieve relevant information → Give it to LLM → Generate answer
```

### Golden distinction
> **FAISS = similarity-search library**
> **Chroma = vector storage/retrieval system for AI applications**

### Overall pipeline
$$\text{Text} \rightarrow \text{Embedding} \rightarrow \text{Vector DB} \rightarrow \text{Similarity Search} \rightarrow \text{Relevant Context} \rightarrow \text{LLM}$$

> **Next topic → Topic 10: Building Task-Specific AI Assistants.**
