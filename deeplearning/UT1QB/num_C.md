# 2-Input XOR Using a Multilayer Perceptron (MLP) — 10 Marks

## 1. Introduction

The **XOR (Exclusive OR)** function produces an output of 1 when **exactly one input is 1**. It produces 0 when both inputs are the same.

A single perceptron **cannot implement XOR** because XOR is **not linearly separable**.

An **MLP with one hidden layer** can solve XOR by combining simpler logical functions.

The key idea is:

$$
\boxed{\mathrm{XOR} = (A \lor B) \land \neg(A \land B)}
$$

---

## 2. XOR Truth Table

| A | B | XOR Output |
| - | - | ---------- |
| 0 | 0 | **0**      |
| 0 | 1 | **1**      |
| 1 | 0 | **1**      |
| 1 | 1 | **0**      |

---

# 3. MLP Architecture

We use:

* **2 input neurons:** (A, B)
* **2 hidden neurons:** (H_1, H_2)
* **1 output neuron:** (Y)

Architecture:

```text
                    Hidden Layer
                  ┌───────────────┐
 A ──────────────►│ H₁ = OR       │──────┐
                  └───────────────┘      │
                                         ▼
                                       ┌─────┐
                                       │ AND │──────► Y
                                         ▲
                  ┌───────────────┐      │
 B ──────────────►│ H₂ = NAND     │──────┘
                  └───────────────┘
```

More explicitly:

```text
              H₁
             /  \
            /    \
           /      \
          A        ──────► Y
          \      /
           \    /
            \  /
              H₂
             /  \
            /    \
           B      \
```

The hidden neurons are designed as:

$$
H_1 = A \lor B
$$

$$
H_2 = \neg(A \land B) = \mathrm{NAND}(A,B)
$$

Then:

$$
Y = H_1 \land H_2
$$

---

# 4. Weights and Thresholds

We use a **step activation function** (Heaviside-type):

$$
f(z)=
\begin{cases}
1, & z \ge \theta \\
0, & z < \theta
\end{cases}
$$

### Hidden Neuron (H_1): OR

Weights:

$$
w_{A1} = 1, \qquad w_{B1} = 1
$$

Threshold:

$$
\theta_1 = 1
$$

Therefore:

$$
H_1 = f(A + B)
$$

This produces:

$$
H_1 = A \lor B
$$

---

### Hidden Neuron (H_2): NAND

For NAND, use negative weights:

$$
w_{A2} = -1, \qquad w_{B2} = -1
$$

Threshold:

$$
\theta_2 = -1
$$

Therefore:

$$
H_2 = f(-A - B)
$$

$$
\[
\begin{aligned}
(A=B=0): &\quad \text{sum}=0 \; (\ge -1) \rightarrow H_2=1,\\
(A=1,B=0): &\quad \text{sum}=-1 \; (\ge -1) \rightarrow H_2=1,\\
(A=0,B=1): &\quad \text{sum}=-1 \; (\ge -1) \rightarrow H_2=1,\\
(A=B=1): &\quad \text{sum}=-2 \; (< -1) \rightarrow H_2=0.
\end{aligned}
\]
$$

So:

$$
H_2 = \mathrm{NAND}(A,B)
$$

---

# 5. Output Neuron

The output neuron performs:

$$
Y = H_1 \land H_2
$$

Therefore, use weights:

$$
w_{H_1Y} = 1, \qquad w_{H_2Y} = 1
$$

and threshold:

$$
\theta_Y = 2
$$

Hence:

$$
Y = f(H_1 + H_2)
$$

---

# 6. Complete Network Structure

```text
                     HIDDEN LAYER
                   ┌───────────────┐
                   │ H₁ = OR       │
              ┌───►│ w₁=1, w₂=1   │───┐
              │    │ θ₁ = 1        │   │
              │    └───────────────┘   │
              │                         │
 INPUT        │                         ▼
              │                       ┌────────┐
 A ───────────┤                       │ OUTPUT │───► Y
              │                       │  AND   │
 B ───────────┤    ┌───────────────┐  │ w=1,1  │
              └───►│ H₂ = NAND     │──│ θ = 2  │
                   │ w₁=-1,w₂=-1  │  └────────┘
                   │ θ₂ = -1       │
                   └───────────────┘
```

### Complete parameters

| Neuron | Input Weights   | Threshold |
| ------ | --------------- | --------: |
| (H_1)  | (A=1, B=1)      |     **1** |
| (H_2)  | (A=-1, B=-1)    |    **−1** |
| (Y)    | (H_1=1, H_2=1)  |     **2** |

---

# 7. Verification

| A | B | (H_1 = A OR B) | (H_2 = NAND) | (Y = H_1 AND H_2) |
| - | - | --------------: | -----------: | -----------------: |
| 0 | 0 |               0 |            1 |              **0** |
| 0 | 1 |               1 |            1 |              **1** |
| 1 | 0 |               1 |            1 |              **1** |
| 1 | 1 |               1 |            0 |              **0** |

Therefore, the final output is:

$$
\boxed{(0,\,1,\,1,\,0)}
$$

which is exactly the **XOR truth table**.

---

# 8. Why an MLP is Required

A single perceptron cannot separate the two classes of XOR using one straight-line decision boundary.

The hidden layer solves this by creating **intermediate representations**:

$$
(A, B) \longrightarrow (\mathrm{OR},\; \mathrm{NAND}) \longrightarrow \mathrm{XOR}
$$

Thus, the MLP combines multiple simple decision boundaries to create the required **non-linear decision boundary**.

---

## Conclusion

A 2-input XOR gate can be implemented using an MLP with **2 input neurons, 2 hidden neurons, and 1 output neuron**. The first hidden neuron performs OR, the second performs NAND, and the output neuron computes their AND to produce XOR.
