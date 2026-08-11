# Topic 11: L1 & L2 Regularization

> **Exam Importance:** ⭐⭐⭐⭐⭐ — Very frequently asked

Now we enter the **regularization** part of the syllabus.

The main goal is simple:

> **Prevent the neural network from overfitting the training data.**

---

# ELI5 Explanation

Imagine you're studying for an exam.

You could memorize every tiny detail from your textbook.

You'll perform amazingly on questions you've already seen—but maybe badly on new questions.

That's **overfitting**.

Regularization basically tells the neural network:

> "Don't make the model unnecessarily complicated."

It adds a **penalty for large weights**.

---

# Why Do We Need Regularization?

Suppose a model has weights:

```text
W1 = 0.2
W2 = 0.5
W3 = 15
W4 = -20
```

Those huge weights can make the model extremely sensitive to small changes in the input.

That can lead to **overfitting**.

Regularization encourages the model to use **smaller weights**.

---

# Basic Idea

Normally, we minimize:

[
Loss
]

With regularization, we minimize:

[
\boxed{Loss + Regularization\ Penalty}
]

So the model now has two goals:

1. Make predictions accurately.
2. Keep the weights under control.

---

# Two Important Types

There are two major regularization techniques:

### L1 Regularization

Uses:

[
\sum |W|
]

### L2 Regularization

Uses:

[
\sum W^2
]

The difference looks tiny mathematically, but it produces very different behavior.

---

# 1. L1 Regularization

L1 adds the **absolute value of weights** to the loss.

### Formula

[
\boxed{
L_{total}=L+\lambda\sum_i|W_i|
}
]

Where:

* (L) = original loss
* (W_i) = model weights
* (\lambda) = regularization strength

---

# What Does L1 Do?

L1 tends to push some weights **exactly to zero**.

Example:

Before L1:

```text
W = [2.5, 0.03, -1.8, 0.01]
```

After L1:

```text
W = [2.3, 0, -1.6, 0]
```

So L1 can effectively **remove unimportant features**.

This is called:

> **Feature Selection**

---

# Real-World Example

Suppose you're predicting house prices using:

```text
Area
Bedrooms
Location
Wall Color
Door Handle Type
Number of Windows
```

Maybe:

```text
Area        → Important
Bedrooms    → Important
Location    → Important
Wall Color  → Not important
Door Handle → Not important
```

L1 may push the weights of unimportant features toward **zero**.

So the model effectively ignores them.

---

# L2 Regularization

L2 adds the **squared values of weights** to the loss.

### Formula

[
\boxed{
L_{total}=L+\lambda\sum_i W_i^2
}
]

Unlike L1, L2 usually doesn't make weights exactly zero.

Instead, it makes them **smaller**.

---

# Example

Suppose:

```text
Weights:

5
-4
2
1
```

L2 penalizes large values strongly because of squaring:

[
5^2=25
]

[
(-4)^2=16
]

[
2^2=4
]

[
1^2=1
]

So:

```text
Large weights → Large penalty
Small weights → Small penalty
```

---

# Why Does L2 Work?

Because large weights receive a larger penalty.

The model therefore prefers:

```text
Smaller, smoother weights
```

instead of:

```text
Huge weights
```

This generally improves **generalization**.

---

# L1 vs L2

| Feature                 | L1                      | L2                    |   |                   |
| ----------------------- | ----------------------- | --------------------- | - | ----------------- |
| Penalty                 | (\lambda\sum            | W                     | ) | (\lambda\sum W^2) |
| Effect                  | Makes some weights zero | Makes weights smaller |   |                   |
| Feature selection       | ✅ Yes                   | Usually ❌             |   |                   |
| Sparse model            | ✅                       | Less likely           |   |                   |
| Large weights penalized | ✅                       | ✅ Strongly            |   |                   |
| Common name             | Lasso                   | Ridge                 |   |                   |

---

# Easy Memory Trick

### L1 → "Leaves weights at 0"

Think:

> **L1 = Less features**

### L2 → "Limits weight size"

Think:

> **L2 = Limits weights**

---

# Worked Example

Suppose:

```text
Original Loss = 10

Weights = [2, -3, 1]

λ = 0.1
```

---

## L1

Calculate:

[
|2|+|-3|+|1|
]

[
=2+3+1=6
]

Penalty:

[
0.1\times6=0.6
]

Total loss:

[
10+0.6=\boxed{10.6}
]

---

## L2

Calculate:

[
2^2+(-3)^2+1^2
]

[
=4+9+1=14
]

Penalty:

[
0.1\times14=1.4
]

Total loss:

[
10+1.4=\boxed{11.4}
]

---

# What is λ?

[
\lambda
]

is called the **regularization parameter**.

It controls how strongly we penalize large weights.

### Small λ

```text
λ = 0.0001

Weak regularization
```

The model can still become complex.

---

### Large λ

```text
λ = 10

Strong regularization
```

Weights are heavily restricted.

But if λ is **too large**, the model may become too simple and **underfit**.

---

# Important Connection to Bias-Variance

Remember our previous topic?

```text
Too Simple
    ↓
High Bias
    ↓
Underfitting
```

and

```text
Too Complex
    ↓
High Variance
    ↓
Overfitting
```

Regularization helps move a high-variance model toward a better balance.

```text
Overfitting
    ↓
Regularization
    ↓
Simpler model
    ↓
Better generalization
```

But too much regularization can cause:

```text
Too much regularization
        ↓
Model becomes too simple
        ↓
Underfitting
        ↓
High Bias
```

So the strength of regularization matters.

---

# L1 and L2 Gradient Intuition

For L2:

[
L_{reg}=L+\lambda\sum W^2
]

The derivative of the regularization term is:

[
\frac{\partial}{\partial W}(\lambda W^2)
========================================

2\lambda W
]

So larger weights receive a larger correction.

This is why L2 tends to **shrink weights toward zero**.

---

# L1 vs L2 Visual Intuition

```text
L1:

Large number of weights
      ↓
Some become exactly 0

[2.1, 0, -1.5, 0, 0.8]
```

```text
L2:

Weights become smaller

[2.1, 0.4, -1.5, 0.2, 0.8]

        ↓

[1.7, 0.3, -1.2, 0.15, 0.7]
```

---

# Exam/Interview Questions

### Q1. What is regularization?

A technique used to reduce overfitting by adding a penalty to the loss function.

### Q2. What is L1 regularization?

Adds the sum of absolute weight values to the loss.

### Q3. What is L2 regularization?

Adds the sum of squared weight values to the loss.

### Q4. Which one performs feature selection?

**L1.**

### Q5. Which one generally produces smoother/smaller weights?

**L2.**

### Q6. What happens if λ is too large?

The model can **underfit**.

---

# Must-Remember

> **L1 → Absolute values → Some weights become zero → Feature selection**

> **L2 → Squared values → Weights become small → Smoother model**

And:

[
\boxed{L_{total}=L+\lambda R(W)}
]

where (R(W)) is the regularization penalty.

---

# Quick Revision Sheet

| Concept           | L1           | L2                         |   |               |
| ----------------- | ------------ | -------------------------- | - | ------------- |
| Penalty           | (\lambda     | W                          | ) | (\lambda W^2) |
| Weight behavior   | Some → 0     | Small but usually non-zero |   |               |
| Feature selection | Yes          | No                         |   |               |
| Main goal         | Sparse model | Small/smooth weights       |   |               |
| Common name       | Lasso        | Ridge                      |   |               |

### One-line memory:

**L1 eliminates; L2 shrinks.**

---

# Active Learning

### Conceptual Questions

1. Why does regularization help prevent overfitting?
2. Why can L1 make some weights exactly zero?
3. What happens if the regularization parameter (\lambda) is too large?

### Practical Question

Given:

* Original Loss = **20**
* Weights = `[2, -3, 4]`
* (\lambda = 0.1)

Calculate:

**a)** Total loss using **L1 regularization**.

**b)** Total loss using **L2 regularization**.

Use:

[
L_1 = L + \lambda\sum|W|
]

[
L_2 = L + \lambda\sum W^2
]

Reply with your answers, and we'll move to **Topic 12: Early Stopping**.
