# Relevance Feedback and Rocchio Algorithm — 10 Marks

## 1. What is Relevance Feedback?

**Relevance Feedback (RF)** is an Information Retrieval technique in which the **user's feedback about the retrieved documents is used to modify and improve the original query**.

The basic idea is:
> **Search → Get results → Identify relevant/non-relevant documents → Modify query → Search again**

It helps the system understand the user's actual information need and retrieve more relevant documents.

### Example
Suppose the user searches:
> `machine learning`

The system retrieves 10 documents. The user marks:
* 3 documents as **relevant**
* 2 documents as **non-relevant**

The system analyzes these documents and identifies useful terms such as:
> `neural networks`, `classification`, `training`

It then modifies the query using these terms and performs another search.

---

## 2. Types of Relevance Feedback

### 1. Explicit Relevance Feedback
The user directly tells the system which documents are relevant.
Example:
> 👍 Relevant
> 👎 Not Relevant

This provides accurate feedback but requires additional user effort.

### 2. Implicit Relevance Feedback
The system infers relevance from user behavior.
For example:
* Clicking a result
* Spending more time on a page
* Saving a document
* Downloading a document

### 3. Pseudo-Relevance Feedback
The system assumes that the **top-ranked documents are relevant** and uses them to improve the query without asking the user.

---

## 3. Rocchio Algorithm

The **Rocchio algorithm** is a classic relevance-feedback algorithm used with the **Vector Space Model**.

It modifies the query vector by:
* Moving it **towards relevant documents**
* Moving it **away from non-relevant documents**

### Rocchio Formula

$$
\vec{q}_{new} = \alpha \vec{q}_{old} + \frac{\beta}{|D_r|} \sum_{\vec{d_j}\in D_r}\vec{d_j} - \frac{\gamma}{|D_{nr}|} \sum_{\vec{d_j}\in D_{nr}}\vec{d_j}
$$

Where:
* $\vec{q}_{new}$ = new/updated query vector
* $\vec{q}_{old}$ = original query vector
* $D_r$ = set of relevant documents
* $D_{nr}$ = set of non-relevant documents
* $\alpha$ = importance given to original query
* $\beta$ = importance given to relevant documents
* $\gamma$ = importance given to non-relevant documents

---

## 4. Working of Rocchio Algorithm

The Rocchio algorithm works in the following steps:

### Step 1: Submit Original Query
The user enters a query.
Example:
> `information retrieval`

The system converts it into a vector.

### Step 2: Retrieve Documents
The search system retrieves documents based on similarity with the query.

### Step 3: Collect Feedback
The user marks documents as:
* Relevant
* Non-relevant

### Step 4: Calculate Relevant Document Centroid
The system calculates the average vector of relevant documents.

### Step 5: Calculate Non-Relevant Document Centroid
The system calculates the average vector of non-relevant documents.

### Step 6: Modify the Query
The algorithm:
* Keeps part of the original query.
* Adds characteristics of relevant documents.
* Removes or reduces characteristics associated with non-relevant documents.

### Step 7: Perform Search Again
The updated query is used to retrieve documents again.

---

## 5. Simple Example

Suppose the original query is:
> `python programming`

After the first search, the user identifies some relevant documents containing:
> `Python, programming, scripting, automation`

Non-relevant documents contain:
> `snake, reptile`

The Rocchio algorithm moves the query vector toward the terms found in relevant documents and away from terms found in non-relevant documents.

Therefore, the updated query becomes more focused on:
> `Python programming scripting automation`

rather than:
> `Python snake reptile`

This improves the quality of subsequent results.

---

## 6. How Relevance Feedback Improves Search Results

1. **Improves Precision:** It helps the system identify what the user considers relevant and reduces irrelevant results.
2. **Improves Recall:** Important terms found in relevant documents can be added to the query, allowing more relevant documents to be retrieved.
3. **Resolves Vocabulary Mismatch:** The user may use one term while relevant documents use another. Example: `car` → `automobile`, `vehicle`. Feedback helps discover these relationships.
4. **Understands User Intent:** The same query can have different meanings. Example: `Java` (programming language, island, coffee). Feedback helps identify the intended meaning.
5. **Reduces Irrelevant Results:** Terms associated with non-relevant documents can be given less importance.
6. **Provides Personalized Search:** The results can adapt according to the user's information need.

---

## 7. Advantages of Rocchio Algorithm

| Advantage | Explanation |
| :--- | :--- |
| **Simple** | Easy to implement using vector operations |
| **Effective** | Can improve retrieval quality |
| **Automatic updating** | Query is modified systematically |
| **Handles relevance information** | Uses both relevant and non-relevant documents |
| **Works with Vector Space Model** | Uses document-query similarity |

---

## 8. Limitations

1. **Requires User Feedback:** Explicit relevance feedback requires users to spend additional effort.
2. **Query Drift:** If incorrect or poorly chosen documents are marked relevant, the query can move away from the user's original intention.
3. **Not Ideal for Short Queries:** A query containing very few terms may not provide enough information for meaningful expansion.
4. **Assumes Vector Representation:** Traditional Rocchio works within the Vector Space Model and depends on suitable term-weight representations.
5. **Quality Depends on Feedback:** Incorrect feedback can result in poor search results.

---

## 9. Diagram

```text
             Original Query
                   ↓
             Search Engine
                   ↓
             Initial Results
                   ↓
          ┌────────┴────────┐
          ↓                 ↓
    Relevant Docs      Non-Relevant Docs
          ↓                 ↓
          └────────┬────────┘
                   ↓
           Rocchio Algorithm
                   ↓
          Updated Query Vector
                   ↓
             Search Again
                   ↓
          Improved Results
```

---

## 10. Conclusion

**Relevance Feedback** improves Information Retrieval by using information about which retrieved documents are relevant or non-relevant to modify the original query.

The **Rocchio algorithm** is a widely used relevance-feedback method that **moves the query vector toward relevant documents and away from non-relevant documents**. This can improve **precision, recall, vocabulary matching, and user-intent understanding**, although incorrect feedback can cause **query drift**.

### ⭐ Exam keywords to remember
**Relevance Feedback → Relevant documents → Non-relevant documents → Vector Space Model → Rocchio → Query modification → Precision + Recall → Query drift**
