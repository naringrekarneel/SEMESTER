# Topic 9: Weight Initialization (Xavier & He Initialization)

> **Exam Importance:** ⭐⭐⭐⭐⭐ (Very Frequently Asked)

Weight Initialization decides **how the weights of a neural network are initialized before training starts**.

A good initialization helps the model:

* Learn faster.
* Avoid vanishing/exploding gradients.
* Reach better accuracy.

---

# ELI5 Explanation

Imagine three students taking an exam.

### Student A

Starts with **all answers blank**.

Needs to think from scratch.

---

### Student B

Starts with **reasonable guesses**.

Can improve quickly.

---

### Student C

Starts with **completely random nonsense**.

Needs more time to correct mistakes.

A neural network behaves similarly.

The **starting weights** affect how quickly and how well it learns.

---

# Why Can't We Initialize All Weights to Zero?

Suppose we initialize:

```text
W1 = 0
W2 = 0
W3 = 0
```

All neurons produce the **same output**.

During backpropagation:

* They receive the same gradients.
* They update identically.

Result:

```text
Neuron 1 = Neuron 2 = Neuron 3
```

The network never learns different features.

This is called the **Symmetry Problem**.

> **Must Remember:** Never initialize all weights to zero.

---

# Why Not Use Very Large Random Weights?

Example:

```text
Weights

15
-20
12
18
```

Problems:

* Activations become extremely large.
* Gradients explode.
* Training becomes unstable.

---

# Why Not Use Very Small Random Weights?

Example:

```text
Weights

0.000001
0.000003
0.000002
```

Problems:

* Outputs become very small.
* Gradients vanish.
* Learning becomes extremely slow.

---

# Goal of Good Weight Initialization

A good initialization should:

* Break symmetry.
* Keep activations in a reasonable range.
* Prevent exploding gradients.
* Prevent vanishing gradients.
* Speed up training.

---

# Xavier Initialization (Glorot Initialization)

> **Best for:** Sigmoid and Tanh activation functions.

### Core Idea

Choose weights so that the variance of activations remains approximately constant across layers.

### Formula

For a uniform distribution:

[
W \sim U\left(-\sqrt{\frac{6}{n_{in}+n_{out}}},;
\sqrt{\frac{6}{n_{in}+n_{out}}}\right)
]

Where:

* (n_{in}) = Number of input neurons.
* (n_{out}) = Number of output neurons.

---

### Example

Suppose:

* Input neurons = 100
* Output neurons = 50

[
\sqrt{\frac{6}{100+50}}
=======================

# \sqrt{\frac{6}{150}}

# \sqrt{0.04}

0.2
]

Weights are initialized between:

[
-0.2 \text{ and } 0.2
]

---

# He Initialization

> **Best for:** ReLU and its variants (Leaky ReLU, ELU, etc.).

### Why Do We Need It?

ReLU sets all negative values to **0**.

If weights are too small, many neurons may stop learning ("dead neurons").

He Initialization compensates by using a larger variance than Xavier.

### Formula

[
W \sim N\left(0,;
\frac{2}{n_{in}}\right)
]

Or equivalently, the standard deviation is:

[
\sqrt{\frac{2}{n_{in}}}
]

---

### Example

Suppose:

* Input neurons = 200

Standard deviation:

[
\sqrt{\frac{2}{200}}
====================

# \sqrt{0.01}

0.1
]

Weights are sampled from a normal distribution with:

* Mean = 0
* Standard deviation = 0.1

---

# Xavier vs He Initialization

| Feature                     | Xavier                     | He                 |
| --------------------------- | -------------------------- | ------------------ |
| Proposed for                | Sigmoid, Tanh              | ReLU               |
| Formula                     | (\frac{6}{n_{in}+n_{out}}) | (\frac{2}{n_{in}}) |
| Distribution                | Uniform or Normal          | Usually Normal     |
| Prevents Vanishing Gradient | ✅                          | ✅                  |
| Best Choice for ReLU        | ❌                          | ✅                  |

---

# Visual Idea

### Poor Initialization

```text
Input
 ↓
Large Weights
 ↓
Huge Outputs
 ↓
Exploding Gradient ❌
```

---

### Good Initialization

```text
Input
 ↓
Balanced Weights
 ↓
Balanced Outputs
 ↓
Stable Training ✅
```

---

# Worked Example

A neural network uses **ReLU** activation.

Number of input neurons = **128**

Using He Initialization:

[
\sqrt{\frac{2}{128}}
====================

# \sqrt{0.015625}

0.125
]

The weights are initialized from a normal distribution with:

* Mean = 0
* Standard deviation = 0.125

---

# Advantages of Proper Weight Initialization

* Faster convergence.
* Stable gradients.
* Better accuracy.
* Prevents exploding gradients.
* Prevents vanishing gradients.

---

# Common Interview Questions

### Q1. Why shouldn't weights be initialized to zero?

Because all neurons learn the same features (symmetry problem).

---

### Q2. Which initialization is best for ReLU?

**He Initialization.**

---

### Q3. Which initialization is best for Sigmoid and Tanh?

**Xavier Initialization.**

---

### Q4. What happens with very large initial weights?

Exploding gradients and unstable training.

---

### Q5. What happens with very small initial weights?

Vanishing gradients and slow learning.

---

# Exam/Interview Must-Remember Points

* Initialize weights randomly, not all zeros.
* Xavier Initialization is used for **Sigmoid** and **Tanh**.
* He Initialization is used for **ReLU**.
* Good initialization speeds up training and stabilizes gradients.
* It helps prevent vanishing and exploding gradients.

---

# Memory Trick 🧠

| Activation Function | Initialization |
| ------------------- | -------------- |
| Sigmoid             | Xavier         |
| Tanh                | Xavier         |
| ReLU                | He             |
| Leaky ReLU          | He             |

**Easy Mnemonic:**

* **Xavier → eXtra smooth activations (Sigmoid/Tanh).**
* **He → Heavy-duty for ReLU.**

---

# Quick Revision

* Never initialize all weights to zero.
* Xavier → Sigmoid/Tanh.
* He → ReLU.
* Good initialization prevents vanishing and exploding gradients.
* Proper initialization leads to faster and more stable training.

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
Weight Initialization
        ↓
Next: Bias-Variance Tradeoff
```

---

# Active Learning

### Conceptual Questions

1. Why is initializing all weights to zero a bad idea?
2. Which initialization method is preferred for ReLU activation, and why?
3. What problems can occur if weights are initialized with very large values?

### Practical Question

A neural network has **64 input neurons** and uses **ReLU** activation.

Using **He Initialization**, calculate the standard deviation of the weight initialization.

[
\text{Std Dev} = \sqrt{\frac{2}{64}}
]

Compute the value and explain why this initialization is suitable for ReLU.

Reply with your answers, and then we'll move to **Topic 10: Bias-Variance Tradeoff**, which introduces the core concepts behind regularization.
