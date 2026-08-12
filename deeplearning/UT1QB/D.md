# MSE and Cross-Entropy Loss Functions — 10 Marks

## 1. Introduction

A **loss function** measures how different the model's predicted output is from the actual target output. During training, the neural network tries to **minimize the loss** by adjusting its weights[...]

Two important loss functions are:

1. **Mean Squared Error (MSE)**
2. **Cross-Entropy Loss**

The choice of loss function depends mainly on whether the problem is **regression or classification**.

---

# 2. Mean Squared Error (MSE)

### Definition

**Mean Squared Error** measures the average squared difference between the actual values and predicted values.

The formula is:

$$
\mathrm{MSE} = \frac{1}{n}\sum_{i=1}^{n}\bigl(y_i - \hat{y}_i\bigr)^2
$$

Where:

* $n$ = number of samples  
* $y_i$ = actual value  
* $\hat{y}_i$ = predicted value

### Example

Suppose actual values are:

$y = [2,\,4,\,6]$

and predictions are:

$\hat{y} = [3,\,5,\,5]$

Then:

$$
\mathrm{MSE} = \frac{(2-3)^2 + (4-5)^2 + (6-5)^2}{3}
       = \frac{1 + 1 + 1}{3} = 1
$$

Therefore, the MSE is **1**.

### Characteristics of MSE

* Squares the prediction error.  
* Large errors are penalized more heavily.  
* Always produces a **non-negative value**.  
* $\mathrm{MSE}=0$ means predictions are exactly correct.  
* It is differentiable and suitable for gradient-based optimization.

---

# 3. When is MSE Preferred?

MSE is mainly preferred for **regression problems**, where the output is a continuous numerical value.

### Examples:

* Predicting house prices  
* Predicting temperature  
* Predicting sales  
* Predicting student marks  
* Predicting stock values

For example:

> Actual house price = ₹50 lakh  
> Predicted house price = ₹48 lakh

MSE can measure the numerical difference between these values.

MSE can also be used in some neural-network applications with continuous outputs, but it is **generally not the preferred loss for classification**.

---

# 4. Cross-Entropy Loss

### Definition

**Cross-Entropy Loss** measures the difference between the **actual probability distribution** and the **predicted probability distribution** produced by a classification model.

For binary classification, Binary Cross-Entropy is:

$$
L = -\bigl[y\log(\hat{y}) + (1-y)\log(1-\hat{y})\bigr]
$$

Where:

* $y$ = actual label (0 or 1)  
* $\hat{y}$ = predicted probability of class 1

For multiple classes, categorical cross-entropy is:

$$
L = -\sum_{i=1}^{C} y_i \log(\hat{y}_i)
$$

where $C$ is the number of classes.

---

# 5. Example of Cross-Entropy

Suppose the actual class is:

$y = 1$

and the model predicts:

$\hat{y} = 0.9$

Then:

$$
L = -\log(0.9)
$$

which gives a small loss.

Now suppose the model predicts:

$\hat{y} = 0.1$

Then:

$$
L = -\log(0.1)
$$

which gives a much larger loss.

Thus, **Cross-Entropy strongly penalizes confident but incorrect predictions**.

---

# 6. When is Cross-Entropy Preferred?

Cross-Entropy is mainly preferred for **classification problems**.

### Examples:

* Spam vs non-spam classification  
* Disease vs healthy classification  
* Cat vs dog classification  
* Digit classification  
* Multi-class image classification

It is commonly paired with:

* **Sigmoid + Binary Cross-Entropy** → binary classification  
* **Softmax + Categorical Cross-Entropy** → multi-class classification

---

# 7. MSE vs Cross-Entropy

| **Feature**                | **MSE**                                               | **Cross-Entropy**                             |
| -------------------------- | ----------------------------------------------------- | --------------------------------------------- |
| Full form                  | Mean Squared Error                                    | Cross-Entropy Loss                            |
| Main use                   | Regression                                            | Classification                                |
| Formula                    | $\dfrac{1}{n}\sum (y - \hat{y})^2$                    | $-\sum y\log(\hat{y})$                        |
| Measures                   | Squared numerical error                               | Difference between probability distributions  |
| Output                     | Non-negative                                          | Non-negative                                  |
| Large errors               | Penalized strongly                                    | Confident wrong predictions heavily penalized |
| Common activation          | Linear output                                         | Sigmoid/Softmax                               |
| Example                    | House-price prediction                                | Image classification                          |
| Classification suitability | Generally less suitable                               | Highly suitable                               |
| Probability interpretation | Not naturally probabilistic                           | Naturally works with predicted probabilities  |

---

# 8. Key Difference

The easiest way to remember:

**MSE → "How far is my prediction from the actual number?"**

**Cross-Entropy → "How wrong is my predicted probability for the correct class?"**

For example, predicting:

> House price = ₹50 lakh → **MSE**

Predicting:

> Cat = 90%, Dog = 10% → **Cross-Entropy**

---

# 9. Conclusion

**MSE** calculates the average squared difference between actual and predicted values and is primarily preferred for **regression problems**. **Cross-Entropy** measures the difference between actual and predicted probability distributions and is primarily preferred for **classification problems**.
