# Topic 12: Case Study — Building an AI Research Assistant

A **research assistant** is a task-specific AI system designed to help users **search, collect, analyze, summarize, and organize information** about a topic.

This is one of the best examples for understanding how **agents + tools + APIs + memory + vector databases + RAG** work together.

---

## 1. What Does an AI Research Assistant Do?

Suppose the user asks:
> **"Research the impact of AI on cybersecurity and prepare a report."**

A simple LLM might generate an answer from its existing knowledge.
A research assistant can perform a workflow like:

```text
User Topic
    ↓
Research Agent
    ↓
Search Sources
    ↓
Collect Information
    ↓
Retrieve Relevant Documents
    ↓
Analyze Information
    ↓
Summarize
    ↓
Review
    ↓
Generate Report
```

So it acts more like a **research team** than a simple chatbot.

---

## 2. Main Objectives

A research assistant should be able to:
1. Understand the research question.
2. Search relevant information.
3. Retrieve useful documents.
4. Extract important information.
5. Compare information from different sources.
6. Summarize findings.
7. Organize the results.
8. Generate a final report.
9. Cite or identify sources where appropriate.

---

## 3. Architecture

A strong exam diagram:

```text
                         USER
                          │
                          ▼
                  Research Request
                          │
                          ▼
                ┌──────────────────┐
                │ Research Agent   │
                └────────┬─────────┘
                         │
             ┌───────────┼───────────┐
             ▼           ▼           ▼
         Web Search    Vector DB    Memory
             │           │           │
             ▼           ▼           ▼
          Sources    Documents    Previous
                                    Research
             └───────────┼───────────┘
                         ▼
                      Analysis
                         │
                         ▼
                    Summarization
                         │
                         ▼
                       Review
                         │
                         ▼
                    Final Report
```

---

## 4. Step 1 — Understand the Research Question

The agent first analyzes the user's request.

Example:
> "Analyze the impact of generative AI on cybersecurity."

The agent can identify:
```text
Topic:
Generative AI

Domain:
Cybersecurity

Objective:
Analyze impact

Output:
Research report
```

This helps determine what research steps are needed.

---

## 5. Step 2 — Break the Problem into Subtasks

A complex research question can be decomposed.

For example:
```text
Main Question
     │
     ├── What is Generative AI?
     │
     ├── How is it used in cybersecurity?
     │
     ├── What are the benefits?
     │
     ├── What are the risks?
     │
     ├── What are real-world applications?
     │
     └── What are future trends?
```

This is an important **agentic behavior**:
> **Break a large problem into smaller tasks.**

---

## 6. Step 3 — Search for Information

The research agent can use tools such as:
* Web search
* Academic databases
* Internal documents
* APIs
* File search

Conceptually:
```text
Research Agent
      ↓
Search Tool
      ↓
External Sources
      ↓
Search Results
```
The agent can perform multiple searches based on the subtasks.

---

## 7. Step 4 — Store and Retrieve Documents

Suppose the agent collects 100 documents.
Storing all of them directly in the prompt would be inefficient.

Instead:
```text
Documents
    ↓
Chunking
    ↓
Embeddings
    ↓
Vector Database
```

Later, when the agent needs information:
```text
Research Question
      ↓
Embedding
      ↓
Vector Search
      ↓
Relevant Documents
```

This is the **RAG approach**.

---

## 8. Step 5 — Analyze Information

The agent can analyze the retrieved information.

For example:
```text
Source A → Benefits of AI
Source B → Cybersecurity risks
Source C → Industry applications
Source D → Research findings
```

The agent can compare:
* Agreements
* Differences
* Trends
* Evidence
* Limitations

---

## 9. Step 6 — Summarization

After collecting and analyzing the information, the agent generates concise summaries.

Example:
```text
100 pages of information
        ↓
Relevant sections
        ↓
Key findings
        ↓
Concise summary
```

This reduces the amount of information the user needs to read.

---

## 10. Step 7 — Source Management

A good research assistant should keep track of **where information came from**.

For example:
```text
Finding 1
   ↓
Source A

Finding 2
   ↓
Source B

Finding 3
   ↓
Source C
```

This improves:
* Traceability
* Verification
* Trust
* Reproducibility

It also helps distinguish sourced information from generated interpretation.

---

## 11. Step 8 — Review

Before producing the final report, a separate reviewer step or agent can check:
* Missing information
* Contradictions
* Unsupported claims
* Relevance
* Structure
* Citation/source mapping
* Formatting

Example:
```text
Researcher
    ↓
Draft Report
    ↓
Reviewer
    ↓
Corrections
    ↓
Final Report
```

This is an example of **multi-agent collaboration**.

---

## 12. Multi-Agent Research Assistant

We can divide the research work among multiple agents.

```text
                 Research Manager
                       │
          ┌────────────┼────────────┐
          ▼            ▼            ▼
      Researcher    Analyst      Reviewer
          │            │            │
          ▼            ▼            ▼
       Sources      Analysis      Quality
                                    Check
                       │
                       ▼
                    Writer
                       │
                       ▼
                 Final Report
```

### Agent roles
* **Researcher:** Finds information.
* **Analyst:** Studies and compares information.
* **Writer:** Produces the report.
* **Reviewer:** Checks quality and consistency.
* **Manager:** Coordinates the workflow.

---

## 13. Research Assistant Workflow

The complete process can be remembered as:

```text
UNDERSTAND
    ↓
DECOMPOSE
    ↓
SEARCH
    ↓
RETRIEVE
    ↓
ANALYZE
    ↓
SUMMARIZE
    ↓
REVIEW
    ↓
GENERATE REPORT
```

---

## 14. Example

### User:
> "Prepare a report on the advantages and risks of Generative AI in education."

### Agent:
**Step 1:** Understand the topic.
`Generative AI + Education`

**Step 2:** Decompose:
```text
Advantages
Risks
Applications
Examples
Future implications
```

**Step 3:** Search relevant sources.
**Step 4:** Store useful documents.
**Step 5:** Retrieve relevant information.
**Step 6:** Analyze the evidence.
**Step 7:** Generate a structured report.

Possible final structure:
```text
1. Introduction
2. Applications
3. Advantages
4. Risks
5. Challenges
6. Future Scope
7. Conclusion
8. Sources
```

---

## 15. Role of Memory

Memory becomes useful when research is performed over multiple sessions.

Example:
```text
Day 1:
Research topic selected.

Day 2:
Sources collected.

Day 3:
Analysis performed.

Day 4:
Final report generated.
```

The agent can retain useful state about the ongoing project.
```text
Previous Research
       ↓
Memory
       ↓
New Research Task
```

This is particularly useful for **long-running research projects**.

---

## 16. Role of Tools and APIs

Tools give the research assistant external capabilities.

```text
Research Agent
      │
      ├── Web Search Tool
      ├── PDF Reader
      ├── Calculator
      ├── Database
      ├── Academic Search API
      └── Document Tool
```

For example, if the research requires numerical analysis:
```text
Research Agent
      ↓
Calculator / Python Tool
      ↓
Analysis
```

---

## 17. Role of Vector Database

The vector database provides semantic retrieval.

```text
Research Documents
       ↓
Embeddings
       ↓
FAISS / Chroma
       ↓
Similarity Search
       ↓
Relevant Information
```

This prevents the agent from having to process every stored document for every query.

---

## 18. Challenges

1. **Information Quality:** Search results may contain inaccurate or low-quality information.
2. **Hallucination:** The LLM may generate claims that aren't supported by retrieved sources.
3. **Retrieval Errors:** The relevant document might not be retrieved.
4. **Source Reliability:** Different sources may disagree in quality or credibility.
5. **Outdated Information:** Research can become outdated as information changes.
6. **Large Amounts of Data:** Processing huge numbers of documents can increase cost and latency.
7. **Citation Problems:** The system may incorrectly associate claims with sources if source tracking is poorly designed.

---

## 19. Advantages

* **Faster Research:** Automates repetitive searching and summarization.
* **Information Organization:** Structures large amounts of information.
* **Multi-Step Reasoning:** Can break complex research into subtasks.
* **Source Retrieval:** Can retrieve relevant documents using RAG.
* **Collaboration:** Multiple agents can specialize in different research tasks.
* **Personalization:** Memory can maintain research context across sessions.

---

## 20. Research Assistant vs Normal Chatbot

| Feature | Normal Chatbot | Research Assistant |
| :--- | :--- | :--- |
| **Main purpose** | Conversation | Research |
| **Web/search tools** | May not have them | Commonly used |
| **Document retrieval** | Limited/optional | Important |
| **Vector database** | Optional | Often useful |
| **Multi-step workflow** | Limited | Common |
| **Source tracking** | May be limited | Important |
| **Analysis** | Basic to advanced | Central task |
| **Report generation** | Possible | Core functionality |

---

## 21. Exam-Ready Answer

> **An AI research assistant is a task-specific agentic system that automates research activities such as searching, retrieving, analyzing, summarizing, and organizing information. It can combine an LLM with search tools, APIs, memory, vector databases, and RAG. The system decomposes a research question into subtasks, collects relevant information, retrieves useful documents, analyzes the results, verifies or reviews the output, and generates a structured report with appropriate source information.**

### Architecture:

```text
User
 ↓
Research Agent
 ↓
Task Decomposition
 ↓
Search Tools / APIs
 ↓
Documents
 ↓
Embeddings
 ↓
Vector Database
 ↓
Relevant Information
 ↓
Analysis
 ↓
Review
 ↓
LLM
 ↓
Final Research Report
```

---

## 📝 Quick Revision

```text
Research Assistant

UNDERSTAND
    ↓
DECOMPOSE
    ↓
SEARCH
    ↓
RETRIEVE
    ↓
ANALYZE
    ↓
SUMMARIZE
    ↓
REVIEW
    ↓
REPORT
```

### Golden concept
> **Research Assistant = Agent + Search + RAG + Tools + Memory + Analysis + Report Generation**

### Most important components
* **Agent** → decides what research steps to perform
* **Tools** → search and external actions
* **Vector DB** → stores/retrieves embeddings
* **RAG** → provides relevant retrieved context
* **Memory** → maintains research history
* **LLM** → understands, analyzes, and generates
* **Reviewer** → checks the result

> **Next topic → Topic 13: Case Study — Building an Automation Bot.**
