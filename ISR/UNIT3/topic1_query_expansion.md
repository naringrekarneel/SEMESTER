# Query Expansion — 10 Marks

## 1. Definition

**Query Expansion (QE)** is an Information Retrieval technique used to **improve a user's original query by adding related words, synonyms, phrases, or terms** before searching the document collection.

The main goal is to **reduce the mismatch between the words used in the query and the words used in relevant documents**.

### Example

Original query:
> `car accident`

Expanded query:
> `car accident automobile crash collision`

A document containing the word **"automobile"** or **"collision"** may now be retrieved even though the user did not use those terms.

---

## 2. Why Query Expansion is Needed

A major problem in Information Retrieval is the **vocabulary mismatch problem**.
The user and the document may describe the same concept using different words.

For example:

| User Query | Document may contain |
| :--- | :--- |
| **car** | automobile, vehicle |
| **mobile phone** | smartphone, cellphone |
| **heart attack** | myocardial infarction |
| **movie** | film, cinema |

Without expansion, relevant documents may be missed.

---

## 3. Techniques of Query Expansion

### 1. Synonym-Based Expansion
Add **synonyms** of the original query terms.

**Example:**
Original:
> `car`

Expanded:
> `car automobile vehicle`

This helps retrieve documents using different words for the same concept.

### 2. Thesaurus-Based Expansion
A **thesaurus or knowledge base** is used to identify related terms.

**Example:**
> Query: `computer`
> Possible expansion: `computer, PC, processor, computing`

Resources such as WordNet or domain-specific thesauri can be used.

### 3. Relevance Feedback
The system asks the user to identify which retrieved documents are relevant.
The system then analyzes those documents and adds useful terms to the original query.

**Example:**
Original query:
> `machine learning`

After examining relevant documents, the system discovers:
> `machine learning → neural networks, classification, prediction`

The query can then be expanded using these terms.

### 4. Pseudo-Relevance Feedback
This is similar to relevance feedback, but **the user does not explicitly identify relevant documents**.
The system assumes that the **top-ranked retrieved documents are relevant** and extracts important terms from them.

**Example:**
Query:
> `deep learning`

Top documents contain:
> `CNN, neural network, training, backpropagation`

The system adds some of these terms to the query.

### 5. Query Expansion Using User Search History
Previous searches or interactions can be used to understand the user's intent.

**Example:**
User searches:
> `python`

Then searches:
> `python web development`

The system can learn that the user may be interested in programming rather than the animal.

### 6. Ontology-Based Expansion
An **ontology** represents concepts and relationships between concepts.

**Example:**
> `Laptop → Computer → Electronic Device`

If the user searches for:
> `Laptop`

the system may use related concepts such as:
> `computer`, `notebook`, `portable computer`

This is particularly useful in specialized domains such as medicine and engineering.

### 7. Semantic / NLP-Based Expansion
Modern search systems can use **Natural Language Processing and embeddings** to find semantically related terms rather than relying only on exact word matches.

**Example:**
> Query: `ways to protect computers`
> Possible semantic expansion: `cybersecurity, computer security, threat protection, malware prevention`

This helps retrieve documents that express the same idea using different wording.

---

## 4. Advantages of Query Expansion

1. **Improves Recall:** It retrieves more relevant documents that may not contain the exact original query terms.
2. **Handles Vocabulary Mismatch:** Different words can express the same concept.
3. **Improves Search Results:** Relevant documents that were previously missed can be retrieved.
4. **Helps Ambiguous Queries:** Additional terms can provide context to the search system.
5. **Reduces User Effort:** Users do not need to know every possible term related to their information need.
6. **Useful in Specialized Domains:** Medical, legal, scientific, and technical searches often use different terminology for the same concept.

---

## 5. Limitations of Query Expansion

1. **Query Drift:** Adding unrelated terms may move the search away from the user's actual intention.
   * **Example:** `Java` expanded with `island`, `coffee`, and `programming` could retrieve unrelated results.
2. **Reduced Precision:** Adding too many terms can retrieve many irrelevant documents.
   * **Example:** `car automobile vehicle transport` may retrieve documents about public transportation that are not relevant.
3. **Ambiguity:** A word can have multiple meanings.
   * **Example:** `apple` could mean Apple Inc. or the fruit. Incorrect expansion can produce irrelevant results.
4. **Computational Cost:** Finding synonyms, analyzing documents, and generating semantic relationships requires additional processing.
5. **Dependence on Knowledge Resources:** Thesauri and ontologies may be incomplete, outdated, or domain-specific.
6. **Incorrect Expansion Terms:** Automatically generated terms may not accurately represent the user's intention.

---

## 6. Example of Query Expansion

Suppose the user searches:
> **Original Query:** `heart attack treatment`

The system expands it to:
> **Expanded Query:** `heart attack myocardial infarction treatment therapy medication`

The expanded query can retrieve documents containing **"myocardial infarction"** even when they do not use the phrase **"heart attack"**.
However, if unrelated terms are added, the system may retrieve irrelevant medical documents, causing **query drift and lower precision**.

---

## 7. Query Expansion Process

```text
        User Query
            ↓
    Analyze Query Terms
            ↓
   Find Related Terms
   ┌────────┼─────────┐
   ↓        ↓         ↓
Synonyms  Feedback  Semantics
   └────────┼─────────┘
            ↓
     Expanded Query
            ↓
      Search System
            ↓
    Retrieved Documents
```

---

## 8. Conclusion

**Query Expansion improves Information Retrieval by adding related terms to the original query.** Techniques such as **synonym expansion, thesaurus-based expansion, relevance feedback, pseudo-relevance feedback, ontology-based expansion, and semantic/NLP-based expansion** help overcome vocabulary mismatch and improve recall.

However, excessive or incorrect expansion can cause **query drift, lower precision, ambiguity, and additional computational cost**. Therefore, query expansion should add **relevant terms while preserving the original search intent**.
