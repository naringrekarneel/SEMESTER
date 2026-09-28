# Topic 1: LangChain Basics

## 1. ELI5: What is LangChain?

Imagine you have an AI model like GPT.

By itself, it is basically:
> **You give it text → it gives you an answer.**

But real applications need much more.
For example, imagine you're building a college study assistant.
You want it to:
* Read a PDF.
* Understand the student's question.
* Search the PDF.
* Ask the LLM to generate an answer.
* Remember previous questions.
* Maybe use a calculator.
* Maybe access a database.

Doing all of this manually would be messy.

**LangChain is a framework that helps you connect these components together.**

Think:
> **LLM + prompts + data + tools + memory + workflows = AI application**

LangChain provides the building blocks for this.

---

## 2. What is LangChain?

**LangChain** is a framework for developing applications powered by large language models (LLMs).

It provides abstractions for connecting an LLM with:
* Prompt templates
* Models
* Chains
* Tools
* Agents
* Retrievers
* Vector databases
* Memory/state
* External APIs

The important idea is:
> **LangChain doesn't replace the LLM. It helps you build an application around the LLM.**

---

## 3. Why do we need LangChain?

Suppose you want to build a **Simple AI application**:
```text
User
 ↓
Prompt
 ↓
LLM
 ↓
Answer
```
Easy.

But suppose you want an **AI research assistant**:
```text
User question
      ↓
Search web
      ↓
Retrieve relevant information
      ↓
Process information
      ↓
LLM
      ↓
Generate answer
      ↓
Return sources
```
Now you have multiple components.
LangChain helps organize this workflow.

---

## 4. Core Components of LangChain

These are very important for exams and interviews.

```text
                    LangChain
                       │
       ┌───────────────┼────────────────┐
       │               │                │
    Models           Prompts          Chains
       │               │                │
       ├───────────────┼────────────────┤
       │               │                │
     Tools           Agents          Retrievers
       │               │                │
       └───────────────┼────────────────┘
                       │
                    Memory
                       │
                Vector Stores
```
Let's understand each.

---

## 5. Models

The model is the brain that generates or processes information.
Examples include:
* OpenAI models
* Anthropic models
* Google models
* Local open-source models

Conceptually:
```text
Input
  ↓
LLM
  ↓
Output
```

Example:
```text
Input:
"Explain neural networks in simple terms."
        ↓
      LLM
        ↓
Output:
"A neural network is a computer model inspired by the brain..."
```

In LangChain, models can be integrated into a common application workflow.

---

## 6. Prompt Templates

Instead of manually writing prompts every time, we can create reusable templates.

For example:
> `Explain {topic} in simple terms for a {student_level} student.`

Then:
* `topic` = "CNN"
* `student_level` = "beginner"

becomes:
> `Explain CNN in simple terms for a beginner student.`

This is useful because applications often generate prompts dynamically.

**Exam point:**
> Prompt templates provide reusable and parameterized prompts for interacting with language models.

---

## 7. Chains

A chain connects multiple operations together.

For example:
```text
Question
   ↓
Prompt
   ↓
LLM
   ↓
Output Parser
   ↓
Final Answer
```
Each step feeds information to the next.

A simple chain might be:
```text
Input → Prompt Template → LLM → Output
```

A more complex chain:
```text
Question → Retrieve information → Create prompt → LLM → Format answer
```
We'll study Chains in detail in Topic 2.

---

## 8. Tools

A language model normally cannot magically interact with the outside world.
For example, suppose you ask:
> "What is the current temperature in Mumbai?"

An LLM may know general information, but it needs a tool/API to obtain current weather information.
**A tool gives the model an ability.**

Examples:
* Calculator
* Weather API
* Web search
* Database
* Python interpreter
* Email API
* File system

Conceptually:
```text
LLM
 │
 ├── Calculator
 ├── Web Search
 ├── Database
 └── Weather API
```
We'll study Tools separately.

---

## 9. Agents

This is where things get interesting.
A normal chain follows a predefined sequence.
```text
Input → Step 1 → Step 2 → Step 3
```

**An agent can decide what to do.**

For example:
> "Find the current weather in Mumbai and convert the temperature to Fahrenheit."

The agent might reason:
```text
I need current weather.
        ↓
Use Weather Tool
        ↓
Get temperature
        ↓
Need conversion
        ↓
Use Calculator
        ↓
Return answer
```

So:
> **Chain = predefined workflow**
> **Agent = dynamically decides which actions/tools to use**

This distinction is VERY important.

---

## 10. Retrievers

Suppose you have a 500-page textbook.
You don't want to send the entire textbook to the LLM every time.

Instead:
```text
User Question
      ↓
Retriever
      ↓
Find relevant sections
      ↓
LLM
      ↓
Answer
```

A retriever searches a knowledge source and returns relevant information.
This becomes especially important with **RAG — Retrieval-Augmented Generation**.

---

## 11. Vector Stores

A vector database stores information in a form that allows semantic similarity search.

For example:
> "How does backpropagation work?"

could retrieve:
> "Backpropagation calculates gradients and updates neural-network weights..."

even though the wording isn't exactly the same.

Popular vector stores include:
* FAISS
* Chroma

These are explicitly in your syllabus, so we'll cover them later.

---

## 12. Memory

Suppose you tell your chatbot:
> "My name is Neel."

Then:
> "What's my name?"

Without appropriate state/memory handling, the application may not know.
Memory/state allows an application to maintain information across interactions.

Conceptually:
```text
Conversation 1
     ↓
   Memory
     ↓
Conversation 2
     ↓
   Memory
     ↓
Conversation 3
```
We'll later distinguish conversational state from longer-term memory and vector-based retrieval.

---

## 13. Complete LangChain Architecture

Put everything together:

```text
                         USER
                           │
                           ▼
                    Prompt Template
                           │
                           ▼
                         LLM
                           │
              ┌────────────┼────────────┐
              │            │            │
              ▼            ▼            ▼
            Tools       Retriever     Memory
              │            │            │
              ▼            ▼            ▼
         External       Vector       Previous
          Systems       Store       Information
              │            │            │
              └────────────┼────────────┘
                           ▼
                         Agent
                           │
                           ▼
                      Final Answer
```
This is the basic mental model you should carry forward.

---

## 14. Real-World Example — College Study Assistant

Suppose we create an **"AI Study Buddy"**.
A student asks:
> "Explain ResNet using my Deep Learning notes."

The application could work like:
```text
Student
   │
Question
   │
Retriever
   │
Search vector database
   │
Relevant notes
   │
Prompt Template
   │
LLM
   │
Answer
```

Now the student asks:
> "Also create 5 MCQs."

The application can generate the questions using another chain.

If the student asks:
> "Calculate my marks percentage."

The application could use a calculator tool.

So a real application may combine:
```text
LangChain
   │
   ├── LLM
   ├── Prompts
   ├── Chains
   ├── Tools
   ├── Agents
   ├── Retrieval
   ├── Memory
   └── Vector Database
```

---

## 15. Chain vs Agent — Must Remember

| Feature | Chain | Agent |
| :--- | :--- | :--- |
| **Workflow** | Predefined | Dynamic |
| **Decision-making** | Limited | Yes |
| **Tool selection** | Usually predetermined | Can choose dynamically |
| **Predictability** | Higher | Lower |
| **Complexity** | Simpler | More complex |
| **Example** | Question → LLM → Answer | LLM decides which tools to use |

### One-line memory trick
> **Chain follows instructions. Agent decides instructions.**

---

## 16. Worked Example

Suppose our task is:
> "Translate a sentence and summarize the translation."

**Using a chain:**
We define:
```text
Input → Translation → Summary → Output
```
Step-by-step:
1. **Input:** "Artificial intelligence is transforming healthcare."
2. **Translation:** "AI is transforming healthcare." → Translated text
3. **Summary:** Translated text → LLM → Short summary

The sequence was predetermined. Therefore, this is a **chain**.

Now imagine:
> "Find information about AI healthcare applications and summarize the latest findings."

The system may decide:
```text
Search web → Retrieve information → Read relevant sources → Summarize
```
It might decide that a calculator isn't needed but web search is.
That is an **agent-like workflow**.

---

## 17. Why LangChain is Useful

1. **Modularity:** Different components can be connected together.
2. **Integration:** It can connect LLMs with external services and data sources.
3. **Reusability:** Prompt templates, tools, and workflows can be reused.
4. **Retrieval:** It supports applications that need external knowledge.
5. **Agents:** It provides abstractions for tool-using AI systems.
6. **Application development:** It helps turn an LLM into a complete application rather than just a chatbot.

---

## 18. Exam Answer — Definition

If asked:
**"What is LangChain?"**

Write:
> LangChain is a framework for developing applications powered by large language models. It provides components for integrating language models with prompts, chains, tools, agents, retrievers, memory, external APIs and vector databases. It simplifies the development of complex LLM-based applications by allowing different components to be connected into reusable workflows.

That's a solid exam definition.

---

## 📝 Quick Revision

### LangChain
* Framework for building LLM-powered applications
* Does not replace the LLM
* Connects LLMs with other application components

### Important components
* **Model** → generates/processes information
* **Prompt** → tells model what to do
* **Chain** → predefined sequence
* **Tool** → gives AI an external capability
* **Agent** → decides what actions/tools to use
* **Retriever** → finds relevant information
* **Vector store** → stores/searches embeddings
* **Memory/state** → maintains useful context

### Most important distinction
> **Chain = fixed workflow**
> **Agent = dynamic decision-making**
