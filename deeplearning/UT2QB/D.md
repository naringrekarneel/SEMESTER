Here are your study notes on Batch Normalization, formatted with proper mathematical notation and clear structure.

# Batch Normalization — 10 Marks

## 1. Introduction

**Batch Normalization (BN)** is a technique used in deep neural networks to **normalize the activations of a layer** during training.

It was introduced to make neural network training **faster, more stable, and less sensitive to initialization**.

Batch Normalization normalizes the values within a mini-batch and then uses two learnable parameters ($\gamma$ and $\beta$) to allow the network to dynamically scale and shift the normalized values when necessary.

---

## 2. Need for Batch Normalization

During training, the distribution of activations changes continuously as the weights of previous layers are updated. This phenomenon forces each layer to adapt to changing input distributions at every epoch, making optimization slow and difficult.

Batch Normalization helps by keeping layer activations within a controlled, stable range throughout training.

### Core Workflow:

$$\boxed{\text{Normalize} \rightarrow \text{Scale} \rightarrow \text{Shift}}$$

---

## 3. Mathematical Formulation

Consider a mini-batch of activations $B = \{x_1, x_2, \ldots, x_m\}$:

### Step 1: Mini-Batch Mean

$$\boxed{\mu_B = \frac{1}{m}\sum_{i=1}^{m}x_i}$$

### Step 2: Mini-Batch Variance

$$\boxed{\sigma_B^2 = \frac{1}{m}\sum_{i=1}^{m}(x_i - \mu_B)^2}$$

### Step 3: Normalize

$$\boxed{\hat{x}_i = \frac{x_i - \mu_B}{\sqrt{\sigma_B^2 + \epsilon}}}$$


*(where $\epsilon$ is a small constant, e.g., $10^{-5}$, to prevent division by zero).*

### Step 4: Scale and Shift

Batch Normalization introduces two learnable parameters:

* $\gamma$ $\rightarrow$ scale parameter
* $\beta$ $\rightarrow$ shift parameter

$$\boxed{y_i = \gamma \hat{x}_i + \beta}$$

> **Note:** If the network learns that the identity transform is optimal ($\gamma = \sqrt{\sigma_B^2 + \epsilon}$ and $\beta = \mu_B$), it can undo the normalization step entirely.

---

## 4. Batch Normalization During Training

During **training**, the following steps are executed for every mini-batch:

1. **Pass Mini-Batch:** Forward pass $m$ samples through a layer.
2. **Compute Batch Stats:** Calculate $\mu_B$ and $\sigma_B^2$.
3. **Normalize:** Transform $x_i \rightarrow \hat{x}_i$.
4. **Scale & Shift:** Calculate output $y_i = \gamma \hat{x}_i + \beta$.
5. **Backpropagation:** Compute gradients and update model weights alongside $\gamma$ and $\beta$.
6. **Track Running Statistics:** Update moving averages of global mean and variance for future inference:

$$\mu_{\text{running}} \leftarrow \alpha \mu_{\text{running}} + (1 - \alpha) \mu_B$$


$$\sigma^2_{\text{running}} \leftarrow \alpha \sigma^2_{\text{running}} + (1 - \alpha) \sigma_B^2$$



---

## 5. Batch Normalization During Inference

During **inference/testing**, calculating mean and variance from a single test sample or small test batch is impossible or unstable.

Instead, the model uses the **running mean** and **running variance** saved during training:

$$\boxed{\hat{x} = \frac{x - \mu_{\text{running}}}{\sqrt{\sigma_{\text{running}}^2 + \epsilon}}}$$

$$\boxed{y = \gamma \hat{x} + \beta}$$

### Workflow Comparison:

```text
Training:
Mini-Batch → Batch Mean & Variance → Normalize → Scale/Shift (γ, β)

Inference:
Test Input → Running Mean & Variance → Normalize → Scale/Shift (γ, β)

```

This guarantees deterministic output that depends strictly on the input sample rather than the test batch composition.

---

## 6. Why Batch Normalization Accelerates Convergence

1. **Stable Activation Distributions:** Prevents layer inputs from drifting drastically during updates.
2. **Improved Gradient Flow:** Mitigates vanishing and exploding gradient problems in deeper layers.
3. **Enables Higher Learning Rates:** Stabilized gradients allow aggressive step sizes without divergence.
4. **Reduces Sensitivity to Weight Initialization:** Networks train effectively even with suboptimal initial weights.
5. **Smoother Loss Landscape:** Smooths optimization curves, allowing gradient descent to make steady progress.
6. **Mild Regularization Effect:** Mini-batch noise acts as a light regularizer, slightly reducing reliance on Dropout.

---

## 7. Numerical Example

Consider a simplified 1D mini-batch activation vector:


$$x = [2, 4, 6, 8]$$

* **Mean ($\mu_B$):** $\frac{2 + 4 + 6 + 8}{4} = 5$
* **Variance ($\sigma_B^2$):** $\frac{(2-5)^2 + (4-5)^2 + (6-5)^2 + (8-5)^2}{4} = \frac{9 + 1 + 1 + 9}{4} = 5$
* **Normalized ($\hat{x}$):** Assuming $\epsilon \approx 0$:

$$\hat{x} \approx \left[ \frac{2-5}{\sqrt{5}}, \frac{4-5}{\sqrt{5}}, \frac{6-5}{\sqrt{5}}, \frac{8-5}{\sqrt{5}} \right] \approx [-1.34, -0.45, 0.45, 1.34]$$


* **Scale & Shift ($y$):** Applied as $y = \gamma \hat{x} + \beta$.

---

## 8. Training vs. Inference Key Differences

| Feature | Training | Inference |
| --- | --- | --- |
| **Mean Source** | Current Mini-batch ($\mu_B$) | Running Population ($\mu_{\text{running}}$) |
| **Variance Source** | Current Mini-batch ($\sigma_B^2$) | Running Population ($\sigma_{\text{running}}^2$) |
| **Learnable Params ($\gamma, \beta$)** | Updated via Backprop | Fixed learned values |
| **Batch Dependency** | High (depends on current batch) | None (deterministic for single inputs) |
| **Primary Purpose** | Stabilize gradient updates | Make deterministic predictions |

---

## 9. Complete Process Flowchart

```text
               TRAINING                               INFERENCE
                  ↓                                       ↓
           Mini-batch Input                           Test Input
                  ↓                                       ↓
         Calculate Mean (μ_B)                   Load Running Mean (μ_run)
                  ↓                                       ↓
       Calculate Variance (σ²_B)             Load Running Variance (σ²_run)
                  ↓                                       ↓
          Normalize (x̂_i)                         Normalize (x̂)
                  ↓                                       ↓
      Scale/Shift (γ x̂_i + β)                  Scale/Shift (γ x̂ + β)
                  ↓                                       ↓
         Forward Pass → Loss                          Prediction
                  ↓
       Backprop & Update γ, β
                  ↓
       Update Running Stats

```

---

## 10. Conclusion

**Batch Normalization** standardizes layer inputs across mini-batches during training and applies stored population statistics during inference. By leveraging learnable scale ($\gamma$) and shift ($\beta$) parameters, it preserves network capacity while providing smooth loss surfaces, robust gradient propagation, and significantly accelerated convergence speeds.
