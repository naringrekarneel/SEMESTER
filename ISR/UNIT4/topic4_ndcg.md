# NDCG (Normalized Discounted Cumulative Gain) — 10 Marks

## 1. Definition

**NDCG (Normalized Discounted Cumulative Gain)** is an Information Retrieval evaluation metric used to measure the **quality of a ranked list of search results**.

NDCG is especially useful when documents can have **different degrees of relevance**, rather than simply being relevant or non-relevant.

For example, search results may be rated:
* **3** → Highly relevant
* **2** → Relevant
* **1** → Slightly relevant
* **0** → Not relevant

The main idea is:
> **Highly relevant documents should appear near the top of the ranking.**

NDCG gives higher importance to relevant documents appearing at earlier ranks and gradually **discounts** the value of documents appearing lower down.

---

## 2. Why NDCG is Used

Suppose two search systems retrieve the same relevant documents.

### System A
```text
Rank 1 → Highly relevant
Rank 2 → Relevant
Rank 3 → Slightly relevant
```

### System B
```text
Rank 1 → Slightly relevant
Rank 2 → Relevant
Rank 3 → Highly relevant
```

Both contain the same documents, but **System A has a better ranking** because the highly relevant document appears first.

NDCG captures this difference.

---

## 3. Components of NDCG

NDCG has three important concepts:
1. **DCG** — Discounted Cumulative Gain
2. **IDCG** — Ideal Discounted Cumulative Gain
3. **NDCG** — Normalized Discounted Cumulative Gain

---

## 4. DCG — Discounted Cumulative Gain

**DCG** measures the usefulness or relevance of documents in their current ranking.

The relevance score of a document is called its **gain**.

A common DCG formula is:

$$
DCG@k = rel_1 + \sum_{i=2}^{k}\frac{rel_i}{\log_2(i)}
$$

where:
* $k$ = number of top results considered
* $rel_i$ = relevance score of the document at rank $i$

An alternative commonly used formulation is:

$$
DCG@k = \sum_{i=1}^{k}\frac{2^{rel_i}-1}{\log_2(i+1)}
$$

The second formulation gives more emphasis to highly relevant documents.

---

## 5. Why Discounting is Used

A document appearing at **rank 1** is generally more valuable than the same document appearing at **rank 10**.

Therefore, DCG applies a discount as the rank increases.
```text
Rank 1 → Full value
Rank 2 → Slightly discounted
Rank 3 → More discounted
Rank 4 → More discounted
...
```

Thus:
> **Higher-ranked relevant documents contribute more to DCG.**

---

## 6. IDCG — Ideal Discounted Cumulative Gain

**IDCG** is the DCG of the **ideal ranking**, where documents are arranged from the most relevant to the least relevant.

In other words:
> **IDCG represents the best possible ranking for the given set of documents.**

The relevance scores are sorted in descending order before calculating DCG.

---

## 7. NDCG — Normalized Discounted Cumulative Gain

NDCG normalizes DCG using the ideal ranking.

### Formula

$$
NDCG@k = \frac{DCG@k}{IDCG@k}
$$

This makes comparison easier because the score is usually between:
$$
0 \leq NDCG \leq 1
$$

A score closer to **1** means the ranking is closer to the ideal ranking.

---

## 8. Suitable Example

Suppose a search engine returns **5 documents** with the following relevance scores:

| Rank | Document | Relevance |
| ---: | :--- | ---: |
| 1 | D1 | 3 |
| 2 | D2 | 2 |
| 3 | D3 | 3 |
| 4 | D4 | 0 |
| 5 | D5 | 1 |

We will calculate **NDCG@5** using the common gain formula:

$$
DCG@k = \sum_{i=1}^{k}\frac{2^{rel_i}-1}{\log_2(i+1)}
$$

---

## 9. Step 1 — Calculate DCG

The relevance scores are:
$$
[3,2,3,0,1]
$$

#### Rank 1
$$
\frac{2^3-1}{\log_2(2)} = \frac{7}{1} = 7
$$

#### Rank 2
$$
\frac{2^2-1}{\log_2(3)} = \frac{3}{1.585} \approx 1.893
$$

#### Rank 3
$$
\frac{2^3-1}{\log_2(4)} = \frac{7}{2} = 3.5
$$

#### Rank 4
$$
\frac{2^0-1}{\log_2(5)} = 0
$$

#### Rank 5
$$
\frac{2^1-1}{\log_2(6)} = \frac{1}{2.585} \approx 0.387
$$

Therefore:
$$
DCG@5 = 7+1.893+3.5+0+0.387
$$
$$
\boxed{DCG@5 \approx 12.78}
$$

---

## 10. Step 2 — Calculate IDCG

Now arrange the relevance scores in the **ideal descending order**:
$$
[3,3,2,1,0]
$$

Calculate DCG again.

#### Rank 1
$$
\frac{2^3-1}{\log_2(2)}=7
$$

#### Rank 2
$$
\frac{2^3-1}{\log_2(3)} = \frac{7}{1.585} \approx 4.417
$$

#### Rank 3
$$
\frac{2^2-1}{\log_2(4)} = \frac{3}{2} = 1.5
$$

#### Rank 4
$$
\frac{2^1-1}{\log_2(5)} = \frac{1}{2.322} \approx 0.431
$$

#### Rank 5
$$
\frac{2^0-1}{\log_2(6)} = 0
$$

Therefore:
$$
IDCG@5 = 7+4.417+1.5+0.431
$$
$$
\boxed{IDCG@5 \approx 13.35}
$$

---

## 11. Step 3 — Calculate NDCG

Now:
$$
NDCG@5 = \frac{DCG@5}{IDCG@5}
$$

Substitute the values:
$$
NDCG@5 = \frac{12.78}{13.35}
$$
$$
\boxed{NDCG@5 \approx 0.957}
$$

Therefore:
$$
\boxed{NDCG@5 \approx 95.7\%}
$$

This means the ranking is **close to the ideal ranking** according to the chosen relevance judgments.

---

## 12. Easy Understanding of DCG, IDCG and NDCG

Think of a classroom ranking:

* **DCG:** > **How good is the ranking we actually produced?**
* **IDCG:** > **How good would the ranking be if everything were arranged perfectly?**
* **NDCG:** > **How close is our actual ranking to the perfect ranking?**

So:
$$
\boxed{NDCG=\frac{\text{Actual Ranking Quality}}{\text{Ideal Ranking Quality}}}
$$

---

## 13. Interpretation of NDCG

| NDCG | Interpretation |
| ---: | :--- |
| **1.0** | Perfect/ideal ranking |
| **Close to 1** | Very good ranking |
| **Around 0.5** | Moderate ranking quality |
| **Close to 0** | Poor ranking |

The exact interpretation depends on the dataset and evaluation setup; NDCG is primarily useful for **comparing ranking systems under the same evaluation conditions**.

---

## 14. Advantages of NDCG

1. **Considers Ranking Position:** Relevant documents appearing at higher ranks receive more value.
2. **Supports Graded Relevance:** It can distinguish between Highly relevant, Moderately relevant, Slightly relevant, Non-relevant.
3. **Useful for Ranking Evaluation:** It evaluates the quality of the entire ranked list rather than just whether a document was retrieved.
4. **Normalized Score:** Because it uses IDCG, results can be normalized and compared more easily across queries with different relevance distributions.

---

## 15. Limitations of NDCG

1. **Requires Relevance Judgments:** The system needs relevance scores for documents.
2. **Requires Graded Relevance:** Its major advantage comes from having meaningful relevance levels.
3. **Different Evaluation Choices Can Affect Results:** Different gain and discount formulations can produce different numerical values.
4. **Does Not Explain Why a Result Is Relevant:** NDCG evaluates ranking quality but does not itself provide explanations for the ranking.

---

## 16. NDCG vs Other IR Metrics

| Metric | Main Focus |
| :--- | :--- |
| **Precision** | How many retrieved results are relevant |
| **Recall** | How many relevant results were retrieved |
| **MRR** | Position of the first relevant result |
| **MAP** | Ranking of multiple relevant documents |
| **NDCG** | Ranking quality with **graded relevance** |

### Important distinction
> **MRR → first relevant result**
> **MAP → all relevant results**
> **NDCG → graded relevance + ranking position**

---

## 17. Complete Formula Summary

### DCG
$$
DCG@k = \sum_{i=1}^{k}\frac{2^{rel_i}-1}{\log_2(i+1)}
$$

### IDCG
$$
IDCG@k = \text{DCG of the ideal ranking}
$$

### NDCG
$$
\boxed{NDCG@k=\frac{DCG@k}{IDCG@k}}
$$

---

## 18. Conclusion

**NDCG (Normalized Discounted Cumulative Gain)** is a powerful Information Retrieval evaluation metric used to measure the **quality of ranked search results when documents have different levels of relevance**.

It first calculates **DCG**, which rewards highly relevant documents appearing near the top. Then it calculates **IDCG**, the maximum possible DCG for an ideal ranking. Finally, it normalizes the result:
$$
NDCG=\frac{DCG}{IDCG}
$$

Thus, **NDCG rewards search systems that place highly relevant documents near the top of the ranking**.

### 🧠 One-line memory trick
> **DCG = actual ranking, IDCG = ideal ranking, NDCG = actual ÷ ideal.**
