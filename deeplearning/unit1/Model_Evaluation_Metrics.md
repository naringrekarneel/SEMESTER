# Topic 17: Model Evaluation Metrics

After training a neural network, we need to **measure how well it performs**. **Model Evaluation Metrics** are numerical measures that help us evaluate the accuracy and reliability of a machine learning or deep learning model.

> **Exam Importance:** ⭐⭐⭐⭐⭐ (Very Frequently Asked)

---

# ELI5 (Explain Like I'm 5)

Imagine you took an exam.

Getting **80/100** tells you how well you performed.

Similarly, after a neural network makes predictions, we need a score to know **how good or bad its performance is**.

That score is called an **evaluation metric**.

---

# Why Do We Need Evaluation Metrics?

Training a model is not enough.

We must answer questions like:

* Is the model making correct predictions?
* How many mistakes does it make?
* Is it better than another model?

Evaluation metrics help answer these questions.

---

# Common Evaluation Metrics

Your syllabus mentions **Model Evaluation Metrics**, and the most commonly expected metrics in exams/interviews are:

1. Confusion Matrix
2. Accuracy
3. Precision
4. Recall
5. F1-Score

---

# 1. Confusion Matrix

A **Confusion Matrix** is a table that compares **actual values** with **predicted values**.

### Binary Classification Example

| Actual / Predicted | Positive | Negative |
| ------------------ | -------- | -------- |
| **Positive**       | TP       | FN       |
| **Negative**       | FP       | TN       |

---

## Terms

### True Positive (TP)

Actual = Positive

Prediction = Positive

Example:

Spam email correctly identified as spam.

---

### True Negative (TN)

Actual = Negative

Prediction = Negative

Example:

Normal email correctly identified as normal.

---

### False Positive (FP)

Actual = Negative

Prediction = Positive

Example:

A normal email is incorrectly marked as spam.

Also called a **Type I Error**.

---

### False Negative (FN)

Actual = Positive

Prediction = Negative

Example:

A spam email is incorrectly marked as normal.

Also called a **Type II Error**.

---

# Easy Memory Trick

| Prediction | Reality  | Result         |
| ---------- | -------- | -------------- |
| Positive   | Positive | True Positive  |
| Negative   | Negative | True Negative  |
| Positive   | Negative | False Positive |
| Negative   | Positive | False Negative |

---

# 2. Accuracy

Accuracy measures the **overall percentage of correct predictions**.

### Formula

[
\boxed{
Accuracy=\frac{TP+TN}{TP+TN+FP+FN}
}
]

---

## Worked Example

Suppose:

TP = 40

TN = 50

FP = 5

FN = 5

Accuracy:

[
\frac{40+50}{40+50+5+5}
=======================

# \frac{90}{100}

90%
]

---

# Advantages

* Easy to understand.
* Good when classes are balanced.

---

# Limitation

Accuracy can be misleading for **imbalanced datasets**.

Example:

99 healthy patients and 1 sick patient.

A model predicting **everyone as healthy** gets:

99% Accuracy

But it completely fails to detect the sick patient.

---

# 3. Precision

Precision measures:

> **Out of all predicted positives, how many were actually positive?**

### Formula

[
\boxed{
Precision=\frac{TP}{TP+FP}
}
]

---

## Example

Model predicts:

50 spam emails.

Actually spam:

45

Precision:

[
\frac{45}{50}=90%
]

---

## Used When

False Positives are costly.

Examples:

* Spam Detection
* Fraud Detection

---

# 4. Recall (Sensitivity)

Recall measures:

> **Out of all actual positives, how many were correctly identified?**

### Formula

[
\boxed{
Recall=\frac{TP}{TP+FN}
}
]

---

## Example

Actual spam emails:

60

Detected:

54

Recall:

[
\frac{54}{60}=90%
]

---

## Used When

Missing a positive case is dangerous.

Examples:

* Cancer Detection
* Disease Diagnosis
* Fraud Detection

---

# 5. F1-Score

Sometimes we need both:

* High Precision
* High Recall

F1-Score balances both using their harmonic mean.

### Formula

[
\boxed{
F1=
\frac{2\times Precision\times Recall}
{Precision+Recall}
}
]

---

## Example

Precision:

80%

Recall:

90%

F1:

Approximately 85%.

---

# Comparison Table

| Metric    | Measures                      | Best Used When                 |
| --------- | ----------------------------- | ------------------------------ |
| Accuracy  | Overall correctness           | Balanced datasets              |
| Precision | Correct positive predictions  | False Positives are costly     |
| Recall    | Ability to detect positives   | False Negatives are costly     |
| F1-Score  | Balance of Precision & Recall | Need both Precision and Recall |

---

# Which Metric Should You Use?

| Problem                | Best Metric      |
| ---------------------- | ---------------- |
| House Price Prediction | MSE (Regression) |
| Spam Detection         | Precision        |
| Cancer Detection       | Recall           |
| Fraud Detection        | Recall / F1      |
| Balanced Dataset       | Accuracy         |

---

# Worked Example

Given:

TP = 45

TN = 35

FP = 10

FN = 10

---

### Accuracy

[
\frac{45+35}{100}=80%
]

---

### Precision

[
\frac{45}{45+10}
================

81.8%
]

---

### Recall

[
\frac{45}{45+10}
================

81.8%
]

---

### F1-Score

Since Precision = Recall,

F1 ≈ 81.8%

---

# Real-World Examples

## Spam Detection

* High Precision
* Don't want normal emails marked as spam.

---

## Cancer Detection

* High Recall
* Better to detect every possible patient, even if some healthy people are flagged for further testing.

---

## Face Unlock

Accuracy tells how often the phone unlocks correctly.

Precision and Recall become important if the cost of false matches or missed matches is high.

---

# Exam Definition (2–3 Marks)

**Model Evaluation Metrics:**
Model Evaluation Metrics are quantitative measures used to assess the performance of a machine learning or deep learning model by comparing its predictions with the actual outcomes.

---

# Frequently Asked Exam/Interview Questions

1. What is a Confusion Matrix?
2. Explain TP, TN, FP, and FN.
3. Write the formula for Accuracy.
4. Differentiate Precision and Recall.
5. What is the F1-Score?
6. When should Accuracy not be used?

---

# Must-Remember Formulas

### Accuracy

[
\boxed{
Accuracy=\frac{TP+TN}{TP+TN+FP+FN}
}
]

---

### Precision

[
\boxed{
Precision=\frac{TP}{TP+FP}
}
]

---

### Recall

[
\boxed{
Recall=\frac{TP}{TP+FN}
}
]

---

### F1-Score

[
\boxed{
F1=
\frac{2\times Precision\times Recall}
{Precision+Recall}
}
]

---

# Must-Remember Points

* Confusion Matrix is the basis for most classification metrics.
* Accuracy is suitable for balanced datasets.
* Precision focuses on reducing False Positives.
* Recall focuses on reducing False Negatives.
* F1-Score balances Precision and Recall.
* Choose evaluation metrics based on the problem, not just the highest accuracy.

---

# Quick Revision Bullets

* TP = Correct Positive.
* TN = Correct Negative.
* FP = Incorrect Positive.
* FN = Incorrect Negative.
* Accuracy = Overall correctness.
* Precision = Correctness of predicted positives.
* Recall = Ability to find actual positives.
* F1-Score = Balance between Precision and Recall.

---

# Final Revision Sheet (Unit 1)

| Topic                         | Key Idea                                 |
| ----------------------------- | ---------------------------------------- |
| Biological Neuron             | Inspiration from the human brain         |
| Artificial Neuron             | Computational model of a neuron          |
| History                       | Evolution of Deep Learning               |
| McCulloch-Pitts Neuron        | First artificial neuron model            |
| Threshold Logic               | Binary decision making                   |
| Perceptron                    | First trainable neural network           |
| Perceptron Learning Algorithm | Updates weights using errors             |
| Multilayer Perceptron (MLP)   | Solves complex non-linear problems       |
| Representation Power of MLP   | Ability to learn complex functions       |
| Activation Functions          | Introduce non-linearity                  |
| Loss Functions                | Measure prediction error                 |
| Gradient Descent              | Optimizes weights to minimize loss       |
| Backpropagation               | Computes gradients using the Chain Rule  |
| Feed Forward Neural Network   | Forward-only data flow                   |
| Representation Power of FFNN  | Ability to approximate complex functions |
| Model Evaluation Metrics      | Measure model performance                |

---

# Unit 1 Mini Quiz

### Q1

Which activation function is most commonly used in hidden layers?

A. Sigmoid

B. ReLU

C. Softmax

D. Tanh

---

### Q2

Which loss function is used for binary classification?

A. MSE

B. Cross Entropy

C. MAE

D. Hinge Loss

---

### Q3

Which algorithm computes gradients?

A. Gradient Descent

B. Backpropagation

C. K-Means

D. PCA

---

### Q4

Which metric is most suitable for cancer detection?

A. Accuracy

B. Recall

C. Precision

D. MSE

---

### Q5

True or False:

A single-layer Perceptron can solve the XOR problem.

---

# Active Learning

### Conceptual Questions

1. Why is Accuracy not always the best evaluation metric?
2. When would you prefer Recall over Precision?
3. Why is the F1-Score useful?

### Practical Question

A model produced the following results:

* TP = 70
* TN = 20
* FP = 5
* FN = 5

Calculate:

1. Accuracy
2. Precision
3. Recall
4. F1-Score

---

## 🎉 Congratulations!

You have completed **Unit 1: Introduction to Deep Learning**.

You now understand:

* The inspiration behind neural networks.
* How artificial neurons and MLPs work.
* Activation functions, loss functions, and optimization.
* Backpropagation and Gradient Descent.
* Feed Forward Neural Networks.
* How to evaluate trained models.

This foundation is essential before moving on to more advanced topics such as **Convolutional Neural Networks (CNNs)**, **Recurrent Neural Networks (RNNs)**, **Transformers**, and other deep learning architectures.
