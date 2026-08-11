# Topic 19: Hyperparameter Tuning — Grid Search & Random Search

> **Exam Importance:** ⭐⭐⭐⭐⭐ — Very common in exams/interviews and essential in practical ML.

This is the **final topic** in your syllabus.

---

# ELI5 Explanation

Imagine you're making coffee.

You need to decide:

* How much coffee?
* How much milk?
* How much sugar?

You don't know the perfect combination beforehand.

So you try different combinations until you find one that tastes best.

That's **hyperparameter tuning**.

---

# What Is a Hyperparameter?

A **hyperparameter** is a value that we choose **before or during training**, rather than something the neural network learns automatically.

Examples:

| Hyperparameter          | Example |
| ----------------------- | ------: |
| Learning rate           |   0.001 |
| Batch size              |      32 |
| Number of layers        |       3 |
| Number of neurons       |     128 |
| Dropout rate            |     0.5 |
| Regularization strength |    0.01 |
| Number of epochs        |      50 |

---

# Hyperparameter vs Parameter

This distinction is very important.

### Parameters

Learned automatically during training.

Examples:

[
W,;b
]

Weights and biases.

### Hyperparameters

Set by us.

Examples:

[
learning\ rate,;batch\ size,;dropout
]

---

## Easy Memory

> **Parameters are learned. Hyperparameters are chosen.**

---

# What Is Hyperparameter Tuning?

It means:

> **Trying different hyperparameter values to find the combination that gives the best validation performance.**

For example:

```text id="8pfy1s"
Learning Rate:
0.1
0.01
0.001

Dropout:
0.2
0.5

Batch Size:
16
32
```

We test different combinations.

---

# Why Do We Need Tuning?

Suppose your model performs badly.

Maybe:

```text id="3b4kgg"
Learning rate too high
```

Or:

```text id="7lj3yo"
Learning rate too low
```

Or:

```text id="4yq4tc"
Dropout too high
```

Or:

```text id="n5ntz7"
Network too small
```

Hyperparameter tuning helps us find better settings.

---

# Two Important Methods

Your syllabus specifically mentions:

1. **Grid Search**
2. **Random Search**

---

# 1. Grid Search

Grid Search tries **every possible combination** from the values we specify.

Suppose:

### Learning Rate

```text
0.1
0.01
0.001
```

### Batch Size

```text
16
32
```

Total combinations:

[
3\times2=6
]

Grid Search tests all 6.

---

# Example

| Experiment | Learning Rate | Batch Size |
| ---------- | ------------: | ---------: |
| 1          |           0.1 |         16 |
| 2          |           0.1 |         32 |
| 3          |          0.01 |         16 |
| 4          |          0.01 |         32 |
| 5          |         0.001 |         16 |
| 6          |         0.001 |         32 |

Every combination is tested.

---

# Advantages of Grid Search

* Simple.
* Systematic.
* Doesn't miss any specified combination.
* Easy to understand.

---

# Disadvantages

The biggest problem:

> **It can be computationally expensive.**

Suppose we have:

```text
5 learning rates
× 5 batch sizes
× 4 dropout rates
× 3 optimizers
```

Experiments:

[
5\times5\times4\times3
]

[
=\boxed{300}
]

That's 300 training runs!

And deep learning models can take hours to train.

---

# 2. Random Search

Instead of testing every combination, Random Search **randomly selects combinations** from the search space.

Example:

```text id="jgy1tg"
Search Space

Learning Rate:
0.1 → 0.0001

Batch Size:
16 → 128

Dropout:
0 → 0.5
```

Random Search might try:

```text id="p4z5y9"
Trial 1 → LR=0.003, Batch=32, Dropout=0.2

Trial 2 → LR=0.0007, Batch=128, Dropout=0.4

Trial 3 → LR=0.02, Batch=16, Dropout=0.1

...
```

It doesn't try every combination.

---

# Why Can Random Search Be Better?

This is a very important interview concept.

Suppose we have:

```text
Learning Rate → VERY important
Dropout       → Less important
Batch Size    → Less important
```

Grid Search wastes many experiments exploring combinations of less important parameters.

Random Search can explore **more different learning-rate values**.

So with the same computational budget, Random Search can often find a good configuration faster.

---

# Grid vs Random Search

| Feature           | Grid Search                    | Random Search       |
| ----------------- | ------------------------------ | ------------------- |
| Selection         | Every combination              | Random combinations |
| Computation       | High                           | Usually lower       |
| Coverage          | Complete over specified grid   | Random              |
| Efficiency        | Can be poor in high dimensions | Often better        |
| Easy to implement | ✅                              | ✅                   |
| Deep learning     | Can be expensive               | Often preferred     |

---

# Worked Example

Suppose you have:

### Learning Rate

[
[0.1,0.01,0.001]
]

### Dropout

[
[0.2,0.5]
]

### Batch Size

[
[32,64]
]

Total combinations:

[
3\times2\times2
]

[
=\boxed{12}
]

---

## Grid Search

Grid Search tries all:

[
12
]

experiments.

---

## Random Search

Suppose you only have enough computing power for **5 experiments**.

Random Search might randomly choose 5 combinations.

```text id="q98jup"
12 possible combinations
        ↓
Randomly select
        ↓
5 experiments
```

Much cheaper.

---

# Validation Set

This is important.

We shouldn't select the best hyperparameters based on the **test set**.

Instead:

```text id="z9j4cd"
Training Data
     ↓
Train model

Validation Data
     ↓
Choose hyperparameters

Test Data
     ↓
Final evaluation
```

The test set should ideally be kept untouched until the final evaluation.

---

# Hyperparameter Tuning Workflow

```text id="l5f4e7"
Define search space
       ↓
Choose tuning method
       ↓
Train models
       ↓
Evaluate validation performance
       ↓
Choose best hyperparameters
       ↓
Train/finalize model
       ↓
Evaluate on test set
```

---

# Example Search Space

Suppose we're training a neural network.

```text
Learning Rate:
0.1, 0.01, 0.001

Batch Size:
32, 64

Dropout:
0.2, 0.5
```

Grid Search:

[
3\times2\times2=12
]

possible combinations.

Random Search:

Could evaluate only:

[
5
]

random combinations.

---

# Important Hyperparameters in Deep Learning

You should remember these:

### Optimization

* Learning rate
* Optimizer
* Momentum

### Architecture

* Number of layers
* Number of neurons
* Activation functions

### Regularization

* Dropout rate
* L1/L2 coefficient

### Training

* Batch size
* Number of epochs

---

# Grid Search vs Random Search — Exam Answer

If asked:

> **Differentiate Grid Search and Random Search.**

Write:

**Grid Search** systematically evaluates every combination of predefined hyperparameter values.

**Random Search** randomly samples combinations from the specified search space.

Grid Search can become computationally expensive as the number of hyperparameters increases, while Random Search generally explores large search spaces more efficiently under a fixed computational budget.

---

# Must-Remember

### Parameter

Learned by the model:

[
W,b
]

### Hyperparameter

Chosen before/during training:

[
LR,\ batch\ size,\ dropout
]

### Grid Search

> **Try everything.**

### Random Search

> **Try some random combinations.**

---

# Memory Trick

```text
GRID

● ● ●
● ● ●
● ● ●

Everything gets tested.
```

```text
RANDOM

●
    ●

  ●

Only selected points get tested.
```

So:

> **Grid = systematic**

> **Random = sampled**

---

# Quick Revision Sheet — Entire Syllabus

You've now covered the entire syllabus:

```text
OPTIMIZATION
│
├── Gradient Descent
├── Momentum
├── Nesterov Accelerated GD
├── Stochastic GD
├── AdaGrad
├── RMSProp
├── Adam
├── Learning Rate Scheduling
└── Weight Initialization
      ├── Xavier
      └── He
│
REGULARIZATION
│
├── Bias-Variance Tradeoff
├── L1/L2 Regularization
├── Early Stopping
├── Dataset Augmentation
├── Parameter Sharing & Tying
├── Input Noise
├── Ensemble Methods
├── Dropout
├── Batch Normalization
└── Hyperparameter Tuning
      ├── Grid Search
      └── Random Search
```

---

# 🔥 Ultra-Short Exam Revision

| Topic             | Remember This                            |
| ----------------- | ---------------------------------------- |
| GD                | Update weights using gradient            |
| Momentum          | Uses previous update direction           |
| NAG               | Looks ahead before calculating gradient  |
| SGD               | Uses individual/random training examples |
| AdaGrad           | Adapts LR based on past gradients        |
| RMSProp           | Fixes AdaGrad's aggressive LR decay      |
| Adam              | Momentum + adaptive learning rate        |
| LR Scheduling     | Change LR during training                |
| Xavier            | Sigmoid/Tanh                             |
| He                | ReLU                                     |
| Bias              | Underfitting                             |
| Variance          | Overfitting                              |
| L1                | Makes weights zero                       |
| L2                | Shrinks weights                          |
| Early Stopping    | Stop when validation stops improving     |
| Augmentation      | Create realistic data variations         |
| Parameter Sharing | Reuse parameters                         |
| Input Noise       | Add noise to improve robustness          |
| Ensemble          | Combine multiple models                  |
| Dropout           | Randomly disable neurons                 |
| BatchNorm         | Normalize activations                    |
| Grid Search       | Try every combination                    |
| Random Search     | Try random combinations                  |

---

# Final Mental Map

The whole unit can be remembered as:

```text
             DEEP LEARNING TRAINING
                     │
          ┌──────────┴──────────┐
          ↓                     ↓
     OPTIMIZATION          REGULARIZATION
          │                     │
     "How do I learn?"    "How do I avoid
                           overfitting?"
          │                     │
     GD → Momentum          L1/L2
     → NAG                  Dropout
     → AdaGrad              Early Stop
     → RMSProp              Augmentation
     → Adam                 Noise
          │                 Ensembles
     LR Scheduling          BatchNorm
     Initialization         Parameter Sharing
          │                     │
          └──────────┬──────────┘
                     ↓
             GOOD GENERALIZATION
```

### The single most important distinction:

> **Optimization techniques help the model learn better.**

> **Regularization techniques help the model generalize better.**

---

## Final Active-Learning Challenge

Since you've completed the entire unit, try these without looking back:

### 1. Conceptual

What is the difference between **Adam, RMSProp, and Momentum**?

### 2. Conceptual

Explain:

**High Bias → ?**

**High Variance → ?**

### 3. Conceptual

Differentiate **L1 and L2 regularization** in one or two sentences.

### 4. Practical

A neural network has:

* Training accuracy = **99%**
* Validation accuracy = **72%**

Name **three techniques from this syllabus** that could help and explain why.

### 5. Exam Question

Explain **Grid Search vs Random Search** with one example.

If you can answer these five, you've got a pretty solid grip on the entire **Optimization & Regularization** unit.
