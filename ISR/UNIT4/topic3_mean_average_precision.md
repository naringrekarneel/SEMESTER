# Mean Average Precision (MAP) — 10 Marks

## 1. Definition

**Mean Average Precision (MAP)** is an evaluation metric used in Information Retrieval to measure the **quality of the ranking of relevant documents across multiple queries**.

Unlike simple Precision, MAP considers **where the relevant documents appear in the ranked results**.

In simple words:
> **MAP measures how well a search system ranks all relevant documents toward the top of the results.**

---

## 2. Average Precision (AP)

Before understanding MAP, we first need to understand **Average Precision (AP)**.

For a single query, AP is calculated by taking the **Precision at every position where a relevant document occurs**, adding those values, and dividing by the total number of relevant documents.

### Formula

$$
AP = \frac{\sum_{k=1}^{n} P@k \times rel(k)}{R}
$$

Where:
* $P@k$ = Precision at rank $k$
* $rel(k)$ = 1 if the document at rank $k$ is relevant, otherwise 0
* $R$ = Total number of relevant documents for that query
* $n$ = Number of retrieved results considered

---

## 3. What is MAP?

**MAP** is simply the mean (average) of the Average Precision values for all queries.

### Formula

$$
MAP = \frac{1}{Q}\sum_{i=1}^{Q} AP_i
$$

Where:
* $Q$ = Number of queries
* $AP_i$ = Average Precision for query $i$

---

## 4. Suitable Example

Suppose a search system retrieves **6 documents** for a query.

Assume the relevance is:

| Rank | Document | Relevant? |
| ---: | :--- | :--- |
| 1 | D1 | Yes |
| 2 | D2 | No |
| 3 | D3 | Yes |
| 4 | D4 | No |
| 5 | D5 | Yes |
| 6 | D6 | No |

There are **3 relevant documents** in total.

---

### Step 1: Calculate Precision at Relevant Positions

#### Rank 1
Relevant document is found.
$$
P@1 = \frac{1}{1}=1
$$

#### Rank 3
There are 2 relevant documents among the first 3 results.
$$
P@3 = \frac{2}{3}=0.667
$$

#### Rank 5
There are 3 relevant documents among the first 5 results.
$$
P@5 = \frac{3}{5}=0.6
$$

We only consider the positions where a relevant document occurs.

---

### Step 2: Calculate Average Precision

$$
AP = \frac{P@1+P@3+P@5}{3}
$$
$$
AP = \frac{1+0.667+0.6}{3}
$$
$$
AP = \frac{2.267}{3}
$$
$$
\boxed{AP \approx 0.756}
$$

So:
$$
AP \approx 75.6\%
$$

---

## 5. MAP Example with Two Queries

Now suppose the search system has two queries.

### Query 1
$$
AP_1 = 0.756
$$

### Query 2
Suppose its calculated Average Precision is:
$$
AP_2 = 0.833
$$

Then:
$$
MAP = \frac{AP_1+AP_2}{2}
$$
$$
MAP = \frac{0.756+0.833}{2}
$$
$$
MAP = 0.7945
$$

Therefore:
$$
\boxed{MAP \approx 0.795}
$$
or:
$$
\boxed{MAP \approx 79.5\%}
$$

---

## 6. Why MAP is Important

MAP evaluates not only **whether relevant documents were retrieved**, but also **how highly they were ranked**.

Consider two systems:

### System A
```text
Rank 1 → Relevant
Rank 2 → Relevant
Rank 3 → Non-relevant
Rank 4 → Relevant
```

### System B
```text
Rank 1 → Non-relevant
Rank 2 → Non-relevant
Rank 3 → Relevant
Rank 4 → Relevant
```

Both may retrieve the same number of relevant documents, but **System A places them earlier**, so its AP will generally be higher.
Thus MAP evaluates the **quality of the ranking**, not just the number of relevant results.

---

## 7. MAP vs Precision

### Precision
Precision measures:
> **Of the documents retrieved, how many are relevant?**

$$
Precision = \frac{TP}{TP+FP}
$$

It does not inherently consider the exact positions of relevant documents.

### MAP
MAP considers:
* Whether documents are relevant
* **Where those relevant documents occur in the ranking**
* Performance across **multiple queries**

Therefore, MAP provides more information about ranking quality.

---

## 8. MAP vs Recall

### Recall
Recall measures:
> **Of all relevant documents available, how many were retrieved?**

$$
Recall = \frac{TP}{TP+FN}
$$

Recall does not directly consider the ranking position of the retrieved documents.

### MAP
MAP focuses on **ranking relevant documents highly**, while recall focuses on **retrieving as many relevant documents as possible**.

---

## 9. Difference Between Precision, Recall and MAP

| Metric | What it measures | Considers ranking? | Multiple queries? |
| :--- | :--- | :--- | :--- |
| **Precision** | Fraction of retrieved documents that are relevant | Not inherently | Can be calculated per query |
| **Recall** | Fraction of all relevant documents that are retrieved | No | Can be calculated per query |
| **AP** | Ranking quality for one query | Yes | No |
| **MAP** | Average ranking quality across queries | Yes | **Yes** |

---

## 10. Simple Comparison Example

Suppose there are **5 relevant documents** in the collection.
A system retrieves only the first **2**, and both are relevant.

Then:
$$
Precision = \frac{2}{2}=1=100\%
$$

But:
$$
Recall = \frac{2}{5}=0.4=40\%
$$

This shows:
* Precision is excellent.
* Recall is low.

MAP adds another dimension by asking:
> **Were those relevant documents ranked near the top?**

---

## 11. Advantages of MAP

1. **Evaluates Ranking Quality:** It rewards systems that put relevant documents near the top.
2. **Considers Multiple Relevant Documents:** Unlike MRR, MAP considers **all relevant documents**.
3. **Useful for Comparing IR Systems:** A single MAP value can summarize performance across many queries.
4. **More Informative Than Simple Precision:** It accounts for the positions of relevant results.

---

## 12. Limitations of MAP

1. **Requires Relevance Judgments:** The system needs to know which documents are relevant.
2. **Sensitive to Missing Relevant Documents:** If relevant documents are not retrieved, AP can be reduced.
3. **Less Suitable for Single-Answer Tasks:** For questions where only one correct answer matters, **MRR** may be more appropriate.
4. **Interpretation Is Less Intuitive:** Precision is easier for beginners to understand than AP/MAP.

---

## 13. MAP vs MRR

This is a very useful exam distinction.

| MAP | MRR |
| :--- | :--- |
| Considers **all relevant documents** | Considers only the **first relevant document** |
| Evaluates overall ranking quality | Focuses on first correct result |
| Good for document retrieval | Good for QA and single-answer tasks |
| Uses Precision at relevant ranks | Uses $1/rank$ |

### Memory trick:
> **MRR = First relevant result**
> **MAP = All relevant results**

---

## 14. Conclusion

**Mean Average Precision (MAP)** is an important Information Retrieval evaluation metric that measures the **average ranking quality of relevant documents across multiple queries**.

For each query, **Average Precision (AP)** is calculated using Precision values at the ranks where relevant documents occur. The AP values are then averaged to obtain MAP.

The key difference is:
> **Precision asks "How many retrieved results are relevant?"**
> **Recall asks "How many relevant results did we find?"**
> **MAP asks "How well are all relevant results ranked across queries?"**

### ⭐ Exam keywords
**MAP → Average Precision → Precision@K → Relevant Ranks → Ranking Quality → Multiple Queries → Mean**

### 🧠 One-line memory trick
> **MAP = Average of AP values, and AP rewards relevant documents appearing higher in the ranking.**
