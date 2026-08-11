# Adaptive Learning Rate Algorithms: AdaGrad, RMSProp and Adam — 10 Marks

## 1. Introduction

The **learning rate** (\eta) controls how much the weights of a neural network change during each optimization step.

A fixed learning rate may not work well for all parameters because some parameters may receive **large gradients** while others receive **small or infrequent gradients**.

**Adaptive learning rate algorithms** solve this problem by automatically adjusting the learning rate for each parameter based on the history of gradients.

Three important algorithms are:

1. **AdaGrad**
2. **RMSProp**
3. **Adam**

---

# 2. AdaGrad

**AdaGrad (Adaptive Gradient)** adjusts the learning rate of each parameter according to the accumulated squared gradients.

### Working mechanism

AdaGrad keeps a running sum of the squared gradients.

First, calculate:

[
g_t=\nabla_\theta L(\theta_t)
]

Then accumulate squared gradients:

[
\boxed{
G_t=G_{t-1}+g_t^2
}
]

The parameter update is:

[
\boxed{
\theta_{t+1}
============

\theta_t-
\frac{\eta}{\sqrt{G_t}+\epsilon}g_t
}
]

where:

* (\theta) = model parameter
* (g_t) = current gradient
* (\eta) = initial learning rate
* (G_t) = accumulated squared gradients
* (\epsilon) = small constant to prevent division by zero

### Advantages

* Automatically adapts the learning rate.
* Gives smaller updates to frequently occurring parameters.
* Useful for sparse data and sparse features.

### Limitation

Because (G_t) **continually increases**, the effective learning rate keeps decreasing.

Eventually, learning can become extremely slow.

---

# 3. RMSProp

**RMSProp (Root Mean Square Propagation)** was developed to address AdaGrad's continuously decreasing learning rate.

Instead of accumulating all squared gradients forever, RMSProp maintains an **exponentially decaying average** of squared gradients.

### Working mechanism

First calculate the gradient:

[
g_t=\nabla_\theta L(\theta_t)
]

Then calculate the moving average:

[
\boxed{
s_t=\rho s_{t-1}+(1-\rho)g_t^2
}
]

The parameter update is:

[
\boxed{
\theta_{t+1}
============

\theta_t-
\frac{\eta}{\sqrt{s_t}+\epsilon}g_t
}
]

where:

* (s_t) = moving average of squared gradients
* (\rho) = decay rate
* (\eta) = learning rate

A common value is:

[
\rho\approx0.9
]

### Advantages

* Prevents the learning rate from continuously shrinking.
* Adapts the learning rate independently for each parameter.
* Works well on noisy and non-stationary loss surfaces.
* Reduces oscillations.

---

# 4. Adam

**Adam (Adaptive Moment Estimation)** combines the advantages of **Momentum** and **RMSProp**.

It maintains two moving averages:

* First moment → average of gradients
* Second moment → average of squared gradients

---

## Step 1: First Moment

The first moment tracks the direction of the gradient:

[
\boxed{
m_t=\beta_1m_{t-1}+(1-\beta_1)g_t
}
]

This behaves similarly to **momentum**.

---

## Step 2: Second Moment

The second moment tracks the magnitude of squared gradients:

[
\boxed{
v_t=\beta_2v_{t-1}+(1-\beta_2)g_t^2
}
]

This provides the adaptive learning-rate behavior similar to RMSProp.

---

## Step 3: Bias Correction

Since (m_t) and (v_t) start at zero, they can be biased toward zero in the initial iterations.

Therefore, Adam uses:

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

---

## Step 4: Parameter Update

The final Adam update is:

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

Common values are:

[
\beta_1=0.9
]

[
\beta_2=0.999
]

---

# 5. Comparison of AdaGrad, RMSProp and Adam

| Feature             | **AdaGrad**                        | **RMSProp**                         | **Adam**                              |
| ------------------- | ---------------------------------- | ----------------------------------- | ------------------------------------- |
| Main idea           | Accumulate squared gradients       | Moving average of squared gradients | Momentum + adaptive squared gradients |
| Gradient memory     | All past squared gradients         | Recent squared gradients            | Recent gradients + squared gradients  |
| Learning rate       | Continuously decreases             | Adaptive                            | Adaptive                              |
| Momentum            | No                                 | No                                  | Yes                                   |
| Bias correction     | No                                 | No                                  | Yes                                   |
| Handles sparse data | Excellent                          | Good                                | Good                                  |
| Main limitation     | Learning rate may become too small | Requires decay parameter            | More hyperparameters                  |
| Typical use         | Sparse features                    | Deep/RNN networks                   | General deep learning                 |

---

# 6. Evolution of the Algorithms

The three algorithms can be understood as an evolution:

[
\boxed{\text{AdaGrad}\rightarrow\text{RMSProp}\rightarrow\text{Adam}}
]

### AdaGrad

[
\text{Accumulated squared gradients}
]

↓

Problem: learning rate becomes too small.

### RMSProp

[
\text{Exponentially weighted squared gradients}
]

↓

Problem improved: learning rate does not continually vanish.

### Adam

[
\text{Momentum + RMSProp}
]

↓

Provides both **directional memory** and **adaptive learning rates**.

---

# 7. Simple Intuition

Imagine walking downhill.

### AdaGrad

You remember **every step you've ever taken** and adjust your step size based on all of them.

### RMSProp

You care more about your **recent steps** and gradually forget older ones.

### Adam

You remember:

* **Which direction you've been moving** → Momentum
* **How large your recent steps have been** → RMSProp

So Adam makes a more informed update.

---

## 8. Conclusion

Adaptive learning rate algorithms automatically adjust the learning rate of individual parameters according to gradient history. **AdaGrad** accumulates squared gradients but may reduce the learning rate excessively. **RMSProp** solves this by using an exponentially weighted average of squared gradients. **Adam** combines RMSProp with momentum and bias correction, making it one of the most widely used optimizers for training deep neural networks.
