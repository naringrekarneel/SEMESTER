# L1 Regularization, L2 Regularization and Dropout — 10 Marks

## 1. Introduction

**Regularization** is used in neural networks to reduce **overfitting** by discouraging the model from becoming unnecessarily complex.

Three important techniques are:

1. **L1 Regularization**
2. **L2 Regularization**
3. **Dropout**

L1 and L2 directly modify the **loss function and weight updates**, while Dropout randomly removes neurons during training.

---

# 2. L1 Regularization

## Definition

L1 regularization adds the **absolute values of weights** to the original loss function.

The modified loss is:

[
\boxed{
L_{L1}=L+\lambda\sum_i|w_i|
}
]

where:

* (L) = original loss
* (w_i) = model weights
* (\lambda) = regularization strength

A larger (\lambda) produces stronger regularization.

---

## Weight Update

Without regularization:

[
w_i\leftarrow w_i-\eta\frac{\partial L}{\partial w_i}
]

With L1 regularization:

[
\boxed{
w_i\leftarrow
w_i-\eta
\left(
\frac{\partial L}{\partial w_i}
+\lambda,\text{sign}(w_i)
\right)
}
]

where:

[
\text{sign}(w)=
\begin{cases}
+1 & w>0\
-1 & w<0
\end{cases}
]

At (w=0), the absolute-value function is not differentiable; in practice, a **subgradient** is used.

---

# 3. Why L1 Produces Sparse Parameters

This is the most important point.

The L1 penalty is:

[
\lambda|w|
]

Its gradient has approximately constant magnitude:

[
\lambda,\text{sign}(w)
]

Therefore, L1 continuously pushes small weights **toward exactly zero**.

For example:

[
[0.8,;0.03,;-0.02,;0.7]
]

may become:

[
[0.8,;0,;0,;0.7]
]

So many parameters become exactly zero.

Therefore:

[
\boxed{\text{L1 regularization} \Rightarrow \text{Sparse weights}}
]

### Intuition

L1 effectively tells the network:

> "Use only the parameters that are really useful."

This can also perform a form of **feature selection**, because unimportant features may receive zero weights.

---

# 4. L2 Regularization

## Definition

L2 regularization adds the **squared values of weights** to the loss function.

[
\boxed{
L_{L2}=L+\frac{\lambda}{2}\sum_iw_i^2
}
]

The factor (1/2) is commonly included because it makes differentiation simpler.

---

## Weight Update

Differentiate the regularization term:

[
\frac{\partial}{\partial w_i}
\left(\frac{\lambda}{2}w_i^2\right)
===================================

\lambda w_i
]

Therefore:

[
\boxed{
w_i\leftarrow
w_i-\eta
\left(
\frac{\partial L}{\partial w_i}
+\lambda w_i
\right)
}
]

Rearranging:

[
w_i\leftarrow
(1-\eta\lambda)w_i
-\eta\frac{\partial L}{\partial w_i}
]

Thus, L2 continuously **shrinks weights toward zero**.

---

# 5. Difference Between L1 and L2

| Feature           | L1                              | L2                       |   |                             |
| ----------------- | ------------------------------- | ------------------------ | - | --------------------------- |
| Penalty           | (\lambda\sum                    | w                        | ) | (\frac{\lambda}{2}\sum w^2) |
| Gradient          | (\lambda,sign(w))               | (\lambda w)              |   |                             |
| Effect            | Pushes weights toward exactly 0 | Shrinks weights toward 0 |   |                             |
| Sparse weights    | **Yes**                         | Usually no               |   |                             |
| Feature selection | Possible                        | Less direct              |   |                             |
| Large weights     | Strongly penalized              | Penalized strongly       |   |                             |

---

# 6. Dropout

## Definition

**Dropout** is a regularization technique in which neurons are randomly deactivated during training.

For example:

```text
Before Dropout:

● ─── ● ─── ● ─── ●
     ● ─── ● ─── ●

After Dropout:

● ─── ✕ ─── ● ─── ✕
     ● ─── ✕ ─── ●
```

Each neuron is randomly dropped with probability (p).

Therefore, it does **not directly add a penalty term** to the loss function like L1 or L2.

---

# 7. Mathematical Formulation of Dropout

Let (h_i) be the activation of a neuron.

A random mask (m_i) is generated:

[
m_i\sim Bernoulli(1-p)
]

Using inverted dropout:

[
\boxed{
\tilde h_i=\frac{m_i h_i}{1-p}
}
]

The scaling factor keeps the expected activation approximately unchanged.

The network then calculates the loss using the modified activations:

[
\boxed{
L_{dropout}=L(y,f(x;m))
}
]

where (m) represents the random dropout mask.

---

# 8. Effect of Dropout on Weight Updates

During each training iteration:

1. Randomly select neurons to deactivate.
2. Perform forward propagation using the remaining neurons.
3. Calculate loss.
4. Perform backpropagation.
5. Update the weights.

Weights connected to dropped neurons receive **no gradient through those dropped connections for that particular iteration**.

On the next iteration, a different dropout mask may be selected.

Thus, the network effectively trains many different subnetworks.

---

# 9. Why Dropout Reduces Overfitting

Without dropout:

```text
Network → may rely heavily on a few neurons
```

With dropout:

```text
Network → cannot depend too heavily on specific neurons
```

Therefore, neurons are encouraged to learn **more useful and distributed features**.

Dropout can be viewed approximately as training a large collection of related subnetworks and sharing their weights.

---

# 10. Overall Comparison

| Property               | **L1**                     | **L2**           | **Dropout**                  |                        |                       |
| ---------------------- | -------------------------- | ---------------- | ---------------------------- | ---------------------- | --------------------- |
| Modifies loss directly | Yes                        | Yes              | Not as an explicit penalty   |                        |                       |
| Penalty                | (\lambda                   | w                | )                            | (\frac{\lambda}{2}w^2) | Random neuron masking |
| Weight effect          | Drives some to zero        | Shrinks weights  | Randomly removes activations |                        |                       |
| Sparse representation  | **Yes**                    | Usually no       | No                           |                        |                       |
| Main purpose           | Sparsity/feature selection | Weight shrinkage | Prevent co-adaptation        |                        |                       |
| Applied during         | Training                   | Training         | Training                     |                        |                       |
| During inference       | Normal network             | Normal network   | Dropout disabled             |                        |                       |

---

# 11. Key Mathematical Summary

### L1

[
\boxed{
L'=L+\lambda\sum_i|w_i|
}
]

[
\boxed{
w_i\leftarrow w_i-\eta
\left(
\frac{\partial L}{\partial w_i}
+\lambda sign(w_i)
\right)
}
]

### L2

[
\boxed{
L'=L+\frac{\lambda}{2}\sum_iw_i^2
}
]

[
\boxed{
w_i\leftarrow w_i-\eta
\left(
\frac{\partial L}{\partial w_i}
+\lambda w_i
\right)
}
]

### Dropout

[
\boxed{
m_i\sim Bernoulli(1-p)
}
]

[
\boxed{
\tilde h_i=\frac{m_i h_i}{1-p}
}
]

---

## Conclusion

**L1 regularization** adds the absolute value of weights to the loss and tends to drive many weights exactly to zero, producing **sparse parameter representations**. **L2 regularization** adds squared weights to the loss and smoothly shrinks weights toward zero without usually making them exactly zero. **Dropout** randomly deactivates neurons during training, preventing excessive dependence on individual neurons and reducing overfitting. Thus, L1 promotes **sparsity**, L2 promotes **small weights**, and Dropout promotes **robust feature learning**.
