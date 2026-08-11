# Topic 3: Idea of Computational Units (Artificial Neuron)

Now that we understand how a **biological neuron** works, let's see how scientists converted it into a **mathematical model** that computers can understand. This model is called a **Computational Unit** or **Artificial Neuron**.

---

# ELI5 (Explain Like I'm 5)

Imagine a teacher deciding whether to pass a student.

The teacher considers:

* Attendance
* Assignment Marks
* Exam Marks

Not every factor is equally important.

For example:

* Attendance → Less important
* Assignment → Moderately important
* Exam → Most important

The teacher gives each factor a different importance, adds them together, and makes a decision.

An **artificial neuron** works exactly the same way.

---

# What is a Computational Unit?

A **Computational Unit (Artificial Neuron)** is the basic building block of an Artificial Neural Network (ANN). It receives multiple inputs, multiplies each input by a weight, adds them together, applies an activation function, and produces an output.

---

# Structure of an Artificial Neuron

```text
Inputs (x₁, x₂, x₃)
        │
        ▼
Multiply by Weights (w₁, w₂, w₃)
        │
        ▼
Weighted Sum + Bias
        │
        ▼
Activation Function
        │
        ▼
      Output (y)
```

---

# Components of an Artificial Neuron

| Component           | Meaning                                             |
| ------------------- | --------------------------------------------------- |
| Input (x)           | Information given to the neuron                     |
| Weight (w)          | Importance of each input                            |
| Bias (b)            | Extra value that helps shift the output             |
| Weighted Sum        | Sum of all weighted inputs                          |
| Activation Function | Decides whether the neuron should produce an output |
| Output (y)          | Final prediction of the neuron                      |

---

# Mathematical Representation

The neuron first calculates the weighted sum:

[
z = x_1w_1 + x_2w_2 + x_3w_3 + b
]

Then applies an activation function:

[
y = f(z)
]

Where:

* **x** = Inputs
* **w** = Weights
* **b** = Bias
* **f()** = Activation Function
* **y** = Output

This is one of the **most important formulas** in Deep Learning.

---

# Why Do We Need Weights?

Weights tell the neuron how important each input is.

Example:

Predicting whether a student will pass.

| Input      | Weight |
| ---------- | ------ |
| Attendance | 0.2    |
| Assignment | 0.3    |
| Exam Marks | 0.8    |

Here, exam marks have the greatest influence on the final decision.

---

# What is Bias?

Bias is an extra value added before applying the activation function.

Think of bias as a "starting point" or "adjustment knob" that helps the neuron make better decisions.

Without bias, the neuron becomes less flexible and may not learn certain patterns.

---

# Step-by-Step Worked Example

Suppose:

Inputs:

* x₁ = 2
* x₂ = 4
* x₃ = 3

Weights:

* w₁ = 0.5
* w₂ = 0.2
* w₃ = 0.4

Bias:

* b = 1

### Step 1: Calculate Weighted Sum

[
z = (2 \times 0.5) + (4 \times 0.2) + (3 \times 0.4) + 1
]

[
z = 1 + 0.8 + 1.2 + 1
]

[
z = 4
]

### Step 2: Apply Activation Function

Assume a simple threshold activation:

* If z ≥ 3 → Output = 1
* Otherwise → Output = 0

Since:

[
4 \geq 3
]

Output:

[
y = 1
]

The neuron "fires."

---

# Biological Neuron vs Artificial Neuron

| Biological Neuron | Artificial Neuron   |
| ----------------- | ------------------- |
| Dendrites         | Inputs              |
| Synapses          | Weights             |
| Cell Body         | Weighted Sum        |
| Threshold         | Activation Function |
| Axon              | Output              |

Scientists copied this biological process to create Artificial Neural Networks.

---

# Real-World Example

Suppose a bank wants to approve a loan.

Inputs:

* Salary
* Credit Score
* Existing Loan
* Age

The neuron assigns different weights to each input.

Example:

* Salary → High weight
* Credit Score → High weight
* Age → Low weight

After calculating the weighted sum and applying the activation function, the output is:

* 1 → Loan Approved
* 0 → Loan Rejected

---

# Why is the Artificial Neuron Important?

Every deep learning model is built using millions (or even billions) of artificial neurons connected together.

Examples:

* Face Recognition
* ChatGPT
* Self-driving Cars
* Voice Assistants
* Medical Diagnosis

All start with this simple computational unit.

---

# Exam Definition (2–3 Marks)

**Artificial Neuron (Computational Unit):**

An artificial neuron is a mathematical model inspired by the biological neuron. It receives multiple inputs, multiplies them by weights, adds a bias, applies an activation function, and produces an output.

---

# Frequently Asked Exam/Interview Questions

1. What is a computational unit?
2. Explain the architecture of an artificial neuron.
3. What is the role of weights?
4. What is the purpose of bias?
5. Write the mathematical model of an artificial neuron.
6. Differentiate between biological and artificial neurons.

---

# Must-Remember Formula

Weighted Sum:

[
z = \sum (x_i w_i) + b
]

Output:

[
y = f(z)
]

These two equations are the foundation of all neural networks.

---

# Must-Remember Points

* Artificial neuron is inspired by the biological neuron.
* Inputs represent information.
* Weights represent importance.
* Bias improves learning flexibility.
* Activation function decides the output.
* Millions of artificial neurons together form a Deep Neural Network.

---

# Quick Revision Bullets

* Artificial neuron = basic unit of ANN.
* Components: Input, Weight, Bias, Activation Function, Output.
* Weighted Sum = Σ(x × w) + b.
* Activation function decides whether the neuron produces an output.
* Weights are learned during training.
* Bias shifts the decision boundary.

---

# Active Learning

### Conceptual Questions

1. What is the purpose of weights in an artificial neuron?
2. Why do we add a bias term?
3. Write the mathematical equation of an artificial neuron.

### Practical Question

A neuron has:

* x₁ = 3, w₁ = 0.4
* x₂ = 5, w₂ = 0.6
* Bias = 1

Calculate the weighted sum (z). If the activation function outputs **1** when (z \geq 5), what will be the output?

**Next Topic:** **History of Deep Learning**, where we'll trace the evolution of neural networks from the **McCulloch-Pitts Neuron (1943)** to today's modern deep learning models like Transformers.
