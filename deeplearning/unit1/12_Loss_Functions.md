# Topic 12: Loss Functions (MSE & Cross Entropy)

A **Loss Function** measures **how wrong a neural network's prediction is**. During training, the model tries to **minimize the loss**, so its predictions become more accurate.

> **Exam Importance:** ⭐⭐⭐⭐⭐ (Very Frequently Asked)

---

# ELI5 (Explain Like I'm 5)

Imagine you're throwing darts at a target.

* If the dart hits the center → Very small error.
* If it lands far away → Large error.

The **distance from the center** is like the **loss**.

The goal is to make the loss as small as possible.

---

# What is a Loss Function?

A **Loss Function** is a mathematical function that calculates the difference between:

* **Actual Output (Target)**
* **Predicted Output**

Smaller loss = Better prediction

Larger loss = Worse prediction

---

# Training Process

```text
Input Data
     ↓
Neural Network
     ↓
Prediction
     ↓
Loss Function
     ↓
Error
     ↓
Update Weights
     ↓
Better Prediction
```

The loss value tells the model **how much it needs to improve**.

---

# Why Do We Need Loss Functions?

Without a loss function:

* The model doesn't know whether its prediction is good or bad.
* It cannot improve its weights.
* Learning cannot happen.

A loss function acts like a **scorecard** for the model.

---

# Types in Your Syllabus

1. Mean Squared Error (MSE)
2. Cross Entropy Loss

---

# 1. Mean Squared Error (MSE)

MSE is mainly used for **Regression Problems**, where the output is a continuous value.

Examples:

* House Price Prediction
* Temperature Prediction
* Stock Price Prediction

---

## Formula

[
\boxed{\text{MSE}=\frac{1}{n}\sum_{i=1}^{n}(y_i-\hat{y}_i)^2}
]

Where:

* (y_i) = Actual value
* (\hat{y}_i) = Predicted value
* (n) = Number of samples

---

# Why Do We Square the Error?

Suppose:

Actual = 10

Prediction = 8

Error = 2

Now,

Actual = 10

Prediction = 12

Error = -2

If we simply add errors:

2 + (-2) = 0 ❌

The errors cancel each other.

By squaring:

[
2^2 = 4
]

[
(-2)^2 = 4
]

Now both contribute positively.

---

# Worked Example (MSE)

Actual values:

[
[5,;8,;10]
]

Predicted values:

[
[4,;9,;8]
]

### Step 1: Errors

| Actual | Predicted | Error |
| ------ | --------- | ----- |
| 5      | 4         | 1     |
| 8      | 9         | -1    |
| 10     | 8         | 2     |

---

### Step 2: Square Errors

| Error | Squared Error |
| ----- | ------------- |
| 1     | 1             |
| -1    | 1             |
| 2     | 4             |

---

### Step 3: Average

[
\frac{1+1+4}{3}=2
]

**MSE = 2**

---

# Advantages of MSE

* Easy to calculate.
* Penalizes large errors more heavily.
* Widely used in regression.

---

# Disadvantages of MSE

* Sensitive to outliers.
* Not suitable for classification problems.

---

# 2. Cross Entropy Loss

Cross Entropy is mainly used for **Classification Problems**.

Examples:

* Spam Detection
* Cat vs Dog
* Digit Recognition
* Disease Prediction

---

# Binary Cross Entropy Formula

[
\boxed{
L=-(y\log(p)+(1-y)\log(1-p))
}
]

Where:

* (y) = Actual class (0 or 1)
* (p) = Predicted probability

---

# Intuition

Suppose:

Actual:

Cat

Prediction:

Cat = 0.99

Loss:

Very small ✅

Now suppose:

Prediction:

Cat = 0.10

Loss:

Very large ❌

Cross Entropy strongly penalizes **confident wrong predictions**.

---

# Worked Example

Actual class:

1

Prediction:

0.90

Loss:

Very small

---

Another prediction:

0.10

Loss:

Very large

The closer the predicted probability is to the true class, the smaller the Cross Entropy loss.

---

# MSE vs Cross Entropy

| Feature     | MSE               | Cross Entropy              |
| ----------- | ----------------- | -------------------------- |
| Used For    | Regression        | Classification             |
| Output Type | Continuous        | Classes/Probabilities      |
| Measures    | Squared Error     | Difference in Probability  |
| Better For  | Regression Models | Neural Network Classifiers |

---

# Which Loss Function Should You Use?

| Problem                | Loss Function |
| ---------------------- | ------------- |
| House Price Prediction | MSE           |
| Temperature Prediction | MSE           |
| Spam Detection         | Cross Entropy |
| Cat vs Dog             | Cross Entropy |
| Digit Recognition      | Cross Entropy |

---

# Real-World Examples

## House Price Prediction

Actual Price:

₹50 lakh

Predicted:

₹47 lakh

Use:

**MSE**

---

## Spam Detection

Prediction:

Spam = 0.98

Actual:

Spam

Use:

**Binary Cross Entropy**

---

## Digit Recognition

Prediction:

Digit 7 = 0.95

Use:

**Cross Entropy**

---

# Loss vs Accuracy

Students often confuse these.

| Loss                      | Accuracy                                   |
| ------------------------- | ------------------------------------------ |
| Measures prediction error | Measures percentage of correct predictions |
| Lower is better           | Higher is better                           |
| Used during training      | Used for evaluation                        |

Example:

Loss = 0.12 ✅ Good

Accuracy = 98% ✅ Good

---

# Exam Definition (2–3 Marks)

**Loss Function:**
A loss function is a mathematical function that measures the difference between the predicted output and the actual output. It guides the neural network during training by indicating how much the model needs to improve.

---

# Frequently Asked Exam/Interview Questions

1. What is a loss function?
2. Why is a loss function required?
3. Write the formula for MSE.
4. Write the formula for Cross Entropy Loss.
5. Differentiate between MSE and Cross Entropy.
6. Which loss function is used for regression and which for classification?

---

# Must-Remember Formulas

### Mean Squared Error

[
\boxed{\text{MSE}=\frac{1}{n}\sum(y-\hat{y})^2}
]

---

### Binary Cross Entropy

[
\boxed{
L=-(y\log(p)+(1-y)\log(1-p))
}
]

---

# Must-Remember Points

* Loss measures prediction error.
* Lower loss means better predictions.
* MSE is used for regression.
* Cross Entropy is used for classification.
* Loss guides the learning process by helping update weights.

---

# Quick Revision Bullets

* Loss = Error between prediction and actual value.
* MSE → Regression.
* Cross Entropy → Classification.
* Lower loss = Better model.
* Training aims to minimize loss.
* Loss is different from accuracy.

---

# Mini Revision Sheet (Topics 10–12)

| Topic                | Key Idea                     |
| -------------------- | ---------------------------- |
| Representation Power | MLPs learn complex functions |
| Activation Functions | Introduce non-linearity      |
| Loss Functions       | Measure prediction error     |

---

# Mini Quiz

### Q1

Which loss function is mainly used for **House Price Prediction**?

A. Cross Entropy

B. MSE

C. Softmax

D. ReLU

---

### Q2

Which loss function is commonly used for **Spam Detection**?

A. MSE

B. Cross Entropy

C. Tanh

D. ReLU

---

### Q3

True or False:

Lower loss indicates better model performance.

---

# Active Learning

### Conceptual Questions

1. Why is a loss function essential during training?
2. Why is MSE not suitable for classification problems?
3. What is the difference between loss and accuracy?

### Practical Question

Choose the correct loss function for each problem and explain why:

1. Predicting house prices.
2. Classifying emails as spam or not spam.
3. Recognizing handwritten digits (0–9).

---

## Topic Connection

So far you've learned:

* **Activation Function** → Decides the neuron's output.
* **Loss Function** → Measures how wrong the prediction is.

The next question is:

**How does the model reduce this loss?**

The answer is **Gradient Descent**, an optimization algorithm that updates the weights in the direction that reduces the loss.

**Next Topic:** **Gradient Descent**.
