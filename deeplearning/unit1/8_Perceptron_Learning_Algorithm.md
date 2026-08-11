# Topic 8: Perceptron Learning Algorithm

The **Perceptron Learning Algorithm (PLA)** is the method used by a Perceptron to **learn from its mistakes**. It adjusts the weights and bias whenever the prediction is incorrect, allowing the model to improve over time.

> **Exam Importance:** ⭐⭐⭐⭐⭐ (Very Frequently Asked)

---

# ELI5 (Explain Like I'm 5)

Imagine a teacher checking a math test.

* Student answers correctly → No correction needed.
* Student answers incorrectly → Teacher explains the mistake.

The next time, the student performs better.

The Perceptron works the same way:

1. Make a prediction.
2. Compare it with the correct answer.
3. If wrong, update the weights.
4. Repeat until the predictions become correct.

---

# What is the Perceptron Learning Algorithm?

The **Perceptron Learning Algorithm** is an iterative algorithm that trains a Perceptron by updating its weights and bias based on the prediction error.

It continues this process until:

* All training examples are classified correctly, **or**
* The maximum number of training iterations (epochs) is reached.

---

# Learning Process

```text id="pla001"
Initialize Weights
        ↓
Read Training Example
        ↓
Calculate Prediction
        ↓
Compare with Actual Output
        ↓
Correct?
   ↙           ↘
Yes             No
 ↓               ↓
Next Sample   Update Weights
        ↖──────────────↙
Repeat Until Training Ends
```

---

# Step-by-Step Algorithm

### Step 1

Initialize:

* Weights = Small random values or zeros.
* Bias = 0.

---

### Step 2

Provide one training example.

Example:

Input:

x = (x₁, x₂)

Target:

t

---

### Step 3

Calculate the weighted sum.

[
z = \sum x_iw_i + b
]

---

### Step 4

Apply the step activation function.

[
y =
\begin{cases}
1, & z \geq 0 \
0, & z < 0
\end{cases}
]

---

### Step 5

Compare prediction with target.

If:

[
y = t
]

No update is required.

If:

[
y \neq t
]

Update the weights and bias.

---

### Step 6

Repeat the process for all training samples.

One complete pass through the dataset is called an **Epoch**.

Training continues until the model learns or the maximum number of epochs is reached.

---

# Weight Update Formula

The Perceptron updates its weights using:

[
w_{\text{new}} = w_{\text{old}} + \eta (t - y)x
]

Bias update:

[
b_{\text{new}} = b_{\text{old}} + \eta (t - y)
]

Where:

| Symbol       | Meaning                |
| ------------ | ---------------------- |
| (w)          | Weight                 |
| (\eta) (eta) | Learning Rate          |
| (t)          | Target (Actual Output) |
| (y)          | Predicted Output       |
| (x)          | Input                  |
| (b)          | Bias                   |

---

# Understanding the Formula

Suppose:

* Target = 1
* Prediction = 0

Error:

[
t-y = 1
]

The weights increase to make it easier for the neuron to predict **1** next time.

Now suppose:

* Target = 0
* Prediction = 1

Error:

[
t-y = -1
]

The weights decrease so the neuron is less likely to predict **1** in similar situations.

---

# Worked Example

Given:

Inputs:

* x₁ = 2
* x₂ = 1

Weights:

* w₁ = 0.5
* w₂ = 0.2

Bias:

* b = 0

Learning Rate:

[
\eta = 0.1
]

Target:

[
t = 1
]

Prediction:

[
y = 0
]

---

## Step 1: Error

[
t-y = 1-0 = 1
]

---

## Step 2: Update Weight 1

[
w_1 = 0.5 + (0.1)(1)(2)
]

[
w_1 = 0.7
]

---

## Step 3: Update Weight 2

[
w_2 = 0.2 + (0.1)(1)(1)
]

[
w_2 = 0.3
]

---

## Step 4: Update Bias

[
b = 0 + (0.1)(1)
]

[
b = 0.1
]

Updated values:

* w₁ = 0.7
* w₂ = 0.3
* b = 0.1

The model has now learned from its mistake.

---

# What is Learning Rate (η)?

The **Learning Rate** determines how large each weight update should be.

| Learning Rate | Effect                          |
| ------------- | ------------------------------- |
| Very Small    | Learning is slow                |
| Very Large    | May overshoot the best solution |
| Moderate      | Faster and more stable learning |

Typical values:

* 0.01
* 0.05
* 0.1

---

# Pseudocode

```text id="pla002"
Initialize weights and bias

Repeat until training ends:

    For each training example:

        Compute output

        Compare with target

        If prediction is wrong:

            Update weights

            Update bias
```

---

# Real-World Example

### Email Spam Detection

Inputs:

* Contains "Win Prize"
* Unknown Sender
* Too Many Links

Initially, the Perceptron may classify many spam emails incorrectly.

Each mistake causes the weights to change.

After many training iterations, it learns to classify emails more accurately.

---

# Advantages

* Very simple learning algorithm.
* Fast training.
* Easy to implement.
* Guaranteed to converge for linearly separable data.

---

# Limitations

* Works only for linearly separable datasets.
* Cannot solve XOR.
* Uses only a single layer.
* Uses a hard step activation function.

These limitations led to the development of the **Multilayer Perceptron (MLP)**.

---

# Exam Definition (2–3 Marks)

**Perceptron Learning Algorithm:**
The Perceptron Learning Algorithm is an iterative training algorithm that updates the weights and bias of a Perceptron whenever the predicted output differs from the target output, enabling the model to learn from its errors.

---

# Frequently Asked Exam/Interview Questions

1. Explain the Perceptron Learning Algorithm.
2. Write the weight update formula.
3. What is the role of the learning rate?
4. How are weights updated in a Perceptron?
5. Why can't the Perceptron Learning Algorithm solve XOR?

---

# Must-Remember Formulas

### Weighted Sum

[
z=\sum x_iw_i+b
]

### Weight Update

[
w_{\text{new}}=w_{\text{old}}+\eta(t-y)x
]

### Bias Update

[
b_{\text{new}}=b_{\text{old}}+\eta(t-y)
]

---

# Must-Remember Points

* Proposed for training the Perceptron.
* Updates weights only when the prediction is wrong.
* Learning Rate controls the size of updates.
* Repeats training for multiple epochs.
* Converges only for linearly separable data.
* Cannot solve XOR.

---

# Quick Revision Bullets

* Predict → Compare → Update → Repeat.
* Update only if prediction is incorrect.
* Weight Update = Old Weight + η(Target − Prediction) × Input.
* Bias is also updated.
* Learning Rate controls learning speed.
* Stops when predictions become correct or the maximum epochs are reached.

---

# Mini Connection (Topics 1–8)

| Topic                         | Main Idea                               |
| ----------------------------- | --------------------------------------- |
| Deep Learning                 | Learning patterns using neural networks |
| Biological Neuron             | Inspiration from the human brain        |
| Artificial Neuron             | Mathematical model of a neuron          |
| History                       | Evolution of neural networks            |
| MCP Neuron                    | First artificial neuron                 |
| Threshold Logic               | Decision rule                           |
| Perceptron                    | First trainable neural network          |
| Perceptron Learning Algorithm | Method to update weights and learn      |

---

# Active Learning

### Conceptual Questions

1. Why are weights updated only when the prediction is incorrect?
2. What is the role of the learning rate (η)?
3. What is an epoch?

### Practical Question

A Perceptron has:

* x = 3
* Current weight = 0.4
* Learning rate = 0.2
* Target = 1
* Prediction = 0

Using the Perceptron Learning Rule, calculate the **new weight**.

---

## Coming Next

The Perceptron can only solve **linearly separable problems**.

But what about problems like **XOR**, which a single Perceptron cannot solve?

To overcome this limitation, we introduce the **Multilayer Perceptron (MLP)**—a network with one or more hidden layers that can learn much more complex patterns.
