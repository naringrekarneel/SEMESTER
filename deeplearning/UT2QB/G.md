Here are your study notes on Batch Normalization, perfectly formatted with mathematical notation and structured for easy exam preparation.

# Batch Normalization During Training and Testing — 10 Marks

## 1. Introduction

**Batch Normalization (BN)** is a technique used in deep neural networks to normalize the activations of a layer. It makes training **more stable and often faster** by controlling the scale and distribution of intermediate activations.

Batch Normalization performs three main operations:


$$\boxed{\text{Normalize} \rightarrow \text{Scale} \rightarrow \text{Shift}}$$

It behaves differently depending on whether the network is in the **training** phase or the **testing (inference)** phase.

---

## 2. Internal Covariate Shift

During neural network training, the weights of earlier layers continuously change. As a result, the distribution of inputs received by later layers also changes. This phenomenon is called **internal covariate shift**.

**The Problem:**

1. Layer 1 changes its weights.
2. The output distribution of Layer 1 changes.
3. Layer 2 receives differently distributed inputs.
4. Layer 2 must continuously adapt to this moving target, making optimization difficult.

Batch Normalization attempts to stabilize intermediate activations by normalizing them.

> **Exam Note:** BN was originally motivated as a way to address internal covariate shift. Modern research suggests its optimization benefits are not explained solely by reducing internal covariate shift; BN also improves the overall conditioning and behavior of optimization.

---

## 3. Mathematical Formulation

Consider a mini-batch:


$$B=\{x_1, x_2, \ldots, x_m\}$$

### Step 1: Calculate Mean

$$\boxed{\mu_B = \frac{1}{m}\sum_{i=1}^{m}x_i}$$

### Step 2: Calculate Variance

$$\boxed{\sigma_B^2 = \frac{1}{m}\sum_{i=1}^{m}(x_i - \mu_B)^2}$$

### Step 3: Normalize

$$\boxed{\hat{x}_i = \frac{x_i - \mu_B}{\sqrt{\sigma_B^2 + \epsilon}}}$$

This operation guarantees that the normalized values have approximately:

* $\text{E}[\hat{x}] \approx 0$
* $\text{Var}(\hat{x}) \approx 1$

*(where $\epsilon$ is a small constant to prevent division by zero).*

### Step 4: Scale and Shift

BN introduces two learnable parameters to ensure the network can still represent complex features:

* $\gamma$ = scale
* $\beta$ = shift

The final output is:


$$\boxed{y_i = \gamma\hat{x}_i + \beta}$$

Forcing every activation to have exactly zero mean and unit variance might restrict what the network can learn. The learnable $\gamma$ and $\beta$ allow the network to dynamically choose the most appropriate scale and mean.

---

## 4. Batch Normalization During Training

During training, BN strictly uses the **current mini-batch statistics**.

1. **Take a mini-batch** of $m$ training examples.
2. **Calculate the mini-batch mean:** $\mu_B = \frac{1}{m}\sum x_i$
3. **Calculate the mini-batch variance:** $\sigma_B^2 = \frac{1}{m}\sum(x_i - \mu_B)^2$
4. **Normalize the values:** $\hat{x}_i = \frac{x_i - \mu_B}{\sqrt{\sigma_B^2 + \epsilon}}$
5. **Scale and shift:** $y_i = \gamma\hat{x}_i + \beta$
6. **Update parameters:** During backpropagation, the network learns the weights, biases, $\gamma$, and $\beta$.

> **Crucial Background Step:** Throughout training, BN also maintains an exponentially weighted **running estimate** of the global mean ($\mu_{\text{running}}$) and variance ($\sigma^2_{\text{running}}$).

---

## 5. Batch Normalization During Testing/Inference

During testing, we generally cannot rely on the current mini-batch's statistics because:

* The test batch may contain only one or a few examples (making batch stats unreliable).
* A single prediction should be deterministic and not depend on which other random samples happen to be in the same batch.

Therefore, BN uses the **running mean and running variance** collected globally during the training phase.

The normalization step becomes:


$$\boxed{\hat{x} = \frac{x - \mu_{\text{running}}}{\sqrt{\sigma_{\text{running}}^2 + \epsilon}}}$$

Followed by the same scale and shift:


$$\boxed{y = \gamma\hat{x} + \beta}$$

The learned $\gamma$ and $\beta$ remain completely **fixed** during inference.

---

## 6. Training vs. Testing Summary

| Feature | Training | Testing / Inference |
| --- | --- | --- |
| **Mean Source** | Current mini-batch mean | Global running mean |
| **Variance Source** | Current mini-batch variance | Global running variance |
| **Scale ($\gamma$)** | Learned and updated | Fixed |
| **Shift ($\beta$)** | Learned and updated | Fixed |
| **Batch dependent?** | Yes | No (Deterministic) |
| **Primary Purpose** | Learn stable representations | Make consistent predictions |

---

## 7. How BN Addresses Internal Covariate Shift

**Without BN:**
Weight changes $\rightarrow$ Activation distribution shifts wildly $\rightarrow$ Next layer receives changing inputs $\rightarrow$ Optimization stalls.

**With BN:**
Weight changes $\rightarrow$ Activation distribution tries to shift $\rightarrow$ **Batch Normalization** steps in $\rightarrow$ Normalized activations are passed on $\rightarrow$ Next layer receives a highly stable, controlled input.

---

## 8. Why BN Improves Training

1. **Stable Activations:** Normalization prevents activations from exploding or vanishing to zero.
2. **Better Gradient Flow:** It propagates gradients more cleanly through deep networks.
3. **Faster Convergence:** The optimization landscape is smoothed, allowing the network to reach a global minimum in fewer iterations.
4. **Higher Learning Rates:** BN allows the use of larger learning rates without destabilizing the training process.
5. **Initialization Robustness:** The network becomes much less dependent on perfectly tuned initial weights.
6. **Mild Regularization:** The inherent randomness of mini-batch statistics acts as a light regularizer, slightly reducing overfitting.

---

## 9. Numerical Example

Suppose a tiny mini-batch contains the values:


$$x = [2, 4, 6, 8]$$

* **Mean:** $\mu_B = 5$
* **Variance:** $\sigma_B^2 = 5$

The intermediate normalized values (assuming $\epsilon \approx 0$) are approximately:


$$\hat{x} = [-1.34, -0.45, 0.45, 1.34]$$

Finally, BN applies the learnable parameters:


$$y = \gamma\hat{x} + \beta$$

The raw inputs (2 to 8) are now controlled, preventing large values from overwhelming the network's next layer.

---

## 10. Complete Process Flow

### During Training

$$\boxed{x \rightarrow \mu_B, \sigma_B^2 \rightarrow \text{Normalize } (\hat{x}) \rightarrow \text{Apply } \gamma, \beta \rightarrow y}$$


*(Global running statistics are updated in the background).*

### During Testing

$$\boxed{x \rightarrow \mu_{\text{running}}, \sigma_{\text{running}}^2 \rightarrow \text{Normalize } (\hat{x}) \rightarrow \text{Apply } \gamma, \beta \rightarrow y}$$

---

## 11. Conclusion

Batch Normalization normalizes intermediate activations using **mini-batch mean and variance during training** and fixed **running mean and variance during testing**. By scaling and shifting the normalized outputs with learnable parameters ($\gamma$ and $\beta$), BN stabilizes activation distributions and smooths the optimization landscape. This reduces the difficulties associated with changing internal representations (internal covariate shift), dramatically improves gradient flow, and allows for faster, more robust convergence.
