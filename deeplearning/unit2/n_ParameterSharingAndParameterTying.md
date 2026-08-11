# Topic 14: Parameter Sharing and Parameter Tying

> **Exam Importance:** ⭐⭐⭐☆☆ — Less common, but important for understanding CNNs, RNNs, and model efficiency.

This topic sounds complicated, but the idea is actually pretty simple:

> **Instead of giving every part of a model its own separate parameters, we can make different parts share the same parameters.**

---

# ELI5 Explanation

Imagine you have **10 doors**.

### Without parameter sharing

You hire 10 different people to design each door.

```text
Door 1 → Designer 1
Door 2 → Designer 2
Door 3 → Designer 3
...
Door 10 → Designer 10
```

That's a lot of unnecessary work.

---

### With parameter sharing

You hire **one designer** and use the same design for all 10 doors.

```text
          One Designer
               ↓
     ┌─────┬─────┬─────┐
     ↓     ↓     ↓     ↓
   Door1 Door2 Door3 Door4 ...
```

That's **parameter sharing**.

---

# Why Do We Share Parameters?

Main reasons:

### 1. Fewer parameters

Less memory is required.

### 2. Less overfitting

The model has fewer independent parameters to memorize the training data.

### 3. Better generalization

The same learned pattern can be recognized in different locations or situations.

### 4. Faster training

Fewer parameters generally means less computation.

---

# Real-World Example: CNN

Parameter sharing is extremely important in **Convolutional Neural Networks (CNNs)**.

Suppose we're looking for a **vertical edge** in an image.

```text id="u0j94f"
|       |
|       |
|       |
```

The edge could appear:

```text id="1m2vry"
Left       Center       Right
 ↓           ↓            ↓
| |         | |          | |
```

Do we need a different detector for every location?

No.

A CNN uses the **same filter/kernel** across the entire image.

```text id="75nq1x"
Same filter
    ↓
┌───┬───┬───┐
│   │   │   │
│ → │ → │ → │
└───┴───┴───┘
```

The same weights detect the same feature everywhere.

That's parameter sharing.

---

# Example

Suppose a CNN filter is:

[
K=
\begin{bmatrix}
1&0&-1\
1&0&-1\
1&0&-1
\end{bmatrix}
]

This filter can detect vertical edges.

The **same kernel** is applied across different regions of the image.

```text id="h55wz6"
Image Region 1 → Kernel K
Image Region 2 → Kernel K
Image Region 3 → Kernel K
Image Region 4 → Kernel K
```

We don't create:

```text
K1
K2
K3
K4
```

Instead:

```text
K
↓
Used everywhere
```

---

# Parameter Tying

Parameter tying is closely related to parameter sharing.

It means we **force two or more parameters to have the same value or relationship**.

For example:

[
W_1=W_2
]

Instead of learning:

```text
W1 = 0.52
W2 = 0.81
```

we require:

```text
W1 = W2
```

So there's really only **one independent parameter**.

---

# Sharing vs Tying

These terms are often used interchangeably, but you can understand them this way:

### Parameter Sharing

The **same parameters are reused** in multiple locations.

Example:

```text
CNN filter → applied across image
```

### Parameter Tying

Different parameters are **constrained to be identical or related**.

Example:

[
W_1=W_2
]

---

# RNN Example

Parameter sharing is also extremely important in **Recurrent Neural Networks (RNNs)**.

Suppose we're processing:

```text
"I love deep learning"
```

The RNN processes:

```text
I → love → deep → learning
```

Instead of having completely different weights for every word position:

```text
Position 1 → W1
Position 2 → W2
Position 3 → W3
Position 4 → W4
```

the RNN uses the **same weights** at each time step:

```text
Time 1 → W
Time 2 → W
Time 3 → W
Time 4 → W
```

This allows the network to handle sequences of different lengths.

---

# Why Is This Useful?

Imagine an RNN processing:

```text
10 words
```

Then another sentence:

```text
100 words
```

If we had separate weights for every position, we'd need different parameters for different sequence lengths.

Parameter sharing solves this.

```text
Same W
 ↓
Time 1
Time 2
Time 3
...
Time 100
```

---

# Worked Example

Suppose a neural network has:

```text
100 locations
```

and each location needs a filter with:

```text
9 parameters
```

### Without parameter sharing:

[
100\times9=900
]

parameters.

### With parameter sharing:

We use one filter:

[
9
]

parameters.

So:

```text
Without sharing → 900 parameters
With sharing    → 9 parameters
```

That's a **huge reduction**.

---

# Parameter Sharing and Regularization

Remember our goal?

> Reduce overfitting.

Parameter sharing helps because the model has fewer independent parameters.

```text
More independent parameters
        ↓
More model capacity
        ↓
Greater chance of overfitting
```

Parameter sharing:

```text
Shared parameters
        ↓
Fewer independent parameters
        ↓
Less complexity
        ↓
Better generalization
```

---

# Advantages

* Reduces number of parameters.
* Reduces memory requirements.
* Reduces overfitting.
* Improves computational efficiency.
* Allows models to detect repeated patterns.
* Essential for CNNs and RNNs.

---

# Disadvantages

Parameter sharing assumes that the **same pattern can be useful in multiple places**.

That isn't always true.

For example, if different parts of an image require completely different specialized processing, forcing the same parameters everywhere may reduce model flexibility.

---

# Exam/Interview Must-Remember

### Parameter Sharing

> Reusing the same set of parameters across different parts of a model.

### Common examples:

* **CNN:** Same convolution filter across image locations.
* **RNN:** Same weights across time steps.

### Benefits:

* Fewer parameters.
* Less memory.
* Less overfitting.
* Better generalization.

---

# Quick Revision

| Concept           | Meaning                              |
| ----------------- | ------------------------------------ |
| Parameter Sharing | Reuse the same parameters            |
| Parameter Tying   | Force parameters to be equal/related |
| CNN               | Shares filters spatially             |
| RNN               | Shares weights across time           |
| Main benefit      | Fewer parameters + less overfitting  |

### One-line memory:

> **"Learn once, use many times."**

---

# Connection

```text
Bias-Variance
     ↓
L1/L2
     ↓
Early Stopping
     ↓
Dataset Augmentation
     ↓
Parameter Sharing & Tying
     ↓
Next: Injecting Noise at Input
```

We're now moving toward techniques that deliberately introduce **controlled randomness** to make neural networks more robust.

---

# Active Learning

### Conceptual Questions

1. Why does parameter sharing reduce the number of parameters?
2. Give one example of parameter sharing in a CNN and one in an RNN.
3. How can parameter sharing help reduce overfitting?

### Practical Question

A CNN applies a **3 × 3 filter** over **1,000 different image locations**.

Without parameter sharing, each location has its own 3 × 3 filter.

With parameter sharing, the same filter is reused everywhere.

How many parameters are required in each case?
