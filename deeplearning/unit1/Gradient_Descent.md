# Topic 13: Gradient Descent

**Gradient Descent** is the optimization algorithm used to **minimize the loss function** by updating the weights and bias of a neural network. It is one of the **most important concepts in Deep Learning**.

> **Exam Importance:** ⭐⭐⭐⭐⭐ (Very Frequently Asked)

---

# ELI5 (Explain Like I'm 5)

Imagine you're standing on a mountain in thick fog.

Your goal is to reach the **lowest point (the valley)**, but you can't see far ahead.

So you:

1. Feel the ground around you.
2. Take one small step downhill.
3. Repeat until you reach the bottom.

This is exactly how **Gradient Descent** works.

* **Mountain** → Loss Function
* **Valley** → Minimum Loss
* **Steps** → Weight Updates

---

# What is Gradient Descent?

Gradient Descent is an optimization algorithm that **reduces the loss** by updating the model's weights in the direction where the loss decreases the fastest.

Its objective is to find the **best weights** that produce the smallest possible loss.

---

# Why Do We Need Gradient Descent?

After computing the loss, the model knows **how wrong** its prediction is.

But it still doesn't know:

> **"How should I change my weights to reduce this error?"**

Gradient Descent answers this question.

---

# Training Process

```text id="gd001"
Input Data
      ↓
Prediction
      ↓
Calculate Loss
      ↓
Compute Gradient
      ↓
Update Weights
      ↓
Repeat Until Loss is Small
```

---

# How Gradient Descent Works

### Step 1

Initialize random weights.

↓

### Step 2

Make predictions.

↓

### Step 3

Calculate the loss.

↓

### Step 4

Compute the gradient (direction of steepest increase).

↓

### Step 5

Move **opposite** to the gradient (toward lower loss).

↓

### Step 6

Repeat until the loss becomes very small.

---

# Weight Update Formula

The most important formula:

[
\boxed{
w_{\text{new}}
==============

## w_{\text{old}}

\eta
\frac{\partial L}{\partial w}
}
]

Where:

| Symbol                          | Meaning                               |
| ------------------------------- | ------------------------------------- |
| (w)                             | Weight                                |
| (L)                             | Loss Function                         |
| (\frac{\partial L}{\partial w}) | Gradient (slope of the loss function) |
| (\eta)                          | Learning Rate                         |

---

# Understanding the Formula

* **Gradient** tells us which direction increases the loss.
* To reduce the loss, we move in the **opposite direction**, which is why the formula uses a **minus (-) sign**.

---

# Worked Example

Suppose:

Current weight:

[
w=5
]

Learning Rate:

[
\eta=0.1
]

Gradient:

[
\frac{\partial L}{\partial w}=2
]

### Step 1

Apply the formula:

[
w_{\text{new}}
==============

## 5

0.1(2)
]

### Step 2

[
w_{\text{new}}
==============

# 5-0.2

4.8
]

The weight has moved slightly in the direction that reduces the loss.

---

# What is Learning Rate?

The **Learning Rate (η)** determines **how big each update step is**.

---

## Small Learning Rate

Example:

η = 0.001

Advantages:

* Stable learning
* Accurate updates

Disadvantage:

* Training is very slow

---

## Large Learning Rate

Example:

η = 1

Advantages:

* Faster movement

Disadvantages:

* May overshoot the minimum
* Training can become unstable

---

## Good Learning Rate

Usually:

* 0.01
* 0.001
* 0.0001

These values often provide a good balance between speed and stability.

---

# Visual Idea

### Good Learning Rate

```text id="gd002"
Start

↓

↓

↓

Minimum
```

Steady progress toward the minimum.

---

### Very Large Learning Rate

```text id="gd003"
Start

↓

Minimum

↑

↓

↑

↓

```

The algorithm jumps back and forth around the minimum instead of settling.

---

# Types of Gradient Descent

## 1. Batch Gradient Descent

* Uses the **entire dataset** to calculate the gradient.
* Stable updates.
* Slower on large datasets.

---

## 2. Stochastic Gradient Descent (SGD)

* Updates weights **after every training example**.
* Faster.
* More noisy (loss fluctuates).

---

## 3. Mini-Batch Gradient Descent

* Uses a **small batch** of training examples.
* Combines the advantages of Batch and SGD.
* Most commonly used in modern deep learning.

---

# Comparison

| Type       | Data Used      | Speed | Stability |
| ---------- | -------------- | ----- | --------- |
| Batch      | Entire dataset | Slow  | High      |
| SGD        | One sample     | Fast  | Low       |
| Mini-Batch | Small batch    | Fast  | High      |

---

# Real-World Example

Imagine adjusting the volume on your headphones.

* Too loud → Decrease slightly.
* Too quiet → Increase slightly.

You don't jump from volume 100 to 0.

You make **small adjustments** until it's comfortable.

Gradient Descent adjusts model weights in the same gradual way.

---

# Advantages

* Simple and efficient.
* Works well with large neural networks.
* Reduces prediction error.
* Forms the basis of most deep learning optimization algorithms.

---

# Limitations

* May get stuck in local minima or saddle points.
* Sensitive to the learning rate.
* Can be slow if the learning rate is too small.

Modern optimizers like **Adam**, **RMSProp**, and **AdaGrad** improve upon basic Gradient Descent.

---

# Exam Definition (2–3 Marks)

**Gradient Descent:**
Gradient Descent is an optimization algorithm used to minimize the loss function by iteratively updating the weights and bias in the direction opposite to the gradient of the loss.

---

# Frequently Asked Exam/Interview Questions

1. What is Gradient Descent?
2. Why is Gradient Descent used?
3. Write the Gradient Descent update formula.
4. What is the role of the learning rate?
5. Differentiate Batch, Stochastic, and Mini-Batch Gradient Descent.
6. Why do we subtract the gradient instead of adding it?

---

# Must-Remember Formula

### Weight Update

[
\boxed{
w_{\text{new}}
==============

## w_{\text{old}}

\eta
\frac{\partial L}{\partial w}
}
]

---

# Must-Remember Points

* Gradient Descent minimizes the loss.
* It updates weights iteratively.
* The gradient indicates the direction of increasing loss.
* The minus sign moves the weights toward decreasing loss.
* Learning rate controls the size of updates.
* Mini-Batch Gradient Descent is the most commonly used approach.

---

# Quick Revision Bullets

* Gradient Descent = Optimization algorithm.
* Goal: Minimize loss.
* Update weights using the gradient.
* Learning rate controls step size.
* Too small → Slow learning.
* Too large → Overshooting.
* Mini-Batch Gradient Descent is widely used.

---

# Mini Quiz

### Q1

What is the main goal of Gradient Descent?

A. Increase accuracy

B. Minimize loss

C. Increase the number of neurons

D. Add hidden layers

---

### Q2

Which symbol represents the learning rate?

A. θ

B. η

C. α

D. β

---

### Q3

Which type of Gradient Descent is most commonly used in Deep Learning?

A. Batch

B. Stochastic

C. Mini-Batch

D. Random

---

# Active Learning

### Conceptual Questions

1. Why do we subtract the gradient in the weight update formula?
2. What happens if the learning rate is too large?
3. Why is Mini-Batch Gradient Descent preferred over Batch Gradient Descent?

### Practical Question

A model has:

* Current weight = **8**
* Learning rate = **0.05**
* Gradient = **4**

Using the Gradient Descent formula, calculate the **new weight**.

---

## Topic Connection

You've now learned the complete learning cycle:

1. **Forward Pass** → The network makes a prediction.
2. **Loss Function** → Measures the prediction error.
3. **Gradient Descent** → Decides how to reduce the error.

The final missing piece is:

**How do we calculate the gradient for every weight in a multi-layer neural network?**

That is the role of **Backpropagation**, one of the most important algorithms in Deep Learning.

**Next Topic:** **Backpropagation**.
