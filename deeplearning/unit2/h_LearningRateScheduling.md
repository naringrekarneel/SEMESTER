# Topic 8: Learning Rate Scheduling

> **Exam Importance:** ⭐⭐⭐⭐⭐ (Very Frequently Asked)

Learning Rate Scheduling is a technique where the **learning rate changes automatically during training** instead of remaining fixed.

---

# ELI5 Explanation

Imagine you're learning to ride a bicycle.

### In the Beginning

You make big adjustments because you're still learning.

### After Practice

You make only small adjustments to improve.

Deep learning works the same way.

* Early training → Large learning rate (big steps)
* Later training → Small learning rate (fine-tuning)

This gradual change is called **Learning Rate Scheduling**.

---

# Real-World Intuition

Imagine searching for a lost ring.

### At First

You walk quickly around the room to search large areas.

### Later

When you know the ring is nearby, you search carefully and slowly.

Large steps help find the area.

Small steps help find the exact location.

---

# Why Do We Need Learning Rate Scheduling?

Suppose the learning rate is always:

[
\eta = 0.1
]

Near the minimum:

```text
      Minimum

      ●
     ↗ ↘
    ↗   ↘
```

The optimizer keeps jumping around the minimum.

It struggles to settle.

Reducing the learning rate over time allows the optimizer to make finer adjustments and converge more smoothly.

---

# Core Idea

Instead of using a fixed learning rate:

```text
0.1
0.1
0.1
0.1
0.1
```

We gradually decrease it:

```text
0.1
0.05
0.02
0.01
0.005
```

Large steps at the beginning.

Small steps near the end.

---

# Types of Learning Rate Scheduling

---

## 1. Step Decay ⭐⭐⭐⭐⭐

Reduce the learning rate after a fixed number of epochs.

Example:

| Epoch | Learning Rate |
| ----- | ------------- |
| 1–10  | 0.1           |
| 11–20 | 0.01          |
| 21–30 | 0.001         |

Visual:

```text
0.1 ───────────
               │
0.01───────────
               │
0.001──────────
```

Very common in exams.

---

## 2. Exponential Decay ⭐⭐⭐⭐

Learning rate decreases continuously.

Formula:

[
\eta_t=\eta_0e^{-kt}
]

Where:

* (\eta_0) = initial learning rate
* (k) = decay constant
* (t) = epoch or iteration

---

## 3. Time-Based Decay ⭐⭐⭐

Formula:

[
\eta_t=\frac{\eta_0}{1+kt}
]

The learning rate decreases gradually with time.

---

## 4. Cosine Annealing ⭐⭐⭐⭐

The learning rate follows a cosine curve.

* Starts high.
* Decreases smoothly.
* Sometimes restarts to escape local minima (Cosine Annealing with Warm Restarts).

Popular in modern deep learning.

---

## 5. Reduce on Plateau ⭐⭐⭐⭐⭐

This is one of the most practical methods.

Rule:

If the **validation loss stops improving** for several epochs:

➡️ Automatically reduce the learning rate.

Example:

```text
Epoch 10

Validation Loss

0.21
0.20
0.20
0.20
0.20

↓

Reduce LR
```

Used in TensorFlow and PyTorch.

---

# Worked Example

Suppose:

* Initial learning rate = **0.1**
* Step Decay: divide by **10 every 5 epochs**

| Epoch | Learning Rate |
| ----- | ------------- |
| 1     | 0.1           |
| 5     | 0.1           |
| 6     | 0.01          |
| 10    | 0.01          |
| 11    | 0.001         |

This allows:

* Fast learning initially.
* Fine-tuning later.

---

# Visual Comparison

### Fixed Learning Rate

```text
0.1
0.1
0.1
0.1
0.1
```

Never changes.

---

### Scheduled Learning Rate

```text
0.1

↓

0.05

↓

0.02

↓

0.01
```

Improves convergence.

---

# Advantages

* Faster convergence.
* Better final accuracy.
* Reduces oscillations near the minimum.
* Helps avoid overshooting.
* Often improves generalization.

---

# Disadvantages

* Requires selecting an appropriate schedule.
* Poor scheduling may slow learning.
* Adds one more hyperparameter to tune.

---

# Learning Rate vs Learning Rate Scheduling

| Learning Rate             | Learning Rate Scheduling |
| ------------------------- | ------------------------ |
| Fixed throughout training | Changes during training  |
| Simple                    | Smarter                  |
| Can overshoot             | Better convergence       |
| May not adapt             | Adapts over time         |

---

# Exam/Interview Must-Remember Points

* Learning Rate Scheduling changes the learning rate during training.
* Large learning rate at the start.
* Small learning rate near convergence.
* Common schedules:

  * Step Decay
  * Exponential Decay
  * Time-Based Decay
  * Cosine Annealing
  * Reduce on Plateau
* Reduce on Plateau is widely used in practice.

---

# Memory Trick 🧠

Imagine driving a car:

```text
Highway

🚗💨

↓

Near destination

🚗
```

Drive fast on the highway.

Slow down when parking.

That's exactly what learning rate scheduling does.

---

# Quick Revision

* Learning Rate Scheduling automatically changes the learning rate.
* Start with larger steps, finish with smaller steps.
* Improves convergence and stability.
* Step Decay and Reduce on Plateau are the most commonly asked methods.
* Frequently used alongside Adam and SGD.

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
Adam
        ↓
Learning Rate Scheduling
        ↓
Next: Weight Initialization (Xavier & He Initialization)
```

---

# Active Learning

### Conceptual Questions

1. Why do we usually reduce the learning rate during training?
2. What happens if the learning rate remains very high near the minimum?
3. Which learning rate scheduling method reduces the learning rate only when the validation loss stops improving?

### Practical Question

A model starts training with a learning rate of **0.1** using **Step Decay**, where the learning rate is divided by **10 every 10 epochs**.

Calculate the learning rate at:

* Epoch **1**
* Epoch **10**
* Epoch **11**
* Epoch **21**

Reply with your answers, and then we'll continue to **Topic 9: Weight Initialization (Xavier & He Initialization)**.
