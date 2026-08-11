# Backpropagation Algorithm for a Feedforward Neural Network — 10 Marks

## 1. Introduction

**Backpropagation** is a supervised learning algorithm used to train **feedforward neural networks**. It calculates the gradient of the loss function with respect to each weight by propagating the error **backward from the output layer toward the input layer**.

The gradients are calculated using the **chain rule of differentiation**, and the weights are then updated using **gradient descent**.

---

## 2. Feedforward Neural Network

Consider a network with:

* Input layer
* One hidden layer
* Output layer

Let:

* (x) = input vector
* (W_1,b_1) = weights and bias of hidden layer
* (W_2,b_2) = weights and bias of output layer
* (f) = hidden-layer activation
* (g) = output activation
* (y) = actual output
* (\hat y) = predicted output

The structure is:

```text
Input → Hidden Layer → Output Layer
  x         h              ŷ
            ↑
         W₁, b₁
                         ↑
                      W₂, b₂
```

---

# 3. Forward Propagation

First, the input is propagated forward.

### Hidden layer

[
z_h=W_1x+b_1
]

Apply activation:

[
h=f(z_h)
]

### Output layer

[
z_o=W_2h+b_2
]

Apply activation:

[
\hat y=g(z_o)
]

Thus:

[
x\rightarrow z_h\rightarrow h\rightarrow z_o\rightarrow\hat y
]

---

# 4. Calculate the Loss

Assume Mean Squared Error for a single training example:

[
L=\frac{1}{2}(y-\hat y)^2
]

The objective is to minimize (L).

The derivative with respect to the predicted output is:

[
\frac{\partial L}{\partial\hat y}=\hat y-y
]

---

# 5. Chain Rule in Backpropagation

The **chain rule** allows us to calculate how much a particular weight contributes to the final error.

For an output-layer weight (W_2):

[
\frac{\partial L}{\partial W_2}
===============================

\frac{\partial L}{\partial\hat y}
\frac{\partial\hat y}{\partial z_o}
\frac{\partial z_o}{\partial W_2}
]

genui{"functions_lines_sequences_learning_block_staging":{"type_id":"GRAPHABLE_FUNCTION","content":"y=\frac{1}{1+e^{-x}}"}}

Since:

[
\frac{\partial L}{\partial\hat y}=\hat y-y
]

and:

[
\frac{\partial\hat y}{\partial z_o}=g'(z_o)
]

we define the output error term:

[
\boxed{\delta_o=(\hat y-y)g'(z_o)}
]

Therefore:

[
\boxed{
\frac{\partial L}{\partial W_2}
===============================

\delta_oh^T
}
]

---

# 6. Gradient for Hidden Layer

Now the error must be propagated from the output layer back to the hidden layer.

Using the chain rule:

[
\frac{\partial L}{\partial W_1}
===============================

\frac{\partial L}{\partial\hat y}
\frac{\partial\hat y}{\partial z_o}
\frac{\partial z_o}{\partial h}
\frac{\partial h}{\partial z_h}
\frac{\partial z_h}{\partial W_1}
]

The hidden-layer error is:

[
\boxed{
\delta_h=(W_2^T\delta_o)\odot f'(z_h)
}
]

where:

[
\odot
]

represents **element-wise multiplication**.

Therefore:

[
\boxed{
\frac{\partial L}{\partial W_1}
===============================

\delta_hx^T
}
]

This is the key idea of backpropagation: **the error at a layer depends on the error from the layer ahead of it multiplied by the local derivative.**

---

# 7. Weight Update Using Gradient Descent

Once gradients are calculated, weights are updated using:

[
W^{new}=W-\eta\frac{\partial L}{\partial W}
]

where (\eta) is the **learning rate**.

### Output-layer weights

[
\boxed{
W_2\leftarrow W_2-\eta\delta_oh^T
}
]

### Hidden-layer weights

[
\boxed{
W_1\leftarrow W_1-\eta\delta_hx^T
}
]

Biases are updated as:

[
\boxed{b_2\leftarrow b_2-\eta\delta_o}
]

[
\boxed{b_1\leftarrow b_1-\eta\delta_h}
]

---

# 8. Complete Mathematical Formulation

The complete algorithm can be summarized as follows:

### Forward pass

[
z_h=W_1x+b_1
]

[
h=f(z_h)
]

[
z_o=W_2h+b_2
]

[
\hat y=g(z_o)
]

### Loss

[
L=\frac12(y-\hat y)^2
]

### Backward pass

[
\delta_o=(\hat y-y)g'(z_o)
]

[
\delta_h=(W_2^T\delta_o)\odot f'(z_h)
]

### Updates

[
W_2\leftarrow W_2-\eta\delta_oh^T
]

[
W_1\leftarrow W_1-\eta\delta_hx^T
]

[
b_2\leftarrow b_2-\eta\delta_o
]

[
b_1\leftarrow b_1-\eta\delta_h
]

---

# 9. Backpropagation Flow

```text
                 FORWARD
                    ↓
Input → Hidden → Output → Prediction
                           ↓
                         Loss
                           ↓
                 BACKWARD PROPAGATION
                           ↓
                    Output Gradient
                           ↓
                    Hidden Gradient
                           ↓
                    Weight Updates
```

The important relationship is:

[
\boxed{
\text{Gradient}
===============

\text{Error}
\times
\text{Local Derivative}
}
]

The chain rule connects these derivatives across all layers.

---

## 10. Conclusion

Backpropagation computes the gradient of the loss function with respect to every network parameter by applying the **chain rule from the output layer backward**. The output error is first calculated, then propagated to the hidden layers using the weights and activation derivatives. Finally, **gradient descent** updates the weights and biases to reduce the loss. Repeating this process over many training examples and epochs allows the feedforward neural network to learn the desired mapping.
