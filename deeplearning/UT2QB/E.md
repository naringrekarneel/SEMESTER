# Regularization Strategies: Data Augmentation, Parameter Sharing/Tying, and Input Noise Injection — 10 Marks

## 1. Introduction

**Regularization** is a set of techniques used to reduce **overfitting** in neural networks.

Overfitting occurs when a model performs very well on training data but performs poorly on unseen data.

Three important regularization strategies are:

1. **Data Augmentation**
2. **Parameter Sharing/Tying**
3. **Input Noise Injection**

The common goal is:

[
\boxed{\text{Improve generalization and reduce overfitting}}
]

---

# 2. Data Augmentation

### Definition

**Data augmentation** is the process of creating additional training examples by applying small, realistic transformations to existing data.

Instead of collecting completely new data, we generate variations of existing examples.

### Examples

For **images**:

* Rotation
* Flipping
* Cropping
* Scaling
* Translation
* Brightness changes
* Small noise

For **audio**:

* Changing pitch
* Adding background noise
* Changing speed

For **text**:

* Synonym replacement
* Word deletion
* Small paraphrases

### Example

Suppose the original image is:

```text
       🐱
```

We can create variations by:

```text
Original → Rotate → Crop → Flip → Brightness change
```

All these images can still represent the same class.

### How it reduces overfitting

Data augmentation forces the model to learn **important features rather than memorizing exact training examples**.

For example, a cat should still be recognized as a cat even if the image is slightly rotated.

### Advantages

* Increases effective training-data diversity.
* Reduces overfitting.
* Improves generalization.
* Useful when collecting additional data is expensive.

---

# 3. Parameter Sharing / Parameter Tying

### Definition

**Parameter sharing** means using the **same model parameters in multiple locations** instead of learning separate parameters for each location.

This reduces the total number of independent parameters.

### Example: Convolutional Neural Networks

In a CNN, the same convolution filter is applied across different regions of an image.

```text
Image:

[ A B C D ]
[ E F G H ]
[ I J K L ]

        ↓
 Same filter
        ↓

Applied to multiple regions
```

Instead of learning a different filter for every image location, one filter is reused.

### Mathematical idea

Suppose the same parameter (w) is used at several locations:

[
y_1=f(x_1,w)
]

[
y_2=f(x_2,w)
]

[
y_3=f(x_3,w)
]

The same (w) is shared.

During training, gradients from all uses contribute to updating the shared parameter:

[
\boxed{
\frac{\partial L}{\partial w}
=============================

\sum_i
\frac{\partial L}{\partial w_i}
}
]

Conceptually, multiple observations help train the **same parameter**.

### How it reduces overfitting

Fewer independent parameters means fewer ways for the model to memorize the training data.

### Advantages

* Reduces model size.
* Reduces number of parameters.
* Improves generalization.
* Exploits repeated patterns or structures.

### Applications

* CNNs → convolution filters
* RNNs → same weights reused across time steps
* Siamese networks → shared weights between branches

---

# 4. Input Noise Injection

### Definition

**Input noise injection** means deliberately adding small amounts of random noise to the input during training.

Instead of training on:

[
x
]

the network is trained on:

[
\boxed{
\tilde{x}=x+\epsilon
}
]

where (\epsilon) is random noise.

For example:

[
x=[0.5,0.8,0.3]
]

After adding small noise:

[
\tilde{x}=[0.51,0.78,0.32]
]

The model should still produce approximately the same target output.

---

## Types of Noise

Common types include:

### Gaussian noise

[
\epsilon\sim N(0,\sigma^2)
]

### Salt-and-pepper noise

Random pixels are changed or removed, commonly used for image data.

### Masking noise

Some input values are randomly set to zero.

---

# 5. How Input Noise Prevents Overfitting

If a model is trained only on perfectly clean inputs, it may memorize very specific patterns.

Adding noise forces the model to learn **robust features**.

For example:

```text
Clean Input
     ↓
+ Random Noise
     ↓
Noisy Input
     ↓
Neural Network
     ↓
Same Target
```

The network learns:

> "Small changes in the input should not completely change my prediction."

This improves generalization to unseen and imperfect data.

---

# 6. Comparison

| Strategy                    | Main Idea                            | How It Regularizes                       |
| --------------------------- | ------------------------------------ | ---------------------------------------- |
| **Data Augmentation**       | Create transformed training examples | Increases data diversity                 |
| **Parameter Sharing/Tying** | Reuse the same parameters            | Reduces number of independent parameters |
| **Input Noise Injection**   | Add random noise to inputs           | Forces robust feature learning           |

---

# 7. Key Differences

### Data Augmentation

[
\boxed{\text{More varied training examples}}
]

### Parameter Sharing

[
\boxed{\text{Fewer independent parameters}}
]

### Input Noise

[
\boxed{\text{More robust representations}}
]

All three reduce the model's ability to simply **memorize the training dataset**.

---

## 8. Conclusion

**Data augmentation** reduces overfitting by creating realistic variations of training examples. **Parameter sharing or tying** reduces the number of independent parameters by reusing the same weights across different locations or time steps. **Input noise injection** adds random perturbations to training inputs, forcing the network to learn robust features instead of memorizing exact input patterns. Together, these techniques improve the **generalization ability and robustness** of neural networks.
