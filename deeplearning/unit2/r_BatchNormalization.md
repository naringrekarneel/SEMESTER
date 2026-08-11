# Topic 18: Batch Normalization

> **Exam Importance:** ⭐⭐⭐⭐⭐ — Very frequently asked in Deep Learning exams and interviews.

Batch Normalization, or **BatchNorm**, is a technique that **normalizes the activations of a neural network during training**.

Its main benefits are:

* More stable training
* Faster convergence
* Better gradient flow
* Sometimes improved generalization

---

# ELI5 Explanation

Imagine you're running a race with 100 people.

Some people are running:

```text
10 km/h
```

Others:

```text
50 km/h
```

It's difficult to manage the group.

So you normalize everyone to roughly the same scale.

Neural networks have a similar problem.

Different layers can produce activations with very different values.

Batch Normalization brings them into a more controlled range.

---

# Basic Idea

Suppose a layer produces:

```text
10
100
1000
50
500
```

These values have very different scales.

BatchNorm transforms them into values with approximately:

```text
mean ≈ 0
variance ≈ 1
```

This makes optimization easier.

---

# Why Is It Useful?

Consider a deep network:

```text
Input
 ↓
Layer 1
 ↓
Layer 2
 ↓
Layer 3
 ↓
Layer 4
 ↓
Output
```

As information moves through the network, activations can become badly scaled.

BatchNorm helps keep the activations controlled.

```text
Layer
 ↓
BatchNorm
 ↓
Next Layer
```

---

# Step-by-Step Batch Normalization

Suppose a mini-batch contains:

[
x=[2,4,6,8]
]

---

## Step 1: Calculate Mean

[
\mu=\frac{2+4+6+8}{4}
]

[
\boxed{\mu=5}
]

---

## Step 2: Calculate Variance

[
\sigma^2=
\frac{(2-5)^2+(4-5)^2+(6-5)^2+(8-5)^2}{4}
]

# [

\frac{9+1+1+9}{4}
]

[
\boxed{\sigma^2=5}
]

---

## Step 3: Normalize

Formula:

[
\boxed{
\hat{x}=
\frac{x-\mu}
{\sqrt{\sigma^2+\epsilon}}
}
]

where (\epsilon) is a very small value added for numerical stability.

So the values are transformed to approximately:

```text
Negative values
      ↓
Around zero
      ↓
Positive values
```

---

# But Why Do We Need γ and β?

Here's an important detail.

If we simply normalize every activation to mean 0 and variance 1, we might restrict what the network can learn.

So BatchNorm introduces two learnable parameters:

[
\gamma
]

and

[
\beta
]

The final transformation is:

[
\boxed{
y=\gamma\hat{x}+\beta
}
]

Where:

* (\gamma) = learnable scale
* (\beta) = learnable shift

The network learns the appropriate scale and position.

---

# Complete BatchNorm Formula

The complete process is:

[
\boxed{
\hat{x}=
\frac{x-\mu_B}
{\sqrt{\sigma_B^2+\epsilon}}
}
]

Then:

[
\boxed{
y=\gamma\hat{x}+\beta
}
]

Where:

* (\mu_B) = mini-batch mean
* (\sigma_B^2) = mini-batch variance
* (\epsilon) = small constant
* (\gamma) = learnable scaling parameter
* (\beta) = learnable shifting parameter

---

# Real-World Intuition

Imagine a teacher receives marks from different exams.

One exam:

```text
10–20
```

Another:

```text
0–100
```

Another:

```text
0–1000
```

Comparing raw numbers isn't useful.

Normalize them first.

BatchNorm does something similar to neural network activations.

---

# Where Is BatchNorm Used?

A common structure is:

```text
Input
 ↓
Linear / Convolution
 ↓
BatchNorm
 ↓
Activation
 ↓
Next Layer
```

For example:

```text
Input
 ↓
Dense
 ↓
BatchNorm
 ↓
ReLU
 ↓
Dense
 ↓
BatchNorm
 ↓
ReLU
 ↓
Output
```

In CNNs, BatchNorm is commonly applied after convolution layers.

---

# BatchNorm and Training

During training, BatchNorm calculates statistics from the **current mini-batch**.

```text
Mini-batch
   ↓
Mean
   ↓
Variance
   ↓
Normalize
   ↓
Scale + Shift
```

---

# BatchNorm During Testing

At inference/testing time, we generally don't calculate statistics from the current test example.

Instead, BatchNorm uses **running estimates** of the mean and variance accumulated during training.

This is important.

### Training

```text
Current mini-batch
       ↓
Mean + Variance
```

### Testing

```text
Running Mean + Running Variance
```

---

# BatchNorm vs Dropout

These are often confused.

| Feature      | BatchNorm               | Dropout                  |
| ------------ | ----------------------- | ------------------------ |
| Main idea    | Normalize activations   | Randomly disable neurons |
| Main purpose | Stable/faster training  | Reduce overfitting       |
| Training     | Uses batch statistics   | Randomly drops neurons   |
| Testing      | Uses running statistics | Dropout disabled         |
| Randomness   | Not the main mechanism  | Central mechanism        |

Both can improve generalization, but they work differently.

---

# Important Benefits

### 1. Faster Training

Normalization can make optimization easier.

### 2. Stable Gradients

Helps keep activations in reasonable ranges.

### 3. Allows Higher Learning Rates

In many cases, BatchNorm makes training more tolerant of larger learning rates.

### 4. Better Optimization

The network can converge more easily.

### 5. Some Regularization Effect

Batch statistics introduce some noise, which can sometimes help generalization.

But:

> **BatchNorm should not simply be thought of as a replacement for all regularization techniques.**

---

# Disadvantages

BatchNorm also has limitations.

### Small Batch Sizes

If the mini-batch is very small, mean and variance estimates can be unreliable.

### Additional Computation

It adds some computation and parameters.

### Train/Test Difference

The way statistics are calculated differs between training and inference.

---

# Worked Example

Suppose:

[
x=[2,4,6,8]
]

Mean:

[
\mu=5
]

Variance:

[
\sigma^2=5
]

Ignoring (\epsilon) for simplicity:

For (x=2):

[
\hat{x}=\frac{2-5}{\sqrt5}
]

[
\approx -1.34
]

For (x=8):

[
\hat{x}=\frac{8-5}{\sqrt5}
]

[
\approx1.34
]

So:

```text
Original:

2   4   6   8

After normalization:

-1.34   -0.45   0.45   1.34
```

Then BatchNorm applies:

[
y=\gamma\hat{x}+\beta
]

The network learns appropriate values of (\gamma) and (\beta).

---

# BatchNorm in One Diagram

```text
             Input
               ↓
          Neural Layer
               ↓
        Calculate Mean
               ↓
      Calculate Variance
               ↓
           Normalize
               ↓
        Scale + Shift
          γ      β
               ↓
          Activation
               ↓
         Next Layer
```

---

# Exam/Interview Must-Remember

### Definition

> **Batch Normalization normalizes activations using the statistics of a mini-batch and then applies learnable scaling and shifting.**

### Formula

[
\boxed{
\hat{x}=
\frac{x-\mu_B}
{\sqrt{\sigma_B^2+\epsilon}}
}
]

[
\boxed{
y=\gamma\hat{x}+\beta
}
]

### Remember:

* (\mu_B) → batch mean
* (\sigma_B^2) → batch variance
* (\gamma) → scale
* (\beta) → shift
* Training → batch statistics
* Testing → running statistics

---

# Memory Trick

Think:

> **Normalize → Scale → Shift**

```text
Raw activation
      ↓
Normalize
      ↓
γ × value
      ↓
+ β
      ↓
Final activation
```

---

# Quick Revision

* BatchNorm normalizes activations.
* Uses mini-batch mean and variance during training.
* Uses running statistics during inference.
* Uses learnable (\gamma) and (\beta).
* Improves training stability and often speeds convergence.
* Can provide some regularization effect.
* Small batches can make BatchNorm less reliable.

### One-line memory:

> **"Keep the activations well-behaved so the network can learn more smoothly."**

---

# Connection

We've now reached the final topic:

```text
L1/L2
  ↓
Early Stopping
  ↓
Dataset Augmentation
  ↓
Parameter Sharing
  ↓
Input Noise
  ↓
Ensemble Methods
  ↓
Dropout
  ↓
Batch Normalization
  ↓
⭐ Hyperparameter Tuning ⭐
```

Next is **Grid Search and Random Search**, where we'll learn how to systematically choose things like learning rate, batch size, dropout rate, number of layers, etc.

---

# Active Learning

### Conceptual Questions

1. What are the two learnable parameters in BatchNorm, and what do they do?
2. What statistics does BatchNorm use during training?
3. Why can BatchNorm help neural networks train faster?

### Practical Question

Given the mini-batch:

[
x=[2,4,6,8]
]

Calculate:

1. Mean (\mu)
2. Variance (\sigma^2)
3. The normalized value of (x=8), ignoring (\epsilon)

Use:

[
\hat{x}=\frac{x-\mu}{\sqrt{\sigma^2}}
]

Reply with your answer, and we'll finish the syllabus with **Topic 19: Hyperparameter Tuning — Grid Search vs Random Search**.
