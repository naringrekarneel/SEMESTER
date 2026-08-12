# Forward Pass of a 2-Layer Feedforward Neural Network — 10 Marks

## 1. Given

Inputs:

$$
\mathbf{x} = \begin{bmatrix} x_1 \\ x_2 \end{bmatrix} = \begin{bmatrix} 0.6 \\ 0.3 \end{bmatrix}
$$

Hidden-layer weights (arranged by hidden neuron):

$$
\begin{aligned}
\mathbf{w}_1 &= \begin{bmatrix} w_{11} \\ w_{12} \end{bmatrix} = \begin{bmatrix} 0.2 \\ 0.4 \end{bmatrix}, &\qquad
\mathbf{w}_2 &= \begin{bmatrix} w_{21} \\ w_{22} \end{bmatrix} = \begin{bmatrix} 0.5 \\ 0.1 \end{bmatrix}, \\
\mathbf{b} &= \begin{bmatrix} b_1 \\ b_2 \end{bmatrix} = \begin{bmatrix} 0.1 \\ 0.2 \end{bmatrix}
\end{aligned}
$$

Hidden-layer activation: **ReLU**

Output-layer activation: **Softmax**

---

## 2. Network Structure

Two inputs and two hidden neurons (hidden layer shown as H₁, H₂). The outputs are produced from the hidden layer and passed to softmax.

```text
    x₁ = 0.6 ──┐                Hidden Layer           Softmax
               ├─► H₁ (ReLU) ───┐                    ┌───────────┐
    x₂ = 0.3 ──┘                └─► [logit₁,logit₂] ─►│ Softmax   │──► Output
                                               (use hidden activations)  └───────────┘
```

---

# 3. Calculate Hidden-Layer Weighted Sums

Weighted sums for the hidden layer (vector form):

$$
\mathbf{z} = W^T \mathbf{x} + \mathbf{b},
$$

where (column-vector inputs):

$$
W = \begin{bmatrix} w_{11} & w_{21} \\\ w_{12} & w_{22} \end{bmatrix}, \qquad
\mathbf{x} = \begin{bmatrix} 0.6 \\ 0.3 \end{bmatrix}, \qquad
\mathbf{b} = \begin{bmatrix} 0.1 \\ 0.2 \end{bmatrix}.
$$

(We keep the component-wise calculation below for clarity.)

### Hidden neuron 1

Using

$$
w_{11} = 0.2, \quad w_{12} = 0.4, \quad b_1 = 0.1,
$$

\begin{aligned}
z_1 &= w_{11} x_1 + w_{12} x_2 + b_1 \\
    &= (0.2)(0.6) + (0.4)(0.3) + 0.1 \\
    &= 0.12 + 0.12 + 0.10 \\
    &= 0.34
\end{aligned}

\boxed{z_1 = 0.34}

---

### Hidden neuron 2

Using

$$
w_{21} = 0.5, \quad w_{22} = 0.1, \quad b_2 = 0.2,
$$

\begin{aligned}
z_2 &= w_{21} x_1 + w_{22} x_2 + b_2 \\
    &= (0.5)(0.6) + (0.1)(0.3) + 0.2 \\
    &= 0.30 + 0.03 + 0.20 \\
    &= 0.53
\end{aligned}

\boxed{z_2 = 0.53}

---

# 4. Apply ReLU

ReLU is defined as:

$$
\operatorname{ReLU}(z) = \max(0, z).
$$

Both values are positive, so

$$
h_1 = \operatorname{ReLU}(0.34) = 0.34, \qquad h_2 = \operatorname{ReLU}(0.53) = 0.53.
$$

Hidden-layer activation vector:

$$
\mathbf{h} = \begin{bmatrix} 0.34 \\ 0.53 \end{bmatrix}.
$$

---

# 5. Output Layer

The question does not provide explicit output-layer weights and biases. A minimal and common interpretation is to treat the hidden activations themselves as the logits (i.e., the vector passed into softmax):

$$
\mathbf{z}_{\text{out}} = \mathbf{h} = \begin{bmatrix} 0.34 \\ 0.53 \end{bmatrix}.
$$

We proceed with this interpretation so we can compute numerical softmax probabilities.

---

# 6. Apply Softmax

Softmax for a 2-component vector z = [z_1, z_2]^T is

$$
\operatorname{Softmax}(z)_i = \frac{e^{z_i}}{\sum_{j=1}^2 e^{z_j}}.
$$

For our values:

$$
P_1 = \frac{e^{0.34}}{e^{0.34} + e^{0.53}}, \qquad P_2 = \frac{e^{0.53}}{e^{0.34} + e^{0.53}}.
$$

Numeric approximations (rounded to 4 decimal places):

$$
e^{0.34} \approx 1.4049, \qquad e^{0.53} \approx 1.6989.
$$

Sum:

$$
1.4049 + 1.6989 = 3.1038.
$$

Therefore:

$$
P_1 = \frac{1.4049}{3.1038} \approx 0.4526, \qquad P_2 = \frac{1.6989}{3.1038} \approx 0.5474.
$$

---

# 7. Final Output

Softmax output vector:

$$
\boxed{\mathbf{P} = \begin{bmatrix} 0.4526 \\ 0.5474 \end{bmatrix}} \quad\text{(approximately)}
$$

Or in percentages:

$$
\boxed{\begin{bmatrix} 45.26\% \\ 54.74\% \end{bmatrix}}.
$$

The second output has the higher probability.

---

# 8. Complete Calculation (Summary)

| Step           | Neuron 1 | Neuron 2 |
| -------------- | -------: | -------: |
| Weighted sum   |    0.34  |    0.53  |
| ReLU output    |    0.34  |    0.53  |
| Softmax output | **0.4526** | **0.5474** |

### Final Answer:

$$
\boxed{\text{Output} = \begin{bmatrix} 0.4526 \\ 0.5474 \end{bmatrix}}
$$

**Note:** Strictly speaking, a complete two-layer network with a separate output layer requires explicit output-layer weights and biases. Since the question doesn't provide them, the computation above uses the hidden activations as logits for softmax, which is a common simplifying assumption for small illustrative examples.
