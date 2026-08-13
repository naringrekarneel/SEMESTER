# Topic 2: Agent vs Model vs Workflow

This is one of the **most frequently asked interview and exam topics** because many people confuse these three terms.

---

# ELI5 Explanation 🧒

Imagine you're hungry.

There are **three different ways** to solve the problem.

### 🧠 Model

You ask someone:

> "Which restaurant has the best pizza?"

They simply **answer** your question.

They don't order the pizza.

➡️ This is a **Model**.

---

### 📋 Workflow

You follow a fixed checklist.

1. Open Zomato
2. Search Pizza
3. Pick first restaurant
4. Order

The same steps happen every time.

➡️ This is a **Workflow**.

---

### 🤖 Agent

You tell your smart assistant:

> "Get me the best pizza under ₹500."

The assistant:

* searches restaurants
* compares prices
* checks ratings
* chooses the best one
* places the order
* tells you when it's arriving

It decides what to do on its own.

➡️ This is an **Agent**.

---

# Formal Definitions (Exam)

### Model

A **Model** is an AI system that takes an input and produces an output based on learned patterns.

Examples:

* ChatGPT
* Image classifier
* Spam detector
* Language translation model

---

### Workflow

A **Workflow** is a predefined sequence of steps executed in a fixed order to complete a task.

Example:

```text
Receive Email
      ↓
Extract Data
      ↓
Save to Database
      ↓
Send Confirmation
```

No thinking.

No decision-making.

---

### Agent

An **Agent** is an autonomous system that observes the environment, reasons, plans, and performs actions to achieve a goal.

Unlike a workflow, an agent can change its plan based on new information.

---

# The Big Difference

Imagine you're planning a trip.

## Using a Model

```text
You:
Recommend a hotel.

Model:
Hotel ABC is good.
```

Only gives information.

---

## Using a Workflow

```text
Search hotels
↓
Sort by price
↓
Choose first one
↓
Book
```

Always follows the same path.

---

## Using an Agent

```text
Goal:
Book the best hotel.

↓

Search hotels

↓

Compare prices

↓

Read reviews

↓

Weather bad?

↓

Change destination

↓

Book hotel

↓

Send confirmation
```

The plan changes if needed.

---

# Comparison Table ⭐⭐⭐

| Feature         | Model                        | Workflow                 | Agent                      |
| --------------- | ---------------------------- | ------------------------ | -------------------------- |
| Purpose         | Generate prediction/response | Execute predefined steps | Achieve goals autonomously |
| Thinking        | Limited to inference         | None                     | Yes                        |
| Planning        | No                           | Fixed                    | Dynamic                    |
| Memory          | Usually temporary            | Usually none             | Can maintain memory        |
| Decision-making | Minimal                      | Rule-based               | Intelligent                |
| Tool usage      | Sometimes                    | Fixed                    | Dynamic                    |
| Adaptation      | Low                          | Very low                 | High                       |
| Autonomy        | No                           | Low                      | High                       |

**Exam Tip:** If asked to differentiate, this table can score full marks.

---

# Real-World Examples

## Example 1: Weather

### Model

```text
Input:
Tomorrow's weather?

↓

Output:
Rain expected.
```

---

### Workflow

```text
Read weather API
↓

Generate report
↓

Email report
```

Same every day.

---

### Agent

```text
Weather predicts rain
↓

Reason:
Umbrella needed

↓

Notify user

↓

Reschedule outdoor meeting

↓

Book indoor room
```

The agent **acts** based on the prediction.

---

## Example 2: Customer Support

### Model

Answers customer questions.

---

### Workflow

```text
Receive ticket
↓

Assign department
↓

Send acknowledgment
```

---

### Agent

```text
Understand complaint

↓

Search order history

↓

Issue refund

↓

Notify customer

↓

Close ticket
```

---

# Relationship Between Them

A common misconception is that these are competing ideas. In practice, they often work together.

```text
          AI Agent
             │
      ┌──────┴──────┐
      │             │
 Uses AI Models   Executes Workflows
```

An **agent** often uses **models** for intelligence and **workflows** for repetitive tasks.

---

# Worked Example

### Problem

User says:

> "Book the cheapest flight to Delhi."

### If Using Only a Model

```text
Suggest airlines.
```

Done.

---

### If Using Workflow

```text
Open website

↓

Search flights

↓

Book first result
```

No optimization.

---

### If Using an Agent

```text
Understand budget

↓

Compare airlines

↓

Check baggage fees

↓

Check timings

↓

Find discounts

↓

Book best option

↓

Email ticket

↓

Monitor for price drops
```

The agent actively works toward the goal.

---

# Why Are Agents Becoming Popular?

Traditional AI systems:

* answer questions
* make predictions

Modern AI agents can:

* use tools
* search the web
* write code
* book appointments
* automate tasks
* collaborate with other agents
* continuously improve based on feedback

This shift from **"answering"** to **"doing"** is what defines Agentic AI.

---

# Common Interview Questions

### Q1. Can an agent use a model?

✅ Yes.

Example:

* The **model** understands language.
* The **agent** decides what actions to take based on that understanding.

---

### Q2. Can an agent execute workflows?

✅ Yes.

Example:

An agent may trigger a predefined invoice approval workflow after deciding it's appropriate.

---

### Q3. Which is the smartest?

* Model → Intelligent at prediction.
* Workflow → Efficient at repetitive tasks.
* Agent → Intelligent at achieving goals by combining models, workflows, memory, planning, and actions.

---

# Must-Remember Points ⭐

* **Model = Thinks (predicts).**
* **Workflow = Follows fixed steps.**
* **Agent = Thinks, plans, decides, and acts.**
* Agents can use both models and workflows.
* Agents adapt to changing situations; workflows generally do not.

---

# Quick Revision

* **Model:** Input → Output (prediction or generation).
* **Workflow:** Fixed sequence of predefined steps.
* **Agent:** Goal-driven, autonomous system that reasons and performs actions.
* Agents are the most flexible because they can combine AI models, workflows, tools, and memory.

---

# Active Learning

### Conceptual Questions

1. What is the main difference between a **Model**, a **Workflow**, and an **Agent**?
2. Why is an **Agent** considered more flexible than a **Workflow**?
3. Explain how an **Agent** can use both **Models** and **Workflows** together.

### Practical Question

A company wants an AI system to:

* Read customer emails
* Detect the issue
* Check order history
* Decide whether to refund or replace the product
* Notify the customer

For each step, identify whether it is mainly performed by a **Model**, a **Workflow**, or an **Agent**, and explain why.

Reply with your answers, or type **"next"** to continue to **Topic 3: Characteristics of Agentic Systems (Autonomy, Memory, Planning, Feedback)**.
