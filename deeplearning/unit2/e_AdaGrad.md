# Topic 5: AdaGrad (Adaptive Gradient)

> **Exam Importance:** ⭐⭐⭐⭐☆ (Frequently Asked)

AdaGrad was the **first popular optimizer that automatically adjusts the learning rate** for each parameter.

Until now:

* Gradient Descent → Fixed learning rate
* Momentum → Fixed learning rate + memory
* NAG → Fixed learning rate + memory + look-ahead

**AdaGrad introduces a new idea:** **Adaptive Learning Rate**.

---

# ELI5 Explanation

Imagine two students learning mathematics.

* **Student A** makes many mistakes.
* **Student B** makes very few mistakes.

Should the teacher give both students the **same amount of correction**?

No.

The teacher gives **more attention** to the weaker student and **less attention** to the stronger one.

AdaGrad works similarly—it gives **different learning rates to different weights**.

---

# Real-World Intuition

Suppose you're learning to play the guitar.

* You're already good at chords, so you only need small improvements.
* You're weak at fingerpicking, so you need larger improvements.

AdaGrad automatically adjusts how much each skill (weight) should change.

---

# Why Do We Need AdaGrad?

In Gradient Descent:

```text
Learning Rate = 0.01
```

Every weight uses the **same learning rate**.

Example:

```text
Weight 1 → 0.01
Weight 2 → 0.01
Weight 3 → 0.01
```

But not all weights learn at the same speed.

Some need **larger updates**, others need **smaller updates**.

AdaGrad solves this problem.

---

# Core Idea

AdaGrad keeps track of the **sum of the squares of past gradients**.

If a parameter has received **large gradients repeatedly**, AdaGrad **reduces its learning rate**.

If a parameter has received **small gradients**, its learning rate stays relatively larger.

---

# Formula

### Step 1: Accumulate Squared Gradients

[
G_t = G_{t-1} + g_t^2
]

Where:

* (G_t) = accumulated squared gradients
* (g_t) = current gradient

---

### Step 2: Update the Weight

[
W = W - \frac{\eta}{\sqrt{G_t + \epsilon}} \times g_t
]

Where:

| Symbol     | Meaning                                                 |
| ---------- | ------------------------------------------------------- |
| (\eta)     | Initial learning rate                                   |
| (G_t)      | Sum of squared gradients                                |
| (\epsilon) | Small value (e.g., (10^{-8})) to avoid division by zero |
| (g_t)      | Current gradient                                        |

---

## Must Remember

AdaGrad **decreases the effective learning rate automatically** as training progresses.

---

# Step-by-Step Worked Example

Suppose:

* Weight = **8**
* Learning rate = **0.1**
* Gradient = **2**
* Previous accumulated gradient = **0**

### Step 1

Accumulate squared gradients:

[
G = 0 + 2^2 = 4
]

---

### Step 2

Compute the adjusted learning rate:

[
\frac{0.1}{\sqrt{4}}
====================

# \frac{0.1}{2}

0.05
]

---

### Step 3

Update the weight:

[
W = 8 - 0.05 \times 2
= 8 - 0.1
= 7.9
]

Notice that the learning rate became **0.05 instead of 0.1** because the optimizer has seen large gradients.

---

# Visual Idea

### Gradient Descent

```text
Learning Rate

0.1
0.1
0.1
0.1
0.1
```

Constant throughout training.

---

### AdaGrad

```text
Learning Rate

0.1
0.08
0.06
0.04
0.02
```

The learning rate gradually decreases.

---

# Advantages

* Automatically adapts the learning rate.
* Good for sparse data (e.g., NLP, text processing).
* No need to manually tune the learning rate as frequently.

---

# Disadvantages

* Learning rate keeps shrinking.
* Eventually, updates become extremely small.
* Training may stop too early before reaching the best solution.

This limitation led to newer optimizers like **RMSProp** and **Adam**, which solve this issue.

---

# Gradient Descent vs AdaGrad

| Feature                               | Gradient Descent | AdaGrad  |
| ------------------------------------- | ---------------- | -------- |
| Learning rate                         | Fixed            | Adaptive |
| Memory of past gradients              | ❌                | ✅        |
| Good for sparse data                  | ❌                | ✅        |
| Learning rate changes during training | ❌                | ✅        |
| Can become too small                  | ❌                | ✅        |

---

# Exam/Interview Must-Remember Points

* AdaGrad = **Adaptive Gradient Algorithm**.
* Each parameter gets its **own learning rate**.
* Uses the **sum of squared gradients**.
* Learning rate decreases over time.
* Performs well for sparse datasets.
* Main drawback: learning rate may become too small.

---

# Quick Revision

* AdaGrad automatically adjusts the learning rate.
* Frequently updated weights receive smaller future updates.
* Uses accumulated squared gradients.
* Excellent for sparse features.
* Main weakness: continuously shrinking learning rate.

---

# Connection So Far

```text
Gradient Descent
        ↓
SGD / Mini-Batch GD
        ↓
Momentum
        ↓
NAG
        ↓
AdaGrad
        ↓
Next: RMSProp (fixes AdaGrad's shrinking learning rate problem)
```

Notice the evolution:

* **GD** → Fixed learning rate.
* **Momentum/NAG** → Better movement.
* **AdaGrad** → Smarter learning rates.

---

# Active Learning

### Conceptual Questions

1. What is the main idea behind AdaGrad?
2. Why is AdaGrad often effective for sparse datasets?
3. What is AdaGrad's biggest limitation?

### Practical Question

Given:

* Initial learning rate = **0.2**
* Gradient = **4**
* Previous accumulated squared gradients = **9**
* Weight = **10**
* Assume (\epsilon) is negligible.

Calculate:

1. The new accumulated squared gradients.
2. The adjusted learning rate.
3. The updated weight.

Reply with your answers, and we'll continue to **Topic 6: RMSProp**, which fixes AdaGrad's biggest weakness.
