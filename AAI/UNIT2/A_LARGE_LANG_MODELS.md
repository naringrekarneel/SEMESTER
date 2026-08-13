# AGENTIC AI — Learning Roadmap

We’ll go from **LLM fundamentals → prompting → reasoning → agents → tools → memory → RAG → self-correction**.

### Learning sequence

| #  | Topic                                        | What you’ll learn                                               |
| -- | -------------------------------------------- | --------------------------------------------------------------- |
| 1  | **Overview of Large Language Models (LLMs)** | What LLMs are, architecture, training, inference, tokens        |
| 2  | **Prompt Engineering**                       | How to design effective prompts                                 |
| 3  | **Prompt Engineering Techniques**            | Zero-shot, few-shot, role prompting, structured prompting, etc. |
| 4  | **Chain-of-Thought Reasoning**               | How LLMs handle multi-step reasoning                            |
| 5  | **ReAct Paradigm**                           | Combining **Reason + Act** to build agents                      |
| 6  | **Tool Usage & Function Calling**            | How agents interact with external tools/APIs                    |
| 7  | **Memory in LLMs**                           | Short-term, long-term memory and vector databases               |
| 8  | **Retrieval-Augmented Generation (RAG)**     | Connecting LLMs to external knowledge                           |
| 9  | **Self-Reflection & Self-Correction**        | Agents checking and improving their own outputs                 |
| 10 | **Agentic AI Integration**                   | Connect everything into a complete agent architecture           |

---

# Topic 1: Overview of Large Language Models (LLMs)

## 1. ELI5 — What is an LLM?

Imagine you have a super-powered autocomplete.

You type:

> "The capital of France is..."

The model predicts:

> "Paris"

But modern LLMs can do much more than autocomplete:

* answer questions
* summarize documents
* write code
* translate languages
* analyze information
* generate plans
* interact with tools
* reason through problems

An **LLM (Large Language Model)** is basically a neural network trained on huge amounts of text to learn patterns in language.

The key idea:

> **Given the text so far, predict what should come next.**

For example:

> "Python is a programming..."

The model might predict:

> "language"

Then:

> "Python is a programming language..."

Then perhaps:

> "used"

And so on.

By repeatedly predicting tokens, the model generates an entire response.

---

# 2. What does "Large" mean?

The word **Large** generally refers to the enormous scale of the model and its training.

Three things are particularly important:

### 1. Large datasets

Models are trained on huge collections of text and other data.

Examples include:

* books
* websites
* articles
* documentation
* code
* conversations

### 2. Large number of parameters

Parameters are learned numerical values inside the neural network.

Think of them as the model's learned internal "knobs."

A model may contain billions of parameters.

### 3. Large computational requirements

Training these models requires enormous computational resources, typically involving many GPUs/accelerators.

---

# 3. How does an LLM actually work?

At a high level:

```text
User Input
    ↓
Tokenization
    ↓
Tokens
    ↓
Embeddings
    ↓
Transformer
    ↓
Next-token prediction
    ↓
Output tokens
    ↓
Generated text
```

Let's understand each step.

---

## Step 1: Input

Suppose you give the model:

> "I love Python"

The computer doesn't directly understand English sentences.

It needs to convert the text into numerical representations.

---

## Step 2: Tokenization

The text is broken into **tokens**.

A token isn't necessarily one complete word.

For example:

```text
"I love Python"
```

might become something conceptually similar to:

```text
["I", "love", "Python"]
```

But real tokenizers can split words into smaller pieces.

For example:

```text
"unbelievable"
```

could be represented as multiple tokens.

### Important

**Token ≠ word**

A token can be:

* a whole word
* part of a word
* punctuation
* whitespace-related text

---

# 4. Embeddings

Tokens are converted into vectors.

For example:

```text
"cat"
   ↓
[0.21, -0.45, 0.73, ...]
```

These vectors are called **embeddings**.

They allow the neural network to work with numerical representations of language.

The important intuition:

> Words/tokens with related meanings tend to have related representations.

For example, concepts such as:

```text
king
queen
man
woman
```

can have meaningful relationships in the learned representation space.

---

# 5. The Transformer

This is the BIG one.

Modern LLMs are primarily based on the **Transformer architecture**.

The Transformer was introduced in the famous 2017 paper:

> **"Attention Is All You Need"**

The most important mechanism is:

## Self-Attention

Self-attention allows the model to determine which other tokens are important when processing a particular token.

Consider:

> "The animal didn't cross the road because **it** was tired."

What does **it** refer to?

The model needs to understand the relationship between:

```text
animal ← it
```

Self-attention helps the model determine which parts of the context are relevant.

---

# 6. Attention — simple intuition

Imagine you're reading:

> "Rahul went to the restaurant because he was hungry."

When interpreting **"he"**, you naturally pay attention to **"Rahul"**.

You don't give equal importance to every word.

Conceptually:

```text
Rahul ───────────► he
        HIGH attention
```

while words like:

```text
the
to
because
```

may be less relevant to resolving "he".

That's the basic intuition behind attention.

---

# 7. Transformer Architecture

A simplified LLM pipeline looks like:

```text
                Input
                  ↓
             Tokenization
                  ↓
              Embedding
                  ↓
        ┌───────────────────┐
        │ Transformer Block  │
        │                   │
        │ Self-Attention    │
        │       ↓           │
        │ Feed Forward      │
        │       ↓           │
        │ Normalization     │
        └───────────────────┘
                  ↓
             Repeat many
                times
                  ↓
          Output probabilities
                  ↓
           Next-token choice
```

A real architecture is much more complex, but this is the structure you should remember for exams.

---

# 8. How does an LLM generate text?

Suppose we ask:

> **"What is Python?"**

The model doesn't magically retrieve a complete sentence from a database.

It generates tokens sequentially.

Conceptually:

```text
What is Python?
       ↓
"Python"
       ↓
"Python is"
       ↓
"Python is a"
       ↓
"Python is a programming"
       ↓
"Python is a programming language"
```

At every step, the model calculates probabilities for possible next tokens.

For example:

```text
Next token probabilities:

language     0.72
tool         0.10
snake        0.08
framework    0.04
...
```

The model then selects a token according to its decoding strategy.

---

# 9. The key mathematical idea

At its core, an autoregressive LLM models:

$$
P(x_1,x_2,\ldots,x_n)
=====================

\prod_{t=1}^{n} P(x_t \mid x_1,\ldots,x_{t-1})
$$

In simpler words:

> The probability of the whole sequence is built by predicting each token based on the tokens that came before it.

For example:

```text
I → love → Python
```

means approximately:

$$
P(\text{"I love Python"})
=========================

P(\text{"I"})
\times
P(\text{"love"}|\text{"I"})
\times
P(\text{"Python"}|\text{"I love"})
$$

### MUST REMEMBER

**LLMs generate text by repeatedly predicting the next token based on previous context.**

---

# 10. Training an LLM

The model initially doesn't know language.

It is trained on enormous amounts of data.

A simplified training process:

```text
Training text
     ↓
Tokenization
     ↓
Input tokens
     ↓
Transformer
     ↓
Predict next token
     ↓
Compare prediction with actual token
     ↓
Calculate loss
     ↓
Backpropagation
     ↓
Update parameters
     ↓
Repeat billions/trillions of times
```

---

## Example

Training sentence:

> "The cat is sleeping."

The model might receive:

```text
Input:
The cat is

Expected:
sleeping
```

Suppose it predicts:

```text
running
```

That's wrong.

The model calculates a **loss** measuring how wrong the prediction was.

Then optimization algorithms adjust the model's parameters.

After enormous numbers of examples, the model becomes much better at predicting language.

---

# 11. Pre-training vs Fine-tuning

This distinction is **very important for exams/interviews**.

### Pre-training

The model learns general patterns from huge datasets.

It learns things like:

* grammar
* facts
* language patterns
* coding patterns
* relationships between concepts

### Fine-tuning

The pretrained model is further trained for a particular purpose.

For example:

```text
Base LLM
   ↓
Fine-tuning
   ↓
Customer-support model
```

or:

```text
Base LLM
   ↓
Instruction tuning
   ↓
Better instruction-following assistant
```

---

# 12. LLM vs Traditional Program

| Traditional Program               | LLM                                       |
| --------------------------------- | ----------------------------------------- |
| Explicit rules                    | Learned patterns                          |
| Programmer defines logic          | Model learns from data                    |
| Usually deterministic             | Often probabilistic                       |
| Input → predefined logic → output | Input → learned model → generated output  |
| Easy to trace exact rules         | Internal reasoning is harder to interpret |

Example:

Traditional:

```python
if temperature > 30:
    print("Hot")
```

LLM:

> "Is 35°C hot?"

The LLM generates an answer based on learned representations and context.

---

# 13. LLM vs Search Engine

This distinction becomes extremely important when we reach **RAG**.

### Search engine

Usually:

```text
Query
 ↓
Search index
 ↓
Relevant documents
 ↓
Results
```

### LLM

```text
Prompt
 ↓
Neural network
 ↓
Token probabilities
 ↓
Generated response
```

An LLM may know information from its training, but that doesn't automatically mean it has access to **current or private information**.

That's one reason we need techniques such as:

> **RAG + tools + memory**

And that's where Agentic AI starts getting interesting.

---

# 14. Why LLMs are the "brain" of Agentic AI

An ordinary LLM:

```text
User
 ↓
LLM
 ↓
Answer
```

An agentic system goes further:

```text
              ┌─────────────┐
              │     LLM     │
              │   "Brain"   │
              └──────┬──────┘
                     ↓
        ┌────────────┼────────────┐
        ↓            ↓            ↓
     Tools         Memory        RAG
        ↓            ↓            ↓
      APIs       Past info    Documents
        └────────────┼────────────┘
                     ↓
                  Action
                     ↓
                   Result
```

The LLM decides:

> "What should I do next?"

This is the foundation of **agentic behavior**.

We'll later see how **ReAct** formalizes this:

```text
Reason → Act → Observe → Reason → Act → ...
```

---

# 15. Worked Example — LLM answering a question

User:

> "Explain photosynthesis in simple terms."

### Step 1 — Tokenize

```text
Explain | photosynthesis | in | simple | terms
```

### Step 2 — Convert tokens to representations

```text
Tokens
  ↓
Vectors
```

### Step 3 — Transformer processes context

Self-attention determines relationships between the tokens.

### Step 4 — Predict next token

Possible output:

```text
"Photosynthesis"
```

Then:

```text
"Photosynthesis is"
```

Then:

```text
"Photosynthesis is the process"
```

And so on.

### Step 5 — Continue until completion

The model generates the answer token by token.

---

# 16. Why LLMs sometimes hallucinate

This is a **must-know concept for Agentic AI**.

An LLM's fundamental objective is essentially:

> Predict plausible next tokens.

It is **not inherently a truth verification engine**.

Therefore, it can generate something that sounds convincing but is incorrect.

Example:

> "Who invented X?"

The model might confidently provide a wrong name.

This is called a:

## Hallucination

Agentic AI tries to reduce this problem using:

* RAG
* external tools
* web search
* databases
* verification
* self-reflection
* self-correction

We'll encounter all of these later.

---

# 17. Core LLM Concepts You MUST Know

| Concept            | Meaning                                            |
| ------------------ | -------------------------------------------------- |
| **Token**          | Basic unit processed by the model                  |
| **Embedding**      | Numerical representation of tokens                 |
| **Transformer**    | Main neural architecture behind modern LLMs        |
| **Attention**      | Mechanism for determining contextual relationships |
| **Parameter**      | Learned numerical value in the model               |
| **Pre-training**   | Learning general language patterns                 |
| **Fine-tuning**    | Adapting a pretrained model                        |
| **Inference**      | Using a trained model to generate output           |
| **Context window** | Amount of context the model can process            |
| **Hallucination**  | Confident but incorrect generated information      |

---

# Quick Revision Sheet

### LLM in one line

> **An LLM is a neural network trained on large datasets to model and generate language, typically by predicting the next token.**

### Pipeline

```text
Text
 ↓
Tokens
 ↓
Embeddings
 ↓
Transformer
 ↓
Attention + Feed Forward
 ↓
Next-token probabilities
 ↓
Generated text
```

### Most important ideas

* **LLM ≠ database**
* **Token ≠ necessarily a word**
* **Transformer is the core architecture**
* **Attention captures relationships between tokens**
* **Training learns parameters**
* **Inference uses those learned parameters**
* **LLMs generate responses token-by-token**
* **LLMs can hallucinate**
* **Agentic AI uses LLMs as a decision-making component**
* **Tools/RAG/memory extend what an LLM can do**

---

# Exam/Interview Must-Remember

If asked **"What is an LLM?"**, hit these points:

1. Large neural network trained on massive datasets.
2. Primarily based on Transformer architecture.
3. Processes text as tokens.
4. Uses embeddings to represent tokens numerically.
5. Uses self-attention to understand contextual relationships.
6. Generates output through next-token prediction.
7. Can perform tasks such as generation, summarization, translation and coding.
8. Can suffer from hallucination and knowledge limitations.

---

# Active Learning — Don't Peek 😈

### Conceptual Q1

What is the difference between a **token** and a **word**?

### Conceptual Q2

Why is **self-attention** important in an LLM?

### Conceptual Q3

Why can an LLM produce a confident but incorrect answer?

### Practical Q4

Suppose an LLM receives:

> **"The dog chased the cat because it was scared."**

Which word does the model need to resolve the relationship for, and how could **self-attention** help it understand what "it" refers to?

Answer these four. **Then we'll move to Topic 2: Prompt Engineering.**
