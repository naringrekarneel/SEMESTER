# Topic 11: Activation Functions (Sigmoid, Tanh, ReLU, Softmax)

An **Activation Function** decides **whether a neuron should be activated (produce an output) and what that output should be**. It introduces **non-linearity**, allowing neural networks to solve complex real-world problems.

> **Exam Importance:** ⭐⭐⭐⭐⭐ (One of the Most Important Topics)

---

# ELI5 (Explain Like I'm 5)

Imagine a teacher deciding whether a student should pass.

The teacher first calculates the total marks.

Then the teacher decides:

* Pass
* Fail
* Grade A
* Grade B

The **decision-making step** is like an **activation function**.

Without it, the neural network would only perform simple calculations and could not learn complex patterns.

---

# Why Do We Need Activation Functions?

Without an activation function:

```text
Input
   ↓
Linear Calculation
   ↓
Output
```

Even if we add many hidden layers, the network behaves like a **single linear model**.

With an activation function:

```text
Input
   ↓
Weighted Sum
   ↓
Activation Function
   ↓
Output
```

Now the network can learn:

* Curves
* Images
* Speech
* Language
* Complex relationships

---

# General Working

Every neuron performs two steps.

### Step 1: Calculate Weighted Sum

[
z = \sum x_iw_i + b
]

### Step 2: Apply Activation Function

[
a = f(z)
]

Where:

* (z) = Weighted Sum
* (f(z)) = Activation Function
* (a) = Output of the neuron

---

# Types of Activation Functions

Your syllabus includes:

1. Sigmoid
2. Tanh
3. ReLU
4. Softmax

---

# 1. Sigmoid Activation Function

## Formula

[
\sigma(x)=\frac{1}{1+e^{-x}}
]

---

## Output Range

[
0 \text{ to } 1
]

---

## Graph Shape

```text
1.0 |                ______
    |             __/
0.5 |---------__/
    |      __/
0.0 |_____/
       x
```

S-shaped (Sigmoid Curve)

---

## Example

Input = 5

Output ≈ 0.99

Input = 0

Output = 0.5

Input = -5

Output ≈ 0.01

Large positive inputs move close to **1**, while large negative inputs move close to **0**.

---

## Uses

* Binary Classification
* Output Layer (Yes/No)

Example:

Spam Probability

0.98 → Spam

0.02 → Not Spam

---

## Advantages

* Smooth curve.
* Produces probability-like outputs.
* Easy to interpret.

---

## Disadvantages

* Suffers from the **Vanishing Gradient Problem**.
* Slow training.
* Output is not zero-centered.

---

# 2. Tanh (Hyperbolic Tangent)

## Formula

[
\tanh(x)=\frac{e^x-e^{-x}}{e^x+e^{-x}}
]

---

## Output Range

[
-1 \text{ to } 1
]

---

## Graph Shape

```text
 1 |          ______
   |       __/
 0 |-----/
   |   __
-1 |__/
```

---

## Example

Input = 5

Output ≈ 1

Input = 0

Output = 0

Input = -5

Output ≈ -1

---

## Uses

Often used in hidden layers (less common today than ReLU).

---

## Advantages

* Zero-centered output.
* Better than Sigmoid in many cases.

---

## Disadvantages

* Still suffers from the Vanishing Gradient Problem.

---

# 3. ReLU (Rectified Linear Unit)

## Formula

[
f(x)=\max(0,x)
]

---

## Output

* If (x < 0) → Output = 0
* If (x \ge 0) → Output = x

---

## Graph

```text
 ^
 |        /
 |      /
 |    /
 |  /
 |/
 +----------------->
```

---

## Example

| Input | Output |
| ----- | ------ |
| -5    | 0      |
| -2    | 0      |
| 0     | 0      |
| 3     | 3      |
| 6     | 6      |

---

## Uses

Most commonly used activation function for **hidden layers** in modern deep learning.

---

## Advantages

* Very fast computation.
* Simple formula.
* Reduces Vanishing Gradient.
* Faster convergence during training.

---

## Disadvantages

* Can suffer from the **Dying ReLU Problem**, where neurons output 0 for all negative inputs and stop learning.

---

# 4. Softmax Activation Function

Softmax is used for **multi-class classification**.

Instead of giving just one output, it converts outputs into **probabilities** that sum to **1**.

---

## Formula

[
P_i=\frac{e^{z_i}}{\sum_j e^{z_j}}
]

---

## Example

Suppose a model predicts:

| Class | Score |
| ----- | ----- |
| Cat   | 2.5   |
| Dog   | 1.2   |
| Horse | 0.3   |

After Softmax:

| Class | Probability |
| ----- | ----------- |
| Cat   | 0.73        |
| Dog   | 0.21        |
| Horse | 0.06        |

The probabilities add up to:

[
0.73 + 0.21 + 0.06 = 1
]

The predicted class is **Cat** because it has the highest probability.

---

# Comparison Table

| Activation Function | Output Range     | Main Use                   | Advantages               | Disadvantages               |
| ------------------- | ---------------- | -------------------------- | ------------------------ | --------------------------- |
| Sigmoid             | 0 to 1           | Binary Classification      | Probability output       | Vanishing Gradient          |
| Tanh                | -1 to 1          | Hidden Layers              | Zero-centered            | Vanishing Gradient          |
| ReLU                | 0 to ∞           | Hidden Layers              | Fast, simple, efficient  | Dying ReLU                  |
| Softmax             | 0 to 1 (sum = 1) | Multi-class Classification | Probability distribution | Used mainly in output layer |

---

# Which Activation Function Should You Use?

| Layer                    | Recommended Function |
| ------------------------ | -------------------- |
| Hidden Layer             | ReLU                 |
| Binary Output Layer      | Sigmoid              |
| Multi-class Output Layer | Softmax              |

---

# Real-World Examples

### Face Unlock

Output:

* Person A → 0.91
* Person B → 0.05
* Person C → 0.04

Softmax selects **Person A**.

---

### Spam Detection

Sigmoid Output:

0.96 → Spam

0.04 → Not Spam

---

### Digit Recognition

Output:

* 0 → 0.01
* 1 → 0.02
* 2 → 0.90
* Others → Very small values

Softmax predicts **Digit 2**.

---

# Exam Definition (2–3 Marks)

**Activation Function:**
An activation function is a mathematical function applied to the weighted sum of a neuron. It introduces non-linearity into the neural network and determines the neuron's output, enabling the network to learn complex patterns.

---

# Frequently Asked Exam/Interview Questions

1. What is an activation function?
2. Why is an activation function required?
3. Compare Sigmoid, Tanh, ReLU, and Softmax.
4. Why is ReLU preferred over Sigmoid?
5. What is the Dying ReLU problem?
6. Why is Softmax used for multi-class classification?

---

# Must-Remember Formulas

### Sigmoid

[
\sigma(x)=\frac{1}{1+e^{-x}}
]

### Tanh

[
\tanh(x)=\frac{e^x-e^{-x}}{e^x+e^{-x}}
]

### ReLU

[
f(x)=\max(0,x)
]

### Softmax

[
P_i=\frac{e^{z_i}}{\sum_j e^{z_j}}
]

---

# Must-Remember Points

* Activation functions introduce **non-linearity**.
* Without them, deep networks behave like linear models.
* **ReLU** is the most commonly used hidden-layer activation.
* **Sigmoid** is mainly used for binary classification.
* **Softmax** is used for multi-class classification.
* **Tanh** outputs values between -1 and 1.

---

# Quick Revision Bullets

* Activation functions decide a neuron's output.
* Sigmoid → Binary classification (0 to 1).
* Tanh → Hidden layers (-1 to 1).
* ReLU → Most popular hidden-layer activation.
* Softmax → Multi-class classification (probabilities sum to 1).
* ReLU helps reduce the vanishing gradient problem.

---

# Mini Quiz

### Q1

Which activation function is most commonly used in hidden layers?

A. Sigmoid

B. Tanh

C. ReLU

D. Softmax

---

### Q2

Which activation function is mainly used for multi-class classification?

A. ReLU

B. Sigmoid

C. Softmax

D. Tanh

---

### Q3

True or False:

Without activation functions, a deep neural network behaves like a linear model.

---

# Active Learning

### Conceptual Questions

1. Why are activation functions necessary in neural networks?
2. Why is ReLU generally preferred over Sigmoid for hidden layers?
3. What is the main difference between Sigmoid and Softmax?

### Practical Question

You are building:

1. A **Spam Detection** system (Spam/Not Spam).
2. A **Digit Recognition** system (Digits 0–9).

Which activation function would you use for the output layer in each case? Explain your answer.

---

## Topic Connection

You've now completed the core building blocks of neural networks:

* Perceptron
* MLP
* Representation Power
* Activation Functions

Next, we'll study **Loss Functions (MSE and Cross Entropy)**, which measure **how wrong a neural network's predictions are** and provide the error signal used during learning.
