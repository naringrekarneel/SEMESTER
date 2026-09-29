# Precision, Recall and F-Measure in Information Retrieval — 10 Marks

## 1. Introduction

In Information Retrieval (IR), a search system needs to be evaluated based on **how many retrieved documents are relevant** and **how many relevant documents were successfully retrieved**.

The three important measures are:
* **Precision** → How many retrieved documents are relevant?
* **Recall** → How many relevant documents were retrieved?
* **F-measure** → Balance between Precision and Recall.

---

## 2. Precision

### Definition
**Precision** is the proportion of retrieved documents that are actually relevant.

In simple words:
> **Precision tells us the accuracy of the retrieved results.**

### Formula

$$
Precision = \frac{Relevant\ Retrieved\ Documents}{Total\ Retrieved\ Documents}
$$

Using Information Retrieval terminology:

$$
Precision = \frac{TP}{TP+FP}
$$

Where:
* $TP$ = Relevant documents retrieved
* $FP$ = Non-relevant documents retrieved

### Example
Suppose a search engine retrieves **10 documents**, and **7 of them are relevant**.

Then:
$$
Precision = \frac{7}{10}=0.7
$$

So,
$$
Precision = 70\%
$$

### Interpretation
A precision of **70%** means that out of every 10 retrieved documents, about 7 are relevant.

---

## 3. Recall

### Definition
**Recall** is the proportion of all relevant documents in the collection that are successfully retrieved.

In simple words:
> **Recall tells us how completely the system finds the relevant information.**

### Formula

$$
Recall = \frac{Relevant\ Retrieved\ Documents}{Total\ Relevant\ Documents}
$$

or:

$$
Recall = \frac{TP}{TP+FN}
$$

Where:
* $TP$ = Relevant documents retrieved
* $FN$ = Relevant documents not retrieved

### Example
Suppose there are **20 relevant documents** in the entire collection, but the system retrieves **7 of them**.

Then:
$$
Recall = \frac{7}{20}=0.35
$$

Therefore:
$$
Recall = 35\%
$$

### Interpretation
A recall of **35%** means the system found 35% of all relevant documents available in the collection.

---

## 4. F-Measure

### Definition
The **F-measure** combines Precision and Recall into a single value.

The most commonly used form is the **F1-score**, which gives equal importance to Precision and Recall.

### Formula

$$
F_1 = \frac{2 \times Precision \times Recall}{Precision + Recall}
$$

It is the **harmonic mean** of Precision and Recall.

Why harmonic mean?
Because it gives a low score when either Precision or Recall is very low.

---

## 5. Suitable Example

Suppose a search system returns **10 documents**.

Out of these:
* **6 are relevant**
* **4 are not relevant**

The collection contains **10 relevant documents in total**.

Therefore:

### Step 1: Identify values
$$
TP=6
$$
$$
FP=4
$$
Since 10 relevant documents exist and 6 were retrieved:
$$
FN=10-6=4
$$

---

### Step 2: Calculate Precision
$$
Precision = \frac{TP}{TP+FP}
$$
$$
Precision = \frac{6}{6+4}
$$
$$
Precision = \frac{6}{10}=0.6
$$

Therefore:
$$
Precision=60\%
$$

---

### Step 3: Calculate Recall
$$
Recall = \frac{TP}{TP+FN}
$$
$$
Recall = \frac{6}{6+4}
$$
$$
Recall = \frac{6}{10}=0.6
$$

Therefore:
$$
Recall=60\%
$$

---

### Step 4: Calculate F1-Measure
$$
F_1 = \frac{2 \times 0.6 \times 0.6}{0.6+0.6}
$$
$$
F_1 = \frac{0.72}{1.2}=0.6
$$

Therefore:
$$
F_1=60\%
$$

---

## 6. Confusion Matrix

The measures can also be understood using four categories:

| | Relevant | Non-Relevant |
| :--- | ---: | ---: |
| **Retrieved** | TP = 6 | FP = 4 |
| **Not Retrieved** | FN = 4 | TN = — |

For IR, **TN (True Negative)** is generally less important for Precision and Recall calculations.

---

## 7. Difference Between Precision and Recall

| Precision | Recall |
| :--- | :--- |
| Measures accuracy of retrieved results | Measures completeness of retrieval |
| Focuses on retrieved documents | Focuses on all relevant documents |
| High precision → fewer irrelevant results | High recall → fewer relevant documents missed |
| Formula: $TP/(TP+FP)$ | Formula: $TP/(TP+FN)$ |
| Important when irrelevant results are costly | Important when missing relevant results is costly |

### Easy example
Suppose a search engine returns only **3 documents**, and all 3 are relevant.

Then precision is high:
$$
Precision=100\%
$$

But if there were actually 100 relevant documents and only 3 were retrieved:
$$
Recall=3\%
$$

So, **high precision does not necessarily mean high recall**.

---

## 8. Precision–Recall Trade-off

Usually, improving one measure can reduce the other.

* **High Precision:** The system retrieves fewer but highly relevant documents.
* **High Recall:** The system retrieves many potentially relevant documents, but some may be irrelevant.

Therefore, an IR system often tries to find a suitable balance between the two.

---

## 9. F-Measure with General $\beta$

The generalized F-measure is:

$$
F_\beta =
(1+\beta^2)
\frac{Precision \times Recall}
{\beta^2 \times Precision + Recall}
$$

Where:
* $\beta < 1$ → gives more importance to **Precision**
* $\beta > 1$ → gives more importance to **Recall**
* $\beta = 1$ → equal importance to both, giving **F1**

Thus:
$$
F_1 = \frac{2PR}{P+R}
$$

---

## 10. Applications

* **Precision is important when:**
  * Search results should contain very few irrelevant documents.
  * Users want highly specific results.

* **Recall is important when:**
  * Missing a relevant document is costly.
  * Searching medical, legal, or research collections.

* **F-measure is useful when:**
  * Both Precision and Recall are important.
  * A single evaluation score is required.

---

## 11. Summary Table

| Measure | Meaning | Formula |
| :--- | :--- | :--- |
| **Precision** | How many retrieved documents are relevant | $\frac{TP}{TP+FP}$ |
| **Recall** | How many relevant documents are retrieved | $\frac{TP}{TP+FN}$ |
| **F1-Measure**| Harmonic mean of Precision and Recall | $\frac{2PR}{P+R}$ |

---

## 12. Conclusion

**Precision, Recall, and F-measure are fundamental evaluation measures in Information Retrieval.** Precision measures the **accuracy of retrieved results**, Recall measures the **completeness of retrieval**, and F1-measure provides a **balance between Precision and Recall**.

For the example above:
$$
Precision = 60\%
$$
$$
Recall = 60\%
$$
$$
F_1 = 60\%
$$

### 🧠 Exam memory trick
> **Precision = Retrieved → How much is relevant?**
> **Recall = Relevant → How much did we retrieve?**
> **F1 = Balance between both.**
