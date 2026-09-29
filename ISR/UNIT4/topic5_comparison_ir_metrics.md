# Comparison of IR Evaluation Metrics — 10 Marks

Information Retrieval (IR) systems are evaluated using different metrics because **no single metric captures every aspect of search quality**. The main metrics are **Precision, Recall, F-measure, MRR, MAP, and NDCG**.

---

## 1. Precision

### Meaning
**Precision** measures how many of the retrieved documents are actually relevant.
> **Question answered:** “Of what I retrieved, how much was relevant?”

### Formula
$$
Precision = \frac{TP}{TP+FP}
$$

### Appropriate when
Precision is important when **irrelevant results are costly or undesirable**.

### Example applications
* Web search
* Product search
* Search results where users want highly specific results

---

## 2. Recall

### Meaning
**Recall** measures how many of all relevant documents were successfully retrieved.
> **Question answered:** “Of everything relevant, how much did I find?”

### Formula
$$
Recall = \frac{TP}{TP+FN}
$$

### Appropriate when
Recall is important when **missing relevant information is costly**.

### Example applications
* Legal document search
* Medical literature search
* Academic/research databases
* E-discovery

---

## 3. F-Measure / F1-Score

### Meaning
**F-measure** combines Precision and Recall into a single metric.
The most commonly used version is **F1-score**, which gives equal importance to both.

### Formula
$$
F_1=\frac{2PR}{P+R}
$$
where:
* $P$ = Precision
* $R$ = Recall

### Appropriate when
Use F1 when you need a **balance between Precision and Recall**.

### Example applications
* General IR evaluation
* Classification-like retrieval tasks
* Situations where both false positives and false negatives matter

---

## 4. Mean Reciprocal Rank (MRR)

### Meaning
MRR measures how high the **first relevant result** appears in the ranking.

For one query:
$$
RR=\frac{1}{rank}
$$

For multiple queries:
$$
MRR=\frac{1}{Q}\sum_{i=1}^{Q}\frac{1}{rank_i}
$$

### Appropriate when
MRR is best when the user mainly needs **one correct result or answer**.

### Example applications
* Question Answering
* Search assistants
* Entity lookup
* Autocomplete
* Tasks where the first correct result matters most

### Example
If the first relevant result is:
* Rank 1 → RR = 1
* Rank 2 → RR = 0.5
* Rank 5 → RR = 0.2

So MRR strongly rewards putting the first correct result near the top.

---

## 5. Mean Average Precision (MAP)

### Meaning
MAP measures the **ranking quality of multiple relevant documents across multiple queries**.

First calculate Average Precision (AP) for each query, then average them.
$$
MAP=\frac{1}{Q}\sum_{i=1}^{Q}AP_i
$$

### Appropriate when
MAP is useful when:
* There are **multiple relevant documents**
* Their positions in the ranking matter
* You want to evaluate performance across many queries

### Example applications
* Document retrieval
* Academic search
* Web search evaluation
* Text retrieval collections

---

## 6. NDCG

### Meaning
**NDCG (Normalized Discounted Cumulative Gain)** evaluates the quality of a ranked list when documents have **different degrees of relevance**.

For example:
* 3 = Highly relevant
* 2 = Relevant
* 1 = Slightly relevant
* 0 = Not relevant

### Formula
A common DCG formulation is:
$$
DCG@k=\sum_{i=1}^{k}\frac{2^{rel_i}-1}{\log_2(i+1)}
$$

Then:
$$
NDCG@k=\frac{DCG@k}{IDCG@k}
$$
where IDCG is the DCG of the ideal ranking.

### Appropriate when
NDCG is especially useful when:
* Ranking position matters
* Relevance is **graded**, not just yes/no
* Highly relevant results should appear above moderately relevant ones

### Example applications
* Web search
* Recommendation systems
* E-commerce ranking
* Personalized search

---

## 7. Overall Comparison

| Metric | Main Question | Ranking Position? | Graded Relevance? | Best Used For |
| :--- | :--- | :--- | :--- | :--- |
| **Precision** | How many retrieved results are relevant? | No | No | Specific, focused retrieval |
| **Recall** | How many relevant results were found? | No | No | Comprehensive retrieval |
| **F1** | How well are Precision and Recall balanced? | No | No | Balanced evaluation |
| **MRR** | How high is the first relevant result? | **Yes** | No | Single-answer/QA tasks |
| **MAP** | How well are multiple relevant results ranked? | **Yes** | Usually binary relevance | Multiple relevant documents |
| **NDCG** | How well are graded relevant results ranked? | **Yes** | **Yes** | Ranked search/recommendation |

---

## 8. Simple Example to Understand the Difference

Suppose a search system returns:
```text
Rank 1 → Highly relevant
Rank 2 → Non-relevant
Rank 3 → Relevant
Rank 4 → Slightly relevant
Rank 5 → Non-relevant
```

Different metrics look at this list differently.

* **Precision:** Looks at: > How many of the retrieved documents are relevant?
It does not inherently care whether the relevant document is at rank 1 or rank 5.
* **Recall:** Looks at: > How many of all relevant documents in the collection were retrieved?
* **F1:** Balances Precision and Recall.
* **MRR:** Looks primarily at: > Where is the **first relevant** document?
Here it is at rank 1, so $RR=1$.
* **MAP:** Looks at the positions of **all relevant documents** and rewards systems that place them higher.
* **NDCG:** Considers both **Position** and **Degree of relevance**.
So a highly relevant document at rank 1 gets more importance than a slightly relevant document at rank 4.

---

## 9. When Should Each Metric Be Used?

* **Precision:** Use when **result accuracy** matters most.
> Example: A user searches for a very specific technical topic and does not want irrelevant pages.
* **Recall:** Use when **missing relevant documents** is a major concern.
> Example: Legal research where potentially relevant documents should not be missed.
* **F1:** Use when you need a **single score balancing Precision and Recall**.
> Example: General retrieval evaluation where both irrelevant results and missed results matter.
* **MRR:** Use when **one correct answer/result** is the primary goal.
> Example: “Who is the CEO of X?” in a QA system.
* **MAP:** Use when there are **multiple relevant documents** and their ranking matters.
> Example: Searching a collection of research papers for a topic.
* **NDCG:** Use when relevance is **graded** and ranking quality matters.
> Example: Search results where some documents are highly relevant, some moderately relevant, and others only slightly relevant.

---

## 10. Key Differences

* **Precision vs Recall**
  * **Precision** = Quality of retrieved results
  * **Recall** = Completeness of retrieval
* **F1 vs Precision/Recall**
  * **F1** = Balance between Precision and Recall
* **MRR vs MAP**
  * **MRR** = First relevant result
  * **MAP** = All relevant results
* **MAP vs NDCG**
  * **MAP** = Multiple relevant results, usually binary relevance
  * **NDCG** = Graded relevance + ranking position

---

## 11. Easy Decision Table

| Situation | Suitable Metric |
| :--- | :--- |
| Want fewer irrelevant results | **Precision** |
| Want to find as many relevant documents as possible | **Recall** |
| Want balance between Precision and Recall | **F1** |
| Need one correct answer quickly | **MRR** |
| Need multiple relevant documents ranked well | **MAP** |
| Need graded relevance and ranking quality | **NDCG** |

---

## 12. Conclusion

The choice of IR evaluation metric depends on **what the search system is expected to do**.
* **Precision** measures retrieval accuracy.
* **Recall** measures retrieval completeness.
* **F1** balances Precision and Recall.
* **MRR** focuses on the first relevant result.
* **MAP** evaluates the ranking of multiple relevant results across queries.
* **NDCG** evaluates ranking quality when relevance has different degrees.

Therefore, a good IR evaluation strategy selects the metric that matches the **user's information need and the behavior expected from the search system**.

### 🧠 Super-easy memory trick
> **Precision → Relevant among Retrieved**
> **Recall → Retrieved among Relevant**
> **F1 → Balance**
> **MRR → First relevant**
> **MAP → All relevant**
> **NDCG → Graded relevance + rank**
