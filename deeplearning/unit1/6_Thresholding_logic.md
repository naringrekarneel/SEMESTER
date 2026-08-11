# Topic 6: Thresholding Logic

Thresholding Logic is the **decision-making mechanism** used by the **McCulloch-Pitts Neuron** and early neural network models. It determines **whether a neuron should fire (output = 1) or not (output = 0)**.

---

# ELI5 (Explain Like I'm 5)

Imagine a school has a rule:

> **You need at least 40 marks to pass.**

* Marks = 75 → Pass ✅
* Marks = 40 → Pass ✅
* Marks = 39 → Fail ❌

Here, **40 is the threshold**.

A neuron works in exactly the same way.

If the total input is greater than or equal to the threshold, it produces an output. Otherwise, it remains inactive.

---

# What is Thresholding Logic?

**Thresholding Logic** is a rule that compares the weighted sum (or sum of inputs) with a predefined threshold value.

* If the sum is **greater than or equal to the threshold**, the neuron fires (Output = 1).
* If the sum is **less than the threshold**, the neuron does not fire (Output = 0).

---

# Mathematical Formula

Let,

* Sum of inputs = **S**
* Threshold = **θ (Theta)**

The output is:

[
y =
\begin{cases}
1, & \text{if } S \geq \theta \
0, & \text{if } S < \theta
\end{cases}
]

This is one of the simplest activation rules used in neural networks.

---

# Working of Thresholding Logic

```text
Inputs
   ↓
Calculate Sum
   ↓
Compare with Threshold (θ)
   ↓
Decision
   ↓
Output (0 or 1)
```

---

# Worked Example 1

Inputs:

* x₁ = 1
* x₂ = 1

Threshold:

θ = 2

### Step 1: Calculate Sum

[
S = 1 + 1 = 2
]

### Step 2: Compare

[
2 \geq 2
]

Output = **1**

The neuron fires.

---

# Worked Example 2

Inputs:

* x₁ = 1
* x₂ = 0

Threshold:

θ = 2

### Step 1

[
S = 1 + 0 = 1
]

### Step 2

[
1 < 2
]

Output = **0**

The neuron does not fire.

---

# Effect of Different Threshold Values

Suppose the input sum is always **3**.

| Threshold (θ) | Output |
| ------------- | ------ |
| 1             | 1      |
| 2             | 1      |
| 3             | 1      |
| 4             | 0      |
| 5             | 0      |

### Observation

* **Lower threshold** → Easier for the neuron to fire.
* **Higher threshold** → Harder for the neuron to fire.

---

# Threshold in Everyday Life

### Example 1: College Attendance

Rule:

Minimum attendance = **75%**

* Attendance = 80% → Allowed ✅
* Attendance = 74% → Not Allowed ❌

Here, **75% is the threshold**.

---

### Example 2: ATM PIN

* Correct PIN → Access Granted.
* Wrong PIN → Access Denied.

The system follows a decision rule, similar to threshold-based logic.

---

### Example 3: Loan Approval

A bank may approve a loan only if a customer's credit score is **700 or above**.

* Credit Score = 750 → Approved.
* Credit Score = 650 → Rejected.

Again, **700 acts as the threshold**.

---

# Thresholding Logic in Logic Gates

## AND Gate

Threshold = 2

| x₁ | x₂ | Sum | Output |
| -- | -- | --- | ------ |
| 0  | 0  | 0   | 0      |
| 0  | 1  | 1   | 0      |
| 1  | 0  | 1   | 0      |
| 1  | 1  | 2   | 1      |

---

## OR Gate

Threshold = 1

| x₁ | x₂ | Sum | Output |
| -- | -- | --- | ------ |
| 0  | 0  | 0   | 0      |
| 0  | 1  | 1   | 1      |
| 1  | 0  | 1   | 1      |
| 1  | 1  | 2   | 1      |

---

# Advantages

* Very simple to understand.
* Easy to implement.
* Fast computation.
* Suitable for binary decision-making.
* Forms the basis of early neural network models.

---

# Limitations

* Produces only binary outputs (0 or 1).
* Cannot represent probabilities.
* Not suitable for complex problems.
* Cannot learn automatically.
* Replaced by modern activation functions like Sigmoid, ReLU, and Tanh in deep learning.

---

# Threshold vs Activation Function

| Threshold Logic        | Modern Activation Functions                         |
| ---------------------- | --------------------------------------------------- |
| Output is only 0 or 1  | Output can be any value (depending on the function) |
| Hard decision boundary | Smooth decision boundary                            |
| No learning capability | Supports gradient-based learning                    |
| Used in MCP Neuron     | Used in modern neural networks                      |

---

# Exam Definition (2–3 Marks)

**Thresholding Logic:**
Thresholding Logic is a decision-making process in which the sum of the inputs is compared with a threshold value. If the sum is greater than or equal to the threshold, the neuron produces an output of 1; otherwise, it produces an output of 0.

---

# Frequently Asked Exam/Interview Questions

1. What is Thresholding Logic?
2. Explain the working of Thresholding Logic with an example.
3. Write the mathematical formula for Thresholding Logic.
4. Differentiate between Thresholding Logic and Activation Functions.
5. How does changing the threshold affect the output?

---

# Must-Remember Points

* Threshold is the minimum value required for a neuron to fire.
* Output = 1 if Sum ≥ Threshold.
* Output = 0 if Sum < Threshold.
* Lower threshold → Easier activation.
* Higher threshold → Harder activation.
* Thresholding Logic was mainly used in early neural network models.

---

# Quick Revision Bullets

* Threshold = Decision boundary.
* Compare sum of inputs with threshold.
* Sum ≥ Threshold → Output = 1.
* Sum < Threshold → Output = 0.
* Used in MCP Neuron and logic gates.
* Modern neural networks use activation functions instead.

---

# Active Learning

### Conceptual Questions

1. What is the purpose of a threshold in a neuron?
2. How does increasing the threshold affect the neuron's output?
3. Why is Thresholding Logic rarely used in modern deep learning?

### Practical Question

A neuron receives the following binary inputs:

* x₁ = 1
* x₂ = 1
* x₃ = 0

The threshold is **θ = 3**.

1. Calculate the sum of inputs.
2. Determine the output.
3. What would the output be if the threshold were changed to **θ = 2**?

---

## Topic Connection

So far you've learned:

* **Biological Neuron** → How the human brain processes information.
* **Artificial Neuron** → Mathematical model inspired by biology.
* **McCulloch-Pitts Neuron** → First artificial neuron.
* **Thresholding Logic** → Decision rule used by the MCP neuron.

The next step is to make the neuron **learn from data** instead of using fixed rules.

**Next Topic:** **Perceptron**, the first trainable neural network proposed by Frank Rosenblatt in 1958.
