# Topic 15: Feed Forward Neural Networks (FFNN)

A **Feed Forward Neural Network (FFNN)** is the simplest and most common type of artificial neural network. In an FFNN, **information flows only in one direction—from the input layer to the output layer—without any loops or feedback connections.**

> **Exam Importance:** ⭐⭐⭐⭐⭐ (Very Frequently Asked)

---

# ELI5 (Explain Like I'm 5)

Imagine a factory assembly line.

A toy moves through different stations:

* Station 1 → Adds wheels
* Station 2 → Paints the toy
* Station 3 → Packs the toy

The toy **never goes backward** to a previous station.

A Feed Forward Neural Network works the same way.

Information moves:

**Input → Hidden Layer(s) → Output**

There is **no backward flow of data during prediction**.

> **Note:** During **training**, errors are sent backward using **Backpropagation**, but during the **forward pass**, data always moves in one direction.

---

# What is a Feed Forward Neural Network?

A **Feed Forward Neural Network (FFNN)** is a neural network in which information passes from:

* **Input Layer**
* **Hidden Layer(s)**
* **Output Layer**

There are **no cycles, loops, or feedback connections**.

It is called **Feed Forward** because data only moves **forward**.

---

# Architecture of an FFNN

```text
             Input Layer
        x₁      x₂      x₃
          \      |      /
           \     |     /
            ▼    ▼    ▼

          Hidden Layer 1
        ●      ●      ●
          \    |    /
           \   |   /
            ▼  ▼  ▼

          Hidden Layer 2
           ●      ●
             \   /
              ▼ ▼

          Output Layer
               y
```

---

# Components of an FFNN

## 1. Input Layer

* Receives input features.
* Does not perform calculations.
* Passes data to the hidden layer.

Example:

For house price prediction:

* Area
* Bedrooms
* Age of house

---

## 2. Hidden Layer(s)

This is where learning happens.

Each neuron:

* Receives inputs.
* Multiplies by weights.
* Adds bias.
* Applies an activation function.
* Passes the output forward.

There can be:

* One hidden layer
* Multiple hidden layers (Deep Learning)

---

## 3. Output Layer

Produces the final prediction.

Examples:

* Spam / Not Spam
* Cat / Dog
* House Price
* Digit Recognition

---

# Working of an FFNN

### Step 1

Input data is given.

↓

### Step 2

Each neuron calculates the weighted sum.

[
z=\sum x_iw_i+b
]

↓

### Step 3

Apply an activation function.

[
a=f(z)
]

↓

### Step 4

The output becomes the input to the next layer.

↓

### Step 5

The final output layer generates the prediction.

---

# During Training

The complete learning cycle is:

```text
Input
   ↓
Forward Pass
   ↓
Prediction
   ↓
Loss Function
   ↓
Backpropagation
   ↓
Gradient Descent
   ↓
Updated Weights
```

Notice:

* **Forward Pass:** Data moves only forward.
* **Backward Pass:** Only the error moves backward during training.

---

# Mathematical Representation

For each neuron:

### Weighted Sum

[
z=\sum x_iw_i+b
]

### Activation

[
a=f(z)
]

The output of one layer becomes the input to the next layer until the final prediction is obtained.

---

# Worked Example

Suppose we want to predict whether an email is spam.

### Inputs

* Contains "Free Money" = 1
* Unknown Sender = 1
* Many Links = 0

↓

### Hidden Layer

Computes weighted sums and applies ReLU.

↓

### Output Layer

Applies Sigmoid.

↓

Output:

0.95

Prediction:

**Spam**

---

# Why is it Called "Feed Forward"?

Because information moves only in one direction.

```text
Input → Hidden → Output
```

There is **no feedback loop** from the output back to the input during prediction.

---

# FFNN vs Recurrent Neural Network (RNN)

| Feed Forward Neural Network | Recurrent Neural Network                                               |
| --------------------------- | ---------------------------------------------------------------------- |
| Data flows only forward     | Data can flow forward and backward through time (feedback connections) |
| No memory                   | Has memory of previous inputs                                          |
| Suitable for static data    | Suitable for sequential data                                           |
| Simpler architecture        | More complex architecture                                              |

> **Exam Tip:** Remember that FFNNs are used for **independent inputs**, while RNNs are designed for **sequential data** like text, speech, or time series.

---

# Applications

* Image Classification
* Spam Detection
* Handwritten Digit Recognition
* Medical Diagnosis
* House Price Prediction
* Fraud Detection

---

# Advantages

* Simple architecture.
* Easy to train.
* Fast prediction.
* Effective for many classification and regression tasks.
* Foundation of many neural network models.

---

# Limitations

* Cannot remember previous inputs.
* Not suitable for sequential or time-series data.
* May require many hidden layers for complex tasks.

---

# Exam Definition (2–3 Marks)

**Feed Forward Neural Network (FFNN):**
A Feed Forward Neural Network is an artificial neural network in which information flows only in the forward direction—from the input layer through one or more hidden layers to the output layer—without any feedback or cyclic connections.

---

# Frequently Asked Exam/Interview Questions

1. What is a Feed Forward Neural Network?
2. Draw the architecture of an FFNN.
3. Explain the working of an FFNN.
4. Why is it called a Feed Forward Neural Network?
5. Differentiate FFNN and RNN.
6. List the applications of FFNN.

---

# Must-Remember Formulas

### Weighted Sum

[
z=\sum x_iw_i+b
]

### Activation

[
a=f(z)
]

---

# Must-Remember Points

* Data flows only in one direction.
* No feedback loops or cycles.
* Consists of input, hidden, and output layers.
* Uses activation functions.
* Trained using Backpropagation and Gradient Descent.
* Suitable for classification and regression tasks.

---

# Quick Revision Bullets

* FFNN = Feed Forward Neural Network.
* Information flows only forward.
* No memory of previous inputs.
* Hidden layers perform computations.
* Uses Backpropagation for training.
* Widely used in deep learning applications.

---

# Mini Revision Sheet (Topics 13–15)

| Topic                       | Key Idea                                |
| --------------------------- | --------------------------------------- |
| Gradient Descent            | Updates weights to minimize loss        |
| Backpropagation             | Computes gradients using the Chain Rule |
| Feed Forward Neural Network | Data flows only from input to output    |

---

# Mini Quiz

### Q1

In an FFNN, information flows:

A. Backward only

B. Forward only

C. Both forward and backward during prediction

D. Randomly

---

### Q2

Which algorithm is used to train an FFNN?

A. K-Means

B. Decision Tree

C. Backpropagation

D. Naive Bayes

---

### Q3

True or False:

An FFNN has feedback loops during prediction.

---

# Active Learning

### Conceptual Questions

1. Why is it called a Feed Forward Neural Network?
2. What is the role of the hidden layer in an FFNN?
3. How is an FFNN different from an RNN?

### Practical Question

Design a simple FFNN for **house price prediction**.

1. What input features would you use?
2. How many output neurons are needed?
3. Which activation function would you use for the hidden layer?

---

## Topic Connection

You now understand:

* **How neurons compute outputs**
* **How MLPs are structured**
* **How FFNNs process information**
* **How Backpropagation and Gradient Descent train the network**

The final two topics in this unit are:

1. **Representation Power of Feed Forward Neural Networks**
2. **Model Evaluation Metrics**

These topics explain **what FFNNs can theoretically represent** and **how to measure a model's performance after training**.
