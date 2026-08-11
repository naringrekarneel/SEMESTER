# Batch Normalization During Training and Testing — 10 Marks

## 1. Introduction

**Batch Normalization (BN)** is a technique used in deep neural networks to normalize the activations of a layer. It makes training **more stable and often faster** by controlling the scale and distribution of intermediate activations.

Batch Normalization performs three main operations:

[
\boxed{\text{Normalize} \rightarrow \text{Scale} \rightarrow \text{Shift}}
]

It behaves differently during **training** and **testing (inference)**.

---

# 2. Internal Covariate Shift

During neural network training, the weights of earlier layers continuously change.

As a result, the distribution of inputs received by later layers also changes.

This phenomenon is called **internal covariate shift**.

For example:

```text
Layer 1
   ↓
Changes its weights
   ↓
Output distribution changes
   ↓
Layer 2 receives different inputs
   ↓
Layer 2 must continuously adapt
```

This can make optimization more difficult.

Batch Normalization attempts to stabilize intermediate activations by normalizing them.

> **Exam note:** BN was originally motivated as a way to address internal covariate shift. Modern research suggests its optimization benefits are not explained solely by reducing internal covariate shift; BN also improves the conditioning and behavior of optimization.

---

# 3. Mathematical Formulation

Consider a mini-batch:

[
B={x_1,x_2,\ldots,x_m}
]

### Step 1: Calculate Mean

[
\boxed{
\mu_B=\frac{1}{m}\sum_{i=1}^{m}x_i
}
]

### Step 2: Calculate Variance

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

This gives approximately:

[
E[\hat{x}]\approx0
]

and

[
Var(\hat{x})\approx1
]

### Step 4: Scale and Shift

BN introduces two learnable parameters:

* (\gamma) = scale
* (\beta) = shift

The final output is:

[
\boxed{
y_i=\gamma\hat{x}_i+\beta
}
]

This is important because forcing every activation to have exactly zero mean and unit variance might restrict what the network can learn. The learnable (\gamma) and (\beta) allow the network to choose an appropriate scale and mean.

---

# 4. Batch Normalization During Training

During training, BN uses the **current mini-batch statistics**.

### Step 1

Take a mini-batch of training examples.

### Step 2

Calculate the mini-batch mean:

[
\mu_B=\frac{1}{m}\sum x_i
]

### Step 3

Calculate the mini-batch variance:

[
\sigma_B^2=\frac{1}{m}\sum(x_i-\mu_B)^2
]

### Step 4

Normalize:

[
\hat{x}_i=
\frac{x_i-\mu_B}
{\sqrt{\sigma_B^2+\epsilon}}
]

### Step 5

Scale and shift:

[
y_i=\gamma\hat{x}_i+\beta
]

### Step 6

Update parameters

During backpropagation, the network learns:

* Network weights
* Biases, where applicable
* (\gamma)
* (\beta)

BN also maintains **running estimates** of the mean and variance for use during inference.

---

# 5. Batch Normalization During Testing/Inference

During testing, we generally cannot rely on the current mini-batch's statistics because:

* The test batch may contain only one or a few examples.
* Predictions should not depend on which other samples happen to be in the batch.

Therefore, BN uses the **running mean and running variance** collected during training.

The normalization becomes:

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

The learned (\gamma) and (\beta) remain fixed during inference.

---

# 6. Training vs Testing

| Feature         | Training                     | Testing/Inference           |
| --------------- | ---------------------------- | --------------------------- |
| Mean            | Mini-batch mean              | Running mean                |
| Variance        | Mini-batch variance          | Running variance            |
| (\gamma)        | Learned                      | Fixed                       |
| (\beta)         | Learned                      | Fixed                       |
| Batch dependent | Yes                          | Normally no                 |
| Purpose         | Learn stable representations | Make consistent predictions |

---

# 7. How BN Addresses Internal Covariate Shift

Without BN:

```text
Weight changes
      ↓
Activation distribution changes
      ↓
Next layer receives changing inputs
      ↓
Optimization becomes harder
```

With BN:

```text
Weight changes
      ↓
Activation distribution changes
      ↓
       Batch Normalization
      ↓
Normalized activations
      ↓
More stable input to next layer
```

Thus, BN helps keep intermediate activations in a controlled range.

---

# 8. How BN Improves Training

### 1. Stable activations

Normalization prevents activations from becoming excessively large or small.

### 2. Better gradient flow

It can make gradients easier to propagate through deep networks.

### 3. Faster convergence

The optimization process can become more stable, allowing the network to reach a good solution in fewer training iterations.

### 4. Higher learning rates

BN often allows the use of relatively larger learning rates without making training unstable.

### 5. Less sensitivity to initialization

The network becomes less dependent on carefully chosen initial weights.

### 6. Mild regularization

Because mini-batch statistics contain some randomness, BN can introduce a small regularizing effect.

---

# 9. Example

Suppose a mini-batch contains:

[
x=[2,4,6,8]
]

Mean:

[
\mu_B=5
]

Variance:

[
\sigma_B^2=5
]

The normalized values are approximately:

[
\hat{x}=[-1.34,-0.45,0.45,1.34]
]

Then BN applies:

[
y=\gamma\hat{x}+\beta
]

So the next layer receives activations whose scale is controlled rather than the raw values.

---

# 10. Complete Flow

### During Training

[
\boxed{
x
\rightarrow
\mu_B,\sigma_B^2
\rightarrow
\text{Normalize}
\rightarrow
\gamma,\beta
\rightarrow
y
}
]

Running statistics are also updated.

### During Testing

[
\boxed{
x
\rightarrow
\mu_{running},\sigma_{running}^2
\rightarrow
\text{Normalize}
\rightarrow
\gamma,\beta
\rightarrow
y
}
]

---

## Conclusion

Batch Normalization normalizes intermediate activations using **mini-batch mean and variance during training** and **running mean and variance during testing**. It then applies learnable scale and shift parameters (\gamma) and (\beta). By stabilizing activation distributions and improving the optimization landscape, BN can reduce the difficulties associated with changing internal representations, improve gradient flow, and accelerate convergence. Although it was originally introduced to address **internal covariate shift**, its practical benefits are now understood to arise from broader optimization effects as well.
