# Topic 16: Ensemble Methods

> **Exam Importance:** ⭐⭐⭐⭐⭐ — Important for exams and interviews

Ensemble learning means:

> **Combine multiple models to produce a better final prediction.**

Instead of trusting one model, we let several models "vote" or contribute to the final answer.

---

# ELI5 Explanation

Imagine you want to know whether a movie is good.

You ask one friend:

> "It's good."

You might trust them.

But if you ask **10 people**:

```text
8 → Good
2 → Bad
```

You're more confident that the movie is good.

That's the basic idea of an **ensemble**.

> **Many models together can often perform better than one model.**

---

# Basic Structure

Instead of:

```text
Input
  ↓
Model
  ↓
Prediction
```

we use:

```text
              ┌→ Model 1 ─→ Prediction
Input ────────┼→ Model 2 ─→ Prediction
              ├→ Model 3 ─→ Prediction
              └→ Model 4 ─→ Prediction
                         ↓
                  Combine Results
                         ↓
                  Final Prediction
```

---

# Why Does It Work?

Different models can make **different mistakes**.

Suppose:

```text
Model 1 → Wrong
Model 2 → Correct
Model 3 → Correct
Model 4 → Correct
```

The ensemble can still produce:

```text
Correct ✅
```

The key idea is:

> **Errors from different models can partially cancel each other.**

---

# Main Ensemble Methods

For your syllabus, understand these major approaches:

1. **Bagging**
2. **Boosting**
3. **Random Forest**
4. **Voting / Averaging**
5. **Stacking**

---

# 1. Bagging

Bagging stands for:

> **Bootstrap Aggregating**

The idea:

1. Create different training subsets.
2. Train separate models.
3. Combine their predictions.

```text
Dataset
   ↓
 ┌──────┬──────┬──────┐
 ↓      ↓      ↓
Data1  Data2  Data3
 ↓      ↓      ↓
Model1 Model2 Model3
  \      |      /
   \     |     /
    Combined
```

Bagging mainly helps reduce:

> **Variance / Overfitting**

---

# Example

Suppose three classifiers predict whether an email is spam.

```text
Model 1 → Spam
Model 2 → Not Spam
Model 3 → Spam
```

Majority vote:

```text
Spam = 2
Not Spam = 1
```

Final prediction:

[
\boxed{Spam}
]

---

# 2. Random Forest

Random Forest is a famous example of **bagging**.

It combines many **Decision Trees**.

```text
             Dataset
                ↓
       ┌────────┼────────┐
       ↓        ↓        ↓
     Tree 1   Tree 2   Tree 3
       ↓        ↓        ↓
       └────────┼────────┘
                ↓
          Majority Vote
                ↓
          Final Output
```

Each tree gets:

* Different samples.
* Random subsets of features.

This makes the trees somewhat different from each other.

---

# 3. Boosting

Boosting works differently.

Instead of training independent models, models are trained **sequentially**.

Each new model focuses more on mistakes made by previous models.

```text
Model 1
   ↓
Find mistakes
   ↓
Model 2 focuses on mistakes
   ↓
Find remaining mistakes
   ↓
Model 3 focuses on them
   ↓
Final prediction
```

Popular boosting algorithms:

* AdaBoost
* Gradient Boosting
* XGBoost
* LightGBM
* CatBoost

---

# Bagging vs Boosting

| Feature   | Bagging              | Boosting          |
| --------- | -------------------- | ----------------- |
| Training  | Parallel/independent | Sequential        |
| Main goal | Reduce variance      | Reduce bias       |
| Models    | Independent          | Dependent         |
| Example   | Random Forest        | AdaBoost, XGBoost |
| Focus     | Different samples    | Previous mistakes |

### Memory trick:

**Bagging = models work independently.**

**Boosting = models learn from previous mistakes.**

---

# 4. Voting

Used mainly for classification.

Suppose:

```text
Model 1 → Cat
Model 2 → Dog
Model 3 → Cat
```

Majority vote:

[
Cat=2
]

[
Dog=1
]

Final:

[
\boxed{Cat}
]

---

# Soft Voting

Instead of just looking at the predicted class, we can combine probabilities.

Example:

| Model   | Cat | Dog |
| ------- | --: | --: |
| Model 1 | 0.8 | 0.2 |
| Model 2 | 0.6 | 0.4 |
| Model 3 | 0.7 | 0.3 |

Average:

[
Cat=\frac{0.8+0.6+0.7}{3}
]

[
=0.70
]

Dog:

[
Dog=\frac{0.2+0.4+0.3}{3}
]

[
=0.30
]

Final:

[
\boxed{Cat}
]

---

# 5. Stacking

Stacking combines different types of models.

Example:

```text
              Input
                ↓
      ┌─────────┼─────────┐
      ↓         ↓         ↓
   Logistic   Decision   Neural
 Regression    Tree      Network
      ↓         ↓         ↓
      └─────────┼─────────┘
                ↓
          Meta Model
                ↓
        Final Prediction
```

The predictions of the first-level models become inputs to another model called the:

> **Meta-model**

---

# Why Ensembles Reduce Overfitting

Suppose:

```text
Model 1 → Error A
Model 2 → Error B
Model 3 → Error C
```

If their errors aren't perfectly correlated, combining them can reduce the overall error.

This is especially useful when individual models have different strengths and weaknesses.

---

# Simple Numerical Example

Three models predict house price:

```text
Model 1 → ₹50 lakh
Model 2 → ₹54 lakh
Model 3 → ₹52 lakh
```

Average:

[
\frac{50+54+52}{3}
]

[
=\boxed{52\text{ lakh}}
]

Instead of trusting one potentially inaccurate model, we use the combined prediction.

---

# Advantages

* Better predictive performance.
* Reduces variance.
* Can improve robustness.
* Often improves generalization.
* Combines different model strengths.

---

# Disadvantages

* More computationally expensive.
* More memory required.
* More difficult to interpret.
* Training multiple models can take longer.

---

# Exam/Interview Must-Remember

### Ensemble Learning

> Combining predictions from multiple models to obtain a stronger final model.

### Bagging

**Parallel + reduces variance**

Example:

**Random Forest**

### Boosting

**Sequential + focuses on errors**

Examples:

**AdaBoost, XGBoost**

### Stacking

**Multiple models + meta-model**

### Voting

**Majority/probability-based decision**

---

# Quick Revision

```text
Ensemble
   │
   ├── Bagging
   │      └── Random Forest
   │
   ├── Boosting
   │      ├── AdaBoost
   │      └── XGBoost
   │
   ├── Voting
   │
   └── Stacking
          └── Meta-model
```

### One-line memory:

> **"Don't bet everything on one model."**

---

# Connection

```text
L1/L2
   ↓
Early Stopping
   ↓
Dataset Augmentation
   ↓
Parameter Sharing
   ↓
Input Noise
   ↓
Ensemble Methods
   ↓
Next: Dropout
```

Dropout takes a very different approach:

> **Randomly turn off some neurons during training.**

---

# Active Learning

### Conceptual Questions

1. What is the main idea behind ensemble learning?
2. What is the difference between **bagging and boosting**?
3. Why can combining multiple models improve generalization?

### Practical Question

Three models classify an image:

```text
Model 1 → Cat
Model 2 → Dog
Model 3 → Cat
Model 4 → Cat
Model 5 → Dog
```

Using **majority voting**, what is the final prediction?

Also state whether this is an example of **hard voting or soft voting**.
