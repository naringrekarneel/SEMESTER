# SGD, RMSProp and Adam Optimizers — 10 Marks

## 1. Introduction

Optimization algorithms are used to **minimize the loss function** of a deep neural network by updating its weights.

When the loss surface is **noisy**, ordinary gradient descent may oscillate or take a long time to converge.

Three commonly used optimizers are:

1. **Stochastic Gradient Descent (SGD)**
2. **RMSProp**
3. **Adam (Adaptive Moment Estimation)**

They differ in how they use the gradient history to determine the size and direction of weight updates.

---

# 2. Stochastic Gradient Descent (SGD)

SGD calculates the gradient using a single training example or a mini-batch and updates the weights.

The basic formulation is:

[
g_t=\nabla_\theta L_t(\theta_t)
]

[
\boxed{\theta_{t+1}=\theta_t-\eta g_t}
]

where:

* (\theta_t) = model parameters
* (g_t) = current gradient
* (\eta) = learning rate
* (L_t) = loss for the current sample/mini-batch

### Convergence behavior

Because SGD uses noisy gradients:

* Updates fluctuate around the true gradient.
* It can oscillate on noisy surfaces.
* It may converge quickly initially.
* Near the minimum, it may continue bouncing around instead of settling exactly.

However, this noise can sometimes help the optimizer escape undesirable regions.

---

# 3. RMSProp

**RMSProp (Root Mean Square Propagation)** adapts the learning rate separately for each parameter.

It maintains an exponentially weighted average of squared gradients.

### Step 1: Calculate squared-gradient average

[
\boxed{
s_t=\rho s_{t-1}+(1-\rho)g_t^2
}
]

where:

* (s_t) = moving average of squared gradients
* (\rho) = decay rate
* (g_t^2) = element-wise squared gradient

### Step 2: Update parameters

[
\boxed{
\theta_{t+1}
============

\theta_t-
\frac{\eta}{\sqrt{s_t}+\epsilon}g_t
}
]

where (\epsilon) is a small value used to avoid division by zero.

### Intuition

If a parameter repeatedly receives **large gradients**, RMSProp reduces its effective learning rate.

If a parameter receives **small gradients**, its effective learning rate remains relatively larger.

---

# 4. Convergence Behavior of RMSProp

RMSProp is particularly useful on noisy or non-stationary loss surfaces because it adapts the step size.

Compared with SGD:

* Reduces oscillations.
* Handles different gradient scales better.
* Usually converges faster in deep networks.
* Can move effectively through steep and flat regions.

The denominator:

[
\sqrt{s_t}+\epsilon
]

normalizes the gradient according to its recent magnitude.

---

# 5. Adam Optimizer

**Adam** combines ideas from **Momentum** and **RMSProp**.

It maintains two moving averages:

1. First moment → average of gradients
2. Second moment → average of squared gradients

### Step 1: First moment

[
\boxed{
m_t=\beta_1m_{t-1}+(1-\beta_1)g_t
}
]

This acts similarly to **momentum**.

### Step 2: Second moment

[
\boxed{
v_t=\beta_2v_{t-1}+(1-\beta_2)g_t^2
}
]

This acts similarly to **RMSProp**.

---

# 6. Bias Correction in Adam

Because (m_t) and (v_t) are initialized to zero, they can be biased toward zero during the first few iterations.

Adam therefore applies bias correction:

[
\boxed{
\hat m_t=\frac{m_t}{1-\beta_1^t}
}
]

[
\boxed{
\hat v_t=\frac{v_t}{1-\beta_2^t}
}
]

The final update is:

[
\boxed{
\theta_{t+1}
============

\theta_t-
\eta
\frac{\hat m_t}
{\sqrt{\hat v_t}+\epsilon}
}
]

Common default values are:

[
\beta_1=0.9,\qquad
\beta_2=0.999
]

---

# 7. Comparison of Mathematical Formulations

| Feature                | **SGD**         | **RMSProp**                               | **Adam**                                           |
| ---------------------- | --------------- | ----------------------------------------- | -------------------------------------------------- |
| Gradient               | (g_t)           | (g_t)                                     | (g_t)                                              |
| Gradient memory        | None            | Squared gradient                          | Gradient + squared gradient                        |
| First moment           | No              | No                                        | Yes                                                |
| Second moment          | No              | Yes                                       | Yes                                                |
| Main update            | (\theta-\eta g) | (\theta-\frac{\eta g}{\sqrt{s}+\epsilon}) | (\theta-\frac{\eta\hat m}{\sqrt{\hat v}+\epsilon}) |
| Adaptive learning rate | No              | Yes                                       | Yes                                                |
| Momentum-like behavior | No              | No                                        | Yes                                                |
| Bias correction        | No              | No                                        | Yes                                                |

---

# 8. Convergence Behavior on a Noisy Surface

Consider a noisy loss surface:

```text
Loss
 ↑
 |      /\     /\
 |  /\ /  \/\_/  \__
 |_/  \              \__
 +--------------------------→ Parameters
```

### SGD

SGD reacts directly to the noisy gradient:

[
\theta_{t+1}=\theta_t-\eta g_t
]

Therefore, its path can be **zigzag and unstable**.

### RMSProp

RMSProp scales the gradient based on its recent squared magnitude:

[
\frac{g_t}{\sqrt{s_t}+\epsilon}
]

Therefore, it reduces excessively large updates and generally gives **smoother convergence**.

### Adam

Adam combines:

* Momentum → smoother direction
* RMSProp → adaptive step sizes

Therefore, Adam generally provides **fast and stable convergence** on many noisy deep-learning problems.

---

# 9. Overall Comparison

| Property                 | SGD                  | RMSProp                      | Adam                 |
| ------------------------ | -------------------- | ---------------------------- | -------------------- |
| Simplicity               | Very high            | Moderate                     | Moderate             |
| Noisy gradient handling  | Moderate             | Good                         | Very good            |
| Learning-rate adaptation | No                   | Yes                          | Yes                  |
| Oscillation reduction    | Low                  | Good                         | Very good            |
| Convergence speed        | Often slower         | Usually faster               | Usually fast         |
| Memory requirement       | Low                  | Moderate                     | Higher               |
| Hyperparameters          | Few                  | More                         | More                 |
| Common use               | General optimization | RNNs/non-stationary problems | Deep neural networks |

---

# 10. Conclusion

**SGD** uses only the current gradient, making it simple but sensitive to noise and capable of oscillatory convergence. **RMSProp** maintains a moving average of squared gradients and adapts the learning rate for each parameter, providing smoother convergence on noisy surfaces. **Adam** combines RMSProp's adaptive learning rates with momentum and bias correction, generally providing fast and stable convergence. Therefore, for a **noisy deep-learning loss surface**, Adam is often a strong default choice, although SGD can sometimes achieve better final generalization when carefully tuned.
