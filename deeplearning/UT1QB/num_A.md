For a **10-mark answer**, focus on the derivation from **forward propagation → MSE → chain rule → output-layer update → hidden-layer update**.

# Backpropagation Weight Update Equations for a Single Hidden-Layer Neural Network

## 1. Introduction

**Backpropagation** is an algorithm used to train neural networks by calculating how much each weight contributes to the error and then updating the weights to reduce that error.

Consider a feedforward neural network with:

* Input layer
* One hidden layer
* Output layer
* Differentiable activation functions
* **Mean Squared Error (MSE)** as the loss function

The weights are updated using **gradient descent**.

---

# 2. Network Structure

Consider the following network:

```text
Input Layer          Hidden Layer          Output Layer

 x₁ ───────┐
           ├──────→ h₁ ───────┐
 x₂ ───────┤                  │
           ├──────→ h₂ ───────┤──────→ ŷ
 x₃ ───────┘                  │
                              │
             W₁               W₂
```

Let:

* X = input
* W_1 = weights between input and hidden layer
* b_1 = hidden-layer bias
* W_2 = weights between hidden and output layer
* b_2 = output-layer bias
* f = hidden-layer activation function
* g = output-layer activation function
* y = actual output
* \hat{y} = predicted output

---

# 3. Forward Propagation

### Step 1: Hidden-layer input

$$
z_h = W_1 X + b_1
$$

### Step 2: Hidden-layer output

$$
h = f(z_h)
$$

### Step 3: Output-layer input

$$
z_o = W_2 h + b_2
$$

### Step 4: Predicted output

$$
\hat{y} = g(z_o)
$$

Thus, information flows:

$$
X \rightarrow z_h \rightarrow h \rightarrow z_o \rightarrow \hat{y}
$$

---

# 4. Mean Squared Error

For a single training example, MSE can be written as:

$$
L = \tfrac{1}{2} (y - \hat{y})^2
$$

The factor $\tfrac{1}{2}$ is commonly included because it makes differentiation simpler.

Differentiate the loss with respect to the predicted output:

$$
\frac{\partial L}{\partial \hat{y}} = \hat{y} - y
$$

---

# 5. Derivation of Output-Layer Weight Update

We want:

$$
\frac{\partial L}{\partial W_2}
$$

Using the chain rule:

$$
\frac{\partial L}{\partial W_2} =
\frac{\partial L}{\partial \hat{y}} \cdot
\frac{\partial \hat{y}}{\partial z_o} \cdot
\frac{\partial z_o}{\partial W_2}
$$

We know:

$$
\frac{\partial L}{\partial \hat{y}} = \hat{y} - y
$$

and:

$$
\frac{\partial \hat{y}}{\partial z_o} = g'(z_o)
$$

Since $z_o = W_2 h + b_2$, we get:

$$
\frac{\partial z_o}{\partial W_2} = h
$$

Therefore:

$$
\frac{\partial L}{\partial W_2} = (\hat{y} - y)\,g'(z_o)\,h^T
$$

Define the output error term:

$$
\boxed{\delta_o = (\hat{y} - y)\,g'(z_o)}
$$

Therefore:

$$
\boxed{\frac{\partial L}{\partial W_2} = \delta_o\,h^T}
$$

---

# 6. Output-Layer Weight Update

Gradient descent updates the weight as:

$$
W_2^{\text{new}} = W_2 - \eta\,\frac{\partial L}{\partial W_2}
$$

where $\eta$ is the **learning rate**.

Therefore:

$$
\boxed{W_2^{\text{new}} = W_2 - \eta\,\delta_o\,h^T}
$$

The bias is updated as:

$$
\boxed{b_2^{\text{new}} = b_2 - \eta\,\delta_o}
$$

---

# 7. Derivation of Hidden-Layer Weight Update

Now we need:

$$
\frac{\partial L}{\partial W_1}
$$

Using the chain rule:

$$
\frac{\partial L}{\partial W_1} =
\frac{\partial L}{\partial \hat{y}} \cdot
\frac{\partial \hat{y}}{\partial z_o} \cdot
\frac{\partial z_o}{\partial h} \cdot
\frac{\partial h}{\partial z_h} \cdot
\frac{\partial z_h}{\partial W_1}
$$

We already know the product of the first two terms equals $\delta_o$.

Also:

$$
\frac{\partial z_o}{\partial h} = W_2
$$

and:

$$
\frac{\partial h}{\partial z_h} = f'(z_h)
$$

Therefore the hidden-layer error term is:

$$
\boxed{\delta_h = (W_2^T \delta_o) \odot f'(z_h)}
$$

where $\odot$ represents element-wise multiplication.

Since $z_h = W_1 X + b_1$, we obtain:

$$
\boxed{\frac{\partial L}{\partial W_1} = \delta_h\,X^T}
$$

---

# 8. Hidden-Layer Weight Update

Using gradient descent:

$$
W_1^{\text{new}} = W_1 - \eta\,\frac{\partial L}{\partial W_1}
$$

Therefore:

$$
\boxed{W_1^{\text{new}} = W_1 - \eta\,\delta_h\,X^T}
$$

The hidden-layer bias is updated as:

$$
\boxed{b_1^{\text{new}} = b_1 - \eta\,\delta_h}
$$

---

# 9. Final Backpropagation Equations

The complete set of equations is:

### Forward propagation

$$
z_h = W_1 X + b_1
$$
$$
h = f(z_h)
$$
$$
z_o = W_2 h + b_2
$$
$$
\hat{y} = g(z_o)
$$

### Loss

$$
L = \tfrac{1}{2}(y - \hat{y})^2
$$

### Output error

$$
\boxed{\delta_o = (\hat{y} - y)\,g'(z_o)}
$$

### Hidden error

$$
\boxed{\delta_h = (W_2^T \delta_o) \odot f'(z_h)}
$$

### Output-layer update

$$
\boxed{W_2 \leftarrow W_2 - \eta\,\delta_o\,h^T}
$$

$$
\boxed{b_2 \leftarrow b_2 - \eta\,\delta_o}
$$

### Hidden-layer update

$$
\boxed{W_1 \leftarrow W_1 - \eta\,\delta_h\,X^T}
$$

$$
\boxed{b_1 \leftarrow b_1 - \eta\,\delta_h}
$$

---

# 10. Working of Backpropagation

The overall process can be remembered as:

```text
FORWARD PASS
     ↓
Input → Hidden Layer → Output
                         ↓
                    Calculate MSE
                         ↓
BACKWARD PASS            ↓
                         Error
                           ↓
                  Output-layer gradient
                           ↓
                  Hidden-layer gradient
                           ↓
                    Update weights
```

The key idea is:

> **Backpropagation calculates the gradient of the loss with respect to every weight using the chain rule, and gradient descent updates the weights in the direction that reduces the loss.**

### Conclusion

For a single-hidden-layer neural network, backpropagation first computes the output error and then propagates this error backward to the hidden layer. Using the **chain rule** and **MSE loss**, gradients for the output and hidden layers are derived and used to update weights and biases via gradient descent. The derivation above shows this step-by-step and presents the final compact update equations used in practice.
