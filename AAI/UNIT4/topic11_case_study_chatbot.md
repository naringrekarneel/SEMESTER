# Topic 11: Case Study — Building an AI Chatbot

Now we’ll put the concepts together and build a **task-specific chatbot** using the Agentic AI architecture.

---

## 1. What is an AI Chatbot?

An **AI chatbot** is a software application that communicates with users using natural language and generates responses using AI models such as LLMs.

A basic chatbot:
```text
User
 ↓
LLM
 ↓
Response
```

An **agentic chatbot** can go further:
```text
User
 ↓
Agent
 ↓
 ┌──────────────┬──────────────┐
 ▼              ▼              ▼
Memory         Tools          RAG
 │              │              │
 ▼              ▼              ▼
Past info      APIs        Knowledge Base
 └──────────────┼──────────────┘
                ▼
               LLM
                ↓
             Response
```

---

## 2. Case Study: College AI Assistant

Let's design a practical chatbot:
> **College AI Assistant**

Its purpose is to help students with:
* College FAQs
* Subjects
* Timetable
* Attendance
* Exam information
* Study material
* Basic administrative questions

---

## 3. Requirements

Before building it, define what the chatbot should do.

### Functional requirements
The chatbot should:
1. Understand natural-language questions.
2. Answer college-related questions.
3. Retrieve information from college documents.
4. Remember relevant conversation context.
5. Use tools when calculations or external actions are required.
6. Handle unknown questions appropriately.

### Example
User:
> "When is the DBMS exam?"

The chatbot should search the relevant exam information rather than simply guess.

---

## 4. System Architecture

A good exam diagram:

```text
                         USER
                          │
                          ▼
                 ┌────────────────┐
                 │  AI CHATBOT    │
                 └───────┬────────┘
                         │
                 ┌───────▼────────┐
                 │     AGENT      │
                 └───────┬────────┘
                         │
          ┌──────────────┼──────────────┐
          ▼              ▼              ▼
       Memory           Tools          RAG
          │              │              │
          ▼              ▼              ▼
     Conversation      APIs        Vector DB
       History                         │
          │                            ▼
          │                      College Documents
          └──────────────┬──────────────┘
                         ▼
                        LLM
                         │
                         ▼
                  Final Response
```

---

## 5. Step 1 — User Sends a Message

Example:
> "What is the attendance requirement for appearing in the exam?"

The chatbot receives the message.
```text
User Question
      ↓
"What is the attendance requirement?"
```

---

## 6. Step 2 — Agent Understands the Request

The agent determines what kind of request this is.

Possible categories:
```text
Question
  │
  ├── General FAQ
  ├── Academic information
  ├── Attendance calculation
  ├── Exam information
  ├── Timetable
  └── Unknown
```
The agent decides what action is appropriate.

---

## 7. Step 3 — Retrieve Knowledge

Suppose the college rules are stored in PDFs.
The system has already performed:
```text
College PDFs
     ↓
Document Chunking
     ↓
Embeddings
     ↓
Vector Database
```

When the user asks a question:
```text
Question
   ↓
Embedding
   ↓
Vector Search
   ↓
Relevant College Rule
```
The retrieved information is given to the LLM.

---

## 8. Step 4 — Generate Answer

The LLM receives:
```text
System Instructions
       +
User Question
       +
Retrieved College Information
       +
Conversation Context
       ↓
      LLM
       ↓
Final Answer
```

The chatbot can now generate a response grounded in the retrieved information.

---

## 9. Adding Memory

Suppose the student says:
> "I'm in third year CSE."

The system can maintain relevant conversation context.

Later:
> "What subjects do I have?"

The chatbot can use the current conversation context to understand that the question refers to the student's third-year CSE curriculum.

```text
Previous Conversation
        ↓
      Memory
        ↓
Current Query
        ↓
      Agent
```

---

## 10. Adding Tools

Now suppose the student asks:
> "My attendance is 68% and I attended 34 out of the last 40 lectures. What will happen if I miss the next 3?"

A calculator tool could perform the arithmetic.

Conceptually:
```text
User
 ↓
Agent
 ↓
Attendance Calculator
 ↓
Calculation
 ↓
Result
 ↓
LLM
 ↓
Explanation
```
This is better than expecting the LLM to perform every operation itself.

---

## 11. Example Conversation

### User
> What is the attendance requirement?

### Agent
Retrieves the relevant college rule.

### Chatbot
> According to the retrieved college policy, the required attendance is X%.

---

### User
> My attendance is 72%. Can I miss tomorrow's lecture?

The agent may need:
```text
Attendance Data
       +
Timetable
       +
Attendance Rule
       ↓
Calculation
       ↓
Answer
```
The important part is that the agent **uses information and tools rather than blindly generating an answer**.

---

## 12. Handling Unknown Questions

A good chatbot should **not hallucinate** when it doesn't know something.

Suppose the user asks:
> "Who will be the guest lecturer next month?"

If the system has no reliable information, it should say that the information isn't available rather than inventing a name.

Conceptually:
```text
Question
   ↓
Search Knowledge
   ↓
No reliable information
   ↓
"I'm unable to find that information."
```

This is an important principle:
> **No evidence → Don't fabricate an answer.**

---

## 13. Complete Chatbot Workflow

```text
                USER
                  │
                  ▼
           User Question
                  │
                  ▼
              AI Agent
                  │
          Understand Intent
                  │
        ┌─────────┼─────────┐
        ▼         ▼         ▼
      Memory     Tools      RAG
        │         │         │
        │         ▼         ▼
        │        APIs    Vector DB
        │                   │
        └─────────┬─────────┘
                  ▼
                 LLM
                  │
                  ▼
            Final Response
                  │
                  ▼
                USER
```

---

## 14. Technologies That Can Be Used

A possible technology stack:

| Component | Example |
| :--- | :--- |
| **LLM** | GPT / other LLM |
| **Framework** | LangChain |
| **Agent** | LangChain agent |
| **Vector DB** | FAISS / Chroma |
| **Backend** | Python / FastAPI |
| **Database** | PostgreSQL |
| **Frontend** | React / Flutter |
| **External services** | REST APIs |
| **Memory** | Database/vector store |

The exact technology choices depend on the application requirements.

---

## 15. Security

A college chatbot may have sensitive information.
Therefore:

### Authentication
Verify the user.

### Authorization
Only allow permitted data access.

### Input validation
Validate user/tool inputs.

### Data protection
Protect stored information.

### Tool restrictions
Don't allow the chatbot to perform unauthorized operations.

Example:
```text
Student
   ↓
Chatbot
   ↓
"Delete my academic record"
   ↓
Authorization Check
   ↓
Not permitted
```

---

## 16. Advantages

1. **24/7 Availability:** Students can ask questions anytime.
2. **Faster Information Access:** Users don't need to manually search through documents.
3. **Natural Interaction:** Users can ask questions in ordinary language.
4. **Personalization:** Memory can provide context-aware responses.
5. **Automation:** Routine questions can be handled automatically.
6. **Knowledge Retrieval:** RAG can provide answers based on institutional documents.

---

## 17. Limitations

1. **Hallucination:** The model may generate incorrect information.
2. **Retrieval Errors:** The correct document may not be retrieved.
3. **Outdated Knowledge:** Documents and policies may change.
4. **Privacy Risks:** Personal information needs careful handling.
5. **API/Tool Failures:** External services may be unavailable.
6. **Cost:** Frequent LLM and API calls can increase costs.

---

## 18. Evaluation of the Chatbot

We can evaluate it using:

1. **Accuracy:** Does it provide correct information?
2. **Relevance:** Does it answer the actual question?
3. **Groundedness:** Is the answer supported by retrieved information?
4. **Response Time:** How quickly does it respond?
5. **Tool Accuracy:** Does it select the correct tool?
6. **User Satisfaction:** Do users find the chatbot useful?

---

## 19. Exam-Ready Answer

> **An AI chatbot is a conversational application that uses an LLM to understand user queries and generate natural-language responses. An agentic chatbot can combine an LLM with memory, tools, APIs, and retrieval systems such as vector databases. When a user asks a question, the agent determines the required action, retrieves relevant information or calls appropriate tools, provides the results to the LLM, and generates the final response.**

### Architecture:

```text
User
 ↓
Agent
 ↓
Intent Understanding
 ↓
 ┌──────────┬──────────┬──────────┐
 ▼          ▼          ▼
Memory     Tools       RAG
 │          │          │
 ▼          ▼          ▼
History    APIs      Vector DB
 └──────────┼──────────┘
            ▼
           LLM
            ↓
      Final Response
```

---

## 📝 Quick Revision

```text
AI CHATBOT
    ↓
User Query
    ↓
Agent
    ↓
Understand Intent
    ↓
Retrieve Memory / Knowledge
    ↓
Use Tools / APIs if required
    ↓
LLM Generates Response
    ↓
Final Answer
```

### Golden concept
> **A basic chatbot mainly responds; an agentic chatbot can reason about what information or tools it needs before responding.**

### Key technologies
**LLM + Agent + RAG + Vector DB + Memory + Tools + APIs**

> **Next topic → Topic 12: Case Study — Building a Research Assistant.**
