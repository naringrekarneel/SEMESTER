# Topic 6: RMSProp (Root Mean Square Propagation)

> **Exam Importance:** ⭐⭐⭐⭐⭐ (Very Frequently Asked)

RMSProp was developed to **solve AdaGrad's biggest problem**—its learning rate keeps decreasing until training almost stops.

---

# ELI5 Explanation

Imagine you're riding a bicycle.

### AdaGrad 🚲

Every time you pedal, your bicycle permanently slows down.

Eventually, you're barely moving.

---

### RMSProp 🚴

Instead of remembering **every pedal forever**, you only remember the **recent pedals**.

So your speed stays balanced.

That's exactly what RMSProp does—it focuses on **recent gradients** instead of the entire history.

---

# Real-World Intuition

Suppose you're preparing for exams.

### AdaGrad

You remember every mistake from the beginning of the semester.

After a while, those old mistakes still influence your study plan, even though you've already improved.

---

### RMSProp

You mainly focus on the mistakes from the **last few days**, since they better reflect your current understanding.

This makes learning more effective.

---

# Why Do We Need RMSProp?

Recall AdaGrad:

[
G = G + g^2
]

The accumulated value (G) **keeps increasing forever**.

As (G) grows larger:

[
\frac{\eta}{\sqrt{G}}
]

becomes smaller and smaller.

Eventually:

* Learning rate ≈ 0
* Weight updates become tiny
* Training slows dramatically

RMSProp fixes this.

---

# Core Idea

Instead of storing **all past squared gradients**, RMSProp stores an **exponentially weighted moving average** of recent squared gradients.

Older gradients gradually lose importance.

Recent gradients matter more.

---

# Formula

### Step 1: Update Running Average

[
S_t = \beta S_{t-1} + (1-\beta)g_t^2
]

Where:

* (S_t) = running average of squared gradients
* (g_t) = current gradient
* (\beta) = decay rate (usually **0.9**)

---

### Step 2: Update Weight

[
W = W - \frac{\eta}{\sqrt{S_t+\epsilon}}g_t
]

---

## Must Remember

AdaGrad stores **all** gradients.

RMSProp stores only a **moving average of recent gradients**.

---

# Step-by-Step Worked Example

Suppose:

* Weight = **8**
* Learning rate = **0.1**
* Gradient = **2**
* Previous running average = **1**
* Decay rate = **0.9**

---

### Step 1

Update running average:

[
S = 0.9(1)+0.1(2^2)
]

[
=0.9+0.4
]

[
=1.3
]

---

### Step 2

Calculate adjusted learning rate

[
\frac{0.1}{\sqrt{1.3}}
]

[
\approx0.0877
]

---

### Step 3

Update weight

[
W=8-0.0877\times2
]

[
=8-0.1754
]

[
=7.8246
]

---

# Visual Comparison

### AdaGrad

```text
Learning Rate

0.10
0.08
0.05
0.03
0.01
0.005
0.001
```

Keeps decreasing forever.

---

### RMSProp

```text
Learning Rate

0.10
0.08
0.09
0.08
0.09
0.08
```

Stays relatively stable because only recent gradients influence it.

---

# Why "Root Mean Square"?

The update divides by

[
\sqrt{S_t}
]

* **Root** → Square root
* **Mean Square** → Average of squared gradients

Hence the name **Root Mean Square Propagation**.

---

# Advantages

* Solves AdaGrad's shrinking learning rate problem.
* Faster convergence.
* Stable updates.
* Works well for deep neural networks.
* Suitable for non-stationary problems.

---

# Disadvantages

* Requires choosing the decay rate ((\beta)).
* Still needs manual tuning of the initial learning rate.
* Often outperformed by Adam in practice.

---

# AdaGrad vs RMSProp

| Feature         | AdaGrad                | RMSProp          |
| --------------- | ---------------------- | ---------------- |
| Learning rate   | Continuously decreases | Remains adaptive |
| Memory          | Entire history         | Recent history   |
| Sparse data     | Excellent              | Good             |
| Long training   | Poor                   | Better           |
| Practical usage | Less common            | Very common      |

---

# Exam/Interview Must-Remember Points

* RMSProp was designed to overcome AdaGrad's main limitation.
* Uses an **exponential moving average** of squared gradients.
* Typical decay rate ((\beta)) = **0.9**.
* Keeps the learning rate adaptive but prevents it from shrinking too much.
* Frequently used in deep learning before Adam became dominant.

---

# Quick Revision

* RMSProp = Improved AdaGrad.
* Remembers **recent** gradients instead of all gradients.
* Prevents the learning rate from becoming extremely small.
* Uses an exponential moving average.
* Common decay rate: **0.9**.

---

# Connection So Far

```text
Gradient Descent
        ↓
SGD / Mini-Batch
        ↓
Momentum
        ↓
NAG
        ↓
AdaGrad
        ↓
RMSProp
        ↓
Next: Adam Optimizer (Momentum + RMSProp)
```

Think of it like this:

* **Momentum** → Remembers previous **updates**.
* **AdaGrad** → Adjusts learning rates using **all gradients**.
* **RMSProp** → Adjusts learning rates using **recent gradients**.
* **Adam** → Combines the strengths of **Momentum** and **RMSProp**.

---

# Active Learning

### Conceptual Questions

1. What limitation of AdaGrad does RMSProp solve?
2. Why does RMSProp use a moving average instead of storing all past gradients?
3. What is the typical value of the decay rate ((\beta)) in RMSProp?

### Practical Question

Given:

* Weight = **12**
* Learning rate = **0.1**
* Gradient = **3**
* Previous running average = **4**
* Decay rate = **0.9**

Calculate:

1. The new running average (S_t).
2. The adjusted learning rate (\frac{0.1}{\sqrt{S_t}}) (approximate).
3. The updated weight.

Reply with your answers, and we'll move to **Topic 7: Adam Optimizer**, the most widely used optimizer in modern deep learning.
