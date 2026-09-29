# Mean Reciprocal Rank (MRR) — 10 Marks

## 1. Definition

**Mean Reciprocal Rank (MRR)** is an evaluation metric used in Information Retrieval to measure **how quickly a system returns the first relevant result**.

It is especially useful when the **position of the first relevant result** is important.

The key idea is:
> **The higher the first relevant result appears in the ranking, the higher the MRR score.**

---

## 2. Reciprocal Rank

For a single query, **Reciprocal Rank (RR)** is the reciprocal of the position of the **first relevant document**.

### Formula

$$
RR = \frac{1}{rank}
$$

Where `rank` is the position of the first relevant result.

### Example

Suppose the search results are:

| Rank | Result | Relevant? |
| ---: | :--- | :--- |
| 1 | D1 | No |
| 2 | D2 | Yes |
| 3 | D3 | No |
| 4 | D4 | Yes |

The **first relevant result** is at rank 2.

Therefore:
$$
RR = \frac{1}{2}=0.5
$$

Only the **first relevant result** matters for RR.

---

## 3. Mean Reciprocal Rank

When there are multiple queries, we calculate the reciprocal rank for each query and then take their average.

### Formula

$$
MRR = \frac{1}{N}\sum_{i=1}^{N}\frac{1}{rank_i}
$$

Where:
* $N$ = Number of queries
* $rank_i$ = Rank of the first relevant result for query $i$

---

## 4. Suitable Example

Suppose there are **4 queries**.

| Query | Rank of First Relevant Result | Reciprocal Rank |
| :--- | ---: | ---: |
| Q1 | 1 | $1/1 = 1.00$ |
| Q2 | 2 | $1/2 = 0.50$ |
| Q3 | 4 | $1/4 = 0.25$ |
| Q4 | 5 | $1/5 = 0.20$ |

Now calculate MRR:
$$
MRR=\frac{1.00+0.50+0.25+0.20}{4}
$$
$$
MRR=\frac{1.95}{4}=0.4875
$$

Therefore:
$$
\boxed{MRR=0.4875}
$$
or approximately:
$$
\boxed{48.75\%}
$$

---

## 5. Understanding the Score

MRR lies between **0 and 1**.

| MRR | Interpretation |
| ---: | :--- |
| **1.0** | First relevant result is always at rank 1 |
| **0.5** | Average first relevant result is around rank 2 |
| **0.25**| Average first relevant result is around rank 4 |
| **Near 0**| First relevant results appear very low in the ranking |

A higher MRR means the system tends to place the **first relevant result closer to the top**.

---

## 6. Special Case: No Relevant Result

Suppose a query returns **no relevant document**.
Its reciprocal rank is taken as:
$$
RR=0
$$

### Example

| Query | First Relevant Rank | RR |
| :--- | ---: | ---: |
| Q1 | 1 | 1 |
| Q2 | 3 | 0.333 |
| Q3 | None | 0 |

These values are included when calculating MRR.

---

## 7. Why Does MRR Focus on the First Relevant Result?

MRR is designed for tasks where the user mainly needs **one correct answer**.

For example, consider a question-answering system.
Query:
> `Who invented the telephone?`

If the correct answer appears at:
* Rank 1 → excellent
* Rank 2 → still useful
* Rank 10 → much less useful

MRR captures this difference directly.
It **does not give additional credit for having many relevant documents** after the first relevant result.

---

## 8. Applications of MRR

1. **Question Answering:** Used to measure how highly the first correct answer is ranked. Example: "What is the capital of Japan?" If the correct answer appears first, the reciprocal rank is 1.
2. **Search Engines:** Useful when users generally want one highly relevant result near the top.
3. **Chatbots:** Can evaluate whether the first appropriate response appears near the top among candidate responses.
4. **Recommendation Systems:** Can measure how quickly the first relevant recommendation appears.
5. **Entity Retrieval:** Useful when searching for a specific Person, Company, Product, or Location and one correct result is especially important.
6. **Autocomplete and Suggestion Systems:** Can measure how high the user's intended suggestion appears in the ranked suggestions.

---

## 9. Advantages of MRR

1. **Simple to Calculate:** The formula is straightforward.
2. **Rewards High Rankings:** A correct result at rank 1 receives much more credit than one at rank 10.
3. **Useful for Single-Answer Tasks:** It works especially well when users primarily need one correct answer.
4. **Easy to Compare Systems:** Two retrieval systems can be compared using their MRR scores.

---

## 10. Limitations of MRR

1. **Considers Only the First Relevant Result:** It ignores other relevant documents appearing after the first one.
2. **Not Ideal for Multiple Relevant Results:** If many relevant documents matter, MRR may not represent retrieval quality completely.
3. **Ranking Beyond the First Relevant Result Is Ignored:** For example:
   * System A: relevant results at ranks 1, 2, 3
   * System B: relevant results at ranks 1, 20, 30
   Both have $MRR=1$ because both have the first relevant result at rank 1.
4. **Depends on Relevance Judgments:** Incorrect or incomplete relevance labels can affect the score.

---

## 11. MRR vs Precision and Recall

| Metric | Measures |
| :--- | :--- |
| **Precision** | How many retrieved results are relevant |
| **Recall** | How many relevant results were retrieved |
| **F1** | Balance between precision and recall |
| **MRR** | Position of the first relevant result |

So:
> **Precision/Recall focus on relevance quantity, while MRR focuses on the position of the first relevant result.**

---

## 12. MRR vs Average Precision

This is an important distinction:

* **MRR:** Considers only the **first relevant result**. Best for tasks where one correct answer is important.
* **Average Precision (AP):** Considers the positions of **all relevant results**. Better when multiple relevant documents matter.

---

## 13. Calculation Steps

To calculate MRR:
```text
Step 1 → Take each query
Step 2 → Find the first relevant result
Step 3 → Record its rank
Step 4 → Calculate 1/rank
Step 5 → Average all reciprocal ranks
```

### Formula

$$
\boxed{MRR=\frac{1}{N}\sum_{i=1}^{N}\frac{1}{rank_i}}
$$

---

## 14. Conclusion

**Mean Reciprocal Rank (MRR)** is an Information Retrieval evaluation metric that measures the **average reciprocal position of the first relevant result** across multiple queries.

It is particularly useful for **question answering, search engines, chatbots, recommendation systems, and other tasks where getting one correct result near the top is important**.

### ⭐ Exam keywords
**MRR → First Relevant Result → Reciprocal Rank → $1/rank$ → Average → Ranking Quality → Question Answering → Search Evaluation**

### 🧠 One-line memory trick
> **MRR = “How high does the first correct result appear?”**
