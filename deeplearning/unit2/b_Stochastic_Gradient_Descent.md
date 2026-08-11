I think you meant **"next"**.

# Topic 2: Stochastic Gradient Descent (SGD) & Mini-Batch Gradient Descent

> **Exam Importance:** ⭐⭐⭐⭐⭐ (Very Frequently Asked)

This topic explains **how Gradient Descent uses training data** to update the model. Understanding the difference between **Batch GD**, **SGD**, and **Mini-Batch GD** is one of the most common exam and interview questions.

---

# ELI5 Explanation

Imagine your teacher gives you **1,000 math problems** to improve.

There are three ways to learn:

### 1. Batch Gradient Descent 📚

Solve **all 1,000 problems**, then ask the teacher how you did and improve once.

* Very accurate feedback
* Very slow

---

### 2. Stochastic Gradient Descent (SGD) 🏃

Solve **one problem**, get feedback immediately, improve immediately.

* Very fast
* Feedback is noisy

---

### 3. Mini-Batch Gradient Descent 📦

Solve **50 problems**, get feedback, improve, then repeat.

* Faster than Batch GD
* More stable than SGD
* Most commonly used in deep learning

---

# Real-World Intuition

Imagine climbing a mountain.

### Batch GD

You walk the **entire mountain**, then decide where to step next.

* Accurate
* Slow

---

### SGD

You decide after **every single step**.

* Fast
* Can zig-zag

---

### Mini-Batch GD

You walk a **small distance**, then decide.

* Balanced
* Efficient

---

# The Problem with Batch Gradient Descent

Suppose you have:

* 10 million images
* 1 training iteration

Batch GD must process **all 10 million images** before updating the weights.

This requires:

* High memory
* Long computation time
* Slow learning

---

# 1. Batch Gradient Descent

### How it works

1. Take the entire dataset.
2. Compute the average loss.
3. Compute gradients.
4. Update weights once.

### Formula

[
W = W - \eta \nabla J(W)
]

Here, the gradient is computed using **all training examples**.

---

### Example

Dataset:

```text
1000 images
```

Process:

```text
Image 1
Image 2
...
Image 1000

↓

Calculate gradient

↓

Update weights once
```

Only **1 update** after seeing all samples.

---

## Advantages

* Stable updates
* Smooth convergence
* Accurate gradient

---

## Disadvantages

* Very slow
* High memory usage
* Not suitable for huge datasets

---

# 2. Stochastic Gradient Descent (SGD)

"Stochastic" means **random**.

Instead of using the entire dataset, SGD updates the weights using **one training sample at a time**.

---

### Algorithm

```text
Take 1 sample

↓

Forward pass

↓

Loss

↓

Gradient

↓

Update weights

↓

Next sample
```

---

### Example

Suppose there are five training samples:

```text
A
B
C
D
E
```

Weight updates happen like this:

```text
A → Update

B → Update

C → Update

D → Update

E → Update
```

There are **5 updates** in one epoch.

---

### Why is SGD Faster?

It doesn't wait for the whole dataset.

It learns continuously.

---

### But...

Because it learns from just one sample:

* Some updates are good.
* Some are noisy.
* Loss may fluctuate.

Visual idea:

```text
Loss

|
|\
| \
|  \__
|     \_
|   _/
| _/
|/
+------------------>

Iterations
```

The loss generally decreases but with zig-zag movements.

---

## Advantages

* Fast updates
* Less memory
* Works well for large datasets
* Can escape shallow local minima because of noisy updates

---

## Disadvantages

* Noisy convergence
* Less stable
* May overshoot the minimum

---

# 3. Mini-Batch Gradient Descent

This combines the strengths of Batch GD and SGD.

Instead of:

* All samples
* One sample

we use a **small batch**.

Common batch sizes:

* 16
* 32
* 64
* 128
* 256

---

### Example

Dataset:

```text
1000 images
```

Batch size:

```text
100
```

Processing:

```text
Images 1–100
↓

Update

Images 101–200
↓

Update

...

Images 901–1000
↓

Update
```

There are **10 updates** in one epoch.

---

# Why Mini-Batch is the Most Popular

It provides:

* Faster training than Batch GD
* More stable updates than SGD
* Better GPU utilization
* Good balance of speed and accuracy

This is why almost all modern deep learning frameworks (TensorFlow, PyTorch, Keras) use Mini-Batch Gradient Descent by default.

---

# Comparison Table

| Feature              | Batch GD       | SGD        | Mini-Batch GD  |
| -------------------- | -------------- | ---------- | -------------- |
| Data used per update | Entire dataset | One sample | Small batch    |
| Speed                | Slow           | Fast       | Fast           |
| Memory usage         | High           | Low        | Moderate       |
| Stability            | High           | Low        | Medium to High |
| Noisy updates        | No             | Yes        | Slight         |
| Most commonly used   | Rarely         | Sometimes  | Yes            |

---

# Worked Example

Dataset size = **1,000 samples**

Batch size = **100**

### Batch GD

* Uses 1,000 samples
* Updates = **1**

---

### SGD

* Uses 1 sample each time
* Updates = **1,000**

---

### Mini-Batch GD

* Uses 100 samples per batch
* Number of batches = 1000 ÷ 100 = **10**
* Updates = **10**

---

# Exam/Interview Must-Remember Points

* **Batch GD:** Uses the entire dataset before each update.
* **SGD:** Updates weights after every training sample.
* **Mini-Batch GD:** Updates weights after a small group of samples.
* Mini-Batch GD is the **most widely used** optimization approach in deep learning.
* Common batch sizes are **32, 64, and 128**.

---

# Quick Revision

* Batch GD = Entire dataset → 1 update.
* SGD = 1 sample → Many updates.
* Mini-Batch GD = Small batch → Balanced approach.
* SGD is faster but noisier.
* Mini-Batch GD offers the best trade-off and is used in practice.

---

# Active Learning

### Conceptual Questions

1. Why is Mini-Batch Gradient Descent preferred over Batch GD in deep learning?
2. Why does SGD produce noisier updates than Batch GD?
3. Which method typically requires the most memory: Batch GD, SGD, or Mini-Batch GD?

### Practical Question

A dataset contains **2,400 training samples**, and the **mini-batch size is 200**.

* How many mini-batches are created?
* How many weight updates occur in **one epoch**?

Reply with your answers, and then we'll move to **Topic 3: Momentum-Based Gradient Descent**.
