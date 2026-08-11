# Topic 12: Early Stopping

> **Exam Importance:** ⭐⭐⭐⭐☆ — Very useful for both exams and practical deep learning

Early Stopping is a simple regularization technique that prevents **overfitting by stopping training at the right time**.

---

# ELI5 Explanation

Imagine you're preparing for an exam.

At first, studying more makes you better.

```text
Study more → Better performance
```

But after a certain point, you start memorizing irrelevant details.

```text
Too much studying → Worse performance on new questions
```

So you stop studying when your performance on **new questions** starts getting worse.

That's **Early Stopping**.

---

# Real-World Intuition

Suppose you're training a neural network.

During training:

```text
Training Loss ↓ ↓ ↓ ↓ ↓

Validation Loss ↓ ↓ ↓
                   ↑
                   ↑
                starts increasing
```

The training loss continues decreasing.

But the validation loss starts increasing.

That's the classic sign of **overfitting**.

So we stop training.

---

# Why Does This Work?

Remember:

> **Training performance ≠ Generalization performance**

A model can continue getting better on training data while becoming worse on unseen data.

Early Stopping says:

> "Don't train just because you can. Stop when the model stops getting better on unseen data."

---

# Training vs Validation Loss

Imagine:

| Epoch | Training Loss | Validation Loss |
| ----: | ------------: | --------------: |
|     1 |          0.80 |            0.85 |
|     2 |          0.60 |            0.65 |
|     3 |          0.45 |            0.50 |
|     4 |          0.35 |            0.40 |
|     5 |          0.28 |        **0.32** |
|     6 |          0.22 |            0.35 |
|     7 |          0.18 |            0.40 |

At epoch 5:

```text
Validation Loss = 0.32
```

That's the best result.

After epoch 5:

```text
Training Loss ↓
Validation Loss ↑
```

The model is beginning to overfit.

Therefore, we should stop around **epoch 5**.

---

# Basic Algorithm

```text
Start Training
      ↓
Train for one epoch
      ↓
Calculate validation loss
      ↓
Is validation loss improving?
      ↓
   Yes → Continue
      ↓
   No → Wait a little
      ↓
Still not improving?
      ↓
   STOP
```

---

# Patience

A very important concept is **patience**.

You usually don't stop immediately after one bad epoch.

Example:

```text
Patience = 3
```

Means:

> Allow up to 3 epochs without improvement before stopping.

---

## Example

Suppose validation loss:

```text
Epoch 1 → 0.50
Epoch 2 → 0.40
Epoch 3 → 0.32
Epoch 4 → 0.34
Epoch 5 → 0.36
Epoch 6 → 0.38
```

Best loss:

```text
0.32
```

If patience = 3:

```text
Epoch 4 → No improvement → 1
Epoch 5 → No improvement → 2
Epoch 6 → No improvement → 3
```

Training stops.

---

# Best Model vs Last Model

This is an important practical detail.

Suppose:

```text
Epoch 5 → Best validation loss
Epoch 6 → Worse
Epoch 7 → Worse
Epoch 8 → Worse
```

We don't necessarily want the model from epoch 8.

We want the model from **epoch 5**.

Therefore, Early Stopping is often combined with:

> **Model Checkpointing**

The best-performing model is saved during training.

---

# Early Stopping as Regularization

Early Stopping limits how much the network can learn from the training data.

Without Early Stopping:

```text
Training
   ↓
More learning
   ↓
More memorization
   ↓
Overfitting
```

With Early Stopping:

```text
Training
   ↓
Learning
   ↓
Best validation performance
   ↓
STOP
   ↓
Better generalization
```

---

# Worked Example

Suppose we train a neural network for 10 epochs.

Validation loss:

| Epoch | Validation Loss |
| ----: | --------------: |
|     1 |            0.90 |
|     2 |            0.70 |
|     3 |            0.55 |
|     4 |            0.42 |
|     5 |        **0.35** |
|     6 |            0.36 |
|     7 |            0.38 |
|     8 |            0.41 |
|     9 |            0.45 |
|    10 |            0.50 |

The lowest validation loss is:

[
\boxed{0.35}
]

at epoch **5**.

Therefore, the best model is from:

[
\boxed{\text{Epoch 5}}
]

Training beyond this point is causing overfitting.

---

# Advantages

* Very simple.
* Reduces overfitting.
* Saves training time.
* Prevents unnecessary computation.
* Requires no modification to the network architecture.

---

# Disadvantages

* Requires a validation dataset.
* Choosing patience can be tricky.
* If stopped too early, the model may underfit.
* The validation metric can fluctuate.

---

# Early Stopping vs L1/L2

| Feature                   | Early Stopping | L1/L2 |
| ------------------------- | -------------- | ----- |
| Prevents overfitting      | ✅              | ✅     |
| Changes weights directly  | ❌              | ✅     |
| Changes training duration | ✅              | ❌     |
| Requires validation data  | Usually ✅      | ❌     |
| Easy to implement         | ✅              | ✅     |

---

# Exam/Interview Must-Remember

### Early Stopping

> **Stop training when validation performance stops improving.**

Important terms:

* Training loss
* Validation loss
* Patience
* Best model
* Overfitting

---

# Memory Trick

Think:

> **"Training loss says keep going; validation loss says enough."**

That's Early Stopping.

---

# Quick Revision

* Early Stopping is a regularization technique.
* Monitor **validation performance** during training.
* Stop when validation performance stops improving.
* **Patience** allows a few bad epochs before stopping.
* Save the model with the best validation performance.
* Prevents overfitting and saves computation.

---

# Connection

So far:

```text
Bias-Variance
     ↓
L1/L2
     ↓
Early Stopping
     ↓
Next: Dataset Augmentation
```

We're gradually building a toolkit for reducing **overfitting**.

---

# Active Learning

### Conceptual Questions

1. Why do we monitor **validation loss** rather than only training loss?
2. What does the **patience** parameter mean?
3. What happens if we stop training too early?

### Practical Question

A model produces:

| Epoch | Training Loss | Validation Loss |
| ----: | ------------: | --------------: |
|     1 |          0.80 |            0.75 |
|     2 |          0.60 |            0.55 |
|     3 |          0.45 |            0.40 |
|     4 |          0.35 |        **0.30** |
|     5 |          0.25 |            0.32 |
|     6 |          0.18 |            0.37 |
|     7 |          0.12 |            0.45 |

At which epoch would you save the **best model**, and why?

Reply with your answer, and we'll move to **Topic 13: Dataset Augmentation**.
