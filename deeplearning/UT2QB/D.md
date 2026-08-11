# Batch Normalization — 10 Marks

## 1. Introduction

**Batch Normalization (BN)** is a technique used in deep neural networks to **normalize the activations of a layer** during training.

It was introduced to make neural network training **faster and more stable**.

Batch Normalization normalizes the values within a mini-batch and then uses two learnable parameters to allow the network to adjust the normalized values when necessary.

---

# 2. Need for Batch Normalization

During training, the distribution of activations can change as the weights of previous layers are updated.

This can make optimization difficult because each layer has to continuously adapt to changing input distributions.

Batch Normalization helps by keeping activations in a more controlled range.

### Basic idea:

[
\boxed{\text{Normalize} \rightarrow \text{Scale} \rightarrow \text{Shift}}
]

---

# 3. Mathematical Formulation

Consider a mini-batch:

[
B={x_1,x_2,\ldots,x_m}
]

### Step 1: Calculate mini-batch mean

[
\boxed{
\mu_B=\frac{1}{m}\sum_{i=1}^{m}x_i
}
]

### Step 2: Calculate mini-batch variance

[
\boxed{
\sigma_B^2=
\frac{1}{m}\sum_{i=1}^{m}(x_i-\mu_B)^2
}
]

### Step 3: Normalize

[
\boxed{
\hat{x}_i=
\frac{x_i-\mu_B}
{\sqrt{\sigma_B^2+\epsilon}}
}
]

where (\epsilon) is a small value added for numerical stability.

### Step 4: Scale and shift

Batch Normalization introduces two learnable parameters:

* (\gamma) → scale
* (\beta) → shift

The final output is:

[
\boxed{
y_i=\gamma\hat{x}_i+\beta
}
]

Thus, the network can learn the appropriate mean and variance rather than being forced to use only zero mean and unit variance.

---

# 4. Batch Normalization During Training

During **training**, the following steps are performed for each mini-batch.

### Step 1: Take mini-batch

A small batch of training examples is passed through the network.

### Step 2: Calculate mean

[
\mu_B=\frac{1}{m}\sum x_i
]

### Step 3: Calculate variance

[
\sigma_B^2=\frac{1}{m}\sum(x_i-\mu_B)^2
]

### Step 4: Normalize

[
\hat{x}_i=
\frac{x_i-\mu_B}
{\sqrt{\sigma_B^2+\epsilon}}
]

### Step 5: Scale and shift

[
y_i=\gamma\hat{x}_i+\beta
]

### Step 6: Update parameters

During backpropagation, the network learns:

* Weights
* Biases
* (\gamma)
* (\beta)

The batch statistics are also used to maintain **running estimates of the mean and variance** for inference.

---

# 5. Batch Normalization During Inference

During **inference/testing**, we usually do not calculate mean and variance from the current input batch.

Instead, the network uses the **running mean and running variance** accumulated during training.

The formula becomes:

[
\boxed{
\hat{x}=
\frac{x-\mu_{running}}
{\sqrt{\sigma_{running}^2+\epsilon}}
}
]

Then:

[
\boxed{
y=\gamma\hat{x}+\beta
}
]

Therefore:

```text
Training:
Mini-batch → Mean & Variance → Normalize → Scale/Shift

Inference:
Input → Running Mean & Variance → Normalize → Scale/Shift
```

This makes inference deterministic and independent of the particular batch used for prediction.

---

# 6. Why Batch Normalization Accelerates Convergence

Batch Normalization can make optimization easier for several reasons.

### 1. More stable activation distributions

It keeps activations in a more controlled range, reducing extreme values.

### 2. Better gradient flow

Normalization can help prevent activations and gradients from becoming excessively large or small, making deep networks easier to train.

### 3. Allows higher learning rates

Because training is often more stable, a somewhat larger learning rate can sometimes be used effectively.

### 4. Reduces sensitivity to initialization

The network becomes less dependent on carefully chosen initial weight values.

### 5. Smooths optimization

Batch Normalization can make the loss landscape easier to optimize in practice, allowing gradient-based optimization to make more consistent progress.

### 6. Provides mild regularization

The randomness introduced by mini-batch statistics can have a regularizing effect, although BN should not be considered a replacement for explicit regularization methods.

---

# 7. Example

Suppose a mini-batch contains:

[
x=[2,4,6,8]
]

Mean:

[
\mu_B=\frac{2+4+6+8}{4}=5
]

Variance:

[
\sigma_B^2=5
]

The values are normalized approximately to:

[
[-1.34,-0.45,0.45,1.34]
]

Then BN applies:

[
y=\gamma\hat{x}+\beta
]

The values are therefore transformed into a more controlled representation before being passed to the next operation.

---

# 8. Training vs Inference

| Feature              | Training            | Inference            |
| -------------------- | ------------------- | -------------------- |
| Mean                 | Mini-batch mean     | Running mean         |
| Variance             | Mini-batch variance | Running variance     |
| Normalize            | Yes                 | Yes                  |
| Learn (\gamma,\beta) | Yes                 | Fixed learned values |
| Batch-dependent      | Yes                 | Normally no          |
| Purpose              | Learn parameters    | Make predictions     |

---

# 9. Complete Process

```text
             TRAINING
                 ↓
          Mini-batch Input
                 ↓
        Calculate Mean (μ)
                 ↓
       Calculate Variance (σ²)
                 ↓
             Normalize
                 ↓
       Scale by γ and Shift by β
                 ↓
          Forward Propagation
                 ↓
            Loss + Backprop
                 ↓
      Update Weights, γ and β
                 ↓
       Update Running Statistics
```

During inference:

```text
          TEST INPUT
              ↓
     Running Mean/Variance
              ↓
          Normalize
              ↓
        γ × x̂ + β
              ↓
          Prediction
```

---

## 10. Conclusion

**Batch Normalization** normalizes layer activations using mini-batch statistics during training and running statistics during inference. It then applies learnable **scale ((\gamma)) and shift ((\beta))** parameters. By stabilizing activations, improving gradient flow, reducing sensitivity to initialization, and often allowing larger learning rates, Batch Normalization can significantly **accelerate and stabilize neural-network convergence**.
