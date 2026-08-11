# Sigmoid vs Tanh Activation Function — 10 Marks

## 1. Introduction

**Activation functions** determine the output of a neuron and introduce non-linearity into a neural network. Two important activation functions used in traditional neural networks are **Sigmoid** and **Tanh (Hyperbolic Tangent)**.

Both have an **S-shaped curve**, but they differ mainly in their **output range, gradient behavior, and suitability for neural network layers**.

---

## 2. Sigmoid Activation Function

The **Sigmoid** function is defined as:

[
\sigma(x)=\frac{1}{1+e^{-x}}
]

Its output lies between:

[
0 < \sigma(x) < 1
]

So, it converts any input into a value between **0 and 1**.

genui{"functions_lines_sequences_learning_block_staging":{"type_id":"GRAPHABLE_FUNCTION","content":"y=\frac{1}{1+e^{-x}}"}}

### Gradient of Sigmoid

The derivative is:

[
\sigma'(x)=\sigma(x)(1-\sigma(x))
]

The maximum gradient is:

[
\frac{1}{4}=0.25
]

Therefore, when the input is very positive or very negative, the gradient becomes very small.

This can cause the **vanishing gradient problem** during backpropagation.

---

## 3. Tanh Activation Function

The **Tanh** function is defined as:

[
\tanh(x)=\frac{e^x-e^{-x}}{e^x+e^{-x}}
]

Its output lies between:

[
-1 < \tanh(x) < 1
]

Thus, unlike sigmoid, Tanh produces both **positive and negative outputs**.

genui{"functions_lines_sequences_learning_block_staging":{"type_id":"GRAPHABLE_FUNCTION","content":"y=\tanh(x)"}}

### Gradient of Tanh

The derivative is:

[
\tanh'(x)=1-\tanh^2(x)
]

The maximum gradient is:

[
1
]

However, just like sigmoid, the gradient becomes very small when the input is highly positive or highly negative. Therefore, **Tanh can also suffer from the vanishing gradient problem**.

---

## 4. Comparison of Sigmoid and Tanh

| **Feature**                      | **Sigmoid**              | **Tanh**                        |
| -------------------------------- | ------------------------ | ------------------------------- |
| **Formula**                      | (\frac{1}{1+e^{-x}})     | (\frac{e^x-e^{-x}}{e^x+e^{-x}}) |
| **Output range**                 | (0) to (1)               | (-1) to (1)                     |
| **Zero-centered?**               | No                       | Yes                             |
| **Maximum gradient**             | 0.25                     | 1                               |
| **Gradient near extremes**       | Very small               | Very small                      |
| **Vanishing gradient**           | More pronounced          | Less pronounced than sigmoid    |
| **Output for (x=0)**             | 0.5                      | 0                               |
| **Suitable for hidden layers**   | Generally less preferred | Better than sigmoid             |
| **Binary classification output** | Very suitable            | Less commonly used              |
| **Learning speed**               | Generally slower         | Generally faster                |
| **Negative outputs**             | No                       | Yes                             |

---

## 5. Why Tanh is Often Better Than Sigmoid in Hidden Layers

The major advantage of Tanh is that it is **zero-centered**.

For example:

* Sigmoid outputs: (0.2, 0.5, 0.8)
* Tanh outputs: (-0.6, 0, 0.6)

Because Tanh produces both positive and negative values, optimization can generally proceed more efficiently than with sigmoid.

However, **both functions can suffer from vanishing gradients**, especially when inputs become very large or very small.

---

## 6. Gradient Characteristics

This is the most important part of the comparison.

### Sigmoid

[
\sigma'(x)=\sigma(x)(1-\sigma(x))
]

Maximum gradient = **0.25**.

Therefore, during repeated multiplication through many layers, gradients can become extremely small.

### Tanh

[
\tanh'(x)=1-\tanh^2(x)
]

Maximum gradient = **1**.

Therefore, Tanh generally preserves gradients better than sigmoid around its central region.

---

## 7. Applications

### Sigmoid

Sigmoid is commonly useful when the output represents a **probability between 0 and 1**, especially in the output layer of **binary classification**.

Example:

[
P(\text{student passes})=0.85
]

### Tanh

Tanh was historically used frequently in **hidden layers**, particularly in recurrent neural networks and older neural network architectures.

---

## 8. Conclusion

Both Sigmoid and Tanh are S-shaped activation functions that introduce non-linearity into neural networks. **Sigmoid has an output range of 0 to 1**, while **Tanh has a range of −1 to 1 and is zero-centered**. Tanh has a larger maximum gradient and generally performs better than sigmoid in hidden layers, although both can suffer from the **vanishing gradient problem**. In modern deep networks, **ReLU and its variants are usually preferred for hidden layers**, while sigmoid remains useful for binary classification outputs.
