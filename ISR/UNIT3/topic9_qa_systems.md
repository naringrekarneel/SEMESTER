# Natural Question Answering (QA) Systems — 10 Marks

## 1. Definition

A **Natural Question Answering (QA) System** is an Information Retrieval system that allows users to ask questions in **natural language** and provides a **direct answer** rather than only returning a list of documents.

### Example

**User:**
> Who invented the telephone?

**QA System:**
> Alexander Graham Bell is commonly credited with inventing the telephone.

A traditional search engine would typically return several webpages related to the question, while a QA system attempts to **identify the answer directly**.

---

## 2. Need for QA Systems

Traditional search engines often require users to:
* Enter keywords
* Examine multiple results
* Open documents
* Find the required information themselves

QA systems reduce this effort by understanding the **question, finding relevant information, and extracting or generating an answer**.

---

## 3. Architecture of a Natural QA System

The basic architecture is:

```text
              User Question
                    ↓
          Question Processing
                    ↓
          Question Classification
                    ↓
         Query Reformulation
                    ↓
          Information Retrieval
                    ↓
       Candidate Document Retrieval
                    ↓
            Answer Extraction
                    ↓
             Answer Ranking
                    ↓
           Final Answer
```

---

## 4. Components of QA Architecture

### 1. Question Input
The user enters a question using natural language.

Example:
> "When was the Internet invented?"

The system receives the complete natural-language question.

---

### 2. Question Processing
The system analyzes the question using **Natural Language Processing (NLP)** techniques.

It identifies:
* Important words
* Grammatical structure
* Entities
* Relationships
* User intent

For example:
> "Who developed the Python programming language?"

The system identifies:
* **Question type:** Who
* **Entity:** Python
* **Expected answer:** Person

---

### 3. Question Classification
The system determines **what type of answer is expected**.

Examples:

| Question | Expected Answer |
| :--- | :--- |
| **Who...?** | Person |
| **Where...?** | Location |
| **When...?** | Date/Time |
| **What...?** | Entity/Concept |
| **How many...?** | Number |
| **Why...?** | Explanation |

Example:
> "When was India founded?"

The system knows that the expected answer should be a **date/year**.

---

### 4. Query Reformulation
The natural-language question is transformed into one or more search queries suitable for the retrieval system.

Example:
Question:
> "Who invented the telephone?"

Possible search query:
> `telephone inventor`

This helps retrieve relevant documents.

---

## 5. Information Retrieval

The system searches a collection of:
* Web documents
* Databases
* Knowledge bases
* Encyclopedias
* Structured/unstructured text

It retrieves potentially relevant documents or passages.

Example:
```text
Question
   ↓
Search Index
   ↓
Relevant Documents
D1, D4, D7
```

---

## 6. Candidate Answer Extraction

The system examines the retrieved documents and identifies possible answers.

For example:

**Document:**
> "Alexander Graham Bell was awarded the first U.S. patent for the telephone in 1876."

For the question:
> "Who invented the telephone?"

The candidate answer is:
> **Alexander Graham Bell**

---

## 7. Answer Ranking

There may be several candidate answers.

The system ranks them based on factors such as:
* Relevance to the question
* Semantic similarity
* Evidence from retrieved documents
* Confidence score
* Position/context within the document

The highest-confidence candidate is selected.

---

## 8. Answer Generation

Finally, the system presents the answer in a natural form.

Example:

**Question:**
> What is the capital of France?

**Answer:**
> Paris is the capital of France.

Modern QA systems may generate an answer using language-generation techniques, while other systems may extract an exact answer span from a source.

---

## 9. Example of Complete QA Process

Suppose the user asks:
> **"Who wrote the Harry Potter series?"**

**Step 1 — Question Processing**
Identify:
* Type → **Who**
* Topic → **Harry Potter series**
* Expected answer → **Person**

**Step 2 — Query Reformulation**
> `Harry Potter author writer`

**Step 3 — Retrieval**
Retrieve relevant webpages or documents.

**Step 4 — Candidate Extraction**
Possible candidate:
> J. K. Rowling

**Step 5 — Ranking**
The system determines that **J. K. Rowling** is strongly supported.

**Step 6 — Final Answer**
> **J. K. Rowling wrote the Harry Potter series.**

---

## 10. QA System vs Traditional Search Engine

| Feature | QA System | Traditional Search Engine |
| :--- | :--- | :--- |
| **Input** | Natural-language question | Usually keywords/queries |
| **Main goal** | Provide a direct answer | Retrieve relevant documents |
| **Output** | Answer, passage, or explanation | Ranked list of results |
| **Question understanding**| High | Usually limited |
| **Answer extraction** | Yes | Usually left to user |
| **User effort** | Lower | Higher |
| **Context understanding** | Often supported | Generally more limited |
| **Example** | "Who wrote Hamlet?" → Shakespeare | Results about Shakespeare and Hamlet |

---

## 11. Traditional Search Example

User enters:
> `Who discovered gravity?`

A traditional search engine may return:
```text
1. Wikipedia
2. Britannica
3. NASA article
4. Educational website
```
The user must open the results and determine the answer.

---

## 12. QA System Example

The same question:
> `Who discovered gravity?`

A QA system attempts to return:
> **Isaac Newton is commonly credited with formulating the law of universal gravitation.**

Thus, the QA system performs an additional **answer-finding step**.

---

## 13. Advantages of QA Systems

1. **Direct Answers:** Users can get the required information without opening multiple documents.
2. **Natural Interaction:** Questions can be asked in normal human language.
3. **Reduced Search Effort:** The system performs answer extraction automatically.
4. **Better for Fact-Based Queries:** Questions such as **who, what, when, where, and how many** can be answered efficiently.
5. **Improved User Experience:** The interaction is closer to a human question-and-answer conversation.

---

## 14. Limitations of QA Systems

1. **Ambiguous Questions:** Questions may have multiple possible interpretations.
2. **Incorrect Retrieval:** If the system retrieves poor documents, the final answer may also be incorrect.
3. **Complex Questions:** Questions requiring reasoning across multiple documents can be difficult.
4. **Knowledge Limitations:** The system depends on the quality and coverage of its information sources.
5. **Generated Answer Errors:** Modern generative QA systems may produce answers that sound convincing but are not adequately supported by evidence.

---

## 15. QA System Architecture Diagram

```text
             Natural Language Question
                       ↓
                Question Analysis
                       ↓
              Question Classification
                       ↓
                Query Reformulation
                       ↓
              Information Retrieval
                       ↓
             Candidate Documents
                       ↓
             Answer Extraction
                       ↓
                Answer Ranking
                       ↓
               Final Answer
                       ↓
                     User
```

---

## 16. Conclusion

A **Natural Question Answering System** enables users to ask questions in natural language and receive a **direct answer**. Its architecture generally consists of **question processing, question classification, query reformulation, information retrieval, candidate answer extraction, answer ranking, and answer generation**.

The major difference from a traditional search engine is:
> **Traditional Search = Find relevant documents.**
> **QA System = Find the information and provide the answer.**

Thus, QA systems reduce the user's effort by moving from **document retrieval** toward **direct information access**.

### ⭐ Exam keywords
**QA → Natural Language → Question Processing → Question Classification → Query Reformulation → Information Retrieval → Candidate Answer → Answer Extraction → Ranking → Final Answer**

### 🧠 One-line memory trick
> **Search Engine finds documents; QA System finds the answer.**
