# Forward Pass of a 2-Layer Feedforward Neural Network — 10 Marks

## 1. Given

Inputs:

$$
x_1 = 0.6,
\quad
x_2 = 0.3
$$

Hidden-layer weights:

$$
\begin{aligned}
w_{11} &= 0.2, & w_{12} &= 0.4 \\
\end{aligned}
$$

$$
\begin{aligned}
w_{21} &= 0.5, & w_{22} &= 0.1
\end{aligned}
$$

Biases:

$$
b_1 = 0.1,\quad b_2 = 0.2
$$

Hidden-layer activation: **ReLU**

Output-layer activation: **Softmax**

---

## 2. Network Structure

We have two input neurons and two hidden neurons:

```text
                  Hidden Layer
               ┌───────────────┐
x₁ = 0.6 ─────►│ H₁            │──────► Output 1
               │ ReLU          │
               └───────────────┘
                  ▲
                  │
               ┌───────────────┐
x₂ = 0.3 ─────►│ H₂            │──────► Output 2
               │ ReLU          │
               └───────────────┘
```

---

# 3. Calculate Hidden-Layer Weighted Sums

The weighted sum for a neuron is:

$$
z = w_1 x_1 + w_2 x_2 + b
$$

### Hidden neuron 1

Using:

$$
w_{11} = 0.2, \quad w_{12} = 0.4, \quad b_1 = 0.1
$$

we get:

$$
\begin{aligned}
z_1 &= w_{11} x_1 + w_{12} x_2 + b_1 \\
&= (0.2)(0.6) + (0.4)(0.3) + 0.1 \\
&= 0.12 + 0.12 + 0.1 \\
&= 0.34
\end{aligned}
$$

\boxed{z_1 = 0.34}

---

### Hidden neuron 2

Using:

$$
w_{21} = 0.5, \quad w_{22} = 0.1, \quad b_2 = 0.2
$$

we get:

$$
\begin{aligned}
z_2 &= w_{21} x_1 + w_{22} x_2 + b_2 \\
&= (0.5)(0.6) + (0.1)(0.3) + 0.2 \\
&= 0.30 + 0.03 + 0.20 \\
&= 0.53
\end{aligned}
$$

\boxed{z_2 = 0.53}

---

# 4. Apply ReLU

The ReLU function is:

$$
\operatorname{ReLU}(z) = \max(0, z)
$$

Since both values are positive:

$$
h_1 = \operatorname{ReLU}(0.34) = 0.34
$$

$$
h_2 = \operatorname{ReLU}(0.53) = 0.53
$$

Therefore, the hidden-layer output is:

$$
H = \begin{bmatrix} 0.34 \\ 0.53 \end{bmatrix}
$$

---

# 5. Output Layer

There is an important point in the question: **Softmax requires output-layer logits/weights**, but those weights are not explicitly provided.

So, to compute a numerical Softmax output, we need to make an assumption.

The simplest interpretation is that the hidden outputs themselves are the two output logits:

$$
z_{\text{out}} = \begin{bmatrix} 0.34 \\ 0.53 \end{bmatrix}
$$

Then Softmax is applied directly to these values.

---

# 6. Apply Softmax

The Softmax function is:

$$
\operatorname{Softmax}(z_i) = \frac{e^{z_i}}{\sum_j e^{z_j}}
$$

For the first output:

$$
P_1 = \frac{e^{0.34}}{e^{0.34} + e^{0.53}}
$$

For the second output:

$$
P_2 = \frac{e^{0.53}}{e^{0.34} + e^{0.53}}
$$

Using numerical approximations:

$$
e^{0.34} \approx 1.4049, \quad e^{0.53} \approx 1.6989
$$

Therefore:

$$
P_1 = \frac{1.4049}{1.4049 + 1.6989} \approx 0.4526
$$

and:

$$
P_2 = \frac{1.6989}{1.4049 + 1.6989} \approx 0.5474
$$

---

# 7. Final Output

Therefore, the Softmax output is:

$$
\boxed{\begin{bmatrix} 0.4526 \\ 0.5474 \end{bmatrix}}
$$

or approximately:

$$
\boxed{\begin{bmatrix} 45.26\% \\ 54.74\% \end{bmatrix}}
$$

The second output has the higher probability.

---

# 8. Complete Calculation

| Step           |   Neuron 1 |   Neuron 2 |
| -------------- | ---------: | ---------: |
| Weighted sum   |     0.34   |     0.53   |
| ReLU output    |     0.34   |     0.53   |
| Softmax output | **0.4526** | **0.5474** |

### Final Answer:

$$
\boxed{\text{Output} = \begin{bmatrix} 0.4526 \\ 0.5474 \end{bmatrix}}
$$

**Note:** Strictly speaking, a complete two-layer network with a separate output layer needs **output-layer weights and biases**. Since the question doesn't provide them, the calculation above assumes the hidden-layer activations are used directly as logits for the Softmax output.
