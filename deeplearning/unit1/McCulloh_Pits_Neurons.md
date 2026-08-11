# Topic 5: McCulloch-Pitts (MCP) Neuron

The **McCulloch-Pitts (MCP) Neuron** is the **first mathematical model of an artificial neuron**, proposed by **Warren McCulloch** and **Walter Pitts** in **1943**. It is considered the foundation of Artificial Neural Networks.

---

# ELI5 (Explain Like I'm 5)

Imagine a room with a light bulb.

The bulb turns **ON** only if enough switches are ON.

Example:

* Switch A = ON
* Switch B = ON

If both are ON, the bulb glows.

If only one is ON, the bulb stays OFF.

The MCP neuron works in the same way.

It checks the inputs and decides:

* **Fire (1)**
* **Don't Fire (0)**

---

# Definition

The **McCulloch-Pitts Neuron** is a simple binary neuron that receives binary inputs (0 or 1), calculates their sum, compares it with a threshold, and produces a binary output (0 or 1).

---

# Characteristics of MCP Neuron

* Accepts only **binary inputs (0 or 1)**.
* Produces only **binary output (0 or 1)**.
* Uses a **threshold value**.
* Does **not learn** from data.
* Performs logical operations such as **AND, OR, and NOT**.

---

# Structure of MCP Neuron

```text
      x₁ ----\
              \
      x₂ ------> [ Σ ] ---> Compare with Threshold ---> Output
              /
      x₃ ----/
```

Where:

* **x₁, x₂, x₃** = Inputs
* **Σ** = Sum of inputs
* **Threshold (θ)** = Decision value
* **Output** = 0 or 1

---

# Working of MCP Neuron

### Step 1

Receive binary inputs.

Example:

x₁ = 1

x₂ = 0

---

### Step 2

Add the inputs.

[
\text{Sum} = x_1 + x_2
]

---

### Step 3

Compare with threshold.

If

[
\text{Sum} \geq \theta
]

Output = 1

Otherwise

Output = 0

---

# Mathematical Model

[
y =
\begin{cases}
1, & \text{if } \sum x_i \geq \theta \
0, & \text{otherwise}
\end{cases}
]

Where:

* **θ (Theta)** = Threshold
* **y** = Output

---

# Worked Example 1

Inputs:

* x₁ = 1
* x₂ = 1

Threshold:

θ = 2

### Step 1

Sum:

[
1 + 1 = 2
]

### Step 2

Compare:

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

Sum:

[
1 + 0 = 1
]

### Step 2

Compare:

[
1 < 2
]

Output = **0**

The neuron does not fire.

---

# Logical Operations Using MCP Neuron

## 1. AND Gate

Condition:

Output is **1 only when all inputs are 1**.

Threshold = 2

| x₁ | x₂ | Sum | Output |
| -- | -- | --- | ------ |
| 0  | 0  | 0   | 0      |
| 0  | 1  | 1   | 0      |
| 1  | 0  | 1   | 0      |
| 1  | 1  | 2   | 1      |

---

## 2. OR Gate

Condition:

Output is **1 if at least one input is 1**.

Threshold = 1

| x₁ | x₂ | Sum | Output |
| -- | -- | --- | ------ |
| 0  | 0  | 0   | 0      |
| 0  | 1  | 1   | 1      |
| 1  | 0  | 1   | 1      |
| 1  | 1  | 2   | 1      |

---

## 3. NOT Gate

The NOT gate has only one input.

| x | Output |
| - | ------ |
| 0 | 1      |
| 1 | 0      |

The MCP neuron can implement a NOT gate by using an inhibitory connection (or an equivalent negative-weight idea in later models).

---

# Real-World Analogy

Imagine a security system.

Inputs:

* Fingerprint matched = 1
* Face recognized = 1

Threshold = 2

If both conditions are satisfied:

Door opens (Output = 1)

Otherwise:

Door remains locked (Output = 0)

---

# Advantages

* Very simple mathematical model.
* Easy to understand.
* Introduced the concept of artificial neurons.
* Can implement basic logical operations.

---

# Limitations

* Accepts only binary inputs.
* Produces only binary outputs.
* Cannot learn from data.
* Cannot solve complex problems.
* Cannot solve the XOR problem.

These limitations later led to the development of the **Perceptron**.

---

# MCP Neuron vs Biological Neuron

| Biological Neuron     | MCP Neuron                     |
| --------------------- | ------------------------------ |
| Receives signals      | Receives binary inputs         |
| Processes signals     | Adds inputs                    |
| Fires after threshold | Outputs 1 after threshold      |
| Very complex          | Very simple mathematical model |

---

# Exam Definition (2–3 Marks)

**McCulloch-Pitts Neuron:**
The McCulloch-Pitts neuron is the first artificial neuron model proposed in 1943. It accepts binary inputs, compares their sum with a threshold value, and produces a binary output. It is capable of implementing basic logical operations such as AND, OR, and NOT.

---

# Frequently Asked Exam/Interview Questions

1. What is the McCulloch-Pitts neuron?
2. Explain the working of the MCP neuron.
3. Draw the architecture of the MCP neuron.
4. Write the mathematical model of the MCP neuron.
5. Explain how the MCP neuron implements the AND gate.
6. List the limitations of the MCP neuron.

---

# Must-Remember Points

* Proposed by **McCulloch & Pitts (1943)**.
* First artificial neuron model.
* Binary inputs and binary outputs.
* Uses a threshold for decision-making.
* No learning capability.
* Performs AND, OR, and NOT logic.
* Cannot solve XOR.

---

# Quick Revision Bullets

* MCP = First artificial neuron.
* Inputs are only 0 or 1.
* Output is only 0 or 1.
* Uses a threshold.
* Implements basic logic gates.
* Cannot learn or solve complex problems.

---

# Active Learning

### Conceptual Questions

1. Why is the McCulloch-Pitts neuron considered the foundation of neural networks?
2. What are the main limitations of the MCP neuron?
3. Why can't the MCP neuron learn from data?

### Practical Question

An MCP neuron has:

* Inputs: x₁ = 1, x₂ = 1, x₃ = 0
* Threshold (θ) = 2

1. Calculate the sum of inputs.
2. Determine the output.
3. Would the output change if the threshold were increased to 3?

**Next Topic:** **Thresholding Logic**, where you'll learn how neurons make decisions using threshold values and how different threshold settings affect the output.
