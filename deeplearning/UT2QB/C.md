Here are your notes on Adaptive Learning Rate Algorithms, cleanly formatted with proper mathematical notation for easy reading and studying.

# Adaptive Learning Rate Algorithms: AdaGrad, RMSProp and Adam — 10 Marks

## 1. Introduction

The **learning rate** ($\eta$) controls how much the weights of a neural network change during each optimization step.

A fixed learning rate may not work well for all parameters because some parameters may receive **large gradients** while others receive **small or infrequent gradients**.

**Adaptive learning rate algorithms** solve this problem by automatically adjusting the learning rate for each parameter based on the history of gradients.

Three important algorithms are:

1. **AdaGrad**
2. **RMSProp**
3. **Adam**

---

## 2. AdaGrad

**AdaGrad (Adaptive Gradient)** adjusts the learning rate of each parameter according to the accumulated squared gradients.

### Working Mechanism

AdaGrad keeps a running sum of the squared gradients.

First, calculate the current gradient:


$$g_t = \nabla_\theta L(\theta_t)$$

Then accumulate squared gradients:


$$\boxed{G_t = G_{t-1} + g_t^2}$$

The parameter update is:


$$\boxed{\theta_{t+1} = \theta_t - \frac{\eta}{\sqrt{G_t} + \epsilon}g_t}$$

where:

* $\theta$ = model parameter
* $g_t$ = current gradient
* $\eta$ = initial learning rate
* $G_t$ = accumulated squared gradients
* $\epsilon$ = small constant to prevent division by zero

### Advantages

* Automatically adapts the learning rate.
* Gives smaller updates to frequently occurring parameters (and larger updates to rare ones).
* Useful for sparse data and sparse features.

### Limitation

Because $G_t$ **continually increases**, the effective learning rate keeps decreasing. Eventually, the learning rate becomes so small that learning virtually stops.

---

## 3. RMSProp

**RMSProp (Root Mean Square Propagation)** was developed to address AdaGrad's continuously decreasing learning rate.

Instead of accumulating all squared gradients forever, RMSProp maintains an **exponentially decaying average** of squared gradients.

### Working Mechanism

First calculate the gradient:


$$g_t = \nabla_\theta L(\theta_t)$$

Then calculate the moving average:


$$\boxed{s_t = \rho s_{t-1} + (1-\rho)g_t^2}$$

The parameter update is:


$$\boxed{\theta_{t+1} = \theta_t - \frac{\eta}{\sqrt{s_t} + \epsilon}g_t}$$

where:

* $s_t$ = moving average of squared gradients
* $\rho$ = decay rate (a common value is $\rho \approx 0.9$)
* $\eta$ = learning rate

### Advantages

* Prevents the learning rate from continuously shrinking.
* Adapts the learning rate independently for each parameter.
* Works well on noisy and non-stationary loss surfaces.
* Reduces oscillations.

---

## 4. Adam

**Adam (Adaptive Moment Estimation)** combines the advantages of **Momentum** and **RMSProp**.

It maintains two moving averages:

* **First moment** $\rightarrow$ average of gradients
* **Second moment** $\rightarrow$ average of squared gradients

### Step 1: First Moment

The first moment tracks the direction of the gradient (behaves similarly to **momentum**):


$$\boxed{m_t = \beta_1 m_{t-1} + (1-\beta_1)g_t}$$

### Step 2: Second Moment

The second moment tracks the magnitude of squared gradients (provides adaptive learning-rate behavior similar to **RMSProp**):


$$\boxed{v_t = \beta_2 v_{t-1} + (1-\beta_2)g_t^2}$$

### Step 3: Bias Correction

Since $m_t$ and $v_t$ start at zero, they can be biased toward zero in the initial iterations. Therefore, Adam uses bias correction:


$$\boxed{\hat{m}_t = \frac{m_t}{1-\beta_1^t}}$$

$$\boxed{\hat{v}_t = \frac{v_t}{1-\beta_2^t}}$$

### Step 4: Parameter Update

The final Adam update is:


$$\boxed{\theta_{t+1} = \theta_t - \eta \frac{\hat{m}_t}{\sqrt{\hat{v}_t} + \epsilon}}$$

Common default values are:

* $\beta_1 = 0.9$
* $\beta_2 = 0.999$

---

## 5. Comparison of AdaGrad, RMSProp and Adam

| Feature | **AdaGrad** | **RMSProp** | **Adam** |
| --- | --- | --- | --- |
| **Main idea** | Accumulate squared gradients | Moving avg of squared gradients | Momentum + adaptive squared gradients |
| **Gradient memory** | All past squared gradients | Recent squared gradients | Recent gradients + squared gradients |
| **Learning rate** | Continuously decreases | Adaptive | Adaptive |
| **Momentum** | No | No | Yes |
| **Bias correction** | No | No | Yes |
| **Handles sparse data** | Excellent | Good | Good |
| **Main limitation** | Learning rate may become too small | Requires decay parameter | More hyperparameters |
| **Typical use** | Sparse features | Deep/RNN networks | General deep learning |

---

## 6. Evolution of the Algorithms

The three algorithms can be understood as a direct evolution:

$$\boxed{\text{AdaGrad} \rightarrow \text{RMSProp} \rightarrow \text{Adam}}$$

* **AdaGrad:** Accumulated squared gradients.
* *Problem:* Learning rate becomes too small.


* **RMSProp:** Exponentially weighted squared gradients.
* *Improvement:* Learning rate does not continually vanish.


* **Adam:** Momentum + RMSProp.
* *Improvement:* Provides both **directional memory** and **adaptive learning rates**.



---

## 7. Simple Intuition

Imagine walking downhill on a rugged mountain:

* **AdaGrad:** You remember **every step you've ever taken** and adjust your step size based on all of them. Eventually, you get overly cautious and barely move.
* **RMSProp:** You care more about your **recent steps** and gradually forget older ones, allowing you to keep a steady pace.
* **Adam:** You remember **which direction you've been moving** (Momentum) AND **how large your recent steps have been** (RMSProp). This gives you the most informed and efficient path down the mountain.

---

## 8. Conclusion

Adaptive learning rate algorithms automatically adjust the learning rate of individual parameters according to gradient history. **AdaGrad** accumulates squared gradients but may reduce the learning rate excessively. **RMSProp** solves this by using an exponentially weighted average of squared gradients. **Adam** combines RMSProp with momentum and bias correction, making it one of the most widely used optimizers for training deep neural networks.
