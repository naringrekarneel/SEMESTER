# Implement AND, OR and NOT Using McCulloch–Pitts Neurons — 10 Marks

## 1. Introduction

The **McCulloch–Pitts (M-P) neuron** is an early mathematical model of a biological neuron. It accepts binary inputs, calculates their weighted sum, and compares the sum with a **threshold**.

The output is:

$$
y = 
\begin{cases}
1, & \text{if weighted sum} \ge \theta\\
0, & \text{if weighted sum} < \theta
\end{cases}
$$

For the following examples, assume every connection has weight **1**, unless mentioned otherwise.

genui{"computing_binary_logic_architecture_learning_block_staging":{"type_id":"BOOLEAN_LOGIC"}}

---

# 2. AND Gate Using M-P Neuron

### Logic

The AND gate produces **1 only when both inputs are 1**.

### Architecture

```text
 A ──────(w=1)─────┐
                   │
                   ▼
                 [ Σ ] ───→ [ Threshold θ = 2 ] ───→ Y
                   ▲
 B ──────(w=1)─────┘
```

### Required threshold

$$\boxed{\theta = 2}$$

### Working

For (A=1, B=1):

$$
A + B = 1 + 1 = 2
$$

Since:

$$
2 \ge 2
$$

$$
Y = 1
$$

For any other combination, the sum is at most 1, so:

$$
Y = 0
$$

### Truth Table

| A | B | Sum | Output |
| - | - | --: | -----: |
| 0 | 0 |   0 |      0 |
| 0 | 1 |   1 |      0 |
| 1 | 0 |   1 |      0 |
| 1 | 1 |   2 |  **1** |

Therefore, an M-P neuron with **two inputs, weights = 1, and threshold = 2** implements an AND gate.

---

# 3. OR Gate Using M-P Neuron

### Logic

The OR gate produces **1 when at least one input is 1**.

### Architecture

```text
 A ──────(w=1)─────┐
                   │
                   ▼
                 [ Σ ] ───→ [ Threshold θ = 1 ] ───→ Y
                   ▲
 B ──────(w=1)─────┘
```

### Required threshold

$$\boxed{\theta = 1}$$

### Working

If (A=1,B=0):

$$
A + B = 1
$$

Since:

$$
1 \ge 1
$$

$$
Y = 1
$$

Similarly, if (A=0,B=1), the output is also 1.

### Truth Table

| A | B | Sum | Output |
| - | - | --: | -----: |
| 0 | 0 |   0 |      0 |
| 0 | 1 |   1 |  **1** |
| 1 | 0 |   1 |  **1** |
| 1 | 1 |   2 |  **1** |

Therefore, an M-P neuron with **weights = 1 and threshold = 1** implements an OR gate.

---

# 4. NOT Gate Using M-P Neuron

A NOT gate has **one input** and produces the opposite output.

$$Y = \overline{A}$$

For NOT, we use a **negative weight**.

### Architecture

```text
             (w = -1)
 A ─────────────────────→ [ Σ ] ───→ [ Threshold θ = 0 ] ───→ Y
```

### Required parameters

$$\boxed{w = -1}$$

$$\boxed{\theta = 0}$$

### Working

If (A=0):

$$
(-1)(0) = 0
$$

Since:

$$
0 \ge 0
$$

$$
Y = 1
$$

If (A=1):

$$
(-1)(1) = -1
$$

Since:

$$
-1 < 0
$$

$$
Y = 0
$$

### Truth Table

| A | Weighted Sum | Output |
| - | -----------: | -----: |
| 0 |            0 |  **1** |
| 1 |           -1 |  **0** |

Therefore, a single M-P neuron with **weight = −1 and threshold = 0** implements a NOT gate.

---

# 5. Summary of Required Thresholds

| Logic Function | Inputs | Weights | Threshold | Output                   |
| -------------- | ------ | ------- | --------: | ------------------------ |
| **AND**        | A, B   | (1,1)   |     **2** | 1 only when both are 1   |
| **OR**         | A, B   | (1,1)   |     **1** | 1 when at least one is 1 |
| **NOT**        | A      | (-1)    |     **0** | Opposite of input        |

---

# 6. Key Point

The M-P neuron implements Boolean logic by using:

$$\boxed{\text{Weighted Sum + Threshold} \rightarrow \text{Binary Output}}$$

By choosing appropriate **weights and thresholds**, a single M-P neuron can implement basic logical functions such as **AND, OR, and NOT**.

## Conclusion

McCulloch–Pitts neurons provide a simple mathematical way to implement Boolean logic. An **AND gate** requires a threshold of 2, an **OR gate** requires a threshold of 1, and a **NOT gate** can be implemented with a negative weight and threshold 0.
