# Forward Pass of a 2-Layer Feedforward Neural Network — 10 Marks

## 1. Given

Inputs:

[
x_1=0.6,\qquad x_2=0.3
]

Hidden-layer weights:

[
w_{11}=0.2,\quad w_{12}=0.4
]

[
w_{21}=0.5,\quad w_{22}=0.1
]

Biases:

[
b_1=0.1,\qquad b_2=0.2
]

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

[
z=w_1x_1+w_2x_2+b
]

### Hidden neuron 1

Using:

[
w_{11}=0.2,\quad w_{12}=0.4,\quad b_1=0.1
]

we get:

[
z_1=(0.2)(0.6)+(0.4)(0.3)+0.1
]

[
=0.12+0.12+0.1
]

[
\boxed{z_1=0.34}
]

---

### Hidden neuron 2

Using:

[
w_{21}=0.5,\quad w_{22}=0.1,\quad b_2=0.2
]

we get:

[
z_2=(0.5)(0.6)+(0.1)(0.3)+0.2
]

[
=0.30+0.03+0.20
]

[
\boxed{z_2=0.53}
]

---

# 4. Apply ReLU

The ReLU function is:

[
ReLU(z)=\max(0,z)
]

Since both values are positive:

[
h_1=ReLU(0.34)=0.34
]

[
h_2=ReLU(0.53)=0.53
]

Therefore, the hidden-layer output is:

[
\boxed{H=[0.34,;0.53]}
]

---

# 5. Output Layer

There is an important point in the question: **Softmax requires output-layer logits/weights**, but those weights are not explicitly provided.

So, to compute a numerical Softmax output, we need to make an assumption.

The simplest interpretation is that the hidden outputs themselves are the two output logits:

[
z_{out}=[0.34,;0.53]
]

Then Softmax is applied directly to these values.

---

# 6. Apply Softmax

The Softmax function is:

[
Softmax(z_i)=\frac{e^{z_i}}{\sum_j e^{z_j}}
]

For the first output:

[
P_1=\frac{e^{0.34}}{e^{0.34}+e^{0.53}}
]

For the second output:

[
P_2=\frac{e^{0.53}}{e^{0.34}+e^{0.53}}
]

Using:

[
e^{0.34}\approx1.4049
]

[
e^{0.53}\approx1.6989
]

Therefore:

[
P_1=\frac{1.4049}{1.4049+1.6989}
]

[
P_1\approx0.4526
]

And:

[
P_2=\frac{1.6989}{1.4049+1.6989}
]

[
P_2\approx0.5474
]

---

# 7. Final Output

Therefore, the Softmax output is:

[
\boxed{
[0.4526,;0.5474]
}
]

or approximately:

[
\boxed{[45.26%,;54.74%]}
]

The second output has the higher probability.

---

# 8. Complete Calculation

| Step           |   Neuron 1 |   Neuron 2 |
| -------------- | ---------: | ---------: |
| Weighted sum   |     (0.34) |     (0.53) |
| ReLU output    |     (0.34) |     (0.53) |
| Softmax output | **0.4526** | **0.5474** |

### Final Answer:

[
\boxed{\text{Output}=[0.4526,;0.5474]}
]

**Note:** Strictly speaking, a complete two-layer network with a separate output layer needs **output-layer weights and biases**. Since the question doesn't provide them, the calculation above assumes the two ReLU outputs are directly used as the two Softmax logits.
