# Pattern and Structural Queries in Information Retrieval — 10 Marks

## 1. Introduction

In Information Retrieval, users can search for information in different ways.

The most common method is an **ordinary keyword query**, where the user enters a few words and the system finds documents containing those words.

However, sometimes the user wants to search for a **specific pattern** or a **specific structure/relationship** in the documents. These are called **Pattern Queries** and **Structural Queries**.

---

## 2. Pattern Queries

### Definition
A **Pattern Query** searches for documents or terms that **match a specified pattern** rather than requiring an exact keyword match.

Patterns may involve:
* Wildcards
* Prefixes
* Suffixes
* Regular expressions
* Character sequences
* Word patterns

### Example 1 — Wildcard
Suppose the query is:
> `comput*`

It may match:
* computer
* computing
* computation
* computational

The `*` represents any sequence of characters.

### Example 2 — Regular Expression
Query:
> `colou?r`

may match:
* color
* colour

Here, `?` represents an optional character.

### Example 3 — Prefix Search
Query:
> `bio*`

could retrieve:
* biology
* biomedical
* biotechnology
* biochemistry

---

## 3. Types of Pattern Queries

### 1. Wildcard Queries
Use symbols such as `*` and `?` to represent unknown characters.
Example:
> `prog*`

matches terms such as:
> `program`, `programming`, `programmer`

### 2. Regular Expression Queries
Use formal patterns to describe possible matching strings.
Example:
> `comp.*`

can match terms beginning with `comp`.

### 3. Fuzzy Queries
Retrieve terms that are **similar to the query term**, allowing spelling variations or minor errors.
Example:
> `retrival`

may match:
> `retrieval`

This is useful when users make spelling mistakes.

---

## 4. Structural Queries

### Definition
A **Structural Query** searches for information based on the **structure, organization, or relationships between elements** in a document rather than simply matching individual words.

It considers where or how information appears.

Structural queries can use:
* Document fields
* Sections
* Metadata
* HTML/XML tags
* Attributes
* Relationships between terms
* Document hierarchy

---

### Example 1 — Title Search
Suppose a search engine allows:
> `title:"machine learning"`

This searches specifically for documents where **"machine learning" appears in the title**.
This is different from searching for the words anywhere in the document.

---

### Example 2 — Author Search
A structured library database might support:
> `author:"Alan Turing"`

This retrieves documents where the author field is Alan Turing.

---

### Example 3 — Field-Based Search
Consider a product database:
```text
Title: Laptop
Brand: Dell
Price: ₹60,000
Category: Computer
```

A structural query could be:
> `Brand:Dell AND Category:Computer`

The query operates on specific **fields** rather than searching the entire text.

---

### Example 4 — HTML/XML Structure
Consider an HTML document:
```html
<h1>Machine Learning</h1>
<p>Machine learning is a branch of AI.</p>
```

A structural query can specifically search for:
> `<h1>Machine Learning</h1>`

rather than simply searching for the words `machine learning` anywhere in the document.

---

## 5. Pattern Query vs Structural Query

| Feature | Pattern Query | Structural Query |
| :--- | :--- | :--- |
| **Basic idea** | Matches a specified pattern | Matches document structure |
| **Focus** | Words/characters | Fields, positions, relationships |
| **Main purpose** | Find variations of terms | Find information in a specific structural location |
| **Examples** | `comput*`, `colou?r` | `title:AI`, `author:Turing` |
| **Uses wildcards** | Commonly used | Not necessarily |
| **Uses metadata** | Usually not required | Commonly used |
| **Handles word variations**| Very useful | Not its primary purpose |
| **Example** | `prog*` | `title:"Python"` |

---

## 6. Ordinary Keyword Queries

An **ordinary keyword query** simply consists of words representing the user's information need.

### Example
> `machine learning algorithms`

The search engine generally looks for documents containing these terms or related terms and ranks them according to relevance.

The user does **not explicitly specify**:
* Where the term should appear
* What pattern it should follow
* Which field should contain it
* What structural relationship should exist

---

## 7. Difference from Ordinary Keyword Queries

| Aspect | Keyword Query | Pattern Query | Structural Query |
| :--- | :--- | :--- | :--- |
| **Search basis** | Keywords | Character/word patterns | Document structure |
| **Complexity** | Simple | Moderate | More advanced |
| **Example** | `machine learning` | `mach*` | `title:"machine learning"` |
| **Location awareness**| Usually low | Usually low | High |
| **Wildcards** | Usually not required | Common | Optional |
| **Metadata** | Usually ignored | Usually ignored | Can be important |
| **Main advantage** | Easy to use | Finds variations | Precise structured retrieval |
| **Typical use** | General web search | Code/text search | Digital libraries, databases, XML/HTML |

---

## 8. Example Comparing All Three

Suppose we have these documents:
```text
Document 1
Title: Introduction to Machine Learning
Author: John
Content: Machine learning uses algorithms...

Document 2
Title: Deep Learning
Author: Smith
Content: Machine learning and neural networks...

Document 3
Title: Machine Learning Applications
Author: John
Content: Applications of machine learning...
```

### Ordinary Keyword Query
> `machine learning`

May retrieve all three documents because the terms occur in their content or titles.

### Pattern Query
> `machine*`

Can match terms such as:
* machine
* machines
* machining

depending on the indexing system.

### Structural Query
> `author:John AND title:"Machine Learning"`

Specifically searches for documents where:
* Author = John
* Title contains the phrase "Machine Learning"

This provides much more precise retrieval.

---

## 9. Advantages

### Pattern Queries
* Find different forms of words.
* Handle spelling variations.
* Useful for incomplete words.
* Useful for code and technical searches.
* Reduce the need to enter every variation manually.

### Structural Queries
* Provide precise retrieval.
* Search specific fields.
* Use metadata effectively.
* Useful for databases and digital libraries.
* Can exploit relationships between document elements.

---

## 10. Limitations

### Pattern Queries
* Complex patterns can be computationally expensive.
* Broad wildcard queries may produce many results.
* Poorly designed patterns may retrieve irrelevant terms.

### Structural Queries
* Require structured or well-indexed documents.
* More difficult for ordinary users to formulate.
* Different systems may use different query syntax.
* Unstructured documents may provide little structural information.

---

## 11. Conclusion

**Pattern Queries** retrieve information by matching **specific word or character patterns**, such as `comput*` or `colou?r`. **Structural Queries** retrieve information by considering the **structure, fields, metadata, location, or relationships within documents**, such as `title:"AI"` or `author:"Turing"`.

Unlike ordinary keyword queries, which mainly search for **terms representing the user's information need**, pattern and structural queries provide **more specialized and precise control over retrieval**.

### ⭐ Exam keywords
**Pattern Query → Wildcard → Regular Expression → Fuzzy Matching → Word Variations**

**Structural Query → Fields → Metadata → Document Structure → Relationships → Precise Retrieval**

**Keyword Query → Simple Terms → General Search → No Explicit Structure**
