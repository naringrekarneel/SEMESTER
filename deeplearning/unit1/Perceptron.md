# Topic 7: Perceptron

The **Perceptron** is the **first learning algorithm** for an Artificial Neural Network. It was proposed by **Frank Rosenblatt** in **1958**. Unlike the McCulloch-Pitts neuron, the Perceptron can **learn from training data** by adjusting its weights.

---

# ELI5 (Explain Like I'm 5)

Imagine a teacher checking whether a student has passed.

At first, the teacher guesses randomly.

After seeing the correct answer, the teacher realizes the mistake and changes the marking strategy.

The next time, the teacher makes a better decision.

This process repeats until the teacher becomes accurate.

A **Perceptron learns in exactly the same way**—it makes predictions, compares them with the correct answers, and updates its weights when it makes mistakes.

---

# What is a Perceptron?

A **Perceptron** is a **single-layer artificial neural network** used for **binary classification** problems. It takes several inputs, assigns weights to them, computes a weighted sum, applies an activation function, and predicts one of two classes.

Examples:

* Spam or Not Spam
* Pass or Fail
* Cat or Dog
* Yes or No

---

# Structure of a Perceptron

```text
      x₁ ──►(×w₁)
               \
      x₂ ──►(×w₂) ─► Σ + Bias ─► Activation Function ─► Output
               /
      x₃ ──►(×w₃)
```

---

# Components

| Component           | Purpose                           |
| ------------------- | --------------------------------- |
| Input (x)           | Features given to the model       |
| Weight (w)          | Importance of each feature        |
| Bias (b)            | Helps shift the decision boundary |
| Weighted Sum        | Combines all inputs               |
| Activation Function | Produces the final output         |
| Output              | Predicted class (0 or 1)          |

---

# Mathematical Model

### Step 1: Calculate Weighted Sum

[
z = x_1w_1 + x_2w_2 + ... + x_nw_n + b
]

or

[
z = \sum_{i=1}^{n} x_iw_i + b
]

### Step 2: Apply Step Activation Function

[
y =
\begin{cases}
1, & \text{if } z \geq 0 \
0, & \text{if } z < 0
\end{cases}
]

Where:

* **z** = Weighted sum
* **y** = Output

---

# How Does the Perceptron Learn?

The learning process consists of four steps:

### Step 1

Take the input values.

↓

### Step 2

Calculate the prediction.

↓

### Step 3

Compare the prediction with the actual answer.

↓

### Step 4

If the prediction is wrong, adjust the weights.

Repeat this process until the predictions become correct.

---

# Worked Example

Suppose we want to predict whether a student passes.

Inputs:

* Attendance = 1
* Assignment = 1

Weights:

* w₁ = 0.5
* w₂ = 0.4

Bias:

* b = -0.3

### Step 1: Weighted Sum

[
z = (1 \times 0.5) + (1 \times 0.4) - 0.3
]

[
z = 0.6
]

### Step 2: Apply Step Function

Since:

[
0.6 \geq 0
]

Output:

[
y = 1
]

Prediction:

**Pass**

---

# Real-World Example

### Spam Email Detection

Inputs:

* Contains "Free Money" = 1
* Unknown Sender = 1
* Trusted Domain = 0

The Perceptron combines these features.

If the score exceeds the decision boundary:

Output = Spam

Otherwise:

Output = Not Spam

---

# Why is the Perceptron Better than the MCP Neuron?

| MCP Neuron         | Perceptron                  |
| ------------------ | --------------------------- |
| Fixed weights      | Learns weights              |
| No learning        | Learns from examples        |
| Binary inputs only | Can use real-valued inputs  |
| Fixed threshold    | Adjustable weights and bias |
| Cannot improve     | Improves through training   |

---

# Advantages

* Learns automatically from data.
* Simple and efficient.
* Easy to implement.
* Fast training.
* Good for linearly separable data.

---

# Limitations

* Can solve only **linearly separable** problems.
* Cannot solve the **XOR problem**.
* Has only one layer.
* Limited capability for complex tasks.

These limitations led to the development of the **Multilayer Perceptron (MLP)**.

---

# Applications

* Spam detection
* Binary image classification
* Credit approval
* Disease prediction (Yes/No)
* Simple pattern recognition

---

# Exam Definition (2–3 Marks)

**Perceptron:**
A Perceptron is a single-layer neural network proposed by Frank Rosenblatt in 1958. It learns by adjusting its weights based on errors and is mainly used for binary classification problems.

---

# Frequently Asked Exam/Interview Questions

1. What is a Perceptron?
2. Who invented the Perceptron?
3. Explain the architecture of a Perceptron.
4. Write the mathematical model of a Perceptron.
5. List the advantages and limitations of a Perceptron.
6. Why can't a Perceptron solve the XOR problem?

---

# Must-Remember Formula

Weighted Sum:

[
z = \sum x_iw_i + b
]

Output:

[
y =
\begin{cases}
1, & z \geq 0 \
0, & z < 0
\end{cases}
]

---

# Must-Remember Points

* Proposed by **Frank Rosenblatt (1958)**.
* First trainable neural network.
* Used for binary classification.
* Learns by updating weights.
* Uses a step activation function.
* Works only for linearly separable data.
* Cannot solve XOR.

---

# Quick Revision Bullets

* Perceptron = First learning algorithm for neural networks.
* Learns by adjusting weights.
* Predicts two classes (0 or 1).
* Uses weighted sum + bias.
* Suitable for linearly separable problems.
* Cannot solve XOR.

---

# Active Learning

### Conceptual Questions

1. What is the main difference between the MCP Neuron and the Perceptron?
2. Why is the Perceptron called a learning algorithm?
3. What type of problems can a Perceptron solve?

### Practical Question

A Perceptron has:

* x₁ = 2, w₁ = 0.5
* x₂ = 3, w₂ = 0.4
* Bias = -1

1. Calculate the weighted sum (z).
2. Using the step activation function, determine the output.
3. Is the prediction class 0 or 1?

---

## Topic Connection

You've now seen the evolution:

* **MCP Neuron** → Fixed weights, no learning.
* **Thresholding Logic** → Simple decision rule.
* **Perceptron** → Learns by adjusting weights.

However, one big question remains:

**How does the Perceptron actually update its weights?**

That is answered by the **Perceptron Learning Algorithm**, which is the next topic and one of the most important algorithms in your syllabus.
