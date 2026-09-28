# Topic 2: Chains in LangChain

## 1. ELI5: What is a Chain?

Imagine making a sandwich.
You don't randomly do things. You follow a sequence:

```text
Take bread
   ↓
Add cheese
   ↓
Add vegetables
   ↓
Add sauce
   ↓
Finish sandwich
```

A **Chain** in LangChain works similarly.
It connects multiple steps together so that the **output of one step becomes the input of the next step**.

> **Chain = a sequence of connected operations used to accomplish a task.**

---

## 2. Basic Structure

The simplest LLM chain looks like:

```text
User Input
    ↓
Prompt Template
    ↓
LLM
    ↓
Output Parser
    ↓
Final Output
```

For example:

```text
Topic: "Neural Networks"
        ↓
Prompt: "Explain {topic} simply"
        ↓
       LLM
        ↓
"Neural networks are..."
```

Each component performs one job.

---

## 3. Why Do We Need Chains?

Without chains, we might have to manually execute every step.

Suppose you want an AI system to:
1. Take a topic.
2. Explain it.
3. Generate questions.
4. Generate answers.
5. Format everything.

Without a chain:
```text
Step 1 → manually call LLM
Step 2 → manually take output
Step 3 → manually call LLM
Step 4 → manually take output
Step 5 → manually format
```

With a chain:
```text
Input
 ↓
Explanation Chain
 ↓
Question Generation
 ↓
Answer Generation
 ↓
Formatting
 ↓
Final Output
```

The workflow becomes organized and reusable.

---

## 4. Important Characteristics of Chains

### 1. Sequential execution
Steps usually happen in a defined order.

### 2. Data flow
Output from one step can become input to another.

### 3. Modularity
Each step can perform a specific operation.

### 4. Reusability
The same chain can be used for many inputs.

### 5. Automation
Once configured, the workflow can execute automatically.

---

## 5. Simple Example

Suppose the user enters:
```text
"Explain CNN"
```

Our chain is:
```text
User Input
    ↓
Prompt Template
    ↓
LLM
    ↓
Output Parser
    ↓
Final Answer
```

### Step 1 — User Input
```text
CNN
```

### Step 2 — Prompt Template
Template:
```text
Explain {topic} in simple terms.
Give one real-world example.
```

After inserting the topic:
```text
Explain CNN in simple terms.
Give one real-world example.
```

### Step 3 — LLM
The LLM processes the prompt.

### Step 4 — Output Parser
The output can be converted into the required format.

### Step 5 — Final Output
```text
CNN stands for Convolutional Neural Network...

Example:
CNNs are commonly used for image recognition.
```

---

## 6. Sequential Chains

A **Sequential Chain** executes multiple chains one after another.

Example:
```text
Topic
 ↓
Generate Explanation
 ↓
Generate Summary
 ↓
Generate Questions
 ↓
Generate Answers
```

Let's say:

**Chain 1:**
```text
Topic → Explanation
```
Output: `"Convolutional Neural Networks are..."`

**Chain 2:**
```text
Explanation → Summary
```
Output: `"CNNs are neural networks mainly used for..."`

**Chain 3:**
```text
Summary → Questions
```
Output:
```text
1. What is CNN?
2. What is convolution?
3. What is pooling?
```

The output flows through the pipeline.

---

## 7. Real-World Example — YouTube Script Generator

Imagine you're building an AI tool that generates YouTube scripts.

Input: `Topic = "Artificial Intelligence"`

Chain:
```text
             Topic
               ↓
        Generate Introduction
               ↓
        Generate Main Content
               ↓
        Generate Examples
               ↓
        Generate Conclusion
               ↓
          Final Script
```

Each stage contributes to the final result.

---

## 8. Chain vs Agent

This is **extremely important for your syllabus**.

### Chain
The developer defines the workflow.
```text
Input
 ↓
Step A
 ↓
Step B
 ↓
Step C
```

### Agent
The AI decides what action should happen next.
```text
              User
                ↓
              Agent
             /  |  \
            /   |   \
       Search  Tool  Database
```

### Key difference

| Feature | Chain | Agent |
| :--- | :--- | :--- |
| **Workflow** | Predefined workflow | Dynamic workflow |
| **Control** | Developer controls sequence | LLM can decide actions |
| **Predictability** | More predictable | More flexible |
| **Best for** | Good for fixed tasks | Good for open-ended tasks |

### Memory trick:
> **Chain = "Do these steps."**
> **Agent = "Figure out which steps to do."**

---

## 9. Chain with External Tools

Chains aren't limited to LLM calls.

For example:
> "Calculate the total price including GST."

A workflow could be:
```text
User Input
    ↓
Extract Price
    ↓
Calculator Tool
    ↓
Calculate GST
    ↓
Format Result
    ↓
Final Answer
```

So chains can combine:
* LLMs
* APIs
* Python functions
* Databases
* Retrievers
* Tools
* Parsers

---

## 10. Modern LangChain Concept: Runnable Pipelines

Modern LangChain commonly uses **Runnable-based composition** to connect components.

Conceptually:
```text
Prompt
  ↓
Model
  ↓
Parser
```

The components are connected so the output flows from one to the next.

The important idea for your exam is:
> **LangChain allows components to be composed into reusable processing pipelines.**

You don't need to memorize every API method yet. We'll focus on the architecture first.

---

## 11. Worked Example

Suppose we want:
> **Input → Translate → Summarize**

Input:
> `"Artificial intelligence is changing the way software applications are developed."`

### Step 1 — Translation
```text
English
  ↓
Translation Model
  ↓
Translated Text
```

### Step 2 — Summary
```text
Translated Text
       ↓
Summary Prompt
       ↓
LLM
       ↓
Short Summary
```

Complete chain:
```text
                Input
                  ↓
          Translation Chain
                  ↓
          Translated Text
                  ↓
           Summary Chain
                  ↓
             Final Output
```

The second step depends on the first step's output.
That's the core idea of a chain.

---

## 12. Advantages of Chains

1. **Simple workflow management:** Complex tasks can be broken into smaller steps.
2. **Reusability:** A chain can be reused with different inputs.
3. **Modularity:** Individual components can be changed independently.
4. **Automation:** Multiple operations can execute automatically.
5. **Integration:** Chains can connect models, tools, APIs, databases and retrieval systems.
6. **Easier debugging:** You can inspect each stage separately.

---

## 13. Limitations of Chains

Chains aren't magic.

### Fixed workflow
If the task changes significantly, the predefined chain may not work well.

### Limited decision-making
A normal chain doesn't independently decide which operation is appropriate.

### Error propagation
If one step produces bad output:
```text
Step 1 ❌
   ↓
Step 2 ❌
   ↓
Step 3 ❌
```
An error can propagate through the pipeline.

### Complex workflows
Highly dynamic tasks may be better handled using **agents**.

---

## 14. Exam-Ready Definition

> **A chain in LangChain is a sequence of interconnected operations in which the output of one component is passed to the next component to accomplish a specific task. Chains can combine prompts, language models, output parsers, retrievers, tools and other components to create automated and reusable workflows.**

---

## 📝 Quick Revision

Remember this:

```text
CHAIN
  │
  ├── Multiple steps
  ├── Defined workflow
  ├── Output → next input
  ├── Reusable
  ├── Automates tasks
  └── Can connect LLMs + tools + APIs + retrieval
```

### Most important points
* **Chain = sequence of operations**
* Output of one step can become input to another.
* Chains are generally **predefined**.
* Sequential chains execute multiple stages.
* Chains are useful for **structured, predictable workflows**.
* Agents are better when the system needs **dynamic decision-making**.

---

## 🧠 Active Learning

### Conceptual
**Q1.** What is a Chain in LangChain?
**Q2.** Why is a chain generally more predictable than an agent?
**Q3.** What happens if an early step in a chain produces incorrect output?

### Practical
Design a chain for this task:
> **User enters a topic → AI generates an explanation → generates a 3-line summary → generates 3 MCQs.**

Write the steps in order, like:
```text
Input
 ↓
 ?
 ↓
 ?
 ↓
 ?
```

> *Reply **NEXT** after you're comfortable, or answer the questions if you want to test yourself.*
